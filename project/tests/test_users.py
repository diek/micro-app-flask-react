# project/test/test_users.py

import json

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Test for the Users Service."""

    def test_users(self):
        """Ensure that the /ping behaves correctly."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])
        self.assertEqual(len(data), 2)
