from flask import Flask
from db_config import get_database_connection

app = Flask(__name__)

@app.route('/')
def home():
    connection = get_database_connection()
    if connection is None:
        return 'Database connection failed', 500

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM students')
        row = cursor.fetchone()
        student_count = row[0] if row else 0
    except Exception:
        return 'Error fetching data', 500
    finally:
        if cursor:
            cursor.close()
        connection.close()

    return f"Total Students: {student_count}"

if __name__ == '__main__':
    app.run(debug=True)