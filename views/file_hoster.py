from flask import Blueprint, render_template

from sys import path
path.append("...")
from public.db.models import notifications

folderpath = "pages/projects/file-hoster/"

file_hoster = Blueprint("file-hoster", __name__)
@file_hoster.route("/")
def index():
    return render_template("pages/placeholder.html", carousel=False, nav_active="", notifications=notifications.render())