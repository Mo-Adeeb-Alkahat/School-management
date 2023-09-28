import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFormLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox , QMessageBox
from models.student import Student


class AddStudentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Student")

        # create the form layout and add widgets to it
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        form_layout.addRow(QLabel("Name:"), self.name_input)

        gender_options = ["Male", "Female"]
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(gender_options)
        form_layout.addRow(QLabel("Gender:"), self.gender_combo)

        self.unit_input = QLineEdit()
        form_layout.addRow(QLabel("Unit:"), self.unit_input)

        self.father_name_input = QLineEdit()
        form_layout.addRow(QLabel("Father's Name:"), self.father_name_input)

        self.mother_name_input = QLineEdit()
        form_layout.addRow(QLabel("Mother's Name:"), self.mother_name_input)

        self.father_phone_input = QLineEdit()
        form_layout.addRow(QLabel("Father's Phone Number:"), self.father_phone_input)

        self.mother_phone_input = QLineEdit()
        form_layout.addRow(QLabel("Mother's Phone Number:"), self.mother_phone_input)

        self.father_job_input = QLineEdit()
        form_layout.addRow(QLabel("Father's Job:"), self.father_job_input)

        self.mother_job_input = QLineEdit()
        form_layout.addRow(QLabel("Mother's Job:"), self.mother_job_input)

        self.phone_input = QLineEdit()
        form_layout.addRow(QLabel("Student Phone Number:"), self.phone_input)

        self.birth_place_input = QLineEdit()
        form_layout.addRow(QLabel("Birth Place:"), self.birth_place_input)

        self.birth_date_input = QLineEdit()
        form_layout.addRow(QLabel("Birth Date (yyyy-mm-dd):"), self.birth_date_input)

        self.joining_date_input = QLineEdit()
        form_layout.addRow(QLabel("Joining Date (yyyy-mm-dd):"), self.joining_date_input)

        self.address_input = QLineEdit()
        form_layout.addRow(QLabel("Address:"), self.address_input)

        self.grade = QLineEdit()
        form_layout.addRow(QLabel("Grade"), self.grade)

        self.tuition_fee_input = QLineEdit()
        form_layout.addRow(QLabel("Tuition Fee:"), self.tuition_fee_input)

        # create the buttons and add them to a horizontal layout
        add_button = QPushButton("Add Student")
        add_button.clicked.connect(self.add_student)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(cancel_button)

        # create the main layout and add the form layout and button layout to it
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def add_student(self):
        name = self.name_input.text()
        gender = self.gender_combo.currentText()
        unit = self.unit_input.text()
        father_name = self.father_name_input.text()
        mother_name = self.mother_name_input.text()
        father_phone_number = self.father_phone_input.text()
        mother_phone_number = self.mother_phone_input.text()
        father_job = self.father_job_input.text()
        mother_job = self.mother_job_input.text()
        student_phone = self.phone_input.text()
        birth_place = self.birth_place_input.text()
        birth_date = self.birth_date_input.text()
        joining_date = self.joining_date_input.text()
        address = self.address_input.text()
        grade = self.grade.text()
        tuition_fee = self.tuition_fee_input.text()

        new_student = Student(name=name, gender=gender, unit=unit, father_name=father_name, mother_name=mother_name,
                          father_phone_number=father_phone_number, mother_phone_number=mother_phone_number,
                          father_job=father_job, mother_job=mother_job, student_phone=student_phone,
                          birth_place=birth_place, birth_date=birth_date, joining_date=joining_date,
                          address=address, grade=grade, tuition_fee=tuition_fee)

        if Student.add_student_to_db(new_student) :
        # add the student to the database
            
            QMessageBox.information(self, "Success", "Student has been added to the database.")
        else :
            QMessageBox.warning(self, "Error", "Could not add student to database. Error: ")


        

