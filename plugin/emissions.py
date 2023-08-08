from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTreeWidget, QLabel, QSlider, QHeaderView
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QEvent 
from PyQt5.QtGui import QMouseEvent, QColor, QFont
from definitions import ROOT_DIR
from PyQt5 import QtCore

def FileDialog(directory='', forOpen=True, fmt='', isFolder=False):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    options |= QFileDialog.DontUseCustomDirectoryIcons
    dialog = QFileDialog()
    dialog.setOptions(options)

    dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)

    # ARE WE TALKING ABOUT FILES OR FOLDERS
    if isFolder:
        dialog.setFileMode(QFileDialog.DirectoryOnly)
    else:
        dialog.setFileMode(QFileDialog.AnyFile)
    # OPENING OR SAVING
    dialog.setAcceptMode(QFileDialog.AcceptOpen) if forOpen else dialog.setAcceptMode(QFileDialog.AcceptSave)

    # SET FORMAT, IF SPECIFIED
    if fmt != '' and isFolder is False:
        dialog.setDefaultSuffix(fmt)
        dialog.setNameFilters([f'{fmt} (*.{fmt})'])

    # SET THE STARTING DIRECTORY
    if directory != '':
        dialog.setDirectory(str(directory))
    else:
        dialog.setDirectory(str(ROOT_DIR))


    if dialog.exec_() == QDialog.Accepted:
        path = dialog.selectedFiles()[0]  # returns a list
        return path
    else:
        return ''

class Tempus:
    def __init__(self):
        self.em_file = ('No file selected yet')

class Emissions(QWidget):
    tab_active = pyqtSignal()
    def __init__(self, iface) -> None:   
        super().__init__()
        self.tempus = Tempus()
        print ("EMISSIONS ",self.tempus)
        self.iface = iface
        self.times = []
        self.vbox = QVBoxLayout()
        self.fileOpenButton = QPushButton('Click to open emissions file',self)
        self.fileOpenButton.setFont(QFont('Verdana', 12))
        self.vbox.addWidget(self.fileOpenButton)
        self.file_nuntium = 'File : ' + self.tempus.em_file 	    
#        self.file_nuntium = 'File : '  	    
        self.emissions_label = QLabel(self.file_nuntium)
        self.emissions_label.setFont(QFont('Verdana', 14))
        self.vbox.addWidget(self.emissions_label)
#        self.fileOpenButton.clicked.connect(self.getncfiles)
        self.fileOpenButton.clicked.connect(self.zzz)
        self.create_variable_selector3()
        self.create_time_selector()
        
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
		    
    def zzz(self):
        self.nomen = FileDialog()
        print ("New file is ", self.nomen)
	    
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
