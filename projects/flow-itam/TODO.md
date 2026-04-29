# Flow ITAM — Python Project TODO

## 🎯 Goal

Build a simple IT Asset Management system using:

- Python 3.12+ (CLI first)
- SQLAlchemy Core
- Alembic
- Pydantic v2
- Click
- SQL Server

Focus:

- Learn deeply
- Keep architecture clean
- Enable future Web API + monetization

---

# ✅ Phase 0 — Repo Setup (Day 1)

- [x] Decide on layout: standalone repo (`flow-itam`) or sub-project under `python-projects/projects/flow-itam/`
- [x] Initialize Python project
  - [x] `py -m venv venv` (or `uv venv`)
  - [x] `pyproject.toml` with project metadata + dependencies

- [x] Create package layout under `src/flow_itam/`:
  - [x] `domain/`
  - [x] `application/`
  - [x] `infrastructure/`
  - [x] `cli/`

- [x] Add `tests/` mirroring the package layout
- [x] Configure `ruff`, `mypy`, and `pytest` via `pyproject.toml`
- [x] Add `.env.example` and `.gitignore`

---

# 🧱 Phase 1 — Domain Modeling (Days 2–3)

Define core entities as **Pydantic v2 models** in `src/flow_itam/domain/`:

- [ ] `Asset`
  - id, name, asset_type, serial_number, purchase_date

- [ ] `User`
  - id, name, email (`EmailStr`)

- [ ] `Assignment`
  - asset_id, user_id, assigned_at, returned_at

- [ ] `Location` (optional)

- [ ] `Vendor` (optional)

- [ ] Use `pydantic.BaseModel` for entities; consider `model_config = ConfigDict(frozen=True)` for value-object semantics
- [ ] Add field validation (constrained types, required fields, custom validators)
- [ ] Keep domain models free of DB and HTTP concerns — no SQLAlchemy imports here

---

# 🗄️ Phase 2 — Database Setup (Days 3–5)

- [ ] Spin up SQL Server (Docker preferred: `mcr.microsoft.com/mssql/server:2022-latest` via `docker compose up -d db`)
- [ ] Install ODBC Driver 18 for SQL Server on the host (required by `pyodbc`)

- [ ] Create database: `itam_dev`

- [ ] Define schema as SQLAlchemy Core `Table` objects in `infrastructure/db/schema.py`:
  - [ ] `assets`
  - [ ] `users`
  - [ ] `assignments`

- [ ] Initialize Alembic (`alembic init alembic/`)
  - [ ] Configure `alembic.ini` / `env.py` to read `DATABASE_URL` from env
  - [ ] Point `target_metadata` at the SQLAlchemy `MetaData` from `schema.py`

- [ ] Generate + review initial migration (`alembic revision --autogenerate -m "init"`)
- [ ] Apply migration (`alembic upgrade head`)

---

# ⚙️ Phase 3 — Infrastructure (SQLAlchemy Core) (Days 5–7)

- [ ] Add deps: `sqlalchemy`, `alembic`, `pyodbc`, `pydantic`, `pydantic-settings`, `click`
- [ ] Connection string format: `mssql+pyodbc://user:pass@host/itam_dev?driver=ODBC+Driver+18+for+SQL+Server`

- [ ] Create engine + connection factory in `infrastructure/db/engine.py`

- [ ] Implement repositories using **Core only** (`select`, `insert`, `update`) — no ORM `Session`:
  - [ ] `AssetRepository`
  - [ ] `UserRepository`
  - [ ] `AssignmentRepository`

- [ ] Write basic queries:
  - [ ] Insert asset
  - [ ] Get all assets
  - [ ] Assign asset
  - [ ] Get assigned/unassigned assets

- [ ] Map row results → domain Pydantic models at the repository boundary (rows never leak upward)

---

# 🧠 Phase 4 — Application Layer (Days 7–10)

- [ ] Create services in `application/`:
  - [ ] `AssetService`
  - [ ] `AssignmentService`

- [ ] Implement use cases:
  - [ ] `add_asset`
  - [ ] `assign_asset`
  - [ ] `list_assets`
  - [ ] `get_audit_report`

- [ ] Inject repositories via constructor — no module-level singletons or globals
- [ ] Keep business logic OUT of the CLI

---

# 🖥️ Phase 5 — CLI Interface (Days 10–12)

- [ ] Setup CLI entry point in `cli/__main__.py` using Click
  - [ ] Add `[project.scripts]` entry: `flow-itam = "flow_itam.cli:main"` in `pyproject.toml`
  - [ ] Wire commands as a `@click.group()` with sub-`@cli.command()` decorators

- [ ] Implement commands:
  - [ ] `flow-itam add-asset`
  - [ ] `flow-itam list-assets`
  - [ ] `flow-itam assign-asset`
  - [ ] `flow-itam audit-report`

- [ ] Basic console output (keep simple — `click.echo`)

---

# 📊 Phase 6 — Reporting (Days 12–14)

- [ ] Build:
  - [ ] Unassigned assets report
  - [ ] Assets by user
  - [ ] Assignment history

- [ ] Optimize at least one query — use `SET STATISTICS IO, TIME ON` (or SSMS's actual execution plan) and tune the SQL behind a SQLAlchemy Core expression (learn the Core API deeply)

---

# 🧪 Phase 7 — Polish & Learn (Ongoing)

- [ ] Add structured logging (stdlib `logging`; `structlog` optional)
- [ ] Add configuration via `pydantic-settings` (reads `.env`)
- [ ] Improve error handling — define domain exceptions, map them at boundaries
- [ ] Write `pytest` tests:
  - [ ] Unit tests for services (mocked repositories)
  - [ ] Integration tests against a real SQL Server test DB (a disposable `mcr.microsoft.com/mssql/server` container, or a dedicated test database)

- [ ] Refactor messy code
- [ ] Document key decisions in README

---

# 🚀 Phase 8 — API Transition (Later)

(Only after the CLI feels solid)

- [ ] Add `api/` package using **FastAPI** — Pydantic domain models double as request/response schemas
- [ ] Add routers:
  - [ ] `assets_router`
  - [ ] `assignments_router`

- [ ] Reuse the Application layer (services) — no business logic in routers
- [ ] Auto-generated OpenAPI docs at `/docs` (free with FastAPI)
- [ ] Run with `uvicorn flow_itam.api:app --reload`

---

# 💡 Stretch Goals (Optional)

- [ ] Authentication (JWT via `pyjwt` or `python-jose`)
- [ ] Multi-tenant support
- [ ] Export to CSV (stdlib `csv`)
- [ ] Simple Vue frontend
- [ ] Dockerize app (Dockerfile + `docker-compose.yml` for app + SQL Server)

---

# 🧠 Rules for This Project

- Keep it simple
- Favor clarity over cleverness
- No business logic in CLI or API routers
- Pydantic models are the contract between layers
- Repositories return domain models, not raw rows
- Domain layer never imports from `infrastructure/` or `cli/`
- Learn something every session
- Ship small, often

---

# 🏁 Definition of "Done" (MVP)

- Can add assets
- Can assign assets
- Can view asset list
- Can generate simple report

---

# 🔥 Reminder

This is not just a CLI tool.

You are building:
→ A system
→ A portfolio piece
→ A potential SaaS foundation
