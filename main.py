import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)  # Загружаем дизайн


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())



#
#
# import sys
# from PyQt5.QtWidgets import QWidget, QApplication
# from PyQt5.QtCore import Qt, QPoint
# from PyQt5.QtGui import QPainter, QPolygon, QColor, QBrush, QPen
# from random import randint
#
#
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(300, 300, 500, 500)
#         self.setWindowTitle("")
#         self.qp = QPainter()
#         self.flag = False
#         self.status = None
#         self.coords = [100, 100]
#         self.setMouseTracking(True)
#
#     def drawf(self):
#         self.flag = True
#         self.update()
#
#     def paintEvent(self, e):
#         try:
#             if self.flag:
#                 self.qp.begin(self)
#                 self.draw()
#                 self.qp.end()
#         except Exception as e:
#             print(e)
#
#     def draw(self):
#         a, b = randint(20, 100), randint(20, 100)
#         red = randint(0, 256)
#         green = randint(0, 256)
#         blue = randint(0, 256)
#         self.qp.setPen(QPen(QColor(red, green, blue)))
#         self.qp.setBrush(QBrush(QColor(red, green, blue)))
#         if self.status == 1:
#             self.qp.drawEllipse(*self.coords, a, b)
#         elif self.status == 2:
#             self.qp.drawRect(*self.coords, a, b)
#         elif self.status == 3:
#             h = randint(5, 50)
#             x, y = self.coords
#             points = [QPoint(x, y + h), QPoint(x - a, y - h), QPoint(x + a, y - h)]
#             self.qp.drawPolygon(*points)
#
#     def mouseMoveEvent(self, e):
#         self.coords = [e.x(), e.y()]
#
#     def mousePressEvent(self, e):
#         if e.button() == Qt.LeftButton:
#             self.status = 1
#         elif e.button() == Qt.RightButton:
#             self.status = 2
#         self.drawf()
#
#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Space:
#             self.status = 3
#         self.update()
#         self.drawf()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     f = App()
#     f.show()
#     sys.exit(app.exec())