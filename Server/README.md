# MAPMG Intern Challenge

Welcome to the MAPMG Software Dev Intern Challenge 2019!
This project is our initial screen for Software Dev interns.

# Why Do We Do This?

As part of this project, we'd like to test your:

1. Proficiency with git version control
2. Proficiency with Python
3. Proficiency with SQL
4. Documentation standards
5. Sense of humor

Our hope is that this project will take a handful of hours,
but that it will be useful as a learning experience for you.
And maybe, just maybe, it'll actually be fun.

# So What's This Task?

The HR department has asked you to create a webservice
that can help them track intern applications in the system.
They've got a nice user interface set up, but they don't have
anywhere to store information on the applicants.

You need to create a webservice (using Python) that they can
deploy to track intern applications in a local (SQLite) database.
They've got a data analyst who will write their queries, but
their analyst needs a database specification from you as well.

You'll also need to write a simple specification to explain
how a user should enter their data, and your boss wants you
to demonstrate that it works using a series of test cases.

Finally, your boss warns you that some other departments have
similar needs and would like to be able to spin up their own
applications, so he'd be very impressed if you 
decided to create a Docker environment
that ships with your code that can build the application.

# Interface

The API interface should accept simple JSON data packet with
the following data:

- Applicant Last Name
- Applicant First Name
- Position Applied For
- Applicant School
- Applicant Degree Program

The API should be able to accept 1 or more applicants simultaneously.

# Data Storage

In the back-end, HR would like a SQLite database that spins up
as part of your application every time it launches.

HR would like you to record all of the data above, along with
the time of entry, unique identifiers for every application,
and an integrity check against a list of canonical positions
that they can provide.  For now, that will just be
the Software Development Intern position.

# Quality Control

Company coding standards require that your code be version-controlled
and well-documented.  Following best practices for software dev
and Python packaging would be advisable, such as writing READMEs
and unit tests.