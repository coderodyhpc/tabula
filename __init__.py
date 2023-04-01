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
    title = iface.mainWindow().windowTitle()
    new_title = title.replace('QGIS', 'TABULA')
    iface.mainWindow().setWindowTitle(new_title)
    vector_menu = iface.vectorMenu()
#    menubar = vector_menu.parentWidget()
#    menubar.removeAction(vector_menu.menuAction())
    return QGISPlugin(iface)

