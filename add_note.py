from PyQt5 import QtCore, QtGui, QtWidgets

from choose_work import MyChooseWork
import messages
from db import get_cursor


class Ui_add_note(object):
    """Класс сгенерированный QTDesigner. Окно 'Дополнить запись'"""

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 453)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(-20, -50, 631, 531))
        self.textBrowser.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.textBrowser.setObjectName("textBrowser")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(60, 80, 381, 281))
        self.calendarWidget.setStyleSheet("alternate-background-color: rgb(85, 170, 255);\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "selection-background-color: rgb(170, 255, 0);\n"
                                          "border-color: rgb(170, 85, 255);\n"
                                          "border-top-color: rgb(170, 170, 255);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(5, 155, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(5, 155, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "ПЕРЕЙТИ"))
        self.label.setText(_translate("Dialog", "Выберите дату старта работ"))
        self.pushButton_4.setText(_translate("Dialog", "ВЕРНУТЬСЯ"))


class MyAddWindow(QtWidgets.QWidget, Ui_add_note):
    """Мой класс для дополнения родительского класса Ui_add_note"""

    def __init__(self, parent):
        """В конструкторе инициализуем setupUi родительского класса,
        а также определяем события для кнопок"""
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.show()

        self.pushButton_3.clicked.connect(self.openChooseWorkWindow)
        self.pushButton_4.clicked.connect(self.back_home)

    def back_home(self):
        """При клике на кнопку 'Вернуться' - закрывается текущее окно и открывается первоначальное"""
        self.close()
        self.parent.show()

    def openChooseWorkWindow(self):
        """Функция срабатывает при нажатии на кнопку 'перейти', делает запрос в БД
         и проверяет были ли записи в выбранную дату.
         Если были - перебрасывает нас на окно с записями choose_work.py,
         если нет - показывает модальное окно с информацией"""

        cursor = get_cursor()
        date_choose = self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
        query = f"select * from works where " \
                f"time >= '{date_choose} 00:00:00' and " \
                f"time <= '{date_choose} 23:59:59' and " \
                f"time_finish is null;"
        cursor.execute(query)
        rez = cursor.fetchall()
        if len(rez) == 0:
            messages.warning_date()
        else:
            self.ui3 = MyChooseWork(date_choose=date_choose)
