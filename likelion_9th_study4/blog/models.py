from django.db import models

class Blog(models.Model):
    # title 변수는 최대 길이 200인 짧은 문자열 형식으로 정의
    title = models.CharField(max_length=200)
    #pub_date 변수는 날짜 형식으로 정의
    pub_date = models.DateField('data published')
    #body 변수는 긴 문자열 형식으로 정의
    body = models.TextField()

    def __str__(self):
        return self.title
