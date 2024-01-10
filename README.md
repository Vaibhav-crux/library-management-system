# Library Management System

## Overview
The Library Management System is a web application developed to streamline the management of a library's resources. Leveraging modern technologies, the system provides an efficient and user-friendly interface for both librarians and library patrons. The front end is built using HTML, CSS, and JavaScript, while the backend is powered by FastAPI.

## Front End Technologies
### HTML
- **Structure:** HTML (HyperText Markup Language) is used for structuring the content of the web pages. It defines the layout and hierarchy of elements such as headings, paragraphs, forms, and more.

### CSS
- **Styling:** CSS (Cascading Style Sheets) is employed for styling the user interface. It defines the visual presentation of HTML elements, ensuring a visually appealing and consistent design.

### JavaScript
- **Interactivity:** JavaScript adds interactivity to the application, enhancing the user experience. It enables dynamic content updates, form validation, and asynchronous communication with the backend.

## Back End Technology
### FastAPI
- **Web Framework:** FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints, is utilized for the backend. It simplifies API development with automatic data validation, interactive documentation, and asynchronous support.

## Key Features
1. **User Authentication:** Secure login and registration mechanisms for both librarians and patrons.
2. **Catalog Management:** Efficiently manage the library's collection, including adding, updating, and removing books.
3. **User Profile:** Patrons can view their borrowing history, fines, and manage personal details.
4. **Checkout and Return:** Streamlined processes for borrowing and returning books, with automated tracking of due dates.
5. **Search and Filters:** Robust search functionality with filters to easily locate books based on titles, authors, genres, and more.
6. **Notifications:** Automated notifications for overdue books, reservation updates, and other important announcements.
7. **Responsive Design:** Ensures a seamless experience across various devices, including desktops, tablets, and smartphones.

## How to Run
1. **Clone the Repository:** `git clone https://github.com/your-username/library_management.git`
2. **Install Dependencies:** Navigate to the project directory and install dependencies using `pip install -r requirements.txt`.
3. **Run the Application:** Execute `uvicorn main:app --reload` to start the FastAPI server.
4. **Access the Application:** Open your web browser and go to `http://localhost:8000` to access the Library Management System.

## Future Enhancements
1. **Integration with External Databases:** Extend support for different database systems to handle larger datasets efficiently.
2. **User Roles:** Implement role-based access control to restrict certain functionalities based on user roles (librarian, admin, patron).
3. **Book Reviews and Ratings:** Allow patrons to leave reviews and ratings for books, enhancing user engagement.

Feel free to contribute to the project and make it even more robust and feature-rich! If you encounter any issues or have suggestions, please create an issue on the GitHub repository.

## Function Documentation: add_book

This function adds a new book to the database.

### Arguments

- **payload (BookCreate):** The book data to add.
- **db (Session):** The database session.

### Returns

- **dict:** A message indicating whether the book was added or not.

### Raises

- **HTTPException:** If there was an error adding the book.

### Usage

```python
async def add_book(payload: BookCreate, db: Session = Depends(get_db)):
    try:
        # Check if the book already exists
        existing_book = db.query(Book).filter(
            Book.title == payload.title,
            Book.author == payload.author
        ).first()

        if existing_book:
            return {"message": "The book is already added"}

        # Add the book to the database
        db_book = Book(**payload.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return {"message": "Book added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

```

## FastAPI Book Management

This FastAPI application provides endpoints to retrieve all books and delete a book by ID.

### Overview

The application is built with FastAPI, a modern, fast web framework for building APIs with Python. It uses SQLAlchemy for database operations and includes two main routes:
- `GET /get_all_book`: Retrieve information about all books.
- `DELETE /delete_book/{book_id}`: Delete a book by ID.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-book-management.git
   ```

### Changes Made

- Added endpoint to retrieve a specific student by ID.
- Added endpoint to retrieve a list of students with optional pagination.
- Added endpoint to delete a student by ID.
- Added endpoint to update a student by ID.

### Endpoints

- `GET /students/{student_id}`: Retrieve information for a specific student.
- `GET /students/`: Retrieve a list of students.
- `DELETE /students/{student_id}`: Delete a student by ID.
- `PUT /students/{student_id}`: Update a student by ID.

### Usage

1. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```
