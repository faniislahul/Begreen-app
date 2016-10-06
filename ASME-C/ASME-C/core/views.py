from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from core.models import *
from django.views.generic import *
from django.db.models import Min, Max, Sum
# Create your views here.

def Home(request):
    tr = Transaction.objects.all().filter(kode__startswith= "4.1.1.")
    produk = Produk.objects.all()
    stats = {}
    for j in produk :
         kod = '4.1.1.{}'.format(j.kode)
         tr = Transaction.objects.filter(kode = kod).aggregate(Sum('quantity'))
         stats[j] = tr
    
    c = ({'stats' : stats,       
        })
    return render(request,'index.html',c)

def settings(request):
    return render(request,'settings.html')

def pengeluaran(request):
    biaya = Akun_l3.objects.all().filter(kode_lv__startswith= "5")
    bb = Bahan_baku.objects.all() 
    c = ({'biaya' : biaya,
          'bb' : bb,        
        })
    #return HttpResponse(print (biaya))
    return render(request,'pengeluaran.html',c)

def pemasukan(request):
    produk = Produk.objects.all() 
    c = ({'produk' : produk,   
        })
    #return HttpResponse(print (biaya))
    return render(request,'pemasukan.html',c)


def persediaan(request):
    bb = Bahan_baku.objects.all() 
    c = ({
          'bb' : bb,        
        })
    return render(request,'persediaan.html',c)

def produk(request):
    bb = Bahan_baku.objects.all()
    produk = Produk.objects.all()
    c = ({
          'bb' : bb,
          'produk' : produk,        
        })
    return render(request,'produk.html',c)

class Akunlv1(ListView):
    model = Akun_l1

class Akunlv2(ListView):
    model = Akun_l2    

class Akunlv3(ListView):
    model = Akun_l3

class Akunlv1Details(DetailView):
    model = Akun_l1

class Akunlv2Details(DetailView):
    model = Akun_l2

class Akunlv3Details(DetailView):
    model = Akun_l3
