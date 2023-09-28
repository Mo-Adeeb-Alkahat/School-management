from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from database.db import Database
from models.student import Student


class RemoveStudentWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Remove Student")
        self.resize(400, 200)

        # Create input fields and labels
        self.id_label = QLabel("Enter Student ID:")
        self.id_input = QLineEdit()
        self.remove_button = QPushButton("Remove Student")


        # Add CSS style to the input fields and remove button
        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }

            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 5px;
                font-size: 18px;
                padding: 5px;
            }

            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                font-size: 18px;
                padding: 10px 20px;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #3e8e41;
            }
        """)

        # Create vertical layout and add input fields and remove button
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.id_label)
        self.layout.addWidget(self.id_input)
        self.layout.addWidget(self.remove_button)

        # Set layout for the window
        self.setLayout(self.layout)

        # Connect remove button to remove_student function
        self.remove_button.clicked.connect(self.remove_student)

    def remove_student(self):
        # Get student id from input field
        id = self.id_input.text()

        # Check if id is empty
        if id == "":
            QMessageBox.warning(self, "Error", "Please enter a valid student ID.")
            return

        # Check if id is numeric
        if not id.isnumeric():
            QMessageBox.warning(self, "Error", "Please enter a valid numeric student ID.")
            return

        # Convert id to integer
        id = int(id)

        # Connect to database
        
        # Check if student exists
        
        if not Student.get_student_by_id(id):
            QMessageBox.warning(self, "Error", f"No student with ID {id} exists.")
            return

        # Remove student from database
        Student.remove(id)
        

        # Show confirmation message
        QMessageBox.information(self, "Success", f"Student with ID {id} has been removed from the database.")

        # Clear input field
        self.id_input.clear()
