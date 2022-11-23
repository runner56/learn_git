import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)  # Загружаем дизайн
        self.drawBtn.clicked.connect(self.drawf)
        self.qp = QPainter()
        self.flag = False

    def drawf(self):
        self.flag = True
        self.update()
        # self.flag = False

    def draw(self):
        # red = randint(0, 256)
        # green = randint(0, 256)
        # blue = randint(0, 256)
        blue = 0
        green = red = 255
        self.qp.setPen(QPen(QColor(red, green, blue)))
        self.qp.setBrush(QBrush(QColor(red, green, blue)))
        x, y = randint(100, 700), randint(100, 500)
        d = randint(10, 100)
        self.qp.drawEllipse(x, y, x + d, y + d)

    def paintEvent(self, e):
        try:
            if self.flag:
                self.qp.begin(self)
                self.draw()
                self.qp.end()
        except Exception as e:
            print(e)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


