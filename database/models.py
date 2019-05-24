from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Database(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    category = models.CharField(max_length = 50,verbose_name = "Kategori")
    position = models.CharField(max_length = 50,verbose_name = "Pozisyon")
    name = models.CharField(max_length = 50,verbose_name = "İsim")
    age = models.CharField(max_length = 50,verbose_name = "Yaş")
    size = models.CharField(max_length = 50,verbose_name = "Boy")
    weight = models.CharField(max_length = 50,verbose_name = "Kilo")
    foot = models.CharField(max_length = 50,verbose_name = "Kullandığı Ayak")
    club_history = models.CharField(max_length = 50,verbose_name = "Kulübe Katılma Tarihi")
    hoca_gorüsü = models.TextField()
    player_image = models.FileField(blank=True, null=True,verbose_name="Fotoğraf Ekleyin")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['-age']

class Galeri(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    galeri_category = models.CharField(max_length = 50,verbose_name = "Kategori")
    galeri_title = models.CharField(max_length = 50,verbose_name = "Başlık")
    galeri_content = models.FileField(blank=True, null=True,verbose_name="Fotoğraf veya Video Ekleyin")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.galeri_title

class Duyuru(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    duyuru_category = models.CharField(max_length = 50,verbose_name = "Kategori")
    duyuru_title = models.CharField(max_length = 50,verbose_name = "Başlık")
    duyuru_content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.duyuru_title

class Haber(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    haber_category = models.CharField(max_length = 50,verbose_name = "Kategori")
    haber_title = models.CharField(max_length = 50,verbose_name = "Başlık")
    haber_image = models.FileField(blank=True, null=True,verbose_name="Fotoğraf veya Video Ekleyin")
    haber_content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.haber_title


class PuanDurumu(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    category = models.CharField(max_length = 50,verbose_name = "Kategori")
    pozisyon = models.CharField(max_length = 50,verbose_name = "Pozisyon")
    takım = models.CharField(max_length = 50,verbose_name = "Takım")
    galibiyet = models.CharField(max_length = 50,verbose_name = "Galibiyet")
    beraberlik = models.CharField(max_length = 50,verbose_name = "Beraberlik")
    mağlubiyet = models.CharField(max_length = 50,verbose_name = "Mağlubiyet")
    a_gol = models.CharField(max_length = 50,verbose_name = "Attığı Gol")
    y_gol = models.CharField(max_length = 50,verbose_name = "Yediği Gol")
    puan = models.CharField(max_length = 50,verbose_name = "Puan")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.category

    class Meta():
        ordering = ['-puan']