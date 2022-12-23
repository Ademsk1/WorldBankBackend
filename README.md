# WorldBankBackend
Backend for World Bank data website.
User information is stored in a PSQL database, including their username, 
password. This is linked to another table consisting of History, and 
another with the type of user accessing the site. The PSQL will be hosted 
on Heroku, alongside a Python script that is able to create/store user 
details, and their history. 
## Running the code:
### Prerequisites
To run this backend, you'll need to have access to an SQL database that can contain a set of users (Mike to do) and also access to an SQL database containing the world bank data. 
-----
### Run
In UserAccounts create a new file called .env, here you will need to set your password for logging in to the user accounts database using the key ‘PASS’
PASS=<DB_PASSWORD> (Ensure there are no spaces between the = sign)

Create another .env file in world_bank_connect and write:
WB_HOST=<HOST_ADDRESS>
WB_USERNAME=<USERNAME>
WB_DBNAME=<DATABASE_NAME>
WB_PASSWORD=<PASSWORD>

If you'd like to push this, don't forget to add the respective .env files into your .gitignore. 

Lastly, you'll need to install the requirements that can be found in world_bank_connect folder and also in UserAccounts folder, we recommend using pip3 install -r requirements.txt in both these folders. 

The backend is now ready to be ran off of an EC2 instance. To run this, run python3 server.py in the command line at the respective git directory. 
## Collaborators:
Callum Hall: Project Manager
Michael Apim: QA
