import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='cSEHWZsrUJx8FDH.root',
        password='jsvw4sIsJShbuMWi',
        database='student_task_manager',
        port=4000
    )
    return connection