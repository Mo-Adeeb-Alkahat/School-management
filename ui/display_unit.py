from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from database.db import Database
from models.student import Student


class DisplayUnitWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize database connection
        self.db = Database()

        # Create UI elements
        self.unit_label = QLabel("Enter unit:")
        self.unit_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.table = QTableWidget()

        # Connect signals to slots
        self.search_button.clicked.connect(self.search_students)

        # Create layout and add elements
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.unit_label)
        hbox.addWidget(self.unit_input)
        hbox.addWidget(self.search_button)
        vbox.addLayout(hbox)
        vbox.addWidget(self.table)

        # Set layout and window title
        self.setLayout(vbox)
        self.setWindowTitle("Display Students by Unit")

    def search_students(self):
        # Clear table
        self.table.clear()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Unit"])

        # Retrieve students from database
        unit = self.unit_input.text().strip()
        students = self.db.query(Student).filter_by(unit=unit).all()

        # Populate table with student information
        self.table.setRowCount(len(students))
        for i, student in enumerate(students):
            self.table.setItem(i, 0, QTableWidgetItem(str(student.id)))
            self.table.setItem(i, 1, QTableWidgetItem(student.name))
            self.table.setItem(i, 2, QTableWidgetItem(student.unit))

        # Resize columns to fit content
        self.table.resizeColumnsToContents()
