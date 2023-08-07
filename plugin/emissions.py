from PyQt5.QtWidgets import QDockWidget, QTabWidget
from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.QtGui import QMouseEvent, QColor

class Emissions(QDockWidget):
    def __init__(self, iface: QgisInterface, dock_widget: QDockWidget) -> None:   
        super().__init__('Emissions')
        print ("EMISSIONS")
                
        
