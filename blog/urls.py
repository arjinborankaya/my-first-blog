from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list.as_view(), name='post_list'),
    path('post/<int:pk>/', views.post_detail.as_view(), name='post_detail'),
    path('post/new/', views.post_new.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit.as_view(), name='post_edit'),
    path('drafts/', views.post_draft_list.as_view(), name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish.as_view(), name='post_publish'),
    path('post/<pk>/remove/', views.post_remove.as_view(), name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post.as_view(), name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve.as_view(), name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove.as_view(), name='comment_remove'),
]