import unittest
import os
from shutil import rmtree
from create_start_page import path_guardrails, write_page

class TestCreateStartPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._test_pages_dir = "test_start_page"
        os.makedirs(cls._test_pages_dir)

    @classmethod
    def tearDownClass(cls):
        rmtree(cls._test_pages_dir)
        return

    def test_guardrails_root_path(self):
        path_guardrails("./")

    def test_guardrails_parent_path(self):
        with self.assertRaises(ValueError):
            path_guardrails("../")

    def test_write_dummy_page(self):
        page_file_name = self._test_pages_dir + "/dummy_page.html"
        write_page(page_file_name, "Dummy Page", "Hello World!")
        self.assertTrue(os.path.exists(page_file_name))
        self.assertTrue(os.path.isfile(page_file_name))
        expected_file_contents = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Dummy Page</title>
    <link href="/index.css" rel="stylesheet" />
  </head>

  <body>
    <p>Hello World!</p>
  </body>
</html>
"""
        page_file = open(page_file_name)
        actual_file_contents = page_file.read()
        page_file.close()
        self.assertEqual(expected_file_contents, actual_file_contents)

