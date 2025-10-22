# VPS Health Dashboard

A modern, lightweight monitoring dashboard for managing multiple Hetzner VPS instances with Coolify-orchestrated containers. Combines a FastAPI backend with a Vue/Nuxt frontend to provide real-time health checks, container status monitoring, and email notifications.


## Why This Project?

Most VPS monitoring solutions are either too simple or too complex. This dashboard strikes the right balance:

- **Simple enough** to understand and modify
- **Powerful enough** to monitor multiple VPS and their Docker containers
- **Modern** with async patterns, type safety, and current best practices

## Features

- **VPS Health Monitoring** - CPU, RAM, Disk usage tracking
- **Container Status Tracking** - Real-time up/down status for Docker containers via Coolify
- **Email Notifications** - Instant alerts when containers fail or VPS becomes unreachable
- **Web Dashboard** - Beautiful, responsive interface for monitoring your infrastructure
- **RESTful API** - Fully documented API for programmatic access
- **Async-first Design** - Non-blocking I/O for responsive monitoring

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.11+ |
| **Package Manager** | `uv` (modern, fast, zero-config) |
| **Backend Framework** | FastAPI (async, type-safe, auto-docs) |
| **Frontend** | Vue 3 / Nuxt 3 |
| **Database** | SQLite (dev) → PostgreSQL (production) |
| **ORM** | SQLAlchemy with async support |
| **Task Scheduling** | APScheduler |
| **Containerization** | Docker & Docker Compose |
| **Configuration** | `pyproject.toml` + environment variables |
| **Testing** | Pytest with coverage |

## Development Phases

This project is built incrementally with clear phases:

1. **Phase 1: Foundation** (In Progress) - Python infrastructure with `uv` and `pyproject.toml`
2. **Phase 2: Backend API** - FastAPI with VPS and container monitoring
3. **Phase 3: Notifications** - Email alerts for health issues
4. **Phase 4: Frontend** - Vue/Nuxt dashboard
5. **Phase 5: Configuration** - Advanced config management
6. **Phase 6: Go Rewrite** - Performance comparison and hybrid approach
7. **Phase 7: Production** - Hardening and deployment guide
