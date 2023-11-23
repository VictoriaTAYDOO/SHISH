import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import uic
from UI import UI_MainWindow


class Example(QMainWindow, UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.setupUi(self)

    def initUI(self):
        # uic.loadUI('UI.ui')
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for i in range(100):
            x = random.randint(20, 600)
            y = random.randint(20, 600)
            r = random.randint(10, 100)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())