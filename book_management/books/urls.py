from django.urls import path
from . import views

# định nghĩa các đường dẫn URL
urlpatterns = [
    path('', views.index, name='index'),   # trang chính
    path('books/', views.books_list, name='books_list'), # danh sách sách
    path('books/add/', views.add_book, name='add_book'), #  trang thêm sách
    path('update/<int:pk>/', views.update_book, name='update_book'),  # trang cập nhật sách
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/<int:pk>/', views.book_details, name='book_details'),   # trang chi tiết sách
]


# <int:pk> là một tham số động trong URL, đại diện cho khóa chính (primary key) của sách cần thao tác