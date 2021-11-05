import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from controller import PyCalcCtrl
from model import evaluateExpression
__version__ = '0.2'
__author__ = 'Oleksandr Kopiievyi'


#  Створюємо дочірній класс від QMainWindow для сетапа інтерфейсу калькулятора
class PyCalcUi(QMainWindow):
    def __init__(self):
        super().__init__()
        #  Параметри вікна
        self.setWindowTitle('PyCalculator for Beetroot')
        self.setFixedSize(300, 300)
        #  Центральний віджет (так як ми наслідуємось від QMainWindow, то віджет потрібен для слугування
        #  як батьківський об'єкт для решти графічних компонентів)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        #  Створюємо дисплей та кнопки
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        #  Створюємо віджет дисплею
        self.display = QLineEdit()
        #  Параметри дисплею
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        #  Добавлення дисплею до загального лейауту
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        #  Створюємо кнопки
        self.buttons = {}
        buttonsLayout = QGridLayout()
        #  Текст кнопок та їх позиція на QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4)}
        #  Створюємо кнопки та добавляєм їх до лейауту гріду
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        #  Добавлення buttons лейауту до загального лейауту
        self.generalLayout.addLayout(buttonsLayout)

    #  Для апдейту інформації що показана на динсплеї
    def setDisplayText(self, text):
        # для того щоб ініціалізувати або змінювати текст
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        # для виводу тексту
        return self.display.text()

    def clearDisplay(self):
        # для його зтирання
        self.setDisplayText("")


#  Код користувача
def main():
    # Створюємо об'єкт QApplication
    pycalc = QApplication(sys.argv)
    #  Вивід інтерфейсу
    view = PyCalcUi()
    view.show()
    #  Створення об'єтку моделі та контролера
    model = evaluateExpression
    PyCalcCtrl(view=view, model=model)
    #  Запуск користувацького циклу
    sys.exit(pycalc.exec())


if __name__ == '__main__':
    main()
