from services.email_sender import send_email
from services.template_loader import load_template

def send_reminder(client, level):

    templates = {
        "soft": ("email_templates/soft.txt", "Friendly Reminder"),
        "medium": ("email_templates/medium.txt", "Payment Overdue"),
        "final": ("email_templates/final.txt", "Final Notice")
    }

    path, subject = templates[level]

    data = {
        "name": client["name"],
        "amount": client["debt"],
        "date": client["due_date"]
    }

    body = load_template(path, data)

    return send_email(client["email"], subject, body)
