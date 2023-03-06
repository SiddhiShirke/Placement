from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import date,datetime
# Create your models here.
from django.utils import timezone

# Create your models here.

today = timezone.now
class signup(AbstractUser):


    email = models.EmailField(unique=True)
    #password = models.CharField(max_length=250)
    username =models.CharField(max_length=20,default='',null=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

#
# class User(AbstractUser):
#     name = models.CharField(_('Name of User'),blank=True,max_length=255)
#     email = models.EmailField(_('Enter Your Email Id'), unique=True,
#                               error_messages={
#                                   "unique":"Email ID already exists"
#                               }
#                               )
#
#     username = models.CharField(max_length=250,unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     EMAIL_FIELD = 'email'
#


class studentData(models.Model):
    user = models.OneToOneField(signup,on_delete=models.CASCADE)
    ssc_percentage = models.CharField(max_length=10)
    hsc_percentage = models.CharField(max_length=10)
    graduation_semester_1_CGPA_or_percentage =models.CharField(max_length=10)
    graduation_semester_2_CGPA_or_percentage=models.CharField(max_length=10)
    graduation_semester_3_CGPA_or_percentage=models.CharField(max_length=10)
    graduation_semester_4_CGPA_or_percentage=models.CharField(max_length=10)
    graduation_semester_5_CGPA_or_percentage=models.CharField(max_length=10)
    graduation_semester_6_CGPA_or_percentage=models.CharField(max_length=10)
    overall_CGPA_or_percentage=models.CharField(max_length=10,default='')
    skills = models.CharField(max_length=200,blank=True,default=' ')
    upload_cv = models.FileField(upload_to='CV', blank=True, null=True)

    def __str__(self):
        return self.user.email
    #year_of_admission = models.DateField()

#

def present_future_dates(value):
    if value < date.today():
        raise ValidationError('Cannot Enter Past Dates')

class company_details(models.Model):
    company_name =models.CharField(max_length=20)
    pa_pm = [('p.m.', 'Monthly'), ('p.a.', 'Annual')]
    jobtype = [('1-months-internship', '1-Months Internship'),
               ('2-months-internship', '2-Months Internship'), ('3-months-internship', '3-Months Internship'),
               ('4-months-internship', '4-Months Internship'), ('5-months-internship', '5-Months Internship'),
               ('6-months-internship', '6-Months Internship'), ('7-months-internship', '7-Months Internship'),
               ('8-months-internship', '8-Months Internship'), ('9-months-internship', '9-Months Internship'),
               ('10-months-internship', '10-Months Internship'), ('11-months-internship', '11-Months Internship'),
               ('12-months-internship', '12-Months Internship'),
               ('full-time', 'Full-Time'), ('part-time', 'Part-Time')]

    job_type = models.CharField(max_length=50, choices=jobtype, default='full-time')
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=200, default=' ')
    location = models.CharField(max_length=100,null=True,blank=True,default='any')
    skills_required = models.CharField(max_length=255)
    salary = models.PositiveIntegerField()
    monthly_annually = models.CharField(_('Monthly or Annual'), max_length=20, choices=pa_pm, default='p.a')
    last_date_of_applying = models.DateField(validators=[present_future_dates])
    rounds_description = models.CharField(max_length=100)
    date_of_interview =models.CharField(max_length=30)
    reporting_time =models.CharField(max_length=10)

    def __str__(self):
        return self.company_name + " " +self.job_title

class appliedStudents(models.Model):
    user = models.ForeignKey(signup,on_delete=models.CASCADE,default=-1)
    company = models.ForeignKey(company_details,on_delete=models.CASCADE,default=-1)
    applied_date = models.DateField(default=today)




#shirke01
#admin
#shirke@gmail.com
#
# first_name = models.CharField(max_length=20)
#     middle_name = models.CharField(max_length=20)
#     last_name =models.CharField(max_length=20)
#     gender = [('male', 'Male'), ('female', 'Female')]
#     birth_date = models.DateField()
#     contact_number = models.CharField(max_length=10)
#     gender = models.CharField(choices=gender,max_length=10)