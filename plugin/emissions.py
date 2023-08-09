import netCDF4 as nc

from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTreeWidget, QLabel, QSlider, QHeaderView
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QEvent 
from PyQt5.QtGui import QMouseEvent, QColor, QFont
from PyQt5 import QtCore

#from qgis.core import QgsCoordinateReferenceSystem, QgsMessageLog, Qgis, QgsProject, QgsLayerTree, QgsRasterLayer, QgsVectorLayer
from qgis.core import QgsProject, QgsLayerTree, QgsRasterLayer, QgsVectorLayer

def FileDialog(directory='', forOpen=True, fmt='', isFolder=False):
    ROOT_DIR = '/home/ubuntu'
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
        self.lex = ('No projection')    

class Emissions(QWidget):
    tab_active = pyqtSignal()
    def __init__(self, iface) -> None:   
        super().__init__()
        self.tempus = Tempus()
#        print ("EMISSIONS ",self.tempus)
        self.iface = iface
        self.times = []
        self.vbox = QVBoxLayout()
# FILE NUNTIUM     
	nuntium1 =QHBoxLayout    
        self.file_label = QLabel('File : ')
        self.file_label.setFont(QFont('Verdana', 14))
#        self.file_nuntium = self.tempus.em_file 	    
        self.emissions_label = QLabel(self.tempus.em_file)
        self.emissions_label.setFont(QFont('Verdana', 14))
        self.emissions_label.setStyleSheet("border: 2px solid black; background-color:slategray; color:white; font-weight: bold;")
        nuntium1.addWidget(self.file_label)
        nuntium1.addWidget(self.emissions_label)
        self.vbox.addLayout(nuntium1)
# PROJ NUNTIUM      
	nuntium2 =QHBoxLayout    
        self.proj_label = QLabel('Projection : ')
        self.proj_label.setFont(QFont('Verdana', 14))
        self.lex_label = QLabel(self.tempus.lex)
        self.lex_label.setFont(QFont('Verdana', 14))
        self.lex_label.setStyleSheet("border: 2px solid black; background-color:lightsteelblue; color:white; font-weight: bold;")
        nuntium2.addWidget(self.proj_label)
        nuntium2.addWidget(self.lex_label)
        self.vbox.addLayout(nuntium2)
# FILE LOADER      
        self.fileOpenButton = QPushButton('Click to open emissions file',self)
#        self.fileOpenButton.setFont(QFont('Verdana', 12))
        self.fileOpenButton.setFixedHeight(25)
        self.fileOpenButton.setFont(QFont('Verdana', 16))
        self.fileOpenButton.setStyleSheet("border: 2px solid black; background-color:black; color:white; font-weight: bold;")
        self.vbox.addWidget(self.fileOpenButton)
#        self.fileOpenButton.clicked.connect(self.getncfiles)
        self.fileOpenButton.clicked.connect(self.zzz)
# SELECTORS      
        self.create_variable_selector3()
        self.create_time_selector()

####################################################################################################
########## SHAPEFILES GROUP SUPERWIDGET 
####################################################################################################
        self.shape_box = QHBoxLayout()                    # Group widget
        self.etiqueta = QLabel("   ")
        self.etiqueta.setFont(QFont('Verdana', 12))
### Selections
        self.geospatial = QLabel("Geospatial data ")
        self.geospatial.setFont(QFont('Verdana', 12))
        self.geospatial.setStyleSheet("font-weight: bold")
        self.shape_box.addWidget(self.geospatial)
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#        self.WB_borders_box = QCheckBox(text="WB_Borders")
#        self.WB_borders_box.setFont(QFont('Verdana', 12))
#        self.WB_borders_box.stateChanged.connect(self.WB_borders_upd)
#        self.shape_box.addWidget(self.WB_borders_box)
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#        self.WB_coastlines_box = QCheckBox(text="WB_Coastlines")
#        self.WB_coastlines_box.setFont(QFont('Verdana', 12))
#        self.WB_coastlines_box.stateChanged.connect(self.WB_coastlines_upd)
#        self.shape_box.addWidget(self.WB_coastlines_box)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
        self.borders_box = QCheckBox(text="Borders")
        self.borders_box.setFont(QFont('Verdana', 12))
        self.borders_box.stateChanged.connect(self.borders_upd)
        self.shape_box.addWidget(self.borders_box)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
        self.coastlines_box = QCheckBox(text="Coastlines")
        self.coastlines_box.setFont(QFont('Verdana', 12))
        self.coastlines_box.stateChanged.connect(self.coastlines_upd)
        self.shape_box.addWidget(self.coastlines_box)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
        self.lakes_box = QCheckBox(text="Lakes")
        self.lakes_box.setFont(QFont('Verdana', 12))
        self.lakes_box.stateChanged.connect(self.lakes_upd)
        self.shape_box.addWidget(self.lakes_box)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#        statelines_box = QCheckBox(text="State lines (U.S.)")
#        statelines_box.setFont(QFont('Verdana', 12))
#        self.shape_box.addWidget(statelines_box)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
        self.usparks_box = QCheckBox(text="U.S. National Parks")
        self.usparks_box.setFont(QFont('Verdana', 12))
        self.usparks_box.stateChanged.connect(self.usparks_upd)
        self.shape_box.addWidget(self.usparks_box)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
        self.urban_box = QCheckBox(text="Urban areas (U.S.)")
        self.urban_box.setFont(QFont('Verdana', 12))
        self.urban_box.stateChanged.connect(self.urban_upd)
        self.shape_box.addWidget(self.urban_box)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
        self.pm25_box = QCheckBox(text="EPA PM-2.5 NAAQS (2012)")
        self.pm25_box.setFont(QFont('Verdana', 12))
        self.pm25_box.stateChanged.connect(self.pm25_upd)
        self.shape_box.addWidget(self.pm25_box)
# Putting everything together and adding to the layout
        self.vbox.addLayout(self.shape_box)
	    
        self.setLayout(self.vbox)

    def zzz(self):
        self.tempus.em_file = FileDialog()
        self.emissions_label.setText(self.tempus.em_file)
        self.emissions_dataset = nc.Dataset(self.tempus.em_file)
# Read variables & times
        try:
            variables = {}
            for var_name in self.pm_dataset.variables:
                var = self.emissions_dataset.variables[var_name]
                dims = var.dimensions
                extra_dim = None
                try:
                    description = var.getncattr('description')
                except AttributeError:
                    description = None
                else:
                    if description == '-':
                        description = None
                    else:
                        description = description.lower()
                try:
                    units = var.getncattr('units')
                except AttributeError:
                    units = None
                else:
                    if units in ['-', 'dimensionless']:
                        units = None
#                variables[var_name] = CMAQNetCDFVariable(var_name,description,units,extra_dim,auto())
# Read #times
            temporibus = self.emissions_dataset.dimensions["TSTEP"].size
        finally:
            self.emissions_dataset.close()
        print ("Variables ",variables)
	    
    def create_variable_selector3(self) -> None:   #self.vbox defined in the constructor
        self.ap3time_label = QLabel('Emission species')
        self.ap3time_label.setFont(QFont('Verdana', 14))
        self.vbox.addWidget(self.ap3time_label)
        
        hbox1 = QHBoxLayout()
        self.hac_index = 1
        self.variable_selector = QTreeWidget()
        self.variable_selector.setStyleSheet('font-size: 13pt; font-family: Verdana;')
        self.variable_selector.setHeaderLabels(['Species', 'Units', 'Max', 'Min'])
        self.variable_selector.setRootIsDecorated(False)
        self.variable_selector.setSortingEnabled(True)
        self.variable_selector.sortByColumn(0, Qt.AscendingOrder)
        self.variable_selector.header().setSectionsMovable(False)
        self.variable_selector.header().setSectionResizeMode(0, QHeaderView.Stretch)
        self.variable_selector.header().setSectionResizeMode(1, QHeaderView.Stretch)
        self.variable_selector.header().setSectionResizeMode(2, QHeaderView.Stretch)
        self.variable_selector.header().setSectionResizeMode(3, QHeaderView.Stretch)
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


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    def addere_borders(self):
        borders_b = QgsVectorLayer('/opt/.Odycloud/FORMAS/ne_10m_admin_0_boundary_lines_land.shp', "Borders", "ogr")
        QgsProject.instance().addMapLayer(borders_b)
#        qml_path = '/home/ubuntu/SHAPEFILES/gris150.qml'
#        set_style_from_qml_name(urbanareas, qml_path)

    def borders_upd(self, int):
        if self.borders_box.isChecked():
            self.addere_borders()
        else:
            genus_nomen = 'Borders'
            unus = QgsProject.instance()                   # type: QgsProject
            radix = unus.layerTreeRoot()                   # type: QgsLayerTree
            genus = radix.findGroup(genus_nomen)
            for capa in unus.mapLayers().values():
                if capa.name() == 'Borders':
                    unus.removeMapLayers( [capa.id()] )

    def addere_coastlines(self):
        coastlines_b = QgsVectorLayer('/opt/.Odycloud/FORMAS/ne_10m_ocean.shp', "Oceans", "ogr")
        QgsProject.instance().addMapLayer(coastlines_b)
        coast_qml_path = '/opt/.Odycloud/FORMAS/oceanblue_50.qml'
        set_style_from_qml_name(coastlines_b, coast_qml_path)

    def coastlines_upd(self, int):
        if self.coastlines_box.isChecked():
            self.addere_coastlines()
        else:
            genus_nomen = 'Oceans'
            unus = QgsProject.instance()                   # type: QgsProject
            radix = unus.layerTreeRoot()                   # type: QgsLayerTree
            genus = radix.findGroup(genus_nomen)
            for capa in unus.mapLayers().values():
                if capa.name() == 'Oceans':
                    unus.removeMapLayers( [capa.id()] )

    def WB_addere_borders(self):
        WB_borders_b = QgsVectorLayer('/opt/.Odycloud/FORMAS/WB_countries_Admin0_10m.shp', "WB_Borders", "ogr")
        QgsProject.instance().addMapLayer(WB_borders_b)

    def WB_borders_upd(self, int):
        if self.WB_borders_box.isChecked():
            self.WB_addere_borders()
        else:
            genus_nomen = 'WB_Borders'
            unus = QgsProject.instance()                   # type: QgsProject
            radix = unus.layerTreeRoot()                   # type: QgsLayerTree
            genus = radix.findGroup(genus_nomen)
            for capa in unus.mapLayers().values():
                if capa.name() == 'WB_Borders':
                    unus.removeMapLayers( [capa.id()] )

    def WB_addere_coastlines(self):
        WB_coastlines_b = QgsVectorLayer('/opt/.Odycloud/FORMAS/WB_Coastlines_10m.shp', "WB_Oceans", "ogr")
        QgsProject.instance().addMapLayer(WB_coastlines_b)
        qml_path = '/opt/.Odycloud/FORMAS/oceanblue_50.qml'
        set_style_from_qml_name(WB_coastlines_b, qml_path)

    def WB_coastlines_upd(self, int):
        if self.WB_coastlines_box.isChecked():
            self.WB_addere_coastlines()
        else:
            genus_nomen = 'WB_Oceans'
            unus = QgsProject.instance()                   # type: QgsProject
            radix = unus.layerTreeRoot()                   # type: QgsLayerTree
            genus = radix.findGroup(genus_nomen)
            for capa in unus.mapLayers().values():
                if capa.name() == 'WB_Oceans':
                    unus.removeMapLayers( [capa.id()] )

    def addere_urban(self):
        urbanareas = QgsVectorLayer('/opt/.Odycloud/FORMAS/cb_2018_us_ua10_500k.shp', "Urban areas", "ogr")
        QgsProject.instance().addMapLayer(urbanareas)
        urban_qml_path = '/opt/.Odycloud/FORMAS/gris150_50.qml'
        set_style_from_qml_name(urbanareas, urban_qml_path)

    def urban_upd(self, int):
        if self.urban_box.isChecked():
#            print("Add urban area")
            self.addere_urban()
        else:
            genus_nomen = 'Urban areas'
            unus = QgsProject.instance()                   # type: QgsProject
            radix = unus.layerTreeRoot()                   # type: QgsLayerTree
            genus = radix.findGroup(genus_nomen)
            for capa in unus.mapLayers().values():
                if capa.name() == 'Urban areas':
                    unus.removeMapLayers( [capa.id()] )

    def addere_lakes(self):
        lakes_b = QgsVectorLayer('/opt/.Odycloud/FORMAS/ne_10m_lakes.shp', "Lakes", "ogr")
        QgsProject.instance().addMapLayer(lakes_b)
        lakes_qml_path = '/opt/.Odycloud/FORMAS/lake_50.qml'
        set_style_from_qml_name(lakes_b, lakes_qml_path)

    def lakes_upd(self, int):
        if self.lakes_box.isChecked():
            self.addere_lakes()
        else:
            genus_nomen = 'Lakes'
            unus = QgsProject.instance()                   # type: QgsProject
            radix = unus.layerTreeRoot()                   # type: QgsLayerTree
            genus = radix.findGroup(genus_nomen)
            for capa in unus.mapLayers().values():
                if capa.name() == 'Lakes':
                    unus.removeMapLayers( [capa.id()] )

    def addere_usparks(self):
        usparks_b = QgsVectorLayer('/opt/.Odycloud/FORMAS/ne_10m_parks_and_protected_lands_area.shp', "Parks", "ogr")
        QgsProject.instance().addMapLayer(usparks_b)
        usparks_qml_path = '/opt/.Odycloud/FORMAS/green_50.qml'
        set_style_from_qml_name(usparks_b, usparks_qml_path)

    def usparks_upd(self, int):
        if self.usparks_box.isChecked():
            self.addere_usparks()
        else:
            genus_nomen = 'Parks'
            unus = QgsProject.instance()                   # type: QgsProject
            radix = unus.layerTreeRoot()                   # type: QgsLayerTree
            genus = radix.findGroup(genus_nomen)
            for capa in unus.mapLayers().values():
                if capa.name() == 'Parks':
                    unus.removeMapLayers( [capa.id()] )

    def addere_PM25(self):
        pm25_b = QgsVectorLayer('/opt/.Odycloud/FORMAS/GREENBOOK/PM25_2012Std_NAA.shp', "PM25", "ogr")
        QgsProject.instance().addMapLayer(pm25_b)
        pm25_qml_path = '/opt/.Odycloud/FORMAS/gris50_20.qml'
        set_style_from_qml_name(pm25_b, pm25_qml_path)

    def pm25_upd(self, int):
        if self.pm25_box.isChecked():
            self.addere_PM25()
        else:
            genus_nomen = 'PM25'
            unus = QgsProject.instance()                   # type: QgsProject
            radix = unus.layerTreeRoot()                   # type: QgsLayerTree
            genus = radix.findGroup(genus_nomen)
            for capa in unus.mapLayers().values():
                if capa.name() == 'PM25':
                    unus.removeMapLayers( [capa.id()] )

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

