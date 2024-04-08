# The API is live on
https://on-counter-billing-api.onrender.com/

## sqlite3 is used for development database and postgreSQL for deployment
> All API endpoints can be accessesed only by employees and superuser

> Employee endpoint can only be accessed by superuser

> Credentials for superuser:

>   username : admin

>   password : 123

>   endpoints : employees, customers, products, bills

> superuser can only add and access employess where it will require username and password for employees

> customers endpoint will require username and their information like address, contactNo but I have used only email for other infos

> product endpoint will require productName, inStockQuantity, productUnitPrice

> bills endpoint will require customer, employees who is on bill counter and the list of products along with its quantity


# Steps for set-up
## Run the following commands in your terminal(lines starting with # are annotations not for execution)
> #Creating a directory for the application

`mkdir billingapi`

`cd billingapi`

> #Creating environment(make sure you have python and pip installed)

`pip install venv`

`python -m venv environment`

> #activating environment

> #for windows

`environment/Scripts/activate`

>#for linux

`source environment/bin/activate`

>#Cloning the repository

`git clone https://github.com/karan-2004/on-counter-billing-api billingapi -b main`

>#changing the directory

`cd billingapi`

>#Installing dependencies

`pip install -r requirements.txt`

>#For database connectivity

`python manage.py makemigrations`

`python manage.py migrate`

# Now you are ready to run the application 
>#The final command

`python manage.py runserver`

## search `127.0.0.1:8000` in the browser







  
  
