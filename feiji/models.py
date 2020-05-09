from django.db import models

# Create your models here.
class Feiji(models.Model):

    id=models.AutoField('序列号',primary_key=True)
    uid=models.CharField('用户id',max_length=200)
    jid=models.CharField('飞机id',max_length=200)
    zuowei=models.CharField('座位号',max_length=200)
    

    class Meta:
        db_table='feiji'
        verbose_name='飞机票'
        verbose_name_plural=verbose_name
    def __str__(self):
        return str(self.id);
