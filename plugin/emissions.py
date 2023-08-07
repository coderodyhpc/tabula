from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtCore import pyqtSignal, QEvent 
from PyQt5.QtGui import QMouseEvent, QColor


class Emissions(QWidget):
    tab_active = pyqtSignal()
    def __init__(self, iface) -> None:   
        super().__init__()
        print ("EMISSIONS")
        
        self.iface = iface
        self.times = []
        self.vbox = QVBoxLayout()
        self.fileOpenButton = QPushButton('Click to open emissions file',self)
        self.fileOpenButton.clicked.connect(self.getncfiles)
        self.vbox.addWidget(self.fileOpenButton)
        
        self.setLayout(self.vbox)
        
    def buttonClicked(self):
        wig = App()
                
    def getncfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("nc files (*.nc)")
        filenames = []
		
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
			
            with f:
                data = f.read()
                self.contents.setText(data)        
