import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from datetime import datetime
from psycopg2 import connect
from dotenv import load_dotenv
from models.exam import Exam
from database.db import Database
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


class AddExamWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Exam")

        # Create widgets
        student_id_label = QLabel("Student ID:")
        self.student_id_field = QLineEdit()
        exam_date_label = QLabel("Exam Date (YYYY-MM-DD):")
        self.exam_date_field = QLineEdit()
        subject_label = QLabel("Subject:")
        self.subject_field = QLineEdit()
        score_label = QLabel("Score:")
        self.score_field = QLineEdit()
        save_button = QPushButton("Save")

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(student_id_label)
        layout.addWidget(self.student_id_field)
        layout.addWidget(exam_date_label)
        layout.addWidget(self.exam_date_field)
        layout.addWidget(subject_label)
        layout.addWidget(self.subject_field)
        layout.addWidget(score_label)
        layout.addWidget(self.score_field)
        layout.addWidget(save_button)
        self.setLayout(layout)

        # Connect signals to slots
        save_button.clicked.connect(self.save_exam)

    def save_exam(self):
        # Get values from fields
        student_id = int(self.student_id_field.text())
        exam_date = datetime.strptime(self.exam_date_field.text(), '%Y-%m-%d').date()
        subject = self.subject_field.text()
        score = float(self.score_field.text())

        # Create exam object and save to DB
        exam = Exam(student_id, exam_date, subject, score)
        with connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as conn:
            with conn.cursor() as cur:
                exam.save_to_db(cur)
                conn.commit()

        # Close the window
        self.close()
