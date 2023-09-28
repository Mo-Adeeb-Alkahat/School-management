import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')




class Payment:
    def __init__(self, db):
        self.db = db

    def add_payment(self, student_id, date, amount, receipt_id, description=None):
        remaining_payment = self.calculate_remaining_payment(student_id)
        self.db.execute('''
            INSERT INTO payments (student_id, date, amount, receipt_id, remaining_amount, description)
            VALUES (%s, %s, %s, %s, %s, %s);
        ''', (student_id, date, amount, receipt_id, remaining_payment, description))
        
        # Update student's tuition fee and remaining payment
        tuition_fee = self.db.execute('SELECT tuition_fee FROM students WHERE id = %s;', (student_id,)).fetchone()[0]
        new_tuition_fee = tuition_fee - amount
        new_remaining_payment = self.calculate_remaining_payment(student_id)
        self.db.execute('''
            UPDATE students SET tuition_fee = %s WHERE id = %s;
            UPDATE payments SET remaining_amount = %s WHERE student_id = %s ORDER BY date DESC LIMIT 1;
        ''', (new_tuition_fee, student_id, new_remaining_payment, student_id))

    @staticmethod
    def get_payments_by_student_id(student_id):
        with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as conn:
            with conn.cursor() as cur:
                query = """
                        SELECT * FROM payments
                        WHERE student_id=%s;
                        """
                cur.execute(query, (student_id,))
                rows = cur.fetchall()
                cur.close()
                return [Payment(*row) for row in rows]

    def delete(self):
        with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as conn:
            with conn.cursor() as cur:
                query = """
                        DELETE FROM payments
                        WHERE id=%s;
                        """
                cur.execute(query, (self.id,))
                conn.commit()
                cur.close()

    def update(self):
        with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as conn:
            with conn.cursor() as cur:
                query = """
                        UPDATE payments
                        SET student_id=%s, date=%s, amount=%s, receipt_id=%s, remaining_amount=%s, description=%s
                        WHERE id=%s;
                        """
                cur.execute(query, (self.student_id, self.date, self.amount, self.receipt_id, self.remaining_amount, self.description, self.id))
                conn.commit()
                cur.close()
