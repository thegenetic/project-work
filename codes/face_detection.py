import cv2
from tkinter import filedialog
from tkinter import *


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# created an instance of tkinter 
root = Tk()
# deleting the default window provided by tkinter
root.withdraw()
filepath = filedialog.askopenfilename(title="select image")
# Read the input image
img = cv2.imread(filepath)

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# uniquely name each detected faces using count variable
count = 0

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    face = img[y:y+h, x:x+w] #slice the face from the image
    cv2.imwrite(str(count)+'.jpg', face) #save the image
    count+=1
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)

# Display the output
cv2.imshow('image', img)
cv2.waitKey()