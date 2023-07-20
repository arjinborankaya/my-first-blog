from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.postDetail.as_view(), name='post_detail'),
    path('post/new/', views.postNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.postEdit.as_view(), name='post_edit'),
    path('drafts/', views.postDraftList.as_view(), name='post_draft_list'),
    path('post/<pk>/publish/', views.postPublish.as_view(), name='post_publish'),
    path('post/<pk>/remove/', views.postRemove.as_view(), name='post_remove'),
    path('post/<int:pk>/comment/', views.addCommentToPost.as_view(), name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.commentApprove.as_view(), name='comment_approve'),
    path('comment/<int:pk>/remove/', views.commentRemove.as_view(), name='comment_remove'),
]