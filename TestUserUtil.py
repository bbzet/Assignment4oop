import unittest
from User import User

class TestUser(unittest.TestCase):
    def test_get_details(self):
        user = User(250000001, 'Baiastan', 'Zamirbekov', 'baiastan.zamirbekov@domain.com', '25042005', '29042005')
        self.assertEqual(user.get_details(), 'User id: 250000001, Name: Baiastan, Surname: Zamirbekov, Email: baiastan.zamirbekov@domain.com, Birthday: 29-04-2005')

    def test_get_age(self):
        user = User(250000001, 'Baiastan', 'Zamirbekov', 'baiastan.zamirbekov@domain.com', '25042005', '29042005')
        self.assertEqual(user.get_age(), 19)
        self.assertEqual(user.get_age(), 20)