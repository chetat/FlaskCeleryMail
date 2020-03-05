import unittest
from flask_sqlalchemy import SQLAlchemy
from app import create_app, sqlalchemy


class UserTestCase(unittest.TestCase):
    """This class represents the User test cases"""
    
    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.base_url = '/api/v1'

        self.new_user = {
            "firstname": "Yeku",
            "lastname": "Chetat",
            "email": "yekuwilfred@yahoo.com",
            "phone": "+237681357962"
        }

    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
            self.db = sqlalchemy
            # drop all tables
            self.db.drop_all()

    def test_get_all_users(self):
        """Test get all users response with 200"""
        res = self.client().get(f"{self.base_url}/users")
        self.assertEqual(res.status_code, 200)
    
    def test_create_user(self):
        """Test get all users response with 200"""
        res = self.client().post(f"{self.base_url}/users", json=self.new_user)
        self.assertEqual(res.status_code, 201)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()