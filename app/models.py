
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.password_validation import validate_password



class User(AbstractUser):
    TOSHKENT = "Toshkent"
    TOSHKENT_V = "Toshkent_v"
    ANDIJON = "Andijon "
    BUXORO = "Buxoro"
    FARGONA = "Farg'ona"
    SIRDARYO = "Sirdaryo"
    JIZZAX = "Jizzax"
    NAMANGAN = "Namangan"
    NAVOIY = "Navoiy"
    QORAQAL = "Qoraqalpog'iston Respublikasi"
    SAMARQAND = "Samarqand"
    SURXONDARYO = "Surxondaryo"
    XORAZM = "Xorazm"
    QASHQADARYO = "Qashqadaryo"

    CITY = (
        (TOSHKENT, "Toshkent"),
        (TOSHKENT_V, "Toshkent_v"),
        (ANDIJON, "Andijon"),
        (BUXORO, "Buxoro"),
        (FARGONA, "Farg'ona"),
        (SIRDARYO, "Sirdaryo"),
        (JIZZAX, "Jizzax"),
        (NAMANGAN, "Namangan"),
        (NAVOIY, "Navoiy"),
        (QORAQAL, "Qoraqalpog'iston Respublikasi"),
        (SAMARQAND, "Samarqand"),
        (SURXONDARYO, "Surxondaryo"),
        (XORAZM, "Xorazm"),
        (QASHQADARYO, "Qashqadaryo"),


    )

    city = models.CharField(max_length=50, choices=CITY)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, validators=[validate_password])


class Category(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)