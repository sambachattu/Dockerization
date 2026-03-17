# Docker Full-Stack Project

A containerized full-stack application running a **React (Vite)** frontend and an **Express.js** backend, orchestrated with Docker Compose.

---

## Project Structure

```
Docker/
├── docker-compose.yml
├── .dockerignore
├── react-docker/          # React + Vite frontend
│   ├── Dockerfile
│   ├── src/
│   ├── public/
│   ├── vite.config.js
│   └── package.json
└── node-docker/           # Express.js backend
|   ├── Dockerfile
|   ├── server.js
|   └── package.json
└── fastapi-docker/        # FastAPI backend
    ├── Dockerfile
    ├── main.js
    └── requirements.txt
```

---

## Services

| Service | Tech Stack | Host Port | Container Port |
|---|---|---|---|
| `react-app` | React + Vite + Nginx | `3000` | `80` |
| `express-app` | Node.js + Express | `8000` | `8000` |
| `fastapi-app` | python + FastAPI | `1010` | `1010` |

---

## Prerequisites

- [Docker](https://www.docker.com/get-started) v20+
- [Docker Compose](https://docs.docker.com/compose/) v2+

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Docker
```

### 2. Build and start all services

```bash
docker compose up --build
```

### 3. Access the apps

| App | URL |
|---|---|
| React Frontend | http://localhost:3000 |
| Express Backend | http://localhost:8000 |
| FastAPI Backend | http://localhost:1010 |

### 4. Stop the services

```bash
docker compose down
```

---

## How It Works

### Frontend — React + Vite + Nginx (Multi-Stage Build)

The React app uses a **two-stage Dockerfile**:

- **Stage 1 (builder):** Uses `node:22-alpine` to install dependencies and run `npm run build`, producing optimized static files in `/app/dist`.
- **Stage 2 (serve):** Uses `nginx:alpine` to serve the static files. This keeps the final image small (~20MB) with no Node.js included.

```dockerfile
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Backend — Express.js

A standard Node.js Express server containerized and exposed on port `8000`.

### Docker Compose

```yaml
version: "3.8"
services:
  react-app:
    build: ./react-docker
    ports:
      - 3000:80        # host:container
  express-app:
    build: ./node-docker
    ports:
      - 8000:8000
  fastapi-app:
    build: ./fastapi-docker
    ports:
      -1010:1010
```

---

## Useful Commands

```bash
# Build images without starting containers
docker compose build

# Start in detached (background) mode
docker compose up -d

# View running containers
docker ps

# View logs for a specific service
docker compose logs react-app
docker compose logs express-app

# Rebuild a single service
docker compose up --build react-app

# Stop and remove containers + networks
docker compose down

# Stop and remove containers + volumes
docker compose down -v

# To build individual containers
docker build -t app-name .

# To start individual containers
docker run -p 8000:8000 app-name


```

---

## .dockerignore

The following are excluded from the Docker build context to keep images lean and builds fast:

```
node_modules
build
.git
.env
*.md
```

---


## Troubleshooting

**Frontend not loading on port 3000?**
- Ensure no other process is using port 3000: `lsof -i :3000`
- Check container logs: `docker compose logs react-app`

**Backend not responding on port 8000?**
- Check your `server.js` is listening on `0.0.0.0`, not just `localhost`
- Check logs: `docker compose logs express-app`

**Changes not reflecting after rebuild?**
- Force a clean rebuild: `docker compose up --build --force-recreate`
