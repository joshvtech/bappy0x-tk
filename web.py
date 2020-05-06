from flask import Flask, render_template, Blueprint

from static.db.models import db, notifications

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///static/db/db.sqlite3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    """@app.errorhandler(403)
    def invalid(error):
        return render_template("pages/error.html", code=403, flask_error=error), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template("pages/error.html", code=404, flask_error=error), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("pages/error.html", code=500, flask_error=error), 500"""

    main = Blueprint("main", __name__)
    @main.route("/")
    def index():
        return render_template("pages/index.html", carousel=True, nav_active="home", notifications=notifications.render())
    @main.route("/my-specialties")
    def my_specialties():
        return render_template("pages/my-specialties.html", carousel=False, nav_active="my-specialties", notifications=notifications.render())
    @main.route("/contact")
    def contact():
        return render_template("pages/placeholder.html", carousel=False, nav_active="contact", notifications=notifications.render())
    app.register_blueprint(main)

    from views import links
    app.register_blueprint(links)

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=80, debug=True)