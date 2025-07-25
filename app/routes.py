from flask import render_template
from app import app
from flask_mail import Message
from app import mail

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About Me")

@app.route("/skills")
def skills():
    return render_template("skills.html", title="Skills & Tools")

@app.route("/projects")
def projects():
    # Example project list you can replace with your own data later
    projects_list = [
        {
            "title": "Flask Notes App",
            "desc": "A CRUD app with Flask and SQLite, clean UI and dark mode.",
            "tech": ["Flask", "SQLite", "Bootstrap"],
            "link": "https://github.com/yourusername/flask-notes-app"
        },
        {
            "title": "Responsive Landing Page",
            "desc": "Built with HTML, CSS, Bootstrap, and JS animations.",
            "tech": ["HTML", "CSS", "Bootstrap", "JavaScript"],
            "link": "https://yourdomain.com/landing-page"
        },
        # Add more projects here...
    ]
    return render_template("projects.html", title="Projects", projects=projects_list)

from flask import request, flash, redirect, url_for
import smtplib

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("Please fill in all fields.", "danger")
            return redirect(url_for("contact"))

        try:
            msg = Message("Portfolio Contact Form",
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[app.config['MAIL_USERNAME']])
            msg.body = f"From: {name} <{email}>\n\n{message}"
            mail.send(msg)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash(f"Error sending message: {str(e)}", "danger")
        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact")
