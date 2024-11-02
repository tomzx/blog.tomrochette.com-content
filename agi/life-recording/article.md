---
title: Life recording
created: 2017-06-14
taxonomy:
  tag: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# What I record
* Record both monitor screen at a 1m interval (using [Auto Screen Capture](https://github.com/gavinkendall/autoscreen))
	* Each 1920x1080 image (in JPG format) takes about 600 KB, 36 MB per hour, thus a full day could amount to approximately 864 MB per monitor
* Record webcam at 720p resolution (using fragmented mp4 to avoid unrecoverable file in case of file crash or application crash) (using [ffmpeg](https://ffmpeg.org/) and a [Logitech C920](https://www.logitech.com/en-ca/product/hd-pro-webcam-c920))
	* This records both a video stream and an audio stream
	* Depending on the uniformity of the background captured by your webcam, an hour of recording generally averages to about 175 MB
* Record computer audio (anything that is played on the computer, using ffmpeg)
* Record the current active application and document (using [ManicTime](http://www.manictime.com/))
	* Use [ManicTimePHP](https://github.com/ManicTimeTools/ManicTimePHP) to analyze the data
* Record mouse clicks and pressed keyboard keys (using [Mousotron](http://www.blacksunsoftware.com/mousotron.html))
* Record latitude/longitude (using Google Android (on my Nexus 5) + [Takeout](https://takeout.google.com/settings/takeout))
* Record exercises progression (using Microsoft Excel)
* Record thoughts and ideas (using [Google Keep](https://keep.google.com) while on the move, otherwise [Sublime Text](https://www.sublimetext.com/))
* Various computer metrics, such as CPU usage, memory usage, cpu/gpu/hdd temperature (using [Open Hardware Monitor](http://openhardwaremonitor.org/))

## Things I'd like to record
* Record both monitor as videos, which would allow for more granularity and to associate what is on screen with possible changes in emotion in the webcam feed for example
* Room temperature, pressure, humidity
* Personal heart rate, heart pressure (systolic/diastolic), sleep tracking (start, end, quality), steps (were previously tracked through Fitbit), blood pressure, sugar levels
* Weight, body fat percentage, water percentage, muscle percentage, bone weight
* What I eat (I've used [FatSecret for Android](https://play.google.com/store/apps/details?id=com.fatsecret.android&hl=en), but even with saved meals, it was time consuming to do tracking)
* Various personal mental metrics such as motivation, energy, hunger, happiness, anger, stress, productivity and comfort (I used to use [Data Tracker Reminder](https://github.com/tomzx/data-tracker-mobile), which I wrote myself, but it was time consuming to enter the data, and it would also interrupt my work flow)
* When I go to the bathroom to urinate and defecate
* When I drink water or a beverage, and how much
* Track everything that isn't on the computer (transit, walking, running, cooking, showering, etc.) to avoid to manually have to enter this information

# Content extraction
* Most of the monitor capture and webcam capture will contain mundane content such as someone fixating its monitor and sometimes uttering words
* It is thus essential to have software that can go through this mountain of data and extract the "anomalies" within this data, that is, the parts that are unique compared to the rest of the content
* It's also important to make the content easy to search, and thus to index
	* Text needs to be extracted from images and videos
	* Speech should be converted to text
		* Speakers should be identified and sentences should be prefixed by the speaker (similar to how it is done in dialogs)
	* Meta data should be automatically added to saved files, such as the date and time

# Things that can be extracted
* There's a lot of information about computer usage, such as the most used program, most visited websites, their frequency, when they are visited, and so on
* Diverse information about the computer user, such as tiredness, overall emotion, posture, tics, various activities such as eating, brushing your teeth, drinking water (or any other beverage),
* Because most of the face is recorded on a daily basis, changes to it can be observed and recorded
* Search engine queries (what you search)

# Things that needs to be fixed
* Synchronize the webcam feed (video + audio) with the computer audio feed, as well as the monitor screenshots

# What do I want to get out of logging?
* Earlier health diagnosis
* The ability to recall information that was perceived by sensors years in the past with good accuracy and perfect recall
* Records of some of my physical features in order to evaluate if there have been noticeable changes to them
	* Redness under the eyes
	* Hair loss
	* Acne
	* Dark skin spots (diameter and darkness, possible precursor of cancer)
* When I had a given illness, how long it lasted and what I might have used to treat it
* The ability to subjectively evaluate whether I do certain activities too much compared to a given figure I give myself

# How I process and centralize data
* I try to keep the data in text format as much as possible (using YAML for formatted/structured data)
* A module per input source is written, which obtains the data from the data source and converts the relevant information/data into bits of information that can be used by the generalized system

# See also

# References
