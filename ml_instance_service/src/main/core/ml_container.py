import os
from pathlib import Path;
from ultralytics import YOLO



def model_loader():
    model_path = Path(os.path.dirname(os.path.realpath(__file__)) + "../../resources/ml_model/yolov8n.pt");
    model = YOLO.load(model_path);

    return model;
    
"""
@link https://docs.ultralytics.com/modes/predict/#key-features-of-predict-mode
"""
def predict(image_path):
    model = model_loader();

    prediction_result = model(image_path);
    # prediction_result.boxes;
    # prediction_result.masks;
    # prediction_result.keypoints;
    # prediction_result.probs;

    return prediction_result;
