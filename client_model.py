from models.db import get_connection

def add_client(name, email, debt, due_date):
    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "INSERT INTO clients (name, email, debt, due_date) VALUES (?,?,?,?)",
        (name, email, debt, due_date)
    )

    conn.commit()
    conn.close()

def get_all_clients():
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM clients ORDER BY due_date ASC")
    rows = c.fetchall()

    conn.close()
    return rows

def get_pending_clients():
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM clients WHERE status='pending'")
    rows = c.fetchall()

    conn.close()
    return rows

def update_status(client_id, status):
    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "UPDATE clients SET status=? WHERE id=?",
        (status, client_id)
    )

    conn.commit()
    conn.close()

def delete_client(client_id):
    conn = get_connection()
    c = conn.cursor()

    c.execute("DELETE FROM clients WHERE id=?", (client_id,))

    conn.commit()
    conn.close()
