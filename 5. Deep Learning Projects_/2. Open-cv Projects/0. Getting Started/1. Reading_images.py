import cv2

################## reading an image from directory.


#image is stored in the format of a 3-D array.
image = cv2.imread('images/google.png')

#resizing image size to half the original size.
resized_image=cv2.resize(image, (int(image.shape[1]/2),int(image.shape[0]/2)))

# showing the image with title labeled window.
cv2.imshow('Window Title', resized_image)

# waiting time after a key is clicked for exit.
cv2.waitKey(0)

# destroy/close all instances of windows open.
cv2.destroyAllWindows()


