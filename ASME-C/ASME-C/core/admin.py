from django.contrib import admin
from core.models import *

# Register your models here.

class Akunl1Admin(admin.ModelAdmin):
    list_display = ("kode_lv", "nama",)
    ordering = ('-kode_lv',)
    exclude =[
                    'kode_lv',
                ]

admin.site.register(Akun_l1, Akunl1Admin)

class Akunl2Admin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        par = Akun_l2.objects.filter(parent = obj.parent).count()+1
        obj.kode_lv = '{}.{}'.format(obj.parent.kode_lv , par)
        obj.save()
    list_display = ("kode_lv","nama","parent",)
    ordering = ('kode_lv',)
    exclude =[
                    'kode_lv',
                ]

admin.site.register(Akun_l2,Akunl2Admin)

class Akunl3Admin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        par = Akun_l3.objects.filter(parent = obj.parent).count()+1
        obj.kode_lv = '{}.{}'.format(obj.parent.kode_lv , par)
        obj.save()
    
    list_display = ("kode_lv","nama","parent",)
    ordering = ('parent',)
    exclude =[
                    'kode_lv',
                ]

admin.site.register(Akun_l3,Akunl3Admin)

class TransactionAdmin(admin.ModelAdmin):
    
    list_display = ("date","kode","jumlah","quantity", "details")
    ordering = ('date',)

admin.site.register(Transaction, TransactionAdmin)

class Satuan_bbAdmin(admin.ModelAdmin):
    
    list_display = ("nama",)
    ordering = ('nama',)

admin.site.register(Satuan_bb, Satuan_bbAdmin)

class Bahan_bakuAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        par = Bahan_baku.objects.all().count()+1
        obj.kode = '1.1.3.{}'.format(par)
        obj.save()    

    list_display = ("kode","nama","harga_beli","quantity", "satuan","used","hpp","langsung")
    ordering = ('kode',)
    exclude =[
                    'kode','harga_beli','quantity','used','hpp'
                ]
admin.site.register(Bahan_baku, Bahan_bakuAdmin)

class bb_stockAdmin(admin.ModelAdmin):
    list_display = ("kode","nama","harga_beli","quantity", "satuan","used","hpp")
    ordering = ('kode',)
   
admin.site.register(bb_stock, bb_stockAdmin)

class BB_logAdmin(admin.ModelAdmin):
        

    list_display = ("date","kode","used","add","last_hpp", "last_price")
    ordering = ('kode',)
    
admin.site.register(bb_log,BB_logAdmin)

class ProdukAdmin(admin.ModelAdmin):
    
    list_display = ("kode","nama","harga_jual")
    ordering = ('kode',)

admin.site.register(Produk, ProdukAdmin)
class costdriverAdmin(admin.ModelAdmin):
    
    list_display = ("nama",)
    ordering = ('nama',)

admin.site.register(cost_driver, costdriverAdmin)
class pbbAdmin(admin.ModelAdmin):
    
    list_display = ("produk","bb")
    ordering = ('produk',)

admin.site.register(p_bb, pbbAdmin)

class abcAdmin(admin.ModelAdmin):
    
    list_display = ("produk","bbl","bbtl","unit_produksi","costdriver","hpp_unit","month","year",)
    ordering = ('produk',)


admin.site.register(abc_log, abcAdmin)