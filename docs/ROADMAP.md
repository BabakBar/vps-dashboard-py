# VPS Health Dashboard - Development Roadmap

A modern, lightweight monitoring dashboard for managing multiple Hetzner VPS instances with Coolify-orchestrated containers. Built with FastAPI, Vue/Nuxt, and designed for simplicity with industry best practices.

---

## 🎯 Overall Vision

Monitor your VPS infrastructure in real-time, detect container failures, and receive email notifications—all through a clean API and intuitive web interface. Built for practitioners, not enterprises.

---

## 📋 Phase 1: Foundation (Current)
**Goal:** Core Python infrastructure with modern tooling

- [x] Project setup with `uv` package manager
- [x] Basic system metrics collection (CPU, RAM, Disk)
- [x] File I/O for metric snapshots
- [ ] Migrate to `pyproject.toml` with `uv` as primary package manager
- [ ] Setup project structure: `src/`, tests, and configuration
- [ ] Git repository organization and commit strategy

**Deliverable:** Clean, documented Python foundation ready for FastAPI layer

---

## 📋 Phase 2: Backend API (FastAPI)
**Goal:** RESTful API for VPS and container health checks

### 2.1 Core API Structure
- [ ] FastAPI project initialization
- [ ] Pydantic models for VPS, Container, HealthCheck entities
- [ ] SQLite database schema and ORM (SQLAlchemy)
- [ ] Async/await patterns throughout

### 2.2 VPS Management API
- [ ] `POST /api/vps` - Register a new VPS
- [ ] `GET /api/vps` - List all VPS
- [ ] `GET /api/vps/{id}` - Get single VPS details
- [ ] `DELETE /api/vps/{id}` - Remove VPS from monitoring
- [ ] `PATCH /api/vps/{id}` - Update VPS configuration

### 2.3 Container Monitoring API
- [ ] `GET /api/vps/{id}/containers` - List containers on VPS
- [ ] `GET /api/vps/{id}/containers/{id}/status` - Container health
- [ ] Integration with Docker daemon via SSH/socket

### 2.4 Health Check Engine
- [ ] APScheduler for periodic health checks
- [ ] Background task execution
- [ ] Health check result storage
- [ ] Status aggregation (last check, current state, historical)

**Deliverable:** Fully functional FastAPI backend with container discovery and monitoring

---

## 📋 Phase 3: Notifications (Email)
**Goal:** Alert user of health issues

- [ ] Email service abstraction layer
- [ ] SMTP configuration via environment variables
- [ ] Notification templates (container down, VPS unreachable, etc.)
- [ ] Notification scheduling (avoid spam, batch notifications)
- [ ] Health check trigger → email notification flow

**Deliverable:** Working email notification system

---

## 📋 Phase 4: Frontend (Vue/Nuxt)
**Goal:** Beautiful, real-time monitoring dashboard

### 4.1 Core Dashboard
- [ ] Project setup (Nuxt 3 or Vue 3 + Vite)
- [ ] API client (axios/fetch wrapper)
- [ ] Component library setup (Tailwind CSS)

### 4.2 Pages & Features
- [ ] Dashboard overview (all VPS status at a glance)
- [ ] VPS detail page (containers, metrics history)
- [ ] Add/manage VPS form
- [ ] Settings page (email config, check intervals)
- [ ] WebSocket integration for real-time updates

### 4.3 UI/UX Polish
- [ ] Status indicators (green/yellow/red states)
- [ ] Charts for historical metrics
- [ ] Responsive design (mobile-friendly)

**Deliverable:** Production-ready web dashboard

---

## 📋 Phase 5: Configuration & Deployment (Modern Approach)
**Goal:** Flexible, future-proof configuration

- [ ] Environment variables for development
- [ ] Configuration schema using Pydantic Settings
- [ ] Docker Compose for local development stack
- [ ] Database migrations strategy
- [ ] Health check interval configuration per VPS
- [ ] Revisit innovative config approach (Pydantic, structured configs)

**Deliverable:** Easy-to-deploy, configurable system

---

## 📋 Phase 6: Go Rewrite & Comparison
**Goal:** Learn by comparison, build performance-critical version

- [ ] Rewrite core health check engine in Go
- [ ] Performance benchmarking (Python vs Go)
- [ ] Document comparison: developer experience, maintenance, performance
- [ ] Decide on hybrid approach (Go for checks, FastAPI for API)

**Deliverable:** Go implementation + detailed comparison document

---

## 📋 Phase 7: Production Hardening
**Goal:** Ready for real-world deployment

- [ ] Database backups strategy
- [ ] Error handling and logging system
- [ ] Security hardening (API authentication, SSH key management)
- [ ] Metrics persistence and retention policies
- [ ] Deployment guide (Docker, systemd, cloud providers)
- [ ] Performance optimization if needed

**Deliverable:** Production-ready system

---

## 🔧 Tech Stack (Current)

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Package Manager | `uv` | Modern, fast, dependency resolution |
| Python Config | `pyproject.toml` | Standard, modern Python tooling |
| Web Framework | FastAPI | Async, modern, great docs |
| Database | SQLite (→ PostgreSQL) | Simple start, scalable later |
| Database ORM | SQLAlchemy | Industry standard, async support |
| Task Scheduling | APScheduler | Simple, reliable background tasks |
| Frontend | Vue 3 / Nuxt 3 | Modern, reactive, great DX |
| Styling | Tailwind CSS | Utility-first, minimal config |
| Notifications | SMTP Email | Universal, simple |
| Containers | Docker, Docker Compose | For local dev and deployment |
| SSH/Docker | `paramiko`, `docker-py` | Remote VPS and container access |

---

## 🚀 Success Criteria

- [ ] Simple, elegant codebase anyone can understand
- [ ] Fully async where it matters (I/O bound operations)
- [ ] Comprehensive documentation and examples
- [ ] Open-source ready (license, contributing guide, issue templates)
- [ ] Can deploy to single VPS with Docker Compose
- [ ] Email notifications working reliably
- [ ] Real-time dashboard showing VPS/container status

---

## 📅 Timeline (Estimated)
- **Phase 1:** 1 week (foundation)
- **Phase 2:** 2-3 weeks (API & monitoring)
- **Phase 3:** 1 week (notifications)
- **Phase 4:** 2-3 weeks (frontend)
- **Phase 5:** 1 week (config & deployment)
- **Phase 6:** 2 weeks (Go rewrite & comparison)
- **Phase 7:** Ongoing (hardening as needed)

**Total:** ~10-14 weeks for a complete, production-ready system

---

## 📚 Notes

- Focus on learning and clean code over speed
- Each phase should be fully documented
- Regular commits with clear messages
- Consider making this a learning case study blog post
- Modern tooling (`uv`, async/await, type hints) prioritized throughout
