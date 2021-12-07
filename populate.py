#creation of django environment
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project11.settings')

#Accessing of Django features
import django
django.setup()

#actual population starts
from app1.models import *
from faker import Faker
f=Faker()
import random
L = ['tennis','rugby','boxing','polo','cycling']

def add_topic():
    t=Topic.objects.get_or_create(topic_name=random.choice(L))[0]
    t.save()
    return t
def add_webpage(name,url):
    t=add_topic()
    w=Webpage.objects.get_or_create(topic_name= t,name=name,url=url)[0]
    w.save()
    return w
def add_records(name,url,date):
    w=add_webpage(name,url)
    a=Access_Records.objects.get_or_create(name=w,date=date)[0]
    a.save()

def add_data():
    n=int(input('enter the data to insert'))
    for i in range(n):
        f_name=f.first_name()
        f_url=f.url()
        f_date=f.date()    
        add_records(f_name,f_url,f_date)

if __name__ =='__main__':
    print('population starts')
    add_data()
    print('population ended')        