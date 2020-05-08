from flask import Blueprint, redirect, redirect

#TODO: Make Links and Videos use database and `<var>` from flask

#NOTE: Links
links = Blueprint("links", __name__, url_prefix="/links")
@links.route("/github")
def github():
    return redirect("https://github.com/Bappy0X", code=301)
@links.route("/discord")
def discord():
    return redirect("http://discord.gg/", code=301)
@links.route("/lbry")
def lbry():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)
@links.route("/patreon")
def patreon():
    return redirect("https://www.patreon.com/", code=301)
@links.route("/fiverr")
def fiverr():
    return redirect("https://www.fiverr.com/", code=301)

#NOTE: Video Links
videos = Blueprint("videos", __name__, url_prefix="/videos")
@videos.route("/latest")
def latest():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)
@videos.route("/start-coding")
def start_coding():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)
@videos.route("/html-beginners")
def html_beginners():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)
@videos.route("/css-beginners")
def css_beginners():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)
@videos.route("/python-beginners")
def python_beginners():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)
