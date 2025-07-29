# Tasks management App 

A full-stack todo application with FastAPI backend and Next.js frontend, running on Docker.

## Features

- 🔐 User authentication with JWT tokens
- ✅ Create, read, update, and delete tasks
- 🎨 Modern UI with Tailwind CSS
- 📱 Responsive design
- 🚀 Fast development with Next.js 14
- 🐍 FastAPI backend with PostgreSQL
- 🐳 Docker support for easy deployment

## Architecture

- **Frontend**: Next.js 14 with TypeScript and Tailwind CSS
- **Backend**: FastAPI with SQLAlchemy and PostgreSQL
- **Database**: PostgreSQL 16
- **Containerization**: Docker and Docker Compose

## Quick Start with Docker

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. Start all services with Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Project Structure

```
todo-app/
├── frontend/              # Next.js frontend application
│   ├── app/              # Next.js app directory
│   ├── components/       # React components
│   ├── lib/             # Utility functions
│   ├── types/           # TypeScript types
│   ├── Dockerfile       # Frontend Docker configuration
│   └── package.json     # Frontend dependencies
├── backend/              # FastAPI backend application
│   ├── app/             # FastAPI application code
│   ├── dockerfile       # Backend Docker configuration
│   └── requirements.txt # Backend dependencies
├── compose.yaml         # Docker Compose configuration
└── README.md           # This file
```

## Development

### Frontend Development

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open http://localhost:3000 in your browser.

### Backend Development

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:
   ```bash
   uvicorn app.api.main:app --reload
   ```

4. Access the API at http://localhost:8000

## API Endpoints

### Authentication
- `POST /auth/login` - User login

### Tasks (requires authentication)
- `GET /tasks/` - Get all tasks
- `GET /tasks/{id}` - Get specific task
- `POST /tasks/` - Create new task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task

## Environment Variables

### Frontend
- `NEXT_PUBLIC_API_URL` - Backend API URL (default: http://localhost:8000)

### Backend
- `DATABASE_URL` - PostgreSQL connection string

## Docker Commands

```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Rebuild and start
docker-compose up --build

# Stop all services
docker-compose down

# View logs
docker-compose logs

# View logs for specific service
docker-compose logs frontend
docker-compose logs backend
docker-compose logs db
```
