# Todo App Frontend

A modern Next.js frontend for the Todo application with authentication and task management.

## Features

- 🔐 User authentication with JWT tokens
- ✅ Create, read, update, and delete tasks
- 🎨 Modern UI with Tailwind CSS
- 📱 Responsive design
- 🚀 Fast development with Next.js 14
- 🐳 Docker support

## Tech Stack

- **Framework**: Next.js 14 with App Router
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **HTTP Client**: Axios
- **Language**: TypeScript

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Docker (optional)

### Local Development

1. Install dependencies:
   ```bash
   npm install
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env.local
   ```
   
   Add your backend API URL:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

### Docker Development

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. The frontend will be available at [http://localhost:3000](http://localhost:3000)

## Project Structure

```
frontend/
├── app/                    # Next.js app directory
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Home page
├── components/            # React components
│   ├── auth/             # Authentication components
│   ├── tasks/            # Task management components
│   └── ui/               # Reusable UI components
├── lib/                  # Utility functions
│   ├── api.ts            # API client
│   └── utils.ts          # Helper functions
├── types/                # TypeScript type definitions
└── Dockerfile            # Docker configuration
```

## API Integration

The frontend communicates with the FastAPI backend through the following endpoints:

- `POST /auth/login` - User authentication
- `GET /tasks/` - Get all tasks
- `POST /tasks/` - Create new task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

## Environment Variables

- `NEXT_PUBLIC_API_URL` - Backend API URL (default: http://localhost:8000) 