from flask import Flask, render_template, Blueprint, redirect, send_from_directory, url_for, abort

from sqlalchemy.orm.exc import NoResultFound

from flask_dance.contrib.github import make_github_blueprint, github#, make_google_blueprint, google
from flask_login import current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized

from os.path import join

from dotenv import load_dotenv
load_dotenv(override=True)
from os import getenv

from public.db.models import *

def create_app():
    #NOTE: STANDARD STUFF
    app = Flask(__name__)

    app.static_url_path = "/public"
    app.static_folder = join(app.root_path, "public")

    app.config["SECRET_KEY"] = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager = LoginManager(app)

    from views.file_hoster import file_hoster as file_blueprint
    app.register_blueprint(file_blueprint, url_prefix="/file-hoster")

    from views.news_bot import news_bot as news_blueprint
    app.register_blueprint(news_blueprint, url_prefix="/news-bot")

    from views.url_shortener import url_shortener as url_blueprint
    app.register_blueprint(url_blueprint, url_prefix="/url-shortener")

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(join(app.static_folder, "img"), "favicon.ico")

    #NOTE: ERRORS
    @app.errorhandler(403)
    def invalid(error):
        return render_template("pages/error.html", code=403, flask_error=error), 403
    @app.errorhandler(404)
    def not_found(error):
        return render_template("pages/error.html", code=404, flask_error=error), 404
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("pages/error.html", code=500, flask_error=error), 500

    #NOTE: LOGIN MANAGEMENT
    @login_manager.user_loader
    def load_user(user_id):
        return users.query.get(int(user_id))

    @app.route("/log-out")
    @login_required
    def log_out():
        logout_user()
        return redirect(url_for("index"))

    #NOTE: GITHUB LOGIN
    github_blueprint = make_github_blueprint(
        client_id=getenv("GITHUB_CLIENT_ID"),
        client_secret=getenv("GITHUB_SECRET"),
        authorized_url="/github/authorised"
    )
    app.register_blueprint(github_blueprint, url_prefix="/login")

    github_blueprint.storage = SQLAlchemyStorage(OAuth, db.session, user=current_user, user_required=False)

    @oauth_authorized.connect_via(github_blueprint)
    def github_logged_in(blueprint, token):
        info = blueprint.session.get("/user")
        if info.ok:
            username = info.json()['login']
            query = users.query.filter_by(username=username)
            try:
                user = query.one()
            except NoResultFound:
                user = users(username=username)
                db.session.add(user)
                db.session.commit()
            login_user(user)

    @app.route("/github_login")
    def github_login():
        if not github.authorized:
            return redirect(url_for("github.login"))
        info = github.get("/user")
        if info.ok:
            return f"<h1>You are @{info.json()['login']} on GitHub</h1>"
        return "<h1>Request failed</h1>", 500

    #NOTE: STANDARD ROUTES
    @app.route("/")
    def index():
        return render_template("pages/index.html", carousel=True, nav_active="home", notifications=notifications.render())
    @app.route("/my-proficiencies")
    def my_proficiencies():
        return render_template("pages/my-proficiencies.html", carousel=False, nav_active="my-proficiencies", notifications=notifications.render())
    @app.route("/contact")
    def contact():
        return render_template("pages/placeholder.html", carousel=False, nav_active="contact", notifications=notifications.render())

    #NOTE: REDIRECTS
    @app.route("/links/<name>")
    def redirect_links(name):
        found = links.query.filter_by(name=name.lower()).first()
        return redirect(found.url, code=301) if found else abort(404)
    @app.route("/videos/<name>")
    def redirect_videos(name):
        found = videos.query.filter_by(name=name.lower()).first()
        return redirect(found.url, code=301) if found else abort(404)

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=80, debug=True)