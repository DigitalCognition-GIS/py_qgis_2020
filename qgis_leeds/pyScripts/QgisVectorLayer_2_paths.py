# Code Source -- QGIS Python Programming Cook Book - Chapter -3 - Page 59
# QgsVectorLayer - Script being run from the QGIS - Python Console 

vectorLyr2 = QgsVectorLayer('/home/dhankar/_dc_all/QGIS_backUp/py_qgis_2020/qgis_leeds/Data/paths/paths.shp','Paths',"ogr")
print(type(vectorLyr2)) #<class 'qgis._core.QgsVectorLayer'> 
vectorLyr2.isValid()
vpr_dataProv = vectorLyr2.dataProvider()
print(type(vpr_dataProv)) # <class 'qgis._core.QgsVectorDataProvider'>
# init - empty List - append Points for a new line 
points = []
points.append(QgsPoint(430841,5589485))
points.append(QgsPoint(432438,5575114))
points.append(QgsPoint(447252,5567663))
#
#create  QgsGeometry object from the line:
line_QgsGeometry = QgsGeometry.fromPolyline(points)
print(type(line_QgsGeometry)) # <class 'qgis._core.QgsGeometry'>
print(line_QgsGeometry) # <QgsGeometry: LineString (430841 5589485, 432438 5575114, 447252 5567663)>
#
#Creating a feature == QgsFeature_1 , setting geometry == line_QgsGeometry
QgsFeature_1 = QgsFeature()
QgsFeature_1.setGeometry(line_QgsGeometry)
print(type(QgsFeature_1))

#Add , feature == QgsFeature_1 ,   to  layer data provider -- update the extent...
vpr_dataProv.addFeatures([QgsFeature_1])
vectorLyr2.updateExtents()
print(type(vectorLyr2))
# <class 'qgis._core.QgsFeature'>
# <class 'qgis._core.QgsVectorLayer'>
### https://qgis.org/pyqgis/3.0/core/Vector/QgsVectorLayer.html
### https://qgis.org/api/classQgsVectorLayer.html

### Source == https://docs.qgis.org/3.4/pdf/en/QGIS-3.4-PyQGISDeveloperCookbook-en.pdf
# "layer" is a QgsVectorLayer instance
for field in vectorLyr2.fields():
    print(field.name()) #id Integer64
    print(field.typeName()) # PATH String

### Source == https://docs.qgis.org/3.4/pdf/en/QGIS-3.4-PyQGISDeveloperCookbook-en.pdf
layer_active = iface.activeLayer()
layer_active_features = layer_active.getFeatures()
print(layer_active_features)
# Below Error in the QGIS Python Console - as we had a RASTER Layer as the ACtive Layer - we need a VECTOR Layer instead..
"""
Traceback (most recent call last):
  File "/usr/lib/python3.6/code.py", line 91, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
  File "<string>", line 42, in <module>
AttributeError: 'QgsRasterLayer' object has no attribute 'getFeatures'
"""
#









