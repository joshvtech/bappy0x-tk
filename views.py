from flask import Blueprint, redirect, redirect

#NOTE: Links
links = Blueprint("links", __name__, url_prefix="/links")

@links.route("/github")
def github():
    return redirect("https://github.com/Bappy0X", code=301)

@links.route("/discord")
def discord():
    return redirect("http://www.example.com", code=301)

@links.route("/lbry")
def lbry():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)
@links.route("/latestpublish")
def latestpublish():
    return redirect("http://www.example.com", code=301)
@links.route("/python-beginners")
def python_beginners():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)
@links.route("/start-coding")
def start_coding():
    return redirect("https://lbry.tv/$/invite/@Bappy0X:6", code=301)

@links.route("/linkedin")
def linkedin():
    return redirect("http://www.example.com", code=301)

@links.route("/patreon")
def patreon():
    return redirect("https://www.patreon.com/", code=301)
