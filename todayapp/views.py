from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView
from .forms import UpdateForm


# Create your views here.
from .models import Employee
def employees_list(request):
    employees=Employee.objects.all()
    context={
        'employees':employees,
        }
    return render(request, 'list.html',context)


def create(request):
        if request.method=="POST":
            emp_name=request.POST['emp_name']
            emp_email=request.POST['emp_email']
            emp_contact=request.POST['emp_contact']
            emp_role=request.POST['emp_role']
            emp_salary=request.POST['emp_salary']
            emp_id=request.POST['emp_id']
            
            Employee.objects.create(emp_name=emp_name,emp_email=emp_email,emp_contact=emp_contact,emp_role=emp_role,emp_salary=emp_salary)
            return render(request,'create.html')

        emp=Employee.objects.all()
        context={}
        context['emp'] = emp
        return render(request,'create.html',context)


# def edit(request,emp_id):
#     if request.method=="POST":
#             emp_name=request.POST['emp_name']
#             emp_email=request.POST['emp_email']
#             emp_contact=request.POST['emp_contact']
#             emp_role=request.POST['emp_role']
#             emp_salary=request.POST['emp_salary']
#             emp_id=request.POST['emp_id']  
#             emp=Employee(emp_name=emp_name,emp_email=emp_email,emp_contact=emp_contact,emp_role=emp_role,emp_salary=emp_salary)
#             emp.save()
#             return redirect('/')
    
#     return render(request,'edit.html')

  
def edit(request, emp_id):
        emp = Employee.objects.get(emp_id=emp_id)    
        emp.save()
        ctx={
            'emp':emp,
            }
        return render(request, 'edit.html', ctx)


def update(request,emp_id):
    data = Employee.objects.get(emp_id=emp_id)
    form = UpdateForm(request.POST, instance=data)
    if form.is_valid():
        form.save()
        data = Employee.objects.all()
        return redirect('employees-list')
    # ctx={
    #     'form':form
    # }
    # return render(request, 'edit.html',ctx)

def delete(request,emp_id):
    member=Employee.objects.get(emp_id=emp_id)
    member.delete()
    return redirect('/')
    return render(request,'list.html')



