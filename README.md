# FaceRecognitionProject
## Introduction:                               
Overview of the System  The purpose of this system is to build an attendance system which is based on face recognition techniques. Here face of an individual will be considered for marking attendance. During each session, Faces will be detected from live streaming video or webcam. The faces detected will be compared with Images present in the dataset/folder. If match is found, attendance will be marked for the respective student. At the end of each session, list of present students will be marked and their name will be  Inserted in the excel sheet on real-time basis.  Traditional method of attendance marking  a tedious task in many schools and colleges. It is also an Extra burden to the faculties who shown attendance by manual while calling the names of students Which might take about 5 minutes of entire session, face recognition is as  important as biometric.                                                                                                                                      
## Background: 
Existing System  Conventional methods are still being followed to mark attendance in many schools and colleges which is a more time-consuming task. The most common conventional methods being practiced in routine lifestyle are, the student is supposed to sign the attendance sheet manually, which is passed around the classroom while the lecturer is giving the lecture, sometimes this particular approach could undoubtedly allow the students to cheat about their attendance, where a student present in the class may sign for a physically absent student. Uncommonly, this attendance sheet could easily be either misplaced or lost with/without the lecturers knowledge. Another stricter conventional method which is more commonly used in practice is the roll call system, where the student is supposed to answer to his/her roll call made by the  lecturer, sometimes this method also allows the student to cheat about their attendance by answering the roll call as present for a student who is not available in the class which is again a big task.                                                                          
## Motivation: 
Manual Student Attendance Management system is a process where a teacher concerned with the particular subject need to call the students name and mark the attendance manually. Manual attendance may be considered as a time-consuming process or sometimes it happens for the teacher to miss someone or students may answer multiple times on the absence of their friends. So, the problem arises when we think about the traditional process of taking attendance in the classroom. To solve all these issue so we go with Face Recognition Smart Attendance System(FRAS).

## Objective and Scope of the Project
•  Thus the attendance of the students presensie the class is marked by using face Recognition technology which is implied with the machine learning algorithms. The Automated Attendance System helps in increasing the accuracy and speed ultimately to Achieve the high-precision real-time attendance and its evaluation process.

•  This system aims to build an effective class attendance system using face recognition Techniques. The proposed system will be able to mark the attendance via face recognition, it will Detect faces via webcam and then recognize the faces which is there in the dataset: After recognition, it will mark the Attendance of the recognized a student and update the attendance record.

# Step to install 
## •  First Install [Python 3.6][1] & [PyCharm][2] on your System. 
[1]:https://www.python.org/downloads/release/python-360/ "Python 3.6" 
[2]:https://www.jetbrains.com/pycharm/ "PyCharm"
## •  Then Create a Python Project `"FaceRecognitionProject"`
## •  Then copy all the file and folders to your project 
## •  Open your project then go to `"File > Settings (ctrl+alt+s) > Project > Python Intrepreter"` install the following packages:
###   1.  numpy
###   2.  cmake
###   3.  dlib (Specified ver. 19.18.0)
###   4.  face-recognition
###   1.  face-recognition-models
###   2.  Kivy
###   3.  Kivy-Garden
###   4.  kivymd
###   1.  opencv-python
###   2.  pandas
###   3.  playsound (Specified ver. 1.2.2)
###   4.  gTTS
###   1.  face-recognition-util
## •  After the packages installed run your project make sure it works correctly.
## •  Open the terminal Change to project directory using cd, then install pyinstaller using command `pip install pyinstaller` then after the installation write command `pyinstaller main_kivy.spec -y` thats it will make a dist folder in your project directory go to `"dist > main_kivy > open 'main_kivy.exe'"`

