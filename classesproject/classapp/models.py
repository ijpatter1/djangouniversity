from django.db import models


class DjangoClass(models.Model):
    course_number = models.AutoField(primary_key='True')
    title = models.CharField(max_length=50, default='', blank='True', null='False')
    instructor_name = models.CharField(max_length=50, default='', blank='True', null='False')
    duration = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    objects = models.Manager()

    def __str__(self):
        return self.title
