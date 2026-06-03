from flask import Blueprint, render_template, request, redirect, url_for

from models.client_model import (
    add_client,
    get_all_clients,
    update_status,
    delete_client
)

client_bp = Blueprint("clients", __name__)

@client_bp.route("/clients")
def clients():
    clients = get_all_clients()
    return render_template("clients.html", clients=clients)

@client_bp.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        add_client(
            request.form["name"],
            request.form["email"],
            float(request.form["debt"]),
            request.form["due_date"]
        )

        return redirect(url_for("clients.clients"))

    return render_template("add_client.html")

@client_bp.route("/mark_paid/<int:id>")
def mark_paid(id):

    update_status(id, "paid")

    return redirect(url_for("clients.clients"))

@client_bp.route("/delete/<int:id>")
def delete(id):

    delete_client(id)

    return redirect(url_for("clients.clients"))
