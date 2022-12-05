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
    new_title = title.replace('QGIS', 'TABULA')
    iface.mainWindow().setWindowTitle(new_title)
    iface.mainWindow().removeToolBar(toolbar)
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
