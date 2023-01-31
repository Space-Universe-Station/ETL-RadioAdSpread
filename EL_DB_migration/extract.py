
#!pip3 install mysql-connector-python==8.0.29
#import libraries
import csv
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
query_source = ("""
SELECT *
FROM radioa26_radioad.vendors
LEFT JOIN radioa26_radioad.vendor_rs_information
ON  radioa26_radioad.vendors.id = radioa26_radioad.vendor_rs_information.vendor_id
LEFT JOIN radioa26_radioad.vendor_profiles
ON radioa26_radioad.vendor_profiles.rs_id = radioa26_radioad.vendors.id;
""") #run query to select all records on vendors table
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
# for i in cursor_source: # type: ignore  
  #user_list.append(('1234',True,hash_str,i[3],datetime.now())) # type: ignore 
  #usergroup_list.append((k,2,datetime.now())) # type: ignore 
  #broadcaster_list.append((i[9],"nigeria",i[2],i[4],k,"","","","","","","","","",datetime.now())) # type: ignore 
  #k+=1

#migrate data
#bulkLoadUsers(user_list)
#bulkLoadBroadcasters(broadcaster_list)
#bulkLoadUserGroup(usergroup_list)


#Graphql Broadcasters query

# 
# (1, None, 'Beat FM', 'enquiries@thebeat99.com ', 'Beat FM Lagos', None, 
# '$2y$10$8tUerc3S8fXyRe9I60gUcetc8KdGrhrdDoLlaBlVRpWYSsbMli...',
# 'HzlcHBt9UUqbefQOhvyBVIyavIpDJ4ShKT9i2HT3IybD3T2Bw2bdhdTqJPEO',
# None, 'radiostation_1356882191.jpg', 'APPROVED', ' ', None, datetime.datetime(2021, 2, 19, 5, 11, 38),
# datetime.datetime(2021, 12, 21, 12, 48, 50), 1, 1,
# None, None, None, None, None, 'The HeartBeat of Lagos', 'Lagos', None, None)
#

# (1, None, 'Beat FM', 'enquiries@thebeat99.com ', 'Beat FM Lagos', None, 
# '$2y$10$8tUerc3S8fXyRe9I60gUcetc8KdGrhrdDoLlaBlVRpWYSsbMli...',
#  'HzlcHBt9UUqbefQOhvyBVIyavIpDJ4ShKT9i2HT3IybD3T2Bw2bdhdTqJPEO', None, 'radiostation_1356882191.jpg', 'APPROVED',
#   ' ', None, datetime.datetime(2021, 2, 19, 5, 11, 38), datetime.datetime(2021, 12, 21, 12, 48, 50),
#  1, 1, None, None, None, None, None, 'The HeartBeat of Lagos', 'Lagos', None, None, 1, 1, 'Sharon Chuks-Nwoko',
#   'Digital Marketing Executive', '08157184246', '26, Keffi Street, Ikoyi, Lagos', 'Ikoyi', 'Lagos', 
#   '0000', 'Nigeria', 'https://thebeat99.com',
#   'Music & Lifestyle', 'https://http://www.thebeat99.com/listen-live', 'beat-fm', None, {'NO'},
# {'NO'}, datetime.datetime(2021, 2, 19, 5, 11, 38), datetime.datetime(2021, 2, 19, 5, 11, 38))

# UPDATE table_name
# SET column_1 = 'default',
#     column_2 = 'default',
#     ...
#     column_n = 'default'
# WHERE column_1 IS NULL OR
#       column_2 IS NULL OR
#       ...
#       column_n IS NULL;


for i in cursor_source: # type: ignore
  broadcaster_register_list.append((i[35],i[2],i[28],i[29],i[31],i[33],i[32],i[36],i[38],i[37],i[30],i[3],"myPassword1234",i[22],i[9]))
  #broadcaster_register_list.append(("nigeria",i[2],i[4],"","",i[23],"","","","","",i[3],hash_str,i[22],i[9]))
  # print(i)
#print(broadcaster_register_list)

# Open the file for writing
# with open('spring_db.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
    
#     # Write the header row
#     writer.writerow(['Name', 'Age'])
    
#     # Write the data rows
#     for row in broadcaster_register_list:
#         writer.writerow(row)

for i in broadcaster_register_list:
  BulkRegisterBroadcasters(country=i[0],name=i[1], fullname=i[2], positionHeld=i[3],address=i[4],state=i[5],city=i[6],
    radioStationWebsite=i[7],radioStationDigitalStreaUrl=i[8],
    radioStationCategory=i[9],phoneNumber=i[10],email=i[11],password=i[12],tagline=i[13],banner=i[14])


















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