// Cập nhật tổng quan và danh sách sách
function updateDashboard() {
    const totalBooks = books.reduce((sum, book) => sum + book.quantity, 0);
    const borrowedBooks = 0; // Giả định ban đầu là 0
    const availableBooks = totalBooks - borrowedBooks;

    document.getElementById('totalBooks').textContent = totalBooks;
    document.getElementById('borrowedBooks').textContent = borrowedBooks;
    document.getElementById('availableBooks').textContent = availableBooks;
}

function populateBookTable() {
    const tableBody = document.getElementById('bookTable').getElementsByTagName('tbody')[0];
    books.forEach(book => {
        const row = tableBody.insertRow();
        row.insertCell(0).textContent = book.name;
        row.insertCell(1).textContent = book.author;
        row.insertCell(2).textContent = book.genre;
        row.insertCell(3).textContent = book.quantity;
    });
}

// Gọi hàm để cập nhật giao diện
updateDashboard();
populateBookTable();
