import random, time, cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision.face_landmarker import FaceLandmarkerOptions

base = mp.tasks.BaseOptions(model_asset_path="face_landmarker.task")

options = FaceLandmarkerOptions(
    base_options=base,
    num_faces=1,
    output_face_blendshapes=False,
    output_facial_transformation_matrixes=False
)

landmarker = vision.FaceLandmarker.create_from_options(options)

challenge = None
start_time = None

def new_challenge():
    global challenge, start_time
    challenge = random.choice(["BLINK","LEFT","RIGHT","MOUTH"])
    start_time = time.time()

def is_live(frame):
    global challenge, start_time

    if challenge is None:
        new_challenge()
        return False

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    res = landmarker.detect(mp_image)

    if not res.face_landmarks:
        return False

    lm = res.face_landmarks[0]

    # Fail if time expired
    if time.time() - start_time > 3:
        new_challenge()
        return False

    # Eye blink
    eye = abs(lm[159].y - lm[145].y)
    blink = eye < 0.004

    # Nose horizontal
    nose = lm[1].x

    # Mouth open
    mouth = abs(lm[13].y - lm[14].y) > 0.05

    if challenge == "BLINK" and blink:
        challenge = None
        return True

    if challenge == "LEFT" and nose < 0.45:
        challenge = None
        return True

    if challenge == "RIGHT" and nose > 0.55:
        challenge = None
        return True

    if challenge == "MOUTH" and mouth:
        challenge = None
        return True

    return False

def draw_challenge(frame):
    if challenge:
        cv2.putText(frame,f"Do: {challenge}",
                    (40,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
