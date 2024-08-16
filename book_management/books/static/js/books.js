// Hiển thị danh sách sách
function populateBookTable() {
    const tableBody = document.getElementById('bookTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = ''; // Xóa nội dung hiện tại

    // Giả sử bạn có danh sách books từ backend
    books.forEach(book => {
        const row = tableBody.insertRow();
        row.insertCell(0).textContent = book.name;
        row.insertCell(1).textContent = book.author;
        row.insertCell(2).textContent = book.genre;
        row.insertCell(3).textContent = book.quantity;
    });
}

// Tìm kiếm và lọc sách
function filterBooks() {
    const searchValue = document.getElementById('searchInput').value.toLowerCase().trim();
    const selectedGenre = document.getElementById('filterGenre').value.toLowerCase().trim();
    const tableBody = document.getElementById('bookTable').getElementsByTagName('tbody')[0];

    Array.from(tableBody.rows).forEach(row => {
        const name = row.cells[0].textContent.toLowerCase().trim();
        const author = row.cells[1].textContent.toLowerCase().trim();
        const genre = row.cells[2].textContent.toLowerCase().trim();

        const matchesSearch = name.includes(searchValue) || author.includes(searchValue);
        const matchesGenre = selectedGenre === '' || genre === selectedGenre;

        if (matchesSearch && matchesGenre) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}


// Đăng ký sự kiện tìm kiếm và lọc
document.getElementById('searchInput').addEventListener('input', filterBooks);
document.getElementById('filterGenre').addEventListener('change', filterBooks);
