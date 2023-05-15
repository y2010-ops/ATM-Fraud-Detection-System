import tkinter.messagebox
import os
import cv2
import pandas as pd
import smtplib

def recognize_attendence(pin):

    print("recog fun", pin)
    # Create recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    # Read data from Trainer.yml file using recognizer
    recognizer.read("./TrainingImageLabel/Trainner.yml")
    harcascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    # Create file Deatils.csv inside Details folder
    df = pd.read_csv("Details" + os.sep + "Details.csv")
    #df = pd.read_csv("Details/Details.csv", error_bad_lines=False)
    font = cv2.FONT_HERSHEY_SIMPLEX
    #col_names = ['Id', 'Name', 'Email']
    #attendance = pd.DataFrame(columns=col_names)
    #Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    #cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    _, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(int(minW), int(minH)),
                                             flags=cv2.CASCADE_SCALE_IMAGE)
    l = len(faces)
    if l != 0:
        print('l = ',l)
        for (x, y, w, h) in faces:
            #print('entered in for loop')
            cv2.rectangle(im, (x, y), (x + w, y + h), (10, 159, 255), 2)
            # pass face data to predict() and get confidence value
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])  #{Id: 1, conf: 75.9999}
            #print(recognizer.predict)

            if conf < 100:
                #print(conf)
                aa = df.loc[df['Id'] == Id]['Name'].values
                ee = df.loc[df['Id'] == Id]['Email'].values
                # ii = df['Id'] == Id
                # print("ii",ii,"\n")
                # aa = df.loc[df['Id'] == Id,'Name']
                confstr = "  {0}%".format(round(100 - conf))
                tt = str(Id) + "-" + aa
                print("tt",tt)
                print("aa",aa)
                print("ee",ee)

                # ----------- mail ----------

                # Set up your email credentials
                sender_email = 'example@gmail.com'
                sender_password = 'wxcbkxcknpxfrwmz'

                # Set up the email content
                receiver_email = f'{ee[0]}'
                subject = 'Suspicious Activity on Your ATM Account'
                body = f'Dear {aa[0]},\n\nI am writing to inform you of a potential security breach on your ATM account. Our system has detected an unauthorized attempt to access your account from an unknown location.\n\nPlease be assured that we take the security of your account very seriously and are doing everything possible to protect your information. We apologize for any inconvenience this may have caused you.\n\nIf you have any further questions or concerns, please do not hesitate to contact us at 1800-2346-1230.\n\nBest regards,\nICICI Bank'

                # Create a message object
                message = f'Subject: {subject}\n\n{body}'

                # Set up the SMTP server
                smtp_server = 'smtp.gmail.com'
                smtp_port = 465

                #print("100-conf", 100-conf)
                #print('id - ', Id, type(Id), '\n pin - ', pin, type(pin))

                if (100-conf) >= 50:
                    #print('id - ',Id,type(Id), '\n pin - ', pin, type(pin))
                    if str(Id) == str(pin):
                        print(f"Hello {aa[0]}! \nWelcome to our ATM!")
                        tkinter.messagebox.showinfo("Recognition", f"Hello, {aa[0]}! \nWelcome to our ATM!")
                    else:
                        print('pin is not valid')

                        # Create a SMTP connection and log in
                        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                            # server.starttls()
                            server.login(sender_email, sender_password)
                            print("logged in")

                            # Send the email
                            server.sendmail(sender_email, receiver_email, message)
                        tkinter.messagebox.showinfo("Recognition", "Pin is not valid")

                else:
                    print("else condition")
                    Id = '  Unknown  '
                    tt = str(Id)
                    confstr = "  {0}%".format(round(100 - conf))
                    print('Unknown user!')
                    print(confstr)
                    # Create a SMTP connection and log in
                    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                        # server.starttls()
                        server.login(sender_email, sender_password)
                        print("logged in")

                        # Send the email
                        server.sendmail(sender_email, receiver_email, message)
                    tkinter.messagebox.showinfo("Recognition", "Unknown User!")

            else:
                print('faces - ',faces)
                print('Your face is not visible!')
                tkinter.messagebox.showinfo("Recognition", "Your face is not visible!")

