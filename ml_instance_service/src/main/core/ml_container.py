import os
from pathlib import Path, PosixPath;
from ultralytics import YOLO

def model_loader():
    model_path = Path("../../resources/ml_model/yolov8n.pt");
    model = YOLO(model_path);

    return model;

"""
@link https://docs.ultralytics.com/modes/predict/#key-features-of-predict-mode
"""
def predict(image_path):
    ml_model = model_loader();
    prediction_result = ml_model(image_path);
    # prediction_result.boxes;
    # prediction_result.masks;
    # prediction_result.keypoints;
    # prediction_result.probs;

    return prediction_result;
