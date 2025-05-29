PROJECT - A COURSE ENROLLMENT CLI APP

this is a cli application for managing instructors, courses, and student enrollments.It uses SQLite.

<!-- Features -->

   -Add and list instructors.
   -Add and list courses(with instructor assignment)
   -Add and list students.
   -Enroll students with multiple courses.
   -View students enrolled in a course.
   -View all courses a student is enrolled in 


<!-- Running the app -->

To use the app, run the following command in your terminal
    $ python lib/cli.py

<!-- HOW IT WORKS -->
-data is stored using SQLite in the database.db

-models define and interact with their specific tables, e.g student model interacts with student tables, type shi

-a join table student_courses is a many to many relationship btwn students and courses

-helper functions manage common operations like enrollment and lookup

-the cli is a simple interface to use all these features interactively


<!-- AUTHOR -->

This project is made by [Lewis Njuma]