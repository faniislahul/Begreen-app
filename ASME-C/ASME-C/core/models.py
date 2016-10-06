from django.db import models

# Create your models here.
class Akun_l1(models.Model):
    kode_lv = models.AutoField(primary_key = True)
    nama = models.CharField(max_length = 40)
    def __str__(self): 
        return self.nama

class Keymaker(models.Model):
    def keymaking(lv, parent):
        prep=int(float(parent))
        code = "%s.%s" % (parent,prep)
        return code

class Akun_l2(models.Model):
    
    
    kode_lv = models.CharField(max_length = 100, primary_key = True)
    parent = models.ForeignKey(Akun_l1, on_delete=models.CASCADE)
    nama = models.CharField(max_length = 40) 
    def get_count(rparent):
        c = self.filter(parent = rparent).count() 
        return c  
    def __str__(self):
        return self.nama

class Akun_l3(models.Model):
    kode_lv = models.CharField(max_length = 100, primary_key = True)
    parent = models.ForeignKey(Akun_l2, on_delete=models.CASCADE)
    nama = models.CharField(max_length = 40)
      
    def get_count(rparent):
        c = self.filter(parent = rparent).count() 
        return c
    def __str__(self):
        return self.nama

class Transaction(models.Model):
    date = models.DateField(auto_now_add=True)
    details = models.CharField(max_length = 100)
    kode = models.CharField(max_length = 100)
    jumlah = models.BigIntegerField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.details

class Satuan_bb(models.Model):
    nama = models.CharField(max_length = 100)
    def __str__(self):
        return self.nama


class Bahan_baku(models.Model):
    kode = models.CharField(max_length = 100, primary_key = True) 
    nama = models.CharField(max_length = 100)
    harga_beli = models.BigIntegerField(default = 0)
    hpp = models.BigIntegerField(default = 0)
    satuan = models.ForeignKey(Satuan_bb, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)
    used = models.IntegerField(default = 0)
    langsung = models.BooleanField(default = True)
    def __str__(self):
        return self.nama

class bb_stock(models.Model):
    kode = models.AutoField(primary_key = True)
    nama = models.ForeignKey(Bahan_baku, on_delete = models.CASCADE)
    harga_beli = models.BigIntegerField(default = 0)
    hpp = models.BigIntegerField(default = 0)
    satuan = models.ForeignKey(Satuan_bb, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)
    used = models.IntegerField(default = 0)
    
  #  def __str__(self):
   #     return self.nama

class bb_log(models.Model):
    kode = models.ForeignKey(Bahan_baku, on_delete = models.CASCADE)
    kode_stock = models.CharField(max_length = 100, null = True, default = None )
    date = models.DateField(auto_now_add=True)
    used = models.IntegerField(default = 0)
    add = models.IntegerField(default = 0)
    last_price = models.BigIntegerField(default = 0)
    last_hpp = models.BigIntegerField(default = 0)
    #def __str__(self):
     #   return self.kode

class cost_driver(models.Model):
    nama = models.CharField(max_length = 100)
    def __str__(self) :
        return self.nama

class Produk(models.Model):
    kode = models.AutoField(primary_key = True)
    nama = models.CharField(max_length = 100)
    harga_jual = models.BigIntegerField(default = 0)
    active = models.BooleanField(default = True)
    def __str__(self):
        return self.nama

class p_bb(models.Model):
    produk = models.ForeignKey(Produk, on_delete = models.CASCADE)
    bb = models.ForeignKey(Bahan_baku, on_delete = models.CASCADE)
 
month = ((1,"Januari"),(2,"Februari"),(3,"Maret"),(4,"April"),(5,"Mei"),(6,"Juni"),(7,"Juli"),(8,"Agustus"),(9,"September"),(10,"Oktober"),(11,"November"),(12,"Desember"),)

class abc_log(models.Model):
    month = models.IntegerField(choices = month)
    year = models.IntegerField()
    produk = models.ForeignKey(Produk, on_delete = models.CASCADE)
    bbl = models.BigIntegerField(default = 0)
    bbtl = models.BigIntegerField(default = 0)
    costdriver = models.ForeignKey(cost_driver, on_delete = models.CASCADE)
    unit_produksi = models.IntegerField(default = 0)
    hpp_unit = models.BigIntegerField(default = 0)