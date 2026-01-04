# Student Management System

A full-stack web application for managing student records with a FastAPI backend and Streamlit frontend.

## 🚀 Live Demo

**Website URL:** [https://studentmanagmentwebapp-jgdfedzb.b4a.run/](https://studentmanagmentwebapp-jgdfedzb.b4a.run/)

## 📋 Features

- **Add Students**: Create new student records with roll number, name, age, and grade
- **View Students**: Display all registered students in a table format
- **Update Students**: Modify existing student information
- **Delete Students**: Remove student records from the database
- **Search Students**: Find students by name or roll number

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation using Python type annotations

### Frontend
- **Streamlit**: Interactive web application framework
- **Requests**: HTTP library for API communication
- **Pandas**: Data manipulation and display

## 📁 Project Structure

```
Student_Management_System_api/
├── backend/
│   └── main.py              # FastAPI application with REST API endpoints
├── frontend/
│   └── app.py               # Streamlit frontend application
├── Dockerfile               # Docker configuration for deployment
├── pyproject.toml          # Project dependencies
└── README.md               # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.12 or higher
- pip or uv package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Student_Management_System_api
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi[standard]>=0.128.0 python-dotenv>=1.2.1 streamlit>=1.52.2 uvicorn>=0.40.0
   ```

3. **Run the backend API**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

4. **Run the frontend (in a new terminal)**
   ```bash
   cd frontend
   streamlit run app.py
   ```

5. **Access the applications**
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Frontend App: http://localhost:8501

## 🐳 Docker Deployment

The application is containerized using Docker for easy deployment:

```bash
docker build -t student-management-system .
docker run -p 8000:8000 -p 8501:8501 student-management-system
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/students/` | Add a new student |
| GET | `/students/` | Get all students |
| GET | `/students/{roll_number}` | Get student by roll number |
| PUT | `/students/{roll_number}` | Update student information |
| DELETE | `/students/{roll_number}` | Delete a student |
| GET | `/students/search/` | Search students by name or roll number |

## 💡 Usage Examples

### Add a Student
Navigate to "Add Student" in the sidebar, fill in the form, and click "Add Student".

### View All Students
Select "Get Students" from the sidebar to display all registered students.

### Update a Student
Go to "Update Student", enter the roll number and new information, then click "Update Student".

### Delete a Student
Choose "Delete Student", enter the roll number, and confirm deletion.

### Search Students
Use "Search Students" to find students by name or roll number.

## 🚧 Future Enhancements

- [ ] JWT Authentication for secure API access
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] User authentication and authorization
- [ ] Export student data to CSV/PDF
- [ ] Pagination for large datasets
- [ ] Advanced search filters
- [ ] Student profile images

## 👨‍💻 Author

Created as a learning project to demonstrate:
- FastAPI basics and REST API development
- CRUD operations
- Frontend-backend integration
- Containerization with Docker
- Cloud deployment

## 📄 License

This project is open source and available for educational purposes.

---

**Note**: This application uses in-memory storage. Data will be lost when the server restarts. For production use, integrate a persistent database.
