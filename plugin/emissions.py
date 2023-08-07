from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTreeWidget, QFileDialog, QSlider
from PyQt5.QtCore import Qt, pyqtSignal, QEvent 
from PyQt5.QtGui import QMouseEvent, QColor, QFont


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
        self.create_variable_selector3()
        self.create_time_selector()
        self.vbox.addWidget(self.fileOpenButton)
        
        self.setLayout(self.vbox)
        
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

    def create_variable_selector3(self) -> None:   #self.vbox defined in the constructor
        self.ap3time_label = QLabel('Emission species')
        self.ap3time_label.setFont(QFont('Verdana', 14))
        self.vbox.addWidget(self.ap3time_label)
        
        hbox1 = QHBoxLayout()
        self.hac_index = 1
        self.variable_selector = QTreeWidget()
        self.variable_selector.setStyleSheet('font-size: 13pt; font-family: Verdana;')
        self.variable_selector.setHeaderLabels(['Species', 'Units'])
        self.variable_selector.setRootIsDecorated(False)
        self.variable_selector.setSortingEnabled(True)
        self.variable_selector.sortByColumn(0, Qt.AscendingOrder)
        self.variable_selector.header().setSectionsMovable(False)
        self.variable_selector.header().setSectionResizeMode(0, QHeaderView.Stretch)
        self.variable_selector.header().setSectionResizeMode(1, QHeaderView.Stretch)
        self.variable_selector.header().setFont(QFont('Verdana', 14))
#        self.variable_selector.currentItemChanged.connect(self.on_variable_selected)
#        self.variable_selector.setFixedHeight(115)
        hbox1.addWidget(self.variable_selector)
        self.vbox.addLayout(hbox1)

        
    def create_time_selector(self) -> None:
        self.time_label = QLabel('Time: N/A')
        self.time_selector = QSlider(Qt.Horizontal)
        self.time_selector.setSingleStep(1)
        self.time_selector.setPageStep(1)
        self.time_selector.setMinimum(0)
        self.time_selector.setMaximum(0)
#        self.time_selector.valueChanged.connect(self.on_time_selected)
        self.time_label.setFont(QFont('Verdana', 12))
        self.vbox.addWidget(self.time_label)
        self.vbox.addWidget(self.time_selector)
