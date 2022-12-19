import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from messages import *
import db


class Ui_choose_work(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(731, 578)
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, -30, 891, 841))
        self.textBrowser_2.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 520, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(153, 229, 0);\n"
                                        "background-color: rgb(0, 170, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(50, 70, 641, 241))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 20, 153, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 330, 258, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 380, 631, 121))
        self.tableWidget_2.setRowCount(3)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        self.textBrowser_2.raise_()
        self.pushButton_4.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget_2.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_4.setText(_translate("Dialog", "Сохранить"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "id"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Ответственный"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Тип работы"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Тема работы"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "Элемент"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "Время начала работы"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        self.label.setText(_translate("Dialog", "Исходные данные"))
        self.label_2.setText(_translate("Dialog", "Заполните финальные данные"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Время завершения"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Ссылка на файл"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Комментарий"))


class MyChooseWork(QtWidgets.QWidget, Ui_choose_work):
    def __init__(self, date_choose=None):
        super().__init__()
        self.date_choose = date_choose
        self.setupUi(self)
        self.show()

        self.create_windgets()
        self.pushButton_4.clicked.connect(self.insertData)

    def create_windgets(self):
        """Тут создаем виджеты в ячейках с datetime, а также создаем в цикле атрибуты, чтобы
                в дальнейшем можно было обращаться к ним для сохранения в БД"""
        column = 0
        self.time_list = []  # список с атрибутами row time
        for i in range(self.tableWidget_2.columnCount()):
            setattr(self, "A" + str(i), QtWidgets.QDateTimeEdit())
            self.tableWidget_2.setCellWidget(0, column, self.__dict__["A" + str(i)])
            self.time_list.append(self.__dict__["A" + str(i)])
            column += 1
        self.loadData()  # вызываем метод для работы с БД именно отсюда, а не из __init__, так как иначе данные не загрузятся в таблицу

    def loadData(self):
        cursor = db.get_cursor()

        query = f"select * from works where time >= '{self.date_choose} 00:00:00' and time <= '{self.date_choose} 23:59:59' and time_finish is null;"
        cursor.execute(query)
        self.rez = cursor.fetchall()
        self.tableWidget.setColumnCount(len(self.rez))
        self.tableWidget_2.setColumnCount(len(self.rez))

        tablecol = 0
        try:
            for row in self.rez:
                self.tableWidget.setItem(0, tablecol, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(1, tablecol, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(2, tablecol, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(3, tablecol, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tableWidget.setItem(4, tablecol, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tableWidget.setItem(5, tablecol, QtWidgets.QTableWidgetItem(str(row[5])))
                self.tableWidget.setItem(6, tablecol, QtWidgets.QTableWidgetItem(str(row[6])))
                tablecol += 1
        except Exception as ex:
            print(ex)

    def insertData(self):
        cursor = db.get_cursor()
        column = self.tableWidget_2.columnCount()

        self.link_list = [self.tableWidget_2.item(1, col).text() if self.tableWidget_2.item(1, col) != None else None
                          for col in range(column)]
        self.comment_list = [self.tableWidget_2.item(2, col).text() if self.tableWidget_2.item(2, col) != None else None
                             for col in range(column)]

        """Проверка на заполненность всех обязательных полей хотя бы в одной записе"""
        Flag = False
        for i in range(self.tableWidget_2.columnCount()):
            if int(self.time_list[i].dateTime().toString('dd-MM-yyyy hh:mm')[6:10]) < 2022 or not self.link_list[i]:
                continue
            else:
                Flag = True
        if not Flag:
            warning_window()

        """После того, как мы нашли хотя бы 1 запись в полностью заполненными полями, проверяем какую именно и сохраняем результат в БД"""
        for i in range(self.tableWidget_2.columnCount()):
            if int(self.time_list[i].dateTime().toString('dd-MM-yyyy hh:mm')[6:10]) < 2022 or not self.link_list[i]:
                continue
            else:
                if self.comment_list[i]:
                    try:
                        query_insert_time = "update works set time_finish = %s, link_finish = %s, comment_finish = %s  where id = %s;"
                        cursor.execute(query_insert_time, (
                            self.time_list[i].dateTime().toString('dd-MM-yyyy hh:mm'), self.link_list[i],
                            self.comment_list[i], self.rez[i][0]))
                    except Exception as ex:
                        error_message(ex)
                    else:
                        complete_success()
                        self.close()

                else:
                    try:
                        query_insert_time = "update works set time_finish = %s, link_finish = %s where id = %s;"
                        cursor.execute(query_insert_time, (
                            self.time_list[i].dateTime().toString('dd-MM-yyyy hh:mm'), self.link_list[i],
                            self.rez[i][0]))
                    except Exception as ex:
                        error_message(ex)
                    else:
                        complete_success()
                        self.close()


# def main():
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_choose_work()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
