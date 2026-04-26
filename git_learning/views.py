"""
=============================================================================
FILE: views.py - Django Views for Versionskontroll-Workflow
=============================================================================
"""

from django.shortcuts import render
from git_learning.services.workflow_provider import WorkflowProvider

provider = WorkflowProvider()


def home_view(request):
    """Renders the home page with topic overview cards."""
    context = {
        "workflows": [workflow.get_summary() for workflow in provider.get_all_workflows()],
        "topics": [
            {"title": "Branching Strategies", "icon": "🌿",
             "description": "GitFlow, Trunk-Based Development, Feature Branching",
             "url_name": "branching", "color": "emerald", "count": "3 strategies"},
            {"title": "Commit Conventions", "icon": "💾",
             "description": "Write clear, meaningful commit messages",
             "url_name": "commits", "color": "blue", "count": "10 commit types"},
            {"title": "Collaboration Practices", "icon": "🤝",
             "description": "Pull Requests, Code Reviews, Merge Conflicts",
             "url_name": "collaboration", "color": "violet", "count": "3 key practices"},
            {"title": "Documentation", "icon": "📚",
             "description": "Reference links and learning resources",
             "url_name": "documentation", "color": "amber", "count": "All resources"},
        ],
        "stats": [
            {"label": "Workflow Strategies", "value": "3"},
            {"label": "Commit Types", "value": "10"},
            {"label": "Collaboration Guides", "value": "3"},
            {"label": "SOLID Principles", "value": "5"},
        ],
    }
    return render(request, "git_learning/home.html", context)


def branching_view(request):
    """Renders the Branching Strategies page."""
    all_workflows = provider.get_all_workflows()
    workflow_summaries = []
    color_map = {
        "GitFlow": "blue",
        "Trunk-Based Development": "emerald",
        "Feature Branch Workflow": "violet",
    }
    for workflow in all_workflows:
        summary = workflow.get_summary()
        summary["color"] = color_map.get(summary["name"], "gray")
        workflow_summaries.append(summary)
    context = {
        "workflows": workflow_summaries,
        "page_title": "Branching Strategies",
        "page_description": (
            "A branch is a parallel copy of your code where you can safely make changes. "
            "Different teams use different strategies. Here are the three most popular."
        ),
    }
    return render(request, "git_learning/branching.html", context)


def commits_view(request):
    """Renders the Commit Conventions page."""
    context = {
        "commit_types": provider.get_commit_types(),
        "good_examples": provider.get_commit_good_examples(),
        "bad_examples": provider.get_commit_bad_examples(),
        "commit_structure": provider.get_commit_structure(),
        "tips": provider.get_commit_tips(),
        "page_title": "Commit Conventions",
        "page_description": (
            "A Git commit saves a snapshot of your work with a descriptive message. "
            "Great commit messages make your team's history easy to understand."
        ),
    }
    return render(request, "git_learning/commits.html", context)


def collaboration_view(request):
    """Renders the Collaboration Practices page."""
    context = {
        "pr_guide": provider.get_pull_request_guide(),
        "code_review_guide": provider.get_code_review_guide(),
        "merge_conflict_guide": provider.get_merge_conflict_guide(),
        "practices": provider.get_collaboration_practices(),
        "page_title": "Collaboration Practices",
        "page_description": (
            "Git is most powerful as a team tool. Pull Requests, Code Reviews, "
            "and Merge Conflict resolution are the three pillars of team development."
        ),
    }
    return render(request, "git_learning/collaboration.html", context)


def documentation_view(request):
    """Renders the Documentation & Resources page."""
    external_resources = [
        {"title": "Official Git Documentation", "url": "https://git-scm.com/doc",
         "description": "The official comprehensive Git reference. Start here.", "category": "Official",
         "emoji": "📗", "level": "All levels"},
        {"title": "Pro Git Book (free)", "url": "https://git-scm.com/book/en/v2",
         "description": "The definitive free Git book. Available online in many languages.", "category": "Official",
         "emoji": "📘", "level": "Beginner → Advanced"},
        {"title": "Conventional Commits Spec", "url": "https://www.conventionalcommits.org",
         "description": "Official specification for structured commit messages.", "category": "Standard",
         "emoji": "📝", "level": "Intermediate"},
        {"title": "Atlassian Git Tutorials", "url": "https://www.atlassian.com/git/tutorials",
         "description": "Beginner-friendly Git tutorials from Atlassian.", "category": "Tutorial",
         "emoji": "🎓", "level": "Beginner"},
        {"title": "Learn Git Branching (Interactive)", "url": "https://learngitbranching.js.org",
         "description": "Visual, interactive branching tutorial. Highly recommended!", "category": "Interactive",
         "emoji": "🎮", "level": "Beginner"},
        {"title": "GitHub Flow Guide", "url": "https://guides.github.com/introduction/flow/",
         "description": "GitHub lightweight branching strategy for continuous deployment.", "category": "Guide",
         "emoji": "🐙", "level": "Beginner"},
        {"title": "GitFlow Original Article", "url": "https://nvie.com/posts/a-successful-git-branching-model/",
         "description": "Vincent Driessen's 2010 article introducing GitFlow.", "category": "Reference",
         "emoji": "📄", "level": "Intermediate"},
        {"title": "Trunk-Based Development", "url": "https://trunkbaseddevelopment.com",
         "description": "The comprehensive reference for Trunk-Based Development.", "category": "Reference",
         "emoji": "🌴", "level": "Intermediate"},
        {"title": "Oh Shit, Git!?", "url": "https://ohshitgit.com",
         "description": "Practical solutions for common Git mistakes. Extremely useful!", "category": "Troubleshooting",
         "emoji": "🆘", "level": "All levels"},
    ]
    solid_principles = [
        {"letter": "S", "name": "Single Responsibility",
         "plain_english": "Each class does ONE thing only",
         "example_in_app": "GitFlowWorkflow only knows GitFlow. CommitConventionService only knows commits.",
         "file": "branching_service.py, commit_service.py", "color": "blue"},
        {"letter": "O", "name": "Open/Closed",
         "plain_english": "Add new things without changing old things",
         "example_in_app": "Add a new workflow class, register in WorkflowFactory — no existing code changes.",
         "file": "branching_service.py (WorkflowFactory)", "color": "emerald"},
        {"letter": "L", "name": "Liskov Substitution",
         "plain_english": "Child classes can replace parent classes seamlessly",
         "example_in_app": "GitFlow, TrunkBased, FeatureBranch all inherit BaseWorkflow and are interchangeable.",
         "file": "base_workflow.py, branching_service.py", "color": "violet"},
        {"letter": "I", "name": "Interface Segregation",
         "plain_english": "Don't force classes to implement unrelated methods",
         "example_in_app": "CollaborationService and CommitConventionService are separate focused classes.",
         "file": "commit_service.py, collaboration_service.py", "color": "amber"},
        {"letter": "D", "name": "Dependency Inversion",
         "plain_english": "High-level code depends on abstractions, not specifics",
         "example_in_app": "views.py only imports WorkflowProvider — never specific service classes.",
         "file": "workflow_provider.py, views.py", "color": "rose"},
    ]
    context = {
        "external_resources": external_resources,
        "solid_principles": solid_principles,
        "page_title": "Documentation & Resources",
        "page_description": "Your complete reference guide — links, SOLID principles, and everything to master Git.",
    }
    return render(request, "git_learning/documentation.html", context)
