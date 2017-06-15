---
title: Life recording
created: 2017-06-14
taxonomy:
  category: [Artificial General Intelligence]
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
* Record computer audio (anything that is played on the computer)
* Record the current active application and document (using [ManicTime](http://www.manictime.com/))
	* Use [ManicTimePHP](https://github.com/ManicTimeTools/ManicTimePHP) to analyze the data
* Record mouse clicks and pressed keyboard keys (using [Mousotron](http://www.blacksunsoftware.com/mousotron.html))

## Things I'd like to record
* Record both monitor as videos, which would allow for more granularity and to associate what is on screen with possible changes in emotion in the webcam feed for example

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

# See also

# References
