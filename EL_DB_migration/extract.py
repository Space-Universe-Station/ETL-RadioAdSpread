
#!pip3 install mysql-connector-python==8.0.29
#import libraries
import argon2,os,datetime
import mysql.connector
from load import *
from graphql_automation import *
from dotenv import load_dotenv
load_dotenv()

#load database configuration
config_source = {
  'user': os.getenv("mysql_user"),
  'password': os.getenv("mysql_password"),
  'host': os.getenv("mysql_host"),
  'database': os.getenv("mysql_database"),
}
cnx_source = mysql.connector.connect(**config_source) #connect to db
cursor_source = cnx_source.cursor() #set cursor
query_source = ("SELECT * FROM radioa26_radioad.vendors") #run query to select all records on vendors table
cursor_source.execute(query_source) #execute the query
#initialize variables
usergroup_list = []
user_list = []
broadcaster_list = []
broadcaster_register_list = []
k=7
password = "myPassword1234" #set default password
password_bytes = bytes(password, "utf-8") #convert password to byte for encryption
hash = argon2.hash_password(password_bytes) #encrypt password with argon2
hash_str = hash.decode().lstrip("b") # Convert the bytes object to a string and remove the leading "b" character
#iterate through the records and append to lists
for i in cursor_source: # type: ignore  
  #user_list.append(('1234',True,hash_str,i[3],datetime.now())) # type: ignore 
  #usergroup_list.append((k,2,datetime.now())) # type: ignore 
  #broadcaster_list.append((i[9],"nigeria",i[2],i[4],k,"","","","","","","","","",datetime.now())) # type: ignore 
  broadcaster_register_list.append(("nigeria",i[2],i[4],"","","","","","","","",i[3],hash_str))
  #k+=1

#migrate data
#bulkLoadUsers(user_list)
#bulkLoadBroadcasters(broadcaster_list)
#bulkLoadUserGroup(usergroup_list)
for i in broadcaster_register_list:
  BulkRegisterBroadcasters(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12])


















"""
for i in cursor_source:
    id.append(i[0])
    supportid.append(i[1])
    name.append(i[2])
    email.append(i[3])
    username.append(i[4])
    email_verified_at.append(i[5])
    password.append(i[6])
    remember_token.append(i[7])
    current_team_id.append(i[8])
    profile_photo_path.append(i[9])
    status.append(i[10])
    verification_code.append(i[11])
    slugs.append(i[12])
    created_at.append(i[13])
    updated_at.append(i[14])
len(email)

data_dict = {
#'id' :id,
#'supportid' :supportid,
'name' :name,
'email' :email,
'username' :username,
'email_verified_at' :email_verified_at,
'password' :password,
'remember_token' :remember_token,
'current_team_id' :current_team_id,
'profile_photo_path' :profile_photo_path,
'status' :status,
'verification_code' :verification_code,
'slugs' :slugs,
#'created_at' :created_at,
#'updated_at' :updated_at
}
print(data_dict)
#bulkLoad()

'address', 'banner', 'city', 'country', 'createdAt', 'fullname', 'id', 'name', 'phoneNumber', 'positionHeld', 
'radioStationCategory', 'radioStationDigitalStreaUrl',
 'radioStationWebsite', 'recommended', 'state', 'updatedAt', 'userId', 'zipcode'
"""