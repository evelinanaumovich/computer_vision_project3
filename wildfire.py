import requests
import cv2
import torch
import os
import time
import numpy as np
from PIL import Image
from io import BytesIO

# Function to download an image
def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print(f"Failed to download image from {url}")
        return None

# Load YOLOv5 model (you can use 'yolov5s.pt', 'yolov5m.pt', etc.)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Set the camera URL
camera_url = "https://i0.wp.com/eos.org/wp-content/uploads/2024/07/wildfire.jpg?fit=1200%2C675&ssl=1" 

# Main function
def main():
    while True:
        # Download the image
        img = download_image(camera_url)
        if img:
            # Convert to a format YOLOv5 can work with
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            # Perform inference
            results = model(img_cv)

            # Print results
            results.print()  # Print detected objects
            results.save()   # Save the results

            # Display the results (optional)
            cv2.imshow("YOLOv5 Detection", results.ims[0])
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Sleep for a while before fetching the next image
        time.sleep(20)  # Adjust as necessary

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


# Object Detection: YOLOv5 will identify objects based on the pre-trained weights. If you want to specifically detect fire and smoke, consider fine-tuning the model with labeled data related to wildfires.

# Loop: The script will continually fetch images every 20 seconds. Adjust the sleep time as needed.

# Displaying Results: The script will display the detected image in a window. Press 'q' to exit.

