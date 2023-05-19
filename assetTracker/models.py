from django.db import models

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=32)

class Lokasi(models.Model):
    nama_lokasi = models.CharField(max_length=32)

class StatusAsset(models.Model):
    status = models.CharField(max_length=16)

class Manufaktur(models.Model):
    nama_manufaktur = models.CharField(max_length=32)

class Asset(models.Model):
    nama_asset = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    serialnumber = models.CharField(max_length=32)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    manufaktur = models.ForeignKey(Manufaktur, on_delete=models.CASCADE)
    tanggalpembelian = models.DateField()
    lamagaransi = models.IntegerField(max_length=3) #dalam bulan
    catatan = models.CharField(max_length=256)
    status = models.ForeignKey(StatusAsset, on_delete=models.CASCADE)
    lokasi = models.ForeignKey(Lokasi, on_delete=models.CASCADE)



