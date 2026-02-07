import cv2, os, numpy as np
from embeddings import get_face, get_embedding


name = input("Enter Name: ")

cap = cv2.VideoCapture(0)
embs = []
# we are taking 30 face samples 
while len(embs)< 30:
    ret, frame = cap.read()
    face = get_face(frame)

    if face is not None:
        emb = get_embedding(face)
        if emb is not None:
            # saving the embeddings in a list 
            embs.append(emb)
            cv2.putText(frame,f"Samples: {len(embs)}/30",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Register", frame)
    if cv2.waitKey(1)==27:
        break

# saving the mean of embeddings
final_emb = np.mean(embs, axis=0)
np.save("faces/"+name+".npy", final_emb)

cap.release()
cv2.destroyAllWindows()
print("Registered successfully!")
