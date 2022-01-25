"""
-*- coding: utf-8 -*-
@Time : 2021/10/25 下午 6:48
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""

from osgeo import gdal, gdalnumeric
from osgeo import ogr
from osgeo import gdal_array
from PIL import Image, ImageDraw


def imageToArray(i):
    a = gdal_array.numpy.fromstring(i.tobytes(), 'b')
    a.shape = i.im.size[1], i.im.size[0]
    return a


def world2Pixel(geoMatrix, x, y):
    ulX = geoMatrix[0]
    ulY = geoMatrix[3]
    xDist = geoMatrix[1]
    yDist = geoMatrix[5]
    pixel = int((x - ulX) / xDist)
    line = int((ulY - y) / abs(yDist))
    return (pixel, line)

source = "./NDVI-update/farm.tif"

target = "ndvi.tif"

srcArray = gdal_array.LoadFile(source)

srcImage = gdal.Open(source)
geoTrans = srcImage.GetGeoTransform()

r = srcArray[1]
ir = srcArray[2]
field = ogr.Open("./NDVI-update/field.shp")  # OGR

lyr = field.GetLayer("field")
# shapefile
poly = lyr.GetNextFeature()
# print(type(poly))
minX, maxX, minY, maxY = lyr.GetExtent()
ulX, ulY = world2Pixel(geoTrans, minX, maxY)
lrX, lrY = world2Pixel(geoTrans, maxX, minY)

pxWidth = int(lrX - ulX)
pxHeight = int(lrY - ulY)

clipped = gdal_array.numpy.zeros((3, pxHeight, pxWidth), gdal_array.numpy.uint8)

rclip = r[ulY:lrY, ulX:lrX]
irclip = ir[ulY:lrY, ulX:lrX]

geoTrans = list(geoTrans)
geoTrans[0] = minX
geoTrans[3] = maxY

points = []
pixels = []

geom = poly.GetGeometryRef()
pts = geom.GetGeometryRef(0)

for p in range(pts.GetPointCount()):
    points.append((pts.GetX(p), pts.GetY(p)))

for p in points:
    pixels.append(world2Pixel(geoTrans, p[0], p[1]))

rasterPoly = Image.new("L", (pxWidth, pxHeight), 1)
rasterize = ImageDraw.Draw(rasterPoly)
rasterize.polygon(pixels, 0)
# gdal_array
mask = imageToArray(rasterPoly)

rclip = gdal_array.numpy.choose(mask, (rclip, 0)).astype(gdal_array.numpy.uint8)
irclip = gdal_array.numpy.choose(mask, (irclip, 0)).astype(gdal_array.numpy.uint8)

gdal_array.numpy.seterr(all='ignore')
#
ndvi = 1.0 * ((irclip - rclip) / (irclip + rclip + 1.0))
# NaN 0
ndvi = gdal_array.numpy.nan_to_num(ndvi)
# NDVI
gdalnumeric.SaveArray(ndvi, target, format="GTiff", prototype=srcImage)

update = gdal.Open(target, 1)
update.SetGeoTransform(list(geoTrans))
update.GetRasterBand(1).SetNoDataValue(0.0)
update = None
print('NDVI ')
