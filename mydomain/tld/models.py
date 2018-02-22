from django.db import models

# Create your models here.
class Domain(models.Model):

    class Meta:
        db_table = 'tld_domain'
    updatetime = models.DateTimeField()
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=30)
    registry = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=30, blank=True)
    cate = models.CharField(max_length=30, blank=True)
    popular = models.IntegerField(blank=True)
    restrictions = models.CharField(max_length=200, blank=True)
    sources = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Registrar(models.Model):

    class Meta:
        db_table = 'tld_registrar'
    keyword = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    color = models.CharField(max_length=10, default="#fff")
    review = models.TextField(blank=True)
    rating = models.FloatField(blank=True)

    def __str__(self):
        return self.name


class Price(models.Model):

    class Meta:
        db_table = 'tld_price'
    register = models.FloatField(blank=True)
    renewal = models.FloatField(blank=True)
    transfer = models.FloatField(blank=True)
    whois = models.FloatField(blank=True)


class Cheapest(models.Model):

    class Mete:
        db_table = 'tld_cheapest'
    name = models.CharField(max_length=20)
    reg_registrar = models.CharField(max_length=30, blank=True)
    reg_price = models.FloatField(blank=True)
    renew_registrar = models.CharField(max_length=30, blank=True)
    renew_price = models.FloatField(blank=True)
    tran_registrar = models.CharField(max_length=30, blank=True)
    tran_price = models.FloatField(blank=True)
    popularity = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
