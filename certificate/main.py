# Python program to explain cv2.putText() method
	
# importing cv2
import cv2
	
# path
path = r'E:\Freelancing\Projects\Backend\Dikkha-Career-Proj\certificate\certificate-template.jpg'
	
# Reading an image in default mode
image = cv2.imread(path)
	
# Window name in which image is displayed
window_name = 'Image'

# text
text = 'Sudipta Sarker'

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (276,396)

# fontScale
fontScale = 2

# Red color in BGR
color = (0, 0, 255)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(image, text, org, font, fontScale,
				color, thickness, cv2.LINE_AA)

date = "08-Mar-2023"

# # Using cv2.putText() method
image = cv2.putText(image, date, (144,572), font, 0.5,
				color, 1, cv2.LINE_AA)

student_id_position = (834, 192)
student_id = "893KJDE93NK8"
batch = "1st"
batch_position = (805, 218)

image = cv2.putText(image, student_id, student_id_position, font, 0.5,
				color, 1, cv2.LINE_AA)

image = cv2.putText(image, batch, batch_position, font, 0.5,
				color, 1, cv2.LINE_AA)




# Displaying the image
cv2.imshow(window_name, image)
file = cv2.imwrite("generated-certificates.jpg", image)
print(file)
