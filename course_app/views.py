from django.shortcuts import render
import datetime
from course_app.models import Student

# Create your views here.
def home(request):
    student = Student.objects.all()[0]
    # print('***************')
    # print(student)
    # print(student.first_name, student.last_name)
    # current_date = datetime.datetime.now()
    return render(request, 'course_app/home.html', {'student':student})