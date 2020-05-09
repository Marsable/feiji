from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField('序列号',primary_key=True)
    uname=models.CharField('账号',max_length=200)
    mima=models.CharField('密码',max_length=12)
    dianhua=models.CharField('电话号码',max_length=11)
    name=models.CharField('姓名',max_length=50)
	

    class Meta:
        db_table='user'
        verbose_name='用户表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return str(self.id);
