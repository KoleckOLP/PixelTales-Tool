import sys, os
import subprocess
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, QThread


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(f"gui.ui", self)

        self.show()

        def status(s=""):  # shows status message and changes color of the status bar.
            self.statusBar().showMessage(s)
            if s == "Ready.":
                self.statusBar().setStyleSheet("background-color: #00BB00")
            elif s == "Busy.":
                self.statusBar().setStyleSheet("background-color: #FF6600")
            else:
                self.statusBar().setStyleSheet("background-color: #A9A9A9")

        def openFolder(loc=""):
            if loc == "":  # if there is no path it should open the folder of the program
                loc = "." + os.path.sep
            if (sys.platform.startswith("win")):
                os.system(f"start {loc}")
            elif (sys.platform.startswith(("darwin", "haiku"))):  # haiku support :3
                os.system(f"open {loc}")
            else:  # (sys.platform.startswith(("linux", "freebsd"))): #hoping that other OSes use xdg-open
                os.system(f"xdg-open {loc}")

        def oldChooser():
            print("clicked old")

        def ssoChooser():
            print("clicked sso")

        self.input_open_button.clicked.connect(lambda: openFolder(self.input_bar.text()))
        self.input_browse_button.clicked.connect(lambda: self.input_bar.setText(QtWidgets.QFileDialog.getExistingDirectory()))
        self.output_open_button.clicked.connect(lambda: openFolder(self.output_bar.text()))
        self.output_browse_button.clicked.connect(lambda: self.output_bar.setText(QtWidgets.QFileDialog.getExistingDirectory()))

        self.run_old_button.clicked.connect(lambda: oldChooser())
        self.run_sso_button.clicked.connect(lambda: ssoChooser())

        status("Ready.")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec()