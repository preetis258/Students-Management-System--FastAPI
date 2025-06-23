# 🧑‍🎓 Students Management System — FastAPI

This is a backend web application built with **FastAPI** that provides a RESTful API to manage student information. It allows users to perform various operations on student records with ease. The application is ideal for educational projects, internal tools, or as a learning project for building REST APIs.

## 🔑 Key Features

- Create, retrieve, update, and delete student records
- Data is stored in a simple `JSON` file — no database setup required
- Built-in validation using **Pydantic**:
  - Ensures all fields follow the correct format and constraints
  - Prevents invalid or incomplete data from being processed
- Computes `total_marks` and `average_marks` dynamically

---

## 🛠️ Setup & Run Locally

### ✅ Prerequisites

- Python ≥ 3.10
- `pip` package manager
- Optional but recommended: virtual environment

### 🚀 Steps to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/preetis258/Students-Management-System--FastAPI.git
   cd Students-Management-System--FastAPI
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv sms_venv
   sms_venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```
---

## 📦 Example Usage

### ➕ Create a new student

```bash
curl -X POST http://127.0.0.1:8000/create \
  -H "Content-Type: application/json" \
  -d '{
    "id": "S012",
    "name": "Alice Jason",
    "age": 20,
    "gender": "Female",
    "roll_number": "CS2025001",
    "attendance_percentage": 92.5,
    "subjects": {
      "Mathematics": 85,
      "Physics": 90,
      "computer_science": 88,
      "English": 93,
      "Chemistry": 87
    }
  }'
```

### ✏️ Update only the Mathematics score

```bash
curl -X PUT http://127.0.0.1:8000/edit/S001 \
  -H "Content-Type: application/json" \
  -d '{
    "subjects": {
      "Mathematics": 95
    }
  }'
```

### 📄 View all students

```bash
curl http://127.0.0.1:8000/view_students
```

---

## 📌 Notes

- Updates are **partial** — you can update just one field without resending all data.
- Validations (like age limits and subject marks) are automatically enforced using Pydantic.
- `total_marks` and `average_marks` are computed on the fly and not stored directly.
- All data is read from and written to `students.json`.

---
