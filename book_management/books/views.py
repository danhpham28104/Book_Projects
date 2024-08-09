from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Genre, Author
from .forms import BookForm

# định nghĩa các hành động mà trang web thực hiện khi người dùng tương tác với giao diện
def index(request):
    total_books = Book.objects.count()   # tổng số sách
    borrowed_books = 0   # số sách đã mượn 
    available_books = total_books - borrowed_books  # số sách còn lại
    books = Book.objects.all()  # Lấy tất cả sách để hiển thị trên trang chính
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)   # Trả về trang chính với các thông tin tổng quan về sách

def books_list(request):
    search_query = request.GET.get('search', '')   # Lấy từ khóa tìm kiếm từ yêu cầu GET
    selected_genre = request.GET.get('genre', '')   # Lấy thể loại sách đã chọn từ yêu cầu GET
     
     # Lọc sách dựa trên từ khóa tìm kiếm tên hoặc thể loại, hoặc lấy tất cả sách nếu không có điều kiện lọc
    if search_query:
        books = Book.objects.filter(name__icontains=search_query)
    elif selected_genre:
        books = Book.objects.filter(genre__name=selected_genre)
    else:
        books = Book.objects.all()

    genres = Genre.objects.values_list('name', flat=True).distinct()
    context = {
        'books': books,
        'genres': genres,
        'selected_genre': selected_genre,
    }
    return render(request, 'books.html', context)   # Trả về danh sách sách với các thông tin lọc

def add_book(request):
    if request.method == 'POST':   # Kiểm tra yêu cầu khi người dùng gửi form
        name = request.POST['name']   # tên
        author_name = request.POST['author']   # tác giả
        genre_name = request.POST['genre']   # thể loại
        quantity = request.POST['quantity']   # số lượng
        description = request.POST['description']   # mô tả sách

# Tìm kiếm đối tượng trong cơ sở dữ liệu 
        author, created = Author.objects.get_or_create(name=author_name)
        genre, created = Genre.objects.get_or_create(name=genre_name)
        
#  tạo mới nếu không tồn tại (dùng cho tác giả và thể loại)
        new_book = Book(name=name, author=author, genre=genre, quantity=quantity, description=description)
        new_book.save()   # lưu dữ liệu mới
        return redirect('books_list')  # Chuyển hướng đến trang danh sách sách sau khi thêm sách mới
    return render(request, 'add_book.html')  #Trả về form thêm sách nếu form ko đúng yêu cấu

def update_book(request, pk):
    # Lấy đối tượng sách theo khóa chính (PK), hoặc trả về lỗi 404 nếu không tìm thấy sách
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':  # Kiểm tra khi người dùng gửi form cập nhật)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_list')  # Hoặc 'index' tùy theo yêu cầu
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form, 'book': book})  # Trả về form cập nhật sách với dữ liệu của sách

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')   # Chuyển hướng đến trang danh sách sách sau khi xóa sách
    return render(request, 'books.html')

def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_details.html', {'book': book})   # Trả về trang chi tiết sách với thông tin sách

