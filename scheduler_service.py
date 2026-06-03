from datetime import datetime

from models.client_model import get_pending_clients
from models.log_model import add_log
from services.reminder_service import send_reminder

def check_due_payments():

    clients = get_pending_clients()
    today = datetime.now().date()

    for client in clients:

        due = datetime.strptime(client["due_date"], "%Y-%m-%d").date()
        days_overdue = (today - due).days

        level = None

        if days_overdue == 3:
            level = "soft"

        elif days_overdue == 7:
            level = "medium"

        elif days_overdue == 14:
            level = "final"

        if level:
            status = send_reminder(client, level)
            add_log(client["id"], level, status)
