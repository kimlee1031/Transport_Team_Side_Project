from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Address(models.Model):
    address_pk = models.CharField(primary_key=True,max_length=100)
    administrative_district = models.CharField(max_length=100, blank=True,)
    departure_number = models.CharField(max_length=100)
    departure_road_name_address = models.CharField(max_length=100)
    destination_number = models.CharField(max_length=100)
    Destination_road_name_address = models.CharField(max_length=100)

    class Meta:
        ordering = ['Address']

class TransInfo(models.Model):
    transinfo_pk = models.CharField(primary_key=True,max_length=100)
    user_pk =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    transinfo_num=models.CharField(max_length=10)
    transinfo_picture=models.CharField(max_length=50)


