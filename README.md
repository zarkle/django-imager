# Django-Imager App
Current deployed site: http://ec2-54-218-26-248.us-west-2.compute.amazonaws.com/

**Author**: Beverly and Austin

**Version**: 0.10.0

[![Build Status](https://travis-ci.org/zarkle/django-imager.svg?branch=master)](https://travis-ci.org/zarkle/django-imager) [![Coverage Status](https://coveralls.io/repos/github/zarkle/django-imager/badge.svg?branch=master)](https://coveralls.io/github/zarkle/django-imager?branch=master)

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 301 class. (i.e. What's your problem domain?) -->
Django replica of imgur style website (image sharing) to learn how to use the Django framework.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
Clone the repo. Pip install the requirements.txt in your ENV. Create an imager database. Migrate and then runserver.

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
Python 3, Django 2, CSS/SCSS, HTML, Postgres, Travis CI, Coveralls, gunicorn, nginx, AWS EC2, AWS RDS, AWS S3, Ansible

## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an examples:

01-01-2001 4:59pm - Application now has a fully-functional express server, with GET and POST routes for the book resource.-->
- 5/10 - Ansible Deployment
- 5/9 - Tests and Sass
- 5/8 - Refactor views to class-based views and make forms for add photo and add album
- 5/3 - Deploy on AWS
- 4/30 - Tests, fix is_active profile query
- 4/27 - Photos/photo, Albums/album, tests
- 4/26 - Library, Profile, Profile/username, Photos, Albums
- 4/25 - Photo and Album tables for database.
- 4/24 - Routing, styling, and registration.
- 4/23 - Initial setup of user database and log-in/out.


## Credits and Collaborations
- Django Docs
- git.io/normalize
- gitignore.io
- codepen.io/geeksmarter/pen/akGJbm
- StackOverflow
- github.com/jrief/django-sass-processor
- Ansible Docs
