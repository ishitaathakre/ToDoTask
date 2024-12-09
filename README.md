# To-Do Reminder App

A simple To-Do reminder app that exposes RESTful APIs for adding, displaying, editing, deleting tasks, and deleting all tasks.

## Features

1. **Add a new To-Do Task**  
   Allows users to create a new task with a description.

2. **Display list of To-Do Tasks**  
   Retrieves all existing tasks and displays them.

3. **Edit or delete a particular To-Do Task**  
   Provides functionality to edit the details of an existing task or delete it.

4. **Delete all To-Do Tasks**  
   Allows for the deletion of all tasks at once.

## Tech Stack

- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Testing**: Pytest
- **Hosting**: Railway

## Directory Structure
The directory structure for this To-Do application is organized as follows:

```
todo_app/
├── app/                    # Main application code
│   ├── __init__.py         # Initializes the app and registers components
│   ├── routes.py           # Defines the API routes (GET, POST, PUT, DELETE)
│   ├── models.py           # Contains the database models (To-Do Task)
│   ├── db.py               # Handles database connection and configuration
├── tests/                  # Contains test files for the application
│   ├── test_routes.py      # Contains test cases for API routes
├── requirements.txt        # Lists all the required dependencies for the project
├── config.py               # Configuration file for app settings
├── .env                    # Example environment file
└── run.py                  # Entry point for running the application
```

## Requirements

To run this app, you need to install the required dependencies:

```bash
pip install -r requirements.txt
```

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ishitaathakre/ToDoTask.git
```
### 2. Install Dependencies
Use the requirements.txt file to install dependencies:
```
pip install -r requirements.txt
````

### 3. Configure Environment Variables
Create a .env file in the project root with the following configuration: Configure DATABASE_URL if you want to use PostgreSQL:

```
FLASK_APP=run.py
DATABASE_URL=<your-postgresql-database-url>
```
I have given an example `.env` file.




# API Endpoints

This To-Do reminder app exposes the following RESTful APIs:

## 1. Add a New To-Do Task

**Endpoint:** `POST /`

**Description:** Adds a new to-do task.

---

### 2. Display List of To-Do Tasks
**Endpoint**: `GET /`

**Description**: Retrieves a list of all to-do tasks.

---

### 3. Edit a Particular To-Do Task
**Endpoint**: `PUT /<task_id>`

**Description**: Updates a specific to-do task.

---

### 4. Delete a Particular To-Do Task
**Endpoint**: `DELETE /<task_id>`

**Description**: Deletes a specific to-do task.

---

### 5. Delete All To-Do Tasks
**Endpoint**: `DELETE /delete_all`

**Description**: Deletes all to-do tasks.

# Running
### 1. Run the Server
Start the development server locally:
```bash
flask run
```
If this gives an error you can run the following command:
```bash
python -m flask run
```

### 2. Access the App
 Visit http://127.0.0.1:5000/ to interact with the application.


# Testing

This application includes test cases for all the API endpoints developed. To ensure the functionality and correctness of the app, follow the instructions below to run the tests.

## Running the Tests

### Unit Tests
The tests are written using the `pytest` framework. You can run the tests using the following command:

```bash
pytest tests/
```

If this gives an error you can try running the following command:

```
python -m pytest tests/
```

This command will automatically discover and run all test cases in the project.
