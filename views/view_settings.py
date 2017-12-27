# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(763, 293)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 6, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 65, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.server_host = QtGui.QLineEdit(Form)
        self.server_host.setGeometry(QtCore.QRect(110, 165, 161, 31))
        self.server_host.setText(_fromUtf8(""))
        self.server_host.setObjectName(_fromUtf8("server_host"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.server_port = QtGui.QLineEdit(Form)
        self.server_port.setGeometry(QtCore.QRect(20, 160, 81, 31))
        self.server_port.setText(_fromUtf8(""))
        self.server_port.setObjectName(_fromUtf8("server_port"))
        self.server_protocol = QtGui.QComboBox(Form)
        self.server_protocol.setGeometry(QtCore.QRect(20, 126, 251, 31))
        self.server_protocol.setObjectName(_fromUtf8("server_protocol"))
        self.server_protocol.addItem(_fromUtf8(""))
        self.server_protocol.addItem(_fromUtf8(""))
        self.button_save = QtGui.QPushButton(Form)
        self.button_save.setGeometry(QtCore.QRect(20, 201, 141, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_save.setFont(font)
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.field_required = QtGui.QLabel(Form)
        self.field_required.setGeometry(QtCore.QRect(300, 131, 161, 51))
        self.field_required.setText(_fromUtf8(""))
        self.field_required.setObjectName(_fromUtf8("field_required"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TPV", None))
        self.label.setText(_translate("Form", "Configuración", None))
        self.label_2.setText(_translate("Form", "Configuración del Punto de Venta (Sólo Administrador)", None))
        self.server_host.setPlaceholderText(_translate("Form", "Host", None))
        self.label_3.setText(_translate("Form", "Servidor ERP", None))
        self.server_port.setPlaceholderText(_translate("Form", "Puerto", None))
        self.server_protocol.setItemText(0, _translate("Form", "http", None))
        self.server_protocol.setItemText(1, _translate("Form", "https", None))
        self.button_save.setText(_translate("Form", "Guardar", None))

