<div id="top"></div>

<!-- PROJECT LOGO -->
<div align="center">
  <!--<a href="#">
    <img src="/static/img/logo.png" alt="Logo" width="80" height="80">
  </a>-->
  <h1 align="center">Melon Tasting Reservation Scheduler</h1>

  <p align="center">
    <br />
    Simple service to help users make reservations to go to a fancy melon tasting.
    <br />
    <a href="https://melonwell.herokuapp.com/" target="_blank">View MelonWell App</a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ul style="list-style-type: none;">
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#tech-stack">Tech Stack</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#database-model">Database Model</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</details>

<br />

<!-- ABOUT THE PROJECT -->

## About The Project

### Tech Stack

<strong>Backend:</strong> Python, [Flask](https://flask.palletsprojects.com/en/2.1.x/), [PostgreSQL](https://www.postgresql.org/), [SQLAlchemy](https://www.sqlalchemy.org/)<br />
<strong>Frontend:</strong> JavaScript, [AJAX](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX), [Jinja](https://jinja.palletsprojects.com/en/3.1.x/), [Bootstrap](https://getbootstrap.com), HTML5, CSS3, [JQuery](https://jquery.com)
<br />
<br />

### Usage

#### Registration

Returning users are able to “log in” (by entering their username).
[![MelonWell Main Page][melonwell-index]](#)

#### Search for available time slots

Users are able to pick a date and see time slots available for reservation. If the user has already booked an appointment on the chosen date the error message will be shown.
Declaring the composite UniqueConstraint as part of the `_table_args_` helps to enforse one reservation per user per day limit.
[![MelonWell Main Page][melonwell-new-reservation]](#)

#### Scheduled appointments

The page shows all reservations for a given user.
[![MelonWell Main Page][melonwell-reservations]](#)

### Database Model

_MelonWell_ is using a PostgreSQL database, with SQLAlchemy as an ORM.
[![MelonWell Model][melonwell-models]](#)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To have this app running on your local computer, please follow the steps below:

### Installation

Clone the repository:

```sh
git clone https://github.com/imagirina/reservation-scheduler.git
```

Create and activate virtual environment:

```sh
$ virtualenv env
$ echo env >> .gitignore
$ source env/bin/activate
```

Install dependencies:

```sh
$ pip install -r requirements.txt
```

Create database `spreadsheetapi` (run from bash and not from psql):

```sh
$ createdb spreadsheetapi
```

Seed the database:

```sh
$ python3 seed.py
```

Run the app from the command line:

```sh
$ python server.py
```

In your web browser, navigate to:

```sh
http://localhost:5000/
```

If you want to use SQLAlchemy to query the database, run in interactive mode:

```sh
$ python -i model.py
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Version 2.0

<ul>
  <li>User Sign Up</li>
  <li>Password hashing</li>
  <li>Timezone handling</li>
  <li>Form validation</li>
  <li>Unit tests</li>
  <li>React.js and Material UI</li>
</ul>

## Contact

👤 [imagirina](https://www.linkedin.com/in/iryna-brechko/)

## Show your support

Give a ⭐️ if you found this project helpful.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[melonwell-index]: /static/img/index.png
[melonwell-new-reservation]: /static/img/new_reservation.png
[melonwell-reservations]: /static/img/reservations.png
[melonwell-models]: /static/img/data_model.png
