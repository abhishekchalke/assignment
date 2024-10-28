'''
Answer for Que.2:
Yes, Django signals run in the same thread as the caller, which means the signal handler and the function that trigerred are executed on the same thread.
The synchronous behaviour of signals also justify that the signals and the caller run on the same thread, since the caller function has to wait
till the signal execution is completed, so this also proves that the signals and caller run on the same thread.
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
import time, threading



@receiver(signals.post_save, sender=models.Student)
def model_post_save_action(sender, instance, created, **kwargs):
    print("signal received for model creation. Thread id:%s" % threading.current_thread().ident)
    print("performing task after instance creation. Thread id:%s" % threading.current_thread().ident)
    time.sleep(60)
    print("task completed. Thread id:%s" % threading.current_thread().ident)





# views.py ----------------------------------------------------------------------------------------------------
from django.http import HttpResponse
from django.utils import timezone
from app import models, forms


def addStudent(request):
    if request.method == 'POST':
        usn = request.POST['usn']
        name = request.POST['name']

        print("started student model creation. Thread id:%s" % threading.current_thread().ident)
        student_obj, created = models.Student.objects.create(usn=usn, name=name)
        print("finished student model creation. Thread id:%s" % threading.current_thread().ident)

        return HttpResponse('<h1> Student created successfully. </h1>')

    



