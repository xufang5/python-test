from django.db import models

# Create your models here.

class Event(models.Model):
    """
    发布会表
    """
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Guest(models.Model):
    """
    嘉宾表
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE) #on_delete=models.CASCADE,关联数据删除，外键也删除
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
