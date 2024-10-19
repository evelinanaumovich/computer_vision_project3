* * Wildfire Classification 
* For this project we took videos that were recorded by ALERTCalifornia from two spots, Blue Ridge 1 and Santiago Peak 2.
* We split out data into two classes in order to train our model, fire and no fire. We are using YOLO as our model in order to classify these images. 

* * Step 1: Gathering Data
* We implemented a program called getData.py and ran it over a span of 10 hours to get enough data for both the cameras. This data was then put in data/coffeePotNoFire and data/santiagoPeakNoFire. For our fire videos we found the same webcams that had fire from youtube and uploaded the images that we took to data/coffeePotFire and data/santiagoPeakFire.

* * Step 2: Training
* In order to train our model we took out data and split it into test and train folders, both folders then had a sub devision of fire and no fire. Train is the images that we used to train our model with and Test is what we used to test out model. Train has 2200 images with fire and 328 without fire and out Test data has 628 images of fire and 94 without fire. 

* * Step 3: Implementation 
* 