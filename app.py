import os
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from models.db import init_db
from routes.dashboard_routes import dashboard_bp
from routes.client_routes import client_bp
from routes.log_routes import log_bp
from services.scheduler_service import check_due_payments

app = Flask(__name__)

init_db()

app.register_blueprint(dashboard_bp)
app.register_blueprint(client_bp)
app.register_blueprint(log_bp)

scheduler = BackgroundScheduler()
scheduler.add_job(check_due_payments, 'interval', hours=24)
scheduler.start()

if __name__ == "__main__":
    app.run()
