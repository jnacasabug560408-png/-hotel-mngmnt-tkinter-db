import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      # default XAMPP root has no password
        database="hotel_db"
    )

if __name__ == "__main__":
    try:
        conn = connect_db()
        print("✅ Connected to MySQL")
        conn.close()
    except Exception as e:
        print("❌ Connection failed:", e)
