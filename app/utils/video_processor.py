import cv2

class VideoProcessor:
    def __init__(self, video_path=None):
        self.cap = cv2.VideoCapture(video_path) if video_path else None
    
    def get_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            return frame if ret else None
        return None
    
    def release(self):
        if self.cap:
            self.cap.release()