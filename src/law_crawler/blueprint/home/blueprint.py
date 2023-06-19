import flask

home = flask.Blueprint("home", __name__, template_folder="templates")


@home.route("/")
def index():
    return flask.render_template("homepage.html")
