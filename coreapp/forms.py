from django import forms
from .models import internship
from .models import regdetails
from .models import im
from .models import admingivetask
from django.forms import ModelForm
from .models import Register
from .models import HRtasks
from .models import admingivetask
from .models import mangivetasks
from  .models import hrprojectsgive
from .models import TeamLeadweeklytask
from .models import drrpayment
'''class ImageForm(forms.ModelForm):
    class Meta:
        model = internship
        fields = ['college', 'regno', 'studname', 'platform', 'department','startdate','enddate','refid','payment','country','branch','course','email','mobile','img']
'''
class SearchForm(forms.ModelForm):
    class Meta:
        model = regdetails
        fields = ['name','email']
class SearchintForm(forms.ModelForm):
    class Meta:
        model = internship
        fields = ['studname','email']

class ImageFormadmin(forms.ModelForm):
    class Meta:
        model = im
        fields = ['img','idproof','name','college','regno','platform','department','startdate','enddate','refid','payment','country','branch','course','email','mobile']

class FileForm(forms.ModelForm):
    class Meta:
        model = admingivetask
        fields = ['date','desc','attach1','branch']

class ViewForm(forms.ModelForm):
    class Meta:
        model = im
        fields = ['img','idproof','name','platform','startdate','enddate','course','email','mobile']


class RegisterForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your full name...'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your email...'}))
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your phone number...'}))

    class Meta:
        model = Register
        fields = '__all__'


class ImageFormHR(forms.ModelForm):
    class Meta:
        model=HRtasks
        fields=("description","attach")


class ImageFormManager(forms.ModelForm):
    class Meta:
        model=admingivetask
        fields=("task","attach")

class QrFileForm(forms.ModelForm):
    class Meta:
        model = regdetails
        fields = ['name','employeeimage']

class RegnewForm(forms.ModelForm):
    class Meta:
        model = regdetails
        fields = ['name','email','mobile','dateofappoinment','department','designation','country','city','branch','password','employeeimage','signature','idproof','employeeid','confirmsalary']


class TLTaskFileForm(forms.ModelForm):
    class Meta:
        model = mangivetasks
        fields = ['json_screenshot','description']

class TLProjectFileForm(forms.ModelForm):
    class Meta:
        model = hrprojectsgive
        fields = ['json_screenshot','description','report','nameid']

class DRTaskFileForm(forms.ModelForm):
    class Meta:
        model = TeamLeadweeklytask
        fields = ['json_screenshot','description']

class DRProjectFileForm(forms.ModelForm):
    class Meta:
        model = hrprojectsgive
        fields = ['json_screenshot','description','report','nameid']

class DRpaymentForm(forms.ModelForm):
    class Meta:
        model = drrpayment
        fields = ['amountpaid','paymentdate','receipt']

class VForm(forms.ModelForm):
    class Meta:
        model = regdetails
        fields = ('name','employeeimage','idproof','signature','email','mobile','altermobile','dadname','momname','presntadd1','presntadd2','presntadd3','presntadd4','permanantadd1','permanantadd2','permanantadd3','permanantadd4','schhol','aggregateschool','degreeug','streamug','passoutyearug','aggregateug','degreepg','intenshipdetails','intenshipduration','intenshipcertification','onlinetrainingdetails','onlinetrainingduration','onlinetrainingcertification','projecttitle','desc','url','projectduration','skill1','skill2','skill3')

class TSProjectFileForm(forms.ModelForm):
    class Meta:
        model = hrprojectsgive
        fields = ['json_testerscreenshot','testerdescr','prostatus','delay']

class TSTaskFileForm(forms.ModelForm):
    class Meta:
        model = mangivetasks
        fields = ['json_testerscreenshot','testerdescr']
