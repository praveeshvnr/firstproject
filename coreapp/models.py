from django.db import models
import datetime
import os
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField
from django.db.models.deletion import CASCADE, DO_NOTHING
#from django.db.models import JSONField

class Country(models.Model):
    name = models.CharField(max_length=30)
class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
    death=models.PositiveIntegerField()
class empperformance(models.Model):
    name = models.CharField(max_length=200)
    employeeid = models.CharField(max_length=100)
    department = models.CharField(max_length=30)
    Punctuality = models.PositiveIntegerField()
    Performance = models.PositiveIntegerField()
    timelycompletion=models.PositiveIntegerField()
    Creativity = models.PositiveIntegerField()
    extrawork = models.PositiveIntegerField()
    date = models.DateField(max_length=100)

    class Meta:
        db_table = "empperformance"
        

class auth_details(User,models.Model):
    contact = models.CharField(max_length=200, default='00000')    
        
class regdetails(models.Model):
    slno = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=150,blank=True,unique=True)
    email = models.EmailField(max_length=120,blank=True)
    password = models.CharField(max_length=25,default='')
    qualification = models.CharField(max_length=10,default='')
    designation = models.CharField(max_length=20,default='')
    trainer = models.CharField(max_length=150,default='')
    #applieddate = models.CharField(max_length=100,default='')
    regid = models.CharField(max_length=15,default='')
    employeetype = models.CharField(max_length=20,default='')
    employeeid = models.CharField(max_length=20,default='')
    mobile = models.CharField(max_length=20,default='')
    duration = models.CharField(max_length=15,default='')
    department = models.CharField(max_length=20,default='')
    qr = models.ImageField(max_length=300,null=True,default='')
    dateofappoinment = models.DateField(max_length=150, default='')
    refid = models.CharField(max_length=25, default='')
    payment = models.CharField(max_length=20, default='')
    updatecondition = models.CharField(max_length=20, default='')
    addconditionno = models.CharField(max_length=20, default='')
    branch = models.CharField(max_length=100, default='')
    altermobile = models.CharField(max_length=10, default='',null=True,blank=True)
    employeeimage = models.FileField(upload_to='', default='')
    dadname = models.CharField(max_length=100, default='',null=True,blank=True)
    momname = models.CharField(max_length=100, default='',null=True,blank=True)

    presntadd1 = models.CharField(max_length=100,default='',null=True,blank=True)
    presntadd2 = models.CharField(max_length=100,default='',null=True,blank=True)
    presntadd3 = models.CharField(max_length=100,default='',null=True,blank=True)
    presntadd4 = models.CharField(max_length=100,default='',null=True,blank=True)
    permanantadd1 = models.CharField(max_length=100, default='',null=True,blank=True)
    permanantadd2 = models.CharField(max_length=100, default='',null=True,blank=True)
    permanantadd3 = models.CharField(max_length=100, default='',null=True,blank=True)
    permanantadd4 = models.CharField(max_length=100, default='',null=True,blank=True)
    schhol = models.CharField(max_length=100, default='',null=True,blank=True)
    aggregateschool = models.CharField(max_length=100, default='',null=True,blank=True)
    viewcertficateplustwo = models.FileField(upload_to='',default='')
    degreeug = models.CharField(max_length=100, default='',null=True,blank=True)
    streamug = models.CharField(max_length=100, default='',null=True,blank=True)
    passoutyearug = models.CharField(max_length=100, default='',null=True,blank=True)
    aggregateug = models.CharField(max_length=100, default='',null=True,blank=True)
    viewcertficateug = models.FileField(upload_to='',default='')
    degreepg = models.CharField(max_length=100, default='',null=True,blank=True)
    viewcertficatepg = models.FileField(upload_to='',default='')
    intenshipdetails = models.CharField(max_length=100, default='',null=True,blank=True)
    intenshipduration = models.CharField(max_length=100, default='',null=True,blank=True)
    intenshipcertification = models.CharField(max_length=100, default='',null=True,blank=True)
    onlinetrainingdetails = models.CharField(max_length=100, default='',null=True,blank=True)
    onlinetrainingduration = models.CharField(max_length=100, default='',null=True,blank=True)
    onlinetrainingcertification = models.CharField(max_length=100, default='',null=True,blank=True)
    projecttitle = models.CharField(max_length=100, default='',null=True,blank=True)
    desc = models.CharField(max_length=100, default='',null=True,blank=True)
    url = models.CharField(max_length=100, default='',null=True,blank=True)
    projectduration = models.CharField(max_length=100, default='',null=True,blank=True)
    skill1 = models.CharField(max_length=100, default='',null=True,blank=True)
    skill2 = models.CharField(max_length=100, default='',null=True,blank=True)
    skill3 = models.CharField(max_length=100, default='',null=True,blank=True)
    idproof = models.FileField(upload_to='',default='')
    photo = models.FileField(upload_to='',default='')
    signature = models.FileField(upload_to='',default='')
    projectdesc = models.CharField(max_length=100, default='')
    addcondition = models.CharField(max_length=100, default='')
    certfanddesig = models.CharField(max_length=100, default='')
    platform = models.CharField(max_length=100, default='')
    intenshipstart = models.CharField(max_length=100, default='')
    intenshipend = models.CharField(max_length=100, default='')
    dateofrelieve = models.CharField(max_length=150, default='')
    dob = models.CharField(max_length=100, default='')
    dispname = models.CharField(max_length=100, default='')
    taxregime = models.CharField(max_length=100, default='')
    pan = models.CharField(max_length=200, default='')
    aadhar = models.CharField(max_length=100, default='')
    uan = models.CharField(max_length=100, default='')
    pf = models.CharField(max_length=100, default='')
    eps = models.CharField(max_length=100, default='')
    datepf = models.CharField(max_length=100, default='')
    pr = models.CharField(max_length=100, default='')
    esi = models.CharField(max_length=100, default='')
    esiname = models.CharField(max_length=100, default='')
    contractstart = models.CharField(max_length=100, default='')
    contractexpry = models.CharField(max_length=100, default='')
    blood = models.CharField(max_length=100, default='')
    acntno = models.CharField(max_length=100, default='')
    ifsc = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=100, default='')
    bankname = models.CharField(max_length=100, default='')
    amountpaid = models.CharField(max_length=100, default='')
    pending = models.CharField(max_length=100, default='')
    duedate = models.CharField(max_length=100, default='')
    paymentdate = models.CharField(max_length=100, default='')
    receipt = models.CharField(max_length=100, default='')
    performance = models.CharField(max_length=100, default='')

    empPunctuality = models.CharField(max_length=100, default='')
    empPerformance = models.CharField(max_length=100, default='')
    emptimelycompletion = models.CharField(max_length=100, default='')
    empCreativity = models.CharField(max_length=100, default='')
    empextrawork = models.CharField(max_length=100, default='')
    empattendance = models.CharField(max_length=100, default='')
    empdate = models.CharField(max_length=100, default='')
    o = models.CharField(max_length=100, default='0')
    country = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')

    confirmsalary = models.CharField(max_length=20, default='')
    deduction = models.CharField(max_length=20, default='')
    intensive = models.CharField(max_length=20, default='')
    increment = models.CharField(max_length=20, default='')
    delay = models.CharField(max_length=20, default='')
    totalsalary = models.CharField(max_length=20, default='')

    class Meta:
        db_table = "regdetails"

class hrprojectsgive(models.Model):
    department = models.CharField(max_length=200)
    designation = models.CharField(max_length=150)
    employee = models.CharField(max_length=120)
    platform = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    date = models.DateField(max_length=20,null=True,blank=True)
    duedate = models.DateField(null=True,blank=True)
    description = models.CharField(max_length=2000)
    assignedBy = models.CharField(max_length=120, default='')
    descri = models.CharField(max_length=2000, default='')
    submited = models.CharField(max_length=200, default='')
    report = models.FileField(upload_to='', default='')
    branch = models.CharField(max_length=2000, default='')
    rqstdays = models.CharField(max_length=200, default='')
    reason = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200, default='')
    tester = models.CharField(max_length=200, default='')
    testerok = models.CharField(max_length=200, default='')
    testerdescr = models.CharField(max_length=200, default='')
    json_testerscreenshot = JSONField(blank=True, null=True)
    json_screenshot = JSONField(blank=True, null=True)
    prostatus = models.CharField(max_length=200, default='')
    testerdate = models.DateField(blank=True, null=True,default='2021-01-01')
    nameid = models.CharField(max_length=200, default='0')
    delay = models.CharField(max_length=20, default='')

    class Meta:
        db_table = "hrprojectsgive"
    def __str__(self):
        return self.name
    @property
    def date_diff(self):
        return (self.testerdate - self.duedate).days

class employeeattendance(models.Model):
        department = models.CharField(max_length=200)
        designation = models.CharField(max_length=200,default='')
        employee = models.CharField(max_length=120)
        branch = models.CharField(max_length=200, default='')
        date = models.DateField(max_length=20)
        status=models.CharField(max_length=100)
        login = models.CharField(max_length=200, default='')
        logout = models.CharField(max_length=200, default='')
        class Meta:
            db_table = "employeeattendance"
class hrreport(models.Model):
        issue = models.CharField(max_length=2000)
        date=models.DateField(max_length=20)
        reportedby=models.CharField(max_length=200,default='')
        actiontaken=models.CharField(max_length=2000,default='')
        designation = models.CharField(max_length=120,default='')
        branch = models.CharField(max_length=120, default='')
        submit=models.CharField(max_length=120, default='')
        class Meta:
            db_table = "hrreport"
class mangivetasks(models.Model):
    department = models.CharField(max_length=200)
    designation = models.CharField(max_length=150)
    employee = models.CharField(max_length=120)
    task = models.CharField(max_length=2000)
    date = models.DateField(max_length=20)
    duedate = models.DateField(max_length=20)
    assignedBy = models.CharField(max_length=120)
    description = models.CharField(max_length=2000, default='')
    json_screenshot = JSONField(blank=True, null=True)
    submited = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=200, default='')
    branch = models.CharField(max_length=200, default='')
    tester = models.CharField(max_length=200, default='')
    testerok = models.CharField(max_length=200, default='')
    testerdescr = models.CharField(max_length=200, default='')
    json_testerscreenshot = JSONField(blank=True, null=True)

    class Meta:
        db_table = "mangivetasks"

class leavereq(models.Model):
        department = models.CharField(max_length=200)
        leavefrom = models.DateField(max_length=150)
        leaveto = models.DateField(max_length=120)
        reason = models.CharField(max_length=2000)
        status = models.CharField(max_length=20)
        assignedBy = models.CharField(max_length=120)
        branch = models.CharField(max_length=200, default='')

        class Meta:
            db_table = "leavereq"
class hrattendancet(models.Model):
    hrid = models.CharField(max_length=100)
    hrname = models.CharField(max_length=100)
    date = models.DateField(max_length=20)
    status=models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    logout = models.CharField(max_length=20)
    class Meta:
        db_table = "hrattendancet"

class syllabus(models.Model):
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date = models.DateField(max_length=20)
    duedate=models.DateField(max_length=20)
    reportstatus = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description=models.CharField(max_length=2000)
    topic=models.CharField(max_length=200,default='')
    branch = models.CharField(max_length=200, default='')
    trainer =models.CharField(max_length=200,default='')

    class Meta:
        db_table = "syllabus"
class HRtasks(models.Model):
    task = models.CharField(max_length=2000)
    duedate = models.DateField(max_length=20)
    date = models.DateField(max_length=20)
    description = models.CharField(max_length=2000, default='')
    attach = models.FileField(upload_to='', default='',null=True, blank=True)
    submited = models.CharField(max_length=200, default='')
    status=models.CharField(max_length=20,default='')
    branch = models.CharField(max_length=200, default='')


    class Meta:
        db_table = "HRtasks"
class Execompletedtasks(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    directmarketer=models.CharField(max_length=100)

    class Meta:
        db_table = "Execompletedtasks"
class marketingassignwrk(models.Model):
    marktype = models.CharField(max_length=200)
    markTl = models.CharField(max_length=150)
    url = models.CharField(max_length=120)
    description = models.CharField(max_length=3000)
    proname = models.CharField(max_length=100, default='')
    newtarget = models.CharField(max_length=50, default='')
    servicename=models.CharField(max_length=100,default='')
    payment=models.CharField(max_length=100,default='')
    post=models.CharField(max_length=100,default='')
    qualification=models.CharField(max_length=200,default='')
    vacancies=models.CharField(max_length=200,default='')
    dttask=models.DateField(blank=True,null=True)
    submited=models.CharField(max_length=100,default='')
    branch = models.CharField(max_length=200,default='')

    class Meta:
        db_table = "marketingassignwrk"


#=============================================Accounts module
class acntexpensest (models.Model):
        payee =models.CharField(max_length=100)
        payacnt=models.CharField(max_length=200)
        paymethod =models.CharField(max_length=100)
        paydate=models.CharField(max_length=100)
        refno=models.CharField(max_length=100)
        category=models.CharField(max_length=100)
        description=models.CharField(max_length=100)
        amount =models.CharField(max_length=100)
        tax=models.CharField(max_length=100)
        total=models.CharField(max_length=100, default='')
        class Meta:
            db_table = "acntexpensest"
class acntspayslip(models.Model):
    eno = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    datejoin = models.CharField(max_length=100)
    taxengime = models.CharField(max_length=100)
    incometax = models.CharField(max_length=100)
    uan = models.CharField(max_length=100)
    pf = models.CharField(max_length=100)
    esi = models.CharField(max_length=100)
    pr = models.CharField(max_length=100)
    dateef = models.DateField(max_length=100)
    ename = models.CharField(max_length=100)
    basicpay = models.CharField(max_length=100)
    basictype = models.CharField(max_length=100)
    hrapay = models.CharField(max_length=100)
    hratype = models.CharField(max_length=100)
    conpay = models.CharField(max_length=100)
    contype = models.CharField(max_length=100)
    propay = models.CharField(max_length=100)
    protype = models.CharField(max_length=100)
    acntno = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    netamt = models.CharField(max_length=100, default='')
    basic = models.CharField(max_length=100, default='')
    hra = models.CharField(max_length=100, default='')
    con = models.CharField(max_length=100, default='')
    pro = models.CharField(max_length=100, default='')
    uan = models.CharField(max_length=100, default='')
    leavesno = models.CharField(max_length=100, default='')
    totalearning = models.CharField(max_length=100, default='')
    totaldeduction = models.CharField(max_length=100, default='')

    class Meta:
        db_table = "acntspayslip"
class acntreceipt (models.Model):
        name =models.CharField(max_length=100)
        department=models.CharField(max_length=200)
        designation =models.CharField(max_length=100)
        amountpaid=models.CharField(max_length=100)
        pending=models.CharField(max_length=100)
        duedate=models.CharField(max_length=100)
        paymentdate =models.CharField(max_length=100)
        received=models.CharField(max_length=100)
        class Meta:
            db_table = "acntreceipt"
#=====================================Admin=====================================
class Branch(models.Model):
    branch = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    pin = models.CharField(max_length=100)
    class Meta:
        db_table = "Branch"
    def __str__(self):
        return self.branch+""+self.country+""+self.state+""+self.city+""+self.area+""+self.pin

class college(models.Model):
    collegename = models.CharField(max_length=100)
    class Meta:
        db_table = "college"
    def __str__(self):
        return self.collegename+""
class internship(models.Model):
    college = models.CharField(max_length=100)
    regno = models.CharField(max_length=20)
    studname = models.CharField(max_length=25)
    platform = models.CharField(max_length=20)
    department = models.CharField(max_length=25)
    startdate = models.CharField(max_length=20)
    enddate = models.CharField(max_length=20)
    refid = models.CharField(max_length=20)
    payment = models.CharField(max_length=25)
    country = models.CharField(max_length=20)
    branch = models.CharField(max_length=25)
    course = models.CharField(max_length=25,default='')
    email = models.CharField(max_length=250,default='')
    mobile = models.CharField(max_length=20,default='')
    img = models.ImageField(upload_to='images/',default='')
    class Meta:
        db_table = "internship"
    def __str__(self):
        return self.college+""+self.regno+""+self.studname+""+self.platform+""+self.department+""+self.startdate+""+self.enddate+""+self.refid+""+self.payment+""+self.country+""+self.branch

class proandmarkng(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    brnch = models.CharField(max_length=100)
    proname = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    date=models.DateField(max_length=20)

    class Meta:
        db_table = "productmarketing"

class service(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    brnch = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    date=models.DateField(max_length=20)
    class Meta:
        db_table = "service"

class recrutement(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    brnch = models.CharField(max_length=100)
    tlname = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    vacancies = models.CharField(max_length=100)
    des = models.CharField(max_length=100)
    date=models.DateField(max_length=20)
    class Meta:
        db_table = "recrutement"
class select(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    class Meta:
        db_table = "select"
class admingivetask(models.Model):
    date = models.CharField(max_length=100)
    duedate = models.CharField(max_length=100,default='')
    desc = models.CharField(max_length=1000)
    attach = models.FileField(upload_to='', default='', null=True, blank=True)
    attach1 = models.FileField(upload_to='',default='', null=True, blank=True)
    task = models.CharField(max_length=2000, default='')
    submited = models.CharField(max_length=200, default='')
    branch = models.CharField(max_length=200, default='')
    class Meta:
        db_table = "admingivetask"

class managerattendance(models.Model):
    date = models.DateField(max_length=20)
    status = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    logout = models.CharField(max_length=20)
    branch = models.CharField(max_length=200, default='')    
    class Meta:
        db_table = "managerattendance"
class viewdata(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    class Meta:
        db_table = "viewdata"
#========================================manager===========
class projectextensionrqst(models.Model):
    proId = models.CharField(max_length=200)
    title = models.CharField(max_length=120)
    rqstdays = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    employee = models.CharField(max_length=120)
    reason = models.CharField(max_length=2000)
    branch = models.CharField(max_length=200,default='')

    class Meta:
        db_table = "projectextensionrqst"
class manproductmarketing(models.Model):
    proname = models.CharField(max_length=100)
    newtarget = models.CharField(max_length=100)
    descri = models.CharField(max_length=3000)
    tlname = models.CharField(max_length=100)
    siteurl = models.CharField(max_length=300)
    class Meta:
        db_table = "manproductmarketing"
class viewintenship(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=20)
    clg = models.CharField(max_length=150)
    course = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    startdate = models.CharField(max_length=20)
    enddate = models.CharField(max_length=20)
    idproof = models.CharField(max_length=100)
    photo = models.FileField(upload_to='',default='')
    class Meta:
        db_table = "viewintenship"
class im(models.Model):
    img = models.ImageField(upload_to='images/')
    idproof = models.FileField(upload_to='images/',default='')
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100,default='')
    regno = models.CharField(max_length=20,default='')
    studname = models.CharField(max_length=25,default='')
    platform = models.CharField(max_length=20,default='')
    department = models.CharField(max_length=25,default='')
    startdate = models.CharField(max_length=20,default='')
    enddate = models.CharField(max_length=20,default='')
    refid = models.CharField(max_length=20,default='')
    payment = models.CharField(max_length=25,default='')
    country = models.CharField(max_length=20,default='')
    branch = models.CharField(max_length=25,default='')
    course = models.CharField(max_length=25,default='')
    email = models.CharField(max_length=250,default='')
    mobile = models.CharField(max_length=20,default='')
    class Meta:
        db_table = "im"



def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    #name = models.TextField(max_length=191)
    #price = models.TextField(max_length=50)
    #description = models.TextField(max_length=500, null=True)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100,default='')
    regno = models.CharField(max_length=20,default='')
    studname = models.CharField(max_length=25,default='')
    platform = models.CharField(max_length=20,default='')
    department = models.CharField(max_length=25,default='')
    startdate = models.CharField(max_length=20,default='')
    enddate = models.CharField(max_length=20,default='')
    refid = models.CharField(max_length=20,default='')
    payment = models.CharField(max_length=25,default='')
    country = models.CharField(max_length=20,default='')
    branch = models.CharField(max_length=25,default='')
    course = models.CharField(max_length=25,default='')
    email = models.CharField(max_length=250,default='')
    mobile = models.CharField(max_length=20,default='')
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    idproof = models.ImageField(upload_to=filepath, null=True, blank=True)
    class Meta:
        db_table = "internshipnew"

class Register(models.Model):
    regChoice = (
        ('Self', 'Self'),
        ('Group', 'Group'),
        ('Corporate', 'Corporate'),
        ('Others', 'Others'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,null=True)
    phoneNumber = models.CharField(max_length=20)
    idCard = models.ImageField(null=True)
    regType = models.CharField(max_length=25, choices=regChoice,null=True)
    ticketNo = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "Register"

class Qr(models.Model):
    name = models.CharField(max_length=50)
class TeamLeadweeklytask(models.Model):
    name = models.CharField(max_length=200)
    task = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
    duedate = models.CharField(max_length=200)
    json_screenshot = JSONField(blank=True, null=True)
    description = models.CharField(max_length=3000)
    branch = models.CharField(max_length=200,default='')
    assignedBy = models.CharField(max_length=200,default='')
    submited=models.CharField(max_length=100,default='')
    submitdate = models.CharField(max_length=200,default='')

    class Meta:
        db_table = "TeamLeadweeklytask"  
        
class drrpayment(models.Model):
    duedate = models.CharField(max_length=100, default='')
    payment = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    amountpaid = models.CharField(max_length=200,default='')
    pending = models.CharField(max_length=200,default='')
    paymentdate = models.CharField(max_length=100, default='')
    department = models.CharField(max_length=100, default='')
    receipt = models.FileField(upload_to='', default='', null=True, blank=True)
    branch = models.CharField(max_length=200, default='')
    submited = models.CharField(max_length=200,default='')
    designation = models.CharField(max_length=20,default='')
    mobile = models.CharField(max_length=20,default='')
    duration = models.CharField(max_length=15,default='')
    refid = models.CharField(max_length=25, default='')

    class Meta:
        db_table = "drrpayment"   
        
#=========================new project section======================
class Project(models.Model):
    projectname = models.CharField(max_length=100)
    startdate = models.DateField()
    duedate = models.DateField()
    description = models.CharField(max_length=2000)
    json_attachfile = JSONField(blank=True, null=True,default='')
    branch = models.CharField(max_length=200)
    assignedto = models.CharField(max_length=200,default='')
    assignedby = models.CharField(max_length=200,default='')
    class Meta:
        db_table = "Project"
class PrTasktoTL(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='pro')
    taskname = models.CharField(max_length=2000)
    taskdescri = models.CharField(max_length=2000)
    startdate = models.DateField()
    duedate = models.DateField()
    json_taskattachfile = JSONField(blank=True, null=True)
    assignedto = models.ForeignKey(regdetails,on_delete=models.CASCADE,related_name='namet')
    assignedby = models.ForeignKey(regdetails, on_delete=models.CASCADE,related_name='nameb')
    branch = models.CharField(max_length=200)
    reqdays = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    progress = models.CharField(max_length=100)
    prostatus = models.CharField(max_length=100)
    testerid = models.ForeignKey(regdetails, on_delete=models.CASCADE,related_name='tester')
    department = models.CharField(max_length=50, default='')
    designation = models.CharField(max_length=50, default='')
    class Meta:
        db_table = "PrTasktoTL"

class PrTasktoDR(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='proj')
    task = models.ForeignKey(PrTasktoTL,on_delete=models.CASCADE,related_name='task')
    subtaskname = models.CharField(max_length=2000)
    subdescri = models.CharField(max_length=2000)
    startdate = models.DateField()
    duedate = models.DateField()
    json_taskattachfile = JSONField(blank=True, null=True)
    assignedto = models.ForeignKey(regdetails,on_delete=models.CASCADE,related_name='assignto')
    assignedby = models.ForeignKey(regdetails, on_delete=models.CASCADE,related_name='assignby')
    branch = models.CharField(max_length=200)
    reqdays = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    progress = models.CharField(max_length=100)
    prostatus = models.CharField(max_length=100)
    testerid = models.ForeignKey(regdetails, on_delete=models.CASCADE,related_name='testerr')
    class Meta:
        db_table = "PrTasktoDR"

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='proje',default='')
    task = models.ForeignKey(PrTasktoTL, on_delete=models.CASCADE,related_name='task_s',default='')
    subtask = models.ForeignKey(PrTasktoDR, on_delete=models.CASCADE,related_name='subtask',blank=True, null=True,default='')
    date = models.DateField()
    workdone = models.CharField(max_length=2000,default='')
    json_attachfile = JSONField(blank=True, null=True)
    branch = models.CharField(max_length=200,default='')
    reportto = models.ForeignKey(regdetails,on_delete=models.CASCADE,related_name='assign_to',default='')
    reportedby = models.ForeignKey(regdetails, on_delete=models.CASCADE,related_name='assign_by',default='')
    testerid = models.ForeignKey(regdetails, on_delete=models.CASCADE,related_name='test_er',default='')
    progress = models.CharField(max_length=100,default='')
    prostatus = models.CharField(max_length=100,default='')
    duedate = models.DateField(default='')
    class Meta:
        db_table = "Report"
class Testing(models.Model):
    reportid = models.ForeignKey(Report, on_delete=models.CASCADE,related_name='repo_t',default='')
    task = models.ForeignKey(PrTasktoTL, on_delete=models.CASCADE,related_name='ta_sk')
    subtask = models.ForeignKey(PrTasktoDR, on_delete=models.CASCADE,related_name='sub_task',blank=True, null=True)
    json_attachfile = JSONField(blank=True, null=True)
    testerdescri = models.CharField(max_length=100)
    testerstatus = models.CharField(max_length=100)
    testerid = models.ForeignKey(regdetails, on_delete=models.CASCADE,related_name='test_rr')
    branch = models.CharField(max_length=200)
    date = models.DateField(default='2021-01-01')
    delay = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='projex',default='')
    #duedate = models.ForeignKey(Report,on_delete=models.CASCADE,related_name='duedatee',blank=True, null=True)
    class Meta:
        db_table = "Testing"
    def __str__(self):
        return self.reportid
    @property
    def date_diff(self):
        return (self.date - self.reportid.duedate).days

    def date_diff1(self):
        return (self.date - self.project.duedate).days
       
#=============================developer
class performance(models.Model):
    department= models.CharField(max_length=200)
    trainee= models.CharField(max_length=200)
    attendance= models.CharField(max_length=200)
    punctuality= models.CharField(max_length=200)
    workcompletion= models.CharField(max_length=200)
    performance= models.CharField(max_length=200)
    attitude= models.CharField(max_length=200)
    timecompletion= models.CharField(max_length=200)
    extraworks= models.CharField(max_length=200)
    creativity= models.CharField(max_length=200)
    perfection= models.CharField(max_length=200)
    accuracy= models.CharField(max_length=200)

    class Meta:
        db_table = "performance"

 
#------------ADMIN        
class sample(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    dateofappoinment = models.CharField(max_length=30)
    dateofrelieve = models.CharField(max_length=30)
    performance = models.CharField(max_length=30)
    employeeimage = models.ImageField(upload_to='')
    qr = models.ImageField(max_length=300,null=True)
    class Meta:
        db_table = "sample"        
        
#----------------------MARKETNG--------------
class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class Dcreg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=200, default='00000')
    address = models.CharField(max_length=200, default='00000')


class Exereg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=200, default='00000')
    address = models.CharField(max_length=200, default='00000')


class Tlreg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=200, default='00000')
    address = models.CharField(max_length=200, default='00000')

    # fk_regdetails = models.ForeignKey(regdetails, models.DO_NOTHING, blank=True, null=True)


class Dctasks(models.Model):
    # tasks_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='00000')
    email = models.EmailField(max_length=200, default='00000')
    qualification = models.CharField(max_length=100, default='00000')
    location = models.CharField(max_length=100, default='00000')
    tmexecutive = models.CharField(max_length=200, default='00000')


class Dcshared(models.Model):
    name = models.CharField(max_length=200, default='00000')
    location = models.CharField(max_length=100, default='00000')
    contact = models.IntegerField()
    status = models.CharField(max_length=200, default='00000')
    remarks = models.CharField(max_length=180, default='00000')


class Dcattendance(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    fromdate = models.DateField(max_length=200, default='2021-09-10')
    status = models.CharField(max_length=200, default='PRESENT')
    logintime = models.TimeField(auto_now_add=True)
    logouttime = models.TimeField(auto_now_add=True)
    todate = models.DateField(max_length=200, default='2021-09-10')


class Exetasks(models.Model):
    name = models.CharField(max_length=20, default='00000')
    location = models.CharField(max_length=100, default='00000')
    contact = models.CharField(max_length=50, default='00000')
    select = models.CharField(max_length=80, default='00000')


class Execompletedtasks(models.Model):
    name = models.CharField(max_length=200, default='00000')
    location = models.CharField(max_length=100, default='00000')
    contact = models.IntegerField()
    status = models.CharField(max_length=200, default='00000')
    description = models.CharField(max_length=200, default='00000')


class Exeattendance(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    fromdate = models.DateField(max_length=200, default='2021-09-10')
    status = models.CharField(max_length=200, default='PRESENT')
    logintime = models.TimeField(auto_now_add=True)
    logouttime = models.TimeField(auto_now_add=True)
    todate = models.DateField(max_length=200, default='2021-09-10')


class Tltasks(models.Model):
    fk_assigned = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    dc_assigned = models.ForeignKey(regdetails, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=200, default='00000')
    email = models.EmailField(max_length=200, default='00000')
    phone = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=100, default='00000')
    tmexecutive = models.CharField(max_length=200, default='00000')
    marktype = models.CharField(max_length=200, default='')
    markTl = models.CharField(max_length=150, default='')
    url = models.CharField(max_length=120, default='')
    description = models.CharField(max_length=3000, default='')
    proname = models.CharField(max_length=100, default='')
    newtarget = models.CharField(max_length=50, default='')
    servicename = models.CharField(max_length=100, default='')
    payment = models.CharField(max_length=100, default='')
    post = models.CharField(max_length=100, default='')
    qualification = models.CharField(max_length=200, default='')
    vacancies = models.CharField(max_length=200, default='')
    dttask = models.DateField(blank=True, null=True)
    submited = models.CharField(max_length=100, default='')
    branch = models.CharField(max_length=200, default='')
    sharetodc = models.BooleanField(default=False)


class Tlshareddatas(models.Model):
    user = models.ForeignKey(Tltasks, on_delete=models.CASCADE, null=True)
    fk_assigned = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=200, default='00000')
    email = models.EmailField(max_length=200, default='00000')
    qualification = models.CharField(max_length=100, default='00000')
    location = models.CharField(max_length=100, default='00000')
    contact = models.CharField(max_length=200, default='00000')
    tmexecutive = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    marketing_executive = models.CharField(max_length=200)
    directmarketer = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Exetasks2(models.Model):
    user = models.ForeignKey(Tlshareddatas, on_delete=models.CASCADE, null=True)
    date = models.DateField(max_length=200, default='00000')
    status = models.CharField(max_length=200, default='00000')
    description = models.CharField(max_length=200, default='00000')
    remarks = models.CharField(max_length=50, default='00000')


class Exetasks3(models.Model):
    exe2 = models.ForeignKey(Exetasks2, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, default='00000')
    location = models.CharField(max_length=100, default='00000')
    contact = models.CharField(max_length=50, default='00000')
    status = models.CharField(max_length=200, default='00000')
    remarks = models.CharField(max_length=50, default='00000')


class Tlattendance(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    fromdate = models.DateField(max_length=200, default='2021-09-10')
    status = models.CharField(max_length=200, default='PRESENT')
    logintime = models.TimeField(auto_now_add=True)
    logouttime = models.TimeField(auto_now_add=True)
    todate = models.DateField(max_length=200, default='2021-09-10')


class Tlshareddatas2(models.Model):
    name = models.CharField(max_length=200, default='00000')
    email = models.EmailField(max_length=200, default='00000')
    qualification = models.CharField(max_length=100, default='00000')
    location = models.CharField(max_length=100, default='00000')
    tmexecutive = models.CharField(max_length=200, default='00000')
    status = models.CharField(max_length=200, default='00000')
    description = models.CharField(max_length=200, default='00000')


'''class Report(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reportissue = models.CharField(max_length=300, default='00000')
    action = models.CharField(max_length=300, default='00000')
    date = models.DateField(max_length=20, default=datetime.now)'''


class Tlreport(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    reportissue = models.CharField(max_length=300, default='00000')
    action = models.CharField(max_length=300, default='00000')
    date = models.DateField(max_length=20, default=datetime.now)


class Exereport(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    reportissue = models.CharField(max_length=300, default='00000')
    action = models.CharField(max_length=300, default='00000')
    date = models.DateField(max_length=20, default=datetime.now)


class Dcapplyleave(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    leavefrom = models.DateField()
    leaveto = models.DateField()
    reason = models.CharField(max_length=300, default='00000')


class Tlapplyleave(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    leavefrom = models.DateField()
    leaveto = models.DateField()
    reason = models.CharField(max_length=300, default='00000')


class Exeapplyleave(models.Model):
    fk_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    leavefrom = models.DateField()
    leaveto = models.DateField()
    reason = models.CharField(max_length=300, default='00000')


class Assign(models.Model):
    tlshareddatas_id = models.ForeignKey(Tlshareddatas, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='00000')
    status = models.CharField(max_length=20, default='00000')

    
    
#-----------------------------------------MARKETING-----------------------------------------#    
        
# product details
class Products(models.Model):
    productname = models.CharField(max_length=200)
    date = models.DateField()   # Will clarify what date it is
    target = models.IntegerField()
    description = models.TextField()

# recruitment details
class Recruitments(models.Model):
    jobpostname = models.CharField(max_length=200)
    date = models.DateField()
    vacancies = models.IntegerField()
    qualifications = models.CharField(max_length=200)
    jobdescription = models.TextField()


#product task shared to data collector
class TL_prod_to_datacollect(models.Model):
    product = models.ForeignKey(Products, on_delete=CASCADE)
    collector = models.ForeignKey(regdetails, on_delete=CASCADE)

#recruitment task shared to data collector
class TL_recr_to_datacollect(models.Model):
    recruitment = models.ForeignKey(Recruitments, on_delete=CASCADE)
    collector = models.ForeignKey(regdetails, on_delete=CASCADE)    

#data collected on each product
class prod_datacollected(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phno = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    product = models.ForeignKey(Products, on_delete=CASCADE)
    exec_assigned = models.ForeignKey(regdetails, on_delete=DO_NOTHING, null=True)    
    status = models.BooleanField(null=True)

#data collected on each job applicant
class jobapplicant_datacollected(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phno = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    fresher_or_exp = models.CharField(max_length=200) # Will confirm whether  it is simply 'experienced' or '2 years experience'
    recruitment = models.ForeignKey(Recruitments, on_delete=CASCADE)
    exec_assigned = models.ForeignKey(regdetails, on_delete=DO_NOTHING, null=True)    
    status = models.BooleanField(null=True)    

# Have some doubts regarding the existing reports table structure. Will give answer tomorrow. For  now, work with the following table:

#report issues model
# class hr_report(models.Model):
#     issue = models.TextField()
#     reported_date = models.DateField()
#     reported_by = models.ForeignKey(regdetails, null=True, on_delete=CASCADE)
#     hr_reply = models.TextField()


# #attendance
# class attendance(models.Model):
#     date = models.DateField()
#     status = models.CharField(max_length=200)
#     logintime = models.CharField(max_length=200)
#     logouttime = models.CharField(max_length=200)
#     reg = models.ForeignKey(regdetails, on_delete=CASCADE) # Will automatically turn into reg_id in database    
    
        
  