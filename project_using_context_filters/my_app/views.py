from django.shortcuts import render
import datetime

# Create your views here.
def filters(request):
    context = {'list': ['a' , 'b' , 'c' , 'd' , 'e'], 'times' : datetime.datetime.now() , 'string':"" , 'num': 10 , 'name': 'rahim ali' , 'peoples':[{'name':'shihab' ,'age':20},{'name':'rasel' ,'age':19},{'name':'alvi' ,'age':20}],
               'string2':'i Am BANgladeshi' , 'custom_date': datetime.datetime(2022, 12, 31, 12, 00),'custom_date2': datetime.datetime(2021, 12, 31, 12, 00), 'notification': 7 ,'non_list': 'ABCDEFG' , 'num2':1025 }

    return render(request,'my_app/filters.html',context)