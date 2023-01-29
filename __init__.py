from qgis.core import QgsCoordinateReferenceSystem, QgsProject

def classFactory(iface):

    from tabula.plugin.mainPlugin import QGISPlugin
    novus_CRS = '+proj=lcc +lat_1=33.0 +lat_2=60.0 +lat_0=40.0 +lon_0=-97.0 +x_0=-792000.0 +y_0=1080000.0 +datum=WGS84 +no_defs'
    qgsProject = QgsProject.instance() 
    qgsProject.setCrs(novus_CRS)
    return QGISPlugin(iface)

def dummy_menu():
    pass
