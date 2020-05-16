from flask import Blueprint, render_template, redirect, url_for

from sys import path
path.append("...")
from static.db.models import notifications

folderpath = "pages/projects/news-bot/"

news_bot = Blueprint("news-bot", __name__)

@news_bot.route("/")
def index():
    return render_template("pages/placeholder.html", carousel=False, nav_active="", notifications=notifications.render())