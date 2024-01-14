# Request approval site for IRIS Rec Task
***
A role based request approval web application where:
1. Students can log in and apply for request approvals
2. College employees can manage their requests and create new templates for requests
3. Admins can control the roles that every user has 

***
## 1. Getting started

1. Django must be installed in the environment where you are running the project
2. Clone the repository
3. Open the terminal and 'cd' into the project directory
4. Run the following commands : <br>
```
  python manage.py makemigrations
  python manage.py migrate
```
***
## 2. Running the server
1. `cd` into the project directory
2. Run the server
```
  python manage.py runserver
```
***
## 3. Features
1. Three groups of users -->
i. students
ii. employees
iii. admin

2. Admin users can further define the roles of the employee users: HOD, Dean, and MIS Officer.
3. Same login page for all users, but different permissions based on groups and roles
4. Student users can apply for employee approvals on requests
5. All requests correspond to templates which involve participants with a linear approval flow (eg. HOD can only approve request after MIS officer approves it)
6. Employee users can approve or delete the requests after examining the request
7. Student users can view the status of their requests
8. Employee and admin users can view the statistics of the page
9. Employee and admin users can create new templates

***
## 4. Planned features

1. Department wise segregation of all users and requests (eg. Chemical, Electronics, Computer Science, etc)
2. Making participants of a template a checkbox field instead of a dropdown list
3. Ability to archive a request after it has been approved by the required participants
