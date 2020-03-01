---
title: Senses
created: 2015-12-12
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* When did the senses appear? For what purpose?
* Is it more tiring to listen to someone from one hear than from both (stereo vs mono)?
* We may be perceptually bounded by our sense organs (eyes accepting only a range of light frequencies, ears only accepting a range of sound frequencies) but the cortex could potentially support processing a wider range of information
* What would happen if someone plugged optic fiber (artificial) in someone optic fiber/nerve (natural)?

# Overview
Considering the finite architecture of the brain, we can postulate a few things:
* Any signal that will be transmitted by a neuron through its axon will be limited by the time it takes to complete an activation/deactivation cycle
	* Thus signal processing cannot be instantaneous
* There are only so many neurons in the brain, if we exclude recurrent neural network/cycles, then the brain has a maximal depth in terms of layers
	* At some point in the processing pipeline the visual image we perceive has to emerge/aggregate

# Sight
> The eye is not a single frame snapshot camera. It is more like a video stream. The eye moves rapidly in small angular amounts and continually updates the image in one's brain to "paint" the detail. We also have two eyes, and our brains combine the signals to increase the resolution further. We also typically move our eyes around the scene to gather more information. Because of these factors, the eye plus brain assembles a higher resolution image than possible with the number of photoreceptors in the retina. So the megapixel equivalent numbers below refer to the spatial detail in an image that would be required to show what the human eye could see when you view a scene.
>
> Based on the above data for the resolution of the human eye, let's try a "small" example first. Consider a view in front of you that is 90 degrees by 90 degrees, like looking through an open window at a scene. The number of pixels would be
> 90 degrees \* 60 arc-minutes/degree \* 1/0.3 \* 90 \* 60 \* 1/0.3 = 324,000,000 pixels (324 megapixels).
> At any one moment, you actually do not perceive that many pixels, but your eye moves around the scene to see all the detail you want. But the human eye really sees a larger field of view, close to 180 degrees. Let's be conservative and use 120 degrees for the field of view. Then we would see
> 120 \* 120 \* 60 \* 60 / (0.3 \* 0.3) = 576 megapixels.
> The full angle of human vision would require even more megapixels. This kind of image detail requires A large format camera to record.[^1]

---

> 7 MP for the fovea region + 1 MP for the rest of the field of view[^2] (citation needed)

---

> The human retina contains about 120 million rod cells and 6 million cone cells.[^3]

> The optic nerve is composed of retinal ganglion cell axons and glial cells. Each human optic nerve contains between 770,000 and 1.7 million nerve fibers, which are axons of the retinal ganglion cells of one retina. In the fovea, which has high acuity, these ganglion cells connect to as few as 5 photoreceptor cells; in other areas of retina, they connect to many thousand photoreceptors.[^4]

The following is not factual but only inferred from the information previously listed.
From this data one could infer there is a maximum of 120 megapixels of raw data per eye. However, the optic nerve is only composed of between 770,000 and 1.7 million nerve fibers, as a great amount of photoreceptors get merged into a single retinal ganglion cell which means that a good amount of the 120 megapixels gets aggregated before being transferred to the occipital lobe. If we consider that a nerve fiber is able to transport all the information required for the equivalent of a single pixel (which is unlikely), we've dropped from 120 megapixels down to 1.7 megapixels per eye.

# Hearing
In humans, the number of nerve fibers within the cochlear nerve averages around 30,000[^5].

# Smell

# Taste

# Touch

# See also

* [Recording information](../recording-information)

# References
[^1]: http://www.clarkvision.com/articles/eye-resolution.html
[^2]: https://www.youtube.com/watch?v=4I5Q3UXkGd0
[^3]: https://en.wikipedia.org/wiki/Photoreceptor_cell
[^4]: https://en.wikipedia.org/wiki/Optic_nerve
[^5]: https://en.wikipedia.org/wiki/Cochlear_nerve
[^6]: https://en.wikipedia.org/wiki/Hearing_range

## Sight
* http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2826883/
* https://www.quora.com/Vision-eyesight-How-many-frames-per-second-do-humans-see
* https://www.quora.com/What-is-the-resolution-of-the-human-eye-in-megapixels
