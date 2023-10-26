from django.db import models


class MyName(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):

    user_name = models.CharField(max_length=30, help_text='name of user-participant')
    user_password = models.CharField(max_lenght=8, help_text="user's password")

    def __str__(self):
        return self.user_name
    '''
    user_stand = models.ForeignKey('Stand', on_delete=models.SET_NULL, null=True)
    comment = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True)

    

class Stand(models.Model):
    stand_name = models.CharField(max_length=30, help_text='name of user who stand his photo')
    photo = models.ImageField(upload_to='uploads/')
    comment = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ForeignKey('Like', on_delete=models.SET_NULL, null=True, default=0)
    user = models.ForeignKey('User')

    def __str__(self):
        return self.stand_name


class Comment(models.Model):
    comment_text = models.TextField(max_length=1000, help_text='text_of_comment')

    def __str__(self):
        return self.comment_text

class Like(models.Model):
'''