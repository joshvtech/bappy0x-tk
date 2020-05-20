from flask import Blueprint, render_template

from sys import path
path.append("...")
from public.db.models import notifications

folderpath = "pages/projects/url-shortener/"

url_shortener = Blueprint("url-shortener", __name__)
@url_shortener.route("/")
def index():
    return render_template("pages/placeholder.html", carousel=False, nav_active="", notifications=notifications.render())

