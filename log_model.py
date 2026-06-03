from models.db import get_connection

def add_log(client_id, level, status):
    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "INSERT INTO logs (client_id, level, status) VALUES (?,?,?)",
        (client_id, level, status)
    )

    conn.commit()
    conn.close()

def get_logs():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    SELECT logs.*, clients.name
    FROM logs
    JOIN clients ON logs.client_id = clients.id
    ORDER BY sent_at DESC
    LIMIT 100
    """)

    rows = c.fetchall()

    conn.close()
    return rows
