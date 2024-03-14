from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name="post_list"),
    path('draft/', views.DraftPostView.as_view(), name="draft_list"),
    path('post/<int:pk>/', views.PostdetailView.as_view(), name= "post_detail"),
    path('post/<int:pk>/postpublish/', views.postpublish, name="postpublish"),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name="edit_post"),
    path('post/<int:pk>/comment/', views.AddComment, name="add_comment"),
    path('comment/<int:pk>/approve/', views.Commentapprove, name="approve_cmt"),
    path('comment/<int:pk>/remove/', views.Commentremove, name="remove_cmt"),
    path('post/<int:pk>/remove/', views.PostRemoveView.as_view(), name="remove_post"),
    path('post/new/', views.CreatePostView.as_view(), name= "CreatePostView"),
]

