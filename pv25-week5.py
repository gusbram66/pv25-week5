# -*- coding: utf-8 -*-
# Form Validation Program
# Nama: Ida Bagus Brahmanta Jayana
# NIM : F1D022052

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form  
        Form.setObjectName("Form Validation")
        Form.resize(400, 350)  # Sedikit lebih tinggi agar muat label nama

        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(10, 0, 380, 20))
        self.label_title.setObjectName("label_title")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_title.setFont(font)

        self.label_nama_nim = QtWidgets.QLabel(Form)
        self.label_nama_nim.setGeometry(QtCore.QRect(10, 20, 380, 20))
        self.label_nama_nim.setObjectName("label_nama_nim")
        self.label_nama_nim.setAlignment(QtCore.Qt.AlignCenter)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 47, 13))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 47, 13))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 47, 13))
        self.label_3.setObjectName("label_3")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 91, 21))
        self.label_4.setObjectName("label_4")

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText("+62")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 47, 13))
        self.label_5.setObjectName("label_5")

        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 170, 131, 61))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 47, 13))
        self.label_6.setObjectName("label_6")

        self.comboBox_gender = QtWidgets.QComboBox(Form)
        self.comboBox_gender.setGeometry(QtCore.QRect(120, 240, 113, 22))
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItems(["", "Male", "Female"])

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 60, 13))
        self.label_7.setObjectName("label_7")

        self.comboBox_education = QtWidgets.QComboBox(Form)
        self.comboBox_education.setGeometry(QtCore.QRect(120, 270, 200, 22))
        self.comboBox_education.setObjectName("comboBox_education")
        self.comboBox_education.addItems([
            "", "Elementary School", "Junior High School", "Senior High School",
            "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"
        ])

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 310, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_data)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 310, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.clear_fields)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            QtWidgets.QApplication.quit()

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Validation Error")
        msg.setText(message)
        msg.exec_()

    def save_data(self):
        name = self.lineEdit.text()
        email = self.lineEdit_2.text()
        age = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()
        address = self.lineEdit_5.text()
        gender = self.comboBox_gender.currentText()
        education = self.comboBox_education.currentText()

        if name.strip() == "":
            self.show_error("Name is required")
            return
        elif any(char.isdigit() for char in name):
            self.show_error("Name must not contain numbers")
            return
        if email.strip() == "" or "@gmail.com" not in email:
            self.show_error("Please enter a valid Gmail address")
            return
        if age.strip() == "" or not age.isdigit():
            self.show_error("Age must be a number")
            return
        if not phone.startswith("+62") or not phone[1:].isdigit() or len(phone.replace("+", "").strip()) != 13:
            self.show_error("Phone number must start with +62 and be 13 digits")
            return
        if address.strip() == "":
            self.show_error("Address is required")
            return
        if gender == "":
            self.show_error("Gender is required")
            return
        if education == "":
            self.show_error("Education is required")
            return

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("Data saved successfully!")
        msg.exec_()

        self.clear_fields()

    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.setText("+62")
        self.lineEdit_5.clear()
        self.comboBox_gender.setCurrentIndex(0)
        self.comboBox_education.setCurrentIndex(0)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form Validation F1D022052"))
        self.label_title.setText(_translate("Form", "Form Validation Program"))
        self.label_nama_nim.setText(_translate("Form", "Ida Bagus Brahmanta Jayana - F1D022052"))
        self.label.setText(_translate("Form", "Name:"))
        self.label_2.setText(_translate("Form", "Email:"))
        self.label_3.setText(_translate("Form", "Age:"))
        self.label_4.setText(_translate("Form", "Phone Number:"))
        self.label_5.setText(_translate("Form", "Address:"))
        self.label_6.setText(_translate("Form", "Gender:"))
        self.label_7.setText(_translate("Form", "Education:"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_2.setText(_translate("Form", "Clear"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
