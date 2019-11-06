# Keith Kirtfield
# Database
# TODO uploading and retrieving data // Smart Selection
import sqlite3


def create_teable():
    conn = sqlite3.connect('applicant.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE if NOT EXISTS applicants(
        app_id INTEGER PRIMARY KEY,
        first_name text
        last_name text
        position text
        school text
        degree text
    )''')
    conn.close()


def retrieve_applicants():
    conn = sqlite3.connect('applicant.db')
    c = conn.cursor()
    c.execute('SELECT * FROM applicants')
    appArray = c.fetchall()
    print(appArray[0])
    return "Tree"
    conn.close()
