from django.db.models.signals import post_save
from .models import Certificate
from dashboard.models import RegistrationInfo
from django.dispatch import receiver
from datetime import date

import string
import random

import os
# import cv2
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings

from .models import (
    StudentCurrentEducationInfo, 
    GraduationExamName,
    PostGraduationExamName,
    GraduationInfo,
    PostGraduationInfo
)


def today_date():
        
        today = date.today()

        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        print("d1 =", d1)

        # Textual month, day and year	
        d2 = today.strftime("%B %d, %Y")
        print("d2 =", d2)
        return d2

# def generate_certificate(file_path, name, certificate_id, batch_id, date):
#     # Reading an image in default mode
#         image = cv2.imread(file_path)
#         if image is None:
#               print("Image is empty!!")
#         else:
#             print("Image is not empty!!")

#         # text
#         # text = 'Sudipta Sarker'

#         # font
#         font = cv2.FONT_HERSHEY_SIMPLEX

#         # org
#         org = (276,396)

#         # fontScale
#         fontScale = 2

#         # Red color in BGR
#         color = (0, 0, 255)

#         # Line thickness of 2 px
#         thickness = 2

#         # Using cv2.putText() method
#         image = cv2.putText(image, name, org, font, fontScale,
#                         color, thickness, cv2.LINE_AA)

#         # date = "08-Mar-2023"

#         # # Using cv2.putText() method
#         image = cv2.putText(image, date, (144,572), font, 0.5,
#                         color, 1, cv2.LINE_AA)

#         certificate_id_position = (834, 192)
#         # car_id = "893KJDE93NK8"
#         # batch = "1st"
#         batch_position = (805, 218)

#         image = cv2.putText(image, certificate_id, certificate_id_position, font, 0.5,
#                         color, 1, cv2.LINE_AA)

#         image = cv2.putText(image, batch_id, batch_position, font, 0.5,
#                         color, 1, cv2.LINE_AA)


#         # write the file
#         cv2.imwrite(file_path, image)

        # return file


def generate_certificate_id(size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


@receiver(post_save,sender=Certificate)
def create_certificate(sender,instance,created,**kwargs):
    if created:
        name = instance.student.fullname
        certificate_id = generate_certificate_id()
        instance.certificate_id = certificate_id
        certificate_id = instance.certificate_id
        batch_id = instance.batch_id
        date = today_date()

        file_path = instance.certificate.path
        print(file_path)
        # generate_certificate(file_path, name, certificate_id, batch_id, date)
        instance.save()
        # self.certificate = file        



@receiver(post_save,sender=StudentCurrentEducationInfo)
def create_student_university_profile(sender,instance,created,**kwargs):
    if created:
        if instance.university_level == "graduation":
            try:
                exam_name = GraduationExamName.objects.filter(id=instance.exam_name)[0]
                print(exam_name)
                GraduationInfo.objects.create(
                                account=instance.account,
                                exam=exam_name,
                                subject=instance.subject,
                                university=instance.university,
                                which_year_student=instance.which_year_student,
                            )
            except GraduationExamName.DoesNotExist:
                print("Ups... Something is wrong")
            
        if instance.university_level == "post_graduation":
            try:
                exam_name = PostGraduationExamName.objects.filter(id=instance.exam_name)[0]
                print(exam_name)
                PostGraduationInfo.objects.create(
                                account=instance.account,
                                exam=exam_name,
                                subject=instance.subject,
                                university=instance.university,
                                which_year_student=instance.which_year_student,
                            )
            except PostGraduationExamName.DoesNotExist:
                print("Ups... Something is wrong")
