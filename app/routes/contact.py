from flask import Blueprint, render_template, request, flash, redirect, url_for
import os
import resend

resend.api_key = os.environ.get("RESEND_API_KEY")

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        service = request.form.get("service")
        budget = request.form.get("budget")
        message = request.form.get("message")

        try:
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "thewonderfuljo80@gmail.com",
                "subject": f"New Contact: {service} — {name}",
                "html": f"""
                    <h2>New message from your portfolio</h2>
                    <p><b>Name:</b> {name}</p>
                    <p><b>Email:</b> {email}</p>
                    <p><b>Service:</b> {service}</p>
                    <p><b>Budget:</b> {budget}</p>
                    <p><b>Message:</b><br>{message}</p>
                """
            })
            flash("success", "success")
        except Exception as e:
            flash("error", "error")

        return redirect(url_for("contact.index"))

    return render_template("contact/index.html")
