from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import loader
from webapp.models import *
from django.views.generic import *
import json
from django.forms.models import model_to_dict
from django.core.serializers import *

def dash(request):
    return render(request,'webapp/admin/admin_dash.html')

def products_admin(request):
    y = products.objects.all()
    z = subcategories.objects.all()
    data = ({'products' : y ,
             'subcategories' : z ,})
    return render(request,'webapp/admin/admin_products.html',data)

def categories_admin(request):
    y = subcategories.objects.all()
    z = categories.objects.all()
    data = ({'subcategories' : y ,'categories' : z})
    return render(request,'webapp/admin/admin_categories.html', data)

def crudhandler(request):
    if request.method == 'POST' : 
        data = request.POST
        
        if data.get('content') == '0':
            danzel = cat_master(data)
        
            res = ({'result' : danzel,})
            return JsonResponse(res)
    
        elif data.get('content') == '1':
            danzel = subcat_master(data)
        
            res = ({'result' : danzel,})
            return JsonResponse(res)
            
    else :
        return render(request, 'webapp/admin/admin_dash.html')


def cat_master(data):
    
    if data.get('operation') == '0' :
        dummy = categories(name = data.get('name'), description = data.get('desc'), pic = "pic")
        dummy.save() 
        id = dummy.id
        result = ({'result' : 4, 'id': id,})
    elif data.get('operation') == '1' :
        count = categories.objects.filter(pk = data.get('id')).count()
        if count > 0 :
            dummy = categories.objects.get(pk = data.get('id'))
            dummy.name = data.get('name')
            dummy.description = data.get('desc')
            dummy.save()
            result = ({'result' : 4,})
        else :
            result = 0
    elif data.get('operation') == '2' :
        count = categories.objects.filter(pk = data.get('id')).count()
        if count > 0 :
            dummy = categories.objects.get(pk = data.get('id'))
            dummy.delete()
            result = 4
        else :
            result = 0
    elif data.get('operation') == '3' :
        count = categories.objects.filter(pk = data.get('id')).count()
        if count > 0 :
            dummy = categories.objects.get(pk = data.get('id'))
            result = model_to_dict(dummy)
        else :
            result = 0
    else :
        result = 1
    return result


def subcat_master(data):
    
    if data.get('operation') == '0' :
        dummy = subcategories(name = data.get('name'), description = data.get('desc'),parent = categories.objects.get(name = data.get('parents')) ,pic = "pic")
        dummy.save() 
        id = dummy.id
        result = ({'result' : 4, 'id': id,})
    elif data.get('operation') == '1' :
        count = subcategories.objects.filter(pk = data.get('id')).count()
        if count > 0 :
            dummy = subcategories.objects.get(pk = data.get('id'))
            dummy.name = data.get('name')
            dummy.description = data.get('desc')
            dummy.parent = categories.objects.get(name = data.get('parents'))
            dummy.save()
            result = ({'result' : 4,})
        else :
            result = 0
    elif data.get('operation') == '2' :
        count = subcategories.objects.filter(pk = data.get('id')).count()
        if count > 0 :
            dummy = subcategories.objects.get(pk = data.get('id'))
            dummy.delete()
            result = 4
        else :
            result = 0
    elif data.get('operation') == '3' :
        count = subcategories.objects.filter(pk = data.get('id')).count()
        if count > 0 :
            dummy = subcategories.objects.get(pk = data.get('id'))
            result = model_to_dict(dummy)
            result['parent']=dummy.parent.name
        else :
            result = 0
    else :
        result = 1
    return result