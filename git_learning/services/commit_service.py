"""
=============================================================================
FILE: commit_service.py
PURPOSE: Handles everything about Git commit conventions — good vs. bad
         commit messages, conventional commit formats, and examples.
=============================================================================

🔷 SOLID PRINCIPLE I — Interface Segregation Principle
   Plain English: "Don't force a class to implement methods it doesn't need."

   Think of restaurant roles:
   - A waiter takes orders and serves food (they don't cook)
   - A chef cooks (they don't serve tables)
   If you forced EVERY restaurant worker to do ALL tasks, it would be chaos.

   In our code, CommitConventionService ONLY handles commit messages.
   It doesn't know about branching or collaboration. If you need to check
   commits, you use CommitConventionService — not a bloated "everything" class.

   ❌ What would be WRONG without this:
      # BAD APPROACH (one massive interface):
      # class GitService:
      #     def get_commit_message(self): ...
      #     def get_branching_strategy(self): ...
      #     def manage_pull_request(self): ...
      #     def send_team_notification(self): ...
      #     def generate_release_notes(self): ...
      # PROBLEM: Every class that "uses" GitService must know about ALL of this,
      # even if it only cares about commit messages. Bloated and confusing!

   ✅ Why this is better:
      # GOOD APPROACH (Interface Segregation):
      # CommitConventionService → only knows about commits
      # CollaborationService → only knows about teamwork
      # BranchingService → only knows about branches
      # Each class is laser-focused on its own job. Clean and maintainable!
=============================================================================
"""


class CommitConventionService:
    """
    Handles all logic related to Git commit conventions.

    # WHAT IS A COMMIT? 💾
    # A commit in Git is like "saving your work" with a message explaining
    # what you changed. Example: saving a Word document with the comment
    # "Fixed typo on page 3 and added new section about budgets."
    # Good commit messages help your whole team understand project history.

    This class has ONE job (Single Responsibility): explain commit conventions.
    It does NOT handle branching, collaboration, or any other Git topic.
    """

    def get_commit_types(self) -> list:
        """
        Returns a list of conventional commit type prefixes and their meanings.

        The Conventional Commits specification (conventionalcommits.org) defines
        standard prefixes for commit messages so everyone writes them consistently.

        Returns:
            list: A list of dictionaries, each with type, emoji, and description
        """
        # Each item in this list is a dictionary describing one commit type
        return [
            {
                "type": "feat",      # The prefix you put before the colon in your commit
                "emoji": "✨",
                # A "feature" is a new functionality added to the project
                "description": "A new feature has been added to the codebase",
                "example": "feat: add user login page",
                "color": "emerald",   # Used by the template to pick a color badge
            },
            {
                "type": "fix",
                "emoji": "🐛",
                # A "bug" is an error in your code; "fix" means you repaired it
                "description": "A bug (error in the code) has been repaired",
                "example": "fix: correct password validation logic",
                "color": "red",
            },
            {
                "type": "docs",
                "emoji": "📚",
                # "docs" = documentation — text that explains the code
                "description": "Only documentation (explanations/guides) was changed",
                "example": "docs: update README with installation steps",
                "color": "blue",
            },
            {
                "type": "style",
                "emoji": "💅",
                # "style" here means code formatting, not CSS/visual styling
                "description": "Code formatting changes only — no logic was altered",
                "example": "style: fix indentation and add missing semicolons",
                "color": "purple",
            },
            {
                "type": "refactor",
                "emoji": "♻️",
                # "Refactor" = rewrite code to be cleaner without changing what it does
                "description": "Code was rewritten to be cleaner, with no feature changes",
                "example": "refactor: simplify user authentication flow",
                "color": "amber",
            },
            {
                "type": "test",
                "emoji": "🧪",
                # A "test" is code that checks if other code works correctly
                "description": "New automated tests were added or existing ones updated",
                "example": "test: add unit tests for login validation",
                "color": "cyan",
            },
            {
                "type": "chore",
                "emoji": "🔧",
                # "Chore" = maintenance work that doesn't affect the app's features
                "description": "Maintenance tasks, dependency updates, config changes",
                "example": "chore: update Django from 4.2 to 5.0",
                "color": "slate",
            },
            {
                "type": "perf",
                "emoji": "⚡",
                # "Performance" = making the app faster or more efficient
                "description": "A performance improvement — app is now faster or uses less memory",
                "example": "perf: cache database queries on the home page",
                "color": "orange",
            },
            {
                "type": "ci",
                "emoji": "🤖",
                # "CI" = Continuous Integration — automated testing/deployment pipelines
                "description": "Changes to the CI/CD pipeline (automated testing setup)",
                "example": "ci: add GitHub Actions workflow for automated testing",
                "color": "indigo",
            },
            {
                "type": "BREAKING CHANGE",
                "emoji": "💥",
                # "Breaking change" = existing users/code must update — it won't work as before
                "description": "A change that breaks backwards compatibility — major version bump",
                "example": "feat!: rename API endpoint from /users to /accounts",
                "color": "rose",
            },
        ]

    def get_good_examples(self) -> list:
        """
        Returns examples of GOOD commit messages with explanations of why they're good.

        Returns:
            list: A list of dicts with 'message' and 'why' keys
        """
        return [
            {
                "message": "feat(auth): add OAuth2 login with Google",
                # This message tells us: WHAT changed (OAuth2 login), HOW (with Google),
                # and WHERE it changed (auth module)
                "why": "Specific and clear — immediately tells you what was added and where",
                "score": 5,  # Score out of 5 stars for quality
            },
            {
                "message": "fix(cart): prevent duplicate items when clicking fast",
                # You immediately know: it's a bug fix, it's in the cart, and WHAT the bug was
                "why": "Describes the exact bug that was fixed — someone can understand without reading code",
                "score": 5,
            },
            {
                "message": "docs: add step-by-step setup guide to README",
                "why": "Clear type prefix, specific about what documentation was added",
                "score": 4,
            },
            {
                "message": "refactor(api): extract user validation into separate helper function",
                "why": "Explains WHY the refactor was done (to extract logic) not just that it happened",
                "score": 5,
            },
            {
                "message": "test(login): add tests for invalid email edge cases",
                "why": "Specific scope (login), specific what was tested (invalid email edge cases)",
                "score": 4,
            },
            {
                "message": "chore: update dependencies — Django 4.2 → 5.0, fix breaking changes",
                "why": "Mentions exact versions and notes that related fixes were included",
                "score": 5,
            },
        ]

    def get_bad_examples(self) -> list:
        """
        Returns examples of BAD commit messages with explanations of why they're bad.

        Returns:
            list: A list of dicts with 'message', 'problem', and 'better' keys
        """
        return [
            {
                "message": "fix stuff",
                # "stuff" tells us NOTHING about what was fixed
                "problem": "What stuff? This could mean anything. Completely useless history.",
                "better": "fix(cart): prevent items being added twice when double-clicking",
                "score": 1,  # 1 out of 5 — very poor
            },
            {
                "message": "wip",
                # "wip" stands for "work in progress" — helpful in drafts, not in final commits
                "problem": "Never commit 'wip' to a shared branch — it means your work isn't done!",
                "better": "Use feature branches and only commit when a small piece is complete",
                "score": 1,
            },
            {
                "message": "AAAAAAA",
                # This happens when developers are frustrated 😅
                "problem": "Expression of frustration committed to the permanent project history.",
                "better": "fix(forms): handle edge case where empty form fields crash the app",
                "score": 0,  # 0/5 — this should never happen
            },
            {
                "message": "changes",
                "problem": "What changed? Where? Why? This message has zero information.",
                "better": "feat(profile): add ability to upload and crop profile picture",
                "score": 1,
            },
            {
                "message": "Updated the thing on the page to make it look nicer and also fixed the bug that John mentioned in the meeting yesterday and also added the new dropdown but it's not finished yet",
                "problem": "Way too long, mixes multiple changes, mentions things nobody else understands (John? which meeting?).",
                "better": "Split into separate commits: one for UI fix, one for the bug, one for the dropdown when finished",
                "score": 1,
            },
            {
                "message": "final",
                # This is a common beginner mistake
                "problem": "'Final' is never final. You'll make another commit called 'final2' tomorrow.",
                "better": "Be specific about what the final change actually was",
                "score": 1,
            },
            {
                "message": "asdfgh",
                "problem": "Keyboard mashing — completely meaningless and pollutes project history.",
                "better": "chore: fix typo in variable name on user registration form",
                "score": 0,
            },
        ]

    def get_commit_structure(self) -> dict:
        """
        Returns the anatomy of a proper Conventional Commit message.

        Returns:
            dict: A breakdown of each part of a commit message
        """
        return {
            # The full example commit message to show visually
            "full_example": "feat(auth)!: add multi-factor authentication — closes #142",

            # Each part of the commit message, explained
            "parts": [
                {
                    "part": "type",
                    "value": "feat",
                    "required": True,  # True/False in Python = boolean (yes/no)
                    "explanation": "What KIND of change: feat, fix, docs, style, etc.",
                },
                {
                    "part": "scope",
                    "value": "(auth)",
                    "required": False,  # Optional but recommended
                    "explanation": "WHERE in the code: which module, page, or feature area",
                },
                {
                    "part": "breaking indicator",
                    "value": "!",
                    "required": False,
                    "explanation": "The '!' signals this change breaks old behaviour — use with care!",
                },
                {
                    "part": "separator",
                    "value": ":",
                    "required": True,
                    "explanation": "Always put a colon and space between type and description",
                },
                {
                    "part": "description",
                    "value": "add multi-factor authentication",
                    "required": True,
                    "explanation": "Short summary (max 72 chars) in present tense, lowercase",
                },
                {
                    "part": "issue reference",
                    "value": "— closes #142",
                    "required": False,
                    "explanation": "Links the commit to a GitHub/GitLab issue for traceability",
                },
            ],
        }

    def get_commit_tips(self) -> list:
        """
        Returns a list of practical tips for writing better commit messages.

        Returns:
            list: A list of tip strings
        """
        return [
            "Write in present tense: 'add feature' not 'added feature'",
            "Keep the subject line under 72 characters",
            "Commit ONE logical change at a time — don't bundle unrelated changes",
            "If you need to say 'and' in your message, consider splitting into two commits",
            "Reference issue numbers (e.g., 'closes #42') to link commits to tasks",
            "The commit message should explain WHAT and WHY, not HOW (the code shows how)",
            "Never commit broken code to a shared branch",
            "Use 'git commit --amend' to fix your last commit message before pushing",
        ]
