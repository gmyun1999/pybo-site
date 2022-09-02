from django.urls import path

from . import views

app_name = 'pybo'
# path()함수에서 첫번쨰 인자는 경로가 아닌 요청받은 주소이다
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create')
]
