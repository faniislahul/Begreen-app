from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from core.models import *
from core import views
from django.db.models import Min, Max, Sum
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView

def response_pengeluaran(request):
    data=request.POST
    
    if data.get('tipe') == '1' :
        
        det=data.get('details')
        jum=data.get('jumlah')
        qty=1
        id='2.1.1'
        jum2='{}'.format(int(float(data.get('jumlah')))*-1)
        id2='1.1.1'
        trans = Transaction(details= det, jumlah=jum, quantity=qty, kode=id)
        trans.save()
        
        trans2 = Transaction(details= det, jumlah=jum2, quantity=qty, kode=id2)
        trans2.save() 
        return HttpResponse('Success')
    elif data.get('tipe') == '2' :
        det=data.get('details')
        jum=data.get('jumlah')
        qty=1
        id='3.1.2'
        jum2='{}'.format(int(float(data.get('jumlah')))*-1)
        id2='1.1.1'
        trans = Transaction(details= det, jumlah=jum, quantity=qty, kode=id)
        trans.save()
        trans2 = Transaction(details= det, jumlah=jum2, quantity=qty, kode=id2)
        trans2.save() 
        return HttpResponse('Success')
    elif data.get('tipe') == '3' :
        det=data.get('details')
        jum=data.get('jumlah')
        qty=1
        id = data.get('jenis-biaya')
        #id='3.1.2'
        jum2='{}'.format(int(float(data.get('jumlah')))*-1)
        id2='1.1.1'
        trans = Transaction(details= det, jumlah=jum, quantity=qty, kode=id)
        trans.save()
        trans2 = Transaction(details= det, jumlah=jum2, quantity=qty, kode=id2)
        trans2.save() 
        return HttpResponse('Success')
    elif data.get('tipe') == '0' :
        det=data.get('details')
        jum=data.get('jumlah')
        qty=data.get('qty')
        id = data.get('jenis-bb')
        #id='3.1.2'
        jum2='{}'.format(int(float(data.get('jumlah')))*-1)
        id2='1.1.1'
        trans = Transaction(details= det, jumlah=jum, quantity=qty, kode=id)
        trans.save()
        trans2 = Transaction(details= det, jumlah=jum2, quantity=qty, kode=id2)
        trans2.save()
        
        hpp = int(float(jum))/int(float(qty))
        bb = Bahan_baku.objects.get(pk=id)
        bbstock = bb_stock(nama = bb, harga_beli = jum, quantity = qty, satuan = Satuan_bb.objects.get(nama = "Kg"), hpp = hpp)
        bbstock.save()
        bblog = bb_log(kode=bb, add = int(float(qty)) , last_hpp = bbstock.hpp, last_price = bbstock.harga_beli)
        bblog.save()
        return HttpResponse('Success')
            
    else:
        return HttpResponse('Failed')
def response_persediaan(request):
    data=request.POST
    id = data.get('jenis-bb')
    qty = int(float(data.get('qty')))
    bb = Bahan_baku.objects.get( pk = id )
    count = bb_stock.objects.filter(nama = bb ).count()
   
    if count == 0 :
       return HttpResponseRedirect(reverse('home'))

    sums = bb_stock.objects.filter(nama = bb ).aggregate(Sum('quantity'))
    
   # return HttpResponse(sums["quantity__sum"])
    if qty > sums["quantity__sum"] :
        return HttpResponse('Kuantitas tidak mencukupi<br><a href = home>Kembali</a>')
    else :

        while (qty>0):                
            bbstock = bb_stock.objects.all().filter(nama = bb )
        
            if qty > bbstock[0].quantity :
            
                bblog=bb_log(kode=bb, used = bbstock[0].quantity , last_hpp = bbstock[0].hpp, last_price = bbstock[0].harga_beli)
                bblog.save()
                qty -= bbstock[0].quantity
                bbstock[0].delete()
            else:
                usedqty = bbstock[0].quantity - qty
                bblog=bb_log(kode=bb, used = qty , last_hpp = bbstock[0].hpp, last_price = bbstock[0].harga_beli)
                bblog.save()
                bbstocklast = bb_stock.objects.get(kode = bbstock[0].kode)
                bbstocklast.quantity = usedqty
                bbstocklast.save()
                qty = 0
        return HttpResponse('Success')
def response_pemasukan(request):
    data=request.POST
    
    if data.get('tipe') == '1' :
        
        det=data.get('details')
        jum=data.get('jbr')
        qty=1
        id='1.1.1'
        jum2='{}'.format(int(float(data.get('jbr')))*-1)
        id2='1.1.2'
        trans = Transaction(details= det, jumlah=jum, quantity=qty, kode=id)
        trans.save()
        
        trans2 = Transaction(details= det, jumlah=jum2, quantity=qty, kode=id2)
        trans2.save() 
        return HttpResponse('Success')
    elif data.get('tipe') == '2' :
        det=data.get('details')
        jum=data.get('jbr')
        qty=1
        id='1.1.1'
        jum2='{}'.format(int(float(data.get('jbr')))*-1)
        id2='2.1.1'
        trans = Transaction(details= det, jumlah=jum, quantity=qty, kode=id)
        trans.save()
        trans2 = Transaction(details= det, jumlah=jum2, quantity=qty, kode=id2)
        trans2.save() 
        return HttpResponse('Success')
    elif data.get('tipe') == '3' :
        det=data.get('details')
        jum=data.get('jbr')
        qty=1
        
        id='1.1.1'
        jum2='{}'.format(int(float(data.get('jbr')))*-1)
        id2='3.1.1'
        trans = Transaction(details= det, jumlah=jum, quantity=qty, kode=id)
        trans.save()
        trans2 = Transaction(details= det, jumlah=jum2, quantity=qty, kode=id2)
        trans2.save() 
        return HttpResponse('Success')
    elif data.get('tipe') == '0' :
        det=Produk.objects.get(kode = data.get('produk')) 
        jum=data.get('jumlah')
        qty=data.get('qty')
        
        id='1.1.1'
        jum2='-{}'.format(jum)
        
        id2='4.1.1.{}'.format(data.get('produk'))
        trans = Transaction(details= det, jumlah=jum, quantity=qty, kode=id)
        trans.save()
        trans2 = Transaction(details= det, jumlah=jum2, quantity=qty, kode=id2)
        trans2.save() 
        return HttpResponse('Success')
            
    else:
        return HttpResponse('Failed')
def response_produk(request):
    data=request.POST
    name = data.get('name')
    harga_jual = data.get('harga_jual')
    bb = data.getlist('bb')
    
    produkz = Produk(nama = name, harga_jual = harga_jual, active = True)
    produkz.save()
   # return HttpResponse(bb[0]) 
    for tmp in bb :

        bbz = Bahan_baku.objects.get(kode = tmp)
        pbb = p_bb(produk = produkz, bb = bbz)
        pbb.save()
    return HttpResponseRedirect(reverse('produk')) 