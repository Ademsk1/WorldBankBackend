# WorldBankBackend
Backend for World Bank data website.
User information is stored in a PSQL database, including their username, 
password. This is linked to another table consisting of History, and 
another with the type of user accessing the site. The PSQL will be hosted 
on Heroku, alongside a Python script that is able to create/store user 
details, and their history. 
## Running the code:

Fork and clone this and world front end repo.
In the backend create a new virtual environment using:

  python3 -m venv venv
  source venv/bin/activate
  
In UserAccounts create a new file called .env, here you will need to set your password for logging in to the user accounts database using the key ‘PASS’
PASS=<DB_PASSWORD> (Ensure there are no spaces between the = sign)

Now on the command line cd to UserAccounts file and run:
  pip3 install -r requirements.txt
Now type in cd .. and then run in the CL:
python3 server.py
## Collaborators:
Callum Hall: Project Manager
Michael Apim: QA
