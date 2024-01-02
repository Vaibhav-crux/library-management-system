function addBook() {
  // Get the values from the form
  var title = document.getElementById("title").value;
  var author = document.getElementById("author").value;
  var publisher = document.getElementById("publisher").value;
  var publicationDate = document.getElementById("publicationDate").value;
  var genre = document.getElementById("genre").value;
  var coverImage = document.getElementById("coverImage").value;
  var synopsis = document.getElementById("synopsis").value;
  var language = document.getElementById("language").value;
  var reviews = document.getElementById("reviews").value;

  // Create a JSON object with the form data
  var formData = {
      title: title,
      author: author,
      publisher: publisher,
      publication_date: publicationDate,
      genre: genre,
      cover_image: coverImage,
      synopsis: synopsis,
      language: language,
      reviews: reviews
  };

  // Perform a fetch request to the server
  fetch('http://127.0.0.1:8000/add_book', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
  })
  .then(response => response.json())
  .then(data => {
      console.log('Success:', data);
      // Redirect to main.html or perform other actions as needed
      window.location.href = 'main.html';
  })
  .catch(error => {
      console.error('Error:', error);
  });
}
