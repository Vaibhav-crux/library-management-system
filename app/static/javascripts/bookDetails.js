
function submitDetails(event) {
  event.preventDefault();

  var fullName = document.getElementById('fullName').value;
  var email = document.getElementById('email').value;
  var phoneNumber = document.getElementById('phone').value;
  var address = document.getElementById('address').value;
  var dateOfBirth = formatDate(document.getElementById('dob').value); 
  var libraryCardNumber = document.getElementById('libraryCard').value;
  var gender = document.getElementById('gender').value;
  var lastSubmitDate = formatDate(document.getElementById('lastSubmitDate').value); 


  var formData = {
    full_name: fullName,
    email: email,
    phone_number: phoneNumber,
    address: address,
    date_of_birth: dateOfBirth,
    library_card_number: libraryCardNumber,
    gender: gender,
    last_submit_date: lastSubmitDate
  };

  fetch('http://127.0.0.1:8000/submit_details', {
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
      // window.location.href = 'main.html';
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

document.getElementById('bookDetailsForm').addEventListener('submit', submitDetails);

function formatDate(inputDate) {
  var dateParts = inputDate.split("-");
  return dateParts[2] + "-" + dateParts[1] + "-" + dateParts[0];
}


async function populateBookDetails() {
  const urlParams = new URLSearchParams(window.location.search);
  const bookId = urlParams.get('bookId');

  try {
    const response = await fetch(`http://127.0.0.1:8000/get_book_title/${bookId}`);
    const data = await response.json();

    // Set the book title as read-only
    const bookNameField = document.getElementById('bookName');
    bookNameField.value = data.book_title;
    bookNameField.setAttribute('readonly', 'true');
  } catch (error) {
    console.error('Error fetching book title:', error);
  }
}

// Call the function to populate book details when the page loads
populateBookDetails();
