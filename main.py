from ultralytics import YOLO

# load custom model with trained weights
model = YOLO("best.pt")
 
# run inference for all files in the data dir
results = model(source="data/*",show=True)

