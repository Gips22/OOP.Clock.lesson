from PyQt5 import QtCore, QtGui, QtWidgets

from add_note import MyAddWindow
from create import MyMainWindow


class Ui_Dialog(object):
    """Класс сгенерированный QTDesigner. Стартовое окно 'Журнал работ'"""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 402)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 501, 111))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 50, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 110, 501, 301))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 160, 201, 191))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/1.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\naletovaa\\Desktop\\PROJECTS\\QT_journal\\1.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 260, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 180, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "        ЖУРНАЛ РАБОТ"))
        self.pushButton_2.setText(_translate("Dialog", "Дополнить запись"))
        self.pushButton_3.setText(_translate("Dialog", "Создать запись"))


class MyFirstWindow(QtWidgets.QWidget, Ui_Dialog):
    """Мой вспомогательный класс, для дополнения родительского класса Ui_Dialog"""

    def __init__(self):
        """В конструкторе инициализуем setupUi родительского класса,
         а также определяем события нажатия на кнопки"""
        super().__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.openMainWindow)
        self.pushButton_2.clicked.connect(self.openAddNoteWindow)

    def openMainWindow(self):
        """Метод, который срабатывает при нажатии на кнопку 'Создать запись'.
        В нем создаем ЭК, отвечающего за отображение окна create.py и далее работаем уже с ним"""
        self.close()
        self.ui = MyMainWindow(
            parent=self)  # предаем ссылку на self чтобы в окне MainWindow не делать импорт из-за которого выдает ошибку циклического импорта

    def openAddNoteWindow(self):
        """Метод, который срабатывает при нажатии на кнопку 'Дополнить запись'.
        В нем создаем ЭК, отвечающего за отображение окна add_note.py и далее работаем уже с ним"""
        self.close()
        self.ui2 = MyAddWindow(parent=self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()
    ui = MyFirstWindow()
    ui.setupUi(Dialog)
    ui.show()

    sys.exit(app.exec_())  # функция exec запускает loop - цикл отслеживания событий и управления обработчиками событий,
    # пока мы не выйдем из приложения. Когда мы выходим ф-ия возвращает exex код == 0 если успешно вышли, если нет ошибки
