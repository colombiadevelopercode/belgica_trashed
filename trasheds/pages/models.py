from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Cbb_company(models.Model):
    vestigingsnummer = models.CharField(verbose_name="vestigingsnummer", max_length=150)
    cbb = models.CharField(verbose_name="cbb", max_length=150)
    class Meta:
        ordering = ['id']


class Company_number(models.Model):
    ondernemin = models.CharField(verbose_name="ondernemin", max_length=150)
    vestiging = models.CharField(verbose_name="vestiging", max_length=150)
    ovamnum = models.CharField(verbose_name="ovamnum", max_length=150)
    ovamvolg = models.CharField(verbose_name="ovamvolg", max_length=150)
    naam = models.CharField(verbose_name="naam", max_length=150)
    straat = models.CharField(verbose_name="straat", max_length=150)
    adresuitbreiding = models.CharField(verbose_name="adresuitbreiding", max_length=150)
    huisnummer = models.CharField(verbose_name="huisnummer", max_length=150)
    postcode = models.CharField(verbose_name="postcode", max_length=150)
    gemeente = models.CharField(verbose_name="gemeente", max_length=150)
    landcode = models.CharField(verbose_name="landcode", max_length=150)
    cbb = models.CharField(verbose_name="cbb", max_length=150)

    class Meta:
        ordering = ['id', 'vestiging']

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="name", max_length=100)
    email = models.CharField(verbose_name="email", max_length=100)
    tel = models.CharField(verbose_name="tel", max_length=100)

    class Meta:
        ordering = ['id']

class Country(models.Model):
    country_spanish = models.CharField(verbose_name="country_spanish", max_length=150)
    country_holanda = models.CharField(verbose_name="country_holanda", max_length=150)
    code = models.CharField(verbose_name="code", max_length=150)

    class Meta:
        ordering = ['id']


class Euralcode(models.Model):
    afvalstof = models.CharField(verbose_name="afvalstof", max_length=150)
    eural = models.CharField(verbose_name="eural", max_length=150)
    rd = models.CharField(verbose_name="rd", max_length=150)
    verwer = models.CharField(verbose_name="verwer", max_length=150)

    class Meta:
        ordering = ['id', 'afvalstof']


class Ihm(models.Model):
    ondernemingsnr = models.CharField(verbose_name="ondernemingsnr", max_length=150)  
    naam = models.CharField(verbose_name="naam", max_length=150)
    ovam = models.CharField(verbose_name="ovam", max_length=150)
    adres = models.CharField(verbose_name="adres", max_length=150)
    postcode = models.CharField(verbose_name="postcode", max_length=150)
    gemeente = models.CharField(verbose_name="gemeente", max_length=150)
    land = models.CharField(verbose_name="land", max_length=150)
    tel = models.CharField(verbose_name="tel", max_length=150)
    email = models.CharField(verbose_name="email", max_length=150)
    vanaf = models.CharField(verbose_name="vanaf", max_length=150)
    tot = models.CharField(verbose_name="tot", max_length=150)

    class Meta:
        ordering = ['id']


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.IntegerField()
    name_user = models.CharField(verbose_name="name_user", max_length=150)
    log_description = models.TextField(verbose_name="log_description")
    referentie = models.CharField(verbose_name="name_user", max_length=150)
    versie = models.CharField(verbose_name="name_user", max_length=50)
    geldig = models.CharField(verbose_name="name_user", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id','name_user','created_at','referentie','versie','geldig','log_description' ]




    