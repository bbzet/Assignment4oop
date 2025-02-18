# Classes
## User
User class created to add its object into another a dictionary that is in Unitservice.
It has method: get_detials() print all the main information about object, get_age() gives an age of the object. 

## UserService
Created to create a dictionary where all the object of class User. Has methods like: add_user() to add object of User into dict., find_user() to find user with user_id, update_user() to update user's information, get_numbers to check how many objects of class User  (users) in dict., __delete__() to delete user from dict.   
**All of methods are classic method as we will work with dict which is in Userservice class**

## UserUtil
Created for checking user's information are validate or not. Methods: generate_user_id() to help user generate validate unique user_id,
generate_password() for creating a validate password, is_strong_password() to check if the password validate, generate_emai() to check if the email is validate counting name and surname, validate_email() to chekc if the email is validate.  
**All the method are static because they work not depending in UserUtil they will work with also dict. So staticmethod are perfect. 

## UML 
![Фото](https://github.com/bbzet/Assignment4oop/issues/1#issue-2859280668)

# Testclasses
Classes are **TestUser, TestUserService, TestUserUtil** all of them has methods of the classes to check classes's methods they are working. 

## Main.py
File for checking sample methods of classes.
