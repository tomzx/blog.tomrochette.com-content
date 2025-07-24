---
title: Photo geolocation
created: 2020-02-15
taxonomy:
  type: post
  tag: [problems, tool]
  status: finished
---

# Problem
I have taken a lot of pictures and I'd like to see where they were taken on a map. I also don't want to have to upload those pictures to a server or download some software.

# Solution
I've developed a simple tool called [Photo geolocation](https://tomzx.github.io/photo-geolocation/) which is a small client-side application. It uses [leaflet](https://leafletjs.com/) to display the images on an [OpenStreetMap map](https://www.openstreetmap.org/). The EXIF image metadata is extracted from the image by reading the image data using [exif.js](https://github.com/exif-js/exif-js). From the EXIF image metadata we extract the GPS coordinates, which are then used to place a pin on the map at the appropriate location. It is possible to click on the pin to see what picture was taken at the provided location.

To use the tool, simply go to the website and drag and drop your images on the page. The images will be read by your browser, the EXIF image metadata read directly by the browser (nothing being sent to a server). The images with GPS coordinates will have a pin displayed on the map at the location they were taken, while those that do not have GPS coordinates will be simply logged to the browser console and not displayed.

# Reference
* https://tomzx.github.io/photo-geolocation/
