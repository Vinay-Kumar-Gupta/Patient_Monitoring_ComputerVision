import pandas as pd
import pyttsx3

voice = pyttsx3.init()
voice.setProperty("rate", 120)
voices = voice.getProperty("voices")
voice.setProperty("voice", voices[-1].id)
csv_file = 'D:\BE.MECHATRONICS\SIH\Patient_record.csv'  
df = pd.read_csv(csv_file)


def patient_record_fetch(input_id):
    result = df[df["P-ID"]==input_id]

    health_issue = result.iloc[0]["HEALTH-ISSUE"]
    prcp = result.iloc[0]["PRESCRIPTION"]
    timming = result.iloc[0]["TIMMING"]
    dose = result.iloc[0]["DOSE"]


    if not result.empty:
        print(f"Patient ID : {input_id} is having {health_issue}, prescription : {prcp}\
            , Dose : {dose} in {timming} ")
        voice.say(f"Patient ID : {' '.join(str(input_id))} is having {health_issue}, prescription : {prcp}\
            , Dose : {dose} in {timming} ")
        voice.runAndWait()
        voice.stop()
        print()

    else:
        print(f"No person found with ID {input_id}")

