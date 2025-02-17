import unittest
from UserUtil import UserUtil
class TestUser(unittest.TestCase):
    def test_generate(self):
        id = UserUtil().generate_user_id()
        print(id)
        self.assertEqual(len(str(id)), 9)
        self.assertEqual(str(id[0:2]), '25')

    def test_password(self):
        password = UserUtil().generate_password()
        self.assertEqual(len(password), 8)


    def test_is_strong_password(self):
        self.assertTrue(UserUtil().is_strong_password('Aa1!aaaa'))
        self.assertFalse(UserUtil().is_strong_password('aa1!aaa'))

    def test_validate_email(self):
        email = 'bektur.momunov@domain.com'
        self.assertTrue(UserUtil().validate_email(email))