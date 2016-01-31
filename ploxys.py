import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ploxys_ui import Ui_main

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_main()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())