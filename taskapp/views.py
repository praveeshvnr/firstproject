from datetime import datetime, date

from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context

from django.views.generic import TemplateView
from coreapp.models import User, Assign, acntspayslip, marketingassignwrk
from coreapp.models import UserType, Dcreg, Tlreg, Exereg, Tlshareddatas, Dcattendance,  Dcapplyleave, Tltasks, \
    Tlshareddatas2, Tlattendance, Tlreport, Tlapplyleave, Exetasks2, Exetasks3, Execompletedtasks, Exeattendance, \
    Exereport, Exeapplyleave, leavereq, hrreport
from coreapp.models import regdetails, mangivetasks, auth_details, HRtasks, employeeattendance


def index(request):
    return render(request, 'taskapp/index.html')


def dc_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        password = request.POST['password']
        try:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('dc_reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('dc_reg')
            else:
                user = User.objects.create_user(first_name=name, username=username, email=email, password=password,
                                                last_name=0)
                user.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "data collector"
                usertype.save()
                reg = Dcreg()
                reg.user = user
                reg.address = address
                reg.contact = contact
                reg.save()
                return render(request, 'taskapp/index.html')
        except:
            # messages="Enter another username"
            return render(request, 'taskapp/dcreg.html')
    return render(request, 'taskapp/dcreg.html')


def tl_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        password = request.POST['password']
        try:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('tl_reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('tl_reg')
            else:
                user = User.objects.create_user(first_name=name, username=username, email=email, password=password,
                                                last_name=0)
                user.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "team lead"
                usertype.save()
                reg = Tlreg()
                reg.user = user
                reg.address = address
                reg.contact = contact
                reg.save()
                return render(request, 'taskapp/index.html')
        except:
            # messages="Enter another username"
            return render(request, 'taskapp/tlreg.html')
    return render(request, 'taskapp/tlreg.html')


def exe_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        password = request.POST['password']
        try:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('exe_reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('exe_reg')
            else:
                user = User.objects.create_user(first_name=name, username=username, email=email, password=password,
                                                last_name=0)
                user.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "executive"
                usertype.save()
                reg = Exereg()
                reg.user = user
                reg.address = address
                reg.contact = contact
                reg.save()
                return render(request, 'taskapp/index.html')
        except:
            # messages="Enter another username"
            return render(request, 'taskapp/exereg.html')
    return render(request, 'taskapp/exereg.html')


class LoginView(TemplateView):
    template_name = 'taskapp/dclogin.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print('1')

            if UserType.objects.get(user_id=user.id).type == "data collector":
                return redirect('profile')
            elif UserType.objects.get(user_id=user.id).type == "team lead":
                return redirect('tl1')
            else:
                return redirect('exe1')

        else:
            print('5')
            return render(request, 'taskapp/dclogin.html', {'message': "Invalid Username or Password"})


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    else:
        usernamedata1 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    return render(request, 'datacol/indexdc1.html', {'mem': mem})


def dcmypropie_chart(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    else:
        usernamedatal = "dummy"
    labels = []
    data = []
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    queryset = regdetails.objects.filter(designation=usernamedatal)
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
    return render(request, 'datacol/indexdc1.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })


def profile2(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    else:
        usernamedatal = "dummy"
    labels = []
    data = []
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    queryset = regdetails.objects.filter(designation=usernamedatal)
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
    return render(request, 'datacol/indexdc2.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })


def tasks(request):
    return render(request, 'datacol/indexdc3.html')


def dctaskspage(request):
    return render(request, 'datacol/dctaskspage.html')


def dctaskproduct(request):
    return render(request, 'datacol/dctaskproduct.html')


def dctasksoft(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    object = Tltasks.objects.all().filter(branch=usernamedata2).filter(marktype="Service").filter(sharetodc=True)
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    return render(request, 'datacol/dctasksoft.html', {'results':object, 'mem': mem})

def dctaskservices(request):
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    emp_id = request.GET.get('empid')
    object = Tltasks.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem, 'results': object}
    return render(request, 'datacol/dctaskservices.html', context)

def dcservicesshare(request):
    return render(request, 'datacol/dcservicesshare.html')

def dctaskrecruitment(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    object = Tltasks.objects.all().filter(branch=usernamedata2).filter(marktype="Recruitment").filter(sharetodc=True)
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    return render(request, 'datacol/dctaskrecritment.html', {'results':object, 'mem': mem})

def dcrecruitmenttask(request):
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    emp_id = request.GET.get('empid')
    object = Tltasks.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem, 'results': object}
    return render(request, 'datacol/dcrecruitmenttask.html', context)

def dcrecruitmentshare(request):
    return render(request, 'datacol/dcrecruitmentshare.html')

def tasks2(request):
    return render(request, 'datacol/indexdc4.html')


def taskstable(request,pk):
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    tasktable = Tlshareddatas.objects.filter(user__id=pk)
    # import pdb;pdb.set_trace()
    mem = regdetails.objects.filter(designation__iexact = 'Marketing Executive').values()
    context = {'names': tasktable, 'mem': mem}
    return render(request, 'datacol/indexdc5.html',context)


# id = request.GET['id']
#     print('hello111')
#     object = UserType.objects.filter(user_id=id)

def assign(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        # res = Tlshareddatas.objects.filter(id=id)
        # context = {'res': res, 'name': name}
        # for key, value in context.items():
        #     print(key, value)
        # context['res'] = res
        # context['name'] = name
        # setattr(context, res, name)
        ob = Assign()
        ob.name = name
        ob.status = 'null'
        ob.Tlshareddatas_id_id = id
        ob.save()
        return render(request, 'datacol/indexdc3.html', {'messages': messages})
    else:
        return render(request, 'datacol/indexdc5.html')


def shared(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    object = Tltasks.objects.all()
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    return render(request, 'datacol/indexdc6.html', {'mem': mem, 'results': object})


def shared2(request):
    return render(request, 'datacol/indexdc7.html')


def shared3(request,pk):
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    shared3 = Tlshareddatas.objects.filter(user__id=pk)
    mem = regdetails.objects.filter(designation__iexact = 'Marketing Executive').values()
    context = {'results':shared3, 'mem':mem}
    return render(request, 'datacol/indexdc8.html', context)


def shared4(request):
    if request.method == "POST":
        id = request.POST['resname']
        results = Tlshareddatas.objects.get(id=id)

        print("1111111111111", id)

        tmname = request.POST['name']
        print("2222222222", tmname)
        results.tmexecutive = tmname
        results.save()
        # return redirect('shared3')
        return redirect('tlshared2')
    # else:
    #     return render(request,'datacol/indexdc5.html')


def marktexe(request):
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    else:
        usernamedatal = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    object = regdetails.objects.filter(designation='Marketing Executive')
    context = {'mem': mem, 'results': object}
    return render(request, 'datacol/indexdc9.html', context)



def marktexe2(request):
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    emp_id = request.GET.get('empid')
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    object = regdetails.objects.filter(designation='Marketing Executive').filter(id=emp_id)
    context = {'mem': mem, 'results': object}
    return render(request, 'datacol/indexdc10.html', context)


def attendance(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    else:
        usernamedata1 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem}
    print('hy')
    return render(request, 'datacol/indexdc11.html', context)


def attendance2(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata1 = "dummy"
    print('hai')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = employeeattendance.objects.all().filter(employee=usernamedata1).filter(branch=usernamedata2)
    # names = employeeattendance.objects.filter(date__range=(dept_id, desig_id)).all().filter(branch=usernamedata2).filter(
    #     employee=usernamedata1)
    print(names.values('status', 'date', 'login', 'logout'))
    return render(request, 'datacol/indexdc12.html', {'names': names})

def reportissue(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem}
    return render(request, 'datacol/indexdc13.html', context)


def reportissue2(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    names = hrreport.objects.filter(reportedby=usernamedata1).filter(branch=usernamedata2).all
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'results': names, 'mem': mem}
    return render(request, 'datacol/indexdc14.html', context)
    # object = Report.objects.filter(fk_created_id=request.user.id).values().order_by('-id')
    # return render(request, 'datacol/indexdc14.html', {'results':object})

def reportissue3(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    emp_id = request.GET.get('empid')
    empid = hrreport.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    return render(request, 'datacol/indexdc15.html', {'emp': empid, 'mem': mem})


def reportissue4(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernameMtl2 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal, name=usernamedata1)
    context = {'mem': mem}
    return render(request, 'datacol/indexdc16.html')
    # if request.method == 'POST':
    #     # import pdb; pdb.set_trace()
    #     results = Report(reportissue=request.POST['reportissue'],fk_created_id = request.user.id)
    #     results.save()
    #     return redirect('reportissue')
    #     # user_id = request.GET.get('userid')
    #     # userid = Report.objects.filter(id=user_id)
    #     # return render(request,'datacol/indexdc17.html', {'user': userid})
    # else:
    #     return render(request,'datacol/indexdc16.html')


def reportissue5(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata1 = "dummy"
    member = hrreport(issue=request.POST['issue'], date=datetime.now(), reportedby=usernamedata1,
                      designation=usernamedatal, branch=usernamedata2)
    member.save()
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem}
    return render(request, 'datacol/indexdc17.html', context)

def payments(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    else:
        usernamedata1 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem}
    return render(request, 'datacol/indexdc18.html', context)


def payments2(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    else:
        usernamedata1 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem}
    return render(request, 'datacol/indexdc19.html', context)


def paymentstable(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    else:
        usernamedata1 = "dummy"
    pay = request.GET.get('salary')
    pay1 = acntspayslip.objects.filter(dateef=pay).filter(ename=usernamedata1)
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    return render(request, 'datacol/indexdc20.html', {'pays':pay1, 'mem': mem})


def applyleave(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata1 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem}
    return render(request, 'datacol/indexdc21.html', context)


def applyleave2(request):
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedatal = "dummy"
    member = leavereq(assignedBy=usernamedata1, leavefrom=request.POST['leavefrom'], leaveto=request.POST['leaveto'],
                      reason=request.POST['reason'],
                      department=usernamedatal, branch=usernamedata2)
    member.save()
    return render(request, 'datacol/indexdc21.html')


def applyleave3(request):
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata1 = "dummy"
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'mem': mem}
    return render(request, 'datacol/indexdc23.html', context)


def applyleave4(request):
    if request.session.has_key('usernamedatal'):
        usernamedatal = request.session['usernamedatal']
    if request.session.has_key('usernamedata1'):
        usernamedata1 = request.session['usernamedata1']
    if request.session.has_key('usernamedata2'):
        usernamedata2 = request.session['usernamedata2']
    else:
        usernamedata2 = "dummy"
    names = leavereq.objects.filter(branch=usernamedata2).filter(assignedBy=usernamedata1)  # all()
    mem = regdetails.objects.filter(designation=usernamedatal).filter(name=usernamedata1)
    context = {'names': names, 'mem': mem}
    return render(request, 'datacol/indexdc24.html', context)


def tl1(request):
    # import pdb; pdb.set_trace()
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    else:
        usernameMtl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    return render(request, 'teamlead/indextl1.html', {'mem': mem})


# def tl2(request):
#     if request.session.has_key('usernameMtl1'):
#         usernameMtl1 = request.session['usernameMtl1']
#     if request.session.has_key('usernameMtl'):
#         usernameMtl = request.session['usernameMtl']
#     else:
#         usernameMtl1 = "dummy"
#     mem=regdetails.objects.filter(designation=usernameMtl) .filter(name=usernameMtl1)
#     return render(request,'teamlead/indextl2.html',{'mem':mem})


# def tl1(request):
#     return render(request,'teamlead/indextl1.html')

def Mtlmypropie_chart(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    else:
        usernamehr = "dummy"
    labels = []
    data = []
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    queryset = regdetails.objects.filter(designation=usernameMtl)
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
    return render(request, 'teamlead/indextl1.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })


def tl2(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    else:
        usernameMtl = "dummy"
    labels = []
    data = []
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    queryset = regdetails.objects.filter(designation=usernameMtl)
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
    return render(request, 'teamlead/indextl2.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })
    # return render(request,'teamlead/indextl2.html')


def tltask(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    return render(request, 'teamlead/indextl3.html', {'mem': mem})


def tltaskspage(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/tltaskspage.html', context)


def tltaskproduct(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    names = HRtasks.objects.all().filter(branch='infox cochin')
    # names = HRtasks.objects.all()
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'names': names, 'mem': mem}
    return render(request, 'teamlead/tltaskproduct.html', context)


def tltaskrecruitment(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    print(request.session)
    print(request.session['useremail'])
    object = Tltasks.objects.filter(branch=usernameMtl2).filter(marktype="Recruitment").filter(email=request.session['useremail'])
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    print(usernameMtl1)
    return render(request, 'teamlead/tltaskrecruitment.html', {'results':object, 'mem': mem})


def tltaskservice(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    object = Tltasks.objects.all().filter(branch=usernameMtl2).filter(marktype="Service").filter(email=request.session['useremail'])
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    return render(request, 'teamlead/tltaskservice.html', {'results': object, 'mem': mem})


def tltask2(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl4.html', context)



def tlshared4(request):
    if request.method == "POST":
        id = request.POST['resname']
        results = Tltasks.objects.get(id=id)

        print("1111111111111", id)

        tmname = request.POST['name']
        print("2222222222", tmname)
        results.tmexecutive = tmname
        results.save()
        return redirect('tltasktable')


def tltask4(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl6.html', context)


def tltask5(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl7.html', context)


def tltaskserviceshare(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    emp_id = request.GET.get('empid')
    object = Tltasks.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem, 'results': object}
    return render(request, 'teamlead/tltaskserviceshare.html', context)



def tltaskservicedone(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/tltaskservicedone.html', context)


def tltask6(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    emp_id = request.GET.get('empid')
    object = Tltasks.objects.get(id=emp_id)
    object.sharetodc = True
    object.save()
    object = Tltasks.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem, 'results': object}
    return render(request, 'teamlead/indextl8.html', context)


def tltask6shared(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    emp_id = request.GET.get('empid')
    object = Tltasks.objects.get(id=emp_id)
    object.sharetodc = True
    object.save()
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/tltask6shared.html', context)


def tltask7(request,pk):
    task = get_object_or_404(Tltasks,pk=pk)
    if request.method == 'POST':

        print(task)
        results = Tlshareddatas(name=request.POST['name'], email=request.POST['email'],
                                qualification=request.POST['qualification'], location=request.POST['location'],
                                contact=request.POST['contact'], user=task)
        results.save()
        return redirect('tltask7table',pk=pk)
    else:
        context={'result':{'id':pk}}
        return render(request, 'teamlead/indextl11.html', context)


def tltask7table(request,pk):
    task = get_object_or_404(Tltasks, pk=pk)
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    fk_id = request.GET.get('fk_assigned')
    # emp_id = request.GET.get('empid')
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    object = Tlshareddatas.objects.filter(user=task)
    # object = Tltasks.fk_assigned.marktype
    context = {'mem': mem, 'results': object, 'taskid':pk}
    return render(request, 'teamlead/indextl11update.html', context)


# def tlsaved(request):
#     if request.session.has_key('usernameMtl'):
#         usernameMtl = request.session['usernameMtl']
#     if request.session.has_key('usernameMtl1'):
#         usernameMtl1 = request.session['usernameMtl1']
#     else:
#         usernameMtl = "dummy"
#     # mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
#     mem = regdetails.objects.filter(designation__iexact='Marketing Executive').filter(name=usernameMtl1).values()
#     dates = Tlshareddatas.objects.values_list('updated_at__date').distinct()
#     context = {'mem': mem, 'date': dates}
#     return render(request, 'teamlead/indextl9.html', context)

def tlsaved(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    tlshareddata = Tlshareddatas.objects.filter(status='Interested').values_list('user', flat=True)
    object = Tltasks.objects.filter(id__in=tlshareddata).filter(email=request.session['useremail'])
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    return render(request, 'teamlead/indextl9.html', {'mem': mem , 'results': object})

# def tltasktable(request,date):
#     if request.session.has_key('usernameMtl'):
#         usernameMtl = request.session['usernameMtl']
#     if request.session.has_key('usernameMtl1'):
#         usernameMtl1 = request.session['usernameMtl1']
#     if request.session.has_key('usernameMtl2'):
#         usernameMtl2 = request.session['usernameMtl2']
#     else:
#         usernameMtl2 = "dummy"
#     tasks = Tlshareddatas.objects.filter(updated_at__date=date).exclude(tmexecutive='')
#     mem = regdetails.objects.filter(designation__iexact = 'Marketing Executive').values()
#     context = {'names':tasks, 'mem':mem}
#     return render(request, 'teamlead/indextl5.html', context)


def tltasktable(request,pk):
    task = get_object_or_404(Tltasks,pk=pk)
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    # fk_id = request.GET.get('fk_assigned')
    mem = regdetails.objects.filter(designation__iexact = 'Marketing Executive').filter(name=usernameMtl1).values()
    object = Tlshareddatas.objects.filter(user__id=pk).filter(status='Interested').filter(user=task).exclude(tmexecutive='')
    context = {'mem':mem, 'results':object, 'taskid':pk}
    return render(request, 'teamlead/indextl5.html', context)




def tlshared(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    # object = Tltasks.objects.all().filter(description=usernameMtl2).filter(marktype=usernameMtl3)
    tlshareddata = Tlshareddatas.objects.filter(user__isnull=False).values_list('user',flat=True)
    print(tlshareddata)

    object = Tltasks.objects.filter(email=request.session['useremail']).filter(id__in=tlshareddata)
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    return render(request, 'teamlead/indextl10.html', {'results': object, 'mem': mem})


def tlsharedtable(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    object = Tlshareddatas2.objects.all()
    context = {'mem': mem, 'results': object}
    return render(request, 'teamlead/indextl28.html', context)


def tlshared2(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    object = Tlshareddatas.objects.all()
    context = {'mem': mem, 'results': object}
    return render(request, 'teamlead/indextl29.html', context)


def tlshared3(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    # object = Tlshareddatas2.objects.all()
    return render(request, 'teamlead/indextl12.html', context)


def tldc(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    else:
        usernameMtl = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    object = regdetails.objects.filter(designation='Data Collector')
    context = {'mem': mem, 'results': object}
    return render(request, 'teamlead/indextl13.html', context)


def tldc2(request):
    # id = request.GET.get('id')
    # object = regdetails.objects.filter(id=id)
    # return render(request, 'teamlead/indextl14.html', {'results': object})

    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    emp_id = request.GET.get('empid')
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    object = regdetails.objects.filter(designation='Data Collector').filter(id=emp_id)
    context = {'mem': mem, 'results': object}
    return render(request, 'teamlead/indextl14.html', context)


def tlattendance(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    else:
        usernameMtl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    print('hy')
    return render(request, 'teamlead/indextl15.html', context)


def tlattendance2(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl1 = "dummy"
    print('hai')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = employeeattendance.objects.all().filter(employee=usernameMtl1).filter(branch=usernameMtl2)
    # names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).all().filter(employee=usernameMtl1).filter(branch=usernameMtl2)
    print(names.values('status', 'date', 'login', 'logout'))
    return render(request, 'teamlead/indextl16.html', {'names': names})


def tlreport(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl17.html', context)


def tlreport2(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    names = hrreport.objects.filter(reportedby=usernameMtl1).filter(branch=usernameMtl2).all
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    # object = Tlreport.objects.filter(fk_created_id=request.user.id).values().order_by('-id')
    context = {'mem': mem, 'results': names}
    return render(request, 'teamlead/indextl18.html', context)


def tlreport3(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    emp_id = request.GET.get('empid')
    empid = hrreport.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    return render(request, 'teamlead/indextl19.html', {'emp': empid, 'mem': mem})

    # id = request.GET['id']
    # object = Tlreport.objects.filter(id=id)
    # return render(request, 'teamlead/indextl19.html', {'results': object})


def tlreport4(request):
    # import pdb; pdb.set_trace()
    # if request.method == 'POST':
    #     # import pdb; pdb.set_trace()
    #     # print('userId:'+request.user.id)
    #     results = Tlreport(reportissue=request.POST['reportissue'],fk_created_id = request.user.id)
    #     results.save()
    #     return redirect('tlreport')
    # else:
    #     return render(request, 'teamlead/indextl20.html')

    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl, name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl20.html', context)


def tlreport5(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl1 = "dummy"
    member = hrreport(issue=request.POST['issue'], date=datetime.now(), reportedby=usernameMtl1,
                      designation=usernameMtl, branch=usernameMtl2)
    member.save()
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl21.html', context)


def tlpayments(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    else:
        usernameMtl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl22.html', context)


def tlpayments2(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    else:
        usernameMtl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl23.html', context)


def tlpayments3(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    else:
        usernameMtl1 = "dummy"
    pay = request.GET.get('salary')
    pay1 = acntspayslip.objects.filter(dateef=pay).filter(ename=usernameMtl1)
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    return render(request, 'teamlead/indextl24.html', {'mem': mem, 'pays': pay1})


def tlapply(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl25.html', context)



def tlapply1(request):
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl = "dummy"
    member = leavereq(assignedBy=usernameMtl1, leavefrom=request.POST['leavefrom'], leaveto=request.POST['leaveto'],
                      reason=request.POST['reason'],
                      department=usernameMtl, branch=usernameMtl2)
    member.save()
    return render(request, 'teamlead/indextl25.html')


def tlapply2(request):
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'mem': mem}
    return render(request, 'teamlead/indextl26.html', context)

    # if request.method == 'POST':
    #     results = Tlapplyleave(leavefrom=request.POST['leavefrom'],leaveto=request.POST['leaveto'],reason=request.POST['reason'],fk_created_id = request.user.id)
    #     results.save()
    #     return redirect('tlapply3')
    # else:
    #     return render(request,'teamlead/indextl26.html')


def tlapply3(request):
    # object = Tlapplyleave.objects.filter(fk_created_id=request.user.id).values().order_by('-id')
    # return render(request,'teamlead/indextl27.html',{'results': object})

    if request.session.has_key('usernameMtl'):
        usernameMtl = request.session['usernameMtl']
    if request.session.has_key('usernameMtl1'):
        usernameMtl1 = request.session['usernameMtl1']
    if request.session.has_key('usernameMtl2'):
        usernameMtl2 = request.session['usernameMtl2']
    else:
        usernameMtl2 = "dummy"
    names = leavereq.objects.filter(branch=usernameMtl2).filter(assignedBy=usernameMtl1)  # all()
    mem = regdetails.objects.filter(designation=usernameMtl).filter(name=usernameMtl1)
    context = {'names': names, 'mem': mem}
    return render(request, 'teamlead/indextl27.html', context)


def exe1(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    return render(request, 'executive/indexexe1.html', {'mem': mem})


def exemypropie_chart(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexel = "dummy"
    labels = []
    data = []
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    queryset = regdetails.objects.filter(designation=usernameMexel)
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
    return render(request, 'executive/indexexe1.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })


def exe2(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexel = "dummy"
    labels = []
    data = []
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    queryset = regdetails.objects.filter(designation=usernameMexel)
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
    return render(request, 'executive/indexexe2.html', {
        'mem': mem,
        'labels': labels,
        'data': data,
    })


def exetask(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe2 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    object = Tltasks.objects.all()
    context = {'mem': mem , 'results': object}
    return render(request, 'executive/indexexe3.html', context)


def exetask2(request):
    return render(request, 'executive/indexexe4.html')


def exetasktable(request,pk):
    task = get_object_or_404(Tltasks,pk=pk)
    # object = Assign.objects.filter(tlshareddatas_id_id=id)
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    fk_id = request.GET.get('fk_assigned')
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1).values()
    object = Tlshareddatas.objects.filter(tmexecutive=usernameMexe1).filter(user__id=pk).filter(user=task)
    context = {'mem': mem,'names':object, 'taskid':pk}
    return render(request, 'executive/indexexe5.html', context)


def exetasktable2(request,pk):
    print(pk)
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1).values()
    obj = get_object_or_404(Tlshareddatas,pk=pk)
    # obj = Tlshareddatas.objects.filter(pk=pk)
    print('haii')
    obje = Exetasks2.objects.filter(user_id=obj)
    return render(request, 'executive/indexexe6.html', {'results': obj, 'res': obje, 'mem':mem})


def exetasktableupdate(request,pk):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1).values()
    object = Tlshareddatas.objects.get(pk=pk)
    if request.method == 'POST':
        date = request.POST['date']
        status = request.POST['status']
        description = request.POST['description']
        results = Exetasks2(date=date, status=status, description=description, user=object)
        results.save()
        if status == "Interested":
            object.status = status
            object.description = description
            object.save()
        return redirect('exetasktable',pk=object.user.id)
    return render(request, 'executive/indexexe6update.html',{'user_id':pk})


def exetableupdate1(request):
    if request.method == 'POST':

        date = request.POST['date']
        status = request.POST['status']
        description = request.POST['description']
        user_id = request.POST['exid']
        results = Exetasks2(date=date, status=status, description=description, user_id=user_id)
        results.save()
        if status == "Interested":
            object = Tlshareddatas.objects.get(id=user_id)
            object.status = status
            object.description = description
            object.save()
        return redirect('exetasktable')


def exetableupdate22(request):
    if request.method == 'POST':
        results = Exetasks2(date=request.POST['date'], status=request.POST['status'],
                            description=request.POST['description'], user_id=request.POST['exid'])
        # exetasks3 =Exetasks3(user_id=request.POST['exid'],status=request.POST['status'])
        # exetasks3.save()
        results.save()
        return redirect('exetasktable')


def exetasktable3(request,pk):
    object = Exetasks2.objects.filter(status="Interested").filter(user_id__user__id=pk)
    return render(request, 'executive/indexexe7.html', {'results': object, 'taskid':pk})


def exetasktable31(request,pk):
    if request.method == 'POST':
        remark = request.POST['remark']
        print("koko", remark)
        result = Exetasks2.objects.get(id=pk)
        result.remarks = remark
        result.save()
        return redirect(request.META['HTTP_REFERER'])


def exetasktable3update(request):
    if request.method == 'POST':
        results = Exetasks3(name=request.POST['name'], location=request.POST['location'],
                            contact=request.POST['contact'], status=request.POST['status'],
                            remarks=request.POST['remarks'])
        results.save()
        return redirect('exetasktable3')
    else:
        return render(request, 'executive/indexexe7update.html')


def exect(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe2 = "dummy"
    object = Tltasks.objects.all()
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    return render(request, 'executive/indexexe8.html', {'mem': mem , 'results': object})


def execttable(request,pk):
    task = get_object_or_404(Tltasks,pk=pk)
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    # fk_id = request.GET.get('fk_assigned')
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1).values()
    object = Tlshareddatas.objects.filter(tmexecutive=usernameMexe1).filter(user__id=pk).filter(status='Interested').filter(user=task)
    # object = Exetasks2.objects.all()
    context = {'mem':mem, 'results':object, 'taskid':pk}
    return render(request, 'executive/indexexe9.html', context)


def exeattendance(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'mem': mem}
    print('hy')
    return render(request, 'executive/indexexe10.html', context)


def exeattendance2(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe1 = "dummy"
    print('hai')
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print('h')
    names = employeeattendance.objects.all().filter(employee=usernameMexe1).filter(branch=usernameMexe2)
    # names = employeeattendance.objects.filter(date__range=(dept_id,desig_id)).all().filter(employee=usernameMtl1).filter(branch=usernameMtl2)
    print(names.values('status', 'date', 'login', 'logout'))
    return render(request, 'executive/indexexe11.html', {'names': names})


def exereport(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe2 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'mem': mem}
    return render(request, 'executive/indexexe12.html', context)


def exereport2(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe2 = "dummy"
    names = hrreport.objects.filter(reportedby=usernameMexe1).filter(branch=usernameMexe2).all
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    # object = Exereport.objects.filter(fk_created_id=request.user.id).values().order_by('-id')
    context = {'mem': mem, 'results': names}
    return render(request, 'executive/indexexe13.html', context)


def exereport3(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe2 = "dummy"
    emp_id = request.GET.get('empid')
    empid = hrreport.objects.filter(id=emp_id)
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    return render(request, 'executive/indexexe14.html', {'emp': empid, 'mem': mem})


def exereport4(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe2 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'mem': mem}
    return render(request, 'executive/indexexe15.html', context)


def exereport5(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe1 = "dummy"
    member = hrreport(issue=request.POST['issue'], date=datetime.now(), reportedby=usernameMexe1,
                      designation=usernameMexel, branch=usernameMexe2)
    member.save()
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'mem': mem}
    return render(request, 'executive/indexexe16.html', context)


def exepayments(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'mem': mem}
    return render(request, 'executive/indexexe17.html', context)


def exepayments2(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'mem': mem}
    return render(request, 'executive/indexexe18.html', context)

def exepayments3(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    else:
        usernameMexe1 = "dummy"
    pay = request.GET.get('salary')
    pay1 = acntspayslip.objects.filter(dateef=pay).filter(ename=usernameMexe1)
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    return render(request, 'executive/exepayments3.html', {'pays': pay1, 'mem': mem})

def exeapply(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'mem': mem}
    return render(request, 'executive/indexexe19.html', context)

def exeapply1(request):
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexel = "dummy"
    member = leavereq(assignedBy=usernameMexe1, leavefrom=request.POST['leavefrom'], leaveto=request.POST['leaveto'],
                      reason=request.POST['reason'],
                      department=usernameMexel, branch=usernameMexe2)
    member.save()
    return render(request, 'executive/indexexe19.html')

def exeapply2(request):
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe1 = "dummy"
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'mem': mem}
    return render(request, 'executive/indexexe20.html', context)


def exeapply3(request):
    if request.session.has_key('usernameMexel'):
        usernameMexel = request.session['usernameMexel']
    if request.session.has_key('usernameMexe1'):
        usernameMexe1 = request.session['usernameMexe1']
    if request.session.has_key('usernameMexe2'):
        usernameMexe2 = request.session['usernameMexe2']
    else:
        usernameMexe2 = "dummy"
    names = leavereq.objects.filter(branch=usernameMexe2).filter(assignedBy=usernameMexe1)  # all()
    mem = regdetails.objects.filter(designation=usernameMexel).filter(name=usernameMexe1)
    context = {'names': names, 'mem': mem}
    return render(request, 'executive/indexexe21.html', context)


