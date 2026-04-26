"""
=============================================================================
FILE: branching_service.py
PURPOSE: Contains the concrete (real, filled-in) implementations of each
         Git branching strategy. Each strategy is its OWN class with a
         Single Responsibility — just describing that ONE strategy.
=============================================================================

🔷 SOLID PRINCIPLE S — Single Responsibility Principle
   Plain English: "Every class should do ONE thing and ONE thing only."

   Think of it like job specialization:
   - A baker ONLY bakes
   - A cashier ONLY handles money
   - A cleaner ONLY cleans

   In our code:
   - GitFlowWorkflow ONLY knows about GitFlow
   - TrunkBasedWorkflow ONLY knows about Trunk-Based Development
   - FeatureBranchWorkflow ONLY knows about Feature Branching

   ❌ What would be WRONG without this:
      # BAD APPROACH (one giant class doing everything):
      # class AllGitWorkflows:
      #     def get_gitflow_name(self): ...
      #     def get_trunk_branches(self): ...
      #     def get_feature_description(self): ...
      #     def save_to_database(self): ...
      #     def send_email_notification(self): ...
      # PROBLEM: This class does EVERYTHING. If you change one part,
      # you risk breaking completely unrelated parts. It's a mess.

   ✅ Why this is better:
      # GOOD APPROACH (Single Responsibility):
      # Each class does ONE thing. Changes to GitFlow don't affect TrunkBased.
      # Easy to read, test, and maintain!
=============================================================================
"""

# Import our blueprint — GitFlow, TrunkBased, etc. all INHERIT from BaseWorkflow
# "Inherit" means they get the template/structure of BaseWorkflow for free
from git_learning.services.base_workflow import BaseWorkflow


# =============================================================================
# 🌊 GITFLOW WORKFLOW
# Each class inherits from BaseWorkflow — this is the "L" principle in action!
# =============================================================================

class GitFlowWorkflow(BaseWorkflow):
    """
    Represents the GitFlow branching strategy.

    GitFlow is a well-known branching model created by Vincent Driessen in 2010.
    It defines specific branch names and rules for how code flows between them.

    This class inherits from BaseWorkflow — meaning it promises to fill in
    all the abstract methods (get_name, get_description, etc.).

    # WHAT IS INHERITING? 🧬
    # Writing "class GitFlowWorkflow(BaseWorkflow)" means:
    # "GitFlowWorkflow is a TYPE OF BaseWorkflow."
    # It gets all the structure of BaseWorkflow for free, and just
    # fills in the specific details for GitFlow.
    """

    def get_name(self) -> str:
        """
        Returns the display name for this workflow strategy.
        Returns: str - The name "GitFlow"
        """
        return "GitFlow"  # This specific strategy is called "GitFlow"

    def get_description(self) -> str:
        """
        Returns a beginner-friendly description of GitFlow.
        Returns: str - The description text
        """
        # Triple-quoted strings (""") let us write multi-line text easily
        return (
            "GitFlow is a branching strategy that defines strict rules for "
            "how branches are created, named, and merged. It uses two permanent "
            "branches — 'main' (production-ready code) and 'develop' (integration) — "
            "plus temporary branches for features, releases, and hotfixes. "
            "It was designed for teams working on scheduled release cycles."
        )

    def get_branches(self) -> list:
        """
        Returns the list of branches used in GitFlow.
        Returns: list - A Python list of branch name strings
        """
        # A list in Python is written with square brackets: [item1, item2, item3]
        # Each item here is a dict with a name and explanation of each branch
        return [
            {
                "name": "main",  # The primary branch name
                # WHAT IS 'main'? The main branch holds PRODUCTION code —
                # code that real users interact with right now
                "description": "Holds production-ready code. What users see live.",
                "type": "permanent",  # This branch always exists (never deleted)
            },
            {
                "name": "develop",
                # 'develop' is where finished features wait before going to 'main'
                "description": "Integration branch — all features merge here before release.",
                "type": "permanent",
            },
            {
                "name": "feature/*",
                # The * means any name — e.g., "feature/user-login", "feature/dark-mode"
                # WHAT IS A FEATURE BRANCH? A temporary branch for building ONE new feature
                "description": "Temporary branches for building new features. e.g., feature/user-login",
                "type": "temporary",
            },
            {
                "name": "release/*",
                # A release branch is where you prepare code for going live
                "description": "Preparation branch before shipping to production. e.g., release/1.2.0",
                "type": "temporary",
            },
            {
                "name": "hotfix/*",
                # A hotfix is an emergency fix — a bug found in live production code
                "description": "Emergency fixes for production bugs. e.g., hotfix/critical-login-bug",
                "type": "temporary",
            },
        ]

    def get_use_cases(self) -> list:
        """
        Returns situations where GitFlow is most appropriate.
        Returns: list - A list of use case description strings
        """
        return [
            "Projects with scheduled releases (e.g., every 2 weeks)",
            "Teams maintaining multiple versions of software simultaneously",
            "Applications requiring strict quality control before deployment",
            "Open-source projects with formal contribution processes",
            "Enterprise software with compliance or audit requirements",
        ]

    def get_pros(self) -> list:
        """
        Returns the advantages of using GitFlow.
        Returns: list - A list of advantage strings
        """
        return [
            "Very structured — clear rules for every situation",
            "Good for managing multiple versions simultaneously",
            "Easy to understand who is working on what",
            "Release process is well-defined and trackable",
            "Supports parallel development of many features",
        ]

    def get_cons(self) -> list:
        """
        Returns the disadvantages/challenges of GitFlow.
        Returns: list - A list of challenge strings
        """
        return [
            "Can feel complex for small teams or simple projects",
            "Many branches can be overwhelming for beginners",
            "Merging can get complicated after long-running feature branches",
            "Slower release cycle — changes wait for the next release",
            "Not ideal for continuous deployment (releasing multiple times per day)",
        ]


# =============================================================================
# 🌴 TRUNK-BASED DEVELOPMENT
# =============================================================================

class TrunkBasedWorkflow(BaseWorkflow):
    """
    Represents the Trunk-Based Development branching strategy.

    In Trunk-Based Development, everyone commits directly to ONE main branch
    (called the 'trunk' or 'main'). Feature branches are kept very short-lived
    (hours, not weeks). This enables Continuous Integration and fast delivery.

    This class also inherits from BaseWorkflow — fulfilling the Liskov principle:
    it can replace BaseWorkflow anywhere in the code without breaking anything.
    """

    def get_name(self) -> str:
        """Returns the name of this workflow strategy."""
        return "Trunk-Based Development"

    def get_description(self) -> str:
        """Returns a plain-English description of Trunk-Based Development."""
        return (
            "Trunk-Based Development is a strategy where all developers commit "
            "their code to a single shared branch — the 'trunk' (also called 'main'). "
            "Instead of long-lived feature branches, work is broken into tiny pieces "
            "that merge to main within hours or a single day. This enables Continuous "
            "Integration — automatically testing code every time it's merged."
        )

    def get_branches(self) -> list:
        """Returns the minimal set of branches used in Trunk-Based Development."""
        return [
            {
                "name": "main",
                # WHAT IS THE TRUNK? The one central branch where all code lives
                "description": "The single source of truth — all developers work from here.",
                "type": "permanent",
            },
            {
                "name": "short-lived feature branches",
                # These branches exist for hours, not weeks!
                "description": "Optional, very short-lived branches (max 1-2 days) for single tasks.",
                "type": "temporary",
            },
            {
                "name": "release branches",
                # These are created ONLY when you need to deploy a specific version
                "description": "Created from main when stabilizing a specific release version.",
                "type": "temporary",
            },
        ]

    def get_use_cases(self) -> list:
        """Returns situations where Trunk-Based Development works best."""
        return [
            "Teams practicing Continuous Integration and Continuous Deployment (CI/CD)",
            "Products that deploy multiple times per day",
            "Small, experienced teams with high trust and communication",
            "Startups moving fast and needing rapid iteration",
            "Teams using feature flags to hide unfinished features from users",
        ]

    def get_pros(self) -> list:
        """Returns the advantages of Trunk-Based Development."""
        return [
            "Very fast integration — code reaches production quickly",
            "Fewer merge conflicts because branches are tiny",
            "Simpler branch structure — less to manage",
            "Encourages small, frequent commits (easier to review)",
            "Works beautifully with automated testing pipelines",
        ]

    def get_cons(self) -> list:
        """Returns the challenges of Trunk-Based Development."""
        return [
            "Requires strong automated testing — bugs can slip through quickly",
            "Harder for beginners — need discipline to keep commits small",
            "Requires feature flags for hiding work-in-progress from users",
            "Less structured — teams need strong communication habits",
            "Not ideal for teams with strict, slow approval processes",
        ]


# =============================================================================
# 🌿 FEATURE BRANCH WORKFLOW
# =============================================================================

class FeatureBranchWorkflow(BaseWorkflow):
    """
    Represents the Feature Branch Workflow strategy.

    This is often the FIRST workflow beginners learn.
    Every new feature gets its own branch, and when done, a Pull Request
    (a formal request to merge code) is opened for code review.

    # WHAT IS A PULL REQUEST? 🔀
    # A Pull Request (or PR) is a way of asking teammates to review your code
    # before it's merged into the main branch. It's like saying:
    # "Hey team, I finished feature X — please check my work before we add it!"
    """

    def get_name(self) -> str:
        """Returns the name 'Feature Branch Workflow'."""
        return "Feature Branch Workflow"

    def get_description(self) -> str:
        """Returns a plain-English description of the Feature Branch Workflow."""
        return (
            "The Feature Branch Workflow is one of the most beginner-friendly strategies. "
            "Every new feature or bug fix gets its own dedicated branch. Developers work "
            "on their branch without affecting the main code, then open a Pull Request "
            "when done. Teammates review the code, suggest improvements, and only then "
            "is the feature merged (combined) into the main branch."
        )

    def get_branches(self) -> list:
        """Returns the branches typically used in Feature Branch Workflow."""
        return [
            {
                "name": "main",
                "description": "The stable, production-ready branch. Always working code here.",
                "type": "permanent",
            },
            {
                "name": "feature/[name]",
                # Each feature has its own named branch — easy to identify
                "description": "One branch per feature. e.g., feature/user-authentication",
                "type": "temporary",
            },
            {
                "name": "bugfix/[name]",
                # A bugfix branch is for fixing a specific problem
                "description": "Branches for fixing specific bugs. e.g., bugfix/fix-login-error",
                "type": "temporary",
            },
        ]

    def get_use_cases(self) -> list:
        """Returns when the Feature Branch Workflow is most appropriate."""
        return [
            "Beginner teams learning Git workflows for the first time",
            "Projects using GitHub, GitLab, or Bitbucket with Pull Request reviews",
            "Medium-sized teams where code review is important",
            "Projects where each feature is built independently",
            "Open-source projects accepting contributions from many developers",
        ]

    def get_pros(self) -> list:
        """Returns the advantages of Feature Branch Workflow."""
        return [
            "Easy to understand — one branch per feature is intuitive",
            "Pull Requests create natural checkpoints for code review",
            "Main branch stays clean — only reviewed, approved code enters",
            "Great for beginners learning collaborative development",
            "Works well with GitHub/GitLab and their PR review tools",
        ]

    def get_cons(self) -> list:
        """Returns the challenges of Feature Branch Workflow."""
        return [
            "Long-running branches can lead to 'merge hell' — many conflicts",
            "No clear rules for releases or hotfixes (unlike GitFlow)",
            "Can become disorganized if branch naming isn't consistent",
            "Feature branches can drift far from main — painful to merge later",
        ]


# =============================================================================
# 🏭 WORKFLOW FACTORY — Demonstrates Open/Closed Principle in action
# =============================================================================

class WorkflowFactory:
    """
    The WorkflowFactory creates workflow objects based on a simple string name.

    # WHAT IS A FACTORY? 🏭
    # A Factory is a class whose job is to CREATE other objects.
    # You say "give me a GitFlow workflow" and the factory hands one back.
    # You don't need to know HOW it's made — just what you want.

    # This demonstrates OPEN/CLOSED:
    # To add a new workflow (e.g., GitHub Flow), just:
    #   1. Create a new class (GithubFlowWorkflow) in this file
    #   2. Add ONE line to the _registry dict below
    # You DON'T change any views, URLs, or templates!
    """

    # A dictionary mapping human-readable names to workflow CLASSES (not instances!)
    # KEY: a short name (string), VALUE: the class itself (not an object yet)
    _registry: dict = {
        "gitflow": GitFlowWorkflow,              # "gitflow" → create a GitFlowWorkflow
        "trunk-based": TrunkBasedWorkflow,       # "trunk-based" → create a TrunkBasedWorkflow
        "feature-branch": FeatureBranchWorkflow, # "feature-branch" → create a FeatureBranchWorkflow
    }

    @classmethod  # @classmethod means this method belongs to the CLASS, not an instance
    def get_workflow(cls, workflow_type: str) -> BaseWorkflow:
        """
        Looks up and returns the correct workflow object for the given type name.

        Parameters:
            workflow_type (str): A string like "gitflow", "trunk-based", etc.

        Returns:
            BaseWorkflow: An instance (object) of the matching workflow class

        Raises:
            ValueError: If the workflow_type doesn't match any known workflow
                        (ValueError = Python's way of saying "invalid input")
        """
        # Look up the class in our registry
        # .get() returns None if the key doesn't exist (safer than direct access)
        workflow_class = cls._registry.get(workflow_type)

        # If nothing was found, raise an error telling the developer what's valid
        if workflow_class is None:
            # f"..." is an f-string — it lets us embed variables inside strings
            raise ValueError(
                f"Unknown workflow type: '{workflow_type}'. "
                f"Valid options are: {list(cls._registry.keys())}"
            )

        # Call the class like a function to CREATE a new object (instance) of it
        # This is called "instantiation" — creating a specific object from a blueprint
        return workflow_class()

    @classmethod
    def get_all_workflows(cls) -> list:
        """
        Returns a list of ALL workflow objects — one for each registered type.

        Returns:
            list: A list of BaseWorkflow objects (one GitFlow, one TrunkBased, etc.)
        """
        # For each key in our registry, create one workflow object
        # This is a "list comprehension" — a compact way to build a list
        # Translation: "For each type name in the registry, get that workflow"
        return [cls.get_workflow(workflow_type) for workflow_type in cls._registry]

    @classmethod
    def get_all_names(cls) -> list:
        """
        Returns just the type name keys (e.g., ["gitflow", "trunk-based", ...]).

        Returns:
            list: A list of workflow type name strings
        """
        return list(cls._registry.keys())  # .keys() returns the dictionary keys
