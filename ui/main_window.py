
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QPushButton, QTableWidget, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QLineEdit ,QDialog

#import os
import sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("School Management System")

        # create menu bar and add options
        menu = self.menuBar()
        students_menu = menu.addMenu("Students")
        classes_menu = menu.addMenu("Classes")
        payments_menu = menu.addMenu("Payments")
        exams_menu = menu.addMenu("Exams")

        # create dashboard
        dashboard_layout = QVBoxLayout()
        summary_label = QLabel("Summary of Key Features and Functionality")
        self.add_student_button = QPushButton("Add New Student")  # create the instance variable
        self.display_student_button = QPushButton("Diplay Student infos")
        self.edit_student_button = QPushButton("Edit Student infos")
        self.remove_student_button = QPushButton("Remove Student infos")
        self.display_class_button = QPushButton("Diplsay Class infos")
        self.add_payment_button = QPushButton("Add New Payment")
        self.add_exam_button = QPushButton("Add New Exam")
        self.generate_exam_button = QPushButton("Generate exam report")
        dashboard_layout.addWidget(summary_label)
        dashboard_layout.addWidget(self.add_student_button)  # add the button to the layout
        dashboard_layout.addWidget(self.display_student_button)
        dashboard_layout.addWidget(self.edit_student_button)
        dashboard_layout.addWidget(self.remove_student_button)

        dashboard_layout.addWidget(self.display_class_button)
        dashboard_layout.addWidget(self.add_payment_button)
        dashboard_layout.addWidget(self.add_exam_button)
        dashboard_layout.addWidget(self.generate_exam_button)
        dashboard_widget = QWidget()
        dashboard_widget.setLayout(dashboard_layout)

        # create tables or lists to display data
        students_table = QTableWidget()
        classes_table = QTableWidget()
        payments_table = QTableWidget()
        exams_table = QTableWidget()

        # create search and filter functionality
        search_label = QLabel("Search:")
        search_box = QLineEdit()
        filter_label = QLabel("Filter:")
        filter_box = QComboBox()
        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(search_box)
        search_layout.addWidget(filter_label)
        search_layout.addWidget(filter_box)

        # create graphs or charts to display statistics
        graph_label = QLabel("Statistics or Insights about Student Performance or Program Activity")

        # create footer
        footer_label = QLabel("School Management System | Contact: info@school.com")

        # add widgets to the main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(dashboard_widget)
        main_layout.addWidget(students_table)
        main_layout.addWidget(classes_table)
        main_layout.addWidget(payments_table)
        main_layout.addWidget(exams_table)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(graph_label)
        main_layout.addWidget(footer_label)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


        self.edit_student_button.clicked.connect(self.open_edit_student_window)
        self.remove_student_button.clicked.connect(self.open_remove_student_window)
        self.display_student_button.clicked.connect(self.open_display_student_window)
        self.add_student_button.clicked.connect(self.open_add_student_window)
        self.display_class_button.clicked.connect(self.open_display_class_button)
        self.add_payment_button.clicked.connect(self.open_add_payment_button)
        self.add_exam_button.clicked.connect(self.open_add_exam_button)
        self.generate_exam_button.clicked.connect(self.open_generat_exam_button)
        
    def open_generat_exam_button(self):
        from generate_exam import GenerateExamWindow  # import the window class
        self.GenerateExamWindow = GenerateExamWindow()  # create an instance of the window
        self.GenerateExamWindow.show()  # show the window            
    
    
    
    def open_add_exam_button(self):
        from add_exam import AddExamWindow  # import the window class
        self.AddExamWindow = AddExamWindow()  # create an instance of the window
        self.AddExamWindow.show()  # show the window        

    
    
    def open_add_payment_button(self):
        from add_payment import AddPaymentWindow  # import the window class
        self.AddPaymentWindow = AddPaymentWindow()  # create an instance of the window
        self.AddPaymentWindow.show()  # show the window    
    
    
    def open_display_class_button(self):
        from display_unit import DisplayUnitWindow  # import the window class
        self.DisplayUnitWindow = DisplayUnitWindow()  # create an instance of the window
        self.DisplayUnitWindow.show()  # show the window    

    def open_remove_student_window(self):
        from remove_student import RemoveStudentWindow  # import the window class
        self.RemoveStudentWindow = RemoveStudentWindow()  # create an instance of the window
        self.RemoveStudentWindow.show()  # show the window    
    
    
    def open_edit_student_window(self):
        from edit_student import EditStudentWindow  # import the window class
        self.EditStudentWindow = EditStudentWindow()  # create an instance of the window
        self.EditStudentWindow.show()  # show the window    
    
    
    def open_display_student_window(self):
        from show_student import ShowStudentWindow  # import the window class
        self.ShowStudentWindow = ShowStudentWindow()  # create an instance of the window
        self.ShowStudentWindow.show()  # show the window    
    
    def open_add_student_window(self):
        from add_student import AddStudentWindow  # import the window class
        self.add_student_window = AddStudentWindow()  # create an instance of the window
        self.add_student_window.show()  # show the window

    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
