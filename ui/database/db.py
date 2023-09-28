import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute(self, query, params=None):
        if params:
            self.cur.execute(query, params)
        else:
            self.cur.execute(query)
        self.conn.commit()
        return self.cur

    def fetchall(self):
        return self.cur.fetchall()

    def create_tables(self):
        self.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                gender VARCHAR(255),
                unit VARCHAR(255),
                father_name VARCHAR(255),
                mother_name VARCHAR(255),
                father_phone_number VARCHAR(20),
                mother_phone_number VARCHAR(20),
                father_job VARCHAR(255),
                mother_job VARCHAR(255),
                student_phone VARCHAR(20),
                birth_place VARCHAR(255),
                birth_date DATE,
                joining_date DATE,
                address TEXT,
                grade VARCHAR(20),
                tuition_fee DECIMAL(10,2)
            );
        ''')

        self.execute('''
            CREATE TABLE IF NOT EXISTS exams (
                id SERIAL PRIMARY KEY,
                student_id INTEGER REFERENCES students(id),
                exam_date DATE,
                subject VARCHAR(255),
                score INTEGER
            );
        ''')

        self.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id SERIAL PRIMARY KEY,
                student_id INTEGER REFERENCES students(id),
                date DATE NOT NULL,
                amount NUMERIC(10, 2) NOT NULL,
                receipt_id VARCHAR(20) NOT NULL,
                remaining_amount NUMERIC(10, 2),
                description TEXT
            );
        ''')

    def drop_tables(self):
        self.execute('DROP TABLE IF EXISTS payments;')
        self.execute('DROP TABLE IF EXISTS exams;')
        self.execute('DROP TABLE IF EXISTS students;')

def create_db() : 
    datab =  Database() 
    datab.drop_tables()

    datab.create_tables()
    s=input('enter to drop and exit')
    datab.drop_tables()

#Note that I added the DROP TABLES method to make it easier to clean up the database during development/testing.
#  You should remove it in production.
#  Also, make sure to update the .env file with the correct database credentials.