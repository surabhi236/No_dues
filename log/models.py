from django.db import models


class Library(models.Model):
    username = models.CharField(max_length=50)
    clear = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class CC(models.Model):
    username = models.CharField(max_length=50)
    clear = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Gymkhana(models.Model):
    username = models.CharField(max_length=50)
    clear = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Csedept(models.Model):
    username = models.CharField(max_length=50)
    clear = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Umiamhostel(models.Model):
    username = models.CharField(max_length=50)
    clear = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Subhansrihostel(models.Model):
    username = models.CharField(max_length=50)
    clear = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Dhansarihostel(models.Model):
    username = models.CharField(max_length=50)
    clear = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Student(models.Model):
    username = models.CharField(max_length=50)
    library = models.IntegerField(default=0)
    cc = models.IntegerField(default=0)
    hostel = models.IntegerField(default=0)
    gymkhana = models.IntegerField(default=0)
    dept = models.IntegerField(default=0)

    def __str__(self):
        return self.username
