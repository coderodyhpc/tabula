import subprocess, os
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

    command1 = 'EC2_INSTANCE_ID=$(ec2metadata --instance-id)'
    command2 = 'EC2_INSTANCE_TYPE=$(ec2metadata --instance-type)'
    command3 = 'EC2_ZONE=$(ec2metadata --availability-zone)'
    os.system(command1)
    os.system(command2)
    temp = subprocess.Popen([ec2metadata, '--instance-id', server], stdout = subprocess.PIPE)
    
    cmd = ['ec2metadata', '--instance-id']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate()
#    temp = subprocess.Popen([ec2metadata, '--instance-id'], stdout = subprocess.PIPE)
    print ("TEMP ",o)
#    os.system(command3)
#    print ('EC2_INSTANCE_ID ',EC2_INSTANCE_ID)
#    print ('EC2_INSTANCE_TYPE ',EC2_INSTANCE_TYPE)
#    print ('EC2_ZONE ',EC2_ZONE)
    
    lscpu_nomen = ((subprocess.check_output("lscpu", shell=True).strip()).decode())
    for item in lscpu_nomen.split("\n"):
        if "Model name" in item:
            modeln_1 = item.strip()
    modeln_2 = modeln_1.replace("Model name:","")    
    cpu_nomen = modeln_2.replace(" ","")    
    cpu_NM = "CPU: "+cpu_nomen
#    iface.mainWindow().statusBar().showMessage(texto)
    odyimum = QPushButton(cpu_NM) 
#    odyimum.setStyleSheet = ('QString', background-color: black; color: orange;)        
#    stultus = "background-color: black; color: orange;"
#    odyimum.setStyleSheet = (const QString &stultus)        
#    odyimum.setStyleSheet = (QtCore.QString ('background-color: black; color: orange;'))
#    odyimum.setStyleSheet(".QWidget {color: blue; background-color: yellow;}")
#    odyimum.setStyleSheet(".QPushButton {color:#F97902; background-color: black;}")
#    odyimum.setStyleSheet(".QPushButton {color: black; background-color:#F97902;}")
    odyimum.setStyleSheet(".QPushButton {color: black; background-color:#FF9900;}")
    odyimum.setFont(QFont('Verdana', 10))
#    stilus.setStyleSheet = ("background-color: black; color: orange;")
    iface.mainWindow().statusBar().addWidget(odyimum)  
#    iface.mainWindow().statusBar().setFont(QFont('Verdana', 20))  
    iface.mainWindow().statusBar().setFont(self, QFont('Verdana', 20))  
    
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
