import time;
from glob import glob;
from pathlib import Path;
from core.ml_container import predict;
import cv2;
from math import floor;

"""
@todo:
Make the code that not using spark and using spark. Just in case you fucked up with spark.
"""
def handle_datalake_puller(args: str): 
    print("Starting datalake storage watcher. . .");

    STORAGE_PATH = "/Users/yosuakristianto/Documents/storage";

    while(True):
        files = [*glob((STORAGE_PATH + "/datalake/*"))];
        
        for file in files:
            print("Processing ", file);

            # Retrieve args input from python cli
            if(args == "no"):
                # 1. Prepare the actual file path to the memory
                # 2. Call YOLO Instance to predict the images
                # 3. Use the bbox to crop the image
                # 4. Save the cropped image to the post procesed folder

                # Get the image from path as 
                frame = cv2.imread(file)

                # Get the filename from the path

                results = predict(frame)[0];

                # Extract the boundary box
                x, y, w, h, score, class_id = results.boxes.data[0]

                # Crop the image and save the image to the post-processed folder with same name as retrieved filename 
                cv2.imwrite("/Users/yosuakristianto/Documents/storage/post-processed/output.jpg", frame[floor(y):floor(y+h), floor(x):floor(x+w)]); 
            

                # Call out message broker to Tesseract to extract the text from the image. 

            else:
                # 1. Prepare the actual file to Spark
                # 2. Call YOLO Instance to predict the images
                # 3. Use the bbox to crop the image
                # 4. Save the cropped image to the post procesed folder

                raise Exception("handle_datalake_puller with args \"yes\" is not yet implemented!");

        # Sleep for 5 seconds
        time.sleep(5);
    