## Setup (Tested with python3.6)
1. Clone the repo from: https://github.com/lucifurtun/issue-tracker.git
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`


## A few notes
1. From the specs (I also explicitly asked) it doesn't seem to a exist the "normal" user role. So, a normal user
doesn't have any permission regarding issues, it can only update it's on configuration.
2. I didn't see any workflow for adding issues, so I assumed that the users that have the manipulate issues,
will choose manually every field of the issue, including `solver` and `submitter`.
3. No listing rules were specified, so I assumed that the users that have the right to read issues, should see them all.
4. It's not clear what "problem solving time" means, so I assumed it's the time that an issue spends it "In Progress",
I called this field duration.


## Requirements (exactly as received):

Design and implement a simple issue tracker in Django:
- Issue has submitter, solver, text description, status, category (e.g. bug, enhancements, documentation)
- Issues can be added, edited, and will have page with a list  (Django Admin or any other library can be used)
- Issue list displays simple statistics in the header (average, longest, and shortest problem solving time)
- You only have a category in the DB, without administration, but in the future it should be as simple as possible
- 2 user roles: superuser and staff, staff cannot change or add anything, the superuser can do everything
- meaningful version of Git
- as a DB is enough to use DBlite
- It must be clear how to install and run

### Updates:

Q: "You only have a category in the DB, without administration, but in the future it should be as simple as possible"
What category are we talking about here ? The issue category ? The same from the first bullet ?   
A: The issue category.

Q: "2 user roles: superuser and staff, staff cannot change or add anything, the superuser can do everything"
Won't we have a normal user role ? Who is the one who is adding issues ? What does it mean that "staff cannot change or add anything" ? Can't staff add it's own issues ?   
A: staff can only see and edit asigned issues, superuser can create issues can do everything

Q: Do we need user management ? I mean user login/signup functionality.   
A: yes we need it. Login, configuration, set password, etc.

Q: "meaningful version of Git"
I don't quite understand this statement. How can a version of Git be meaningful ? Do you mean to use Git and to provide meaningful commit messages ? Are you interested in Pull Requests and Branches for this task ?   
A: readable comments, commits can be logicaly parted, etc.

Q: "as a DB is enough to use DBlite"
Do you mean "SQLite" ?   
A: Yes it should be SQLite.
