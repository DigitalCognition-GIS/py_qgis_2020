# Code Source -- QGIS Python Programming Cook Book - Chapter -3 - Page 56
# QgsVectorLayer - Script being run from the QGIS - Python Console 
vectorLyr = QgsVectorLayer('Point?crs=epsg:4326&field=city:string(25)&field=population:nt', 'Layer 1' , "memory")
print(type(vectorLyr)) #<class 'qgis._core.QgsVectorLayer'>
print(vectorLyr)
vectorLyr.isValid() # True - when run directly in - QGIS - Python Console 

from collections import OrderedDict
fields = OrderedDict([('city','str(25)'),('population','int')])
print(fields)
path = '&'.join(['field={}:{}'.format(k,v) for k,v in fields.items()])
vectorLyr1 = QgsVectorLayer('Point?crs=epsg:4326&' + path, 'Layer 1' , "memory")
print(vectorLyr1)
# <QgsMapLayer: 'Layer 1' (memory)>
vectorLyr1.isValid() # True
#
