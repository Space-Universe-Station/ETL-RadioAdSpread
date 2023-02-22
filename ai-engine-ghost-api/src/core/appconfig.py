# Load .env file using:
from dotenv import load_dotenv
load_dotenv()
import os

Env= os.getenv("PYTHON_ENV")
app_port = os.getenv("PORT")
pg_pd_user= os.getenv("DB_PG_PROD_USER")
pg_pd_password= os.getenv("DB_PG_PROD_PASSWORD")
pg_pd_host =os.getenv("DB_PG_PROD_HOST")
pg_dbname= os.getenv("DB_PG_DBNAME")
pg_user= os.getenv("DB_PG_USER")
pg_password= os.getenv("DB_PG_PASSWORD")
pg_host =os.getenv("DB_PG_HOST")
mongo_host =os.getenv("DB_HOST")
mongo_port= os.getenv("DB_PORT")
mongo_user= os.getenv("DB_USER")
mongo_password= os.getenv("DB_PASSWORD")
mongo_dbname= os.getenv("DB_DBNAME")
auth_user = os.getenv("AUTH_USERNAME")
auth_password= os.getenv("AUTH_PASSWORD")
amqp_url=os.getenv("APPSETTING_AMQP_URL")
azureblob_account_url =os.getenv("AZUREBLOB_URL")
azureblob_conn =os.getenv("AZUREBLOB_CONN_STRING")