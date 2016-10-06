from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from core.models import *
from core import views
from django.db.models import Min, Max, Sum
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from datetime import datetime

def calculate(self):
    datenow = datetime.now()
    produk = Produk.objects.all()
    for more in produk: 
        count = Transaction.objects.filter(kode = '4.1.1.{}'.format(more.kode), date__month = datenow.month).aggregate(Sum('quantity'))
        unit = count['quantity__sum']
        bblx = bbl(more)*(1/unit)
        bbtlx = bbtl(more)*(1/unit)
        hpp = bblx+bbtlx
        csd = cost_driver.objects.get(nama = 'Unit Produksi')
        write = abc_log(produk = more, bbl = bblx, bbtl = bbtlx, unit_produksi = unit, hpp_unit = hpp, year = datenow.year, month = datenow.month, costdriver = csd)
        write.save()
    return HttpResponseRedirect(reverse('home'))

def bbtl(Produk):
    pbb = p_bb.objects.all().filter(produk = Produk)
    sum = 0
    datenow = datetime.now()
    for some in pbb:
        bb = some.bb
        if bb.langsung == False:
            stock_used = bb_log.objects.all().filter(kode = bb, date__month = datenow.month)
            stocksum = 0
            count = 0
            for it in stock_used :
                value = it.used * it.last_hpp
                stocksum += value
                count += it.used
                if count>0:
                    avg = stocksum*(1/count)
                    sum += avg
                else:
                    sum+=0
    return sum

def bbl(Produk):
    pbb = p_bb.objects.all().filter(produk = Produk)
    sum = 0
    datenow = datetime.now()
    for some in pbb:
        bb = some.bb
        if bb.langsung == True:
            stock_used = bb_log.objects.all().filter(kode = bb, date__month = datenow.month)
            stocksum = 0
            count = 0
            for it in stock_used :
                value = it.used * it.last_hpp
                stocksum += value
                count += it.used
                avg = stocksum/count
                sum += avg
            
    return sum