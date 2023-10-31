from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Message(models.Model):
    tweet = models.TextField(verbose_name='Твит')
    username = models.CharField(verbose_name='Автор', max_length=50)
    nick = models.ForeignKey(User, verbose_name='Ник', on_delete=models.CASCADE)
    like = models.IntegerField(verbose_name='Количество лайков')
    dislike = models.IntegerField(verbose_name='Количество дизлайков')

class RegData(models.Model):
    username = models.CharField(verbose_name='Имя', max_length=50)
    phone = models.IntegerField(verbose_name='Телефон')
    password = models.TextField(verbose_name='Пароль')