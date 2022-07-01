from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QIcon
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QPlainTextEdit, QListView
from PyQt5 import uic  # Импортируем uic
from random import randint
import sqlite3


class Example(QWidget):
    def __init__(self):
        super().__init__()
        # Загружаем дизайн
        uic.loadUi('project_ui.ui', self)
        self.start.clicked.connect(self.start_test)
        self.reset.clicked.connect(self.reset_test)

        # Списки лучших игроков, подключение базы данных
        self.con = sqlite3.connect('data.sqlite')
        self.cursor = self.con.cursor()

        # Поиск нужной информации из базы данных
        self.result = self.cursor.execute('''SELECT Playername, Playernick, time, country FROM projectPRO
                                             WHERE time != 'None' ''').fetchall()

        # Вывод нужных для нас элементов из базы данных в QPlainTextEdit
        for elem in self.result:
            self.spisok.appendPlainText(f'Имя: {elem[0]}')
            self.spisok.appendPlainText(f'Nick: {elem[1]}')
            self.spisok.appendPlainText(f'Время: {elem[2]} сек')
            self.spisok.appendPlainText(f'Страна: {elem[3]}')
            self.spisok.appendPlainText('---------')

        # Прячем все элементы, которые не должны присутствовать на стартовом экране
        self.c1.hide(), self.c2.hide(), self.c3.hide(), self.c4.hide(), self.c5.hide()
        self.c6.hide(), self.c7.hide(), self.c8.hide(), self.c9.hide(), self.c10.hide()
        self.c11.hide(), self.c12.hide(), self.c13.hide(), self.c14.hide(), self.c15.hide()
        self.c16.hide(), self.c17.hide(), self.c18.hide(), self.c19.hide(), self.c20.hide()
        self.c21.hide(), self.c22.hide(), self.c23.hide(), self.c24.hide(), self.c25.hide()
        self.c26.hide(), self.c27.hide(), self.c28.hide(), self.c29.hide(), self.c30.hide()
        self.silver.hide(), self.gold.hide(), self.bronze.hide(), self.silver_2.hide()
        self.bronze_2.hide(), self.gold_2.hide(), self.need1.hide(), self.need2.hide()

        # Вызов TXT файла для записи информации
        self.zapis.clicked.connect(self.txteditor)

        # Реализация секундомера
        self.count = 0
        self.flag = False  # Прекращение отсчёта
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        self.init_UI()  # Подключаем initUI для добавления функции

    # Редактирование txt файла
    def txteditor(self):
        con = sqlite3.connect('data.sqlite')

        cursor = con.cursor()

        cursor.execute(
            f"INSERT INTO projectPRO(playername, Time) VALUES('{self.urname.text()}', {str(self.count / 10)})")
        con.commit()

        if self.timecheck.text() == '' and self.urname.text() == '':  # Проверка все ли пункты соблюдены
            self.need1.show()
            self.need2.show()
        elif self.timecheck.text() == '':
            self.need2.hide()
            self.need1.show()
        elif self.urname.text() == '':
            self.need2.show()
            self.need1.hide()
        else:
            self.need1.hide(), self.need2.hide()
            self.file_edit = open('Результаты.txt', 'a+')  # Открытие txt файла и возможность его редактировать
            self.file_edit.write(
                f'\nИмя: {self.urname.text()} \nВозраст: {self.urage.text()} лет \nВремя: {str(self.count / 10)} сек \n-----')  # Запись в файл нужных для нас данных
            self.file_edit.close()

    # Изменение названия и иконки приложения
    def init_UI(self):
        self.setWindowTitle('Aim Training')
        self.setWindowIcon(QIcon('img/logo.png'))

    # Функция отвечающая за вывод времени секундомера
    def showTime(self):
        if self.flag:  # Проверка работы секундомера
            self.count += 1
        text = str(self.count / 10)
        self.labeltimer.setText(text)

    # Функция, которая начинает тренировку
    def start_test(self):
        self.count = 0
        self.labeltimer.setText(str(self.count))  # Вывод времени секундомера
        self.flag = True  # Отсчёт секундомера
        self.gamemode.hide()
        self.c1.move(randint(400, 1700), randint(100, 1100))
        self.c1.show()
        self.c1.clicked.connect(self.c2btn)  # Подключение к началу цикла тренировки

    # Последовательное появление кнопок в зависимости от нажатой кнопки до этого в течении 30 раз
    def c2btn(self):
        self.c2.move(randint(400, 1700), randint(100, 1100))
        self.c2.show()
        self.c1.hide()
        self.c2.clicked.connect(self.c3btn)

    def c3btn(self):
        self.c3.move(randint(400, 1700), randint(100, 1100))
        self.c3.show()
        self.c2.hide()
        self.c3.clicked.connect(self.c4btn)

    def c4btn(self):
        self.c4.move(randint(400, 1700), randint(100, 1100))
        self.c4.show()
        self.c3.hide()
        self.c4.clicked.connect(self.c5btn)

    def c5btn(self):
        self.c5.move(randint(400, 1700), randint(100, 1100))
        self.c5.show()
        self.c4.hide()
        self.c5.clicked.connect(self.c6btn)

    def c6btn(self):
        self.c6.move(randint(400, 1700), randint(100, 1100))
        self.c6.show()
        self.c5.hide()
        self.c6.clicked.connect(self.c7btn)

    def c7btn(self):
        self.c7.move(randint(400, 1700), randint(100, 1100))
        self.c7.show()
        self.c6.hide()
        self.c7.clicked.connect(self.c8btn)

    def c8btn(self):
        self.c8.move(randint(400, 1700), randint(100, 1100))
        self.c8.show()
        self.c7.hide()
        self.c8.clicked.connect(self.c9btn)

    def c9btn(self):
        self.c9.move(randint(400, 1700), randint(100, 1100))
        self.c8.hide()
        self.c9.show()
        self.c9.clicked.connect(self.c10btn)

    def c10btn(self):
        self.c10.move(randint(400, 1700), randint(100, 1100))
        self.c10.show()
        self.c9.hide()
        self.c10.clicked.connect(self.c11btn)

    def c11btn(self):
        self.c11.move(randint(400, 1700), randint(100, 1100))
        self.c11.show()
        self.c10.hide()
        self.c11.clicked.connect(self.c12btn)

    def c12btn(self):
        self.c12.move(randint(400, 1700), randint(100, 1100))
        self.c12.show()
        self.c11.hide()
        self.c12.clicked.connect(self.c13btn)

    def c13btn(self):
        self.c13.move(randint(400, 1700), randint(100, 1100))
        self.c13.show()
        self.c12.hide()
        self.c13.clicked.connect(self.c14btn)

    def c14btn(self):
        self.c14.move(randint(400, 1700), randint(100, 1100))
        self.c14.show()
        self.c13.hide()
        self.c14.clicked.connect(self.c15btn)

    def c15btn(self):
        self.c15.move(randint(400, 1700), randint(100, 1100))
        self.c15.show()
        self.c14.hide()
        self.c15.clicked.connect(self.c16btn)

    def c16btn(self):
        self.c16.move(randint(400, 1700), randint(100, 1100))
        self.c16.show()
        self.c15.hide()
        self.c16.clicked.connect(self.c17btn)

    def c17btn(self):
        self.c17.move(randint(400, 1700), randint(100, 1100))
        self.c17.show()
        self.c16.hide()
        self.c17.clicked.connect(self.c18btn)

    def c18btn(self):
        self.c18.move(randint(400, 1700), randint(100, 1100))
        self.c18.show()
        self.c17.hide()
        self.c18.clicked.connect(self.c19btn)

    def c19btn(self):
        self.c19.move(randint(400, 1700), randint(100, 1100))
        self.c19.show()
        self.c18.hide()
        self.c19.clicked.connect(self.c20btn)

    def c20btn(self):
        self.c20.move(randint(400, 1700), randint(100, 1100))
        self.c20.show()
        self.c19.hide()
        self.c20.clicked.connect(self.c21btn)

    def c21btn(self):
        self.c21.move(randint(400, 1700), randint(100, 1100))
        self.c21.show()
        self.c20.hide()
        self.c21.clicked.connect(self.c22btn)

    def c22btn(self):
        self.c22.move(randint(400, 1700), randint(100, 1100))
        self.c22.show()
        self.c21.hide()
        self.c22.clicked.connect(self.c23btn)

    def c23btn(self):
        self.c23.move(randint(400, 1700), randint(100, 1100))
        self.c23.show()
        self.c22.hide()
        self.c23.clicked.connect(self.c24btn)

    def c24btn(self):
        self.c24.move(randint(400, 1700), randint(100, 1100))
        self.c24.show()
        self.c23.hide()
        self.c24.clicked.connect(self.c25btn)

    def c25btn(self):
        self.c25.move(randint(400, 1700), randint(100, 1100))
        self.c25.show()
        self.c24.hide()
        self.c25.clicked.connect(self.c26btn)

    def c26btn(self):
        self.c26.move(randint(400, 1700), randint(100, 1100))
        self.c26.show()
        self.c25.hide()
        self.c26.clicked.connect(self.c27btn)

    def c27btn(self):
        self.c27.move(randint(400, 1700), randint(100, 1100))
        self.c27.show()
        self.c26.hide()
        self.c27.clicked.connect(self.c28btn)

    def c28btn(self):
        self.c28.move(randint(400, 1700), randint(100, 1100))
        self.c28.show()
        self.c27.hide()
        self.c28.clicked.connect(self.c29btn)

    def c29btn(self):
        self.c29.move(randint(400, 1700), randint(100, 1100))
        self.c29.show()
        self.c28.hide()
        self.c29.clicked.connect(self.c30btn)

    def c30btn(self):
        self.c30.move(randint(400, 1700), randint(100, 1100))
        self.c30.show()
        self.c29.hide()
        self.c30.clicked.connect(self.information)  # Подключение информационного блока

    # Информационный блок, вывод основной информации
    def information(self):
        self.c30.hide()
        self.timecheck.setText(f'Ваш результат: {str(self.count / 10)} сек')  # Вывод результата по времени
        self.flag = False  # Остановка отсчёта

        # Вывод формальных результатов тренировки
        if (self.count / 10) < 23:
            self.rating.setText('Алмаз')
            self.gold.show()
            self.gold_2.show()
        elif (self.count / 10) < 26:
            self.rating.setText('Золото')
            self.silver.show()
            self.silver_2.show()
        elif (self.count / 10) > 26:
            self.rating.setText('Бронза')
            self.bronze.show()
            self.bronze_2.show()

    # Кнопка сброса тренировки с полным обнулением
    def reset_test(self):
        self.c1.hide(), self.c2.hide(), self.c3.hide(), self.c4.hide()
        self.c5.hide(), self.c6.hide(), self.c7.hide(), self.c8.hide()
        self.c9.hide(), self.c10.hide(), self.c11.hide(), self.c12.hide()
        self.c13.hide(), self.c14.hide(), self.c15.hide(), self.c16.hide()
        self.c17.hide(), self.c18.hide(), self.c19.hide(), self.c20.hide()
        self.c21.hide(), self.c22.hide(), self.c23.hide(), self.c24.hide()
        self.c25.hide(), self.c26.hide(), self.c27.hide()
        self.c28.hide(), self.c29.hide(), self.c30.hide(), self.silver.hide(),
        self.silver_2.hide(), self.gold.hide(), self.gold_2.hide(), self.bronze.hide(),
        self.bronze_2.hide(), self.rating.clear(), self.timecheck.clear()

        # Обнуление времени секундомера
        self.c1.show()
        self.flag = True
        self.count = 0
        self.labeltimer.setText(str(self.count))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
