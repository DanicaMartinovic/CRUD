from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student
from django.contrib import messages

def index(request):
    return render(request,"vezba/index.html")

def view(request):
    return render(request, "vezba/view.html",{
        'students':Student.objects.all().order_by('student_number').values()
})
    

def add(request):
    return render(request, 'vezba/add.html')

def add_rec(request):
    k = request.POST.get('student_number')
    x = request.POST.get('first_name')
    y = request.POST.get('last_name')
    z = request.POST.get('email')
    i = request.POST.get('field_of_study')
    
    
    if not Student.objects.filter(student_number=k).exists():
        student = Student(student_number=k,first_name=x, last_name=y, email=z, field_of_study=i)
        student.save()
        return redirect("/")
    else:
        messages.error(request,"Student number exists")
        return redirect("add/")
    

def delete(request, student_number):
    student = Student.objects.get(student_number = student_number)
    student.delete()
    return redirect("/")
  
  
def update(request, student_number) :
    student = Student.objects.get(student_number=student_number) 
    return render(request, 'vezba/update.html', {'student':student})

def uprec(request, student_number):
    x = request.POST['first_name']
    y = request.POST['last_name']
    z = request.POST['email']
    i = request.POST['field_of_study']
    student = Student.objects.get(student_number=student_number)
    student.first_name=x
    student.last_name = y
    student.email = z
    student.field_of_study = i
    student.save()
    return redirect('/')