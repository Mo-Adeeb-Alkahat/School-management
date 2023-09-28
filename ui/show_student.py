import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFormLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer
from database.db import Database
import datetime
from models.student import Student


class ShowStudentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show Student Information")
        
        # create the form layout and add widgets to it
        form_layout = QFormLayout()

        self.id_input = QLineEdit()
        form_layout.addRow(QLabel("Student ID:"), self.id_input)

        # create the buttons and add them to a horizontal layout
        show_button = QPushButton("Show Information")
        show_button.clicked.connect(self.show_student_info)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
        button_layout.addWidget(show_button)
        button_layout.addWidget(cancel_button)

        # create the main layout and add the form layout and button layout to it
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def show_student_info(self):
        student_id = self.id_input.text()

        # query the database for the student with the given id
        
        student =  Student.get_student_by_id(student_id)

        if student:
            # create a form layout to display the student information
            info_layout = QFormLayout()

            info_layout.addRow(QLabel("Name:"), QLabel(student.name))
            info_layout.addRow(QLabel("Gender:"), QLabel(student.gender))
            info_layout.addRow(QLabel("Unit:"), QLabel(student.unit))
            info_layout.addRow(QLabel("Father's Name:"), QLabel(student.father_name))
            info_layout.addRow(QLabel("Mother's Name:"), QLabel(student.mother_name))
            info_layout.addRow(QLabel("Father's Phone Number:"), QLabel(student.father_phone_number))
            info_layout.addRow(QLabel("Mother's Phone Number:"), QLabel(student.mother_phone_number))
            info_layout.addRow(QLabel("Father's Job:"), QLabel(student.father_job))
            info_layout.addRow(QLabel("Mother's Job:"), QLabel(student.mother_job))
            info_layout.addRow(QLabel("Student Phone Number:"), QLabel(student.student_phone))
            info_layout.addRow(QLabel("Birth Place:"), QLabel(student.birth_place))
            info_layout.addRow(QLabel("Birth Date:"), QLabel(student.birth_date.strftime('%Y-%m-%d')))
            info_layout.addRow(QLabel("Joining Date:"), QLabel(student.joining_date.strftime('%Y-%m-%d')))
            info_layout.addRow(QLabel("Address:"), QLabel(student.address))
            info_layout.addRow(QLabel("Grade:"), QLabel(student.grade))
            info_layout.addRow(QLabel("Tuition Fee:"), QLabel(str(student.tuition_fee)))

            # create a new dialog to display the student information
            info_dialog = QDialog(parent=self)
            info_dialog.setWindowTitle("Student Information")
            info_dialog.setLayout(info_layout)
            print(info_dialog.dumpObjectTree())
            # create a button to close the dialog
            close_button = QPushButton("Close")
            close_button.clicked.connect(info_dialog.accept)

            timer = QTimer()
            timer.setSingleShot(True)
            timer.timeout.connect(info_dialog.close)
            timer.start(5000000) # 5000 ms = 5 seconds
            info_dialog.show()
        else:
            # display an error message if the student was not found
            error_dialog = QDialog(parent=self)
            error_dialog.setWindowTitle("Error")
            error_layout = QVBoxLayout()
            error_layout.addWidget(QLabel("Student not found"))
            error_dialog.setLayout(error_layout)
            error_dialog.show()
