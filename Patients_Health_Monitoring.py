# ==================================== Imports ===================================
import cv2
import numpy as np
import face_recognition
import os
import pandas as pd
import pyttsx3
import time
# ======================================== Voice Setup =====================================

voice = pyttsx3.init()
voice.setProperty("rate", 125)
voices = voice.getProperty("voices")
voice.setProperty("voice", voices[0].id)

# ========================================== Read the CSV file ========================

csv_file = 'D:\BE.MECHATRONICS\SIH\Patient_record.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# ========================================= Variable declare ==================================

flag1=1
pre_face_id=0
path='Patients_Image'
images=[]
classNames=[]
myList=os.listdir(path)

# print(myList)

for cl in myList:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
# print(classNames)


def find_encodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown=find_encodings(images)

cap=cv2.VideoCapture(0)

# ====================================== Data fetching funtion =============================

def patient_record_fetch(input_id):
    result = df[df["P-ID"]==input_id]

    health_issue = result.iloc[0]["HEALTH-ISSUE"]
    prcp = result.iloc[0]["PRESCRIPTION"]
    timming = result.iloc[0]["TIMMING"]
    dose = result.iloc[0]["DOSE"]


    if not result.empty:
        print(f"Patient ID : {input_id} is having {health_issue}, prescription : {prcp}, Dose : {dose} in {timming} ")
        voice.say(f"Patient ID : {' '.join(str(input_id))} is having {health_issue}, prescription : {prcp}\
            , Dose : {dose} in {timming} ")
        voice.runAndWait()
        voice.stop()

    else:
        print(f"No person found with ID {input_id}")
        voice.say(f"No person found with ID {' '.join(str(input_id))}")
        voice.runAndWait()
        voice.stop()

# ====================================== Main Loop =========================================

while 1:
    a,imag=cap.read()
    imag = cv2.flip(imag,1)
    imgs=cv2.resize(imag,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imag,cv2.COLOR_BGR2RGB)
    

    faceCurFrame=face_recognition.face_locations(imgs)
    encodeCurFrame=face_recognition.face_encodings(imgs,faceCurFrame)

    for encodeFace,faceLoc in zip(encodeCurFrame,faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
        
        matchIndex=np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            y1,x2,y2,x1=faceLoc
            #y1,x2,y2,x1=y1*4 , x2*4 , y2*4 , 0x1*4
            cv2.rectangle(imag,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(imag,(x1,y1-50),(x2,y1),(0,255,0),cv2.FILLED)
            cv2.putText(imag,name,(x1+2,y1-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)

# =============================== Repeation_stop and record_fetching =====================================
            Face_ID = eval(name[2:])
            if Face_ID != pre_face_id:
                flag1=1
            if flag1==1:
                flag1=0
                pre_face_id = Face_ID
                patient_record_fetch(Face_ID)


    cv2.imshow('Testing',imag)
    if cv2.waitKey(1) & 0xFF == 27:
        break    
