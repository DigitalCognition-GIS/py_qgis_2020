#!/usr/bin/env python
# Lint as: python3
"""Compute hillshade from elevation."""

import math
import ee
import ee.mapclient

ee.Initialize()
ee.mapclient.centerMap(-121.767, 46.852, 11)


def Radians(img):
    radians_var = img.toFloat().multiply(math.pi).divide(180)
    print(radians_var)
    return img.toFloat().multiply(math.pi).divide(180)


def Hillshade(az, ze, slope, aspect):
  """Compute hillshade for the given illumination az, el."""
  azimuth = Radians(ee.Image(az))
  print(type(azimuth)) # horizontal plane - direction in degrees ( 90 , 180 etc )

  zenith = Radians(ee.Image(ze)) # Directly above - straight up from the Horizontal Plane 
  # Hillshade = cos(Azimuth - Aspect) * sin(Slope) * sin(Zenith) +
  #     cos(Zenith) * cos(Slope)
  return (azimuth.subtract(aspect).cos()
          .multiply(slope.sin())
          .multiply(zenith.sin())
          .add(zenith.cos().multiply(slope.cos())))

terrain = ee.Algorithms.Terrain(ee.Image('CGIAR/SRTM90_V4'))
slope_img = Radians(terrain.select('slope'))
print(type(slope_img))
aspect_img = Radians(terrain.select('aspect'))

# Add 1 hillshade at az=0, el=60.
ee.mapclient.addToMap(Hillshade(0, 60, slope_img, aspect_img))
