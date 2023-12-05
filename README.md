# Career Gates
-    you are heired

This is a portfolio project at holberton school as a requirment for 9 month foundation course.

As a team project, we decided to build a web application which can be used by a Career expert fairm to relate, interact and serve their clients.

This project offers the Administrator the oppurtunity to recieve resume review request and an interview request from their clients. It also gives them the opportunity to response to such requests.

### You see this project at:
- https://www.iniworld.tech
The project is divided into faces which include, Project approval 1, Project approval 2....

Table of Content
* [Research and Project Approval 1](#Research-and-Project-Approval-1)
* [Research and Project Approval 1](#Research and Project Approval 1)
* [Build your portfolio project (Week 1): Making Progress](#Build your portfolio project (Week 1): Making Progress)
* [Build your portfolio project (Week 2): MVP Complete](#Build your portfolio project (Week 2): MVP Complete)
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)
## Research and Project Approval 1
In this stage if the project we research on ideas which we can develope and work on. By the end we submitted a google document that addressed the major issues related to the project.
You can access the document here: https://docs.google.com/document/d/1BWSQP5hsklI5bFE3O2Ro38fNebYYUMye6rr4q_ANWUA/edit?usp=drivesdk

## Research and Project Approval 2
In this project's stage we developed and submitted a document that contain the discription of our MVP.
You can find it here: https://docs.google.com/document/d/1kph_60eoDTzfHrLD9A3nFkIX8TU3LYLUSmdsWyfl9Oc/edit?usp=drivesdk


## Research and Project Approval 3
In part 3 of the project we plan the project execution process. To achieve a well organized and updateable plan, we used a Trello board to create the tasks that will have to be done to achieve our project MVP. You can see the Trello board here: https://trello.com/invite/b/vJDoz84d/ATTIf15edd959dc39ae6e3e31b425fac00d443378EAF/career-gate

## Build your portfolio project (Week 1): Making Progress

## Build your portfolio project (Week 2): MVP Complete
## Environment
This project is interpreted/tested on Ubuntu 16.04 LTS using python3 (version 3.4.3)

## How to run the project:
* Clone this project on your local mechine: `git clone `
* Access the Career_Gate directory: `cd Career_Gate`


###### To run with filstorage
`python3 app.py`

###### To run with database

`ENV=dev MYSQL_USER=<user_name> MYSQL_PWD=<user_password> MYSQL_HOST=localhost MYSQL_DB=<database_name> STORAGE=db python3 app.py`

You can as well visit https://www.iniworld.tech
to use the application.

The `/` route is a landingpage with a navigation bar, some description of services and a footer. The Get Started button on the page directs you to a login page where you can iether login or use the sign in button to sign in. Both sign in and login can be access from the navigation bar. After a successful login you are redirected to the user dashboard where you can create and view a resume request as well as an interview booking.


## File Descriptions

#### `models/` directory contains classes and views used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [interview.py](models/interview.py)
* [resume.py](models/resume.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization, and Database Storage class that handles the storing and retieving from a database :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* `def reload(self)` -  deserializes the JSON file to __objects

[db_storage.py](models/engine/db_storage.py) - interact with a mysql database
* `def all(self)` - returns the dictionary of objects with key <obj class name>.id
* `def new(self, obj)` - add a new object to the databse
* `def save(self)` - commits the database
* `def reload(self)` -  loads database

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects


[/test_models/test_engine/test_file_storage.py](/tests/test_models/test_engine/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_file_storage(self)` - Test that models/file_storage.py conforms to PEP8
* `def test_pep8_conformance_test_file_storage(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8
* `def test_file_storage_module_docstring(self)` - Test for the file_storage.py module docstring
* `def test_file_storage_class_docstring(self)` - Test for the FileStorage class docstring


[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_user(self)` - Test that models/user.py conforms to PEP8
* `def test_pep8_conformance_test_user(self)` - Test that tests/test_models/test_user.py conforms to PEP8
* `def test_user_module_docstring(self)` - Test for the user.py module docstring
* `def test_user_class_docstring(self)` - Test for the User class docstring


## Bugs
- There is aTypeError: Cannot create a consistent method resolution
order (MRO) for bases object, UserMixin

when running with file storage so you should run it with database.

## Authors
Inimfon Ebong - [Github](https://github.com/Inialpha) / [Twitter](https://twitter.com/Inimfon_Tech)   
Kasiemobi Eke [Github]()


## License                             
Public Domain. No copy write protection
