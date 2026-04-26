"""
=============================================================================
FILE: urls.py (app-level)
PURPOSE: Maps URL paths to their corresponding view functions.

# WHAT IS URL ROUTING? 🗺️
# URL routing is how Django knows WHICH view to run based on what URL
# the user typed in their browser.
#
# Example:
# User visits: http://127.0.0.1:8000/branching/
# Django looks at urls.py and finds: path("branching/", branching_view)
# Django calls: branching_view(request)
# Django sends back: the rendered HTML page
#
# Think of it like a post office sorting system:
# Each package (URL) goes to the right destination (view function).
=============================================================================
"""

# 'path' is Django's function for defining URL patterns
# It takes: (url_pattern, view_function, name)
from django.urls import path  # URL pattern creator

# Import all our view functions from views.py
# Each function handles one page of the website
from git_learning import views  # The views.py file in this same app folder


# 'app_name' sets the namespace for this app's URLs
# This allows us to use "branching:home" in templates instead of just "home"
# WHAT IS A NAMESPACE? Like a prefix that prevents name collisions
# Example: if two apps both have a view called 'home', namespacing tells them apart
app_name = "git_learning"  # The namespace for all URLs in this app


# 'urlpatterns' is a LIST that Django REQUIRES to be here with EXACTLY this name
# Django automatically looks for this variable in urls.py files
# Each entry in the list is one URL pattern → view function mapping
urlpatterns = [

    # HOME PAGE — the root URL of our app
    # path("", ...) means no extra path after the domain
    # name="home" lets us use {% url 'git_learning:home' %} in templates
    path(
        "",                  # The URL pattern — "" matches the root URL
        views.home_view,     # Which view function to call
        name="home"          # The name we can reference in templates
    ),

    # BRANCHING STRATEGIES PAGE
    path(
        "branching/",        # User visits /branching/
        views.branching_view, # Call this view function
        name="branching"     # Named 'branching' for template URL references
    ),

    # COMMIT CONVENTIONS PAGE
    path(
        "commits/",
        views.commits_view,
        name="commits"
    ),

    # COLLABORATION PRACTICES PAGE
    path(
        "collaboration/",
        views.collaboration_view,
        name="collaboration"
    ),

    # DOCUMENTATION PAGE
    path(
        "documentation/",
        views.documentation_view,
        name="documentation"
    ),
]
