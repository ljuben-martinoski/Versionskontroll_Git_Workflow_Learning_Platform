"""
=============================================================================
FILE: workflow_provider.py
PURPOSE: Demonstrates the Dependency Inversion Principle by acting as the
         "middleman" that provides services to views.py without views.py
         needing to know WHICH specific service class is being used.
=============================================================================

🔷 SOLID PRINCIPLE D — Dependency Inversion Principle
   Plain English: "High-level code (views.py) should depend on ABSTRACTIONS,
   not on specific concrete classes."

   THE ANALOGY 🔌:
   Think of a USB port. Your laptop (views.py) expects a USB connection.
   You can plug in a keyboard, mouse, flash drive — anything that is USB.
   The laptop doesn't care WHICH device it is — just that it uses USB.

   In our app:
   - views.py calls "give me collaboration data" → it doesn't care HOW
   - WorkflowProvider is the "USB port" — a stable interface for views.py
   - The actual service classes (CollaborationService, CommitService) are
     the "devices" — they can be swapped without changing views.py!

   ❌ What would be WRONG without this:
      # BAD (Direct dependency — tight coupling):
      # In views.py:
      # from git_learning.services.collaboration_service import CollaborationService
      # from git_learning.services.commit_service import CommitConventionService
      # from git_learning.services.branching_service import WorkflowFactory
      # collaboration_service = CollaborationService()
      # commit_service = CommitConventionService()
      # PROBLEM: views.py now knows about 3 different service files.
      # If you rename a file, move a class, or swap a service — you must
      # update EVERY view that imported it directly. Fragile and messy!

   ✅ Why this is better:
      # GOOD (Dependency Inversion):
      # In views.py:
      # from git_learning.services.workflow_provider import WorkflowProvider
      # provider = WorkflowProvider()
      # That's it! views.py imports ONE thing.
      # To change services → update WorkflowProvider only.
      # views.py never changes!
=============================================================================
"""

# Import all our concrete service classes — this file knows about them, views.py doesn't
from git_learning.services.branching_service import WorkflowFactory  # The factory for workflows
from git_learning.services.commit_service import CommitConventionService  # Commit message guide
from git_learning.services.collaboration_service import CollaborationService  # Team collaboration


class WorkflowProvider:
    """
    The WorkflowProvider acts as a single gateway to ALL application services.

    Instead of views.py importing 3 different services from 3 different files,
    it imports just WorkflowProvider. This centralizes all dependencies.

    # WHAT IS DEPENDENCY INJECTION? 💉
    # Dependency Injection means giving an object its dependencies from the outside
    # rather than having it create them internally.
    # Example: Instead of a chef buying their own ingredients (creating dependencies),
    # a manager buys the ingredients and GIVES them to the chef (injecting dependencies).
    # This makes the chef's behavior easier to test and change!

    When views.py creates a WorkflowProvider, it gets a stable "interface"
    it can use without knowing anything about the underlying services.
    """

    def __init__(self):
        """
        Initialize the provider with all the services it wraps.

        '__init__' is the CONSTRUCTOR — it runs automatically when you create
        a new object. It's like the moment a factory opens for business.

        # WHAT IS 'self'? 🪞
        # 'self' refers to the specific object being created right now.
        # When you write self.something, you're saving data ONTO that object.
        # Like writing your name inside a book you own — it marks it as YOURS.
        """
        # Create one instance of each service class
        # We store them as attributes (properties) of this object using 'self'
        self._collaboration_service = CollaborationService()  # Team workflows
        self._commit_service = CommitConventionService()       # Commit message rules
        self._workflow_factory = WorkflowFactory()             # Branching strategies

        # The underscore prefix (_) is a Python convention meaning
        # "this is private — code outside this class shouldn't touch it directly"

    # ===========================================================================
    # BRANCHING STRATEGY METHODS
    # ===========================================================================

    def get_all_workflows(self) -> list:
        """
        Returns all branching workflow objects via the factory.

        Returns:
            list: All available BaseWorkflow instances
        """
        # Delegate (pass the call along) to the factory — provider just forwards
        return self._workflow_factory.get_all_workflows()

    def get_workflow(self, workflow_type: str):
        """
        Returns one specific workflow by its type key.

        Parameters:
            workflow_type (str): e.g., "gitflow", "trunk-based", "feature-branch"

        Returns:
            BaseWorkflow: The specific workflow object
        """
        return self._workflow_factory.get_workflow(workflow_type)

    # ===========================================================================
    # COMMIT CONVENTION METHODS
    # ===========================================================================

    def get_commit_types(self) -> list:
        """
        Returns all Conventional Commit type prefixes and their meanings.

        Returns:
            list: Commit type dictionaries
        """
        return self._commit_service.get_commit_types()

    def get_commit_good_examples(self) -> list:
        """
        Returns examples of high-quality commit messages.

        Returns:
            list: Good commit message examples with explanations
        """
        return self._commit_service.get_good_examples()

    def get_commit_bad_examples(self) -> list:
        """
        Returns examples of poor commit messages with fixes.

        Returns:
            list: Bad commit message examples with explanations and better alternatives
        """
        return self._commit_service.get_bad_examples()

    def get_commit_structure(self) -> dict:
        """
        Returns the anatomy/structure of a well-formed commit message.

        Returns:
            dict: The structure breakdown of a commit message
        """
        return self._commit_service.get_commit_structure()

    def get_commit_tips(self) -> list:
        """
        Returns practical tips for writing better commits.

        Returns:
            list: A list of tip strings
        """
        return self._commit_service.get_commit_tips()

    # ===========================================================================
    # COLLABORATION METHODS
    # ===========================================================================

    def get_pull_request_guide(self) -> dict:
        """
        Returns the complete Pull Request guide.

        Returns:
            dict: Pull Request creation guide and best practices
        """
        return self._collaboration_service.get_pull_request_guide()

    def get_code_review_guide(self) -> dict:
        """
        Returns the code review guide with checklists and tips.

        Returns:
            dict: Code review checklist and feedback tips
        """
        return self._collaboration_service.get_code_review_guide()

    def get_merge_conflict_guide(self) -> dict:
        """
        Returns the merge conflict explanation and resolution guide.

        Returns:
            dict: Merge conflict guide with steps and prevention strategies
        """
        return self._collaboration_service.get_merge_conflict_guide()

    def get_collaboration_practices(self) -> list:
        """
        Returns general team collaboration best practices.

        Returns:
            list: List of collaboration practice dictionaries
        """
        return self._collaboration_service.get_collaboration_practices()
