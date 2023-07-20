from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostNew.as_view(), name='post_new'),
    path('post/new/', views.PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('drafts/', views.PostDraftList.as_view(), name='post_draft_list'),
    path('post/<pk>/publish/', views.PostPublish.as_view(), name='post_publish'),
    path('post/<pk>/remove/', views.PostRemove.as_view(), name='post_remove'),
    path('post/<int:pk>/comment/', views.AddCommentToPost.as_view(), name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.CommentApprove.as_view(), name='comment_approve'),
    path('comment/<int:pk>/remove/', views.CommentRemove.as_view(), name='comment_remove'),
]