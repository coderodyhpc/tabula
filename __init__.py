from qgis.core import QgsCoordinateReferenceSystem, QgsProject

def classFactory(iface):

    from tabula.plugin.mainPlugin import QGISPlugin
    novus_CRS = '+proj=lcc +lat_1=33.0 +lat_2=60.0 +lat_0=40.0 +lon_0=-97.0 +datum=WGS84 +no_defs'
    crs = QgsCoordinateReferenceSystem.fromProj4(novus_CRS)
    qgsProject = QgsProject.instance() 
    qgsProject.setCrs(novus_crs)
    return QGISPlugin(iface)

def dummy_menu():
    pass
