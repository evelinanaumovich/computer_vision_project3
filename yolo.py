# import YOLO
from ultralytics import YOLO

# load a pretrained model
model = YOLO('yolov8n-cls.pt')

# Train the model
results = model.train(data="data", epochs=20, imgsz=500, patience=3)

# load a custom model
model = YOLO('runs/classify/train3/weights/best.pt')

# Validate the model
metrics = model.val()
metrics.top1

# list all file directories in path
path = 'Images'
files = [path+"/"+file for file in os.listdir(path)]

# predict images
results = model(files)
