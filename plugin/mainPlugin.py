from typing import List, Callable, Union
from threading import Timer
import time

from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QAction, QWidget, QDockWidget, QTabWidget, QMenu
from PyQt5.QtGui import QIcon, QColor, QPainterPath, QPainter, QBrush, QFont

from qgis.core import (QgsCoordinateReferenceSystem, QgsMessageLog, Qgis, QgsProject, QgsLayerTree, QgsRasterLayer,
    QgsVectorLayer, QgsPoint, QgsPointXY, QgsGeometry, QgsMapRendererJob, QgsWkbTypes
)
from qgis.gui import QgisInterface, QgsMapCanvas, QgsVertexMarker, QgsMapCanvasItem, QgsMapMouseEvent, QgsRubberBand

class TextCanvasItem(QgsMapCanvasItem):
    def __init__(self, canvas):
        super().__init__(canvas)
        
    def paint(self, painter, option, widget):
        painter.drawText(50, 50, "ONES")

class Legenda9(QgsMapCanvasItem):
    def __init__(self, canvas, numeri, titulus, unitas):
        super().__init__(canvas)
        self.numeri = numeri
        self.titulus = titulus 
        self.unitas = unitas
        self.altitudo = 12
        self.longitudo = 40
        
    def setCenter(self, center):
        self.center = center

    def center(self):
        return self.center

    def paint(self, painter, option, widget):
        imum_sinister = [100, 400]
        painter.setPen(QColor(Qt.black))
        painter.drawRect(imum_sinister[0]-5, imum_sinister[1]-5-(11*self.altitudo), 130, 11*self.altitudo+10)
        painter.setPen(QColor(Qt.black))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-2-(10*self.altitudo), self.titulus)
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-2-(9*self.altitudo), self.unitas)
        for iii in range(9):
            painter.setPen(QColor(Qt.black))
            painter.setFont(QFont('Verdana', self.altitudo-2))
            aaa = str(self.numeri[iii])
            painter.drawText(imum_sinister[0]+self.longitudo+5, imum_sinister[1]-2-(iii*self.altitudo), aaa[:7])
            if iii == 0:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 0, 0))          
            elif iii == 1:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255,64,64))          
            elif iii == 2:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255,128,128))          
            elif iii == 3:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255,191,191))          
            elif iii == 4:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 255, 255))          
            elif iii == 5:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(191,191,255))          
            elif iii == 6:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(128,129,255))          
            elif iii == 7:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(64, 64, 255))          
            elif iii == 8:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(0, 0, 255))          

class Legenda11(QgsMapCanvasItem):
    def __init__(self, canvas, numeri, titulus, unitas):
        super().__init__(canvas)
        self.numeri = numeri
        self.titulus = titulus 
        self.unitas = unitas
        self.altitudo = 12
        self.longitudo = 40
        
    def setCenter(self, center):
        self.center = center

    def center(self):
        return self.center

    def paint(self, painter, option, widget):
        imum_sinister11 = [600, 400]
        painter.setPen(QColor(Qt.black))
        painter.drawRect(imum_sinister11[0]-5, imum_sinister11[1]-5-(13*self.altitudo), 130, 13*self.altitudo+10)
        painter.setPen(QColor(Qt.black))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        painter.drawText(imum_sinister11[0]+5, imum_sinister11[1]-2-(12*self.altitudo), self.titulus)
        painter.drawText(imum_sinister11[0]+5, imum_sinister11[1]-2-(11*self.altitudo), self.unitas)
        for iii in range(11):
            painter.setPen(QColor(Qt.black))
            painter.setFont(QFont('Verdana', self.altitudo-2))
            aaa = str(self.numeri[iii])
            painter.drawText(imum_sinister11[0]+self.longitudo+5, imum_sinister11[1]-2-(iii*self.altitudo), aaa[:7])
            if iii == 0:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(41, 27, 45))          
            elif iii == 1:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(78,141,73))          
            elif iii == 2:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(114, 254, 101))          
            elif iii == 3:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(179,228,72))          
            elif iii == 4:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(243, 201, 43))          
            elif iii == 5:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(248,154,34))          
            elif iii == 6:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(252, 106, 25))          
            elif iii == 7:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(218,69,17))          
            elif iii == 8:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(184, 32, 8))          
            elif iii == 9:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(164, 22, 4))          
            elif iii == 10:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(144, 12, 0))          
                

class TabulaDock(QDockWidget):
    def __init__(self, iface: QgisInterface, dock_widget: QDockWidget) -> None:   
        super().__init__('TABULA')
#_____ TABS SET UP _____#
        tabs = QTabWidget()
        tabs.setStyleSheet('''QTabBar::tab {font-size: 10pt; font-family: Verdana; font-weight: bold; color: #004F00; height: 40px; width: 140px;}''')
        self.tab1 = QWidget()
        tabs.addTab(self.tab1,"TAB 1")
        self.tab2 = QWidget()
        tabs.addTab(self.tab2,"TAB 2")
        self.setWidget(tabs)
        self.tabs = tabs
        self.add_stamen_basemap()
        Zsize = iface.mapCanvas().size()
        print(Zsize, "Width : " + str(Zsize.width()) + " / Height : " + str(Zsize.height()))
        rasa = QgsMapCanvas()
        print ("RASA ", rasa, type(rasa))
        print ("RASAsize ", rasa.size())

        title = "U10 (U at 10 m)"
        units = "m s-1"
        numerum_l = ["aaa.111554254", "bbb.267", "c.963456","fffff.111", "50.267", "65.963","70.111", "80.267", "95.963"] 
        item4 = Legenda9(iface.mapCanvas(), numerum_l, title, units)
        
        title11 = "P (P at 10 m)"
        units11 = "Pa"
        numerum_11 = ["10.111554254", "0.267", "35.963456","40.111", "50.267", "65.963", "70.111", "80.267", "95.963", "100.963", "1295.963"] 
        item5 = Legenda11(iface.mapCanvas(), numerum_11, title11, units11)


    def add_stamen_basemap(self):
        print ("Adding Stamen")
        url = 'type=xyz&zmin=0&zmax=20&url=http://a.tile.stamen.com/terrain-background/{z}/{x}/{y}.png'
        attribution = 'Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL'
        attribution_url = 'http://maps.stamen.com'
        registry = QgsProject.instance() # type: QgsProject
        root = registry.layerTreeRoot() # type: QgsLayerTree

        tree_layers = filter(QgsLayerTree.isLayer, root.children())
        if any(tree_layer.layer().source() == url for tree_layer in tree_layers):
            return
        layer = QgsRasterLayer(url, 'Stamen Terrain Background', 'wms')
        layer.setAttribution(attribution)
        layer.setAttributionUrl(attribution_url)
        registry.addMapLayer(layer, False)
        root.addLayer(layer)

#    # Reset the Project CRS to WGS84 otherwise it will be set to the stamen layer CRS
#        def setWGS84():
#            registry.setCrs((QgsCoordinateReferenceSystem.fromProj4("+proj=longlat +datum=WGS84 +no_defs")))
#        setWGS84()
#    # Again with a delay, which is a work-around as sometimes QGIS does not apply the CRS change above.
#        Timer(0.5, setWGS84).start()

        
#__ Initialization of the graphic environment ___#
class QGISPlugin():
    def __init__(self, iface: QgisInterface) -> None:
        self.iface = iface
        self.actions = []  # type: List[QAction]
        self.dock_widget = None # type: WrfDock
        
    def initGui(self) -> None:
        """Create the menu entries and toolbar icons inside the QGIS GUI.
           Note: This method is called by QGIS.
        """

        self.menu = '&' + 'TABULA'
        self.add_action(icon_path='/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/TABULA/logo16B.png',
                        text="TABULA", callback=self.show_dock, add_to_toolbar=True,
                        parent=self.iface.mainWindow(), status_tip='Testing TABULA')

    def unload(self) -> None:
        """Removes the plugin menu item and icon from QGIS GUI.
           Note: This method is called by QGIS.
        """
        pass

#__ Functions  ___#
    def show_dock(self) -> None:
        if not self.dock_widget:
            self.dock_widget = TabulaDock(self.iface, self.dock_widget)
        self.iface.addDockWidget(
            Qt.RightDockWidgetArea, self.dock_widget)

    def add_action(self, icon_path: str, text: str, callback: Callable,
                   enabled_flag: bool=True, add_to_menu: bool=True,
                   add_to_toolbar: bool=False, add_to_add_layer: bool=False,
                   status_tip: str=None, whats_this: str=None, parent: QWidget=None
                   ) -> QAction:
        """Helper function for creating menu items
        Parameters
        ----------
        icon_path: Path to the icon for this action. Can be a resource
            path (e.g. `:/plugins/foo/bar.png`) or a normal file system path.
        text: Text that should be shown in menu items for this action.
        callback: Function to be called when the action is triggered.
        enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        add_to_toolbar: Flag indicating whether the action should also
            be added to the Plugins toolbar. Defaults to False.
        add_to_layer: Flag indicating whether the action should also
            be added to the Layer > Add Layer menu. Defaults to False.
        status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action after clicking on `?`.
        parent: Parent widget for the new action. Defaults None.
        Returns
        -------
        out: The action that was created. Note that the action is
            also added to `self.actions` list.
        """
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        if add_to_add_layer:
            self.iface.insertAddLayerAction(action)

        self.actions.append(action)

        return action
    
