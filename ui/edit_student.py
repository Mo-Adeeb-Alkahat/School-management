from PyQt5.QtWidgets import QApplication, QDialog, QFormLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton,QMessageBox, QComboBox
from database.db import Database
from models.student import Student


class EditStudentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Student")

        # create the form layout and add widgets to it
        form_layout = QFormLayout()

        self.id_input = QLineEdit()
        form_layout.addRow(QLabel("ID:"), self.id_input)

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
        form_layout.addRow(QLabel("Birth Date (dd-mm-yyyy):"), self.birth_date_input)

        self.joining_date_input = QLineEdit()
        form_layout.addRow(QLabel("Joining Date (dd-mm-yyyy):"), self.joining_date_input)

        self.address_input = QLineEdit()
        form_layout.addRow(QLabel("Address:"), self.address_input)

        self.grade_input = QLineEdit()
        form_layout.addRow(QLabel("Grade: "), self.grade_input)

        self.tuition_fee_input = QLineEdit()
        form_layout.addRow(QLabel("Tution fee: "), self.tuition_fee_input)

        # create the buttons and add them to a horizontal layout
        update_button = QPushButton("Update Student")
        update_button.clicked.connect(self.update_student)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
        button_layout.addWidget(update_button)
        button_layout.addWidget(cancel_button)

        # create the main layout and add the form layout and button layout to it
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def update_student(self):
            # get the values from the input fields
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
            grade = self.grade_input.text()
            tuition_fee = self.tuition_fee_input.text()
        
            # update the 
            # student in the database
            student_id = self.id_input.text()
            updated_student = Student(name, gender, unit, father_name, mother_name, father_phone_number,
                                  mother_phone_number, father_job, mother_job, student_phone, birth_place, birth_date,
                                  joining_date, address, grade , tuition_fee)
            
            try:
                Student.update_in_db(updated_student,student_id)
            except Exception as e:
                QMessageBox.warning(self, "Error", "Failed to update student information.\n\nError message: {}".format(e))
            else:
                QMessageBox.information(self, "Success", "Student information updated successfully.")
                self.accept()
