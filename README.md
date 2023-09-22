# Face Recognition and Patient Record Fetching System

This Python script combines face recognition with patient record retrieval from a CSV file. It utilizes the OpenCV, numpy, face_recognition, pandas, and pyttsx3 libraries to accomplish this task.

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [Setup](#setup)
- [Features](#features)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview
This script captures real-time video input from a webcam, detects faces using the face_recognition library, and matches recognized faces with patient records from a CSV file. When a match is found, it retrieves and speaks the patient's health information using text-to-speech (TTS).

## Usage
1. **Prerequisites:** Ensure you have the required Python libraries installed using `pip install opencv-python numpy face_recognition pandas pyttsx3`.

2. **Data Preparation:**
   - Create a CSV file (e.g., `Patient_record.csv`) containing patient records with columns such as "P-ID," "HEALTH-ISSUE," "PRESCRIPTION," "TIMMING," and "DOSE."
   - Organize patient images in a directory (e.g., `Patients_Image`) with filenames corresponding to patient IDs (e.g., `110.jpg`, `111.jpg`).

3. **Configuration:**
   - Modify the `csv_file` variable to specify the path to your CSV file:

     ```python
     csv_file = 'D:\BE.MECHATRONICS\SIH\Patient_record.csv'  # Replace with your CSV file path
     ```

4. **Run the Script:**
   - Execute the script using `python your_script_name.py`.

5. **Recognition and Retrieval:**
   - The system captures video from your webcam and performs real-time face recognition.
   - When a recognized face matches a patient, it speaks out the patient's information.

## Setup
- Ensure your CSV file follows the specified format.
- Resize patient images to improve recognition accuracy.
- Patient image filenames should correspond to patient IDs.

## Features
- Real-time face recognition from a webcam feed.
- Text-to-speech (TTS) for speaking patient information.
- Easily customizable for different CSV file formats and use cases.


## Contributing
Contributions to this project are welcome. If you want to improve the code or fix any issues, please open a pull request.

## Contact
For questions or feedback, feel free to contact [Vinay Kumar Gupta] at [vinaygupta2781998@gmail.com].

---

This README provides an overview of the Face Recognition and Patient Record Fetching System. For more details, refer to the code and comments in the Python script.

## OUTPUT 

Demo Video Link : [https://www.loom.com/share/0293b36bc8284cb2aaf4c77ffa10d431?sid=1508c5a8-c520-4a4f-b2c8-d0e410f43c68]

```
PS D:\BE.MECHATRONICS\SIH> python -u "d:\BE.MECHATRONICS\SIH\Patients_Health_Monitering.py"
Patient ID : 110 is having Headache, prescription : Iburophen, Dose : 1 in Morning 
PS D:\BE.MECHATRONICS\SIH> 

```
<img width="477" alt="image" src="https://github.com/Vinay-Kumar-Gupta/SIH/assets/108336700/1b82c976-27f6-4b25-873b-c2413b08af5c">

