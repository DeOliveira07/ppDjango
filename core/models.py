from django.db import models

class Product(models.Model):
    name = models.CharField('Nome',max_length=100)
    price = models.DecimalField('Preço',max_digits=10,decimal_places=2)
    storage = models.IntegerField('Estoque')

    def __str__(self):
        return self.name

class Client(models.Model):
    nome = models.CharField('Nome',max_length=100)
    lastname = models.CharField('Last Name',max_length=100)
    email = models.CharField('Email',max_length=100)

    def __str__(self):
        return self.nome

class city(models.Model):
    nome = models.CharField('Nome',max_length=100)
    def __str__(self):
        return self.nome







