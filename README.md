## Instaclone

### 7/06/2022

## Author

[Ninah Odoyo]

# Description

This is a clone of the website of the popular photo app Instagram.


## Live link
www.instaclone.com


## User Story
The user should be able to:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.
* See all the comments on a picture.
* See all the pictures of a user.

## Setup and Installation

##### Clone the repository
```bash
git@github.com/odoyoninah/InstaClone.git
```
##### Install requirements 
```bash
cd Insta-Clone pip install -r requirements.txt
```
### Install and activate virtual environment
```bash
python3 -m venv env - source env/bin/activate
```
 ##### Database  
  SetUp your database. Add user and password, host then make migrations. 
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
python3.8 manage.py runserver

``` 

##### Tests 
 ```bash 
 python manage.py test 
```

Open application at '127.0.0.1.8000' at your web browser



## Technologies Used

* Python
* Django
* Heroku
* HTML
* CSS

# Known Bugs


## License
MIT License


Authors Information

[odoyoninah@gmail.com]

Ninah Odoyo (c) 2022


[Go Back to the top](#Instaclone)



