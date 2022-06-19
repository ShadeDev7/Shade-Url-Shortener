from flask import url_for, redirect

from website import create_app

app = create_app()


@app.errorhandler(404)
def not_found(_):
    return redirect(url_for("views.index"))


if __name__ == "__main__":
    app.run(debug=True)
