# Gv3GEWRF 
# Copyright (c) Odycloud.

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
    out: Gv3GEWRF.plugin.QGISPlugin
    I have gotten rid of the bootstrap component
    """

    from Gv3GEWRF.plugin.plugin import QGISPlugin
    return QGISPlugin(iface)


