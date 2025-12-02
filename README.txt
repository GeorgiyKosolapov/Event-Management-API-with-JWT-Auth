# Event Management API

## Key Features

* **User Authentication:** Secure JWT-based authentication (Sign up, Login, Token Refresh).
* **Events Management:** Full CRUD operations for events (Create, Read, Update, Delete).
* **Event Registration:** Logic for users to join or leave events.
* **Permissions System:**
    * **Guests:** Read-only access to event lists.
    * **Authenticated Users:** Can create events and join others.
    * **Organizers/Admins:** Full control over their events.
* **Documentation:** Auto-generated interactive Swagger & ReDoc UI.
* **Containerization:** Fully dockerized application (Docker & Docker Compose).

## 🛠 Tech Stack

* **Language:** Python 3.10
* **Framework:** Django 5.0 + Django REST Framework
* **Database:** SQLite (Default) / Ready for PostgreSQL
* **Auth:** Simple JWT
* **Docs:** drf-yasg (Swagger/OpenAPI)
* **Tools:** Docker, Git

## 📂 Project Structure

```text
.
├── api/                # API Application (Models, Views, Serializers)
├── django_main/        # Project Configuration (Settings, WSGI, ASGI)
├── Dockerfile          # Docker build instructions
├── docker-compose.yml  # Container orchestration
├── manage.py           # Django command-line utility
├── requirements.txt    # Python dependencies
└── .env                # Environment variables (not in repo)

## 📦 How to Run
Prerequisites
Docker installed on your machine.

Quick Start (Recommended)
Clone the repository:

git clone <your-repository-url>
cd <repository-name>
Setup Environment Variables: Create a .env file from the example:

cp .env.example .env
(Or manually create .env and copy content from .env.example)

Build and Run:

docker-compose up --build
Access the API:

Swagger UI (Docs): http://127.0.0.1:8000/swagger/

API Root: http://127.0.0.1:8000/api/

##🧪 Testing
You can test the API endpoints directly via Swagger UI or Postman.

Test Flow:
    1. Register: POST /api/users/
    2. Login: POST /api/token/ (Get access token)
    3. Authorize: Click Authorize in Swagger and enter Bearer <your_token>
    4. Create Event: POST /api/events/
    5. Join Event: POST /api/events/{id}/join/

##👤 Author
Developed by Georgiy Kosolapov