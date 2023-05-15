import csv
import cv2
import os
import os.path

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# Take image function

def takeImages(Id,name,email):
    #print(Id, name, email)

    if is_number(Id) and name and email:
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        # Load the cascade
        harcascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while (True):
            # Read the frame
            ret, img = cam.read()
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect the faces
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()

        res = "Images Saved for ID : " + Id + " Name : " + name
        header = ["Id", "Name", "Email"]
        row = [Id, name, email]
        if os.path.isfile("Details" + os.sep + "Details.csv"):
            with open("Details" + os.sep + "Details.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(j for j in row)
            csvFile.close()
        else:
            with open("Details" + os.sep + "Details.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(i for i in header)
                writer.writerow(j for j in row)
            csvFile.close()
    else:
        if is_number(Id):
            print("Enter Alphabetical ID")
        if name.isalpha():
            print("Enter Numeric Name")
