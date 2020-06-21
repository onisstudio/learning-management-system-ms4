# Learning Management System

Full Stack Frameworks with Django Milestone Project | Learning Management System

## Demo

A live demo can be found [here](https://lms-ms4.herokuapp.com/).

## Project Purpose

LMS is an app where you can add new courses or where you can learn new things from the courses already added to the app. Courses can be free or paid.

## UX

### User Stories

As a Student I want to:
    - view a list of courses so I can select some to purchase
    - view individual course details so I can view the price, description or image
    - add a course to my cart so that I can buy that course
    - review my cart so I can make adjustments prior to checkout
    - review my orders so I can see what I’ve purchased in the past
    - search for a course so that I can find a specific course
    - add a rating for a ourse so that other students can know the course rating

As an Admin I want to:
    - add new courses so I can have more students joining
    - add as many lessons as I need for a course so that students learn new things
    - add a course in a specific topic so that can make it easier for students to easily find courses

### Structure

The app is strucured with a backend and a frontend. Backend is only accessible by admins and from there they can add new topics or courses, manage new users or manage orders created on the frontend.

From the frontend users can search for courses, view individual course details, add ratings, buy courses or enroll to courses.

### Skeleton

### Surface

## Technologies

1. HTML
2. CSS
3. Bootstrap (v4.4.1)
4. Javascript and jQuery (v3.5.1)
5. PostgresSQL
6. Python Django

## Features

    - Existing Features:
        - create an account
        - add courses to your cart so that you can buy them from the checkout page
        - remove courses from your cart
        - search for specific courses

    - Features to Implement:
        - add images/videos as lessons
        - add courses/lessons from the frontent
        - add quizzes at the end of the courses
        - give certificates on course completion

## Testing

The app was tested on all major browsers with no known issues.

## Deployment

The site is hosted on GitHub, deployed from the master branch. The deployed site will update automatically upon new commits to the master branch.

The project is also hosted on Heroku [here](https://personaljournal.herokuapp.com/). To deploy the app to Heroku, you typically use the git push command to push the code from your local repository's master branch to your heroku remote, like so: \$ git push heroku master.

To run locally, you can clone this repository directly into the editor of your choice by pasting git clone <https://github.com/onisstudio/personal-journal-ms3.git> into your terminal. To cut ties with this GitHub repository, type git remote rm origin into the terminal.

The following process was undertaken to succesfully deploy the project on the Heroku:
    - Added a requirements.txt file using 'pip freeze > requirements.txt', so that Heroku knows which apps to install to get the project running
    - Created a Procfile with 'web: gunicorn learning_management_system.wsgi:application'
    - Pushed everything to Github
    - Created a Heroku app with all the environmental variables that I'm using within the project
    - From the Deply tab I enabled Automatic deploys

## Credits

Full Stack Frameworks module: A lot of the code added was inspired by following this module.

### Media

The photo used on the main page was obtained from [Pexels](https://www.pexels.com/).
