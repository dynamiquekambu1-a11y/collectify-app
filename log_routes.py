from flask import Blueprint, render_template, redirect, url_for

from models.log_model import get_logs
from services.scheduler_service import check_due_payments

log_bp = Blueprint("logs", __name__)

@log_bp.route("/logs")
def logs():

    logs = get_logs()

    return render_template("logs.html", logs=logs)

@log_bp.route("/run_now")
def run_now():

    check_due_payments()

    return redirect(url_for("logs.logs"))
