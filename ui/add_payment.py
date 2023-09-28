from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDateEdit, QMessageBox
from PyQt5.QtCore import Qt
from database.db import Database
from models.payment import Payment

class AddPaymentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Payment")
        self.resize(400, 300)

        # Create input fields and labels
        self.id_label = QLabel("Student ID:")
        self.id_input = QLineEdit()
        self.date_label = QLabel("Payment Date:")
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.amount_label = QLabel("Payment Amount:")
        self.amount_input = QLineEdit()
        self.receipt_label = QLabel("Receipt ID:")
        self.receipt_input = QLineEdit()
        self.description_label = QLabel("Payment Description:")
        self.description_input = QLineEdit()
        self.add_button = QPushButton("Add Payment")

        # Create vertical layout and add input fields and add button
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.id_label)
        self.layout.addWidget(self.id_input)
        self.layout.addWidget(self.date_label)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.receipt_label)
        self.layout.addWidget(self.receipt_input)
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.description_input)
        self.layout.addWidget(self.add_button)

        # Set layout for the window
        self.setLayout(self.layout)

        # Connect add button to add_payment function
        self.add_button.clicked.connect(self.add_payment)

    def add_payment(self):
        # Get payment details from input fields
        student_id = self.id_input.text()
        payment_date = self.date_input.date().toString(Qt.ISODate)
        payment_amount = self.amount_input.text()
        receipt_id = self.receipt_input.text()
        payment_description = self.description_input.text()

        #  Check if input fields are not empty
        if student_id == "" or payment_date == "" or payment_amount == "" or receipt_id == "":
            QMessageBox.warning(self, "Error", "Please fill in all required fields.")
            return

        # Check if input fields contain valid values
        if not student_id.isnumeric():
            QMessageBox.warning(self, "Error", "Please enter a valid numeric student ID.")
            return

        if not payment_amount.isnumeric():
            QMessageBox.warning(self, "Error", "Please enter a valid numeric payment amount.")
            return

        # Convert input fields to appropriate data types
        student_id = int(student_id)
        payment_amount = int(payment_amount)

        # Connect to database
        db = Database()
        conn = db.create_connection()

        # Check if student exists
        if not db.execute('SELECT * FROM students WHERE id = %s;', (student_id,)).fetchone():
            QMessageBox.warning(self, "Error", f"No student with ID {student_id} exists.")
            return

        # Create new Payment object and add payment to database
        payment = Payment(db)
        payment.add_payment(student_id, payment_date, payment_amount, receipt_id, payment_description)

        # Show confirmation message
        QMessageBox.information(self, "Success", "Payment has been added to the database.")

        # Clear input fields
        self.id_input.clear()
        self.date_input.setDate(self.date_input.minimumDate())
        self.amount_input.clear()
        self.receipt_input.clear()
        self.description_input.clear()

