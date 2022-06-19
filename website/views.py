from flask import Blueprint, render_template, request, redirect
from .classes import Database

views = Blueprint("views", __name__)


@views.route("/")
def index():
    return render_template("index.html")


@views.route("/", methods=["POST"])
def create_url():
    if not request.form:
        return render_template("index.html")

    url = dict(request.form).get("url")
    if not url:
        return render_template("index.html")

    db = Database()
    shortened_url = db.create_url(url)

    return render_template("index.html", url=url, shortened_url=shortened_url)


@views.route("/<url_id>")
def redirect_url(url_id):
    db = Database()
    url = db.get_url(url_id)

    if not url:
        return render_template("index.html")

    url = url if "http" in url or "https" in url else f"http://{url}"

    return redirect(url)
