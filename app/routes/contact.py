from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from app.extensions import mail

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        service = request.form.get("service")
        budget = request.form.get("budget")
        message = request.form.get("message")

        msg = Message(
            subject=f"New Contact: {service} — {name}",
            recipients=["thewonderfuljo80@gmail.com"],
            body=f"""
New message from your portfolio:

Name:    {name}
Email:   {email}
Service: {service}
Budget:  {budget}

Message:
{message}
            """
        )

        try:
            mail.send(msg)
            flash("success", "success")
        except Exception as e:
            flash("error", "error")

        return redirect(url_for("contact.index"))

    return render_template("contact/index.html")
