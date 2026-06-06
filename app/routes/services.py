from flask import Blueprint, render_template

services_bp = Blueprint("services", __name__, url_prefix="/services")

@services_bp.route("/web-development")
def web_dev():
    return render_template("services/web_dev.html")

@services_bp.route("/api-development")
def api_dev():
    return render_template("services/api_dev.html")

@services_bp.route("/translation")
def translation():
    return render_template("services/translation.html")
