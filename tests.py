# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from onlineapp.models import College

class CollegeTests(APITestCase):
    def test_college_detail(self):
        url = reverse('college_detail','4')
        data = {'acronym': 'gvp'}
        response = self.client.get(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # //self.assertEqual(College.objects.count(), 1)
        # //self.assertEqual(College.objects.get().name, 'DabApps')
