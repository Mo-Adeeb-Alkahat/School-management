import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from main_window import MainWindow

class SignInForm(QWidget):
    def __init__(self):
        super().__init__()

        # create widgets
        self.username_label = QLabel('Username:')
        self.username_textbox = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_textbox = QLineEdit()
        self.password_textbox.setEchoMode(QLineEdit.Password)
        self.signin_button = QPushButton('Sign In')
        #self.forgot_button = QPushButton('Forgot Password?')

        # create layout
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox1.addWidget(self.username_label)
        hbox1.addWidget(self.username_textbox)
        hbox2.addWidget(self.password_label)
        hbox2.addWidget(self.password_textbox)
        hbox3.addWidget(self.signin_button)
        #hbox3.addWidget(self.forgot_button)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        self.setLayout(vbox)

        # set properties
        self.setWindowTitle('Sign In Form')
       #setGeometry(x, y, width, height)
        self.setGeometry(300, 300, 300, 350)

        # apply styles
        self.setStyleSheet("""
            SignInForm {
                background-color: #f0f0f0;
                border-radius: 10px;
            }
            QLabel {
                color: black;
                font-size: 18px;
            }
            QLineEdit {
                background-color: white;
                border-radius: 5px;
                font-size: 18px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 18px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #3E8E41;
            }
        """)

        # connect button to method
        self.signin_button.clicked.connect(self.signin)
        self.username_textbox.returnPressed.connect(self.signin)
        self.password_textbox.returnPressed.connect(self.signin)

        self.show()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.signin()

    def signin(self):
        username = self.username_textbox.text()
        password = self.password_textbox.text()
        if(username=='admin' and password == 'admin') :
            # create and show main window
            self.hide() # hide the sign in window
            self.home_window = MainWindow()
            self.home_window.show()
        # close current window
            self.close()
        else :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Incorrect credentials")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    signin_form = SignInForm()
    sys.exit(app.exec_())
