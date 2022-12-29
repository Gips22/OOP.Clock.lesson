"""Окно создания новой записи в БД"""
import datetime
from typing import Optional

from PyQt5 import QtCore, QtGui, QtWidgets
from loguru import logger

from db import get_cursor
from messages import create_error, create_unknown_error, create_note_success


logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB")


class Ui_CreateNote(object):
    """Класс сгенерированный QTDesigner. Окно 'Создать запись'"""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 763)
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(60, 550, 443, 70))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(163, 502, 125, 20))
        self.dateTimeEdit.setStyleSheet("\n"
                                        "font: 10pt \"MS Shell Dlg 2\";\n"
                                        "")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 260, 261, 22))
        self.comboBox_2.setStyleSheet("\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(250, 182, 73, 20))
        self.checkBox.setStyleSheet("\n"
                                    "font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(60, 630, 443, 70))
        self.textBrowser_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 660, 261, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(60, 230, 443, 70))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 340, 261, 22))
        self.comboBox_3.setStyleSheet("\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(60, 470, 443, 70))
        self.textBrowser_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(339, 182, 66, 20))
        self.checkBox_2.setStyleSheet("\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.textBrowser_8 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_8.setGeometry(QtCore.QRect(60, 310, 443, 70))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 420, 261, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(296, 501, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 580, 261, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.fioBox = QtWidgets.QComboBox(Dialog)
        self.fioBox.setGeometry(QtCore.QRect(160, 100, 261, 22))
        self.fioBox.setStyleSheet("\n"
                                  "font: 75 10pt \"MS Shell Dlg 2\";")
        self.fioBox.setObjectName("fioBox")
        self.fioBox.addItem("")
        self.fioBox.addItem("")
        self.fioBox.addItem("")
        self.fioBox.addItem("")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 150, 443, 70))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_9 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_9.setGeometry(QtCore.QRect(60, 390, 443, 70))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(-90, 0, 701, 811))
        self.widget.setStyleSheet("background-color: rgb(5, 155, 255);")
        self.widget.setObjectName("widget")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 20, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("home.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(480, 710, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 730, 321, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(60, 70, 443, 70))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(162, 182, 72, 20))
        self.checkBox_3.setStyleSheet("\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.widget.raise_()
        self.textBrowser_5.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.fioBox.raise_()
        self.textBrowser_4.raise_()
        self.lineEdit_4.raise_()
        self.textBrowser_9.raise_()
        self.textBrowser_8.raise_()
        self.textBrowser_7.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_3.raise_()
        self.comboBox_3.raise_()
        self.textBrowser_3.raise_()
        self.pushButton_2.raise_()
        self.dateTimeEdit.raise_()
        self.comboBox_2.raise_()
        self.checkBox_3.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser_4.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">* ССЫЛКА НА ФАЙЛ</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Не выбрано"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Тема1"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Тема2"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Тема3"))
        self.checkBox.setText(_translate("Dialog", "2"))
        self.textBrowser_7.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">КОММЕНТАРИИ</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">* ТЕМА</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Не выбрано"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Часть1"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Часть2"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "Часть3"))
        self.textBrowser_5.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">* ВРЕМЯ СТАРТА РАБОТ</span></p></body></html>"))
        self.checkBox_2.setText(_translate("Dialog", "3"))
        self.textBrowser_8.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">* ЧАСТЬ</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "текущая дата/время"))
        self.fioBox.setItemText(0, _translate("Dialog", "Не выбрано"))
        self.fioBox.setItemText(1, _translate("Dialog", "Иванов Иван Иванович"))
        self.fioBox.setItemText(2, _translate("Dialog", "Петров Петр Петрович"))
        self.fioBox.setItemText(3, _translate("Dialog", "Семенов Семен Иванович"))
        self.textBrowser_2.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">* ТИП РАБОТ</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">ЭЛЕМЕНТ</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "ВЕРНУТЬСЯ"))
        self.pushButton.setText(_translate("Dialog", "СОЗДАТЬ"))
        self.label_2.setText(_translate("Dialog", "Поля со * являются обязательными для заполнения"))
        self.textBrowser.setHtml(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">* ОТВЕТСТВЕННЫЙ</span></p></body></html>"))
        self.checkBox_3.setText(_translate("Dialog", "1"))


class MyMainWindow(QtWidgets.QWidget, Ui_CreateNote):
    """Мой вспомогательный класс, для дополнения родительского класса Ui_CreateNote"""
    def __init__(self, parent):
        """В конструкторе инициализуем setupUi родительского класса,
        а также определяем события нажатия на кнопки"""
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.show()

        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(lambda: self.dateTimeEdit.setDateTime(datetime.datetime.now()))
        self.pushButton_3.clicked.connect(self.back_home)

        self.fio = None
        self.type1 = None
        self.type2 = None
        self.type3 = None
        self.theme = None
        self.part = None
        self.element = None
        self.time_start = None
        self.file_start = None
        self.comments_start = None

    def back_home(self):
        """Метод, который срабатываем при нажатии на кнопку 'Домой'.
        Закрывает текущее окно и открывает стартовое окно"""
        self.close()
        self.parent.show()

    def on_click(self):
        """Метод, который срабатывает при нажатии на кнопку 'Создать'.
        Делает валидацию введенных данных, проверяет все ли обязательные поля заполнены.
        Если нет-выдает ошибку. Если все ок - сохраняет запись в БД (через метод check_finally_to_db)
        и показывает модальное окно 'Запись успешно создана'"""
        self.cursor = get_cursor()
        self.check_finally_to_db()

    def check_finally_to_db(self):
        """Функция финально проверяет заполненность всех обязательных полей и сохраняет в БД,
        если все заполнено. Если нет - выдает модальное окно с ошибкой, в зависимости от ее типа"""
        if any(x == None for x in
               (self._check_fio_field(), self._check_type_work_field(), self._check_field_theme_work(),
                self._check_field_part(), self._check_field_time_start(), self._check_field_file_start())):
            return create_error()

        try:
            self._check_field_element()
            self._check_field_comments_start()
            self.insert_data = (
                "insert into works "
                "(fio, type, tema, part, element, time, link_start, comment_start) "
                "values (%s, %s, %s, %s, %s, %s, %s, %s)")
            self.cursor.execute(self.insert_data,
                                (self.fio, self.type_rezult, self.theme, self.part, self.element,
                                 self.time_start,
                                 self.file_start,
                                 self.comments_start))
        except Exception as ex:
            create_unknown_error(ex)
            logger.error(ex)
        else:
            create_note_success()
            self.close()
            self.parent.show()

    def _check_fio_field(self) -> Optional[str]:
        """Проверям заполнил ли пользователь обязательное поле 'Ответственный'"""
        self.fio = self.fioBox.currentText()
        if self.fio == "Не выбрано":
            self.fio = None
        return self.fio

    def _check_type_work_field(self) -> Optional[str]:
        """Проверям заполнил ли пользователь обязательное поле 'Тип работ'"""
        self.type1 = self.checkBox.isChecked()
        self.type2 = self.checkBox_2.isChecked()
        self.type3 = self.checkBox_3.isChecked()
        if not self.type1 and not self.type2 and not self.type3:
            return None
        self.type_rezult = []
        if self.type1:
            self.type_rezult.append(self.checkBox.text())
        if self.type2:
            self.type_rezult.append(self.checkBox_2.text())
        if self.type3:
            self.type_rezult.append(self.checkBox_3.text())
        self.type_rezult = ', '.join(self.type_rezult)
        return self.type_rezult

    def _check_field_theme_work(self) -> Optional[str]:
        """Проверям заполнил ли пользователь обязательное поле 'Тема'"""
        self.theme = self.comboBox_2.currentText()
        if self.theme == "Не выбрано":
            self.theme = None
        return self.theme

    def _check_field_part(self) -> Optional[str]:
        """Проверям заполнил ли пользователь обязательное поле 'Часть'"""
        self.part = self.comboBox_3.currentText()
        if self.part == "Не выбрано":
            self.part = None
        return self.part

    def _check_field_element(self) -> Optional[str]:
        """Проверям заполнил ли пользователь необязательное поле 'Элемент'"""
        self.element = self.lineEdit_5.text()
        if not self.element:
            self.element = None
        return self.element

    def _check_field_time_start(self) -> Optional[str]:
        """Проверям заполнил ли пользователь обязательное поле 'Время старта работ'"""
        self.time_start = self.dateTimeEdit.dateTime().toString('dd-MM-yyyy hh:mm')
        if self.time_start == "01-01-2000 00:00":
            self.time_start = None
        return self.time_start

    def _check_field_file_start(self) -> Optional[str]:
        """Проверям заполнил ли пользователь обязательное поле 'Ссылка на файл'"""
        self.file_start = self.lineEdit_4.text()
        if not self.file_start:
            self.file_start = None
        return self.file_start

    def _check_field_comments_start(self) -> Optional[str]:
        """Проверям заполнил ли пользователь обязательное поле 'Комментарий'"""
        self.comments_start = self.lineEdit_3.text()
        if not self.comments_start:
            self.comments_start = None
        return self.comments_start
