from flask import Flask, render_template, Blueprint, redirect, send_from_directory
from os.path import join

from static.db.models import db, links, videos, notifications

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///static/db/db.sqlite3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(join(app.root_path, "static/img"), "favicon.ico")

    @app.errorhandler(403)
    def invalid(error):
        return render_template("pages/error.html", code=403, flask_error=error), 403
    @app.errorhandler(404)
    def not_found(error):
        return render_template("pages/error.html", code=404, flask_error=error), 404
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("pages/error.html", code=500, flask_error=error), 500

    @app.route("/")
    def index():
        return render_template("pages/index.html", carousel=True, nav_active="home", notifications=notifications.render())
    @app.route("/my-specialties")
    def my_specialties():
        return render_template("pages/my-specialties.html", carousel=False, nav_active="my-specialties", notifications=notifications.render())
    @app.route("/contact")
    def contact():
        return render_template("pages/placeholder.html", carousel=False, nav_active="contact", notifications=notifications.render())

    @app.route("/links/<name>")
    def redirect_links(name):
        found = links.query.filter_by(name=name.lower()).first()
        return redirect(found.url, code=301) if found else (render_template("pages/error.html", code=500, flask_error="404 Not Found: That redirect couldn't be found!"), 500)
    @app.route("/videos/<name>")
    def redirect_videos(name):
        found = videos.query.filter_by(name=name.lower()).first()
        return redirect(found.url, code=301) if found else (render_template("pages/error.html", code=500, flask_error="404 Not Found: That redirect couldn't be found!"), 500)

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=80, debug=True)