import sqlite3

# Function to connect to the database
def get_db_connection(db):
    """Connect to SQLite database."""
    conn = sqlite3.connect(db)
    return conn

# Function to create the database table (if not exists)
def create_student_table(db="student.db"):
    """Create the STUDENT table in the database."""
    table_creation_query = """CREATE TABLE IF NOT EXISTS STUDENT (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                NAME TEXT NOT NULL,
                                CLASS TEXT NOT NULL,
                                SECTION TEXT NOT NULL,
                                MARKS INTEGER CHECK (MARKS >= 0 AND MARKS <= 100)
                              );"""
    conn = get_db_connection(db)
    cursor = conn.cursor()
    cursor.execute(table_creation_query)
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(db="student.db"):
    """Insert sample student data into the database."""
    student_data = [
        ('Grabriel', 'Data Science', 'A', 90),
        ('Mike', 'ML Engineer', 'B', 77),
        ('Rose', 'Devops', 'C', 74),
        ('Eric', 'Data Engineer', 'B', 68)
    ]
    conn = get_db_connection(db)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)', student_data)
    conn.commit()
    conn.close()

# Function to execute SQL queries and fetch results
def read_sql_query(sql, db="student.db"):
    """Execute SQL query and return results."""
    conn = get_db_connection(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows