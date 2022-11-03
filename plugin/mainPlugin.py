from typing import List, Callable
import webbrowser
import time
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QWidget

from qgis.core import QgsMessageLog, Qgis
from qgis.gui import QgisInterface

#from Gv3GEWRF.core import (logger)
#__ Loading of the docks for the different apps ___#
#from Gv3GEWRF.plugin.ui.wrfIII import WrfDock
#from Gv3GEWRF.plugin.options import get_options
#from Gv3GEWRF.plugin.geo import add_default_basemap, load_wps_binary_layer
#from Gv3GEWRF.plugin.geo import add_naip_basemap


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
        self.init_logging() #This is probably to track what happens while running the plugin A.F. 

#        install_user_error_handler(self.iface) #This is at plugin/ui/helpers.py
#___ These are the actions defining the different options at the Gv3GEWRF menu 
#___ (maybe I should get rid of it and simply start the app w/o asking any Qs) 
        self.menu = '&' + PLUGIN_NAME
        self.add_action(icon_path='/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins/Gv3GEWRF/plugin/resources/WRF_logo16B.png',
                        text="TABULA", callback=self.show_dock, add_to_toolbar=True,
                        parent=self.iface.mainWindow(), status_tip='Run WRF')

#__ I believe that this might be to set up the Settings/options ___#
        self.options_factory = OptionsFactory() # This is at gis4wrf/plugin/ui/options.py
        self.iface.registerOptionsWidgetFactory(self.options_factory)
        self.options = get_options()

#        self.check_versions() #I'm deactivating check_versions - probably needs to be erased

    def unload(self) -> None:
        """Removes the plugin menu item and icon from QGIS GUI.
           Note: This method is called by QGIS.
        """

        self.destroy_logging()

#__ Functions  ___#
    def show_dock(self) -> None:
#        Pass
#        if not self.dock_widget:
#            self.dock_widget = WrfDock(self.iface, self.dock_widget, self.dies)
#            self.dock_widget = WrfDockII(self.iface)
#! What happens if I change Right with Left
        self.iface.addDockWidget(
            Qt.RightDockWidgetArea, self.dock_widget)
#        add_default_basemap()
#        add_naip_basemap()
#        self.dock_widget.hasFocus.connect(self.on_dock_focus)
#        self.iface.addWidget(
#            self.dock_widget)

