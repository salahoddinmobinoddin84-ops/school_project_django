from django.shortcuts import render
from .models import Student, Course

def admission_view(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        course_id = request.POST.get('course')
        address = request.POST.get('address')
        marksheet = request.FILES.get('marksheet')

        course_obj = Course.objects.get(id=course_id)

        Student.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            dob=dob,
            course=course_obj,
            address=address,
            marksheet=marksheet
        )
        return render(request, 'success.html')
    
    return render(request, 'admission_form.html', {'courses': courses})

def status_views(request):
    students = None
    if request.method == 'POST':
        email = request.POST.get('email')
        students = Student.objects.filter(email=email)
    return render(request, 'status.html', {'students': students})