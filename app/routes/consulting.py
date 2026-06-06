from flask import Blueprint, render_template

consulting_bp = Blueprint("consulting", __name__)

@consulting_bp.route("/consulting")
def index():
    return render_template("consulting/index.html")


