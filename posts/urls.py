from django.urls import path
# from 다음에 . 은 urls.py를 포함한 현재 위치(posts)를 의미
from . import views

app_name = 'posts'
urlpatterns = [
    # 'posts/'는 kawork의 urls.py에서 이미 언급되어 있기에 여기서는 ''만 입력
    # name = 'index'는 약속된 별칭을 의미 
    path('', views.index, name = 'index'),
    path('<int:post_id>/', views.detail, name = 'detail'), # <type:변수명>/ 
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('<int:post_id>/edit/', views.edit, name = 'edit'),
    path('<int:post_id>/update/', views.update, name = 'update'),
    path('<int:post_id>/delete/', views.delete, name = 'delete'),
    path('<int:post_id>/like/', views.like, name = 'like'),
]
