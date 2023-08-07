from typing import Optional, List, Iterable, Tuple, Any, Union
from qgis.gui import QgisInterface, QgsMapCanvas, QgsMapCanvasItem

from qgis.core import QgsCoordinateReferenceSystem, QgsProject, QgsLayerTree, QgsRasterLayer, QgsApplication

#import os
#import sys

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||            SECTION TO CHANGE THE PROJECTION                 ||||||||||||||| 
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#def mutatio(lex):   
#    novus_CRS = QgsCoordinateReferenceSystem.fromProj4(lex)
#    qgsProject = QgsProject.instance() 
#    qgsProject.setCrs(novus_CRS)
    
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||            SECTION TO PLOT BOUNDARY(IES)                 ||||||||||||||| 
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||            SECTION FOR NESTED DOMAINS ?????                 ||||||||||||||| 
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#def zoom_out_to_layer(canvas: QgsMapCanvas, layer: QgsVectorLayer) -> None:
#    settings = canvas.mapSettings() # type: QgsMapSettings
#    new_extent = settings.layerExtentToOutputExtent(layer, layer.extent()) # type: QgsRectangle
#    new_extent.scale(1.05)

#    old_extent = canvas.extent() # type: QgsRectangle

#    if old_extent.contains(new_extent):
#        return

#    canvas.setExtent(new_extent)
#    canvas.refresh()

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||            SECTION TO PLOT LAYERS                 ||||||||||||||| 
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#def tabulas(uris_and_names: List[Tuple[str,str,Optional[str]]], group_name=None,
#                visible: Union[bool,int]=0, expanded: bool=True) -> List[QgsRasterLayer]:
##    time_0 = time.time()
#    registry = QgsProject.instance() # type: QgsProject
#    root = registry.layerTreeRoot() # type: QgsLayerTree
#    if group_name:
#        group = root.findGroup(group_name) # type: QgsLayerTreeGroup
#        if group is None:
#            group = root.insertGroup(0, group_name)
#            group.setExpanded(expanded)
#            visibility = (type(visible) == bool and visible) or (type(visible) == int)
#            group.setItemVisibilityChecked(visibility)
#        else:
#            group.removeAllChildren()
##    time_1 = time.time()
##    print ("TIME 1 ",time_1-time_0)
#    layers = []
#    for i, (uri, name, short_name) in enumerate(uris_and_names):
##        time_2 = time.time()
##        print ("TIME 2 ",time_2-time_1)
#        layer = QgsRasterLayer(uri, name)
##        time_3 = time.time()
##        print ("TIME 3 ",time_3-time_2)
        
#        if short_name:
#            layer.setShortName(short_name)
##        fix_style(layer)
#        registry.addMapLayer(layer, False)
#        if group_name:
#            layer_node = group.addLayer(layer) # type: QgsLayerTreeLayer
#            visibility = (type(visible) == bool) or (type(visible) == int and i == visible)
#        else:
#            layer_node = root.insertLayer(0, layer)
#            visibility = (type(visible) == bool and visible) or (type(visible) == int and i == visible)
#        layer_node.setItemVisibilityChecked(visibility)
#        layers.append(layer)
##        time_5 = time.time()
##        print ("TIME 5 ",time_5-time_3)

#    return layers

#def fix_style(layer: QgsRasterLayer) -> None:
#    provider = layer.dataProvider() # type: QgsRasterDataProvider
#    color_interp = provider.colorInterpretation(1)
#    is_palette = color_interp == QgsRaster.PaletteIndex
#    renderer = layer.renderer() # type: QgsRasterRenderer
#    new_renderer = None
#    if is_palette:
#        color_table = provider.colorTable(1)
#        classes = QgsPalettedRasterRenderer.colorTableToClassData(color_table)
#        if not any(c.label == '__UNUSED__' for c in classes):
#            return
#        new_classes = filter(lambda c: c.label != '__UNUSED__', classes)
#        new_renderer = QgsPalettedRasterRenderer(renderer.input(), 1, new_classes)
#        layer.setRenderer(new_renderer)
#    else:
#        if not isinstance(renderer, QgsSingleBandGrayRenderer):
#            new_renderer = QgsSingleBandGrayRenderer(renderer.input(), 1)
#            layer.setRenderer(new_renderer)
#            layer.setDefaultContrastEnhancement() # must be *after* setting the renderer

def get_raster_layers_in_group(group_name: str) -> List[QgsRasterLayer]:
    registry = QgsProject.instance() # type: QgsProject
    root = registry.layerTreeRoot() # type: QgsLayerTree

    group = root.findGroup(group_name) # type: QgsLayerTreeGroup
    if group is None:
        return []
    layers = [tree_layer.layer()
              for tree_layer
              in group.findLayers()
              if isinstance(tree_layer.layer(), QgsRasterLayer)]
    return layers

def remove_group(group_name: str) -> None:
    registry = QgsProject.instance() # type: QgsProject
    root = registry.layerTreeRoot() # type: QgsLayerTree
    group = root.findGroup(group_name) # type: QgsLayerTreeGroup
    if group is None:
        return
    root.removeChildNode(group)    

#def switch_band(layer: QgsRasterLayer, index: int) -> None:
#    renderer = layer.renderer().clone() # type: QgsRasterRenderer
#    renderer.setInput(layer.renderer().input())
#    if isinstance(renderer, QgsSingleBandGrayRenderer):
#        renderer.setGrayBand(index + 1)
#    elif isinstance(renderer, QgsPalettedRasterRenderer):
#        # TODO need to replace renderer to set new band
#        pass
#    elif isinstance(renderer, QgsSingleBandPseudoColorRenderer):
#        renderer.setBand(index + 1)
#    layer.setRenderer(renderer)
#    layer.triggerRepaint()
    

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||| LEGENDA||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class Legenda00(QgsMapCanvasItem):
    def __init__(self, canvas, numeri_0, titulus, unitas):
        super().__init__(canvas)
        self.numeri_0 = numeri_0
        self.titulus = titulus 
        self.unitas = unitas
        self.altitudo = 12
        self.longitudo = 40
        
    def setCenter(self, center):
        self.center = center

    def center(self):
        return self.center

    def paint(self, painter, option, widget):
        imum_sinister = [25, 750]
        painter.setPen(QColor(Qt.white))
        painter.drawRect(imum_sinister[0]-5, imum_sinister[1]-10-(3*self.altitudo), 150, 3*self.altitudo+15)
        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-7-(2*self.altitudo), self.titulus)
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-7-(self.altitudo), self.unitas)
        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        aaa = str(self.numeri_0)
        painter.drawText(imum_sinister[0]+self.longitudo+5, imum_sinister[1]-2, "0")
        painter.fillRect(imum_sinister[0], imum_sinister[1]-self.altitudo, self.longitudo, self.altitudo, QColor(0, 0, 0))          

class Legenda15(QgsMapCanvasItem):
    def __init__(self, canvas, numeri, titulus, unitas):
        super().__init__(canvas)
        self.numeri = numeri
        self.titulus = titulus 
        self.unitas = unitas
        self.altitudo = 12
        self.longitudo = 40
        
    def setCenter(self, center):
        self.center = center

    def center(self):
        return self.center

    def paint(self, painter, option, widget):
        imum_sinister = [25, 750]
        painter.setPen(QColor(Qt.white))
        painter.drawRect(imum_sinister[0]-5, imum_sinister[1]-(17*self.altitudo)-10, 140, 17*self.altitudo+20)
        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-7-(16*self.altitudo), self.titulus)
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-7-(15*self.altitudo), self.unitas)
        for iii in range(15):
            painter.setPen(QColor(Qt.white))
            painter.setFont(QFont('Verdana', self.altitudo-2))
            aaa = str(self.numeri[iii])
            painter.drawText(imum_sinister[0]+self.longitudo+5, imum_sinister[1]-2-(iii*self.altitudo), aaa[:14])
            if iii == 0:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(0, 0, 255))          
            elif iii == 1:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(36, 36, 255))          
            elif iii == 2:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(73, 73, 255))          
            elif iii == 3:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(109, 109, 255))          
            elif iii == 4:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(146, 146, 255))          
            elif iii == 5:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(182, 182, 255))          
            elif iii == 6:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(219, 219, 255))          
            elif iii == 7:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 255, 255))          
            elif iii == 8:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 219, 219))          
            elif iii == 9:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 182, 182))          
            elif iii == 10:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 146, 146))          
            elif iii == 11:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 109, 109))          
            elif iii == 12:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 73, 73))          
            elif iii == 13:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 36, 36))          
            elif iii == 14:
                painter.fillRect(imum_sinister[0], imum_sinister[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 0, 0))          

class Legenda11(QgsMapCanvasItem):
    def __init__(self, canvas, numeri, titulus, unitas):
        super().__init__(canvas)
        self.numeri = numeri
        self.titulus = titulus 
        self.unitas = unitas
        self.altitudo = 12
        self.longitudo = 40
        
    def setCenter(self, center):
        self.center = center

    def center(self):
        return self.center

    def paint(self, painter, option, widget):
        imum_sinister11 = [25, 750]
        painter.setPen(QColor(Qt.white))
        painter.drawRect(imum_sinister11[0]-5, imum_sinister11[1]-(13*self.altitudo)-10, 130, 13*self.altitudo+20)
        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        painter.drawText(imum_sinister11[0]+5, imum_sinister11[1]-7-(12*self.altitudo), self.titulus)
        painter.drawText(imum_sinister11[0]+5, imum_sinister11[1]-7-(11*self.altitudo), self.unitas)
        for iii in range(11):
            painter.setPen(QColor(Qt.white))
            painter.setFont(QFont('Verdana', self.altitudo-2))
            aaa = str(self.numeri[iii])
            painter.drawText(imum_sinister11[0]+self.longitudo+5, imum_sinister11[1]-2-(iii*self.altitudo), aaa[:14])
            if iii == 0:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(41, 27, 45))          
            elif iii == 1:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(78,141,73))          
            elif iii == 2:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(114, 254, 101))          
            elif iii == 3:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(179,228,72))          
            elif iii == 4:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(243, 201, 43))          
            elif iii == 5:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(248,154,34))          
            elif iii == 6:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(252, 106, 25))          
            elif iii == 7:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(218,69,17))          
            elif iii == 8:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(184, 32, 8))          
            elif iii == 9:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(164, 22, 4))          
            elif iii == 10:
                painter.fillRect(imum_sinister11[0], imum_sinister11[1]-((iii+1)*self.altitudo), self.longitudo, self.altitudo, QColor(144, 12, 0))          
    
    
class Legenda0(QgsMapCanvasItem):
    def __init__(self, canvas, numeri_0, titulus, unitas):
        super().__init__(canvas)
        self.numeri_0 = numeri_0
        self.titulus = titulus 
        self.unitas = unitas
        self.altitudo = 12
        self.longitudo = 40
        
    def setCenter(self, center):
        self.center = center

    def center(self):
        return self.center

    def paint(self, painter, option, widget):
        imum_sinister = [25, 750]
        painter.setPen(QColor(Qt.white))
        painter.drawRect(imum_sinister[0]-5, imum_sinister[1]-10-(3*self.altitudo), 150, 2*self.altitudo+15)
        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-7-(2*self.altitudo), self.titulus)
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-7-(self.altitudo), self.unitas)
        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        aaa = str(self.numeri_0)
        painter.drawText(imum_sinister[0]+self.longitudo+5, imum_sinister[1]-2, "0")
        painter.fillRect(imum_sinister[0], imum_sinister[1]-self.altitudo, self.longitudo, self.altitudo, QColor(0, 0, 0))          

class Legenda100(QgsMapCanvasItem):
    def __init__(self, canvas, numeri_100, titulus, unitas):
        super().__init__(canvas)
        self.numeri_100 = numeri_100
        self.titulus = titulus 
        self.unitas = unitas
        self.altitudo = 12
        self.longitudo = 40
        
    def setCenter(self, center):
        self.center = center

    def center(self):
        return self.center

    def paint(self, painter, option, widget):
        imum_sinister = [25, 750]
        painter.setPen(QColor(Qt.white))
        painter.drawRect(imum_sinister[0]-5, imum_sinister[1]-10-(2*self.altitudo), 150, 2*self.altitudo+15)
        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Verdana', self.altitudo-2))
#        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-7-(2*self.altitudo), self.titulus)
        painter.drawText(imum_sinister[0]+5, imum_sinister[1]-7-(self.altitudo), self.titulus)
        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Verdana', self.altitudo-2))
        aaa = str(self.numeri_100)
        painter.drawText(imum_sinister[0]+self.longitudo+5, imum_sinister[1]-2, self.numeri_100)
        painter.fillRect(imum_sinister[0], imum_sinister[1]-self.altitudo, self.longitudo, self.altitudo, QColor(0, 0, 255))          

class Legenda12(QgsMapCanvasItem):
    def __init__(self, canvas, numeri, titulus, unitas):
        super().__init__(canvas)
        self.numeri = numeri
        self.titulus = titulus 
        self.unitas = unitas
        self.altitudo = 12
        self.longitudo = 40
        
    def setCenter(self, center):
        self.center = center

    def center(self):
        return self.center

    def paint(self, painter, option, widget):
        imum_sinister12 = [25, 750]
#        if self.pigmem_leg == "albinus":
        painter.setPen(QColor(Qt.white))
#        else:
#            painter.setPen(QColor(Qt.black))
#        painter.drawRect(imum_sinister12[0]-5, imum_sinister12[1]-(16*self.altitudo), 135, 14*self.altitudo+5)
        painter.drawRect(imum_sinister12[0]-5, imum_sinister12[1]-(17*self.altitudo), 135, 15*self.altitudo+5)
        painter.setFont(QFont('Verdana', self.altitudo-2))
        titulusI, titulusII = self.titulus.split (' in ', 1)
        titulusIII = '(' + titulusII.strip() +')' 
#        painter.drawText(imum_sinister12[0]+5, imum_sinister12[1]-7-(15*self.altitudo), self.titulus)
        painter.drawText(imum_sinister12[0]+5, imum_sinister12[1]-7-(15*self.altitudo), titulusI)
        painter.drawText(imum_sinister12[0]+5, imum_sinister12[1]-7-(14*self.altitudo), titulusIII)
        painter.drawText(imum_sinister12[0]+5, imum_sinister12[1]-7-(13*self.altitudo), self.unitas)
        for iii in range(12):
 #           if self.pigmem_leg == "albinus":
            painter.setPen(QColor(Qt.white))
 #           else:
 #               painter.setPen(QColor(Qt.black))
            painter.setFont(QFont('Verdana', self.altitudo-2))
            aaa = str(self.numeri[iii])
#            nuntium_sci = ('{:.6e}'.format(self.numeri[iii]))
#            print ("NUNTIUM_SCI ",nuntium_sci,type(nuntium_sci))
            painter.drawText(imum_sinister12[0]+self.longitudo+5, imum_sinister12[1]-2-((iii+2)*self.altitudo), aaa[:10])
#            painter.drawText(imum_sinister12[0]+self.longitudo+5, imum_sinister12[1]-2-((iii+2)*self.altitudo), nuntium_sci)
            if iii == 0:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 255, 255))          
            elif iii == 1:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(38, 115, 0))          
            elif iii == 2:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(56, 168, 0))          
            elif iii == 3:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(85, 255, 0))          
            elif iii == 4:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(152, 230, 0))          
            elif iii == 5:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(209, 255, 115))          
            elif iii == 6:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 235, 175))          
            elif iii == 7:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(204, 204, 204))          
            elif iii == 8:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 167, 127))          
            elif iii == 9:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(255, 0, 0))          
            elif iii == 10:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(168, 0, 0))          
            elif iii == 11:
                painter.fillRect(imum_sinister12[0], imum_sinister12[1]-((iii+3)*self.altitudo), self.longitudo, self.altitudo, QColor(115, 38, 0))          

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# CMAQ PINGERE
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def CMAQ_Lambert_geo(ancilla) -> Tuple[float,float,float,float,float,float]:
    wrf_dataset = nc.Dataset(ancilla.point_wrfout)
    CMAQ_crs = CRS(ancilla.lex)
    lons_u = wrf_dataset.variables['XLONG_U']
    lons_v = wrf_dataset.variables['XLONG_V']
    lats_u = wrf_dataset.variables['XLAT_U']
    lats_v = wrf_dataset.variables['XLAT_V']
    dim_x = wrf_dataset.dimensions['west_east'].size
    dim_y = wrf_dataset.dimensions['south_north'].size
    t = 0
    proj_id = wrf_dataset.getncattr('MAP_PROJ')
    inferior_sinister_I = LonLat(lon=ancilla.CMAQ_lon[0,0], lat=ancilla.CMAQ_lat[0,0])
    superior_sinister_I = LonLat(lon=ancilla.CMAQ_lon[-1,0], lat=ancilla.CMAQ_lat[-1,0])
    inferior_dextera_I = LonLat(lon=ancilla.CMAQ_lon[0,-1], lat=ancilla.CMAQ_lat[0,-1])
    superior_dextera_I = LonLat(lon=ancilla.CMAQ_lon[-1,-1], lat=ancilla.CMAQ_lat[-1,-1])
    inferior_sinister = CMAQ_crs.to_xy(inferior_sinister_I)
    superior_sinister = CMAQ_crs.to_xy(superior_sinister_I)
    inferior_dextera = CMAQ_crs.to_xy(inferior_dextera_I)
    superior_dextera = CMAQ_crs.to_xy(superior_dextera_I)
    cmaq_dx = (inferior_dextera.x - inferior_sinister.x) / (ancilla.nx[0]-1)
    cmaq_dy = (superior_sinister.y - inferior_sinister.y) / (ancilla.ny[0]-1)
    ancilla.CMAQ_geo_transform = (0.5*(inferior_sinister.x+superior_sinister.x), cmaq_dx, 0, 0.5*(superior_sinister.y+superior_dextera.y), 0, -cmaq_dy)
    Cgeo_transform = (0.5*(inferior_sinister.x+superior_sinister.x), cmaq_dx, 0, 0.5*(superior_sinister.y+superior_dextera.y), 0, -cmaq_dy)
    return Cgeo_transform
    
