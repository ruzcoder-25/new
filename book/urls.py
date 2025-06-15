
from django.urls import path

from book import views

urlpatterns = [
    # book
    path('',views.book_list,name='book-list'),
    path('create/',views.create_book,name='create-book'),
    path('book/<int:pk>',views.book_detail,name='book-detail'),
    path('update/<int:pk>',views.update_book,name='update-book'),
    path('delete/<int:pk>',views.delete_book,name='delete-book'),

    # author

    path('author/',views.author_list,name='author-list'),
    path('create_auth/',views.create_author,name='create-author'),
    path('detail_auth/<int:pk>/',views.author_detail,name='author-detail'),
    path('update_auth/<int:pk>/',views.author_update,name='author-update'),
    path('delete_auth/<int:pk>/',views.delete_author,name='author-delete'),
]