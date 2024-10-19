import cv2
import torch
import os
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def main():
    # Directory containing images
    image_folder = '/Users/evelinanaumovich/Desktop/computer vision/computer_vision_project3/data/santiagoPeakFire'
    
    # Iterate over all files in the directory
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Add other extensions if needed
            image_path = os.path.join(image_folder, filename)
            
            # Read the image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error: Could not read image {filename}.")
                continue
            
            # Perform inference
            results = model(image)
            
            # Print results
            results.print()  # Print detected objects
            
            # Check for fire detection
            detected = any(x in results.names for x in ['fire', 'smoke'])  # Modify as needed based on your model
            if detected:
                print(f"Fire detected in {filename}!")
            else:
                print(f"No fire detected in {filename}.")
            
            # Display the results
            cv2.imshow("YOLOv5 Detection", np.squeeze(results.render()))
            if cv2.waitKey(1000) & 0xFF == ord('q'):  # Display each image for 1 second
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
