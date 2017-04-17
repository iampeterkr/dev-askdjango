from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        ('d' , 'Draft') ,
        ('p' , 'Published') ,
        ('w' , 'Withdrawn') ,
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)  # Tag class 연결
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(Post)
    author=models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

