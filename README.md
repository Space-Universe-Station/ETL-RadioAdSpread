## ETL-RadioAdSpread
Continuously seed your Analytics Engine database with server information whenever the function is triggered. 
### Usage
a HTTP request to the function's URL.
### Deployment
To deploy this Python script to Azure Functions, you can follow these steps:

1. Sign in to the Azure portal and create a new Function App.
2. In your Function App, create a new Python function using the "HTTP trigger" template.
3. Replace the default code in the function with the Python script from the previous answer.
4. In the function's settings, under the "Configuration" section, add the following application settings:
 - ENDPOINT: the URL of the endpoint for getting user information
 - DB_NAME: the name of your PostgreSQL database
 - DB_USER: the username for accessing your PostgreSQL database
 - DB_PASSWORD: the password for accessing your PostgreSQL database
5. Install the requests and psycopg2 modules in your function's Python environment by adding them to the requirements.txt file.
6. Deploy your function by saving and publishing it.

