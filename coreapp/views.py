from django.shortcuts import render,redirect
from datetime import datetime, date

from .models import *
from .models import  acntexpensest,acntspayslip,projectextensionrqst,marketingassignwrk,Execompletedtasks,Tlshareddatas,Tltasks,Project,PrTasktoTL,PrTasktoDR,Report,Testing
from .models import Branch,college,internship,proandmarkng,service,recrutement,select,regdetails,admingivetask,managerattendance,leavereq,employeeattendance,hrreport,hrprojectsgive,mangivetasks,syllabus,viewdata,hrattendancet,drrpayment,manproductmarketing
from .forms import ImageFormHR,ImageFormManager,ImageFormadmin,SearchForm,FileForm,ViewForm,RegisterForm,RegnewForm,VForm
# from qrcode import *
from django.core.files import File
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from infoxcoreproject import settings
from urllib.parse import urlencode
# import qrcode.image.svg
from io import BytesIO
from django.views.generic import View
# from xhtml2pdf import pisa
from coreapp.utils import render_to_pdf ,get_template
from django.db.models import Q
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from coreapp.models import TeamLeadweeklytask
from .forms import TLTaskFileForm
from .forms import TLProjectFileForm
from .forms import DRTaskFileForm
from .forms import DRProjectFileForm
from .forms import DRpaymentForm,TSTaskFileForm
import time
import re
#===================================================================================================
def please(request):
    return render(request,'please.html')
def log1(request):
    return render(request, 'login.html')
def home(request):
    # import pdb; pdb.set_trace()
    if request.method =='POST':
        print(request.POST['email'])
        print(request.POST['password'])
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='Executive').exists():
            member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['usernamehr'] = member.designation
           
            request.session['usernamehr1'] = member.name
            request.session['usernamehr2'] = member.branch
            print(member.branch)
            return render(request, 'hrsec.html', {'member':member})
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='account').exists():
            member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['usernameacnt'] = member.designation
            request.session['usernameacnt1'] = member.name
            request.session['usernameacnt2'] = member.branch
            return render(request, 'acntsec.html', {'member':member})
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='admin').exists():
            member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['usernameadmin'] = member.designation
            request.session['usernameadmin1'] = member.name
            request.session['usernameadminid'] = member.id
            return render(request, 'adminsec.html', {'member':member})
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='MANAGER').exists():
            member = regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['usernameM'] = member.designation
            request.session['usernameM1'] = member.name
            request.session['usernameM2'] = member.branch
            request.session['usernameMid'] = member.id
            return render(request, 'MANsec.html', {'member': member})
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='TL').exists():
            member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['usernametl'] = member.designation
            request.session['usernametl1'] = member.name
            request.session['usernametl2'] = member.branch
            request.session['usernametl3'] = member.department
            request.session['usernametl4'] = member.id
            return render(request, 'TLsec.html', {'member':member})

        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],department='Software').exists():
            member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['usernamedr'] = member.designation
            request.session['usernamedr1'] = member.name
            request.session['usernamedr2'] = member.branch
            request.session['usernamedr3'] = member.department
            request.session['usernamedr4'] = member.trainer
            request.session['usernamedr5'] = member.id

            return render(request, 'DRsec.html', {'member':member})
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='Tester').exists():
            member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['usernamets'] = member.designation
            request.session['usernamets1'] = member.name
            request.session['usernamets2'] = member.branch
            request.session['usernamets3'] = member.department
            request.session['usernamets4'] = member.id
            return render(request, 'TSsec.html', {'member':member})
            
        # if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='Marketing TL').exists():
        #     member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
        #     request.session['usernameMtl'] = member.designation
        #     request.session['usernameMtl1'] = member.name
        #     request.session['usernameMtl2'] = member.branch
        #     request.session['usernameMtl3'] = member.department
        #     request.session['useremail'] = member.email
        #     return render(request, 'teamlead/indextlsec.html', {'member':member}) 
        # if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='Data Collector').exists():
        #     member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
        #     request.session['usernamedatal'] = member.designation
        #     request.session['usernamedata1'] = member.name
        #     request.session['usernamedata2'] = member.branch
        #     request.session['usernamedata3'] = member.department
        #     request.session['useremail'] = member.email
        #     return render(request, 'datacol/indexdcsec.html', {'member':member})  
        # if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='Marketing Executive').exists():
        #     member=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
        #     request.session['usernameMexel'] = member.designation
        #     request.session['usernameMexe1'] = member.name
        #     request.session['usernameMexe2'] = member.branch
        #     request.session['usernameMexe3'] = member.department
        #     request.session['useremail'] = member.email
        #     return render(request, 'executive/indexexesec.html', {'member':member})             
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='marketing TL').exists():
            print('yay')
            user=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['marketing_userid'] = user.id
            return redirect('TL_dash')
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='data collector').exists():
            user=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['marketing_userid'] = user.id
            return redirect('collect_dash')  
        if regdetails.objects.filter(email=request.POST['email'], password=request.POST['password'],designation='marketing executive').exists():
            user=regdetails.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['marketing_userid'] = user.id
            return redirect('marketing_dash') 
        
        else:
            context={'msg':'Invalid uname or password'}
            return render(request,'login.html',context)
def MANmanagerprofile(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1).filter(branch=usernameM2)
    return render(request, 'MANmanagerprofile.html', {'mem': mem})


def MANmanagerprofile1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmanagerprofile1.html', {'mem': mem})




def MANtask(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANtask.html',context)
def MANmydupdate(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    if request.method == "POST":
        team = admingivetask.objects.get(id=request.POST.get('team_id'))
        mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
        team.submited='submitted'
        form = ImageFormManager(data=request.POST, files=request.FILES, instance=team)
        form.save()
        return render(request, "MANMytaskCompleted.html", {'teams': team,'mem':mem})

def MANgivetasktoemployee(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    department1 = regdetails.objects.values('department').distinct().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    tester=regdetails.objects.values('name').distinct().filter(branch=usernameM2).filter(designation='Tester')
    context = {'departments': department1,'mem':mem,'tester':tester}
    return render(request, 'MANgivetasktoemployee.html', context)

def MANgivetask(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANgivetask.html',context)

def MANTaskGivetaskToEmployeeAssign(request):
    return render(request, 'MANTaskGivetaskToEmployeeAssign.html')

#------------------Assigned Task------------------
def MANassignedtask(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    #tas=mangivetasks.objects.filter(assignedBy='MANAGER').all()
    tas = mangivetasks.objects.all().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANassignedtask.html',{'tasks':tas,'mem':mem})
def MANassigntasklistclick(request):
    # import pdb;pdb.set_trace()
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    proj_id=request.GET.get('prid')
    givpro=mangivetasks.objects.filter(id=proj_id).values()
    for ins_pro in givpro:
        lst_screenshot = []
        if ins_pro['json_screenshot']:
            for temp in ins_pro['json_screenshot']:
                lst_screenshot.append(settings.HOSTNAME + temp)
            ins_pro['json_screenshot'] = lst_screenshot
    #import pdb;pdb.set_trace()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    if mangivetasks.objects.filter(id=proj_id,testerok='Tested ok'):
        return render(request, 'MANassignedtask1TS.html',{'pro':givpro,'mem':mem})
    if mangivetasks.objects.filter(id=proj_id,submited=''):
        return render(request, 'MANassignedtask1.html',{'pro':givpro,'mem':mem})
    else:
        return render(request, 'MANassignedtaskSubmitted.html', {'pro': givpro,'mem':mem})
    '''if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    task_id=request.GET.get('taskid')
    name=mangivetasks.objects.filter(id=task_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context={'names':name,'mem':mem}
    if mangivetasks.objects.filter(id=task_id,submited=''):
        return render(request, 'MANassignedtask1.html',context)

    else:
        return render(request, 'MANassignedtaskSubmitted.html',context)'''

def MANassignedtaskSubmitted(request):
    return render(request, 'MANassignedtaskSubmitted.html')
def MANassignedtask1(request):
    return render(request, 'MANassignedtask1.html')
def GiveTaskRemind(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    if request.method == 'POST':
        team = mangivetasks.objects.get(id=request.POST.get('team_id'))
        mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
        team.status = request.POST.get("status")
        team.save()
        return render(request,'MANRemindButtonSuccesfully.html',{'mem':mem})


def loadEmployees(request):
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(department=dept_id).all()
    return render(request, 'dropdown.html', {'name': names})


def loadDesignation(request):
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).values('designation').distinct()
    return render(request, 'Designation.html', {'Desig': Desig})


def MANemployees(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    edepartment1 = regdetails.objects.values('department').distinct().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'edepartments': edepartment1,'mem':mem}
    return render(request, 'MANemployees.html', context)


def MANemp(request):
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).filter(designation=desig_id).all().filter(branch=usernameM2)
    return render(request, 'MANemployeesearch.html', {'names': names})


def MANtasksuccess(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM = "dummy"
    member = mangivetasks(department=request.POST['department'], designation=request.POST['designation'],
                          employee=request.POST['employee'], task=request.POST['task'], date=datetime.now(),
                          duedate=request.POST['duedate'],branch=request.POST['branch'],assignedBy=usernameM,tester=request.POST['tester'])
    member.save()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANTaskGivetaskToEmployeeAssign.html',context)


def MANloademployeess(request):
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    desig_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(designation=desig_id).filter(department=dept_id).all().filter(branch=usernameM2)
    return render(request, 'dropdown.html', {'names': names})


def MANloaddesi(request):
    desi_id = request.GET.get('desi_id')
    desi = regdetails.objects.filter(department=desi_id).values('designation').distinct()
    return render(request, 'MANdesi.html', {'desi': desi})


def MANgiveprojects(request):
    department1 = regdetails.objects.values('department').distinct()
    context = {'departments': department1}
    return render(request, 'MANgivetasktoemployee.html', context)

def MANprojects(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANprojects.html',context)

def MANassignedproject(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    #pro=hrprojectsgive.objects.filter(assignedBy='MANAGER')
    pro=hrprojectsgive.objects.all().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANassignedproject.html',{'projects':pro,'mem':mem})

def MANassignedpro(request):
    # import pdb;pdb.set_trace()
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    proj_id=request.GET.get('prid')
    givpro=hrprojectsgive.objects.filter(id=proj_id).values()
    for ins_pro in givpro:
        lst_screenshot = []
        if ins_pro['json_screenshot']:
            for temp in ins_pro['json_screenshot']:
                lst_screenshot.append(settings.HOSTNAME + temp)
            ins_pro['json_screenshot'] = lst_screenshot
    #import pdb;pdb.set_trace()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    if hrprojectsgive.objects.filter(id=proj_id,testerok='Tested ok'):
        return render(request, 'MANassignedprojects1TS.html',{'pro':givpro,'mem':mem})
    if hrprojectsgive.objects.filter(id=proj_id,submited=''):
        return render(request, 'MANassignedprojects1.html',{'pro':givpro,'mem':mem})
    else:
        return render(request, 'MANassignedprojectsSubmitted.html', {'pro': givpro,'mem':mem})

def MANassignedprojects1(request):
    return render(request, 'MANassignedprojects1.html')

def MANassignedprojectsSubmitted(request):
    return render(request, 'MANassignedprojectsSubmitted.html')

    #--------------
def mangivepro(request):#giveprojects
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    department1=regdetails.objects.values('department').distinct().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    tester=regdetails.objects.values('name').distinct().filter(branch=usernameM2).filter(designation='Tester')
    context={'departments':department1,'mem':mem,'tester':tester}
    return render(request,'MANgiveproject.html',context)
#import datetime
def manprojectsuccess(request):
    print(request.POST['department'])
    print(request.POST['designation'])
    print(request.POST['employee'])
    print(request.POST['platform'])
    print(request.POST['title'])
    print(request.POST['email'])
    print(request.POST['phone'])
    #print(datetime.now())
    print(request.POST['duedate'])
    print(request.POST['description'])
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM = "dummy"
    member = hrprojectsgive(department=request.POST['department'], designation=request.POST['designation'],
                             employee=request.POST['employee'], platform=request.POST['platform'],
                             title=request.POST['title'], email=request.POST['email'], phone=request.POST['phone'],
                              duedate=request.POST['duedate'],
                             description=request.POST['description'],branch=request.POST['branch'],assignedBy=usernameM,tester=request.POST['tester'])
    member.save()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request,'manprojectsuccess.html',context)
def loadmantaskemp(request):
    eid = request.GET.get('emp_id')
    emails = regdetails.objects.filter(id=eid)
    data = emails[0].email + "," + emails[0].mobile + "," + emails[0].name + "," + emails[0].branch
    # data = json.dumps({"email": emails[0].email, "mobile": emails[0].mobile})
    return HttpResponse(data)

def loadmanprogive(request):
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(designation=desi_id).all().filter(department=dept_id).all().filter(branch=usernameM2)
    return render(request, 'manprogive.html', {'names': names})
def loadmanprodesi(request):
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    desi_id = request.GET.get('desi_id')
    desi = regdetails.objects.filter(department=desi_id).values('designation').distinct().filter(branch=usernameM2)
    return render(request, 'manprodesi.html', {'desi': desi})
def loadmanproemp(request):
    eid = request.GET.get('emp_id')
    emails = regdetails.objects.filter(id=eid)
    data = emails[0].email + "," + emails[0].mobile+","+emails[0].name+","+emails[0].branch
    # data = json.dumps({"email": emails[0].email, "mobile": emails[0].mobile})
    return HttpResponse(data)
def MANemployees1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request,'MANemployees1.html',{'emp':empdetails,'mem':mem})

def MANemployeetraineeflowchart(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    emp_name = request.GET.get('traineeName')
    empdetails=regdetails.objects.filter(trainer=emp_name)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request,'MANemployeeflowchart.html',{'emp':empdetails,'mem':mem})

#--------------------project Extension Request------------------------
def MANprojectextensionrequest(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    day_id=request.GET.get('extndid')
    day=hrprojectsgive.objects.filter(id=day_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANprojectextensionrequest.html',{'days':day,'mem':mem})

def MANprojectextensionrequest1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    days=hrprojectsgive.objects.filter(branch=usernameM2).all().filter(~Q(submited='submitted'))
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANprojectextensionrequest1.html',{'day':days,'mem':mem})

def extndaccptORreject(request):
    if request.method == 'POST':
        team = hrprojectsgive.objects.get(id=request.POST.get('team_id'))
        team.submited = request.POST.get("status")
        team.save()
        return render(request,'MANprojectextensionrequest1.html')

#-------------------
def manperfoDesignation(request):
    dept_id = request.GET.get('dept_id')
    Desigperfo = regdetails.objects.filter(department=dept_id).values('designation').distinct()
    return render(request, 'manperfoDesignation.html', {'Desigperfo': Desigperfo})
def MANperemp(request):
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).filter(designation=desig_id).all().filter(branch=usernameM2)
    return render(request, 'MANperfoemployeesearch.html', {'names': names})
def MANperformance(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    edepartment1 = regdetails.objects.values('department').distinct().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'perfodepartments': edepartment1,'mem':mem}
    return render(request, 'MANperformance.html', context)
def MANperformance1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request,'MANperformance1.html',{'emp':empdetails,'mem':mem})

def MANpie_chart(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    labels = []
    data = []
    emp_id = request.GET.get('empid')
    #empdetails=regdetails.objects.filter(id=emp_id)
    queryset = regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    for e1 in queryset:
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'MANpiechart.html', {
        'labels': labels,
        'data': data,
        'mem':mem,
    })
def MANbar_chart(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    labels = []
    data = []
    emp_id = request.GET.get('empid')
    #empdetails=regdetails.objects.filter(id=emp_id)
    queryset = regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    for e1 in queryset:
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'MANbarchart.html', {
        'labels': labels,
        'data': data,
        'mem':mem,
    })

def MANhrpie_chart(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    labels = []
    data = []
    emp_id = request.GET.get('empid')
    #empdetails=regdetails.objects.filter(id=emp_id)
    queryset = regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    for e1 in queryset:
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'MANpiechart.html', {
        'labels': labels,
        'data': data,
        'mem':mem,
    })
def MANhrbar_chart(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    labels = []
    data = []
    emp_id = request.GET.get('empid')
    #empdetails=regdetails.objects.filter(id=emp_id)
    queryset = regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    for e1 in queryset:
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
        labels.append('o')
        data.append(e1.o)
    return render(request, 'MANbarchart.html', {
        'labels': labels,
        'data': data,
        'mem':mem,
    })
def MANperinsert(request):
    if request.method == 'POST':
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        team.empPunctuality = request.POST.get("punctuality")
        team.empPerformance = request.POST.get("perfo")
        team.emptimelycompletion = request.POST.get("tim")
        team.empextrawork = request.POST.get("extra")
        team.empCreativity = request.POST.get("creativity")
        team.empattendance = request.POST.get("attend")
        team.save()
    return render(request,'MANmanageHR.html')

def MANmypropie_chart(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM = "dummy"
    labels = []
    data = []
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    queryset = regdetails.objects.filter(designation=usernameM)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'MANmanagerprofile1.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })
def MANmyprobar_chart(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM = "dummy"
    labels = []
    data = []
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    queryset = regdetails.objects.filter(designation=usernameM)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'MANmanagerprofile2.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })

#------------------
def traineeloadDesignation(request):
    dept_id = request.GET.get('dept_id')
    Desigtrain = regdetails.objects.filter(department=dept_id).distinct().filter(~Q(designation='TL')).distinct()
    return render(request, 'mantraineeDesignation.html', {'Desigtrain': Desigtrain})
def MANtraineebutton(request):
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).filter(designation=desig_id).filter(~Q(designation='TL')).distinct().filter(branch=usernameM2)
    return render(request, 'MANtraineeemployeesearch.html', {'names': names})
def MANtrainees(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    edepartment1 = regdetails.objects.values('department').distinct().filter(department='Software').filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'departments': edepartment1,'mem':mem}
    return render(request, 'MANtrainees.html', context)
def MANtrainees1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request,'MANtrainees1.html',{'emp':empdetails,'mem':mem})


#------marketing-------------------------
def MANmarketing(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANmarketing.html',context)
def Massignwork(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    MarkTl = regdetails.objects.filter(designation='Marketing TL').filter(branch=usernameM2)
    Tl = regdetails.objects.filter(designation='Marketing TL').filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'TLname': MarkTl,'TL':Tl,'mem':mem}
    return render(request, 'Massignwork.html', context)

def MANmarkassignwrk(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    work = Tltasks(marktype=request.POST['Mtype'], name=request.POST['Mtl'],
                  url=request.POST['url'], description=request.POST['descri'],
                   dttask=datetime.now(),branch=request.POST['branch'],
                   email=request.POST['email'],phone=request.POST['mobile'])

    work.save()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANmarketingassignwrksuccess.html',context)

def MANmarketingassignwrksuccess(request):
    return render(request, 'MANmarketingassignwrksuccess.html')

def MANmarketingMyWork(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANmarketingMyWork.html',context)
def MANmarkserviceslist(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    ser=service.objects.all().filter(brnch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmarkserviceslist.html',{'serv':ser,'mem':mem})
def MANmarkProductlist(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    pro=proandmarkng.objects.all().filter(brnch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmarkProductlist.html',{'productname':pro,'mem':mem})
def MANmarkRecriutmentlist(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    rec=recrutement.objects.all().filter(brnch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmarkRecriutmentlist.html',{'recruit':rec,'mem':mem})
def MANmarkProductDetails(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    pro_id= request.GET.get('proid')
    prductid=proandmarkng.objects.filter(id=pro_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmarkProductDetails.html', {'products': prductid,'mem':mem})


def MANmarkProductDetailsShare(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    pr_id=request.GET.get('prodid')
    prod=proandmarkng.objects.filter(id=pr_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    Mark_Tl = regdetails.objects.filter(designation='Marketing TL').all().filter(branch=usernameM2)
    return render(request, 'MANmarkProductDetailsShare.html',{'product':prod, 'TLs': Mark_Tl,'mem':mem})

def MANproductmarketingshare(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    print(request.POST['prname'])
    work=Tltasks(marktype='Product',proname=request.POST['prname'],newtarget=request.POST['target'],description=request.POST['descri'],
                            url=request.POST['url'],markTl=request.POST['tl'],dttask=datetime.now())
    work.save()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request,'MANmarketingassignwrksuccess.html',context)

def MANmarkServiceDetails(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    ser_id= request.GET.get('serviceid')
    servid=service.objects.filter(id=ser_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmarkServiceDetails.html', {'services': servid,'mem':mem})

def MANmarkServiceDetailsShare(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    btn_id=request.GET.get('buttnid')
    btnid=service.objects.filter(id=btn_id)
    service_id=regdetails.objects.filter(designation='Marketing TL').all()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmarkServiceDetailsShare.html', {'share': btnid, 'serv': service_id,'mem':mem})

def MANServicemarketingshare(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    service=Tltasks(marktype='Service',servicename=request.POST['service'],payment=request.POST['payment'],
                               description=request.POST['desc'],markTl=request.POST['tl'],dttask=datetime.now())
    service.save()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmarketingassignwrksuccess.html',{'mem':mem})


def MANmarkRecruitmentDetails(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    recruit_id=request.GET.get('recid')
    Recruit=recrutement.objects.filter(id=recruit_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request,'MANmarkRecruitmentDetails.html',{'recrutments':Recruit,'mem':mem})


def MANmarkRecruitmentDetailsShare(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    rec_Id=request.GET.get('recruId')
    recrut=recrutement.objects.filter(id=rec_Id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    rec1=regdetails.objects.filter(designation='Marketing TL').all().filter(branch=usernameM2)
    return render(request, 'MANmarkRecruitmentDetailsShare.html',{'rec':recrut,'recs':rec1,'mem':mem})
def MANrecruitmarketingshare(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    recruit=Tltasks(marktype='Recruitment',post=request.POST['post'],qualification=request.POST['quali'],
                               vacancies=request.POST['vacan'],markTl=request.POST['tl'],description=request.POST['des'],dttask=datetime.now())
    recruit.save()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANmarketingassignwrksuccess.html',context)

#------------------Marketing shared work-----------------------------

def MANmarketingSharedTask(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    names=Tltasks.objects.all().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmarketingSharedTask.html',{'name':names,'mem':mem})

def MANmarketingSharedTaskSub(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    task_id = request.GET.get('taskid')
    taskk = Tltasks.objects.filter(id=task_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    if Tltasks.objects.filter(id=task_id, submited=''):
        return render(request, 'MANmarketingSharedTask1.html', {'tasks': taskk,'mem':mem})
    else:
        return render(request, 'MANmarketingSharedTask2.html', {'tasks': taskk,'mem':mem})


def MANviewdatainsharedtask2(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    direct=Tlshareddatas.objects.all()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANviewdatainsharedtask2.html',{'directmeet':direct,'mem':mem})

def MANmarketingDirectMarketerfn(request):
    if request.method == 'POST':
        team = Tlshareddatas.objects.get(id=request.POST.get('team_id'))
        team.directmarketer = request.POST.get("directmarketer")
        team.save()
        return render(request,'MANmarketingassignwrksuccess.html')


def MANmarketingDirectMarketer(request):
    mark_id=request.GET.get('marketerid')
    mark=Tlshareddatas.objects.filter(id=mark_id)
    return render(request, 'MANmarketingDirectMarketer.html',{'marks':mark})

   # mar=request.GET.get('marketerid')
    #marketer=Execompletedtasks.objects.filter(id=mar)
    #return render(request,'MANmarketingDirectMarketer.html',{'mark':marketer})


#---------------------attendance------------------------
def MANattendance(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANattendance.html',context)
def MANemployeeAttendance(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    edepartment1 = employeeattendance.objects.values('department').distinct().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'edepartments': edepartment1,'mem':mem}
    return render(request, 'MANemployeeAttendance.html',context)
def loadmanemployeeatten(request):
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    dept_id = request.GET.get('dept_id')
    Desig = employeeattendance.objects.filter(department=dept_id).values('employee').distinct().filter(branch=usernameM2)
    return render(request, 'employeeattendanceMAN.html', {'Desig': Desig})
def employattendancebtn(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    dept_id = request.GET.get('regdetails')
    emp_Id = request.GET.get('regdetails1')
    frm_date = request.GET.get('frmdate')
    to_date = request.GET.get('todate')
    names = employeeattendance.objects.filter(department=dept_id).filter(employee=emp_Id).filter(date__range=(frm_date,to_date))
    template='MANemployeeAttendance1.html',
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, template, {'name': names,'mem':mem})

def MANHRAttendance(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    attn=regdetails.objects.filter(designation='Executive').filter(branch=usernameM2)
    attn1=regdetails.objects.filter(designation='Executive').filter(branch=usernameM2).distinct()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANHRAttendance.html',{'hr':attn,'hr1':attn1,'mem':mem})

def Mhrattendance(request):
    atten = employeeattendance(employee=request.POST['employee'],department=request.POST['department'],
                         date=request.POST['datename'], status=request.POST['status'],
                         logout=request.POST['logout'],login=request.POST['login'],branch=request.POST['branch'])

    atten.save()
    return render(request,'MANattendance.html')

def MANmyattendance(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANmyattendance.html',context)
def MANattendncemy(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    print('h')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).all().filter(branch=usernameM2).filter(employee=usernameM1)
    print(names.values('status','date','login','logout'))
    return render(request, 'MANattenMYTable.html', {'names': names})

#--------------ManageHR----------------------------------
def MANmanageHR(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANmanageHR.html',context)

def MANmanageHRgivetask(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    name=regdetails.objects.filter(branch=usernameM2).distinct()
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmanageHRgivetask.html',{'names':name,'mem':mem})
def givetasktoHR(request):
    task=HRtasks(task=request.POST['task'],date=datetime.now(),duedate=request.POST['duedate'],branch=request.POST['branch'])
    task.save()
    return render(request,'MANmanageHR.html')

def MANmanageHRsharedtask(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    name=HRtasks.objects.all().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmanageHRsharedtask.html',{'names':name,'mem':mem})

def MANmanagehrassigned(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    share_id=request.GET.get('shareid')
    share=HRtasks.objects.filter(id=share_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context={'shares':share,'mem':mem}
    if HRtasks.objects.filter(id=share_id,submited=''):
        return render(request, 'MANmanageHRsharedtask1.html',context)
    else:
        return render(request, 'MANmanageHRsharedtaskSubmitted.html',context)


def RemindAction(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    if request.method == 'POST':
        team = HRtasks.objects.get(id=request.POST.get('team_id'))
        mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
        team.status = request.POST.get("status")
        team.save()
        return render(request,'MANRemindButtonSuccesfully.html',{'mem':mem})
#MANmanageHRsharedtask
def MANManageHrPerformance1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM1 = "dummy"
    empdetails = regdetails.objects.filter(designation='Executive').filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request,'MANManageHrPerformance1.html',{'emp': empdetails,'mem':mem})
def MANManageHrPerformance(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails = regdetails.objects.filter(designation='Executive').filter(branch=usernameM2).filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANManageHrPerformance.html',{'emp': empdetails,'mem':mem})

def MANManageHrPerformanceUpdate(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails = regdetails.objects.filter(designation='Executive').filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANManageHrPerformanceUpdate.html',{'emp': empdetails,'mem':mem})


#------------Leave Request-----------------------------
def MANLeaverequests(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    leave=leavereq.objects.all().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANLeaverequests.html',{'leaves':leave,'mem':mem})
def MANLeaverequests1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    le_id=request.GET.get('leavId')
    le=leavereq.objects.filter(id=le_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANLeaverequests1.html', {'levs':le,'mem':mem})

def accptORreject(request):
    if request.method == 'POST':
        team = leavereq.objects.get(id=request.POST.get('team_id'))
        team.status = request.POST.get("status")
        team.save()
        return render(request,'MANattendance.html')

#-------------reported issue--------------------
def MANreportedissues(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANreportedissues.html',context)
def MANreportedissues1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    name=hrreport.objects.all().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANreportedissues1.html', {'names':name,'mem':mem})
def MANreportedissues2(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    emp_id=request.GET.get('empid')
    empid=hrreport.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANReportedissues2.html',{'emp':empid,'mem':mem})

def MANmytasks(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    task=admingivetask.objects.all().filter(branch=usernameM2).order_by('-id')
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmytasks.html',{'tasks':task,'mem':mem})

def MANtask1(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    task_id=request.GET.get('taskid')
    task=admingivetask.objects.filter(id=task_id)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    form = ImageFormManager()
    img = admingivetask.objects.all()
    if admingivetask.objects.filter(id=task_id,submited=''):
        return render(request, 'MANtask1.html', {'tasks1': task,"img": img, "form": form,'mem':mem})
    else:
        return render(request, 'MANtask2.html', {'tasks1': task,"img": img, "form": form,'mem':mem})

def MANmytaskupdate(request):
    if request.method == 'POST':
        team = admingivetask.objects.get(id=request.POST.get('team_id'))
        team.task = request.POST.get("status")
        team.submited='submitted'
        team.save()
        return render(request,'MANmarketingassignwrksuccess.html')

#-----------------------------Payments-------------------------------
#def MANpaymentBill22(request):
#    if request.session.has_key('username'):
#        username = request.session['username']
#    else:
#        username = "dummy"
 #   pay_id=request.GET.get('birthday')
 #   pay=acntspayslip.objects.filter(dateef=pay_id)
 #   return render(request, 'MANpaymentBill.html',{'pays':pay})

def MANPayments(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANPayments.html',context)

def MANPaymentsViewDetailButton(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    context = {'mem':mem}
    return render(request, 'MANPaymentsViewDetailButton.html',context)

def MANpayments33(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    else:
        usernameM1 = "dummy"
    pay=request.GET.get('birthday')
    pay1=acntspayslip.objects.filter(dateef=pay).filter(ename=usernameM1)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request,'MANpaymentBill.html',{'pays':pay1,'mem':mem})

def MANmyproject(request):
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    projectt=Project.objects.filter(assignedto=usernameM,branch=usernameM2).all()
    #task=hrprojectsgive.objects.filter(branch=usernameM2,employee=usernameM1).all().order_by('-id')
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    return render(request, 'MANmyproject.html',{'pro':projectt,'mem':mem})

def MANmyprojectsubtask(request):
    #import pdb;
    #pdb.set_trace()
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    if request.session.has_key('usernameMid'):
        usernameMid = request.session['usernameMid']
    else:
        usernameM2 = "dummy"

    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    emp_id = request.GET.get('prid')
    pro=Project.objects.filter(id=emp_id,branch=usernameM2)
    repo=Report.objects.filter(project_id=emp_id,branch=usernameM2).all()
    map = {}
    for i in repo:
        id = i.task_id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)
    #for Teststatus===========
    test = Testing.objects.filter(project_id=emp_id,branch=usernameM2).all()
    testmap={}
    for i in test:
        id = i.reportid.task_id
        if testmap.get(id) is None:
            list = []
            list.append(i)
            testmap[id] = list
        else:
            list = testmap.get(id)
            list.append(i)
    # for Extension Request===========
    extensionrqst = PrTasktoTL.objects.filter(project_id=emp_id,branch=usernameM2).all()
    Extensionmap = {}
    for i in extensionrqst:
        id = i.id
        if Extensionmap.get(id) is None:
            list = []
            list.append(i)
            Extensionmap[id] = list
        else:
            list = Extensionmap.get(id)
            list.append(i)


    emp1=PrTasktoTL.objects.filter(assignedby=usernameMid,project__id=emp_id,branch=usernameM2)
    #task1=PrTasktoTL.objects.filter(assignedby=usernameMid,project__id=emp_id,branch=usernameM2,)

    return render(request, 'MANmyprojectsubtask.html', { 'mem': mem, 'emp': emp1,'proj':pro,'rep':map,'testm':testmap,'extension':Extensionmap })
   # if emp_id ==None:
    #    emp = hrprojectsgive.objects.filter(title=emp_id).filter(assignedBy=usernameM).all()
    #    return render(request, 'MANmyprojectsubtasktable.html', { 'emp1': emp})

   # else:
     #   emp = hrprojectsgive.objects.filter(title=emp_id).filter(assignedBy=usernameM).all()
      #  task=hrprojectsgive.objects.all().filter(branch=usernameM2).order_by('-id')
      #  mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
      #  x=emp[0].title

       # return render(request, 'MANmyprojectsubtask.html',{'tasks':task,'mem':mem,'emp1':emp,'xx':x})


def MANmyprojectsubtaskAdd(request):

    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    if request.session.has_key('usernameMid'):
        usernameMid = request.session['usernameMid']
    else:
        usernameM2 = "dummy"
    emp_id = request.GET.get('prid')
    emp = PrTasktoTL.objects.filter(assignedby=usernameMid,project__id=emp_id,branch=usernameM2).all
    proj=Project.objects.filter(id=emp_id,branch=usernameM2)
    department1 = regdetails.objects.values('department').distinct().filter(branch=usernameM2)
    mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    tester = regdetails.objects.filter(branch=usernameM2).filter(designation='Tester')
    context = {'departments': department1,'mem':mem,'emp1':emp,'tester':tester,'pro':proj}
    return render(request, 'MANmyprojectsubtaskAdd.html', context)

def MANmyprojectSubtaskAddfun(request):
    #import pdb;
    #pdb.set_trace()
    if request.session.has_key('usernameM1'):
        usernameM1 = request.session['usernameM1']
    if request.session.has_key('usernameM'):
        usernameM = request.session['usernameM']
    if request.session.has_key('usernameMid'):
        usernameMid = request.session['usernameMid']
    else:
        usernameM = "dummy"
    #mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    if request.method == "POST":
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['taskattachfile']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                '''str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)'''
                
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                
        member = PrTasktoTL(department=request.POST['department'], designation=request.POST['designation'],
                            assignedto_id=request.POST['assignedto'],
                            project_id=request.POST['prid'], taskname=request.POST['task'],
                            startdate=request.POST['date'], duedate=request.POST['duedate'],
                            taskdescri=request.POST['descri'], branch=request.POST['branch'], assignedby_id=usernameMid,
                            testerid_id=request.POST['tester'],json_taskattachfile=lst_file)
        member.save()
        base_url = reverse('MANmyprojectsubtask')
        query_string = urlencode({'prid': member.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)


def MANDropdownemp(request):
    if request.session.has_key('usernameM2'):
        usernameM2 = request.session['usernameM2']
    else:
        usernameM2 = "dummy"
    desig_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(designation=desig_id).filter(department=dept_id).all().filter(branch=usernameM2)
    return render(request, 'MANdropdown.html', {'names': names})

def MANMyprojectsubtaskProjectstatus(request):
    if request.method == 'POST':
        team = PrTasktoTL.objects.get(id=request.POST.get('team_id'))
        team.prostatus = request.POST.get("status")
        team.progress = request.POST.get("progre")
        team.save()
        base_url = reverse('MANmyprojectsubtask')
        query_string = urlencode({'prid': team.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
            # return render(request,'DEProjectActiveProjects1.html')
def MANMyprojecttaskextensionstatus(request):
    if request.method == 'POST':
        team = PrTasktoTL.objects.get(id=request.POST.get('team_id'))
        team.status = request.POST.get("extstatus")

        team.save()
        base_url = reverse('MANmyprojectsubtask')
        query_string = urlencode({'prid': team.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

#==================================HR module=============================================================
def hr(request):
    emp_id = request.GET.get('empid')
    edepartments = mangivetasks.objects.filter(branch=emp_id)
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hr.html',{'mem':mem,'brs':edepartments})
def hrmypropie_chart(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr = "dummy"
    labels = []
    data = []
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    queryset = regdetails.objects.filter(designation=usernamehr)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'hrmyprofilepiechart.html', {
        'mem':mem,
        'labels': labels,
        'data': data,
    })
def hr1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr = "dummy"
    labels = []
    data = []
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    queryset = regdetails.objects.filter(designation=usernamehr)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'hr1.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })

#============================================tasks===============================
def hrtasks(request):
    regdetails3 = request.GET.get('empid')
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    give = mangivetasks.objects.all().filter(branch=regdetails3).values('branch').distinct()
    context = {'brs':give,'mem':mem}
    return render(request,'hrtasks.html',context)
def hrtasks1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    names = HRtasks.objects.all().filter(branch=usernamehr2)
    mem = regdetails.objects.filter(designation=usernamehr).filter(name=usernamehr1)
    context = {'names': names,'mem':mem}
    return render(request,'hrtasks1.html',context)
def hrmytasks(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    task_id=request.GET.get('taskid')
    task=HRtasks.objects.filter(id=task_id)
    mem = regdetails.objects.filter(designation=usernamehr).filter(name=usernamehr1)
    form = ImageFormHR()
    img = HRtasks.objects.all()
    if HRtasks.objects.filter(id=task_id,submited=''):
        return render(request, 'hrmy tasks.html', {'tasks1': task,"img": img, "form": form,'mem':mem})
    else:
        return render(request, 'hrmy tasks1.html', {'tasks1': task,'mem':mem})
def hrmydupdate(request):
    if request.method == "POST":
        team = HRtasks.objects.get(id=request.POST.get('team_id'))
        team.submited='submitted'
        form = ImageFormHR(data=request.POST, files=request.FILES, instance=team)
        form.save()
        return render(request, 'hrtasks.html', {'teams': team})
def hrgiveprojects(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    department1=regdetails.objects.values('department').filter(~Q(department='HR')).filter(~Q(department='')).filter(branch=usernamehr2).distinct()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context={'departments':department1,'mem':mem}
    return render(request,'hrgive projects.html',context)
def hrtasksuccess(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr = "dummy"
    member = mangivetasks(department=request.POST['department'], designation=request.POST['designation'],
                          employee=request.POST['employee'], task=request.POST['task'], date=datetime.now(),
                          duedate=request.POST['duedate'],branch=request.POST['branch'],assignedBy=usernamehr)
    member.save()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrtasksuccess.html',context)
def loadhremployeess(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(designation=desi_id).all().filter(department=dept_id).filter(branch=usernamehr2).all()
    return render(request, 'hrdropdown.html', {'names': names})
def loadhrdesi(request):
    desi_id = request.GET.get('desi_id')
    desi = regdetails.objects.filter(department=desi_id).values('designation').distinct()
    return render(request, 'hrdesi.html', {'desi': desi})
def hrassignedtasks(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    names = mangivetasks.objects.filter(assignedBy='Executive').filter(branch=usernamehr2).all()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context={'names':names,'mem':mem}
    return render(request,'hrassigned tasks.html',context)
def hrassigned1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    emp_id = request.GET.get('empid')
    names=mangivetasks.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'names': names,'mem':mem}
    if mangivetasks.objects.filter(id=emp_id,submited=''):
        return render(request,'hrassigned tasks1.html',context)
    else:
        return render(request,'hrassigned tasks2.html',context)
def hrGiveTaskRemind(request):
    if request.method == 'POST':
        team = mangivetasks.objects.get(id=request.POST.get('team_id'))
        team.status = request.POST.get("status")
        team.save()
        return render(request,'hrtasks.html')
def loadhrtaskemp(request):
    eid = request.GET.get('emp_id')
    emails = regdetails.objects.filter(id=eid)
    data = emails[0].email + "," + emails[0].mobile+","+emails[0].name+","+emails[0].branch
    #data = json.dumps({"email": emails[0].email, "mobile": emails[0].mobile})
    return HttpResponse(data)
#========================================Projects=========================================
def basenav(request):
    return render(request,'basenav.html')
    
def HRMANmyproject(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    projectt=Project.objects.all().filter(branch=usernamehr2)
    #task=hrprojectsgive.objects.filter(branch=usernameM2,employee=usernameM1).all().order_by('-id')
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    #return render(request, 'adminMANmyproject.html',{'pro':projectt,'mem':mem})
    return render(request,'HRMANmyproject.html',{'pro':projectt,'mem':mem})
def HRMANmyprojectsubtask(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    emp_id = request.GET.get('prid')
    emp = PrTasktoTL.objects.filter(project_id=emp_id,branch=usernamehr2).all
    proj=Project.objects.filter(id=emp_id).filter(branch=usernamehr2)
    repo = Report.objects.filter(project_id=emp_id,branch=usernamehr2).all()
    department1 = regdetails.objects.values('department').distinct().all()#.filter(branch=usernameM2)
    tester = regdetails.objects.all()#.filter(branch=usernameM2).filter(designation='Tester')
    map = {}
    for i in repo:
        id = i.task_id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)
    # for Test status===========

    test = Testing.objects.filter(project_id=emp_id,branch=usernamehr2).all()
    testmap = {}
    for i in test:
        id = i.reportid.task_id
        if testmap.get(id) is None:
            list = []
            list.append(i)
            testmap[id] = list
        else:
            list = testmap.get(id)
            list.append(i)

    # for extension status=====
    extensionrqst = PrTasktoTL.objects.filter(project_id=emp_id,branch=usernamehr2).all()
    Extensionmap = {}
    for i in extensionrqst:
        id = i.id
        if Extensionmap.get(id) is None:
            list = []
            list.append(i)
            Extensionmap[id] = list
        else:
            list = Extensionmap.get(id)
            list.append(i)

    test1 = Testing.objects.filter(project_id=emp_id)#,task_id=emp_id)
    #leave=Testing.objects.all().filter(project_id=emp_id)
    return render(request, 'HRMANmyprojectsubtaskAdd.html', {'mem': mem, 'emp1': emp, 'proj': proj, 'rep': map,'testm':testmap,'leave_object':test1,'extension':Extensionmap})

def hrprojects(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    #return render(request,'HRMANmyproject.html',context)
    return render(request, 'hrprojects.html',context)
def hrgivepro(request):#giveprojects
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    department1=regdetails.objects.values('department').filter(~Q(department='HR')).filter(~Q(department='')).filter(
        branch=usernamehr2).distinct()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context={'departments':department1,'mem':mem}
    return render(request,'hrgive projects2.html',context)
def hrprojectsuccess(request):
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    else:
        usernamehr = "dummy"
    member = hrprojectsgive(department=request.POST['department'], designation=request.POST['designation'],
                          employee=request.POST['employee'],platform=request.POST['platform'],
                          title=request.POST['title'],email=request.POST['email'],phone=request.POST['phone'], date=datetime.now(),
                          duedate=request.POST['duedate'],description=request.POST['description'],branch=request.POST['branch'],
                          assignedBy=usernamehr)
    member.save()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrprojectsuccess.html',context)
def loadhrprogive(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(designation=desi_id).all().filter(department=dept_id).filter(branch=usernamehr2).all()
    return render(request, 'hrprogive.html', {'names': names})
def loadhrprodesi(request):
    desi_id = request.GET.get('desi_id')
    desi = regdetails.objects.filter(department=desi_id).values('designation').distinct()
    return render(request, 'hrprodesi.html', {'desi': desi})
def loadhrproemp(request):
    eid = request.GET.get('emp_id')
    emails = regdetails.objects.filter(id=eid)
    data = emails[0].email + "," + emails[0].mobile+","+emails[0].name+","+emails[0].branch
    #data = json.dumps({"email": emails[0].email, "mobile": emails[0].mobile})
    return HttpResponse(data)
def hrassignedprojects(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    pro=hrprojectsgive.objects.filter(assignedBy='Executive').filter(branch=usernamehr2)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request, 'hrassigned projects.html',{'projects':pro,'mem':mem})
def hrassignedpro(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    proj_id=request.GET.get('prid')
    givpro=hrprojectsgive.objects.filter(id=proj_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    if hrprojectsgive.objects.filter(id=proj_id,submited=''):
        return render(request, 'hrprojects1.html',{'pro':givpro,'mem':mem})
    else:
        return render(request, 'hrprojects2.html', {'pro': givpro,'mem':mem})
#=================================report issues=========================================
def hrreportissues(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrreport issues.html',context)
def hrreport1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrreport1.html',context)
def hrreportsuccess(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr1 = "dummy"
    member= hrreport(issue=request.POST['issue'],date=datetime.now(),reportedby=usernamehr1,
                     designation=usernamehr,branch=usernamehr2)
    member.save()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrreportsuccess.html',context)
def hrreportedissue1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    names = hrreport.objects.filter(~Q(designation='Executive')).filter(branch=usernamehr2).all
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context={'names':names,'mem':mem}
    return render(request,'hrreported issue1.html',context)
def hrreportedissue2(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=hrreport.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    if hrreport.objects.filter(id=emp_id, actiontaken=''):
        return render(request,'hrreportactiontaken.html',{'emp':empdetails,'mem':mem})
    else:
        return render(request, 'hrreported issue2.html', {'emp': empdetails,'mem':mem})
def hrreportedupdate(request):
    if request.method == 'POST':
        team = hrreport.objects.get(id=request.POST.get('team_id'))
        team.actiontaken = request.POST.get("status")
        team.submit = 'Action taken'
        team.save()
        return render(request,'hrreport issues.html')
#======================================employees==================================
def hremployeess(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
         
    else:
        usernamehr1 = "dummy"
    edepartment=regdetails.objects.values('department').filter(department='Software').distinct()
    mem=regdetails.objects.filter(designation=usernamehr).filter(name=usernamehr1)
    
    context={'edepartments':edepartment,'mem':mem}
    return render(request, 'hremployeess.html',context)
def hremp(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).all().filter(designation=desig_id).filter(branch=usernamehr2).all()
    return render(request, 'hremployeesearch.html', {'names': names})
def hrempdesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).all().values('designation').filter(designation='TL').distinct()
    return render(request, 'hrempdesi.html', {'Desig': Desig})
def hremployees1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hremployees1.html',{'emp':empdetails,'mem':mem})
def hremployeeflowchart(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(trainer=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hremployeeflowchart.html',{'emp':empdetails,'mem':mem})
#====================================performance=======================
def hrperformance(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    edepartments = regdetails.objects.values('department').filter(branch=usernamehr2).filter(~Q(department='HR')).filter(~Q(department='')).filter(~Q(department='Manager')).filter(~Q(department='')).distinct()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'edepartments': edepartments,'mem':mem}
    return render(request, 'hrperformance.html', context)
def hrperformance1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hrperformance1.html',{'emp':empdetails,'mem':mem})
def hrperdesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).values('designation').distinct()
    return render(request, 'hrperdesi.html', {'Desig': Desig})
def hrper(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).filter(designation=desig_id).filter(branch=usernamehr2).all()
    return render(request, 'hrpersearch.html', {'names': names})
def hrperformance2(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hrperformance2.html',{'emp':empdetails,'mem':mem})
def hrperinsert(request):
    if request.method == 'POST':
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        team.empPunctuality = request.POST.get("punctuality")
        team.empPerformance = request.POST.get("perfo")
        team.emptimelycompletion = request.POST.get("tim")
        team.empextrawork = request.POST.get("extra")
        team.empCreativity = request.POST.get("creativity")
        team.empattendance = request.POST.get("attend")
        team.save()
    return render(request,'hrperformance1.html')
def pie_chart(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    labels = []
    data = []
    emp_id = request.GET.get('empid')
    #empdetails=regdetails.objects.filter(id=emp_id)
    queryset = regdetails.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    for e1 in queryset:
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'hrpie_chart.html', {
        'labels': labels,
        'data': data,
        'mem': mem,
    })
def bar_chart(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    labels = []
    data = []
    emp_id = request.GET.get('empid')
    #empdetails=regdetails.objects.filter(id=emp_id)
    queryset = regdetails.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    for e1 in queryset:
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'hrempbar.html', {
        'labels': labels,
        'data': data,
        'mem':mem,
    })


#================================trainee==============================
def hrtrainees1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    edepartment1 = regdetails.objects.values('department').distinct()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'departments': edepartment1,'mem':mem}
    return render(request, 'hrtrainees1.html', context)
def hrviewtrainee(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    edepartments = regdetails.objects.values('department').filter(department='Software').distinct()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'edepartments': edepartments,'mem':mem}
    return render(request,'hrview trainee.html',context)
def hrtraineedesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).distinct().filter(~Q(designation='TL'))
    return render(request, 'hrtraineedesi.html', {'Desig': Desig})
def hrtrainee(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).filter(designation=desig_id).filter(~Q(designation='TL')).filter(branch=usernamehr2).distinct()
    return render(request, 'hrtraineesearch.html', {'names': names})
def hrtrainees2(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hrtrainees2.html',{'emp':empdetails,'mem':mem})
def hrviewsyllabus(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    edepartments = syllabus.objects.values('department').filter(branch=usernamehr2).distinct()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'edepartments': edepartments,'mem':mem}
    print('hy')
    return render(request,'hrview syllabus.html',context)
def hrsyllabusdesi(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    dept_id = request.GET.get('dept_id')
    Desig = syllabus.objects.filter(department=dept_id).values('designation').filter(branch=usernamehr2).distinct()
    return render(request, 'hrsyllabusdesi.html', {'Desig': Desig})
def hrsyllabus(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = syllabus.objects.filter(department=dept_id).filter(designation=desig_id).values('topic','date','duedate').filter(branch=usernamehr2).distinct()
    msg=syllabus.objects.filter(department=dept_id).filter(designation=desig_id).values('topic','date','duedate').distinct().count()
    print(msg)
    return render(request, 'hrsyllabussearch.html', {'names': names})
def hrtrainees(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=syllabus.objects.filter(topic=emp_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hrtrainees.html',{'emp':empdetails,'mem':mem})
#====================================attendance==================================
def hrattendance(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrattendance.html',context)
def hrputattendance(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr2 = "dummy"
    edepartments = regdetails.objects.values('department').filter(branch=usernamehr2).distinct()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'edepartments': edepartments,'mem':mem}
    return render(request,'hrputattendance.html',context)
def hrattend(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).filter(branch=usernamehr2).all().values('name').distinct()
    return render(request, 'hrempput.html', {'Desig': Desig})
def hrputattendancesearch(request):
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).all().filter(name=desig_id).all()
    return render(request, 'hrputattendancesearch.html', {'names': names})
def empattend(request):
    '''for key in request.POST:
        print(key)
        value=request.POST[key]
        print(value)
    member= employeeattendance(department=request.POST['department'],date=request.POST['date'],employee=request.POST['employee'],
    )
    member.save()'''
    member = employeeattendance(department=request.POST['department'], date=request.POST['date'],
                               employee=request.POST['employee'], status=request.POST['status'],
                               branch=request.POST['branch'],login=request.POST['login'],logout=request.POST['logout'])
    member.save()
    return render(request,'hrattendance.html')
def hrattendance4(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request, 'hrattendance4.html',context)
def hrattendncemy(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    print('hai')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).all().filter(branch=usernamehr2).filter(employee=usernamehr1)
    print(names.values('status','date','login','logout'))
    return render(request, 'hratt.html', {'names': names})
def hrattendance5(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    edepartments = employeeattendance.objects.values('department').filter(branch=usernamehr2).distinct()
    mem = regdetails.objects.filter(designation=usernamehr).filter(name=usernamehr1)
    context = {'edepartments': edepartments,'mem':mem}
    return render(request,'hrattendance5.html',context)
def hremployeedesi(request):
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    dept_id = request.GET.get('dept_id')
    Desig = employeeattendance.objects.filter(department=dept_id).values('employee').filter(branch=usernamehr2).distinct()
    return render(request, 'hremployeedesi.html', {'Desig': Desig})
def hremployeeattend(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    dept_id = request.GET.get('regdetails')
    desig_id = request.GET.get('regdetails1')
    date1_id = request.GET.get('fromdate')
    date2_id = request.GET.get('todate')
    names = employeeattendance.objects.filter(date__range=(date1_id,date2_id)).filter(department=dept_id).all().filter(employee=desig_id).all()
    mem = regdetails.objects.filter(designation=usernamehr).filter(name=usernamehr1)
    template='hrattendance6.html',
    return render(request, template, {'names': names,'mem':mem})
#==================================leave req==================================
def hrattendance2(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrattendance2.html',context)
def hrattendance1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrattendance1.html',context)
def hrattendance3(request):
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr = "dummy"
    member= leavereq(assignedBy=usernamehr1,leavefrom=request.POST['leavefrom'],leaveto=request.POST['leaveto'],reason=request.POST['reason'],
                     department=usernamehr,branch=usernamehr2)
    member.save()
    return render(request,'hrattendance2.html')
def hrreqleaves(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    if request.session.has_key('usernamehr2'):
        usernamehr2 = request.session['usernamehr2']
    else:
        usernamehr2 = "dummy"
    names = leavereq.objects.filter(branch=usernamehr2)#all()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context={'names':names,'mem':mem}
    return render(request,'hrreq leaves.html',context)
#====================================payments======================================================
def hrPayments1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrPayments1.html',context)
def hrPaymentsViewDetailButton(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrPaymentsViewDetailButton.html',context)
def hrpayments33(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
        if request.session.has_key('usernamehr'):
            usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    pay=request.GET.get('birthday')
    #pay1=acntspayslip.objects.filter(dateef=pay).filter(ename=usernamehr1)
    pay1=acntspayslip.objects.filter(dateef=pay).filter(ename=usernamehr1)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hrpayments3.html',{'pays':pay1,'mem':mem})
#=====================================marketing======================
def hrmarketing1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    context = {'mem':mem}
    return render(request,'hrmarketing1.html',context)
def hrsharedtask1(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    names=Tltasks.objects.filter(marktype='Product')
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hrshared task1.html',{'name':names,'mem':mem})
def hrsharedtasks2(request):
    return render(request,'hrshared tasks2.html')
def hrsharedtasks(request):
    return render(request,'hrshared tasks.html')
def hrviewdeatails(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    direct=Tlshareddatas.objects.all()
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    return render(request,'hrviewdeatails.html',{'directmeet':direct,'mem':mem})
def hrmarketingSharedTaskSub(request):
    if request.session.has_key('usernamehr1'):
        usernamehr1 = request.session['usernamehr1']
    if request.session.has_key('usernamehr'):
        usernamehr = request.session['usernamehr']
    else:
        usernamehr1 = "dummy"
    task_id = request.GET.get('taskid')
    taskk = Tltasks.objects.filter(id=task_id)
    mem=regdetails.objects.filter(designation=usernamehr) .filter(name=usernamehr1)
    if Tltasks.objects.filter(id=task_id, submited=''):
        return render(request, 'hrshared tasks2.html', {'tasks': taskk,'mem':mem})
    else:
        return render(request, 'hrshared tasks.html', {'tasks': taskk,'mem':mem})

#=========================================Accounts module=====================
def accounts(request):
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    else:
        usernameacnt1 = "dummy"
    mem=regdetails.objects.filter(designation=usernameacnt) .filter(name=usernameacnt1)
    return render(request,'accounts.html',{'mem':mem})
def acnmypropie_chart(request):
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    else:
        usernameacnt1 = "dummy"
    mem=regdetails.objects.filter(designation=usernameacnt) .filter(name=usernameacnt1)
    labels = []
    data = []
    queryset = regdetails.objects.filter(designation=usernameacnt)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'acntspiechart.html', {
        'mem':mem,
        'labels': labels,
        'data': data,
    })
def accounts1(request):
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    else:
        usernameacnt1 = "dummy"
    mem=regdetails.objects.filter(designation=usernameacnt) .filter(name=usernameacnt1)
    labels = []
    data = []
    queryset = regdetails.objects.filter(designation=usernameacnt)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'accounts1.html', {
        'mem':mem,
        'labels': labels,
        'data': data,
    })
#=================================employees==================================
def acntemp(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    if request.session.has_key('usernameacnt2'):
        usernameacnt2 = request.session['usernameacnt2']
    else:
        usernameacnt2 = "dummy"
    edepartments = regdetails.objects.values('department').distinct().filter(branch=usernameacnt2)
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'edepartments': edepartments,'mem':mem}
    return render(request,'acntemp.html',context)
def acntempdesi(request):
    if request.session.has_key('usernameacnt2'):
        usernameacnt2 = request.session['usernameacnt2']
    else:
        usernameacnt2 = "dummy"
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).values('designation').distinct().filter(branch=usernameacnt2)
    return render(request, 'acntempdesi.html', {'Desig': Desig})
def accountemp(request):
    if request.session.has_key('usernameacnt2'):
        usernameacnt2 = request.session['usernameacnt2']
    else:
        usernameacnt2 = "dummy"
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).filter(designation=desig_id).filter(branch=usernameacnt2).all()
    return render(request, 'acntemployeesearch.html', {'names': names})
def acntemp1(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(employeeid=emp_id)
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'emp':empdetails,'mem':mem}
    return render(request,'acntemp1.html',context)
def acntemp2(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(employeeid=emp_id)
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'emp':empdetails,'mem':mem}
    return render(request,'acntemp2.html',context)
def acntempupdate(request):
    if request.method == 'POST':
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        team.dispname = request.POST.get("dispname")
        team.gender = request.POST.get("gender")
        team.blood = request.POST.get("blood")
        team.acntno = request.POST.get("acntno")
        team.ifsc = request.POST.get("ifsc")
        team.taxregime = request.POST.get("taxregime")
        team.pan = request.POST.get("pan")
        team.aadhar = request.POST.get("aadhar")
        team.uan = request.POST.get("uan")
        team.pf = request.POST.get("pf")
        team.eps = request.POST.get("eps")
        team.datepf = request.POST.get("datepf")
        team.pr = request.POST.get("pr")
        team.esi = request.POST.get("esi")
        team.esiname = request.POST.get("esiname")
        team.contractstart = request.POST.get("contractstart")
        team.contractexpry = request.POST.get("contractexpry")
        team.bankname=request.POST.get("bankname")
        team.save()
        
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    if request.session.has_key('usernameacnt2'):
        usernameacnt2 = request.session['usernameacnt2']
    else:
        usernameacnt2 = "dummy"
    edepartments = regdetails.objects.values('department').distinct().filter(branch=usernameacnt2)
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'edepartments': edepartments,'mem':mem}
    
    return render(request,'acntemp.html',context)
def acntdefine(request):
    print('hai')
    member= acntspayslip(dateef=request.POST['dateef'],ename=request.POST['enam'],eno=request.POST['employeeid'],
                         bank=request.POST['bankname'],branch=request.POST['branch'],
                         email=request.POST['email'],acntno=request.POST['acntno'],
                         basicpay=request.POST['basicpay'],basictype=request.POST['basictype'],
                         hrapay=request.POST['hrapay'],hratype=request.POST['hratype'],
                         conpay=request.POST['conpay'],contype=request.POST['contype'],
                         propay=request.POST['propay'],protype=request.POST['protype'],
                         basic='Basic salary',hra='HRA',con='Conveyence allowance',
                         pro='Profesional tax',department=request.POST['department'],
                         designation=request.POST['designation'],pr=request.POST['pr'],
                         pf=request.POST['pf'],datejoin=request.POST['datejoin'],
                         taxengime=request.POST['taxengime'],uan=request.POST['uan'],
                         esi=request.POST['esi'],incometax=request.POST['pan'])
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    if request.session.has_key('usernameacnt2'):
        usernameacnt2 = request.session['usernameacnt2']
    else:
        usernameacnt2 = "dummy"
    edepartments = regdetails.objects.values('department').distinct().filter(branch=usernameacnt2)
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'edepartments': edepartments,'mem':mem}
    member.save()
    return render(request,'acntemp.html',context)
    
    
    
#==============================expenses=================================================
def acntexpenses(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    names=acntexpensest.objects.all()
    context = {'names': names,'mem':mem}
    return render(request,'acntexpenses.html',context)
def acntnewt(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'mem':mem}
    return render(request,'acntnewt.html',context)
def acntnewtsave(request):
    member = acntexpensest(payee=request.POST['payee'], payacnt=request.POST['payacnt'],
                               paymethod=request.POST['paymethod'], paydate=request.POST['paydate'],
                               refno=request.POST['refno'], category=request.POST['category'],
                               description=request.POST['description'], amount=request.POST['amount'],
                               tax=request.POST['tax'],total=request.POST['total'])
    member.save()
    war=acntexpensest.objects.all()
    mem=regdetails.objects.all()
    return render(request,'acntexpenses.html',{'names':war,'mem':mem})
def acntexpviewedit(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    emp_id = request.GET.get('empid')
    empdetails=acntexpensest.objects.filter(id=emp_id)
    context = {'emp':empdetails,'mem':mem}
    return render(request,'acntexpviewedit.html',context)
def acntexpvieweditupdate(request):
    if request.method == 'POST':
        team = acntexpensest.objects.get(id=request.POST.get('team_id'))
        team.payee = request.POST.get("payee")
        team.paymethod = request.POST.get("paymethod")
        team.paydate = request.POST.get("paydate")
        team.payacnt = request.POST.get("payacnt")
        team.refno = request.POST.get("refno")
        team.category = request.POST.get("category")
        team.description = request.POST.get("description")
        team.amount = request.POST.get("amount")
        team.tax = request.POST.get("tax")
        team.total = request.POST.get("total")
        team.save()
        war=acntexpensest.objects.all()
        mem=regdetails.objects.all()
        return render(request,'acntexpenses.html',{'names':war,'mem':mem})
#=============================================receipts==============================
def acntreceipts(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'mem':mem}
    return render(request,'acntreceipts.html',context)
def acntviewreceipts(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    edepartments = regdetails.objects.values('department').distinct()
    context = {'edepartments': edepartments,'mem':mem}
    return render(request,'acntviewreceipts.html',context)
def acntviewattend(request):
    if request.session.has_key('usernameacnt2'):
        usernameacnt2 = request.session['usernameacnt2']
    else:
        usernameacnt2 = "dummy"
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(department=dept_id).filter(branch=usernameacnt2).all()
    return render(request, 'acntviewreceiptsearch.html', {'names': names})


def acntview1(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    emp_id = request.GET.get('emp_id')
    emp=drrpayment.objects.filter(id=emp_id)
    context = {'emp':emp,'mem':mem}
    return render(request,'acntview1.html',context)
def acntsendpay(request):
     if request.session.has_key('usernameacnt'):
         usernameacnt = request.session['usernameacnt']
     if request.session.has_key('usernameacnt1'):
         usernameacnt1 = request.session['usernameacnt1']
     mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
     edepartments = regdetails.objects.values('department') .distinct()
     context = {'edepartments': edepartments,'mem':mem}
     return render(request,'acntsendpay.html',context)
def acntattend(request):
     if request.session.has_key('usernameacnt2'):
         usernameacnt2 = request.session['usernameacnt2']
     else:
         usernameacnt2 = "dummy"
     dept_id = request.GET.get('dept_id')
     names = regdetails.objects.filter(department=dept_id).filter(branch=usernameacnt2).all()
     #n1=acntreceipt.objects.filter(department=dept_id).all()
     return render(request, 'acntsendpaysearch.html', {'names': names})
def acntsendinsert(request):
    '''if request.method == 'POST':
        team = drrpayment.objects.get(id=request.POST.get('team_id'))
        team.department = request.POST.get("department")
        team.name = request.POST.get("name")
        team.duedate = request.POST.get("duedate")
        team.save()
        return render(request,'acntreceipts.html')'''
    branch1 = drrpayment(name=request.POST['name'],department=request.POST.get('department'),duedate=request.POST.get('duedate'),
                         branch=request.POST.get('branch'),designation=request.POST.get('designation'),
                         mobile=request.POST.get('mobile'),duration=request.POST.get('duration'),refid=request.POST.get('refid'))
    branch1.save()
    return render(request, 'acntreceipts.html')
def acntremain(request):
    if request.method == 'POST':
        team = drrpayment.objects.get(id=request.POST.get('team_id'))
        team.payment = request.POST.get("pending")
        team.save()
        return render(request,'acntreceipts.html')
def acntrdecline(request):
    if request.method == 'POST':
        team = drrpayment.objects.get(id=request.POST.get('team_id'))
        team.pending = request.POST.get("decline")
        team.save()
        return render(request,'acntreceipts.html')
def acntpayhis(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    if request.session.has_key('usernameacnt2'):
        usernameacnt2 = request.session['usernameacnt2']
    else:
        usernameacnt2 = "dummy"
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    names = drrpayment.objects.filter(department="Software")#.filter(branch=usernameacnt2)
    context = {'names': names,'mem':mem}
    return render(request,'acntpayhis.html',context)

#=============================account payslip=======================================
def acntpayslips(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    names=acntspayslip.objects.all()
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'names': names,'mem':mem}
    print('fy')
    return render(request, 'acntpayslips.html', context)
def acntpay(request):
    if request.session.has_key('usernameacnt2'):
        usernameacnt2 = request.session['usernameacnt2']
    else:
        usernameacnt2 = "dummy"
    print('hai')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = acntspayslip.objects.filter(dateef__range=(dept_id,desig_id)).filter(branch=usernameacnt2).all()
    template='acntpay.html',
    return render(request, template, {'names': names})
def acntpay1(request):
    if request.session.has_key('usernameacnt'):
        usernameacnt = request.session['usernameacnt']
    if request.session.has_key('usernameacnt1'):
        usernameacnt1 = request.session['usernameacnt1']
    emp_id = request.GET.get('empid')
    empdetails=acntspayslip.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernameacnt).filter(name=usernameacnt1)
    context = {'emp':empdetails,'mem':mem}
    return render(request,'acntpay1.html',context)
def acntpayinsert(request):
    emp_id = request.GET.get('empid')
    empdetails=acntspayslip.objects.filter(id=emp_id)

    if request.method == 'POST':
        team = acntspayslip.objects.get(id=request.POST.get('team_id'))
        team.leavesno = request.POST.get("leaveno")
        team.totalearning = request.POST.get("totalearning")
        team.totaldeduction = request.POST.get("totalduduction")
        team.netamt = request.POST.get("netamt")
        team.save()
        return render(request,'acntpayslips.html',{'emp':empdetails})
class acntGeneratePdf(View):
    def get(self, request, *args, **kwargs):
        emp_id = request.GET.get('empid')
        #intern = regdetails.objects.filter(id=emp_id)#get(id=id)
        #empdetails = regdetails.objects.all()#filter(id=emp_id)
        emp_id = request.GET.get('empid')
        intern = acntspayslip.objects.filter(id=emp_id)
        data = {'names': intern}
        #data = {
#             'today': datetime.date.today(),
        #     'amount': 39.99,
         #   'customer_name': 'Cooper Mann',
          #  'order_id': 1233434,
        #}
        pdf = render_to_pdf('acntpayprint.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
def acntprint(request):
    emp_id = request.GET.get('empid')
    names = acntspayslip.objects.filter(id=emp_id)
    return render(request, 'acntpayprint.html', {'emp': names})


#-----------------------------TL-------------------------------------------------------
def tl(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    else:
        usernametl1 = "dummy"
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    return render(request,'TL.html',{'mem':mem})
def tlmypropie_chart(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    else:
        usernametl = "dummy"
    labels = []
    data = []
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    queryset = regdetails.objects.filter(designation=usernametl)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'TLmyprofilepiechart.html', {
        'mem':mem,
        'labels': labels,
        'data': data,
    })
def tl1(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernamehr'):
        usernametl = request.session['usernametl']
    else:
        usernametl = "dummy"
    labels = []
    data = []
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    queryset = regdetails.objects.filter(designation=usernametl)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'TL1.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })
def tlattendance2(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context={'mem':mem}
    return render(request, 'TLattendance2.html',context)
def tlattendance1(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context={'mem':mem}
    return render(request,'TLattendance1.html',context)
def tlattendance3(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl = "dummy"
    member= leavereq(assignedBy=usernametl1,leavefrom=request.POST['leavefrom'],leaveto=request.POST['leaveto'],reason=request.POST['reason'],
                     department=usernametl,branch=usernametl2)
    member.save()
    return render(request,'TLattendance2.html')
def tlreqleaves(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    names = leavereq.objects.filter(branch=usernametl2).filter(assignedBy=usernametl1)#all()
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context={'names':names,'mem':mem}
    return render(request,'TLreqleaves.html',context)
def tlPayments1(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    #empdetails=[acntspayslip.objects.latest('ename')]#filter(id=emp_id)
    context={'mem':mem}#,'emp':empdetails}
    return render(request,'TLPayments1.html',context)
def tlPaymentsViewDetailButton(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context={'mem':mem}
    return render(request,'TLPaymentsViewDetailButton.html',context)
def tlpayments33(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl1 = "dummy"
    pay=request.GET.get('birthday')
    #pay1=acntspayslip.objects.filter(dateef=pay).filter(ename=usernamehr1)
    pay1=acntspayslip.objects.filter(dateef=pay).filter(ename=usernametl1)
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    return render(request,'TLpayments3.html',{'pays':pay1,'mem':mem})
def tlreportissues(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context={'mem':mem}
    return render(request,'TLreportissues.html',context)
def tlreportedissue1(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    names = hrreport.objects.filter(reportedby=usernametl1).filter(branch=usernametl2).all
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context={'names':names,'mem':mem}
    return render(request,'TLreportedissue1.html',context)
def tlreportedissue2(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    emp_id=request.GET.get('empid')
    empid=hrreport.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    return render(request, 'TLreportedissue2.html',{'emp':empid,'mem':mem})
def tlreport1(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context = {'mem':mem}
    return render(request,'TLreport1.html',context)
def tlreportsuccess(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    member= hrreport(issue=request.POST['issue'],date=datetime.now(),reportedby=usernametl1,
                     designation=usernametl,branch=usernametl2)
    member.save()
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context = {'mem':mem}
    return render(request,'TLreportsuccess.html',context)
def tlemployeess(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    else:
        usernametl1 = "dummy"
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context={'mem':mem}
    print('hy')
    return render(request,'TLattendance.html',context)
def tlattendncemy(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    print('hai')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).all().filter(employee=usernametl1).filter(branch=usernametl2)
    print(names.values('status','date','login','logout'))
    return render(request, 'TLatt.html', {'names': names})
'''def tlperformance(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl4'):
        usernametl4 = request.session['usernametl4']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    #names = hrprojectsgive.objects.filter(branch=usernametl2).filter(employee=usernametl1).all()
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    names = PrTasktoTL.objects.filter(assignedto_id=usernametl4)
    #names = hrprojectsgive.objects.filter(employee=usernametl1)
    context={'names':names,'mem':mem}
    return render(request,'TLMANmyproject.html',context)'''
    #return render(request,'TLProjects.html',context)
def TLMANmyprojectsubtask(request):
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    else:
        usernametl1 = "dummy"
    mem=regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    emp_id = request.GET.get('prid')
    emp = PrTasktoTL.objects.filter(project_id=emp_id,branch=usernametl2).all
    proj=Project.objects.filter(id=emp_id).filter(branch=usernametl2)
    repo = Report.objects.filter(project_id=emp_id,branch=usernametl2).all()
    department1 = regdetails.objects.values('department').distinct().all()#.filter(branch=usernameM2)
    tester = regdetails.objects.all()#.filter(branch=usernameM2).filter(designation='Tester')
    map = {}
    for i in repo:
        id = i.task_id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)
    # for Test status===========

    test = Testing.objects.filter(project_id=emp_id,branch=usernametl2).all()
    testmap = {}
    for i in test:
        id = i.task_id
        if testmap.get(id) is None:
            list = []
            list.append(i)
            testmap[id] = list
        else:
            list = testmap.get(id)
            list.append(i)

    # for extension status=====
    extensionrqst = PrTasktoTL.objects.filter(project_id=emp_id,branch=usernametl2).all()
    Extensionmap = {}
    for i in extensionrqst:
        id = i.id
        if Extensionmap.get(id) is None:
            list = []
            list.append(i)
            Extensionmap[id] = list
        else:
            list = Extensionmap.get(id)
            list.append(i)

    test1 = Testing.objects.filter(project_id=emp_id)#,task_id=emp_id)
    return render(request, 'TLMANmyprojectsubtaskAdd.html', {'mem': mem, 'emp1': emp, 'proj': proj, 'rep': map,'testm':testmap,'leave_object':test1,'extension':Extensionmap})
def TLMANMyprojectsubtaskProjectstatus(request):
    if request.method == 'POST':
        team = PrTasktoTL.objects.get(id=request.POST.get('team_id'))
        team.prostatus = request.POST.get("status")
        team.progress = request.POST.get("progre")
        team.save()
        base_url = reverse('TLMANmyprojectsubtask')
        query_string = urlencode({'prid': team.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
def tlsplitpro(request):
    emp_id = request.GET.get('prid')
    emp = PrTasktoTL.objects.filter(id=emp_id).all
    context = {'emp1':emp}
    return render(request,'TLMANsplitpro.html',context)
def tlprojects2(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    proj_id=request.GET.get('prid')
    givpro=hrprojectsgive.objects.filter(id=proj_id).values()

    for ins_pro in givpro:
        lst_screenshot = []
        if ins_pro['json_screenshot']:
            for temp in ins_pro['json_screenshot']:
                lst_screenshot.append(settings.HOSTNAME + temp)
            ins_pro['json_screenshot'] = lst_screenshot
    #import pdb;pdb.set_trace()
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    if hrprojectsgive.objects.filter(id=proj_id,testerok='Tested ok'):
        return render(request, 'TLassignedprojects2.html',{'pro':givpro,'mem':mem})
    if hrprojectsgive.objects.filter(id=proj_id,submited=''):
        return render(request, 'TLProjects2.html',{'pro':givpro,'mem':mem})
    else:
        return render(request, 'TLProjects3.html', {'pro': givpro,'mem':mem})

    '''emp_id=request.GET.get('empid')
    task=hrprojectsgive.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    form = TLProjectFileForm()
    img = hrprojectsgive.objects.all()
    if hrprojectsgive.objects.filter(id=emp_id,submited=''):
        return render(request, 'TLProjects2.html', {'names': task,"img": img, "form": form,'mem':mem})
    else:
        return render(request, 'TLProjects3.html', {'tasks1': task,'mem':mem})'''
    #return render(request,'TLProjects2.html')
def tlproject2add(request):
    if request.session.has_key('usernametl4'):
        usernametl4 = request.session['usernametl4']
    else:
        usernametl4 = "dummy"
    if request.method == "POST":

        team = hrprojectsgive.objects.get(id=request.POST.get('team_id'))
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['screenshot']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)
        team.submited='submitted'
        #team.nameid= request.POST.get("usernametl4")
        form = TLProjectFileForm(data=request.POST, files=request.FILES, instance=team)
        #form.screenshot = request.FILES.getlist('screenshot')
        form.save()
        #import pdb;pdb.set_trace()
        hrprojectsgive.objects.filter(id=int(request.POST.get('team_id'))).update(json_screenshot=lst_file)
        return render(request, 'TLprojects2success.html', {'teams': team})
    return render(request, 'TLProjects3.html')#, {'tasks1': task,"img": img, "form": form})'''
def tlprojects2assign(reqest):
    return render(reqest,'TLprojects2assign.html')
def tlprojects2extend(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    else:
        usernametl1 = "dummy"
    emp_id = request.GET.get('empid')
    edepartments1 = hrprojectsgive.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context={'mem':mem,'edepartments1':edepartments1}
    return render(request,'TLprojects2extend.html',context)
def tlprojects2extendadd(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl3'):
        usernametl3 = request.session['usernametl3']
    else:
        usernametl3 = "dummy"
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context = {'mem': mem}
    if request.method == 'POST':
        team = hrprojectsgive.objects.get(id=request.POST.get('team_id'))
        team.rqstdays = request.POST.get("rqstdays")
        team.reason = request.POST.get("reason")
        print('hy')
        team.save()
    return render(request,'TLproextendsuccess.html',context)
def tlprojects2success(request):
    return render(request,'TLprojects2success.html')
def tlprojects3(request):
    return render(request,'TLProjects3.html')
def tlprojects(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    names = mangivetasks.objects.filter(branch=usernametl2).filter(employee=usernametl1).all()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context={'names':names,'mem':mem}
    return render(request,'TLTask.html',context)
def tltask2(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl1 = "dummy"
    emp_id=request.GET.get('empid')
    task=mangivetasks.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    form = TLTaskFileForm()
    img = mangivetasks.objects.all()
    if mangivetasks.objects.filter(id=emp_id,submited=''):
        return render(request, 'TLtask2.html', {'names': task,"img": img, "form": form,'mem':mem})
    else:
        return render(request, 'TLtask3.html', {'tasks1': task,'mem':mem})
    #emp_id = request.GET.get('empid')
    #names = mangivetasks.objects.filter(id=emp_id)
    #context = {'names': names}
    #return render(request,'TLtask2.html',context)
def tltask2add(request):
    if request.method == "POST":

        team = mangivetasks.objects.get(id=request.POST.get('team_id'))
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['screenshot']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)
        team.submited='submitted'
        form = TLTaskFileForm(data=request.POST, files=request.FILES, instance=team)
        #form.screenshot = request.FILES.getlist('screenshot')
        form.save()
        #import pdb;pdb.set_trace()
        mangivetasks.objects.filter(id=int(request.POST.get('team_id'))).update(json_screenshot=lst_file)
        return render(request, 'TLprojects2success.html', {'teams': team})
    return render(request, 'hrmy tasks.html')#, {'tasks1': task,"img": img, "form": form})
def tltasks(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    else:
        usernametl1 = "dummy"
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'mem':mem}
    return render(request, 'TLtrainees.html',context)
def tlviewtrainee(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    tr = regdetails.objects.filter(department='Software').filter(~Q(designation='TL')).filter(trainer=usernametl1).filter(branch=usernametl2)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'tr':tr,'mem':mem}
    return render(request,'TLviewtrainee.html',context)
def tlviewtrainee1(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl1 = "dummy"
    emp_id = request.GET.get('empid')
    tr = regdetails.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'tr':tr,'mem':mem}
    return render(request,'TLviewtrainees1.html',context)
def tluploadtopics(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    tr = syllabus.objects.filter(branch=usernametl2).all().filter(trainer=usernametl1)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'tr':tr,'mem':mem}
    return render(request,'TLuploadtopics.html',context)
def tluploadtopicsadd(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    member = syllabus(topic=request.POST['topic'],duedate=request.POST['duedate'],
                      date=request.POST['date'],branch=usernametl2,trainer=usernametl1)
    member.save()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'mem':mem}
    return render(request,'TLuploadtopicsuccess.html',context)
def tlweeklytasks(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl1 = "dummy"
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'mem':mem}
    return render(request,'TLweeklytasks.html',context)
def tlgivetasks(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    tr = regdetails.objects.filter(department='Software').filter(~(Q(designation='TL'))).filter(trainer=usernametl1).filter(branch=usernametl2)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'tr': tr,'mem':mem}
    return render(request,'TLgivetasks.html',context)
def tlgivetasksadd(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    member = TeamLeadweeklytask(name=request.POST['name'], task=request.POST['task'],
                          duedate=request.POST['duedate'], date=datetime.now(),assignedBy=usernametl1,branch=usernametl2)
    member.save()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'mem':mem}
    return render(request,'TLtasksuccess.html',context)
def tltaskgiven(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    names = TeamLeadweeklytask.objects.filter(assignedBy=usernametl1).filter(branch=usernametl2).all()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context={'names':names,'mem':mem}
    return render(request,'TLtaskgiven.html',context)
def tltrtask2(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl1 = "dummy"
    emp_id=request.GET.get('empid')
    task=TeamLeadweeklytask.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    form = TLTaskFileForm()
    img = TeamLeadweeklytask.objects.all()
    if TeamLeadweeklytask.objects.filter(id=emp_id,submited=''):
        return render(request, 'TLtasknotsubmit.html', {'names': task,"img": img, "form": form,'mem':mem})
    else:
        return render(request, 'TLtasksubmit.html', {'tasks1': task,'mem':mem})
def tltasknotsubmit(request):
    return render(request,'TLtasknotsubmit.html')
def tltasksubmit(request):
    return render(request,'TLtasksubmit.html')
def tltasksubmit2(request):
    # import pdb;pdb.set_trace()
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    else:
        usernametl1 = "dummy"
    proj_id=request.GET.get('prid')
    givpro=TeamLeadweeklytask.objects.filter(id=proj_id).values()
    for ins_pro in givpro:
        lst_screenshot = []
        if ins_pro['json_screenshot']:
            for temp in ins_pro['json_screenshot']:
                lst_screenshot.append(settings.HOSTNAME + temp)
            ins_pro['json_screenshot'] = lst_screenshot
    #import pdb;pdb.set_trace()
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    if TeamLeadweeklytask.objects.filter(id=proj_id,submited=''):
        return render(request, 'TLtasksubmit2.html',{'pro':givpro,'mem':mem})
    else:
        return render(request, 'TLtasksubmit2.html', {'pro': givpro,'mem':mem})
def tlgiveprojects(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    department1=regdetails.objects.values('department').filter(department='Software').filter(
        branch=usernametl2).distinct()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context={'departments':department1,'mem':mem}
    return render(request,'TLgiveprojects.html',context)
def tlloadhrprodesi(request):
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    desi_id = request.GET.get('desi_id')
    desi = regdetails.objects.filter(department=desi_id).values('designation').filter(~Q(designation='TL')).filter(branch=usernametl2).distinct()
    return render(request, 'TLhrprodesi.html', {'desi': desi})
def tlloadhrprogive(request):
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(designation=desi_id).all().filter(department=dept_id).filter(branch=usernametl2).all()
    return render(request, 'TLhrprogive.html', {'names': names})
def tlloadhrproemp(request):
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    eid = request.GET.get('emp_id')
    emails = regdetails.objects.filter(id=eid).filter(branch=usernametl2)
    data = emails[0].email + "," + emails[0].mobile+","+emails[0].name+","+emails[0].branch
    #data = json.dumps({"email": emails[0].email, "mobile": emails[0].mobile})
    return HttpResponse(data)
def tlhrprojectsuccess(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl = "dummy"
    member = hrprojectsgive(department=request.POST['department'], designation=request.POST['designation'],
                          employee=request.POST['employee'],platform=request.POST['platform'],
                          title=request.POST['title'],email=request.POST['email'],phone=request.POST['phone'], date=datetime.now(),
                          duedate=request.POST['duedate'],description=request.POST['description'],branch=request.POST['branch'],
                          assignedBy=usernametl,name=usernametl1)
    member.save()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'mem':mem}
    return render(request,'TLprojects2success.html',context)
def tlviewprojects(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl1 = "dummy"
    names = hrprojectsgive.objects.filter(assignedBy='TL').filter(branch=usernametl2).filter(name=usernametl1).all()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context={'names':names,'mem':mem}
    return render(request,'TLviewprojects.html',context)
def tltrviewproject2(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl1 = "dummy"
    emp_id=request.GET.get('empid')
    task=hrprojectsgive.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    form = TLTaskFileForm()
    img = hrprojectsgive.objects.all()
    if hrprojectsgive.objects.filter(id=emp_id,submited=''):
        return render(request, 'TLproextend.html', {'names': task,"img": img, "form": form,'mem':mem})
    else:
        return render(request, 'TLprosubmit.html', {'tasks1': task,'mem':mem})
def tlproextend(request):
    return render(request,'TLproextend.html')
def tlprosubmit(request):
    return render(request,'TLprosubmit.html')
def tlviewprosubmit(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl1 = "dummy"
    emp_id = request.GET.get('empid')
    intern1=hrprojectsgive.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'names': intern1,'mem':mem}
    return render(request,'TLviewprosubmit.html',context)
def tlattendance(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    edepartments = regdetails.objects.values('department').filter(department='Software').filter(~Q(designation='TL')).filter(branch=usernametl2).distinct()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'edepartments': edepartments,'mem':mem}
    return render(request,'TLtrattendance.html',context)
def tlattend(request):
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).filter(~Q(designation='TL')).filter(trainer=usernametl1).filter(branch=usernametl2).all().values('name').distinct()
    return render(request, 'TLtrput.html', {'Desig': Desig})
def tlputattendancesearch(request):
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).all().filter(name=desig_id).all()
    return render(request, 'TLputattendancesearch.html', {'names': names})
def tlempattend(request):
    member = employeeattendance(department=request.POST['department'],designation=request.POST['designation'], date=request.POST['date'],
                               employee=request.POST['employee'], status=request.POST['status'],
                               branch=request.POST['branch'],login=request.POST['login'],logout=request.POST['logout'])
    member.save()
    return render(request,'TLtrattendance.html')
def tlviewattendance(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    edepartments = employeeattendance.objects.values('department').filter(department='Software').filter(~Q(designation='TL')).filter(branch=usernametl2).distinct()
    mem=regdetails.objects.filter(designation=usernametl) .filter(name=usernametl1)
    context = {'edepartments': edepartments,'mem':mem}
    return render(request,'TLtrviewattendance.html',context)
def tlemployeedesi(request):
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    dept_id = request.GET.get('dept_id')
    Desig = employeeattendance.objects.filter(department=dept_id).values('employee').filter(branch=usernametl2).filter(department='Software').filter(~Q(designation='TL')).distinct()
    return render(request, 'TLemployeedesi.html', {'Desig': Desig})
def tlviewattendance1(request):
    dept_id = request.GET.get('regdetails')
    desig_id = request.GET.get('regdetails1')
    date1_id = request.GET.get('fromdate')
    date2_id = request.GET.get('todate')
    names = employeeattendance.objects.filter(date__range=(date1_id,date2_id)).filter(department=dept_id).all().filter(employee=desig_id).all()
    template='TLtrviewattendance1.html',
    return render(request, template, {'names': names})
    #return render(request,'TLtrviewattendance1.html')
def tltrperformance(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    edepartments = regdetails.objects.values('department').filter(department='Software').filter(~Q(designation='TL')).filter(branch=usernametl2).distinct()
    mem = regdetails.objects.filter(designation=usernametl).filter(name=usernametl1)
    context = {'edepartments': edepartments,'mem':mem}
    return render(request,'TLtrperformance.html',context)
def tltrper(request):
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    else:
        usernametl2 = "dummy"
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).filter(~Q(designation='TL')).filter(branch=usernametl2).all().values('name').distinct()
    return render(request, 'TLtrper.html', {'Desig': Desig})
def tltrperformancesearch(request):
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = regdetails.objects.filter(department=dept_id).all().filter(name=desig_id).all()
    return render(request, 'TLtrperformancesearch.html', {'names': names})
def tltrrperinsert(request):
    if request.method == 'POST':
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        team.empPunctuality = request.POST.get("punctuality")
        team.empPerformance = request.POST.get("perfo")
        team.emptimelycompletion = request.POST.get("tim")
        team.empextrawork = request.POST.get("extra")
        team.empCreativity = request.POST.get("creativity")
        team.empattendance = request.POST.get("attend")
        team.save()
    return render(request,'TLtrperformance.html')
def tlperformance(request):
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl4'):
        usernametl4 = request.session['usernametl4']
    else:
        usernametl4 = "dummy"

    names = PrTasktoTL.objects.filter(branch=usernametl2).filter(assignedto_id=usernametl4,designation=usernametl)._values('project_id').distinct()
    mem = regdetails.objects.filter(designation=usernametl).filter(id=usernametl4)
    context={'name':names,'mem':mem}
    return render(request,'TLProjects.html',context)


def TLProjectTasks(request):
    emp_id = request.GET.get('prid')
    # import pdb;
    # pdb.set_trace()
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl4'):
        usernametl4 = request.session['usernametl4']
    else:
        usernametl4 = "dummy"

    mem = regdetails.objects.filter(designation=usernametl).filter(id=usernametl4)

    pro = Project.objects.filter(id=emp_id, branch=usernametl2)

    # for Teststatus===========

    #import pdb;
    #pdb.set_trace()
    test = Testing.objects.filter(project_id=emp_id, branch=usernametl2).all()
    testmap = {}
    for i in test:
        id = i.reportid.task_id
        print(id)
        if testmap.get(id) is None:
            list = []
            list.append(i)
            testmap[id] = list
        else:
            list = testmap.get(id)
            list.append(i)
    # for Extension Request===========
    extensionrqst = PrTasktoTL.objects.filter(project_id=emp_id, branch=usernametl2).all()
    Extensionmap = {}
    for i in extensionrqst:
        id = i.id
        if Extensionmap.get(id) is None:
            list = []
            list.append(i)
            Extensionmap[id] = list
        else:
            list = Extensionmap.get(id)
            list.append(i)

    emp1 = PrTasktoTL.objects.filter(assignedto_id=usernametl4, project_id=emp_id, branch=usernametl2)
    repo = Report.objects.filter(project_id=emp_id, branch=usernametl2, reportedby_id=usernametl4).all()
    map = {}

    for i in emp1:
        map[i.id] = None
    for i in repo:
        id = i.task_id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)
    # task1=PrTasktoTL.objects.filter(assignedby=usernameMid,project__id=emp_id,branch=usernameM2,)

    return render(request, 'TLProjectTasks.html',
                  {'mem': mem, 'emp': emp1, 'proj': pro, 'rep': map, 'testm': testmap, 'extension': Extensionmap})

def TLprojectsubtasksAddReport(request):
    #import pdb;
    #pdb.set_trace()
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl4'):
        usernametl4 = request.session['usernametl4']
    else:
        usernametl4 = "dummy"
    #mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    if request.method == "POST":
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['taskattachfile']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                '''str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)'''
                
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))                
                
        duedate1 = request.POST.get('duedate')
        member = Report(reportto_id=request.POST['assignedto'],reportedby_id=usernametl4,
                            project_id=request.POST['projectid'], task_id=request.POST['selected'],date=datetime.now(),#date=request.POST['wdate'],
                            workdone=request.POST['work'],duedate=datetime.strptime(duedate1, '%b. %d, %Y'),
                             branch=usernametl2,testerid_id=request.POST['testerid'],json_attachfile=lst_file)
        member.save()
        base_url = reverse('TLProjectTasks')
        query_string = urlencode({'prid': member.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

def TLMyprojectsubtaskProjectstatus(request):
    if request.method == 'POST':
        team = PrTasktoTL.objects.get(id=request.POST.get('team_id'))
        team.prostatus = request.POST.get("status")
        team.progress = request.POST.get("progre")
        team.save()
        base_url = reverse('TLProjectTasks')
        query_string = urlencode({'prid': team.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

def TLprojectsubtaskextensionrqst(request):
    if request.method == 'POST':
        team = PrTasktoTL.objects.get(id=request.POST.get('team_id'))
        team.reqdays = request.POST.get("days")
        team.reason = request.POST.get("reason")
        team.save()
        base_url = reverse('TLProjectTasks')
        query_string = urlencode({'prid': team.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

def TLProjectTaskSubtask(request):
    emp_id = request.GET.get('tid')
    # import pdb;
    # pdb.set_trace()
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl4'):
        usernametl4 = request.session['usernametl4']
    else:
        usernametl4 = "dummy"
    tsk=emp_id
    mem = regdetails.objects.filter(designation=usernametl).filter(id=usernametl4)
    subtas = PrTasktoDR.objects.filter(task_id=emp_id, branch=usernametl2,assignedby_id=usernametl4)
    repo = Report.objects.filter(task_id=emp_id, branch=usernametl2,reportto_id=usernametl4).all()
    map = {}

    for i in repo:
        id = i.subtask_id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)

    # for Teststatus===========
    test = Testing.objects.filter(task_id=emp_id, branch=usernametl2).all()
    testmap = {}
    for i in test:
        id = i.reportid.subtask_id
        if testmap.get(id) is None:
            list = []
            list.append(i)
            testmap[id] = list
        else:
            list = testmap.get(id)
            list.append(i)

    # for Extension Request===========
    extensionrqst = PrTasktoDR.objects.filter(task_id=emp_id, branch=usernametl2).all()
    Extensionmap = {}
    for i in extensionrqst:
        id = i.id
        if Extensionmap.get(id) is None:
            list = []
            list.append(i)
            Extensionmap[id] = list
        else:
            list = Extensionmap.get(id)
            list.append(i)

    emp1 = PrTasktoDR.objects.filter(assignedby_id=usernametl4, task_id=emp_id, branch=usernametl2)
    imap = {}
    for i in emp1:
        id = i.id
        if imap.get(id) is None:
            list = []
            list.append(i)
            imap[id] = list
        else:
            list = imap.get(id)
            list.append(i)
    # task1=PrTasktoTL.objects.filter(assignedby=usernameMid,project__id=emp_id,branch=usernameM2,)

    return render(request, 'TLProjectTaskSubtask.html',
                  {'mem': mem, 'emp': emp1, 'subtask1': subtas, 'rep': map, 'testm': testmap, 'extension': Extensionmap,'imap1':imap,'task':tsk})

def TLmyprojectsubtaskAdd(request):
    emp_id = request.GET.get('tskid')

    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl4'):
        usernametl4 = request.session['usernametl4']
    else:
        usernametl4 = "dummy"


    #proj = Project.objects.filter(id=emp_id, branch=usernametl2)
    emp = PrTasktoTL.objects.filter(assignedto_id=usernametl4,id=emp_id,branch=usernametl2).all()
    map = {}

    for i in emp:
        id = i.id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)

    department1 = regdetails.objects.values('department').distinct().filter(branch=usernametl2,)
    mem = regdetails.objects.filter(designation=usernametl).filter(id=usernametl4)
    tester = regdetails.objects.filter(branch=usernametl2).filter(designation='Tester')
    context = {'departments': department1,'mem':mem,'emp1':emp,'tester':tester,'map1':map}
    return render(request, 'TLmyprojectsubtaskAdd.html', context)

def TLmyprojectSubtaskAddfun(request):
    #import pdb;
    #pdb.set_trace()
    if request.session.has_key('usernametl'):
        usernametl = request.session['usernametl']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl4'):
        usernametl4 = request.session['usernametl4']
    else:
        usernametl4 = "dummy"
    #mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    if request.method == "POST":
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['taskattachfile']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                '''str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)'''
                
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                
        member = PrTasktoDR(assignedto_id=request.POST['assignedto'],task_id=request.POST['taskid'],
                            project_id=request.POST['prid'], subtaskname=request.POST['task'],
                            startdate=datetime.now(), duedate=request.POST['duedate'],
                            subdescri=request.POST['descri'], branch=request.POST['branch'], assignedby_id=usernametl4,
                            testerid_id=request.POST['tester'],json_taskattachfile=lst_file)
        member.save()
        base_url = reverse('TLProjectTaskSubtask')
        query_string = urlencode({'tid': member.task_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

def TLDropdownemp(request):
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    if request.session.has_key('usernamedr4'):
        usernamedr4 = request.session['usernamedr4']
    else:
        usernamedr2 = "dummy"
    desig_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(designation=desig_id).filter(department=dept_id).all().filter(branch=usernamedr2).filter(trainer=usernamedr4)
    return render(request, 'MANdropdown.html', {'names': names})
def Tlsplitprojectsubtaskextensionstatus(request):
    if request.method == 'POST':
        team = PrTasktoDR.objects.get(id=request.POST.get('team_id'))
        team.status = request.POST.get("extstatus")

        team.save()
        base_url = reverse('TLProjectTaskSubtask')
        query_string = urlencode({'tid': team.task_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
'''def TLMyprojectsubtaskProjectstatus(request):
    if request.method == 'POST':
        team = PrTasktoDR.objects.get(id=request.POST.get('team_id'))
        team.prostatus = request.POST.get("status")
        team.progress = request.POST.get("progre")
        team.save()
        base_url = reverse('TLProjectTaskSubtask')
        query_string = urlencode({'tid': team.task_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)'''
def TLDropdownemp(request):
    if request.session.has_key('usernametl2'):
        usernametl2 = request.session['usernametl2']
    if request.session.has_key('usernametl1'):
        usernametl1 = request.session['usernametl1']
    else:
        usernametl1 = "dummy"
    desig_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = regdetails.objects.filter(designation=desig_id).filter(department=dept_id).all().filter(branch=usernametl2,trainer=usernametl1)
    return render(request, 'TLdropdown.html', {'names': names})

def TLloaddesi(request):
    desi_id = request.GET.get('desi_id')
    desi = regdetails.objects.filter(department=desi_id).values('designation').distinct()
    return render(request, 'TLdesi.html', {'desi': desi})

def TLloadmantaskemp(request):
    eid = request.GET.get('emp_id')
    emails = regdetails.objects.filter(id=eid)
    data = emails[0].email + "," + emails[0].mobile + "," + emails[0].name + "," + emails[0].branch
    # data = json.dumps({"email": emails[0].email, "mobile": emails[0].mobile})
    return HttpResponse(data)        
#----------------------------DEVELOPER----------------
def dr(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    #mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    #return render(request,'DR.html',{'mem':mem})
    labels = []
    data = []
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    queryset = regdetails.objects.filter(designation=usernamedr)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'DR.html', {
        'mem':mem,
        'labels': labels,
        'data': data,
    })

def drmypropie_chart(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr = "dummy"
    labels = []
    data = []
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    queryset = regdetails.objects.filter(designation=usernamedr)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'DRmyprofilepiechart.html', {
        'mem':mem,
        'labels': labels,
        'data': data,
    })
def dr1(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr = "dummy"
    labels = []
    data = []
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    queryset = regdetails.objects.filter(designation=usernamedr)
    emp_id = request.GET.get('empid')
    for e1 in queryset.filter(id=emp_id):
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'DR1.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })
def drtopics(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    if request.session.has_key('usernamedr4'):
        usernamedr4 = request.session['usernamedr4']
    else:
        usernamedr2 = "dummy"
    names = syllabus.objects.filter(branch=usernamedr2).filter(trainer=usernamedr4)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context={'names':names,'mem':mem}
    return render(request,'DRtopics.html',context)
def drtoptcs2(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    emp_id=request.GET.get('empid')
    task=syllabus.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'names':task,'mem':mem}
    return render(request,'DRtoptcs2.html',context)
def drtopic3add(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr3'):
        usernamedr3 = request.session['usernamedr3']
    else:
        usernamedr3 = "dummy"
    if request.method == 'POST':
        team = syllabus.objects.get(id=request.POST.get('team_id'))
        team.name= usernamedr1
        team.department= usernamedr3
        team.designation= usernamedr
        team.reportstatus = request.POST.get("reportstatus")
        team.description = request.POST.get("description")
        team.save()
        return render(request,'DRreviewsuccess.html')
def drreviewsuccess(request):
    return render(request,'DRreviewsuccess.html')
def drweeklytask(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr2 = "dummy"
    names = TeamLeadweeklytask.objects.filter(name=usernamedr1).filter(branch=usernamedr2).all()
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context={'names':names,'mem':mem}
    return render(request,'DRweeklytask.html',context)
def drmanagerattendanceadd(request):
    if request.method == 'POST':
        manager1 = syllabus.objects.get(id=request.POST.get('team_id'))
        manager = syllabus(reportstatus=request.POST['reportstatus'],
                            description=request.POST['description'],
                            )
        manager.save()
        context = {'names':manager1}
        return render(request,'adminattendance2.html',context)
def drweeklytask2(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    else:
        usernamedr1 = "dummy"
    emp_id=request.GET.get('empid')
    task=TeamLeadweeklytask.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    form = DRTaskFileForm()
    img = TeamLeadweeklytask.objects.all()
    if TeamLeadweeklytask.objects.filter(id=emp_id,submited=''):
        return render(request, 'DRweeklytask2.html', {'names': task,"img": img, "form": form,'mem':mem})
    else:
        return render(request, 'DRweeklytask3.html', {'tasks1': task,'mem':mem})
'''def drweeklytask2add(request):
    if request.method == "POST":

        team = TeamLeadweeklytask.objects.get(id=request.POST.get('team_id'))
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['screenshot']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                #str_img = fs.save(str(img_emp), img_emp)
                #str_img_path = fs.url(str_img)
                #lst_file.append(str_img_path)
                
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                
        team.submited = 'submited'
        form = DRTaskFileForm(data=request.POST, files=request.FILES, instance=team)
        # form.screenshot = request.FILES.getlist('screenshot')
        form.save()
        # import pdb;pdb.set_trace()
        TeamLeadweeklytask.objects.filter(id=int(request.POST.get('team_id'))).update(json_screenshot=lst_file)
        return render(request, 'DRtasksuccess.html', {'teams': team})
    return render(request, 'DRweeklytask2.html')'''
def drweeklytask2add(request):
    if request.method == "POST":

        team = TeamLeadweeklytask.objects.get(id=request.POST.get('team_id'))
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['screenshot']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                '''str_img = fs.save(img_emp.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,/<>?\|`~-=_+"}, img_emp))
                str_img_path = fs.url(translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,/<>?\|`~-=_+"},str_img))
                lst_file.append('/media/'+translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,/<>?\|`~-=_+"}, str(img_emp)))'''
                
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                
        team.submited = 'submited'
        form = DRTaskFileForm(data=request.POST, files=request.FILES, instance=team)
        # form.screenshot = request.FILES.getlist('screenshot')
        form.save()
        # import pdb;pdb.set_trace()
        TeamLeadweeklytask.objects.filter(id=int(request.POST.get('team_id'))).update(json_screenshot=lst_file)
        return render(request, 'DRtasksuccess.html', {'teams': team})
    return render(request, 'DRweeklytask2.html')    
def drtasksuccess(request):
    return render(request,'DRtasksuccess.html')
def drapplyleave(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    else:
        usernamedr = "dummy"
    mem = regdetails.objects.filter(designation=usernamedr).filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRapplyleave.html',context)
def drapplyleave2(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    else:
        usernamedr = "dummy"
    mem = regdetails.objects.filter(designation=usernamedr).filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRapplyeleave2.html',context)
def drapplyleave3(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr = "dummy"
    member= leavereq(assignedBy=usernamedr1,leavefrom=request.POST['leavefrom'],leaveto=request.POST['leaveto'],reason=request.POST['reason'],
                     department=usernamedr,branch=usernamedr2)
    member.save()
    return render(request,'DRapplyleave.html')
def drleavereq(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr2 = "dummy"
    names = leavereq.objects.filter(branch=usernamedr2).filter(assignedBy=usernamedr1)#all()
    mem = regdetails.objects.filter(designation=usernamedr).filter(name=usernamedr1)
    context={'names':names,'mem':mem}
    return render(request,'DRreqleaves.html',context)
def drreportissues(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRreportissues.html',context)
def drreportedissue1(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr2 = "dummy"
    names = hrreport.objects.filter(reportedby=usernamedr1).filter(branch=usernamedr2).all
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context={'names':names,'mem':mem}
    return render(request,'DRreportedissue1.html',context)
def drreportedissue2(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    emp_id=request.GET.get('empid')
    empid=hrreport.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    return render(request, 'DRreportedissue2.html',{'emp':empid,'mem':mem})
    #return render(request,'DRreportedissue2.html')
def drreport1(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRreport1.html',context)
def drreportsuccess(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernametl'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr1 = "dummy"
    member= hrreport(issue=request.POST['issue'],date=datetime.now(),reportedby=usernamedr1,
                     designation=usernamedr,branch=usernamedr2)
    member.save()
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRreportsuccess.html',context)
'''def drprojects(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr2 = "dummy"
    names = hrprojectsgive.objects.filter(employee=usernamedr1).filter(branch=usernamedr2).all()
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context={'names':names,'mem':mem}
    return render(request,'DRprojects.html',context)'''
def drprojects2(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']

    proj_id=request.GET.get('prid')
    givpro=hrprojectsgive.objects.filter(id=proj_id).values()

    for ins_pro in givpro:
        lst_screenshot = []
        if ins_pro['json_screenshot']:
            for temp in ins_pro['json_screenshot']:
                lst_screenshot.append(settings.HOSTNAME + temp)
            ins_pro['json_screenshot'] = lst_screenshot
    #import pdb;pdb.set_trace()
    mem = regdetails.objects.filter(designation=usernamedr).filter(name=usernamedr1)
    if hrprojectsgive.objects.filter(id=proj_id,testerok='Tested ok'):
        return render(request, 'DRassignedprojects2.html',{'pro':givpro,'mem':mem})
    if hrprojectsgive.objects.filter(id=proj_id,submited=''):
        return render(request, 'DRprojects2.html',{'pro':givpro,'mem':mem})
    else:
        return render(request, 'DRprojects3.html', {'pro': givpro,'mem':mem})


    '''emp_id=request.GET.get('empid')
    task=hrprojectsgive.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    form = DRTaskFileForm()
    img = hrprojectsgive.objects.all()
    if hrprojectsgive.objects.filter(id=emp_id,submited=''):
        return render(request, 'DRprojects2.html', {'names': task,"img": img, "form": form,'mem':mem})
    else:
        return render(request, 'DRprojects3.html', {'tasks1': task,'mem':mem})'''
    #return render(request,'DRprojects2.html')
def drproject2add(request):
    '''if request.method == "POST":

        team = hrprojectsgive.objects.get(id=request.POST.get('team_id'))
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['screenshot']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)
        team.submited='submitted'
        form = DRProjectFileForm(data=request.POST, files=request.FILES, instance=team)
        #form.screenshot = request.FILES.getlist('screenshot')
        form.save()
        #import pdb;pdb.set_trace()
        hrprojectsgive.objects.filter(id=int(request.POST.get('team_id'))).update(json_screenshot=lst_file)'''
    if request.method == "POST":

        team = hrprojectsgive.objects.get(id=request.POST.get('team_id'))
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['screenshot']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)
        team.submited='submitted'
        #team.nameid= request.POST.get("usernametl4")
        form = DRProjectFileForm(data=request.POST, files=request.FILES, instance=team)
        #form.screenshot = request.FILES.getlist('screenshot')
        form.save()
        #import pdb;pdb.set_trace()
        hrprojectsgive.objects.filter(id=int(request.POST.get('team_id'))).update(json_screenshot=lst_file)
        return render(request, 'DRProjectsuccess.html', {'teams': team})
    return render(request, 'DRprojects3.html')
def drprojects2extend(request):

    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    emp_id = request.GET.get('empid')
    edepartments1 = hrprojectsgive.objects.filter(id=emp_id)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'mem':mem,'edepartments1':edepartments1}
    return render(request,'DRprojects2extend.html',context)
def drprojects2extendadd(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    if request.session.has_key('usernamedr3'):
        usernamedr3 = request.session['usernamedr3']
    else:
        usernamedr3 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedr).filter(name=usernamedr1)
    context = {'mem': mem}
    if request.method == 'POST':
        team = hrprojectsgive.objects.get(id=request.POST.get('team_id'))
        team.rqstdays = request.POST.get("rqstdays")
        team.reason = request.POST.get("reason")
        team.save()
    return render(request,'DRprojrct2extendsuccess.html',context)
    '''member = hrprojectsgive(rqstdays=request.POST['rqstdays'],reason=request.POST['reason'],employee=usernamedr1,branch=usernamedr2,
                      department=usernamedr3)
    member.save()

    return render(request,'DRprojrct2extendsuccess.html',context)'''
def drprojrct2extendsuccess(request):
    return render(request,'DRprojrct2extendsuccess.html')
def drprojects3(request):
    return render(request,'DRprojects3.html')
def drattendance(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRattendance.html',context)
def drattendncemy(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr1 = "dummy"
    print('hai')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    #print('h')
    names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).all().filter(employee=usernamedr1).filter(branch=usernamedr2)
    print(names.values('status','date','login','logout'))
    return render(request, 'TLatt.html', {'names': names})
def drpayments(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRpayments.html',context)
def drpaymenthistory(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr1 = "dummy"
    edepartments = drrpayment.objects.filter(name=usernamedr1).filter(~Q(submited=''))
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'names': edepartments,'mem':mem}
    return render(request,'DRpaymenthistory.html',context)
def drpaymentnotifications(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr1 = "dummy"
    edepartments = drrpayment.objects.filter(name=usernamedr1).filter(submited='')#.filter(branch=usernamedr2)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'names': edepartments,'mem':mem}
    return render(request,'DRpaymentnotifications.html',context)
def drpaymentnotifications2(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    else:
        usernamedr1 = "dummy"
    emp_id = request.GET.get('empid')
    edepartments1 = drrpayment.objects.filter(id=emp_id)
    #emp_idd = request.GET.get('empidd')
    #edepartments2 = drrpayment.objects.filter(id=emp_idd)
    edepartments = drrpayment.objects.filter(name=usernamedr1).filter(id=emp_id)#.filter(branch=usernamedr2)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'names':edepartments,'name':edepartments1,'mem':mem}
    return render(request,'DRpaymentnotifications2.html',context)
def drpaymentnotifications2add(request):
    if request.method == "POST":
        team = drrpayment.objects.get(id=request.POST.get('team_id'))
        team.submited = 'submitted'
        form = DRpaymentForm(data=request.POST, files=request.FILES, instance=team)
        form.save()
        return render(request, 'DRpayments.html', {'teams': team})
    return render(request, 'DRpaymentnotifications2.html')
def d(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    else:
        usernamedr1 = "dummy"
    edepartments = drrpayment.objects.filter(name=usernamedr1)#filter(name=usernamedr1)#.filter(branch=usernamedr2)
    context = {'names': edepartments}
    return render(request,'d.html',context)
def d1(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    else:
        usernamedr1 = "dummy"
    #dept_id = request.GET.get('dept_id')
    emp_id = request.GET.get('empid')
    names=drrpayment.objects.filter(id=emp_id).filter(name=usernamedr1)
    #names = drrpayment.objects.filter(name=usernamedr1)#filter(id=dept_id).all()#.filter(department="Software")
    return render(request, 'd1.html', {'names': names})
def drsalaryslip(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    else:
        usernamedr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRsalaryslip.html',context)
def drPaymentsViewDetailButton(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    context = {'mem':mem}
    return render(request,'DRPaymentsViewDetailButton.html',context)
def drpayments33(request):
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    else:
        usernamedr1 = "dummy"
    pay=request.GET.get('birthday')
    #pay1=acntspayslip.objects.filter(dateef=pay).filter(ename=usernamehr1)
    pay1=acntspayslip.objects.filter(dateef=pay).filter(ename=usernamedr1)
    mem=regdetails.objects.filter(designation=usernamedr) .filter(name=usernamedr1)
    return render(request,'DRpayments3.html',{'pays':pay1,'mem':mem})
def drprojects(request):
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    if request.session.has_key('usernamedr5'):
        usernamedr5 = request.session['usernamedr5']
    else:
        usernamedr5 = "dummy"

    mem = regdetails.objects.filter(designation=usernamedr).filter(id=usernamedr5)
    tasks=PrTasktoDR.objects.filter(assignedto=usernamedr5,branch=usernamedr2)._values('project_id').distinct()
    #names = hrprojectsgive.objects.filter(employee=usernamedr1).filter(branch=usernamedr2).all()

    context={'task1':tasks,'mem':mem}
    return render(request,'DRprojects.html',context)

def DRprojectsubtasks(request):
    emp_id = request.GET.get('prid')
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    if request.session.has_key('usernamedr5'):
        usernamedr5 = request.session['usernamedr5']
    else:
        usernamedr5 = "dummy"
    #import pdb;
    #pdb.set_trace()


        # for Teststatus===========
    test = Testing.objects.filter(project_id=emp_id, branch=usernamedr2).all()
    testmap = {}
    for i in test:
        id = i.reportid.subtask_id
        if testmap.get(id) is None:
            list = []
            list.append(i)
            testmap[id] = list
        else:
            list = testmap.get(id)
            list.append(i)

        # for Extension Request===========
    extensionrqst = PrTasktoDR.objects.filter(project_id=emp_id, branch=usernamedr2).all()
    Extensionmap = {}
    for i in extensionrqst:
        id = i.id
        if Extensionmap.get(id) is None:
            list = []
            list.append(i)
            Extensionmap[id] = list
        else:
            list = Extensionmap.get(id)
            list.append(i)

    #personal = employee.objects.filter(id=usernamedevid)
    tas = PrTasktoDR.objects.filter(project_id=emp_id,assignedto_id=usernamedr5 ,branch=usernamedr2)
    repo = Report.objects.filter(project_id=emp_id, branch=usernamedr2, reportedby_id=usernamedr5).all()
    map = {}
    for i in tas:
        map[i.id] = None

    for i in repo:
        id = i.subtask_id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)


    subtas = PrTasktoDR.objects.filter(project_id=emp_id, assignedto_id=usernamedr5, branch=usernamedr2)
    subtasmap = {}
    for i in subtas:
        id = i.id
        if subtasmap.get(id) is None:
            list = []
            list.append(i)
            subtasmap[id] = list
        else:
            list = subtasmap.get(id)
            list.append(i)

    return render(request,'DRprojectsubtasks.html',{'tas1':tas,'rep':map,'test':testmap,'extndmap':Extensionmap,'subtas1':subtasmap})
def DRprojectsubtasksAddStatus(request):
    if request.method == 'POST':
        team = PrTasktoDR.objects.get(id=request.POST.get('team_id'))
        team.prostatus = request.POST.get("status")
        team.progress = request.POST.get("progre")
        team.save()
        base_url = reverse('DRprojectsubtasks')
        query_string = urlencode({'prid': team.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
def DRprojectsubtaskextensionrqst(request):
    if request.method == 'POST':
        team = PrTasktoDR.objects.get(id=request.POST.get('team_id'))
        team.reqdays = request.POST.get("days")
        team.reason = request.POST.get("reason")
        team.save()
        base_url = reverse('DRprojectsubtasks')
        query_string = urlencode({'prid': team.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

def DRprojectsubtasksAddReport(request):
    #import pdb;
    #pdb.set_trace()
    if request.session.has_key('usernamedr'):
        usernamedr = request.session['usernamedr']
    if request.session.has_key('usernamedr1'):
        usernamedr1 = request.session['usernamedr1']
    if request.session.has_key('usernamedr2'):
        usernamedr2 = request.session['usernamedr2']
    if request.session.has_key('usernamedr5'):
        usernamedr5 = request.session['usernamedr5']
    else:
        usernamedr5 = "dummy"
    #mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    if request.method == "POST":
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['taskattachfile']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                '''str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)'''
                
                
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                
        duedate1 = request.POST.get('duedate')
        member = Report(reportto_id=request.POST['assignedto'],reportedby_id=usernamedr5,
                            project_id=request.POST['projectid'], task_id=request.POST['taskid'],date=datetime.now(),#date=request.POST['wdate'],
                            workdone=request.POST['work'],
                            subtask_id=request.POST['selected'],duedate=datetime.strptime(duedate1, '%b. %d, %Y'),
                            branch=usernamedr2,testerid_id=request.POST['testerid'],json_attachfile=lst_file)
        member.save()
        base_url = reverse('DRprojectsubtasks')
        query_string = urlencode({'prid': member.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
#-----------------------------TS-------------------------------------------------------
def ts(request):
    if request.session.has_key('usernamets1'):
        usernamets1 = request.session['usernamets1']
    if request.session.has_key('usernamets'):
        usernamets = request.session['usernamets']
    else:
        usernamets1 = "dummy"
    mem=regdetails.objects.filter(designation=usernamets) .filter(name=usernamets1)
    return render(request,'TS.html',{'mem':mem})
def tsproject(request):
    if request.session.has_key('usernamets1'):
        usernamets1 = request.session['usernamets1']
    if request.session.has_key('usernamets4'):
        usernamets4 = request.session['usernamets4']
    if request.session.has_key('usernamets'):
        usernamets = request.session['usernamets']
    if request.session.has_key('usernamets2'):
        usernamets2 = request.session['usernamets2']
    else:
        usernamets2 = "dummy"
    name = Report.objects.filter(testerid_id=usernamets4,branch=usernamets2)._values('project_id').distinct()
    mem = regdetails.objects.filter(designation=usernamets).filter(name=usernamets1)
    context = {'names':name,'mem':mem}
    return render(request,'TSMANproject.html',context)
def TSMANmyprojectsubtask(request, request_datetime=None):
    #import pdb;pdb.set_trace()
    if request.session.has_key('usernamets'):
        usernamets = request.session['usernamets']
    if request.session.has_key('usernamets1'):
        usernamets1 = request.session['usernamets1']
    if request.session.has_key('usernamets2'):
        usernamets2 = request.session['usernamets2']
    if request.session.has_key('usernamets4'):
        usernamets4 = request.session['usernamets4']
    else:
        usernamets4 = "dummy"
    mem = regdetails.objects.filter(designation=usernamets,branch=usernamets2).filter(name=usernamets1)
    emp_id = request.GET.get('prid')
    #emp = PrTasktoTL.objects.filter(project_id=emp_id).all
    emp2 = PrTasktoTL.objects.filter(project_id=emp_id,testerid_id=usernamets4,branch=usernamets2).all

    proj=Project.objects.filter(id=emp_id)
    repo = Testing.objects.filter(project_id=emp_id,testerid_id=usernamets4,branch=usernamets2)
    test1 = Testing.objects.filter(project_id=emp_id,testerid_id=usernamets4,branch=usernamets2)#,task_id=emp_id)
    tas = Report.objects.filter(project_id=emp_id, testerid_id=usernamets4, branch=usernamets2)
    #------
    rep = Report.objects.filter(project_id=emp_id,testerid_id=usernamets4,branch=usernamets2)
    barmap = {}
    #import pdb;pdb.set_trace()
    for i in rep:
        id = i.id
        if barmap.get(id) is None:
            list = []
            list.append(i)
            barmap[id] = list
        else:
            list = barmap.get(id)
            list.append(i)

    #------
    map = {}
    diff = 0
    for i in tas:
        map[i.id] = None

        #diff = datetime.now().date()-i.duedate
    for i in repo:
        #====
        '''a = datetime.now().date()
        date1 = i.reportid.duedate
        diff = a - date1
        print(diff)'''
        #====
        id = i.reportid_id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)
    #import pdb; pdb.set_trace()
    # for Test status===========

    test = Report.objects.filter(project_id=emp_id,testerid_id=usernamets4,branch=usernamets2).all()
    testmap = {}
    for i in test:
        id = i.id
        if testmap.get(id) is None:
            list = []
            list.append(i)
            testmap[id] = list
        else:
            list = testmap.get(id)
            list.append(i)

    # for extension status=====
    extensionrqst = PrTasktoTL.objects.filter(project_id=emp_id,testerid_id=usernamets4,branch=usernamets2).all()
    Extensionmap = {}
    for i in extensionrqst:
        id = i.id
        if Extensionmap.get(id) is None:
            list = []
            list.append(i)
            Extensionmap[id] = list
        else:
            list = Extensionmap.get(id)
            list.append(i)

    return render(request, 'TSMANmyprojectsubtaskAdd.html', {'emp2':emp2,'diff':diff,'tas11':tas,'mem': mem, 'emp1': barmap, 'proj': proj, 'rep': map,'testm':testmap,'leave_object':test1,'extension':Extensionmap})
def TSprojectsubtasksAddReport(request):
    if request.session.has_key('usernamets'):
        usernamets = request.session['usernamets']
    if request.session.has_key('usernamets1'):
        usernamets1 = request.session['usernamets1']
    if request.session.has_key('usernamets2'):
        usernamets2 = request.session['usernamets2']
    if request.session.has_key('usernamets4'):
        usernamets4 = request.session['usernamets4']
    else:
        usernamets4 = "dummy"
    #mem = regdetails.objects.filter(designation=usernameM).filter(name=usernameM1)
    if request.method == "POST":
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['attachfile']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                '''str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)'''


                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))

        #rstreport=Report.objects.get(id=int(request.POST['reportid']))
        member = Testing(project_id=request.POST['projectid'], task_id=request.POST['taskid'],#duedate_id=request.POST['duedate_id'],
                            date=datetime.now(),testerdescri=request.POST['work'],testerstatus=request.POST['testerstatus'],
                            reportid_id=request.POST['selected'],subtask_id=request.POST['subtask'],#delay=request.POST['delay'],
                            branch=usernamets2,testerid_id=request.POST['testerid'],json_attachfile=lst_file)
        member.save()
        base_url = reverse('TSMANmyprojectsubtask')
        query_string = urlencode({'prid': member.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
def tsproject2(request):
    # import pdb;pdb.set_trace()
    if request.session.has_key('usernamets1'):
        usernamets1 = request.session['usernamets1']
    if request.session.has_key('usernamets'):
        usernamets = request.session['usernamets']
    else:
        usernamets1 = "dummy"
    proj_id=request.GET.get('prid')
    givpro=hrprojectsgive.objects.filter(id=proj_id).values()

    for ins_pro in givpro:
        lst_screenshot = []
        if ins_pro['json_screenshot']:
            for temp in ins_pro['json_screenshot']:
                lst_screenshot.append(settings.HOSTNAME + temp)
            ins_pro['json_screenshot'] = lst_screenshot
    #import pdb;pdb.set_trace()
    mem = regdetails.objects.filter(designation=usernamets).filter(name=usernamets1)
    '''import datetime
    from_date = datetime.datetime(2019, 10, 21)
    to_date = datetime.datetime(2019, 10, 25)
    result = to_date - from_date
    print(result.days)'''
    leave=hrprojectsgive.objects.all().filter(id=proj_id,tester=usernamets1)
    if hrprojectsgive.objects.filter(id=proj_id,testerok='Tested ok'):
        return render(request, 'TSassignedprojects2.html',{'pro':givpro,'mem':mem,'leave_object':leave})
    if hrprojectsgive.objects.filter(id=proj_id,submited=''):
        return render(request, 'TSassignedprojects1.html',{'pro':givpro,'mem':mem})
    else:
        return render(request, 'TSassignedprojectsSubmitted.html', {'pro': givpro,'mem':mem,'leave_object':leave})

def tsproject2add(request):
    if request.method == "POST":
        team = hrprojectsgive.objects.get(id=request.POST.get('team_id'))
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['testerscreenshot']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)
        team.testerok='Tested ok'
        team.testerdate = datetime.now()
        form = TSProjectFileForm(data=request.POST, files=request.FILES, instance=team)
        #form.screenshot = request.FILES.getlist('screenshot')
        form.save()
        #import pdb;pdb.set_trace()
        hrprojectsgive.objects.filter(id=int(request.POST.get('team_id'))).update(json_testerscreenshot=lst_file)
        return render(request, 'TSprojects2success.html', {'teams': team})
    return render(request, 'TSassignedprojectsSubmitted.html')#, {'tasks1': task,"img": img, "form": form})'''
def tstask(request):
    if request.session.has_key('usernamets1'):
        usernamets1 = request.session['usernamets1']
    if request.session.has_key('usernamets'):
        usernamets = request.session['usernamets']
    if request.session.has_key('usernamets2'):
        usernamets2 = request.session['usernamets2']
    else:
        usernamets2 = "dummy"
    #pro=hrprojectsgive.objects.filter(assignedBy='MANAGER')
    pro=mangivetasks.objects.all().filter(branch=usernamets2).filter(tester=usernamets1)
    mem = regdetails.objects.filter(designation=usernamets).filter(name=usernamets1)
    return render(request, 'TStask.html',{'projects':pro,'mem':mem})
def tstask2(request):
    # import pdb;pdb.set_trace()
    if request.session.has_key('usernamets1'):
        usernamets1 = request.session['usernamets1']
    if request.session.has_key('usernamets'):
        usernamets = request.session['usernamets']
    else:
        usernamets1 = "dummy"
    proj_id=request.GET.get('prid')
    givpro=mangivetasks.objects.filter(id=proj_id).values()

    for ins_pro in givpro:
        lst_screenshot = []
        if ins_pro['json_screenshot']:
            for temp in ins_pro['json_screenshot']:
                lst_screenshot.append(settings.HOSTNAME + temp)
            ins_pro['json_screenshot'] = lst_screenshot
    #import pdb;pdb.set_trace()
    mem = regdetails.objects.filter(designation=usernamets).filter(name=usernamets1)
    if mangivetasks.objects.filter(id=proj_id,testerok='Tested ok'):
        return render(request, 'TSassignedtask2.html',{'pro':givpro,'mem':mem})
    if mangivetasks.objects.filter(id=proj_id,submited=''):
        return render(request, 'TSassignedtask1.html',{'pro':givpro,'mem':mem})
    else:
        return render(request, 'TSassignedtaskSubmitted.html', {'pro': givpro,'mem':mem})
def tstask2add(request):
    if request.method == "POST":
        team = mangivetasks.objects.get(id=request.POST.get('team_id'))
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['testerscreenshot']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                str_img = fs.save(str(img_emp), img_emp)
                str_img_path = fs.url(str_img)
                lst_file.append(str_img_path)
        team.testerok='Tested ok'
        form = TSTaskFileForm(data=request.POST, files=request.FILES, instance=team)
        #form.screenshot = request.FILES.getlist('screenshot')
        form.save()
        #import pdb;pdb.set_trace()
        mangivetasks.objects.filter(id=int(request.POST.get('team_id'))).update(json_testerscreenshot=lst_file)
        return render(request, 'TSprojects2success.html', {'teams': team})
    return render(request, 'TSassignedtaskSubmitted.html')#, {'tasks1': task,"img": img, "form": form})'''


#----------------------------ADMIN-----------------
def adminmyprofile(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    #return render(request, 'hr.html', {'mem': mem})
    #emp_id = request.GET.get('empid')
    #intern1=regdetails.objects.filter(id=emp_id)
    intern1 = regdetails.objects.filter(designation='admin')
    intern2 = Branch.objects.all()
    msg = Branch.objects.all().count()
    a = regdetails.objects.all().count()
    ab = regdetails.objects.filter(department='Software').filter(~Q(designation='TL')).count()
    context = {'myprofile': intern1,'my': intern2,'msg':msg,'a':a,'ab':ab,'mem': mem}
    print(msg)
    print(a)
    print(ab)
    return render(request,'adminmyprofile.html',context)
def adminbranch1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'adminbranch1.html',context)
def adminaddbranch1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'adminaddbranch1.html',context)
def adminbranchadded(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    branch1 = Branch(branch=request.POST['branch'],country=request.POST['country'],
                     state=request.POST['state'], city=request.POST['city'], area=request.POST['area'],
                     pin=request.POST['pin'])
    branch1.save()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'adminbranchadded.html',context)

'''def adminviewbranch1(request):
    return render(request,'viewbranch1admin.html')'''
def adminviewbranch2(request):
    return render(request,'viewbranch2admin.html')


def admininternshipregistration1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'admininternshipregistration1.html',context)
def admininternshipregistration2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    college1 = college.objects.all()
    branch1 = Branch.objects.values('branch',).distinct()
    countrys1 = Branch.objects.values('country',).distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'colleges': college1, 'branches': branch1,'countrys':countrys1,'mem':mem}
    return render(request, 'admininternshipregistration2.html', context)

    #department1 = select.objects.values('country').distinct()
    #context = {'register': department1}
    #return render(request,'registrationdetails1.html',context)

def admininsertcollege(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'admininsertcollege.html',context)
def admindetailsadded1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    college1 = college(collegename=request.POST['collegename'])
    college1.save()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'admindetailsadded.html',context)
def admindetailsadded(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    '''intern = Item(college=request.POST['college'],regno=request.POST['regno'],studname=request.POST['studname'],platform=request.POST['platform'],department=request.POST['department'],startdate=request.POST['startdate'],enddate=request.POST['enddate'],refid=request.POST['refid'],payment=request.POST['payment'],country=request.POST['country'],branch=request.POST['branch'],course=request.POST['course'],email=request.POST['email'])
    intern.save()
    return render(request, 'admindetailsadded.html')'''
    if request.method == "POST":
        college = request.POST.get('college')
        regno = request.POST.get('regno')
        studname = request.POST.get('studname')
        platform = request.POST.get('platform')
        department = request.POST.get('department')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        refid = request.POST.get('refid')
        payment = request.POST.get('payment')
        country = request.POST.get('country')
        branch = request.POST.get('branch')
        course = request.POST.get('course')
        email = request.POST.get('email')
        college1 = Item(college=college, regno=regno, studname=studname, platform=platform, department=department,
                              startdate=startdate, enddate=enddate, refid=refid,
                              payment=payment,country=country,branch=branch,course=course,email=email)

        qr = make(settings.LOCALROOT + studname)
        qr.save(settings.MEDIA_ROOT + "\\" + studname + ".png")
        with open(settings.MEDIA_ROOT + "\\" + studname + ".png", "rb") as reopen:
            djangofile = File(reopen)
            college1.qr = djangofile
            college1.save()
            mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
            context = {'mem':mem}
        #return redirect(reverse('qrshow', args=[name]))
    return render(request, 'admindetailsadded.html',context)
'''def admindetailsadded(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ImageForm()
            img = internship.objects.all()
            #obj=form.instance
            return render(request, "admininternshipregistration1.html",{"img": img, "form": form})
    else:
        form = ImageForm()
        img = internship.objects.all()
        return render(request, "admindetailsadded.html", {"img": img, "form": form})'''



def adminmarketingadm1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'adminmarketingadm1.html',context)
def adminmarketingadmadd(request):
    return render(request,'adminmarketingadm1.html')


'''def adminpromarket1(request):
    countrys1 = branch.objects.values('country',).distinct()
    city1 = branch.objects.values('city',).distinct()
    branch1 = branch.objects.values('branch',).distinct()
    context = {'countrys':countrys1,'citys':city1,'branches':branch1}
    return render(request, 'adminpromarket1.html',context)'''
def promarketadd(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    college2 = proandmarkng(country=request.POST['country'],
                            city=request.POST['city'],
                            brnch=request.POST['brnch'],
                            proname=request.POST['proname'],
                            target=request.POST['target'],
                            status=request.POST['status'],
                            des=request.POST['des'],
                            date=datetime.now())
    college2.save()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'admindetailsadded.html',context)

'''def serviceadmin(request):
    return render(request, 'serviceadmin.html')'''
def serviceadd(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    servc = service(country=request.POST['country'],
                            city=request.POST['city'],
                            brnch=request.POST['brnch'],
                            service=request.POST['service'],
                            payment=request.POST['payment'],
                            des=request.POST['des'],
                            date=datetime.now())
    servc.save()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'admindetailsadded.html',context)

'''def recrutementadmin(request):
    return render(request, 'recrutementadmin.html')'''
def recrutementadd(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    servc = recrutement(country=request.POST['country'],
                            city=request.POST['city'],
                            brnch=request.POST['brnch'],
                            post=request.POST['post'],
                            qualification=request.POST['qualification'],
                            vacancies=request.POST['vacancies'],
                            des=request.POST['des'],
                            date=datetime.now())
    servc.save()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'admindetailsadded.html',context)

def marketingassignedadmin(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    intern1 = proandmarkng.objects.all()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'promark': intern1,'mem':mem}
    return render(request,'marketingassignedadmin.html',context)

def marketingassignedshowadmin(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    #intern1 = proandmarkng.objects.all()
    emp_id = request.GET.get('empid')
    intern1=proandmarkng.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'promark': intern1,'mem':mem}
    return render(request,'marketingassignedshowadmin.html',context)

def adminmarass2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    intern1 = Tlshareddatas.objects.all()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'promark': intern1,'mem':mem}
    return render(request,'adminmarass2.html',context)
def admininternshipregistrationdetails(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    intern1 = Item.objects.all().order_by('-id')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'intern': intern1,'mem':mem}
    return render(request, 'admininternshipregistrationdetails.html',context)

def editinternship(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    college1 = college.objects.all()
    branch1 = Branch.objects.values('branch',).distinct()
    countrys1 = Branch.objects.values('country',).distinct()
    intern=Item.objects.get(id=id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'intern': intern,'colleges': college1, 'branches': branch1,'countrys':countrys1,'mem':mem}
    return render(request, 'editinternship.html', context)
def updatinternship(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    inte = Item.objects.get(id=id)
    inte.college = request.POST['college']
    inte.regno = request.POST['regno']
    inte.studname = request.POST['studname']
    inte.platform = request.POST['platform']
    inte.department = request.POST['department']
    inte.startdate = request.POST['startdate']
    inte.enddate = request.POST['enddate']
    inte.refid = request.POST['refid']
    inte.payment = request.POST['payment']
    inte.country = request.POST['country']
    inte.branch = request.POST['branch']
    inte.course = request.POST['course']
    inte.email = request.POST['email']
    inte.mobile = request.POST['mobile']
    inte.image = request.POST['image']
    inte.idproof = request.POST['idproof']
    inte.save()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'admindetailsadded.html',context)
'''def addpandseedit(request):
    if request.method == "POST":
        form = Imageform(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            form = Imageform()
            img = im.objects.all()
            return render(request, "admininternshipregistration1.html", {"img": img, "form": form})
    else:
        form = Imageform()
        img = im.objects.all()
        return render(request, "admindetailsadded.html", {"img": img, "form": form})'''
def admininternshipview(request,id):
    '''form = ImageForm()
    img = im.objects.all()
    return render(request, "internviewdetails.html", {"intern": img, "form": form})'''
    intern=Item.objects.get(id=id)
    context = {'intern': intern}
    #return render(request, 'internviewdetails.html', context)
    return render(request,'new.html',context)

def updateadmininternshipview(request,id):
    inte = Item.objects.get(id=id)
    inte.name = request.POST['name']
    inte.email = request.POST['email']
    inte.mobile = request.POST['mobile']
    inte.course = request.POST['course']
    inte.platform = request.POST['platform']
    inte.startdate = request.POST['startdate']
    inte.enddate = request.POST['enddate']
    inte.image = request.POST['image']
    inte.idproof = request.POST['idproof']
    inte.save()
    return render(request, 'admindetailsadded.html', )
def deleteinternship(request,id):
    sl = Item.objects.get(id=id)
    sl.delete()
    return render(request, 'admininternshipregistration1.html')


def adminregistration(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    edepartment1=Branch.objects.values('country').distinct()
    br1 = regdetails.objects.values('branch').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'edepartments': edepartment1,'brs':br1,'mem':mem}
    return render(request, 'registrationdetails1.html', context)
    '''department1 = select.objects.values('country').distinct()
    context = {'register': department1}
    return render(request,'registrationdetails1.html',context)'''
def loadadmindesi(request):
    desi_id = request.GET.get('desi_id')
    desi = select.objects.filter(country=desi_id).values('city').distinct()
    return render(request, 'registrationdetails1.html', {'desi': desi})
def loadhremployeess1(request):
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = select.objects.filter(city=desi_id).all().filter(branch=dept_id).all()
    return render(request, 'registrationdetails1.html', {'names': names})

def admintasksandproject1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'tasksandproject1admin.html',context)
def adminassigned1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    #emp_id = request.GET.get('empid')
    intern1 = admingivetask.objects.all()#values('branch').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'give':intern1,'mem':mem}
    return render(request,'adminassigned1.html',context)
'''def admingivetask1(request):
#    intern1 = proandmarkng.objects.all()
    branch1 = branch.objects.all()
    context = {'branches': branch1}#,'promark': intern1 }
    return render(request,'admingivetask1.html',context)'''

def adminregistrationdetails2(request):
    return render(request,'adminregistrationdetails2.html')

def adminviewtrainee(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    edepartments3 = Branch.objects.filter(branch=emp_id)
    print('hai')
    edepartment1=Branch.objects.values('country').distinct()
    edepartment2 = Branch.objects.values('branch').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'brs':edepartment2,'brs1':edepartments3,'mem':mem}
    return render(request, 'admingivetask1.html', context)
def admintraineedesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = Branch.objects.filter(country=dept_id).all().values('city').distinct()
    return render(request, 'admintraineedesi.html', {'Desig': Desig})
def adminloademployeess(request):
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = Branch.objects.filter(city=desi_id).all().filter(country=dept_id).all()
    return render(request, 'adminloademployeess.html', {'names': names})
def admingivetask2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    give = admingivetask.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    if admingivetask.objects.filter(id=emp_id,submited=''):
        return render(request, 'admingivetask3.html', {'give': give,'mem':mem})
    else:
        return render(request, 'admingivetask4.html', {'give': give,'mem':mem})

    '''emp_id = request.GET.get('empid')
    give = admingivetask.objects.filter(branch=emp_id)
    context = {'give': give}
    return render(request, 'admingivetask3.html',context)'''

def admintaskmanager(request):
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    branch_id = request.GET.get('branch_id')
    names = Branch.objects.filter(country=dept_id).all().filter(city=desig_id).all().filter(branch=branch_id).all()
    return render(request, 'admingivetask2.html', {'names': names})
def givtaskadminadd(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    give = admingivetask.objects.all()
    context = {'give': give}
    if request.method == "POST":
        form = FileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            form = FileForm()
            attach = admingivetask.objects.all()
            mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
            return render(request, "admindetailsadded.html", {"img": attach, "form": form,'mem':mem})
    else:
        form = FileForm()
        attach = admingivetask.objects.all()
        return render(request, "admindetailsadded.html", {"img": attach, "form": form},context)
    '''servc = admingivetask(date=request.POST['date'],
                            desc=request.POST['desc'],)
    servc.save()
    return render(request, 'admindetailsadded.html')'''

def proadminviewtrainee(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    print('hai')
    edepartment1=Branch.objects.values('country').distinct()
    tl =  regdetails.objects.filter(designation='TL')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    print(tl)
    context={'edepartments':edepartment1,'mem':mem, 'tl':tl}
    return render(request, 'adminpromarket1.html', context)

def proadmintraineedesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = Branch.objects.filter(country=dept_id).all().values('city').distinct()
    return render(request, 'admintraineedesi.html', {'Desig': Desig})
def proadminloademployeess(request):
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = Branch.objects.filter(city=desi_id).all().filter(country=dept_id).values('branch').distinct()
    return render(request, 'adminloademp.html', {'names': names})

def seradminviewtrainee(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    print('hai')
    edepartment1=Branch.objects.values('country').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'mem':mem}
    return render(request, 'serviceadmin.html', context)
def seradmintraineedesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = Branch.objects.filter(country=dept_id).all().values('city').distinct()
    return render(request, 'admintraineedesi.html', {'Desig': Desig})
def seradminloademployeess(request):
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = Branch.objects.filter(city=desi_id).all().filter(country=dept_id).values('branch').distinct()
    return render(request, 'adminloademployeess.html', {'names': names})

def recadminviewtrainee(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    print('hai')
    edepartment1=Branch.objects.values('country').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'mem':mem}
    return render(request, 'recrutementadmin.html', context)
def recadmintraineedesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = Branch.objects.filter(country=dept_id).all().values('city').distinct()
    return render(request, 'admintraineedesi.html', {'Desig': Desig})
def recadminloademployeess(request):
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = Branch.objects.filter(city=desi_id).all().filter(country=dept_id).values('branch').distinct()
    return render(request, 'adminloademployeess.html', {'names': names})

#-----------branch
def viewbranch1admin(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    print('hai')
    edepartment1=Branch.objects.values('country').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'mem':mem}
    return render(request, 'adminattendance1.html', context)
def viewbranch1showadmin(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    #intern1 = proandmarkng.objects.all()
    emp_id = request.GET.get('empid')
    intern1=Branch.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'names': intern1,'mem':mem}
    return render(request,'adminviewbranch3.html',context)
def admintraineebranch1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    #br1 = regdetails.objects.values('department').distinct().filter(branch=emp_id)
    br1 = regdetails.objects.filter(department='Software').filter(~Q(designation='TL')).distinct().filter(branch=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'brs': br1,'mem':mem}
    return render(request, 'admintraineebranch1.html', context)
def admintraineebranch2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    '''emp_id = request.GET.get('empid')
    intern1=traineeattendance.objects.filter(name=emp_id).values('name').distinct()
    context = {'regdetails': intern1}
    return render(request,'admintraineebranch2.html',context)'''
    emp_id = request.GET.get('empid')
    intern1 = regdetails.objects.filter(name=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'regdetails': intern1,'mem':mem}
    return render(request, 'admintraineebranch2.html', context)
def admintrabranchper1(request):
    emp_id = request.GET.get('empid')
    intern1=regdetails.objects.filter(name=emp_id).values('name').distinct()
    #intern1=traineeattendance.objects.filter(name=emp_id).values('name').distinct()
    context = {'regdetails': intern1}
    return render(request,'admintrabranchper1.html',context)
def admintrabranchatt1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1=employeeattendance.objects.filter(employee=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'names': intern1,'mem':mem}
    return render(request,'admintrabranchatt1.html',context)

def admintrabranchatt11(request):
    emp_id = request.GET.get('empid')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).all().filter(employee=emp_id)
    print(names.values('status','date'))
    return render(request, 'adminatteemp.html', {'names': names})


def viewbranch1admin1(request):
    dept_id = request.GET.get('dept_id')
    Desig = Branch.objects.filter(country=dept_id).all().values('city').distinct()
    return render(request, 'admintraineedesi.html', {'Desig': Desig})
#-------------------------------------------


def adminempbranch1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    #intern1=regdetails.objects.filter(id=emp_id)
    i = regdetails.objects.filter(~Q(designation='admin')).all().filter(branch=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    #intern1 = regdetails.objects.filter(~Q(designation='Trainee')).all
    '''inten = employeeattendance.objects.values('employee').distinct()
    intern1 = regdetails.objects.filter(designation='Manager').all
    i = regdetails.objects.filter(designation='HR').all
    e = employeeattendance.objects.values('employee').distinct()'''
    '''d = regdetails.objects.filter(designation='Developer').all()
    des = regdetails.objects.filter(designation='Designer').all'''
    #context = {'intern': intern1,'hr':i,'inte':inten,'e':e}#,'de':d,'des':des}
    context = {'i':i,'mem':mem}
    return render(request,'adminempbranch1.html',context)

def adminpie_chart(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    labels = []
    data = []
    emp_id = request.GET.get('empid')
    #empdetails=regdetails.objects.filter(id=emp_id)
    queryset = regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    for e1 in queryset:
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
    return render(request, 'adminpie.html', {
        'labels': labels,
        'data': data,
        'mem':mem,
    })
def adminbar_chart(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    labels = []
    data = []
    emp_id = request.GET.get('empid')
    #empdetails=regdetails.objects.filter(id=emp_id)
    queryset = regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    for e1 in queryset:
        labels.append('extrawork')
        data.append(e1.empextrawork)
        labels.append('Creativity')
        data.append(e1.empCreativity)
        labels.append('Performance')
        data.append(e1.empPerformance)
        labels.append('timelycompletion')
        data.append(e1.emptimelycompletion)
        labels.append('attendance')
        data.append(e1.empattendance)
        labels.append('Punctuality')
        data.append(e1.empPunctuality)
        labels.append('o')
        data.append(e1.o)
    return render(request, 'adminbar.html', {
        'labels': labels,
        'data': data,
        'mem':mem,
    })
def admintraperformance1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    return render(request,'admintraper.html',{'emp':empdetails,'mem':mem})
def adminperformance1(request):
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    return render(request,'adminempper1.html',{'emp':empdetails})
def adminperformance2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    return render(request,'adminperformance2.html',{'emp':empdetails,'mem':mem})
def adminperinsert(request):
    if request.method == 'POST':
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        team.empPunctuality = request.POST.get("punctuality")
        team.empPerformance = request.POST.get("perfo")
        team.emptimelycompletion = request.POST.get("tim")
        team.empextrawork = request.POST.get("extra")
        team.empCreativity = request.POST.get("creativity")
        team.empattendance = request.POST.get("attend")
        team.save()
    return render(request,'adminempper1.html')
def admintraperinsert(request):
    if request.method == 'POST':
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        team.empPunctuality = request.POST.get("punctuality")
        team.empPerformance = request.POST.get("perfo")
        team.emptimelycompletion = request.POST.get("tim")
        team.empextrawork = request.POST.get("extra")
        team.empCreativity = request.POST.get("creativity")
        team.empattendance = request.POST.get("attend")
        team.save()
    return render(request,'admintraer1.html')
#--------------------
def adminempman1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1=regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'intern': intern1,'mem':mem}
    return render(request,'adminempman1.html',context)
def adminempper1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    return render(request,'adminempper1.html',{'emp':empdetails,'mem':mem})
def adminempper2(request):
    return render(request,'adminempper2.html')
def adminemphr1(request):
    emp_id = request.GET.get('empid')
    intern1=regdetails.objects.filter(id=emp_id)
    context = {'intern': intern1}
    return render(request,'adminemphr1.html',context)
def adminempde1(request):
    emp_id = request.GET.get('empid')
    intern1=employeeattendance.objects.filter(employee=emp_id)
    context = {'intern': intern1}
    return render(request,'adminempde1.html',context)
def adminempdes1(request):
    emp_id = request.GET.get('empid')
    intern1=regdetails.objects.filter(id=emp_id)
    context = {'intern': intern1}
    return render(request,'adminempdes1.html',context)
def adminempdes11(request):
    emp_id = request.GET.get('empid')
    intern1=employeeattendance.objects.filter(employee=emp_id)
    context = {'inte': intern1}
    return render(request,'adminempdesi11.html',context)

'''def adminempdes11(request):
    emp_id = request.GET.get('empid')
    intern1=employeeattendance.objects.filter(id=emp_id)
    context = {'intern': intern1}
    return render(request,'adminempdes1.html',context)'''
#-reorted issue
def adminrepbranch(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    br1 = hrreport.objects.all().filter(branch=emp_id)#values('branch').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'report': br1,'mem':mem}
    return render(request,'adminrepbranch.html',context)
def rep1(request):
    dept_br = request.GET.get('dept_br')
    Desig = hrreport.objects.filter(branch=dept_br).all()
    return render(request, 'rep1.html', {'report': Desig})
def adminrepbranch1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1=hrreport.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'report': intern1,'mem':mem}
    return render(request,'adminrepbranch1.html',context)
#projectgive
def adminprobranch1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1 = hrprojectsgive.objects.all().filter(branch=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    #intern1 = hrprojectsgive.objects.all()
    context = {'project': intern1,'mem':mem}
    return render(request,'adminprobranch1.html',context)
def adminprobranch2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1=hrprojectsgive.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'project': intern1,'mem':mem}
    return render(request,'adminprobranch2.html',context)
#taskgive
def admintaskbranch1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1 = mangivetasks.objects.all().filter(branch=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'givetask': intern1,'mem':mem}
    return render(request,'admintaskbranch1.html',context)
def admintaskbranch2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1=mangivetasks.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'givetask': intern1,'mem':mem}
    return render(request,'admintaskbranch2.html',context)
#syllabus
def adminsylbranch1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    edepartments = syllabus.objects.filter(branch=emp_id).values('department').distinct()
    edepartments1 = syllabus.objects.filter(branch=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'brs': edepartments,'brs1':edepartments1,'mem':mem}

    #emp_id = request.GET.get('empid')
    #edepartments = syllabus.objects.values('department').distinct().filter(branch=emp_id)
    #context = {'brs': edepartments}
    return render(request,'adminsylbranch1.html',context)
def adminsy(request):
    emp_id = request.GET.get('empid')
    dept_br = request.GET.get('dept_br')
    Desig = syllabus.objects.filter(department=dept_br).distinct().filter(branch=emp_id)
    return render(request, 'adminsy.html', {'Desig': Desig})
def adminsy1(request):
    emp_id = request.GET.get('empid')
    dept_br = request.GET.get('dept_br')
    Desig = admingivetask.objects.filter(department=dept_br).distinct().filter(branch=emp_id)
    return render(request, 'adminsy.html', {'Desig': Desig})

def adminsylbranch2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1=syllabus.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'Desig': intern1,'mem':mem}
    return render(request,'adminsylbranch2.html',context)
'''def adminsyllabusdesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = syllabus.objects.filter(department=dept_id).values('designation').distinct()
    return render(request, 'adminsy.html', {'Desig': Desig})'''



#--------------------------registration

def adminpregistrationdetails(request):
    intern1 = regdetails.objects.all()
    context = {'intern': intern1}
    return render(request, 'adminregistrationdetails2.html',context)

#---view
def adminregistrationdetailsview(request):
    #intern1 = proandmarkng.objects.all()
    emp_id = request.GET.get('empid')
    intern1=regdetails.objects.filter(id=emp_id)
    context = {'intern': intern1}
    return render(request,'adminregistrationdetails2view.html',context)
def adminregistrationdetailsview1(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    inte = regdetails.objects.get(id=id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    #import pdb;pdb.set_trace()
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(inte.employeeimage) > 0:
                os.remove(inte.employeeimage.path)
            inte.employeeimage = request.FILES['employeeimage']
            #inte.signature = request.FILES['signature']
            #inte.idproof = request.FILES['idproof']
        inte.name = request.POST['name']
        inte.email = request.POST['email']
        inte.mobile = request.POST['mobile']
        inte.altermobile = request.POST['altermobile']
        inte.dadname = request.POST['dadname']
        inte.momname = request.POST['momname']
        inte.presntadd1 = request.POST['presntadd1']
        inte.presntadd2 = request.POST['presntadd2']
        inte.presntadd3 = request.POST['presntadd3']
        inte.presntadd4 = request.POST['presntadd4']
        inte.permanantadd1 = request.POST['permanantadd1']
        inte.permanantadd2 = request.POST['permanantadd2']
        inte.permanantadd3 = request.POST['permanantadd3']
        inte.permanantadd4 = request.POST['permanantadd4']
        inte.schhol = request.POST['schhol']
        inte.aggregateschool = request.POST['aggregateschool']
        inte.degreeug = request.POST['degreeug']
        inte.streamug = request.POST['streamug']
        inte.passoutyearug = request.POST['passoutyearug']
        inte.aggregateug = request.POST['aggregateug']
        inte.degreepg = request.POST['degreepg']
        inte.intenshipdetails = request.POST['intenshipdetails']
        inte.intenshipduration = request.POST['intenshipduration']
        inte.intenshipcertification = request.POST['intenshipcertification']
        inte.onlinetrainingdetails = request.POST['onlinetrainingdetails']
        inte.onlinetrainingduration = request.POST['onlinetrainingduration']
        inte.onlinetrainingcertification = request.POST['onlinetrainingcertification']
        inte.projecttitle = request.POST['projecttitle']
        inte.desc = request.POST['desc']
        inte.url = request.POST['url']
        inte.projectduration = request.POST['projectduration']
        inte.skill1 = request.POST['skill1']
        inte.skill2 = request.POST['skill2']
        inte.skill3 = request.POST['skill3']
        inte.save()
    context = {'inter':inte,'mem':mem}
    return render(request, 'adminregistrationdetails2view.html', context)

def updateregdetailsview(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    inte = regdetails.objects.get(id=id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    inte.name = request.POST['name']
    inte.email = request.POST['email']
    inte.mobile = request.POST['mobile']

    inte.altermobile = request.POST['altermobile']
    inte.dadname = request.POST['dadname']
    inte.momname = request.POST['momname']
    inte.presntadd1 = request.POST['presntadd1']
    inte.presntadd2 = request.POST['presntadd2']
    inte.presntadd3 = request.POST['presntadd3']
    inte.presntadd4 = request.POST['presntadd4']
    inte.permanantadd1 = request.POST['permanantadd1']
    inte.permanantadd2 = request.POST['permanantadd2']
    inte.permanantadd3 = request.POST['permanantadd3']
    inte.permanantadd4 = request.POST['permanantadd4']
    inte.schhol = request.POST['schhol']
    inte.aggregateschool = request.POST['aggregateschool']
    inte.degreeug = request.POST['degreeug']
    inte.streamug = request.POST['streamug']
    inte.passoutyearug = request.POST['passoutyearug']
    inte.aggregateug = request.POST['aggregateug']
    inte.degreepg = request.POST['degreepg']
    inte.intenshipdetails = request.POST['intenshipdetails']
    inte.intenshipduration = request.POST['intenshipduration']
    inte.intenshipcertification = request.POST['intenshipcertification']
    inte.onlinetrainingdetails = request.POST['onlinetrainingdetails']
    inte.onlinetrainingduration = request.POST['onlinetrainingduration']
    inte.onlinetrainingcertification = request.POST['onlinetrainingcertification']
    inte.projecttitle = request.POST['projecttitle']
    inte.desc = request.POST['desc']
    inte.url = request.POST['url']
    inte.projectduration = request.POST['projectduration']
    inte.skill1 = request.POST['skill1']
    inte.skill2 = request.POST['skill2']
    inte.skill3 = request.POST['skill3']

    inte.employeeimage = request.POST['employeeimage']
    inte.signature = request.POST['signature']
    inte.idproof = request.POST['idproof']
    inte.save()
    context = {'mem':mem}
    return render(request, 'admindetailsadded.html',context)
#---update
def adminregistrationdetailsedit(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    empdetails=regdetails.objects.filter(id=emp_id)
    countrys1 = Branch.objects.values('branch',).distinct()
    trainer = regdetails.objects.filter(designation='TL').values('name').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    intern1 = Testing.objects.filter(reportid__reportedby=emp_id)
    #pro = [hrprojectsgive.objects.filter(nameid=emp_id).latest('id')]
    #pro = hrprojectsgive.objects.filter(nameid=emp_id)#latest('id')

    #pro = [Testing.objects.filter(testerstatus='Completed',reportid__reportedby=emp_id).latest('id')]
    #pro = Testing.objects.filter(testerstatus='Completed',reportid__reportedby=emp_id)
    context = {'emp': empdetails, 'br': countrys1, 'br2': trainer, 'mem': mem,'promark': intern1}#'leave_object': pro}
    #print('drishya')
    return render(request, 'adminregistrationdetails2update.html', context)
 
'''def adminattenmy112(request):
    regdetails3 = request.GET.get('empid')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = Testing.objects.filter(date__range=(dept_id,desig_id)).filter(reportid__reportedby_id=regdetails3)#.filter(testerstatus='Completed')
    ab = (names.values('date'))
    print(ab)
    #----
    list=[]
    for i in names:
        Dct = {}
        Dct['id'] = i.id

    lst_temp =[]
    lst_count=[]
    lst_task = Report.objects.filter(reportedby_id=regdetails3).values_list('task_id',flat=True).order_by('-id')
    for ins_task in lst_task:
        if ins_task not in lst_count:
            #import pdb;
            #pdb.set_trace()
            lst_count.append(ins_task)
            ins_test=Testing.objects.filter(date__range=(dept_id,desig_id),reportid__reportedby_id=regdetails3,reportid__task_id=ins_task).values('id','project_id__projectname').order_by('-id').first()
            rst_test=Testing.objects.get(id=ins_test['id'])

            if rst_test:
                Dct_temp = {}
                #import pdb;
                #pdb.set_trace()
                Dct_temp['id']=rst_test.id
                Dct_temp['project_id'] = rst_test.project_id
                Dct_temp['projectname'] = rst_test.project.projectname
                Dct_temp['date_diff'] = rst_test.date_diff
                lst_temp.append(Dct_temp)
    print(lst_temp)

    #-----
    return render(request, 'adminattenmy11.html', {'names': names,'latest':lst_temp})'''
def adminattenmy112(request):
    regdetails3 = request.GET.get('empid')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = Testing.objects.filter(date__range=(dept_id,desig_id)).filter(reportid__reportedby_id=regdetails3)#.filter(testerstatus='Completed')
    ab = (names.values('date'))
    print(ab)
    #----
    '''    list=[]
    for i in names:
        Dct = {}
        Dct['id'] = i.id'''

    lst_temp =[]
    lst_count=[]
    lst_task = Report.objects.filter(reportedby_id=regdetails3).values_list('task_id',flat=True).order_by('-id')
    for ins_task in lst_task:
        if ins_task not in lst_count:
            #import pdb;
            #pdb.set_trace()
            lst_count.append(ins_task)
            ins_test=Testing.objects.filter(date__range=(dept_id,desig_id),reportid__reportedby_id=regdetails3,reportid__task_id=ins_task).\
                values('id','project_id__projectname').order_by('-id').first()
            rst_test=Testing.objects.get(id=ins_test['id'])
            if rst_test:
                Dct_temp = {}
                #import pdb;
                #pdb.set_trace()
                Dct_temp['id']=rst_test.id
                Dct_temp['project_id'] = rst_test.project_id
                Dct_temp['projectname'] = rst_test.project.projectname
                Dct_temp['date_diff'] = rst_test.date_diff
                lst_temp.append(Dct_temp)
    print(lst_temp)

    lst_tempsub = []
    lst_countsub = []
    lst_tasksub = Report.objects.filter(reportedby_id=regdetails3).values_list('subtask_id', flat=True).order_by('-id')
    for ins_tasksub in lst_tasksub:
        if ins_tasksub not in lst_countsub:
            # import pdb;
            # pdb.set_trace()
            lst_countsub.append(ins_tasksub)
            ins_testsub = Testing.objects.filter(date__range=(dept_id, desig_id), reportid__reportedby_id=regdetails3,
                                              reportid__subtask_id=ins_tasksub). \
                values('id', 'project_id__projectname').order_by('-id').first()
            rst_testsub = Testing.objects.get(id=ins_testsub['id'])
            if rst_testsub:
                Dct_temp = {}
                # import pdb;
                # pdb.set_trace()
                Dct_temp['id'] = rst_testsub.id
                Dct_temp['project_id'] = rst_testsub.project_id
                Dct_temp['projectname'] = rst_testsub.project.projectname
                Dct_temp['date_diff'] = rst_testsub.date_diff
                lst_tempsub.append(Dct_temp)
    print(lst_tempsub)
    names = Testing.objects.filter(date__range=(dept_id,desig_id)).filter(reportid__reportedby_id=regdetails3)#.filter(testerstatus='Completed')
    sd = 0
    '''for i in names:
        if i.reportid.reportedby.designation == 'TL':
            sd=lst_temp
        else:
            sd=lst_tempsub'''
    for i in names:
        if i.reportid.subtask_id is None:
            sd=lst_temp
        else:
            sd=lst_tempsub
    #print(sd)
    #-----
    return render(request, 'adminattenmy11.html', {'names': names,'latest':lst_temp,'latestsub':lst_tempsub,'sd':sd})

def adminattenmy(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    regdetails3 = request.GET.get('taskid')
    intern1 = Testing.objects.filter(reportid__reportedby=regdetails3)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'promark': intern1,'mem':mem}
    print('hy')
    #regdetails3 = request.GET.get('empid')
    return render(request,'addelay.html',context)
def adminattenmy11(request):
    regdetails3 = request.GET.get('taskid')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = Testing.objects.filter(date__range=(dept_id,desig_id)).filter(reportid_id=regdetails3)
    ab=(names.values('date'))
    print(ab)
    return render(request, 'adminattenmy11.html', {'names': names})
def updateregdetails(request):
    if request.method == 'POST':
        inte = regdetails.objects.get(id=request.POST.get('team_id'))
        #inte = regdetails.objects.get(id=id)
        inte.employeeid = request.POST['employeeid']
        inte.name = request.POST['name']
        inte.email = request.POST['email']
        inte.mobile = request.POST['mobile']
        inte.qualification = request.POST['qualification']
        inte.duration = request.POST['duration']
        inte.department = request.POST['department']
        #inte.dateofappoinment = request.POST['dateofappoinment']
        inte.dateofrelieve = request.POST['dateofrelieve']
        inte.refid = request.POST['refid']
        inte.payment = request.POST['payment']
        inte.updatecondition = request.POST['updatecondition']
        inte.addconditionno = request.POST['addconditionno']
        inte.addcondition = request.POST['addcondition']
        inte.certfanddesig = request.POST['certfanddesig']
        inte.branch = request.POST['branch']
        inte.designation = request.POST['designation']
        inte.trainer = request.POST['trainer']
        inte.platform = request.POST['platform']
        inte.intenshipstart = request.POST['intenshipstart']
        inte.intenshipend = request.POST['intenshipend']
        inte.deduction = request.POST['deduction']
        inte.intensive = request.POST['intensive']
        inte.increment = request.POST['increment']
        inte.confirmsalary = request.POST['confirmsalary']
        inte.delay = request.POST['delay']
        inte.totalsalary = request.POST['totalsalary']
        inte.save()
        '''num1=inte.intensive = request.GET['intensive']
        num2=inte.intensive = request.GET('increment')
        num3 = num1 - num2
        print(num3)'''
        return render(request, 'adminregistrationdetails2.html', )
def calc(request):
    task_id = request.GET.get('taskid')
    mem=regdetails.objects.filter(id=task_id)
    context = {'mem':mem}
    return render(request,'calc.html',context)
def calca(request):
    confirmsalary = int(request.GET.get("confirmsalary"))
    delay = int(request.GET.get("delay"))
    num3 = ((confirmsalary)/31)*delay
    print(num3)
    num4 = confirmsalary - num3
    print(num4)
    return render(request,'calc1.html',{'Result':num4})
def deleteregdetails(request, id):
    sl = regdetails.objects.get(id=id)
    sl.delete()
    return render(request, 'registrationdetails1.html')

#------expeirnce certificate
'''def adminexperiencecertificate1(request):
    edepartment1=branch.objects.values('country').distinct()
    #bdepartment1=regdetails.objects.values('branch').distinct()
    context={'edepartments':edepartment1}#,'bdepartments':bdepartment1}
    return render(request, 'adminexperiencecertificate1.html', context)'''
def adminexperiencecertificate2(request):
    emp_id = request.GET.get('email')
    intern1=regdetails.objects.filter(id=emp_id)
    context = {'intern': intern1}
    return render(request,'adminexperiencecertificate2.html',context)
def adminexperiecnceedit(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    print('hi')
    intern = regdetails.objects.get(id=id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'intern': intern,'mem':mem}
    return render(request, 'adminupdateexp.html', context)

def updateexperiencedetails(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    inte = regdetails.objects.get(id=id)
    inte.slno = request.POST['slno']
    inte.name = request.POST['name']
    inte.email = request.POST['email']
    inte.password = request.POST['password']
    inte.qualification = request.POST['qualification']
    inte.duration = request.POST['duration']
    inte.department = request.POST['department']
    inte.dateofappoinment = request.POST['dateofappoinment']
    inte.regid = request.POST['regid']
    inte.payment = request.POST['payment']
    inte.performance = request.POST['performance']
    inte.save()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request, 'admindetailsadded.html',context)

#expeience completed!--------------------


def adminid(request):
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(email=dept_id).all().values('email').distinct()
    return render(request, 'adminid.html', {'Desig': Desig})

def adminbranch11(request):
    dept_id = request.GET.get('dept_id')
    Desig = Branch.objects.filter(country=dept_id).all().values('city').distinct()
    return render(request, 'adminbranch11.html', {'Desig': Desig})
def adminbranch(request):
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = Branch.objects.filter(city=desi_id).all().filter(country=dept_id).all()
    return render(request, 'viewbranch2admin.html', {'names': names})

def adminbranch2(request):
    intern1 = Branch.objects.all()
    context = {'branchs': intern1}
    return render(request,'viewbranch2admin.html',context)
#-------------------
'''def adminattendance1(request):
    edepartment1 = branch.objects.values('country').distinct()
    context = {'edepartments': edepartment1}
    return render(request,'adminattendance1.html',context)'''
def adminhremp(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    dept_id = request.GET.get('regdetails1')
    desig_id = request.GET.get('regdetails2')
    names = Branch.objects.filter(country=dept_id).all().filter(city=desig_id).all()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    return render(request, 'adminhremployeesearch.html', {'names': names,'mem':mem})


def adminempdesi(request):
    dept_id = request.GET.get('dept_id')
    Desig = Branch.objects.filter(country=dept_id).all().values('city').distinct()
    return render(request, 'adminhrempdesi.html', {'Desig': Desig})
#====branch
def br(request):
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    desig_br = request.GET.get('desig_br')
    Desig = Branch.objects.filter(country=dept_id).all().filter(city=desig_id).filter(branch=desig_br).all
    return render(request, 'br.html', {'Desig': Desig})
def br1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    dept_br = request.GET.get('branch')
    dept_id = request.GET.get('enterid')
    names = regdetails.objects.filter(email=dept_id).all().filter(branch=dept_br).all()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    return render(request, 'adminexperiencecertificate2.html', {'names': names,'mem':mem})
def br2(request):
    dept_id = request.GET.get('dept_id')
    dept_city = request.GET.get('dept_city')
    Desig = Branch.objects.filter(country=dept_id).all().filter(city=dept_city).all().values('branch').distinct()
    return render(request, 'br2.html', {'Desig': Desig})

def loadbranch(request):
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = Branch.objects.filter(city=desi_id).all().filter(country=dept_id).all()
    return render(request, 'loadbranch.html', {'names': names})
def regi1(request):
    branchId = request.GET.get('branch_id')
    names = Branch.objects.filter(country=branchId).all()
    print('hai')
    return render(request, 'regsearch.html', {'brs': names})

def adminexperiencecertificate1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    edepartment1 = Branch.objects.values('country').distinct()
    br1 = regdetails.objects.values('branch').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'edepartments': edepartment1,'brs':br1,'mem':mem}
    return render(request,'adminexperiencecertificate1.html',context)

#--------attendance--
def adminattendance1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    edepartment3 = Branch.objects.filter(branch=emp_id)
    edepartment1 = Branch.objects.values('country').distinct()
    br1 = regdetails.objects.values('branch').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'edepartments': edepartment1,'brs':br1,'brs1':edepartment3,'mem':mem}
    return render(request,'adminattendance11.html',context)
def adminattendance2(request):
    return render(request,'adminattendance2.html')
def adminputmanagerattendance(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    regdetails3 = request.GET.get('empid')
    give1 = regdetails.objects.all().filter(branch=regdetails3).filter(designation='MANAGER')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'give1':give1,'mem':mem}
    return render(request,'adminputmanagerattendance.html',context)
def managerattendanceadd(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    manager = employeeattendance(branch=request.POST['branch'],employee=request.POST.get('employee'),department=request.POST.get('department'),
                            date=request.POST['date'],
                            status=request.POST['status'],
                            login=request.POST['login'],
                            logout=request.POST['logout'],)
    manager.save()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem}
    return render(request,'adminattendance2.html',context)
def adminmanagerattendance1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    regdetails3 = request.GET.get('empid')
    intern1 = employeeattendance.objects.all().filter(branch=regdetails3).filter(department='Manager')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'promark': intern1,'mem':mem}
    print('hy')
    #regdetails3 = request.GET.get('empid')
    return render(request,'adminmanagerattendance1.html',context)
def adminmanagerattendance11(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    regdetails3 = request.GET.get('empid')
    intern1 = employeeattendance.objects.filter(employee=regdetails3)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'promark': intern1,'mem':mem}
    print('hy')
    #regdetails3 = request.GET.get('empid')
    return render(request,'adminmanagerattendance11.html',context)
def adminmanageratte11(request):
    regdetails3 = request.GET.get('empid')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).filter(employee=regdetails3)
    print(names.values('status','date','login','logout'))
    return render(request, 'adminatte1.html', {'names': names})
def adminmanageratte1(request):
    regdetails3 = request.GET.get('empid')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).filter(employee=regdetails3)
    print(names.values('status','date','login','logout'))
    return render(request, 'adminatte.html', {'names': names})
def adminhrattendance1(request):
    return render(request,'adminemphratt1.html')
def adminhratte1(request):
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = hrattendancet.objects.filter(date__range=(dept_id,desig_id)).all()
    print(names.values('status','date','login','logout'))
    return render(request, 'adminhr.html', {'names': names})
#----leave request
def adminleaveapplication1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    regdetails3 = request.GET.get('empid')
    intern1 = leavereq.objects.all().filter(branch=regdetails3)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'leave': intern1,'mem':mem}
    return render(request,'adminleaveapplication1.html',context)
def adminleaveapplication2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    #intern1 = proandmarkng.objects.all()
    emp_id = request.GET.get('empid')
    intern1=leavereq.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'leave': intern1,'mem':mem}
    return render(request,'adminleaveapplication2.html',context)









def at2(request):
    emp_id = request.GET.get('empid')
    #br1 = regdetails.objects.values('department').distinct().filter(branch=emp_id)
    #br1 = regdetails.objects.filter(department='Software').filter(~Q(designation='TL')).distinct().filter(branch=emp_id)
    dept_br = request.GET.get('dept_br')
    Desig = regdetails.objects.filter(designation=dept_br).values('name').distinct().filter(department='Software').filter(branch=emp_id)
    #Desig = traineeattendance.objects.filter(department=dept_br).values('name').distinct()#.filter(department='Software').all
    return render(request, 'at2.html', {'Desig': Desig})

def reg2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    dept_br3 = request.GET.get('branch')
    #Desig = branch.objects.filter(branch=dept_br).all
    Desig = regdetails.objects.filter(branch=dept_br3).all()
    intern1 = regdetails.objects.filter(branch=dept_br3).all().order_by('-id')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    form = SearchForm(request.POST or None)
    context = {'Desig': Desig,'intern': intern1,"fadmintraineebranch1orm": form,'mem':mem}
    if request.method == 'POST':
        #n = request.GET.get('n1')
        #queryset = regdetails.objects.filter(name=n).all()
        queryset = regdetails.objects.all().order_by('-employeeid').filter(name__icontains=form['name'].value(), email__icontains = form['email'].value())
        context = {"queryset": queryset}
    print('hy')
    return render(request, 'adminregistrationdetails2.html',context)#,{'Desig': Desig,'intern': intern1,"form": form})   #reg2.html
def seradmintraineedesi1(request):
    dept_id = request.GET.get('dept_id')
    Desig = Branch.objects.filter(country=dept_id).all().values('city').distinct()
    return render(request, 'admintraineedesi1.html', {'Desig': Desig})
def seradminloademployeess1(request):
    desi_id = request.GET.get('desi_id')
    dept_id = request.GET.get('dept_id')
    names = Branch.objects.filter(city=desi_id).all().filter(country=dept_id).values('branch').distinct()
    return render(request, 'adminloademployeess1.html', {'names': names})
def admintaskmanager1(request):
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    branch_id = request.GET.get('branch_id')
    names = Branch.objects.filter(country=dept_id).all().filter(city=desig_id).all().filter(branch=branch_id).all()
    return render(request, 'adminregistrationdetails2.html', {'names': names})
'''def reg22(request):
    form = SearchForm(request.POST or None)
    context = {"form": form}
    if request.method == 'POST':
        #n = request.GET.get('n1')
        #queryset = regdetails.objects.filter(name=n).all()
        queryset = regdetails.objects.all().order_by('-employeeid').filter(name__icontains=form['name'].value(), email__icontains = form['email'].value())
        context = {"queryset": queryset}
    print('hy')
    return render(request,'adminregistrationdetails2.html',context)'''
'''class Blogsearchadmin():
    model = regdetails
    template_name = 'adminregistrationdetails2.html'
    context_object_name = 'posts'
    def get_queryset(self):
        query = self.request.GET.get('g')
        return regdetails.objects.filter(title_icontains=query).order_by('-created_at')'''
def searchadmin(request):
    dept_br = request.GET.get('dept_br')
    Desig = regdetails.objects.filter(name=dept_br).all()
    return render(request,'searchadmin.html', {'Desig': Desig})
def ex(request):
    intern1=regdetails.objects.all
    context = {'intern': intern1}
    return render(request,'adminupdateexp.html',context)

def adminmanageinternship1(request):
    edepartment1=Branch.objects.values('country').distinct()
    br1 = regdetails.objects.values('branch').distinct()
    context = {'edepartments': edepartment1,'brs':br1}
    return render(request, 'adminmanageinternship1.html', context)

def addpandse(request):
    if request.method == "POST":
        form = ImageFormadmin(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            form = ImageFormadmin()
            img = im.objects.all()
            idproof = im.objects.all()
            return render(request, "admininternshipregistration1.html", {"img": img,"idproof":idproof ,"form": form})
    else:
        form = ImageFormadmin()
        img = im.objects.all()
        idproof = im.objects.all()
        return render(request, "admindetailsadded.html", {"img": img, "idproof":idproof,"form": form})

def s(request):
    intern1=regdetails.objects.all
    context = {'intern': intern1}
    return render(request,'searchadmin.html',context)
def dynamic_articles_view(request):
    intern1=regdetails.objects.filter(name__icontains=request.GET.get('search')) or regdetails.objects.filter(designation__icontains=request.GET.get('search'))
    context = {'intern': intern1}
    return render(request, 'adminregistrationdetails2.html', context)
def dynamic_articles_view1(request):
    intern1=Item.objects.filter(startdate__icontains=request.GET.get('search')) or Item.objects.filter(college__icontains=request.GET.get('search')) or Item.objects.filter(name__icontains=request.GET.get('search'))
    context = {'intern': intern1}
    return render(request, 'admininternshipregistrationdetails.html', context)
'''def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404'''
def intqrshow(request,username):
    user=Item.objects.get(studname=username)
    return render(request,'qshow.html',{"data":user})
def addProduct(request):
    #college1 = college.objects.all()
    branch1 = Branch.objects.values('branch',).distinct()
    countrys1 = Branch.objects.values('country',).distinct()
    context = { 'branches': branch1,'countrys':countrys1}#'colleges': college1,
    if request.method == "POST":
        college = request.POST.get('college')
        regno = request.POST.get('regno')
        name = request.POST.get('name')
        platform = request.POST.get('platform')
        department = request.POST.get('department')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        refid = request.POST.get('refid')
        payment = request.POST.get('payment')
        country = request.POST.get('country')
        branch = request.POST.get('branch')
        course = request.POST.get('course')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        college1 = Item(college=college,regno=regno,name=name,platform=platform,department=department,startdate=startdate,enddate=enddate,refid=refid,payment=payment,country=country,branch=branch,course=course,email=email,mobile=mobile)
        qr = make(settings.LOCALROOT + name)
        qr.save(settings.MEDIA_ROOT + "\\" + name + ".png")
        with open(settings.MEDIA_ROOT + "\\" + name + ".png", "rb") as reopen:
            djangofile = File(reopen)
            college1.qr = djangofile
            #college1.image = request.FILES['image']
            #college1.idproof = request.FILES['idproof']
            college1.save()
        #return redirect(reverse('intqrshow', args=[name]))
    return render(request, 'add.html',context)
    '''if request.method == "POST":
        prod = Item()
        prod.college = request.POST.get('college')
        prod.regno = request.POST.get('regno')
        prod.name = request.POST.get('name')
        prod.platform = request.POST.get('platform')
        prod.department = request.POST.get('department')
        prod.startdate = request.POST.get('startdate')
        prod.enddate = request.POST.get('enddate')
        prod.refid = request.POST.get('refid')
        prod.payment = request.POST.get('payment')
        prod.country = request.POST.get('country')
        prod.branch = request.POST.get('branch')
        prod.course = request.POST.get('course')
        prod.email = request.POST.get('email')
        prod.mobile = request.POST.get('mobile')


        if len(request.FILES) != 0:
            prod.image = request.FILES['image']
            prod.idproof = request.FILES['idproof']
        prod.save()
        #messages.success(request, "Product Added Successfully")
        return render(request, 'add.html')
    return render(request, 'add.html',context)'''
def indexxxx(request):
    products = Item.objects.all()
    context = {'products':products}
    return render(request, 'indexxxx.html', context)
def editProduct(request, id):
    prod = Item.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
            prod.idproof = request.FILES['idproof']
        prod.college = request.POST.get('college')
        prod.regno = request.POST.get('regno')
        prod.name = request.POST.get('name')
        prod.platform = request.POST.get('platform')
        prod.department = request.POST.get('department')
        prod.startdate = request.POST.get('startdate')
        prod.enddate = request.POST.get('enddate')
        prod.refid = request.POST.get('refid')
        prod.payment = request.POST.get('payment')
        prod.country = request.POST.get('country')
        prod.branch = request.POST.get('branch')
        prod.course = request.POST.get('course')
        prod.email = request.POST.get('email')
        prod.mobile = request.POST.get('mobile')
        prod.save()
        #messages.success(request, "Product Updated Successfully")
        return render(request, 'edit.html')

    context = {'prod':prod}
    return render(request, 'edit.html', context)

def viewProduct(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    prod = Item.objects.get(id=id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
            prod.idproof = request.FILES['idproof']
        prod.name = request.POST.get('name')
        prod.platform = request.POST.get('platform')
        prod.startdate = request.POST.get('startdate')
        prod.enddate = request.POST.get('enddate')
        prod.course = request.POST.get('course')
        prod.email = request.POST.get('email')
        prod.mobile = request.POST.get('mobile')
        prod.save()
        #messages.success(request, "Product Updated Successfully")
        #return redirect('admininternshipregistration1.html')

    context = {'prod':prod,'mem':mem}
    return render(request, 'internviewdetails.html', context)

'''def GeneratePdf(request):
    return render(request,'invoice.html')'''
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        emp_id = request.GET.get('empid')
        intern = regdetails.objects.filter(id=emp_id)#get(id=id)
        #empdetails = regdetails.objects.all()#filter(id=emp_id)
        data = {'names': intern}
        #data = {
#             'today': datetime.date.today(),
        #     'amount': 39.99,
         #   'customer_name': 'Cooper Mann',
          #  'order_id': 1233434,
        #}
        pdf = render_to_pdf('pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf.html', context,html)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

'''def invoi(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('preview', pk=instance.id)
    context = {'form':form}
    return render(request, 'invoice.html', context)
def preview(request, id):
    reg = Register.objects.get(id=id)
    prev = RegisterForm(instance=reg)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=reg)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'reg':reg, 'prev':prev}
    return render(request, 'preview.html', context)'''
#-----------------------------------------------------------pdf-----------



def render_to_pdf1(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    "company": "Dennnis Ivanov Company",
    "address": "123 Street name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",

    "phone": "555-555-2345",
    "email": "youremail@dennisivy.com",
    "website": "dennisivy.com",
}


# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        emp_id = request.GET.get('empid')
        intern = Item.objects.filter(id=emp_id)#get(id=id)
        d = {'intern': intern}
        pdf = render_to_pdf('preview.html', d)
        return HttpResponse(pdf, content_type='application/pdf')
class ViewPDFreg(View):
    def get(self, request, *args, **kwargs):
        emp_id = request.GET.get('empid')
        intern = regdetails.objects.filter(id=emp_id)#get(id=id)
        d = {'intern': intern}
        pdf = render_to_pdf('previewreg.html', d)
        return HttpResponse(pdf, content_type='application/pdf')

# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('app/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def invoice(request):
    context = {}
    return render(request, 'invoice.html', context)

def render_to_pdf2(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
class GeneratePdf2(View):
    def get(self, request, *args, **kwargs):
        emp_id = request.GET.get('empid')
        intern = regdetails.objects.filter(id=emp_id)
        data = {'names': intern}
        pdf = render_to_pdf('appoinment.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
'''class GeneratePDF2(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('appoinment.html')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")'''

def render_to_pdf3(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
class GeneratePdf3(View):
    def get(self, request, *args, **kwargs):
        #emp_id = request.GET.get('empid')
        intern = regdetails.objects.all()#filter(id=emp_id)
        data = {'names': intern}
        pdf = render_to_pdf('idcardadmin.html', data)
        return HttpResponse(pdf, content_type='application/pdf',)

def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    return path
#--------------------idcardpd

def render_pdf_view11(request):
    emp_id = request.GET.get('empid')
    intern = regdetails.objects.filter(id=emp_id)
    template_path = 'idcardadmin.html'
    context = {'myvar': 'this is your template context','names': intern}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def newid(request):
    emp_id = request.GET.get('empid')
    intern = regdetails.objects.filter(id=emp_id)
    context = {'names':intern}
    return render(request,'newid.html',context)
'''def newid(request):
    emp_id = request.GET.get('empid')
    intern = regdetails.objects.filter(id=emp_id)
    template_path = 'newid.html'
    context = {'myvar': 'this is your template context','names': intern}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/jpg')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response'''
def qr(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("name"), image_factory=factory, box_size=10)
        #img = regdetails.objects.get(id=request.POST.get('name'))
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
    return render(request,'qr.html',context)

def addqr(request):
    branch1 = Qr(name=request.POST['name'],svg=request.POST['svg'])
    branch1.save()
    return render(request, 'adminbranchadded.html')
    '''if request.method == 'POST':
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        team.payment = request.POST.get("pending")
        team.save()
        return render(request,'acntreceipts.html')'''

def viewProductreg(request,id):
    prod = regdetails.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.photo) > 0:
                os.remove(prod.photo.path)
            prod.photo = request.FILES['photo']
            prod.idproof = request.FILES['idproof']
        prod.name = request.POST.get('name')
        prod.platform = request.POST.get('platform')
        prod.startdate = request.POST.get('startdate')
        prod.enddate = request.POST.get('enddate')
        prod.course = request.POST.get('course')
        prod.email = request.POST.get('email')
        prod.mobile = request.POST.get('mobile')
        prod.save()
        #messages.success(request, "Product Updated Successfully")
        return redirect('/')

    context = {'prod':prod}
    return render(request, 'adminregistrationdetails2view.html', context)
#-----------------add
def qrnew(request):
    '''if request.method == 'Post':
        urname = request.POST.get('urname')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        member = Profile(urname=urname,name=name,phone=phone,age=age)
        img= make(settings.LOCALROOT+urname)
        img.save(settings.MEDIA_ROOT+"\\"+urname+".png")
        with open(settings.MEDIA_ROOT+"\\"+urname+".png","rb") as reopen:
            djangofile =File(reopen)
            member.img=djangofile
            member.save()
        return redirect(reverse('qrshow.html', args=[urname]))'''
    return render(request,'qrnew.html')
# def qrshow(request,username):
#     user=regdetails.objects.get(name=username)
#     return render(request,'qrshow.html',{"data":user})
    '''user=Profile.objects.get(urname=username)
    return render(request,'qrshow.html',{"data":user})'''
def qradd(request):
    '''if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        designation = request.POST.get('designation')
        mobile = request.POST.get('mobile')
        dateofappoinment = request.POST.get('dateofappoinment')
        dateofrelieve = request.POST.get('dateofrelieve')
        performance = request.POST.get('performance')
        college1 = regdetails(name=name,email=email,qualification=qualification,designation=designation,mobile=mobile,dateofappoinment=dateofappoinment,dateofrelieve=dateofrelieve,performance=performance)
        qr = make(settings.LOCALROOT + name)
        qr.save(settings.MEDIA_ROOT + "\\" + name + ".png")
        with open(settings.MEDIA_ROOT + "\\" + name + ".png", "rb") as reopen:
            djangofile = File(reopen)
            college1.qr = djangofile
            college1.save()
        return redirect(reverse('qrshow',args=[name]))
    return render(request, 'qrnew.html')'''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        designation = request.POST.get('designation')
        mobile = request.POST.get('mobile')
        dateofappoinment = request.POST.get('dateofappoinment')
        dateofrelieve = request.POST.get('dateofrelieve')
        performance = request.POST.get('performance')
        employeeimage = request.POST.get('employeeimage')
        college1 = regdetails(name=name,email=email,qualification=qualification,designation=designation,mobile=mobile,dateofappoinment=dateofappoinment,dateofrelieve=dateofrelieve,performance=performance,employeeimage=employeeimage)

        qr = make(settings.LOCALROOT + name)
        qr.save(settings.MEDIA_ROOT + "\\" + name + ".png")
        with open(settings.MEDIA_ROOT + "\\" + name + ".png", "rb") as reopen:
            djangofile = File(reopen)
            college1.qr = djangofile
            college1.save()
        return redirect(reverse('qrshow', args=[name]))
    return render(request, 'qrnew.html')

def adtask2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    regdetails3 = request.GET.get('branch')
    give = regdetails.objects.all().filter(branch=regdetails3)
    give1 = Branch.objects.all().filter(branch=regdetails3)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'give': give,'give1':give1,'mem':mem}
    return render(request, 'admingivetask2.html',context)
def adminat2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    regdetails3 = request.GET.get('branch')
    give = Branch.objects.all().filter(branch=regdetails3).values('branch').distinct()
    give1 = Branch.objects.all().filter(branch=regdetails3).values('branch').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'give': give,'give1':give1,'mem':mem}
    return render(request, 'adminattendance2.html',context)
#--------------------------------------------------------END--------------------------------------------------




#---employee attendence
def adminemployeeattendance1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    edepartment1=employeeattendance.objects.values('department').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'edepartments': edepartment1,'mem':mem}
    return render(request,'adminemployeeattendance1.html',context)
def adminempatte(request):
    dept_id = request.GET.get('dept_id')
    Desig = employeeattendance.objects.filter(department=dept_id).all().values('branch').distinct()
    return render(request, 'adminempatte.html', {'Desig': Desig})
'''def adminempatt(request):
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).all().values('branch').distinct()
    return render(request, 'adminemp1.html', {'Desig': Desig})'''

def empat2(request):
    intern1 = employeeattendance.objects.all()
    context = {'names': intern1}
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    Desig = employeeattendance.objects.filter(department=dept_id).all().filter(branch=desig_id).values('employee').distinct()
    return render(request, 'emp2.html', {'Desig': Desig},context)
def adminempatteshow(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    intern1=employeeattendance.objects.filter(employee=emp_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'names': intern1,'mem':mem}
    return render(request,'adminempatteshow.html',context)

def adminempatte1(request):
    emp_id = request.GET.get('empid')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).all().filter(employee=emp_id)
    print(names.values('status','date'))
    return render(request, 'adminatteemp.html', {'names': names})


#-------admin register
def adminregnew(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    print('hai')
    #br1=Branch.objects.values('country').distinct()
    edepartment1 = Branch.objects.values('country').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'edepartments': edepartment1,'mem':mem}
    return render(request,'adminregnew.html',context)
def adminregsmall(request):
    dept_id = request.GET.get('dept_id')
    Desig = regdetails.objects.filter(department=dept_id).all().values('designation').distinct()
    return render(request, 'adminregsmall.html', {'Desig': Desig})
def adminregnewadd(request):
    if request.method == "POST":
        form = RegnewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            form = RegnewForm()
        employeeimage = regdetails.objects.all()
        return render(request, "admindetailsadded.html", {"img": employeeimage, "form": form})
    else:
        form = RegnewForm()
        employeeimage = regdetails.objects.all()
        return render(request, "admindetailsadded.html", {"img": employeeimage, "form": form})
#-----admin change password
def adminpassword(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    intern = regdetails.objects.get(id=id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'inter': intern,'mem':mem}
    return render(request,'adminpassword.html',context)
def updateadminpassword(request,id):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    inte = regdetails.objects.get(id=id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    inte.password = request.POST['password']
    inte.save()
    context = {'mem':mem}
    return render(request,'admindetailsadded.html',context)
def admingiveproject1(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    emp_id = request.GET.get('empid')
    edepartments3 = Branch.objects.filter(branch=emp_id)
    print('hai')
    edepartment1=Branch.objects.values('country').distinct()
    edepartment2 = Branch.objects.values('branch').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'brs':edepartment2,'brs1':edepartments3,'mem':mem}
    return render(request,'admingiveproject1.html',context)
def adproject2(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    regdetails3 = request.GET.get('branch')
    give = regdetails.objects.all().filter(branch=regdetails3)
    give1 = Branch.objects.all().filter(branch=regdetails3)
    give2 = regdetails.objects.all().filter(branch=regdetails3,designation='MANAGER')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'give': give,'give1':give1,'mem':mem,'give2':give2}
    return render(request, 'admingiveproject2.html',context)
def giveprojrctadminadd(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    give = Project.objects.all()
    context = {'give': give}
    #import pdb;pdb.set_trace()
    if request.method == "POST":
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['attachfile']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,
                                       base_url=settings.MEDIA_URL)
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
        form = Project(branch=request.POST['branch'],assignedto=request.POST['assignedto'],assignedby=usernameadmin,
                startdate=request.POST['startdate'],duedate=request.POST['duedate'],projectname=request.POST['projectname'],
                description=request.POST['description'],json_attachfile=lst_file)
        form.save()
        return render(request, "admindetailsadded.html")
def adminMANmyproject(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    projectt=Project.objects.all()
    #task=hrprojectsgive.objects.filter(branch=usernameM2,employee=usernameM1).all().order_by('-id')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    return render(request, 'adminMANmyproject.html',{'pro':projectt,'mem':mem})
def adminMANmyprojectsubtask(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    emp_id = request.GET.get('prid')
    emp = PrTasktoTL.objects.filter(project_id=emp_id).all
    proj=Project.objects.filter(id=emp_id)
    repo = Report.objects.filter(project_id=emp_id).all()
    department1 = regdetails.objects.values('department').distinct().all()#.filter(branch=usernameM2)
    tester = regdetails.objects.all()#.filter(branch=usernameM2).filter(designation='Tester')
    map = {}
    for i in repo:
        id = i.task_id
        #id = i.reportedby_id
        if map.get(id) is None:
            list = []
            list.append(i)
            map[id] = list
        else:
            list = map.get(id)
            list.append(i)
    # for Test status===========

    test = Testing.objects.filter(project_id=emp_id).all()
    testmap = {}
    for i in test:
        id = i.reportid.task_id
        if testmap.get(id) is None:
            list = []
            list.append(i)
            testmap[id] = list
        else:
            list = testmap.get(id)
            list.append(i)

    # for extension status=====
    extensionrqst = PrTasktoTL.objects.filter(project_id=emp_id).all()
    Extensionmap = {}
    for i in extensionrqst:
        id = i.id
        if Extensionmap.get(id) is None:
            list = []
            list.append(i)
            Extensionmap[id] = list
        else:
            list = Extensionmap.get(id)
            list.append(i)

    test1 = Testing.objects.filter(project_id=emp_id)#,task_id=emp_id)
    return render(request, 'adminMANmyprojectsubtaskAdd.html', {'mem': mem, 'emp1': emp, 'proj': proj, 'rep': map,'testm':testmap,'leave_object':test1,'extension':Extensionmap})

def adminMANMyprojectsubtaskProjectstatus(request):
    if request.method == 'POST':
        team = PrTasktoTL.objects.get(id=request.POST.get('team_id'))
        team.prostatus = request.POST.get("status")
        team.progress = request.POST.get("progre")
        team.save()
        base_url = reverse('adminMANmyprojectsubtask')
        query_string = urlencode({'prid': team.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

def one(request):
    return render(request,'1.html')

def qrshowres(request):
    return render(request,'qres.html')
def qrnotres(request):
    return render(request,'qrshow.html')
def new(request):
    return render(request,'l.html')
def please(request):
    return render(request,'please.html')
def v(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    task_id = request.GET.get('taskid')
    task = regdetails.objects.filter(id=task_id)
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    #countrys1 = Branch.objects.values('branch',).distinct()
    context = {'inter': task,'mem':mem}#,'br':countrys1}
    return render(request, 'v.html', context)
def up(request):
    if request.method == "POST":
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        #team.submited='submitted'
        form = VForm(data=request.POST, files=request.FILES, instance=team)
        form.save()
        return render(request, 'v.html', {'inter': team})
def homesec(request):
    if request.session.has_key('usernameadmin'):
        usernameadmin = request.session['usernameadmin']
    if request.session.has_key('usernameadmin1'):
        usernameadmin1 = request.session['usernameadmin1']
    else:
        usernameadmin = "dummy"
    task_id = request.GET.get('taskid')
    #task = regdetails.objects.filter(id=task_id)
    mem=regdetails.objects.filter(id=task_id)
    mem1 = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    return render(request,'v.html',{'mem':mem,'mem1':mem1})
def logindp(request):
    if request.method == "POST":
        team = regdetails.objects.get(id=request.POST.get('team_id'))
        form = VForm(data=request.POST, files=request.FILES, instance=team)
        form.save()
        return render(request,'registrationdetails1.html')
def logout(request):
    return render(request,'login.html')


#----------------Bibin Section---------------------------------------------------------------------------------------------------

def MANmarketing(request):
    if request.session.has_key('usernameM'):
        usernameadmin = request.session['usernameM']
    if request.session.has_key('usernameM1'):
        usernameadmin1 = request.session['usernameM1']
    else:
        usernameadmin = "MANAGER"
    edepartment1=Branch.objects.values('country').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'mem':mem}
    return render(request, 'MANmarketing.html', context)

def MANPromarketing(request):
    if request.session.has_key('usernameM'):
        usernameadmin = request.session['usernameM']
    if request.session.has_key('usernameM1'):
        usernameadmin1 = request.session['usernameM1']
    else:
        usernameadmin = "MANAGER"
    edepartment1=regdetails.objects.filter(designation='TL')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'mem':mem}
    return render(request, 'MANPromarketing.html', context)

def manpromarketadd(request):
    if request.session.has_key('usernameM'):
        usernameadmin = request.session['usernameM']
    if request.session.has_key('usernameM1'):
        usernameadmin1 = request.session['usernameM1']
    else:
        usernameadmin = "MANAGER"
    college2 = manproductmarketing(tlname=request.POST['country'],
            proname=request.POST['proname'],
            newtarget=request.POST['target'],
            descri=request.POST['des'],
            siteurl=request.POST['status'])
    college2.save()
    count = 0
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem, 'count': count}
    return render(request, 'admindetailsadded.html',context)

def MANservices(request):
    if request.session.has_key('usernameM'):
        usernameadmin = request.session['usernameM']
    if request.session.has_key('usernameM1'):
        usernameadmin1 = request.session['usernameM1']
    else:
        usernameadmin = "MANAGER"
    edepartment1=Branch.objects.values('country').distinct()
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'mem':mem}
    return render(request, 'MANservices.html', context)

def MANrecru(request):
    if request.session.has_key('usernameM'):
        usernameadmin = request.session['usernameM']
    if request.session.has_key('usernameM1'):
        usernameadmin1 = request.session['usernameM1']
    else:
        usernameadmin = "MANAGER"
    edepartment1=Branch.objects.values('country').distinct()
    edepartment2=regdetails.objects.filter(designation='TL')
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context={'edepartments':edepartment1,'mem':mem,'edepartments2':edepartment2}
    return render(request, 'MANrecru.html', context)

def manrecruadd(request):
    if request.session.has_key('usernameM'):
        usernameadmin = request.session['usernameM']
    if request.session.has_key('usernameM1'):
        usernameadmin1 = request.session['usernameM1']
    else:
        usernameadmin = "TL"
    college2 = recrutement(country=request.POST['country'],
            city=request.POST['city'],
            brnch=request.POST['brnch'],
            tlname=request.POST['tl'],
            post=request.POST['post'],
            qualification=request.POST['qualification'],
            vacancies=request.POST['vacancies'],
            des=request.POST['des'],
            date=datetime.now())
    college2.save()
    count = 0
    mem = regdetails.objects.filter(designation=usernameadmin).filter(name=usernameadmin1)
    context = {'mem':mem, 'count': count}
    return render(request, 'admindetailsadded.html',context)

def sidebarnew(request):
    return render(request,'sidebarnew.html')
#----------------Marketing Section---------------------------------------------------------------------------------------------------    
