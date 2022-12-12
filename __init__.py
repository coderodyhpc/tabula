import subprocess
from PyQt5.QtWidgets import QToolBar, QPushButton
from PyQt5.QtGui import QFont

def classFactory(iface):
    """Load QGISPlugin class.
    Parameters
    ----------
    iface: qgis.gui.QgisInterface
        An interface instance that will be passed to this class
        which provides the hook by which you can manipulate the QGIS
        application at run time.
    Returns
    -------
    """

    from tabula.plugin.mainPlugin import QGISPlugin
#    project = QgsProject.instance()
#    project.setTitle('HOLAAAA')
#    project.write()
    title = iface.mainWindow().windowTitle()
    toolbar = QToolBar()
    new_title = title.replace('QGIS', 'TABULA')
    iface.mainWindow().setWindowTitle(new_title)
    
#    iface.mainWindow().removeToolBar(toolbar)
    
    toolbar = iface.helpToolBar()
    parent = toolbar.parentWidget()
    parent.removeToolBar(toolbar)

    lscpu_nomen = ((subprocess.check_output("lscpu", shell=True).strip()).decode())
    for item in lscpu_nomen.split("\n"):
        if "Model name" in item:
            modeln_1 = item.strip()
    modeln_2 = modeln_1.replace("Model name:","")    
    cpu_nomen = modeln_2.replace(" ","")    
    cpu_NM = "CPU: "+cpu_nomen
#    iface.mainWindow().statusBar().showMessage(texto)
    odyimum = QPushButton(cpu_NM) 
    odyimum.setStyleSheet = ("background-color: black; color: orange;")        
    odyimum.setFont(QFont('Verdana', 14))
#    stilus.setStyleSheet = ("background-color: black; color: orange;")
    iface.mainWindow().statusBar().addWidget(odyimum)  
    
#    vector_menu = iface.vectorMenu()
#    raster_menu = iface.rasterMenu()
#    mesh_menu = iface.meshMenu()
#    database_menu = iface.databaseMenu()
#    web_menu = iface.webMenu()
#    processing_menu = iface.processingMenu()
#    menubar = vector_menu.parentWidget()
#    menubar.removeAction(vector_menu.menuAction())
#    menubar.removeAction(raster_menu.menuAction())
#    menubar.removeAction(database_menu.menuAction())
#    menubar.removeAction(mesh_menu.menuAction())
#    menubar.removeAction(web_menu.menuAction())
#    menubar.removeAction(processing_menu.menuAction())
#    menubar.addAction(dummy_menu)
    return QGISPlugin(iface)

def dummy_menu():
    pass
