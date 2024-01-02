// Function to fetch data from the API
async function fetchData() {
  try {
    const response = await fetch('http://127.0.0.1:8000/get_data');
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    return [];
  }
}

// Function to display books on the main page
async function displayBooks() {
  const bookListContainer = document.querySelector('.book-list');

  // Fetch data from the API
  const books = await fetchData();

  // Display books in the DOM
  books.forEach(book => {
    const bookCard = document.createElement('div');
    bookCard.classList.add('book-card');

    // Use a placeholder image if cover_image is not available
    const imageUrl = book.cover_image || 'placeholder-image.jpg';

    bookCard.innerHTML = `
      <img src="${imageUrl}" alt="${book.title}" onclick="openBook('${book.id}')">
      <h4>${book.title}</h4>
      <p>Author: ${book.author}</p>
    `;
    bookCard.addEventListener('click', () => openBook(book.id));
    bookListContainer.appendChild(bookCard);
  });
}

// Function to handle book click
function openBook(bookId) {
  // Redirect to the book details page with the book ID
  window.location.href = `bookDetails.html?bookId=${bookId}`;
}

// Call the displayBooks function to load and display books
displayBooks();
