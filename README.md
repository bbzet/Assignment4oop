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
![Фото](https://private-user-images.githubusercontent.com/150649109/414087694-e34a4629-8a84-4a84-97ad-26fb995aa21a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk5NTczMjUsIm5iZiI6MTczOTk1NzAyNSwicGF0aCI6Ii8xNTA2NDkxMDkvNDE0MDg3Njk0LWUzNGE0NjI5LThhODQtNGE4NC05N2FkLTI2ZmI5OTVhYTIxYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxOVQwOTIzNDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMjNjZTI4YzA0ZDYyNDNhYzdiMWE2MmExNjc0MTI3M2UwMTg3OWZlOGY5NmRkMzE4YmI4ZTVhOTNiOTc0MTVjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.YO_zvIdK0UAhePRH_mOXV3XzzH2Q_Mvb7jOTZhEK5XI)

# Testclasses
Classes are **TestUser, TestUserService, TestUserUtil** all of them has methods of the classes to check classes's methods they are working. 

## Main.py
File for checking sample methods of classes.
