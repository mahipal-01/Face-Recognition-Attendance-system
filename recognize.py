import cv2, os, numpy as np
from embeddings import get_face, get_embedding
from attendance import mark
from sklearn.metrics.pairwise import cosine_similarity
from liveness import is_live, draw_challenge

# load faces data
db = {f.replace(".npy",""):np.load("faces/"+f) for f in os.listdir("faces")}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face=get_face(frame)
    draw_challenge(frame)

    if face is not None:
        emb=get_embedding(face)
        if emb is not None:
            for name, ref in db.items():
                sim=cosine_similarity([emb],[ref])[0][0]
                # if similarity found + liveness check passed
                if sim > 0.6 and is_live(frame):
                    # mark attendance
                    action = mark(name)
                    print(name, action)

                    cv2.putText(frame, action,(50,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                    cv2.imshow("Attendance", frame)
                    cv2.waitKey(1500)   
                    # exit
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1)==27:
        break


