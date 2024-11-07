# Todo API

## Overview

This API provides endpoints to manage to-do items, including creating, reading, updating, and deleting tasks. It also supports user authentication and authorization with different user roles (such as "admin") to control access to certain endpoints.

## Features

- **User Authentication**: Token-based authentication to secure endpoints.
- **Admin Control**: Only users with admin roles can access certain admin endpoints.
- **CRUD Operations for Todos**: Create, read, update, and delete tasks.
- **User Management**: Endpoints for user registration, password changes, and updating phone numbers.

## Tech Stack

- **FastAPI**: Framework for building the API.
- **JWT Authentication**: For secure token-based authentication.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database for data storage.

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL

### Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Setup**:
   - Create a `.env` file to set environment variables such as `SECRET_KEY`, `DATABASE_URL`, and `ALGORITHM`.

4. **Run Migrations**:
   - Initialize and migrate the database (e.g., using Alembic if configured).

5. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Authentication

- **Create a User**  
  - `POST /auth/`
  - Registers a new user.

- **Login**  
  - `POST /auth/token`
  - Logs in a user and returns a JWT token.

### Admin Endpoints (Protected)

- **Get All Todos**  
  - `GET /admin/todo`
  - Returns all todos. Requires an admin role.

- **Delete a Todo by ID**  
  - `DELETE /admin/todo/{todo_id}`
  - Deletes a todo item by ID. Requires an admin role.

### Todos (User-Specific)

- **Get All Todos for User**  
  - `GET /todos/`
  - Returns all todos associated with the authenticated user.

- **Get Todo by ID**  
  - `GET /todos/todo/{todo_id}`
  - Returns a specific todo item for the authenticated user.

- **Create a Todo**  
  - `POST /todos/todo`
  - Creates a new todo item for the authenticated user.

- **Update a Todo by ID**  
  - `PUT /todos/todo/{todo_id}`
  - Updates a todo item for the authenticated user.

- **Delete a Todo by ID**  
  - `DELETE /todos/todo/{todo_id}`
  - Deletes a todo item for the authenticated user.

### User Profile

- **Get User Profile**  
  - `GET /user/`
  - Retrieves the profile of the authenticated user.

- **Change Password**  
  - `PUT /user/password`
  - Updates the user's password.

- **Update Phone Number**  
  - `PUT /user/phonenumber/{phone_number}`
  - Updates the phone number of the authenticated user.

## Error Handling

- **401 Unauthorized**: Returned when a user fails authentication or lacks permission.
- **404 Not Found**: Returned when a resource is not found (e.g., a todo item).
- **500 Internal Server Error**: Returned when there’s a server-side error.

## Security

This API uses JWT tokens for authentication, with role-based access control for administrative routes.
