---
title: Photo geolocation
created: 2020-02-15
taxonomy:
  type: post
  category: [Problems]
  status: finished
---

# Problem
I have taken a lot of pictures and I'd like to see where they were taken on a map. I also don't want to have to upload those pictures to a server.

# Solution
I've developed a simple tool called [Photo Geolocation](https://tomzx.github.io/photo-geolocation/) that is a small client-side application. It uses [leaflet](https://leafletjs.com/) to display the images on an [OpenStreetMap map](https://www.openstreetmap.org/). The EXIF image metadata is extracted from the image by reading the image data using [exif.js](https://github.com/exif-js/exif-js). From the EXIF image metadata we extract the GPS coordinates, which are then used to place a pin on the map at the appropriate location. It is possible to click on the pin to see what picture was taken at the provided location.

# Reference
* https://tomzx.github.io/photo-geolocation/
