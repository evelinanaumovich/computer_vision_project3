# Wildfire Classification 
For this project we took screenshots from public, live camera feeds that were recorded by ALERTCalifornia from two spots, Blue Ridge 1 and Santiago Peak 2.
We split out data into two classes in order to train our model, fire and no fire. We are using YOLO as our model in order to classify these images and future images from these
live camera feeds in order to automate the detection of possible wildfires. 

# Step 1: Gathering Data
We implemented a program called getData.py and ran it over a span of 10 hours to get enough data for both the cameras. This data was then put in data/coffeePotNoFire and data/santiagoPeakNoFire. For our fire videos we found the same webcams that had fire from youtube and uploaded the images that we took to data/coffeePotFire and data/santiagoPeakFire.

# Step 2: Training
To train our model we took out data and split it into test and train folders, both folders then had a sub devision of fire and no fire. Train is the images that we used to train our model with and Test is what we used to test out model. Train has 2200 images with fire and 328 without fire and out Test data has 628 images of fire and 94 without fire. 

Our model training code is in detectFires.py. For our model we API we used YOLOv8. 

We trained the model 5 seperate times for epocs all with around 85% accuracy. 

**Here are the outputs that we got:**
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

# How To Run 
In order to run our program you need to make sure to get set up in a virtual enviornment and download the requirements. 
 
To train a model using the dataset in the /Images folder, run the below command from the root folder
 ```
 python trainModel.py
 ```

 The output will be stored in the ./runs/classify/train4/ folder

 
