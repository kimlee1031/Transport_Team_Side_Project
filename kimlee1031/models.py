from django.db import models

class User(models.Model):
    user_pk = models.CharField(primary_key=True,max_length=100)
    nickname =models.CharField(max_length= 10,null=True)
    school_name=models.CharField(max_length=100)
    id =models.CharField(max_length=16)
    pw =models.CharField(max_length=16)

    class Meta:
        db_table = 'Userkimsang'

class User_information(models.Model):
    information_pk =models.CharField(max_length=100)
    user_pk =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    p_number=models.CharField(max_length=11)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'User_information'

class Taxi_posts(models.Model):
    t_posts= models.CharField(max_length=50)
    user_pk=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    post_name=models.CharField(max_length=100)
    post_content=models.CharField(max_length=100)
    post_content=models.DateTimeField()

    class Meta:
        db_table = 'Taxi_posts'


