from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail

# Create your views here.
from .models import Department, Employee


def home(request):

    if request.method == "POST":
        name = request.POST['name']
        size = request.POST['size']
        hod = request.POST['hod']

        depart = Department(name=name, size=size, department_head=hod)
        depart.save()
        return redirect('departments')

    else:
        return render(request, 'home.html')


def departments(request):

    departments = Department.objects.all()

    return render(request, 'department.html', {"departs": departments})


def removedepartment(request, id):

    depart = Department.objects.get(pk=id)

    depart.delete()

    return redirect("departments")




def employee(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        email = request.POST['email']
        salary = float(request.POST['salary'])
        depart = request.POST['depart']

        depart = get_object_or_404(Department, name=depart)

        dep = Department.objects.filter(name__exact=depart)

        tax = ''
        balance =''

        if salary >= 10000:
            tax = 0.2
            balance = salary - (salary*0.2)
        elif salary >= 5000:
            tax = 0.15
            balance = salary - (salary * 0.15)
        else:
            tax = 0.1
            balance = salary - (salary * 0.1)

        employee = Employee(firstName=fname, lastName=lname, age=age, email=email, salary=salary,
                             tax=tax, balance=balance, departId=depart)
        employee.save()
        # dep.size += 1

        #
        # subject = f'Welcome To SoftCode Company {fname}'
        # message = f'Your Staff Id is C2024{employee.id} and your salary is ${salary}'
        # recipient_list = [email]  # Replace with recipient email(s)
        #
        # send_mail(
        #     subject,
        #     message,
        #     'rilelaboye@gmail.com',  # From email (matches EMAIL_HOST_USER)
        #     recipient_list,
        #     fail_silently=False,  # Raise error if sending fails
        # )


        return redirect("employeedetails")

    else:
        departments = Department.objects.all()

        return render(request, 'employeeform.html', {"departs": departments})


def employeedetails(request):

    employees = Employee.objects.all()
    return render(request, 'employeedata.html', {"employees": employees})


def searchemployee(request):

    departments = Department.objects.all()

    if request.method == "POST":
        depart = request.POST['depart']

        depart = get_object_or_404(Department, name=depart)

        employees = Employee.objects.filter(departId__exact=depart)

        return render(request, 'search.html', {"employees": employees, "departs": departments})

    else:

        departments = Department.objects.all()

        return render(request, 'search.html', {"departs": departments})


def removeemployee(request, id):

    employee = Employee.objects.get(pk=id)

    employee.delete()

    return redirect("employeedetails")












