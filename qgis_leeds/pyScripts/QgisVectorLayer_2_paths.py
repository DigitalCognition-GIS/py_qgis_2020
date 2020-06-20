# Code Source -- QGIS Python Programming Cook Book - Chapter -3 - Page 59
# QgsVectorLayer - Script being run from the QGIS - Python Console 

vectorLyr2 = QgsVectorLayer('/home/dhankar/_dc_all/QGIS_backUp/py_qgis_2020/qgis_leeds/Data/paths/paths.shp','Paths',"ogr")
print(type(vectorLyr2)) #<class 'qgis._core.QgsVectorLayer'>
vectorLyr2.isValid()