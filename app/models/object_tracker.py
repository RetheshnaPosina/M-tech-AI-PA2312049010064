from ultralytics import YOLO
import cv2

class ObjectTracker:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')
        self.tracking_config = {
            'tracker': 'bytetrack.yaml',
            'persist': True
        }
    
    def process_frame(self, frame):
        results = self.model.track(frame, **self.tracking_config)
        return results[0].plot()