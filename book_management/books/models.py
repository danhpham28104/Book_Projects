from django.db import models   #Nhập Các Thư Viện

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):   # Định nghĩa một lớp Book
    name = models.CharField(max_length=100) #Dùng để lưu trữ chuỗi ký tự có độ dài cố định tối đa 100 kí tự
    author = models.ForeignKey(Author, on_delete=models.CASCADE)   # lưu trữ tên tác giả sách
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)     # lưu trữ thể loại sách
    quantity = models.IntegerField()    # lưu trữ số lượng sách
    description = models.TextField()    # lưu trữ mô tả chi tiết sách

    def __str__(self):
        return self.name   
