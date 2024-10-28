'''
Answer for Que.1:
By default django signals are executed synchronously, which means when the signal function is called,
once the model is created. After completion of the signal funcion, the further code is executed.
'''



# models.py ----------------------------------------------------------------------------------------------------
class Student(models.Model):
    name = models.CharField(max_length=30)
    usn = models.CharField(max_length=30)

    class Meta:
        db_table = 'student'




# signals.py ----------------------------------------------------------------------------------------------------
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from app import models
import time


@receiver(signals.post_save, sender=models.Student)
def model_post_save_action(sender, instance, created, **kwargs):
    print("signal received for model creation. Time:%s" % timezone.now())
    print("performing task after instance creation. Time:%s" % timezone.now())
    time.sleep(60)
    print("task completed. Time:%s" % timezone.now())





# views.py ----------------------------------------------------------------------------------------------------
from django.http import HttpResponse
from django.utils import timezone
from app import models, forms


def addStudent(request):
    if request.method == 'POST':
        usn = request.POST['usn']
        name = request.POST['name']

        print("started student model creation. Time:%s" % timezone.now())
        student_obj, created = models.Student.objects.create(usn=usn, name=name)
        print("finished student model creation. Time:%s" % timezone.now())

        return HttpResponse('<h1> Student created successfully. </h1>')

    



