<<<<<<< HEAD
from django.test import TestCase, Client
import unittest

#test pages exist
class SimpleTest(unittest.TestCase):
    client = Client()
    def test_admin(self): #admin main exists
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
    def test_workflow(self):
        client = Client()
        response = client.get('/workflow/')
        self.assertEqual(response.status_code, 302)
    def test_employee(self):
        client = Client()
        response = client.get('/workflow/employee/')
        self.assertEqual(response.status_code, 302)
    def test_employee_add(self):
        client = Client()
        response = client.get('/workflow/employee/add/')
        self.assertEqual(response.status_code, 302)
    def test_picture(self):
        client = Client()
        response = client.get('/workflow/picture/')
        self.assertEqual(response.status_code, 302)
    def test_picture_add(self):
        client = Client()
        response = client.get('/workflow/picture/add/')
        self.assertEqual(response.status_code, 302)
=======
from django.test import TestCase
import unittest
>>>>>>> Create tests directory for app workflow. Create test files for admin, forms, models, views
