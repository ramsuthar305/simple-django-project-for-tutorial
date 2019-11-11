from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
from .models import REGISTRATIONS
import datetime
import os

def register(request):
    context={}
    students=[]
    company=[]
    if request.method=='POST':
        data = request.POST
        r = REGISTRATIONS(name = data['name'], email = data['email'], password=data['password'], roll_no = data['roll_no'],user_type=data['user_type'],cgpa=data['cgpa'],company_cgpa=data['r_cgpa'])
        r.save()
        context={'display':"Registered Successfully!"}
        
        if data['user_type']=='student':
            return redirect('/student_result/'+data['name'])
        else:
            return redirect('/company/')
    return render(request,'register.html',context)

def company(request,nam):
    if nam:
        stds=REGISTRATIONS.objects.filter(user_type='student')
        cmpn=REGISTRATIONS.objects.filter(id=nam)
        company=[]
        students=[]
        for i in cmpn:
            for j in stds:
                print('\n\n\n',i.name)
                print('i.cgpa: {}, j.copany_cgpa:{}'.format(i.cgpa,j.company_cgpa))
                if float(j.cgpa)>=float(i.company_cgpa):
                    students.append(j)
        return render(request,'company.html',{'students':students,'name':request.session['username']})
    else:
        return redirect('/login/')


def error_404(request,exception):
        return redirect('/login/')

def allcompanies(request):
    if request.session['username']:
        companies=REGISTRATIONS.objects.filter(user_type='company')
        return render(request,'allcompanies.html',{'companies':companies})
    else:
        return redirect('/login/')

def allstudents(request):
    if request.session['username']:
        students=REGISTRATIONS.objects.filter(user_type='student')
        return render(request,'allstudents.html',{'students':students})
    else:
        return redirect('/login/')

def login(request):
    print('\nhii'*10)
    if request.method=='POST':
        print("\n\n\n\n\n\n\nin login")
        data=request.POST
        em_id = data['email']
        ps = data['password']
        print('\n\n\n\n\n\n\n\ndekh:',ps)
        var = REGISTRATIONS.objects.filter(email=em_id)
        print('\n\n\n\n\n\nvar:',var)
        id=len(var)
        if id!=0:
            for i in var:
                if i.password==ps:
                    request.session['username']=i.name
                    request.session['userId']=i.id
                    if i.user_type=='student':
                        return redirect('/student_result/'+i.name)
                    else:
                        return redirect('/company/'+str(i.id))
    
    return render(request,'login.html',{})

def admin(request):
    return render(request,'admin.html',{})
def form(request):
    return render(request,'form.html',{})

def student_result(request,nam):
    if nam:
        request.session['username'] = nam
        print('usernamemeeeeeeeeeeeeeeeeeeeeeee',request.session['username'])
        cmpn=REGISTRATIONS.objects.filter(user_type='company')
        stds=REGISTRATIONS.objects.filter(name=nam)
        company=[]
        students=[]
        print('\n\n\n\nhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        for i in cmpn:
            for j in stds:
                print('\n\n\n',i.name)
                print('i.cgpa: {}, j.copany_cgpa:{}'.format(i.cgpa,j.company_cgpa))
                if float(j.cgpa)>=float(i.company_cgpa):
                    
                    company.append(i)
        return render(request,'student_result.html',{'company':company,'name':nam})
    else:
        return redirect('/login/')

def admin_students(request):
    return render(request,'students.html',{'students':REGISTRATIONS.objects.filter(user_type='student')})

def admincompanies(request):
    return render(request,'admincompanies.html',{'students':REGISTRATIONS.objects.filter(user_type='company')})

def upload(request):
    if request.session['username']:
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            student=REGISTRATIONS.objects.get(id=request.session['userId'])
            student.resume=uploaded_file.name
            student.save()
            print(student.name,student.resume)
        return render(request,'upload.html',{})
    else:
        return redirect('/login/')

def logout(request):
    request.session['username']=False
    return redirect('/login/')

def info(request):
    return render(request,'tmp.html',{})