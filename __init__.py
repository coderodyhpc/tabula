import subprocess
from PyQt5.QtWidgets import QToolBar, QPushButton
from PyQt5.QtGui import QFont
#from PyQt5.QtCore import QString
from PyQt5 import QtCore

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

    iface.mainWindow().statusBar().setFont(QFont('Verdana', 10))  
    iface.mainWindow().statusBar().setStyleSheet("background-color: black; color: white;")  
    command1 = ['ec2metadata', '--instance-id']
    proc1 = subprocess.Popen(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    EC2_INSTANCE_ID = proc1.communicate()[0].decode("utf-8")
    command2 = ['ec2metadata', '--instance-type']
    proc2 = subprocess.Popen(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    EC2_INSTANCE_TYPE = proc2.communicate()[0].decode("utf-8")
    command3 = ['ec2metadata', '--availability-zone']
    proc3 = subprocess.Popen(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    EC2_ZONE = proc3.communicate()[0].decode("utf-8")
    
    lscpu_nomen = ((subprocess.check_output("lscpu", shell=True).strip()).decode())
    for item in lscpu_nomen.split("\n"):
        if "Model name" in item:
            modeln_1 = item.strip()
    modeln_2 = modeln_1.replace("Model name:","")    
    cpu_nomen = modeln_2.replace(" ","")  
    if cpu_nomen == 'Neoverse-N1':
        nomen2 = "Graviton2"
    else:    
        nomen2 = cpu-nomen
    cpu_NM = "CPU: "+nomen2+"\n"
    cpu_NM2 = "("+EC2_INSTANCE_TYPE+")"
    cpu_TOTAL = cpu_NM+cpu_NM2 
#    iface.mainWindow().statusBar().showMessage(texto)
    odyimum = QPushButton(cpu_TOTAL) 
#    odyimum.setStyleSheet = ('QString', background-color: black; color: orange;)        
#    stultus = "background-color: black; color: orange;"
#    odyimum.setStyleSheet = (const QString &stultus)        
#    odyimum.setStyleSheet = (QtCore.QString ('background-color: black; color: orange;'))
#    odyimum.setStyleSheet(".QWidget {color: blue; background-color: yellow;}")
#    odyimum.setStyleSheet(".QPushButton {color:#F97902; background-color: black;}")
#    odyimum.setStyleSheet(".QPushButton {color: black; background-color:#F97902;}")
    odyimum.setStyleSheet(".QPushButton {color: black; background-color:#FF9900;}")
#    odyimum.setFont(QFont('Verdana', 10))
#    stilus.setStyleSheet = ("background-color: black; color: orange;")
    iface.mainWindow().statusBar().addWidget(odyimum)  

    iface.messageBar().pushMessage("Error", "I'm sorry Dave, I'm afraid I can't do that")

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
