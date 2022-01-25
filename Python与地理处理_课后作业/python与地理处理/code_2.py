"""
-*- coding: utf-8 -*-
@Time : 2021/10/25 下午 7:10
@Author : sunguoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""

from osgeo import gdal_array as gd
import operator
from functools import reduce


def histogram(a, bins=list(range(256))):
    fa = a.flat
    n = gd.numpy.searchsorted(gd.numpy.sort(fa), bins)
    n = gd.numpy.concatenate([n, [len(fa)]])
    hist = n[1:] - n[:-1]
    return hist

def stretch(a):
    hist = histogram(a)
    lut = []
    for b in range(0, len(hist), 256):
        step = reduce(operator.add, hist[b:b + 256]) / 255
        n = 0
        for i in range(256):
            lut.append(n / step)
            n += hist[i + b]
    gd.numpy.take(lut, a, out=a)
    return a


# NDVI
source = "./ndvi.tif"
target = "ndvi_color.tif"
ndvi = gd.LoadFile(source).astype(gd.numpy.uint8)
# NDVI
ndvi = stretch(ndvi)
# NDVI 3
rgb = gd.numpy.zeros((3, len(ndvi), len(ndvi[0])), gd.numpy.uint8)
# NDVI
classes = [58, 73, 110, 147, 184, 220, 255]

# lut RGB
lut = [[120, 69, 25], [255, 178, 74], [255, 237, 166], [173, 232, 94], [135, 181, 64], [3, 156, 0], [1, 100, 0]]

start = 1

for i in range(len(classes)):
    mask = gd.numpy.logical_and(start <= ndvi, ndvi <= classes[i])
    for j in range(len(lut[i])):
        rgb[j] = gd.numpy.choose(mask, (rgb[j], lut[i][j]))
        start = classes[i] + 1

# NDVI geotiff
output = gd.SaveArray(rgb, target, format="GTiff", prototype=source)
output = None
print('分类完成!')
