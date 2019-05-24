from django import forms
from .models import Database,Galeri,Duyuru,Haber,PuanDurumu

class AddPlayerForm(forms.ModelForm):
    
    class Meta :
        model = Database
        fields = ["category","position","name","age","size","weight","foot","club_history","hoca_gorüsü","player_image"]
    
class AddGaleriForm(forms.ModelForm):

    class Meta:
        model = Galeri
        fields = ["galeri_category","galeri_title","galeri_content"]

class AddDuyuruForm(forms.ModelForm):

    class Meta:
        model = Duyuru
        fields = ["duyuru_category","duyuru_title","duyuru_content"]
class AddHaberForm(forms.ModelForm):

    class Meta:
        model = Haber
        fields = ["haber_category","haber_title","haber_image","haber_content"]

class AddPuanDurumuForm(forms.ModelForm):

    class Meta:
        model = PuanDurumu
        fields = ["category","pozisyon","takım","galibiyet","beraberlik","mağlubiyet","a_gol","y_gol","puan"]