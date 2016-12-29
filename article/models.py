from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100) #blog title
    category = models.CharField(max_length= 50, blank= True) # blog tags
    date_time = models.DateTimeField(auto_now_add= True) # blog date
    content = models.TextField(blank=True, null= True) #blog contents

    def __str__(self):
        return self.title

    class Meta: #按时间下降排序
        ordering = ['-date_time']
