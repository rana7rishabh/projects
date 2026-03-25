import face_recognition
import numpy as np
import cv2
from datetime import datetime
import csv
import os

video_capture=cv2.VideoCapture(0)

# Load known faces
# face1=face_recognition.load_image_file("students_face/face1.jpg")
# face1_encoding=face_recognition.face_encodings(face1)[0]
# face2=face_recognition.load_image_file("students_face/face2.jpg")
# face2_encoding=face_recognition.face_encodings(face2)[0]

path='students_face'
known_faces_encodings=[]
known_faces_names=[]

my_list= os.listdir(path)

for curr in my_list:
    cur_img=face_recognition.load_image_file(f"{path}/{curr}")
    encodings=face_recognition.face_encodings(cur_img)
    
    if len(encodings)>0:
        known_faces_encodings.append(encodings[0])
        # use filename as the name
        known_faces_names.append(os.path.splitext(curr)[0])
    else:
        print(f"No Face found in {curr}")

# print(f"Loaded {len(known_faces_names)} students: {known_faces_names}")

# list of expected students
students=known_faces_names.copy()

# Get current date and time
now=datetime.now()
current_date=now.strftime("%Y-%m-%d")

# write in csv

f=open(f"{current_date}.csv", 'a', newline="")
lnwriter=csv.writer(f)

while True:
    _,frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_frame=cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
    
    # recognize faces
    
    face_location=face_recognition.face_locations(rgb_frame)
    face_encodings=face_recognition.face_encodings(rgb_frame,face_location)
    
    for face_encoding in face_encodings:
        matches=face_recognition.compare_faces(known_faces_encodings, face_encoding)
        face_distace=face_recognition.face_distance(known_faces_encodings,face_encoding) #like cosine similarity
        best_match_index=np.argmin(face_distace)
        
        name=None
        
        if (matches[best_match_index]):
            name=known_faces_names[best_match_index]
            
            if name in students:
                students.remove(name)
                current_time=datetime.now().strftime("%H-%M-%S")
                lnwriter.writerow([name,current_time])
        
    
    
    cv2.imshow("Attendence", frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()
