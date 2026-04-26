"""
=============================================================================
FILE: collaboration_service.py
PURPOSE: Handles everything about team collaboration in Git workflows —
         Pull Requests, Code Reviews, and handling Merge Conflicts.
=============================================================================

🔷 SOLID PRINCIPLE I — Interface Segregation Principle (continued)
   This file demonstrates I by being SEPARATE from CommitConventionService.
   CollaborationService ONLY handles team collaboration topics.
   It knows nothing about commit messages or branching strategies.

   If you need to display Pull Request information → use CollaborationService.
   If you need to display commit message tips → use CommitConventionService.
   Each service is focused and small — no overlap, no bloat.

🔷 SOLID PRINCIPLE D — Dependency Inversion Principle (setup for views.py)
   Plain English: "High-level modules (views) should NOT depend on low-level
   details (specific service implementations). Both should depend on
   ABSTRACTIONS (interfaces/base classes)."

   Think of it like an electrical outlet:
   - Your laptop doesn't care if power comes from solar, wind, or nuclear
   - It just uses the standard 'plug' interface
   - The power source can change without you buying a new laptop!

   In this app:
   - views.py depends on CollaborationService (abstract concept)
   - NOT on a specific implementation like "SlackCollaborationService"
   - Later we could swap to GitHubCollaborationService without changing views.py

   ❌ What would be WRONG without this:
      # BAD APPROACH (Dependency Inversion violated):
      # In views.py:
      # from git_learning.services.collaboration_service import CollaborationService
      # service = CollaborationService()  # Hardcoded to ONE specific class
      # PROBLEM: If you want to swap implementations, you MUST edit views.py.
      # Every view that uses this is tightly coupled to one specific class.

   ✅ Why this is better:
      # GOOD APPROACH (with Dependency Inversion):
      # Services are passed IN to views (or a factory creates them).
      # views.py just calls .get_pull_request_steps() — it doesn't care
      # which specific class implements that method.
=============================================================================
"""


class CollaborationService:
    """
    Handles all collaboration-related Git knowledge.

    This class's single responsibility (SRP) is explaining team Git workflows:
    how teams open Pull Requests, review code, and resolve Merge Conflicts.

    # WHAT IS COLLABORATION IN GIT? 🤝
    # When multiple developers work on the same project, they need rules for
    # how to combine their work safely. These practices prevent accidental
    # overwrites, catch bugs early, and maintain code quality.
    """

    def get_pull_request_guide(self) -> dict:
        """
        Returns a comprehensive guide to Pull Requests (PRs).

        # WHAT IS A PULL REQUEST? 🔀
        # When you finish working on a feature branch, you create a PR to say:
        # "Hey team, I'd like to merge my changes into main. Can you check them?"
        # Teammates review your code, suggest improvements, then approve (or reject).
        # Only AFTER approval does the code get merged (combined) into main.

        Returns:
            dict: A guide containing steps, tips, and best practices
        """
        return {
            "title": "Pull Requests (PRs)",
            "tagline": "The formal, reviewable way to merge code into the main branch",

            # The steps a developer follows to create a good Pull Request
            "creation_steps": [
                {
                    "step": 1,
                    "action": "Create a feature branch",
                    # WHAT IS A FEATURE BRANCH? A copy of main where you build ONE new thing
                    "command": "git checkout -b feature/my-awesome-feature",
                    "tip": "Name it clearly — 'feature/add-dark-mode' is better than 'new-stuff'",
                },
                {
                    "step": 2,
                    "action": "Make your changes and commit them",
                    # WHAT IS COMMIT? Saving a snapshot of your changes with a message
                    "command": "git commit -m 'feat: add dark mode toggle to navigation'",
                    "tip": "Commit small, logical pieces — not one giant commit at the end",
                },
                {
                    "step": 3,
                    "action": "Push the branch to the remote repository",
                    # WHAT IS 'PUSH'? Uploading your local commits to the server (e.g., GitHub)
                    # WHAT IS 'REMOTE'? The version of your project stored on a server online
                    "command": "git push origin feature/my-awesome-feature",
                    "tip": "Push regularly as backup — don't wait until completely finished",
                },
                {
                    "step": 4,
                    "action": "Open a Pull Request on GitHub/GitLab",
                    "command": "Use the GitHub web interface or: gh pr create",
                    "tip": "Fill in the PR template: what you changed, why, and how to test it",
                },
                {
                    "step": 5,
                    "action": "Wait for code review and address feedback",
                    "command": "Make requested changes, then: git push (updates the PR automatically)",
                    "tip": "Be open to feedback — code review makes everyone better!",
                },
                {
                    "step": 6,
                    "action": "Get approval and merge",
                    # WHAT IS MERGE? Combining the changes from your branch into main
                    "command": "Click 'Merge Pull Request' on GitHub (or: git merge)",
                    "tip": "Delete your feature branch after merging — keep the repo tidy",
                },
            ],

            # What makes a PR description excellent
            "pr_template": {
                "sections": [
                    {
                        "heading": "## What does this PR do?",
                        "guidance": "2-3 sentences explaining the change in plain English",
                        "example": "Adds a dark mode toggle to the navigation bar. Users can now switch between light and dark themes, and their preference is saved in localStorage.",
                    },
                    {
                        "heading": "## Why is this needed?",
                        "guidance": "Link to issue/ticket or explain the motivation",
                        "example": "Closes #234. Several users reported eye strain when using the app at night.",
                    },
                    {
                        "heading": "## How was it implemented?",
                        "guidance": "Brief technical explanation — what approach was taken",
                        "example": "Added CSS custom properties for theme colors. Toggle button in Navbar component dispatches a Redux action to update the theme state.",
                    },
                    {
                        "heading": "## How to test",
                        "guidance": "Step-by-step testing instructions for the reviewer",
                        "example": "1. Start the dev server\n2. Click the moon icon in top-right nav\n3. Verify all pages switch to dark theme\n4. Refresh — preference should be remembered",
                    },
                    {
                        "heading": "## Screenshots (if UI change)",
                        "guidance": "Before/after screenshots if you changed the visual interface",
                        "example": "[Attach screenshots here]",
                    },
                ]
            },
        }

    def get_code_review_guide(self) -> dict:
        """
        Returns a guide on how to conduct and receive code reviews effectively.

        # WHAT IS CODE REVIEW? 👀
        # Code review is when your teammates READ your code before it's merged.
        # They look for bugs, suggest improvements, and share knowledge.
        # It's normal and healthy — even senior developers get their code reviewed!

        Returns:
            dict: A guide with reviewer tips, author tips, and common issues to check
        """
        return {
            "title": "Code Reviews",
            "tagline": "Collaborative quality checks before code enters the main branch",

            # Things the code REVIEWER should look for
            "reviewer_checklist": [
                {
                    "category": "Correctness",
                    "emoji": "✅",
                    "items": [
                        "Does the code actually solve the problem described in the PR?",
                        "Are there obvious logical errors or off-by-one mistakes?",
                        "Are edge cases (empty inputs, null values, extreme numbers) handled?",
                        "Does it break any existing tests?",
                    ],
                },
                {
                    "category": "Readability",
                    "emoji": "📖",
                    "items": [
                        "Can you understand what the code does without the author explaining it?",
                        "Are variable and function names clear and descriptive?",
                        "Is the code DRY (Don't Repeat Yourself — no copy-pasted blocks)?",
                        "Are complex parts explained with comments?",
                    ],
                },
                {
                    "category": "Security",
                    "emoji": "🔒",
                    "items": [
                        "Is user input validated and sanitized (cleaned) before use?",
                        "Are any credentials, passwords, or API keys accidentally included?",
                        "Are proper authorization checks in place?",
                        "Could this be vulnerable to common attacks (SQL injection, XSS)?",
                    ],
                },
                {
                    "category": "Performance",
                    "emoji": "⚡",
                    "items": [
                        "Are there unnecessary loops running inside other loops (O(n²))?",
                        "Are database queries repeated when they could be cached?",
                        "Are large files or images handled efficiently?",
                    ],
                },
                {
                    "category": "Tests",
                    "emoji": "🧪",
                    "items": [
                        "Do new features have corresponding automated tests?",
                        "Do tests cover happy path AND edge cases?",
                        "Are tests readable and well-named?",
                    ],
                },
            ],

            # How to GIVE feedback kindly and effectively
            "giving_feedback_tips": [
                "Use questions instead of commands: 'What do you think about...' vs 'Change this to...'",
                "Explain WHY, not just what: 'This could cause a null error if the user is logged out' vs 'This is wrong'",
                "Distinguish severity: use labels like 'nit:' (minor style) vs 'blocker:' (must fix)",
                "Praise good work too! Code review should be a positive, learning experience",
                "Review the code, not the person — never personal, always professional",
                "Be specific: point to the exact line and suggest a concrete improvement",
            ],

            # How to RECEIVE feedback gracefully
            "receiving_feedback_tips": [
                "Remember: the reviewer wants to help, not criticize you personally",
                "Say 'thank you' for feedback — it takes effort to review carefully",
                "Ask questions if you don't understand a suggestion",
                "If you disagree, explain your reasoning calmly with facts",
                "Don't take long to address feedback — keep the PR moving forward",
                "A PR with many comments is learning in action — embrace it!",
            ],
        }

    def get_merge_conflict_guide(self) -> dict:
        """
        Returns a beginner-friendly guide to understanding and resolving merge conflicts.

        # WHAT IS A MERGE CONFLICT? ⚔️
        # A merge conflict happens when two developers change the SAME line of code
        # in different ways, and Git doesn't know which version to keep.
        #
        # Example:
        # Developer A changes line 10 to: "Welcome to our website!"
        # Developer B changes line 10 to: "Hello, welcome!"
        # Git sees TWO different changes to the same place → CONFLICT!
        # A human must decide which version to keep (or combine them).

        Returns:
            dict: A guide with explanation, steps, and prevention strategies
        """
        return {
            "title": "Merge Conflicts",
            "tagline": "When two changes collide — and how to resolve them calmly",

            # The conflict markers that Git adds to your files
            "conflict_anatomy": {
                "explanation": "When Git finds a conflict, it adds special markers to the file to show you both versions:",
                "example": (
                    "<<<<<<< HEAD\n"
                    "Welcome to our amazing website!\n"
                    "=======\n"
                    "Hello there, welcome to our site!\n"
                    ">>>>>>> feature/update-homepage-text\n"
                ),
                "parts": [
                    {
                        "marker": "<<<<<<< HEAD",
                        # HEAD is Git's name for "the current branch you're on"
                        "means": "Start of YOUR version (from HEAD = your current branch)",
                    },
                    {
                        "marker": "=======",
                        "means": "Divider between the two conflicting versions",
                    },
                    {
                        "marker": ">>>>>>> feature/...",
                        "means": "End of THEIR version (from the branch being merged in)",
                    },
                ],
            },

            # Step-by-step resolution process
            "resolution_steps": [
                {
                    "step": 1,
                    "action": "Don't panic! Conflicts are normal and resolvable.",
                    "detail": "Every experienced developer has resolved hundreds of merge conflicts.",
                },
                {
                    "step": 2,
                    "action": "Run 'git status' to see which files have conflicts",
                    "command": "git status",
                    "detail": "Files with conflicts are listed as 'both modified'",
                },
                {
                    "step": 3,
                    "action": "Open each conflicted file and find the markers",
                    "detail": "Search for '<<<<<<' in your editor — modern editors highlight these!",
                },
                {
                    "step": 4,
                    "action": "Choose the correct version (or combine both)",
                    "detail": "Delete the conflict markers AND the version you don't want. Keep what makes sense.",
                },
                {
                    "step": 5,
                    "action": "Mark the file as resolved",
                    "command": "git add [filename]",
                    # 'git add' tells Git "I've resolved this file, include it in the commit"
                    "detail": "After editing, 'git add' marks the conflict as resolved",
                },
                {
                    "step": 6,
                    "action": "Complete the merge with a commit",
                    "command": "git commit -m 'merge: resolve conflict in homepage text'",
                    "detail": "Git will create a 'merge commit' that records the resolution",
                },
            ],

            # How to avoid conflicts in the first place
            "prevention_strategies": [
                "Pull (download) the latest changes from main frequently — before starting new work",
                "Keep feature branches short-lived — merge quickly to avoid drift",
                "Communicate with teammates — 'I'm working on file X' prevents collisions",
                "Break work into small, focused tasks instead of large sprawling changes",
                "Use automatic code formatters (Prettier, Black) so formatting never conflicts",
                "Divide the codebase clearly — teammates working on different files = fewer conflicts",
            ],
        }

    def get_collaboration_practices(self) -> list:
        """
        Returns a list of general team collaboration best practices.

        Returns:
            list: A list of practice dictionaries with titles and descriptions
        """
        return [
            {
                "title": "Branch Protection Rules",
                "emoji": "🛡️",
                "description": "Set up rules on GitHub/GitLab to prevent direct commits to 'main'. Require at least one approving review before merging. This enforces code review for EVERYONE.",
                "level": "Team Setup",
            },
            {
                "title": "PR Size Guidelines",
                "emoji": "📏",
                "description": "Keep Pull Requests small — ideally under 400 lines of changed code. Small PRs are reviewed faster, have fewer conflicts, and are easier to understand.",
                "level": "Best Practice",
            },
            {
                "title": "Draft Pull Requests",
                "emoji": "📝",
                "description": "Open a Draft PR early in development to share progress and get early feedback, even before it's ready to merge. Label it 'WIP' or use GitHub's Draft feature.",
                "level": "Workflow Tip",
            },
            {
                "title": "Commit Signing",
                "emoji": "🔏",
                "description": "Sign commits with a GPG key to cryptographically prove that commits came from you. This prevents impersonation and verifies authenticity in open-source projects.",
                "level": "Security",
            },
            {
                "title": "Rebasing vs Merging",
                "emoji": "🔀",
                # REBASE = replaying your commits on top of the latest main (cleaner history)
                # MERGE = combining branches with a merge commit (preserves history)
                "description": "Choose a strategy: Rebase (cleaner, linear history) vs. Merge (preserves branch history). Be consistent team-wide to keep the Git log readable.",
                "level": "Advanced Concept",
            },
            {
                "title": "CODEOWNERS File",
                "emoji": "👤",
                "description": "Add a CODEOWNERS file to automatically request review from the right person based on which files were changed. Ensures domain experts review relevant code.",
                "level": "Team Setup",
            },
        ]
