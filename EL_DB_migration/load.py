
#import libraries
import os,psycopg2,pytz
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


#load database configuration
connection = psycopg2.connect(
user = os.getenv("pg_user"),
password = os.getenv("pg_password"),
host = os.getenv("pg_host"),
database = os.getenv("pg_database")
)
cursor = connection.cursor() #connect to db
cols=set()
def CheckTableStatus(connection=connection):
    """
    This function runs a select all query on the table and prints the columns that exist
    :params - connection
    """
    cursor = connection.cursor()
    try:
        postgreSQL_select_Query = 'SELECT * FROM "BroadcasterProfile"'
        cursor.execute(postgreSQL_select_Query)
        column_names = [desc[0] for desc in cursor.description]
        for i in column_names:
            cols.add(i)
        print(cols)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()
        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Id = ", row[0], )
            print("Model = ", row[1])
            print("Price  = ", row[2], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def bulkLoadBroadcasters(records:list,connection=connection):
    """
    This function runs an insert query on the table
    :params - connection
    :params - records
    """
    cursor = connection.cursor()
    try:
        sql_insert_query = 'INSERT INTO "BroadcasterProfile" (banner, country, fullname, name,"userId","positionHeld",address,state,city,zipcode,"radioStationWebsite","radioStationDigitalStreaUrl","radioStationCategory","phoneNumber","updatedAt") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # execute many() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into broadcasters table")
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into broadcasters table {}".format(error))
 

def bulkLoadUsers(records:list,connection=connection):
    """
    This function runs an insert query on the table
    :params - connection
    :params - records
    """
    cursor = connection.cursor()
    try:
        sql_insert_query = 'INSERT INTO users ("verificationCode", "isApproved", password, email,"updatedAt") VALUES (%s,%s,%s,%s,%s)'
        # execute many() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into users table")
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into users table {}".format(error))


def bulkLoadUserGroup(records:list,connection=connection):
    """
    This function runs an insert query on the table
    :params - connection
    :params - records
    """
    cursor = connection.cursor()
    try:
        sql_insert_query = 'INSERT INTO "UserGroup" ("userId","groupId","updatedAt") VALUES (%s,%s,%s)'
        # execute many() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into usergroup table")
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into usergroup table {}".format(error))
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def LoadDefaultSlots(records:list,connection=connection):
    """
    This function runs an insert query on the table
    :params - connection
    :params - records
    """
    cursor = connection.cursor()
    try:
        sql_insert_query = 'INSERT INTO "Slot" (id,"broadcasterId","startTime","endTime", "Ann50WordsPrice", "Ann75WordsPrice","Ann100WordsPrice","Jingle30SecPrice", "Jingle45SecPrice",  "Jingle60SecPrice","Jingle15SecPrice","updatedAt") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # execute many() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into slots table")
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into slots table {}".format(error))
        
utc = pytz.timezone('GMT')
# Create a datetime object with the current date and time
dt = datetime(1970, 1, 1, 0, 0, 0,tzinfo=utc)
dt_h = datetime(1970, 1, 1, 0, 59, 0,tzinfo=utc)
#initialize variables
slot_list=[]
b=9
id=1
for i in range(0,100):
  slot_list.append((id,b,dt,dt_h,5000,5000,5000,5000,5000,5000,5000,datetime.now()))
  id+=1
  b+=1

#print(slot_list[0])
LoadDefaultSlots(slot_list)