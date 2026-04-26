"""
=============================================================================
FILE: base_workflow.py
PURPOSE: Defines the BLUEPRINT that all Git workflow types must follow.

Think of this like a recipe template — it says "every recipe must have
ingredients and steps", but doesn't say WHAT the ingredients are.
=============================================================================

🔷 SOLID PRINCIPLE O — Open/Closed Principle
   Plain English: "Software should be open for EXTENSION but closed for MODIFICATION."
   This means: You can ADD new Git workflow types (like GitHub Flow) without
   changing any existing code. New things can be added; old things stay safe.

   ❌ What would be WRONG without this:
      # BAD APPROACH (without Open/Closed):
      # def get_workflow_info(workflow_type):
      #     if workflow_type == "gitflow":
      #         return "GitFlow info..."
      #     elif workflow_type == "trunk":
      #         return "Trunk info..."
      #     # PROBLEM: Every time you add a new workflow, you must CHANGE this
      #     # function! This breaks things and risks introducing bugs.

   ✅ Why this is better:
      # GOOD APPROACH (with Open/Closed):
      # Each workflow is its OWN class. To add GitHub Flow, just create a new
      # class — you don't touch the existing GitFlow or TrunkBased classes.
      # Nothing breaks, nothing changes, new feature just gets added safely!

=============================================================================

🔷 SOLID PRINCIPLE L — Liskov Substitution Principle
   Plain English: "Any child class should be able to replace its parent class
   without breaking the program."

   Think of it like electrical sockets: any plug (GitFlow, TrunkBased, etc.)
   that fits the socket (BaseWorkflow) should work correctly.

   ❌ What would be WRONG without this:
      # BAD APPROACH (breaking Liskov):
      # class GitFlowWorkflow:
      #     def get_name(self): return "GitFlow"
      # class TrunkBasedWorkflow:
      #     def workflow_title(self): return "Trunk"  # DIFFERENT method name!
      # PROBLEM: You can't treat them the same way — each has different methods.
      # Code that uses one can't use the other without rewriting.

   ✅ Why this is better:
      # GOOD APPROACH (Liskov applied):
      # Both GitFlow and TrunkBased inherit from BaseWorkflow and have the
      # SAME method names. Any code that works with BaseWorkflow automatically
      # works with ALL workflow types — no special cases needed!
=============================================================================
"""

# "abc" stands for Abstract Base Classes — Python's built-in tool for
# creating blueprint/template classes that can't be used directly
# but MUST be filled in by child classes (classes that inherit from them)
from abc import ABC, abstractmethod  # ABC = Abstract Base Class (a "template class")


class BaseWorkflow(ABC):
    """
    This is the BLUEPRINT class for all Git workflows.
    'ABC' means this class is Abstract — you can't create it directly.
    It's a TEMPLATE that says: "Every workflow MUST provide these things."

    Think of it like a job description:
    "Every employee must be able to: greet customers, handle cash, stock shelves."
    The actual employee (GitFlowWorkflow, TrunkBasedWorkflow) fills in the details.

    # WHAT IS INHERITANCE? 🤔
    # Inheritance is when one class (child) "borrows" the structure of another
    # class (parent). The child class gets everything from the parent FOR FREE,
    # and just needs to fill in the blanks marked with @abstractmethod.
    """

    @abstractmethod  # This decorator means: "Every child class MUST implement this method"
    def get_name(self) -> str:
        """
        Return the human-readable name of this workflow.
        For example: "GitFlow" or "Trunk-Based Development"

        @abstractmethod means this is a REQUIRED BLANK that child classes fill in.
        You CANNOT skip this — Python will raise an error if you forget.

        Returns:
            str: The display name of the workflow (str = a "string" = text)
        """
        pass  # 'pass' means "nothing here yet" — child classes fill this in

    @abstractmethod
    def get_description(self) -> str:
        """
        Return a beginner-friendly description of this workflow strategy.

        Returns:
            str: A plain-English description of the workflow
        """
        pass

    @abstractmethod
    def get_branches(self) -> list:
        """
        Return a list of the typical Git branches used in this workflow.

        # WHAT IS A BRANCH? 🌿
        # A branch in Git is like a parallel copy of your code.
        # Imagine a tree — the trunk is the main code, and branches are
        # separate versions where you can try new things safely.
        # When you're done, you "merge" (combine) the branch back into the trunk.

        Returns:
            list: A Python list (a collection of items) of branch names
        """
        pass

    @abstractmethod
    def get_use_cases(self) -> list:
        """
        Return a list of situations where this workflow works best.

        Returns:
            list: A Python list of use case descriptions
        """
        pass

    @abstractmethod
    def get_pros(self) -> list:
        """
        Return a list of advantages/benefits of this workflow.

        Returns:
            list: A Python list of benefit strings
        """
        pass

    @abstractmethod
    def get_cons(self) -> list:
        """
        Return a list of disadvantages/challenges of this workflow.

        Returns:
            list: A Python list of challenge strings
        """
        pass

    def get_summary(self) -> dict:
        """
        This method is NOT abstract — it comes for FREE to all child classes!
        It bundles all the workflow information into one neat package (a dict).

        # WHAT IS A dict? 📦
        # A dict (short for dictionary) is like a real dictionary — it has
        # KEYS (like words) and VALUES (like definitions).
        # Example: {"name": "GitFlow", "branches": ["main", "develop"]}

        Returns:
            dict: A dictionary with all workflow data collected together
        """
        # Call the methods that child classes implemented and bundle them up
        return {
            "name": self.get_name(),                  # The workflow's display name
            "description": self.get_description(),    # What this workflow is
            "branches": self.get_branches(),          # What branches it uses
            "use_cases": self.get_use_cases(),        # When to use it
            "pros": self.get_pros(),                  # Its advantages
            "cons": self.get_cons(),                  # Its disadvantages
        }
