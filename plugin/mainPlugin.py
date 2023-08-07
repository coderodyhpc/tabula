from typing import List, Callable, Union
from threading import Timer
import time

from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QAction, QWidget, QDockWidget, QTabWidget, QMenu, QHBoxLayout, QLabel, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon, QColor, QPainterPath, QPainter, QBrush, QFont

from qgis.core import (QgsCoordinateReferenceSystem, QgsMessageLog, Qgis, QgsProject, QgsLayerTree, QgsRasterLayer,
    QgsVectorLayer, QgsPoint, QgsPointXY, QgsGeometry, QgsMapRendererJob, QgsWkbTypes
)
from qgis.gui import QgisInterface, QgsMapCanvas, QgsVertexMarker, QgsMapCanvasItem, QgsMapMouseEvent, QgsRubberBand

#from tabula.plugin.pingere import renovatio_formas, remove_group, tabulas, switch_band, get_raster_layers_in_group
from tabula.plugin.pingere import remove_group, get_raster_layers_in_group
#from tabula.plugin.pingere import Legenda0, Legenda100, Legenda12, TuDataset, CMAQNetCDFVariable, CMAQ_Lambert_geo
from tabula.plugin.emissions import Emissions

class TabulaDock(QDockWidget):
    def __init__(self, iface: QgisInterface, dock_widget: QDockWidget) -> None:
        super().__init__('TABULA')
        self.iface = iface
#_____ TABS SET UP _____#
        tabs = QTabWidget()
        tabs.setStyleSheet('''QTabBar::tab {font-size: 12pt; font-family: Verdana; font-weight: bold; color: #800000; height: 40px; width: 200px;}''')
        self.tab1 = Emissions(self.iface)
        tabs.addTab(self.tab1,"EMISSIONS")
        self.tab2 = QWidget()
        tabs.addTab(self.tab2,"WRF RESULTS")
        self.setWidget(tabs)
        self.tabs = tabs
        self.add_stamen_basemap()
#        Zsize = iface.mapCanvas().size()
#        print(Zsize, "Width : " + str(Zsize.width()) + " / Height : " + str(Zsize.height()))
#        rasa = QgsMapCanvas()
#        print ("RASA ", rasa, type(rasa))
#        print ("RASAsize ", rasa.size())

#        self.imum_box = QHBoxLayout()
#        self.classis_pigmemti = QButtonGroup()
#        pigmemti_box = QHBoxLayout()
#        self.nuntium_1 = QLabel("Font color")
#        self.nuntium_1.setFont(QFont('Verdana', 12))
#        self.nuntium_1.setStyleSheet("font-weight: bold")
#        pigmemti_box.addWidget(self.nuntium_1)
#        self.t_albinus = QRadioButton("White",self)
#        self.t_albinus.setFont(QFont('Verdana', 12))
#        self.t_albinus.setChecked(True)
##        self.t_albinus.toggled.connect(self.pigmemtum_has_changed)
#        self.t_nigreos = QRadioButton("Black",self)
#        self.t_nigreos.setFont(QFont('Verdana', 12))
##        self.t_nigreos.toggled.connect(self.pigmemtum_has_changed)
#        pigmemti_box.addWidget(self.t_albinus)
#        pigmemti_box.addWidget(self.t_nigreos)
#        self.classis_pigmemti.addButton(self.t_albinus)
#        self.classis_pigmemti.addButton(self.t_nigreos)

#-#        self.etiqueta = QLabel("   ")
#-#        self.etiqueta.setFont(QFont('Verdana', 12))
#-###        pigmemti_box.addWidget(self.etiqueta)
#-#        pigmemti_box.addWidget(self.etiqueta)
        
#        palette_box = QHBoxLayout()
#        self.classis_palette = QButtonGroup()
#        self.nuntium_2 = QLabel("Color palette")
#        self.nuntium_2.setFont(QFont('Verdana', 12))
#        self.nuntium_2.setStyleSheet("font-weight: bold")
#        palette_box.addWidget(self.nuntium_2)
#        self.red_blue = QRadioButton("Blue and red",self)
#        self.red_blue.setFont(QFont('Verdana', 12))
#        self.red_blue.setChecked(True)
##        self.red_blue.toggled.connect(self.palette_has_changed)
#        palette_box.addWidget(self.red_blue)
#        self.echo_tops = QRadioButton("Echo tops",self)
#        self.echo_tops.setFont(QFont('Verdana', 12))
#        self.echo_tops.setChecked(False)
##        self.echo_tops.toggled.connect(self.palette_has_changed)
#        palette_box.addWidget(self.echo_tops)
#        self.black_white = QRadioButton("Black and white",self)
#        self.black_white.setFont(QFont('Verdana', 12))
#        self.black_white.setChecked(False)
##        self.black_white.toggled.connect(self.palette_has_changed)
#        palette_box.addWidget(self.black_white)
#        self.classis_palette.addButton(self.red_blue)
#        self.classis_palette.addButton(self.echo_tops)
#        self.classis_palette.addButton(self.black_white)
#        self.imum_box.addLayout(pigmemti_box)
#        self.imum_box.addLayout(palette_box)

#        self.tab1.setLayout(self.imum_box)


#        title = "U10 (U at 10 m)"
#        units = "m s-1"
#        numerum_l = ["aaa.111554254", "bbb.267", "c.963456","fffff.111", "50.267", "65.963","70.111", "80.267", "95.963"]
#        item4 = Legenda9(iface.mapCanvas(), numerum_l, title, units)

#        title11 = "P (P at 10 m)"
#        units11 = "Pa"
#        numerum_11 = ["10.111554254", "0.267", "35.963456","40.111", "50.267", "65.963", "70.111", "80.267", "95.963", "100.963", "1295.963"]
#        item5 = Legenda11(iface.mapCanvas(), numerum_11, title11, units11)


    def add_stamen_basemap(self):
#        print ("Adding Stamen")
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
