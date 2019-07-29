from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos') 
    # User 테이블과 관계맺음. on_delete: 연결된 모델삭제될경우 -> 하위객체도 같이 삭제

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default = 'photos/no_image.png')
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-updated']     #내림차순으로 정렬


    def __str__(self): 
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])
        # 상세 페이지 주소 반환              # args : 여러값을 리스트로 전달-> URL만드는데 필요한 pk값 전달
        # reverse 메소드 : URL 패턴 이름을 가지고 해당 패턴을 찾아 주소를 만들어주는 함수.




