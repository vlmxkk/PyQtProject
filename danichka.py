from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

app=QApplication([])

window=QWidget()


window.resize(500,500)
window.move(100,150)
window.setWindowTitle('Перша програма')
window.setWindowIcon(QIcon('mihail-zalivako.jpeg'))
window.show()

app.exec_()