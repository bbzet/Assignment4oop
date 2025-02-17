from User import User
from UserService import UserService
from UserUtil import UserUtil

if __name__ == '__main__':
    user = User(250000001, 'Baiastan', 'Zamirbekov', 'baiastan.zamirbekov@domain.com', '25042005', '29042005')
    UserService.add_user(user)

    print(user.get_details())
    print(user.get_age())

    print(UserService.find_user(250000001).get_details())

    user_update = User(250000002, 'Bektur', 'Momunov', 'bektur.momunov@domain.com', '19032005', '19032005')
    UserService.update_user(250000001, user_update)
    print(UserService.find_user(250000001).get_details())

    print(UserService.get_numbers())

    user1 = User(UserUtil.generate_user_id(), 'Baiastan', 'Zamirbekov', UserUtil.generate_email('Baiastan', 'Zamirbekov'), UserUtil.generate_password(), '29042005')
    UserService.add_user(user1)

    print(UserService.get_numbers())

    print(UserService.find_user(user1.user_id).get_details())

    print(UserUtil.is_strong_password(UserUtil.generate_password()))
    print(UserUtil.validate_email(UserUtil.generate_email('Baiastan', 'Zamirbekov')))
