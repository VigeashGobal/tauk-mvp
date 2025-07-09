# Tauk MVP

A monorepo containing the Tauk MVP application with multiple services.

## 🏗️ Project Structure

```
tauk-mvp/
├── docker-compose.yml      # Docker services configuration
├── .gitignore             # Git ignore rules
├── .env.example          # Environment variables template
├── README.md             # This file
└── src/
    ├── simulator/        # Simulation service
    ├── backend/          # API backend service
    ├── dashboard/        # Frontend dashboard
    └── services/         # Shared services and utilities
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js (for local development)
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tauk-mvp
   ```

2. **Copy environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your specific values
   ```

3. **Start all services with Docker**
   ```bash
   docker-compose up -d
   ```

4. **Access the services**
   - Dashboard: http://localhost:3000
   - Backend API: http://localhost:8000
   - Simulator: http://localhost:4000
   - Database: localhost:5432

## 🛠️ Development

### Local Development

Each service can be developed independently:

```bash
# Backend
cd src/backend
npm install
npm run dev

# Dashboard
cd src/dashboard
npm install
npm start

# Simulator
cd src/simulator
npm install
npm run dev
```

### Docker Development

```bash
# Start all services
docker-compose up

# Start specific service
docker-compose up backend

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

## 📁 Services

### Backend (`src/backend/`)
- RESTful API server
- Database models and migrations
- Authentication and authorization
- Business logic

### Dashboard (`src/dashboard/`)
- React-based frontend
- Real-time data visualization
- User interface for system management

### Simulator (`src/simulator/`)
- Data simulation service
- Test data generation
- Performance testing utilities

### Services (`src/services/`)
- Shared utilities and libraries
- Common configurations
- Cross-service communication

## 🔧 Configuration

Environment variables are managed through `.env` files. See `.env.example` for available options.

## 📝 Contributing

1. Create a feature branch
2. Make your changes
3. Add tests if applicable
4. Submit a pull request

## 📄 License

[Add your license information here]

## 🤝 Support

For questions and support, please [create an issue](link-to-issues) or contact the development team. 