# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZSQ_login(object):
    def setupUi(self, ZSQ_login):
        ZSQ_login.setObjectName("ZSQ_login")
        ZSQ_login.resize(342, 378)
        ZSQ_login.setMinimumSize(QtCore.QSize(342, 378))
        ZSQ_login.setMaximumSize(QtCore.QSize(342, 450))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        ZSQ_login.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icone (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ZSQ_login.setWindowIcon(icon)
        ZSQ_login.setStyleSheet("#ZSQ_login{\n"
"background-image:url(/home/pi/Documents/projeto tcc/ZSQ/ZSQ/imagens/estrela3.png);\n"
#/home/pi/Documents/projeto tcc/ZSQ/ZSQ/imagens
"transform: scaleX(-1);\n"
"\n"
"}\n"
"\n"
"#txtlogo{\n"
"background-repeat:no-repeat;\n"
"background-size: auto;\n"
"background-image:url(/home/pi/Documents/projeto tcc/ZSQ/ZSQ/imagens/Logo_1.png);\n"
"\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ZSQ_login)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(126, 300, 47, 13))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(150, 280, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("border-radius:15px;\n"
"    \n"
"    background-color: rgb(94, 197, 230);\n"
"    \n"
"    border-style:solid;\n"
"\n"
"    font-weight:bold;\n"
"    color: rgb(255, 255, 255);\n"
"")
        self.btn_login.setObjectName("btn_login")
        self.btn_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cadastro.setGeometry(QtCore.QRect(50, 280, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_cadastro.setFont(font)
        self.btn_cadastro.setStyleSheet("border-radius:15px;\n"
"    \n"
"    background-color: rgb(94, 197, 230);\n"
"    \n"
"    border-style:solid;\n"
"\n"
"    font-weight:bold;\n"
"    color: rgb(255, 255, 255);\n"
"")
        self.btn_cadastro.setObjectName("btn_cadastro")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 291, 461))
        self.frame.setStyleSheet(" background-color:#0055aa;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtlogo = QtWidgets.QLabel(self.frame)
        self.txtlogo.setGeometry(QtCore.QRect(60, 20, 300, 110))
        self.txtlogo.setMinimumSize(QtCore.QSize(300, 110))
        self.txtlogo.setMaximumSize(QtCore.QSize(300, 110))
        self.txtlogo.setText("")
        self.txtlogo.setObjectName("txtlogo")
        self.usuarioCPF = QtWidgets.QLineEdit(self.centralwidget)
        self.usuarioCPF.setGeometry(QtCore.QRect(57, 158, 171, 20))
        self.usuarioCPF.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"border:none;\n"
"color:white;")
        self.usuarioCPF.setMaxLength(14)
        self.usuarioCPF.setFrame(True)
        self.usuarioCPF.setCursorPosition(0)
        self.usuarioCPF.setObjectName("usuarioCPF")
        self.lbl_usuario = QtWidgets.QLabel(self.centralwidget)
        self.lbl_usuario.setEnabled(True)
        self.lbl_usuario.setGeometry(QtCore.QRect(57, 130, 60, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_usuario.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.lbl_senha = QtWidgets.QLabel(self.centralwidget)
        self.lbl_senha.setGeometry(QtCore.QRect(57, 200, 49, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_senha.setFont(font)
        self.lbl_senha.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_senha.setObjectName("lbl_senha")
        self.senhaUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.senhaUsuario.setGeometry(QtCore.QRect(57, 230, 171, 20))
        self.senhaUsuario.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"border:none;\n"
"color:white;\n"
"")
        self.senhaUsuario.setInputMask("")
        self.senhaUsuario.setMaxLength(32767)
        self.senhaUsuario.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senhaUsuario.setObjectName("senhaUsuario")
        self.frame.raise_()
        self.label_3.raise_()
        self.btn_login.raise_()
        self.btn_cadastro.raise_()
        self.usuarioCPF.raise_()
        self.lbl_usuario.raise_()
        self.lbl_senha.raise_()
        self.senhaUsuario.raise_()
        ZSQ_login.setCentralWidget(self.centralwidget)

        self.retranslateUi(ZSQ_login)
        QtCore.QMetaObject.connectSlotsByName(ZSQ_login)

    def retranslateUi(self, ZSQ_login):
        _translate = QtCore.QCoreApplication.translate
        ZSQ_login.setWindowTitle(_translate("ZSQ_login", "ZSQ - Login"))
        self.btn_login.setText(_translate("ZSQ_login", "Logar"))
        self.btn_cadastro.setText(_translate("ZSQ_login", "Cadastre-se"))
        self.usuarioCPF.setInputMask(_translate("ZSQ_login", "000.000.000-00"))
        self.lbl_usuario.setText(_translate("ZSQ_login", "Usuário"))
        self.lbl_senha.setText(_translate("ZSQ_login", "Senha"))