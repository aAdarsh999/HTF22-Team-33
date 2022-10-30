from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import student
from django.core.files.storage import FileSystemStorage
import PyPDF2
from app1 import points
import os
import glob

from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    
    if request.method == 'POST':
        if(len((request.POST))) == 4:
            rollno = request.POST.get("rollno")
            username = request.POST.get("name")
            password = request.POST.get("password")
            print(username,password)
            # stud = User.objects.filter(id = rollno)        
            user = authenticate(username = username,password = password)
            # user = authenticate(id = rollno,password = password)

            print("user: ",user,rollno)
            if user is not None:
                auth_login(request,user)
                return redirect("dashboard")
            else:
                messages.info(request,"User credentails incorrect!")
                return redirect("login")
        else:
            username = request.POST["name"]
            rollno = request.POST["rollno"]
            password = request.POST["password"]
            password2 = request.POST["password2"]

            if password == password2:
                if User.objects.filter(username = username).exists():
                    messages.info(request,"This username is already taken!")
                    return redirect("login")

                elif User.objects.filter(id = rollno).exists():
                    messages.info(request,"This rollno is already taken!")
                    return redirect("login")
                else:
                    user = User.objects.create_user(username = username,first_name = rollno,password = password)
                    user.save()
                    return redirect("dashboard")
            else:
                messages.info(request,"The passwords entered are not same!")
                return redirect("login")    
        

    return render(request,'login_signup.html')

@login_required
def dashboard(request):
    # Activity points calculation
    user = request.user
    ips = student.objects.filter(u_id = user.first_name)
    # print(ips)
    pts = 0
    for i in ips:
        pts += i.points
    # print(pts)
    
    return render(request,'dashboard.html',{'points':pts,'ips':ips})

@login_required
def upload(request):
    return render(request,'upload.html')

name = ''
@login_required
def save(request):
    if request.method == 'POST':
        global name
        name=''
        docu = request.FILES['document']
        fs = FileSystemStorage()
        file = fs.save(docu.name, docu)
        fileurl = fs.url(file)
        # print(docu.name)
        name = docu.name
        title = docu.name
        print(title)
        
        # a=PyPDF2.PdfFileReader('media/'+docu.name)
        # print(a)
        # text = a.getPage(0).extractText()
        # print(text)
        user = request.user
        item = student()
        item.u_id = user.first_name
        item.name = user.username
        item.file = request.FILES['document']
        item.points = points.find_points(name)
        # item.points = 0       
        item.save()
    
        # folder = 'D:/activity_point_tracker/media'
        # for filename in os.listdir(folder):
        #     file_path = os.path.join(folder, filename)
        #     try:
        #         if os.path.isfile(file_path) or os.path.islink(file_path):
        #             os.unlink(file_path)
        #         elif os.path.isdir(file_path):
        #             shutil.rmtree(file_path)
        #     except Exception as e:
        #         print('Failed to delete %s. Reason: %s' % (file_path, e))
        
        
        
        
        # print(user)
        # if student.objects.filter(id = first_name) is None:
        # ins = student(id = user.first_name,name = user.username,file = docu,points = 0)
        # ins.save()
        # else:
        # points = 
        # ins = student.objects.filter(id = )
        # ins.points += points
        # ins.save()

    return redirect('dashboard')
    
@login_required
def logout_user(request):
    logout(request)
    return redirect("login")


