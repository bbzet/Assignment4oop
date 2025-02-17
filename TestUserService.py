import unittest
from UserService import UserService
from User import User
from UserUtil import UserUtil

class TestUserService(unittest.TestCase):
    def test_add_user(self):
        user = User(250000001, 'Baiastan', 'Zamirbekov', 'baiastan.zamirbekov@domain.com', '25042005', 29042005)
        UserService.add_user(user)

        self.assertIn(user.user_id, UserService.users)
        self.assertEqual(UserService.users[user.user_id], user)



    def test_find_user(self):
        user = User(250000001, 'Baiastan', 'Zamirbekov', 'baiastan.zamirbekov@domain.com', '25042005', 29042005)
        UserService.add_user(user)

        self.assertEqual(UserService.find_user(user.user_id), user)

    def test_delete_method(self):
        user = User(250000001, 'Baiastan', 'Zamirbekov', 'baiastan.zamirbekov@domain.com', '25042005', 29042005)
        UserService.add_user(user)
        UserService.__delete__(user.user_id)
        self.assertNotIn(user.user_id, UserService.users)

    def test_update_user(self):
        user = User(250000001, 'Baiastan', 'Zamirbekov', 'baiastan.zamirbekov@domain.com', '25042005', 29042005)
        UserService.add_user(user)
        user_update = User(250000002, 'Bektur', 'Momunov', 'bektur.momunov@domain.com', '19032005', 19032005)
        UserService.update_user(user.user_id, user_update)
        self.assertNotEqual(UserService.users[user.user_id], user_update)


    def test_get_numbers(self):
        user = User(250000001, 'Baiastan', 'Zamirbekov', 'baiastan.zamirbekov@domain.com', '25042005', 29042005)
        UserService.add_user(user)

        self.assertEqual(UserService.get_numbers(), 1)

        user1 = User(250000002, 'Bektur', 'Momunov', 'bektur.momunov@domain.com', '19032005', 19032005)
        UserService.add_user(user1)

        self.assertEqual(UserService.get_numbers(), 1)