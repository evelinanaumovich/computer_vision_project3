# import YOLO model
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-cls.pt') 

# Train the model
model.train(data='./Images', epochs=5)

# Validate the model
metrics = model.val()
metrics.top1 # top1 accuracy
metrics.top5 # top5 accuracy

results = model.predict('./Images/test/fire/frame209.jpg')

probs = result.probs
print(probs.data)
