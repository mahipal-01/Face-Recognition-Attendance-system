import cv2
import numpy as np
import mediapipe as mp
from deepface import DeepFace
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision.face_detector import FaceDetectorOptions

# Load MediaPipe face detector
base_options = mp.tasks.BaseOptions(model_asset_path="blaze_face_short_range.tflite")
options = FaceDetectorOptions(base_options=base_options)
detector = vision.FaceDetector.create_from_options(options)

def get_face(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    detection_result = detector.detect(mp_image)

    if not detection_result.detections:
        return None

    bbox = detection_result.detections[0].bounding_box
    h, w, _ = frame.shape

    x = int(bbox.origin_x)
    y = int(bbox.origin_y)
    bw = int(bbox.width)
    bh = int(bbox.height)

    face = frame[y:y+bh, x:x+bw]
    if face.size == 0:
        return None

    return face

def get_embedding(face):
    try:
        rep = DeepFace.represent(
            face,
            model_name="Facenet512",
            enforce_detection=False
        )
        return np.array(rep[0]["embedding"])
    except:
        return None
