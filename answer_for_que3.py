'''
Answer for Que.3:
Yes, Django signals run in the same database transaction as the caller.
For this answer i have used help of google and chatgpt as was not sure about this concept.
'''


# models.py ----------------------------------------------------------------------------------------------------
class Student(models.Model):
    name = models.CharField(max_length=30)
    usn = models.CharField(max_length=30)

class Logs(models.Model):
    msg = models.CharField(max_length=30)




# signals.py ----------------------------------------------------------------------------------------------------
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from app import models



@receiver(signals.post_save, sender=models.Student)
def model_post_save_action(sender, instance, created, **kwargs):
    models.Logs.objects.create(msg='Instance create for student with name: %s' % instance.name)




# views.py ----------------------------------------------------------------------------------------------------
from django.http import HttpResponse
from django.utils import timezone
from app import models, forms
from django.db import transaction



@login_required
def addStudent(request):
    if request.method == 'POST':
        usn = request.POST['usn']
        name = request.POST['name']
        
        student_obj = None
        try:
            with transaction.atomic():
                student_obj = models.Person.objects.create(name=name)            
                raise Exception("Forcing rollback")
        except:
            print("Exception")
        
        if student_obj:
            return HttpResponse('<h1> Student created successfully. </h1>')
        else:
            return HttpResponse('<h1> Student creation failed. </h1>')





