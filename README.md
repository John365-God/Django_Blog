Django Blog Website Setup Guide
This is a simple blog website built with Django and Python. 
The project contains two main apps: blog-post and bloggers.

Getting Started
To get started with the project, follow the instructions below.

Note: Most of the following commands is to be run in your terminal/bash/command prompt.

1. Clone the Project
First, clone the repository if you haven’t already done so:
In your bash,copy and past this:
`git clone https://github.com/your-username/your-repository.git`
`cd your-repository`
2. Set Up the Project
Once inside the project directory (make sure you’re in the d_blog folder), follow the steps below to get the project running.

3. Set Up Virtual Environment (Optional but Recommended)
To avoid dependency conflicts, it’s a good idea to use a virtual environment:

Install virtualenv (if not already installed):
bash
Copy and paste this:
`pip install virtualenv`

Create a virtual environment:
bash
Copy and paste this:
`python -m venv venv`
Activate the virtual environment:

Windows:
bash
Copy and paste this:
`.\venv\Scripts\activate`

macOS/Linux:
bash
Copy and paste this:
`source venv/bin/activate`

Install the project dependencies:
bash
Copy and paste this:
`pip install -r requirements.txt`

4. Running the Server
Now that everything is set up, you can run the project locally:

Run the Django development server:
bash
Copy and paste this:
`python manage.py runserver`
After running the above command, Django will provide a link in the terminal (typically http://127.0.0.1:8000/). 
Open this link in your browser to start using the website.

If you don’t see a clickable link, you can copy and paste the address (e.g., http://127.0.0.1:8000/) into your browser.

5. Starting Fresh: Wipe the Database and Start Over
If you want to wipe the database and start fresh with a clean slate, follow these steps:

1.Delete the database file:
2.Delete db.sqlite3 from the root directory of the project.
3.Delete migration files:
4.Go to both the blog-post and bloggers apps and delete the migration files.
These are located in each app’s migrations folder (except __init__.py).

Recreate the migrations:
In the terminal, run:
bash
Copy and paste this:
`python manage.py makemigrations`
This will generate new migration files based on the current state of your models.

Apply the migrations:
Now, run:
bash
Copy and paste this:
`python manage.py migrate`
This will apply the migrations and recreate the database tables.

6. Create a Superuser
After wiping the database, there will be no superuser (admin) account. Create one:
Run:
bash
Copy
`python manage.py createsuperuser`
Follow the prompts to set the username, email, and password.

7. Run the Server Again
Once the superuser is created, you can start the server again:
bash
`python manage.py runserver`
You can now log in to the Django admin panel at http://127.0.0.1:8000/admin using the superuser credentials you created earlier.

Summary of Commands:
bash
Copy
# Navigate to project folder
cd d_blog

# (Optional) Set up virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver

# To wipe the database and start fresh:
# 1. Delete db.sqlite3
# 2. Delete migration files in blog-post and bloggers apps
# 3. Run makemigrations
python manage.py makemigrations
# 4. Run migrate to apply migrations
python manage.py migrate
# 5. Create superuser
python manage.py createsuperuser
# 6. Run server again
python manage.py runserver
