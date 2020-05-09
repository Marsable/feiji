from django.db import models

# Create your models here.
class Ji(models.Model):
    GENDER_CHOICES=(
        ('0','停用'),
        ('1','启用'),

        )
    id=models.AutoField('序列号',primary_key=True)
    banhao=models.CharField('航班号',max_length=200)
    status=models.CharField(choices=GENDER_CHOICES,default=0,max_length=1)

    

    class Meta:
        db_table='ji'
        verbose_name='飞机航班'
        verbose_name_plural=verbose_name
    def __str__(self):
        return str(self.id);
