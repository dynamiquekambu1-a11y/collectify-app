from datetime import datetime
from flask import Blueprint, render_template
from models.client_model import get_all_clients

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    clients = get_all_clients()
    today = datetime.now().date()

    total_due = sum(c["debt"] for c in clients if c["status"] == "pending")
    total_paid = sum(c["debt"] for c in clients if c["status"] == "paid")

    overdue = len([
        c for c in clients
        if c["status"] == "pending" and
        datetime.strptime(c["due_date"], "%Y-%m-%d").date() < today
    ])

    return render_template(
        "dashboard.html",
        total_due=total_due,
        total_paid=total_paid,
        overdue=overdue
    )
