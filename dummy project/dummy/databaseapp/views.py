	
from multiprocessing import context

from django.db import connection
from .models import course_t, school_t
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render 


def index(request):
    data= 'current data'
    context= {
        "data": data
    }
    return render(request, 'index.html',context)

def generate(request):

    query= """
            select d.school_title, count(*) AS Count
            from section_t AS S, department_t AS D
            where S.dept_id=D.dept_id AND
            enroll_capacity<50
            group BY S.dept_id
            """
    result=[]
    with connection.cursor() as cursor:
        cursor.execute(query)   
        result = cursor.fetchall()
        sum=0
        for c in count:
            sum+=sum+[c]
        context={
            'school_title':school_title
            'school_total':count
            'total':sum
        }

            
    return render(request, 'index.html',context)

'''
def upload(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                 
                
                obj = course_t.objects.create(course_ID=dbframe.COFFER_COURSE_ID,course_name=dbframe.COURSE_NAME, credit_hours=dbframe.CREDIT_HOUR)
                print(type(obj))
                obj.save()
 
            return render(request, 'upload_2.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'admin_page.html',{})
    ''' 