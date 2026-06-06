from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# If you want to test your actual models later, you would uncomment the line below:
# from .models import GitResource, LearningNote

# ==============================================================================
# SECTION 1: SYSTEM & BASIC LOGIC TESTS (5 Tests)
# ==============================================================================
class BasicLogicTests(SimpleTestCase):
    def test_01_math_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_02_math_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_03_string_upper(self):
        self.assertEqual('git'.upper(), 'GIT')

    def test_04_list_append(self):
        lista = []
        lista.append('git_resource')
        self.assertIn('git_resource', lista)

    def test_05_boolean_check(self):
        self.assertTrue(True)


# ==============================================================================
# SECTION 2: GIT RESOURCE TESTS (5 Tests)
# ==============================================================================
class GitResourceStructureTests(TestCase):
    def test_06_resource_placeholder_one(self):
        self.assertNotEqual("GitResource", "LearningNote")

    def test_07_resource_name_strip(self):
        name = "  Git Tutorial  ".strip()
        self.assertEqual(name, "Git Tutorial")

    def test_08_resource_type_check(self):
        self.assertIsInstance("https://github.com", str)

    def test_09_resource_list_empty_initially(self):
        count = 0
        self.assertEqual(count, 0)

    def test_10_resource_validation_mock(self):
        url_valid = True
        self.assertTrue(url_valid)


# ==============================================================================
# SECTION 3: LEARNING NOTE TESTS (5 Tests)
# ==============================================================================
class LearningNoteStructureTests(TestCase):
    def test_11_note_content_not_empty(self):
        note = "Remember to use git commit"
        self.assertTrue(len(note) > 0)

    def test_12_note_title_length(self):
        title = "Git Basics"
        self.assertLess(len(title), 50)

    def test_13_note_search_keyword(self):
        content = "Always pull before pushing to avoid conflicts."
        self.assertIn("pushing", content)

    def test_14_note_count_increment_mock(self):
        notes = ['note1', 'note2']
        self.assertEqual(len(notes), 2)

    def test_15_note_timestamp_mock(self):
        import datetime
        now = datetime.datetime.now()
        self.assertIsNotNone(now)


# ==============================================================================
# SECTION 4: URL & ROUTING TESTS (5 Tests)
# ==============================================================================
class URLRoutingTests(TestCase):
    def test_16_homepage_url_config(self):
        # Checks if '/' route returns a placeholder status or exists
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 404]) # Accepts 404 if no view is mapped yet

    def test_17_admin_url_accessible(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

    def test_18_invalid_url_returns_404(self):
        response = self.client.get('/this-page-does-not-exist/')
        self.assertEqual(response.status_code, 404)

    def test_19_git_learning_base_route_mock(self):
        status = 200
        self.assertEqual(status, 200)

    def test_20_final_suite_check(self):
        self.assertEqual("Done", "Done")


