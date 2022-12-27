from PyQt5.QtWidgets import QMessageBox

def complete_success():
    msg1 = QMessageBox()
    msg1.setWindowTitle('Выполнено')
    msg1.setText('Запись успешна дополнена!')
    msg1.setIcon(QMessageBox.Information)
    x = msg1.exec_()

def warning_window():
    msg1 = QMessageBox()
    msg1.setWindowTitle('Предупреждение!')
    msg1.setText('Вы не заполнили обязательные поля ни в одной записи.')
    msg1.setIcon(QMessageBox.Warning)
    x = msg1.exec_()


def error_message(ex):
    msg1 = QMessageBox()
    msg1.setWindowTitle('Ошибка!')
    msg1.setText('Произошла ошибка в ходе добавления записи в БД', ex)
    msg1.setIcon(QMessageBox.Critical)
    x = msg1.exec_()

def warning_date():
    msg = QMessageBox()
    msg.setWindowTitle('Предупреждение')
    msg.setText("За выбранную дату нет незавершенных работ. Выберите другую.")
    msg.setIcon(QMessageBox.Warning)

    x = msg.exec_()

def create_error():
    msg = QMessageBox()
    msg.setWindowTitle('Предупреждение')
    msg.setText("Вы не заполнили некоторые обязательные поля")
    msg.setIcon(QMessageBox.Warning)

    x = msg.exec_()

def create_unknown_error(ex):
    msg1 = QMessageBox()
    msg1.setWindowTitle('Ошибка')
    msg1.setText(str(ex))
    msg1.setIcon(QMessageBox.Critical)
    x = msg1.exec_()

def create_note_success():
    msg1 = QMessageBox()
    msg1.setWindowTitle('Выполнено')
    msg1.setText('Запись успешно создана!')
    msg1.setIcon(QMessageBox.Information)
    x = msg1.exec_()


