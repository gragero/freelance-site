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
    <div style="background:#0b0f19;padding:40px 0;font-family:Arial,sans-serif;">
      <div style="max-width:600px;margin:0 auto;background:#111827;border-radius:12px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.3);">

        <!-- Header -->
        <div style="background:linear-gradient(135deg,#00ff41,#00c853);padding:20px;text-align:center;">
          <h1 style="margin:0;color:#0b0f19;font-size:20px;">📩 New Portfolio Message</h1>
        </div>

        <!-- Body -->
        <div style="padding:24px;color:#e5e7eb;">

          <p style="margin:0 0 12px;font-size:14px;color:#9ca3af;">
            You received a new message from your website
          </p>

          <div style="margin-top:20px;">
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Service:</strong> {service}</p>
          </div>
          <p><strong>Budget:</strong> {budget}</p>

          <div style="margin-top:20px;padding:16px;background:#1f2937;border-radius:8px;">
            <p style="margin:0;white-space:pre-line;">
              {message}
            </p>
          </div>

          <!-- CTA -->
          <div style="margin-top:25px;text-align:center;">
            <a href="mailto:{email}"
               style="display:inline-block;background:#00ff41;color:#0b0f19;
                      padding:10px 18px;border-radius:6px;text-decoration:none;
                      font-weight:bold;">
              Reply Now
            </a>
          </div>

        </div>

        <!-- Footer -->
        <div style="padding:14px;text-align:center;font-size:12px;color:#6b7280;background:#0b0f19;">
          Automated message from your portfolio system
        </div>

      </div>
    </div>
    """
})
            flash("success", "success")
        except Exception as e:
            flash("error", "error")

        return redirect(url_for("contact.index"))

    return render_template("contact/index.html")
