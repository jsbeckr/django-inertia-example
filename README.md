# Django Inertia.js Example

## Introduction

~~This is an example repository to show of the [inertia-django](https://github.com/jsbeckr/inertia-django) adapter for [Inertia.js](https://github.com/inertiajs).~~

> **WARNING:** This is my local development project. A proper demo is in the making.

## Requirements

You have to have Node installed (for some webpack fun) and [pipenv](https://pipenv.readthedocs.io/en/latest/) to install the dependencies.

* Node
* pipenv

## Installation

Run the following commands to install the node and django dependencies:

```
$ npm i
$ pipenv install
$ pipenv shell
$ pipenv run python manage.py migrate
```

## Run

First start webpack:

```
$ npm start
```

And afterwards run django:
```
$ pipenv run python manage.py runserver
```

## Issues

Have you encountered any issues? Please report them either here https://github.com/jsbeckr/django-inertia-example/issues or in the main repo https://github.com/jsbeckr/inertia-django/issues.
