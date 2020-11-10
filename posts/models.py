from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model) :
    # 아래는 Table을 만드는 과정과 유사
    # author, body, created_at이라는 column을 만드는 것
    # django model을 검색하면 다양한 종류의 field를 확인할 수 있음
    # author = models.CharField(max_length = 100) # 짧은 글자
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField() # 긴 글자
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self) :
        # return f'{self.author} : {self.body}' 를 아래와 같이 바꾼다.
        if self.user:
            return f'{self.user.get_username()} : {self.body}'

        return f'{self.body}'
    
