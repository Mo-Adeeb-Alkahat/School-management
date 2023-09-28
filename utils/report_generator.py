import os
import psycopg2
from dotenv import load_dotenv
from db import Database








def generate_exam_report(student_id, year, month):
    with Database() as db:
        db.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        student = db.fetchall()

        db.execute("""
            SELECT *
            FROM exams
            WHERE student_id = %s
            AND date_part('year', exam_date) = %s
            AND date_part('month', exam_date) = %s
            """, (student_id, year, month))
        exams = db.fetchall()

        report = f"Report for {student[0][1]} - Exams in {month}/{year}\n"
        for exam in exams:
            report += f"Subject: {exam[3]}, Score: {exam[4]}\n"
        return report
