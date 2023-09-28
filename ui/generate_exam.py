from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QCalendarWidget
from datetime import datetime, timedelta
from database.db import Database
from models.exam import Exam

class GenerateExamWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generate Exam Report")
        self.resize(600, 400)

        layout = QVBoxLayout()

        # Student ID input
        student_id_layout = QHBoxLayout()
        student_id_label = QLabel("Student ID:")
        self.student_id_input = QLineEdit()
        self.student_id_input.setPlaceholderText("Enter Student ID")
        student_id_layout.addWidget(student_id_label)
        student_id_layout.addWidget(self.student_id_input)

        # Month selection
        month_layout = QHBoxLayout()
        month_label = QLabel("Month:")
        self.month_input = QComboBox()
        for month in range(1, 13):
            self.month_input.addItem(datetime(2000, month, 1).strftime('%B'))
        month_layout.addWidget(month_label)
        month_layout.addWidget(self.month_input)

        # Calendar widget to select a date
        calendar_layout = QHBoxLayout()
        calendar_label = QLabel("Choose a date:")
        self.calendar_widget = QCalendarWidget()
        calendar_layout.addWidget(calendar_label)
        calendar_layout.addWidget(self.calendar_widget)

        # Submit button
        submit_layout = QHBoxLayout()
        self.submit_button = QPushButton("Generate Report")
        self.submit_button.clicked.connect(self.generate_report)
        submit_layout.addWidget(self.submit_button)

        # Table widget to display exam results
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Exam Date", "Subject", "Score", "Month"])
        layout.addWidget(QLabel("Generate Exam Report"))
        layout.addLayout(student_id_layout)
        layout.addLayout(month_layout)
        layout.addLayout(calendar_layout)
        layout.addLayout(submit_layout)
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def generate_report(self):
        # Retrieve input data
        student_id = self.student_id_input.text().strip()
        if not student_id.isdigit():
            self.table_widget.setRowCount(0)
            return

        selected_month = self.month_input.currentIndex() + 1
        selected_date = self.calendar_widget.selectedDate().toPyDate()

        # Get exams from the database
        with Database() as db:
            exams = Exam.get_by_student_id(db, student_id)
            exams = [exam for exam in exams if exam.exam_date.month == selected_month and exam.exam_date.year == selected_date.year]

        # Populate table widget with results
        self.table_widget.setRowCount(len(exams))
        for row, exam in enumerate(exams):
            self.table_widget.setItem(row, 0, QTableWidgetItem(exam.exam_date.strftime('%Y-%m-%d')))
            self.table_widget.setItem(row, 1, QTableWidgetItem(exam.subject))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(exam.score)))
            self.table_widget.setItem(row, 3, QTableWidgetItem(selected_date.strftime('%B %Y')))
