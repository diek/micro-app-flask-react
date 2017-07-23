# project/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from project import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        """Test environment variables for Development."""
        self.assertTrue(app.config['SECRET_KEY'] == 'bacon')
        self.assertTrue(app.config['DEBUG'] is True)  # <= Fail
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@users-db:5432/users_dev'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        """Test environment variables for Testing."""
        self.assertTrue(app.config['SECRET_KEY'] == 'bacon')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@users-db:5432/users_test'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        """Test environment variables for Production."""
        self.assertTrue(app.config['SECRET_KEY'] == 'bacon')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
