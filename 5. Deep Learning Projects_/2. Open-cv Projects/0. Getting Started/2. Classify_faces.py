import cv2

################## Face detection from an image.

#Step1: Create a cascade classifier. This classifier is predesigned to collect facial features into a series.
#Step2: Open-cv will feature file and convert it to a numpy array.
#Step3: Open-cv will determine the rows and columns in which the face is composed from the matrix.
#Step4: Draw a rectangle around those rows and columns. After converting to gray-scale image.

# Create a cascade classifier object
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# reading image as it is.
image=cv2.imread('/home/akshatra/Desktop/Updated MyGitHub/DataScience-Starter-Pack/5. Deep Learning Projects./2. Open-cv Projects/0. Getting Started/images/photo')

# Reading image as gray scale image.
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Search for co-ordinates of the image.
# detectMultiScale helps to search for the rectangle co-ordinates.
# ScaleFactor is like the learning rate and determines the rate at which the image is read.
# minNeighbors determine the neighbors to consider at a time.
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    image=cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow('Gray', image)

cv2.waitKey(0)

#printing the faces.
print(faces)
