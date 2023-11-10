from kafka import KafkaProducer;
import json;

TOPIC = "IMAGE_OCR_PROCESSOR_TOPIC"

def image_ocr_processor_producer(image_path: str): 
    producer = KafkaProducer(bootstrap_servers="localhost:9072");
    producer.send(TOPIC, json.dumps({"image_path": image_path}));