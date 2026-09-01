# Versionskontroll Workflow Project

A Django web application for learning Git workflows, branching strategies, commit conventions, and team collaboration practices. The codebase is intentionally structured to demonstrate all five SOLID principles in a real-world context.

## Features

| Section | What you learn |
|---|---|
| Branching Strategies | GitFlow, Trunk-Based Development, Feature Branch Workflow |
| Commit Conventions | Conventional Commits spec, 10 commit types, good vs. bad examples |
| Collaboration Practices | Pull Requests, Code Reviews, Merge Conflict resolution |
| Documentation | Curated external resources and SOLID principles walkthrough |

## Tech Stack

- **Python / Django 6.0.4** — backend framework
- **SQLite** — default database (zero configuration)
- **Django Templates** — server-rendered HTML

## Project Structure

```
versionskontroll_workflow_project/
├── manage.py
├── versionskontroll_workflow/   # Django project config (settings, urls, wsgi)
└── git_learning/                # Main application
    ├── views.py                 # One view per page
    ├── models.py                # GitResource, LearningNote models
    ├── urls.py                  # URL routing
    ├── templates/git_learning/  # HTML templates
    ├── migrations/
    └── services/
        ├── base_workflow.py         # Abstract base class (LSP)
        ├── branching_service.py     # WorkflowFactory + workflow classes (OCP)
        ├── commit_service.py        # CommitConventionService (SRP)
        ├── collaboration_service.py # CollaborationService (ISP)
        └── workflow_provider.py     # WorkflowProvider facade (DIP)
```

## SOLID Principles in This Codebase

| Principle | Where |
|---|---|
| **S** - Single Responsibility | `branching_service.py`, `commit_service.py` - each class does one thing |
| **O** - Open/Closed | `WorkflowFactory` - add new workflows without changing existing code |
| **L** - Liskov Substitution | `GitFlowWorkflow`, `TrunkBasedWorkflow`, `FeatureBranchWorkflow` all extend `BaseWorkflow` |
| **I** - Interface Segregation | `CollaborationService` and `CommitConventionService` are separate, focused classes |
| **D** - Dependency Inversion | `views.py` only imports `WorkflowProvider` - never concrete service classes |

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone <repo-url>
cd versionskontroll_workflow_project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

### Optional: Create a superuser for the Django admin

```bash
python manage.py createsuperuser
```

Admin panel is available at `/admin/`.

## Pages

| URL | Description |
|---|---|
| `/` | Home - topic overview cards and stats |
| `/branching/` | Branching strategies with visual comparisons |
| `/commits/` | Commit convention reference and examples |
| `/collaboration/` | PR guide, code review checklist, merge conflict steps |
| `/documentation/` | External resources and SOLID principles reference |

## Database Models.

- **GitResource** - stores categorised learning resources (title, URL, category, ordering)
- **LearningNote** - personal notes organised by topic (branching, commits, merging, pull requests)
