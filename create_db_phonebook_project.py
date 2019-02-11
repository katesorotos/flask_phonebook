import json
import sqlite3
import requests

person_data_list = json.loads(open('./person_data.json').read())
business_data_list = json.loads(open('./business.json').read())

def getdb():
    """
        check we can connect to db.
    """
    try:
        conn = sqlite3.connect('phonebook_project.db')
        c = conn.cursor()
        return c, conn
    except:        
        return False
    
def create_table(table_name, column_name):
  """
  input: table name and column names
  output: table.
  creates a table within phonebook database.
  """
  column_names = ", ".join(column_name)
  db = getdb()
  c = db[0]
  conn = db[1]
  query_string = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, column_names)
     
  c.execute(query_string)
 
  conn.commit()
 


def add_data_to_table(table_name, data_for_table, column_name):
    """
    input: data for table.
    output:data into table.
    adds data to tables.
    """
    question_mark = []
    for n in range(len(column_name)):
        question_mark.append("?")
    question_mark = ", ".join(question_mark)
    column_names = ", ".join(column_name)
    
    for item in data_for_table:
        column_name_list = []
        for thing in column_name:
            thing = item[thing]
            column_name_list.append(thing)
        add_data = 'INSERT INTO {} ({}) VALUES({})'.format(table_name, column_names, question_mark)
        db = getdb()
        c = db[0]
        conn = db[1]
        c.execute(add_data, column_name_list)
        conn.commit()

def dynamic_coordinates_data_entry():
     """
         adds unique postcodes from person and business table into coordinates table.
         input: postcodes from person and business table (minus duplicates)
         output: postcodes in  coordinate table.
         
     """
     postcode_list = []
     for item in person_data_list:
         postcode_list.append(item["postcode"])
     
     for item in business_data_list:
         postcode_list.append(item["postcode"])


     unique_postcode_list = set(postcode_list)
     
     endpoint = "https://api.postcodes.io/postcodes/"
     coor_dict = []
     
     for item in unique_postcode_list:
        
        payload = item
        
        
        postcode_response = requests.get(endpoint + payload)
        data_postcode = postcode_response.json()
        
        if data_postcode["status"] == 200:
            longitude_val = data_postcode['result']['longitude']
            latitude_val = data_postcode['result']['latitude']
            dic_1 = {"postcode": payload, "longitude": longitude_val, "latitude": latitude_val} 
            coor_dict.append(dic_1)
#            return "coordinates", coor_dict, ["postcode", "longitude", "latitude"]
        
        else: 
            pass
        
     add_data_to_table("coordinates", coor_dict, ["postcode", "longitude", "latitude"])
        
#create_table("person", ["first_name TEXT", "last_name TEXT", "address_line_1 TEXT", "address_line_2 TEXT", "address_line_3 TEXT", "postcode TEXT", "country TEXT", "telephone_number TEXT"])
#create_table("business", ["business_name TEXT", "address_line_1 TEXT", "address_line_2 TEXT", "address_line_3 TEXT", "postcode TEXT", "country TEXT", "telephone_number TEXT", "business_category TEXT"])
#create_table("coordinates", ["postcode TEXT", "longitude INT", "latitude INT"])
#
#add_data_to_table("person", person_data_list, ["first_name", "last_name", "address_line_1", "address_line_2", "address_line_3", "postcode", "country", "telephone_number"])
#add_data_to_table("business", business_data_list, ["business_name", "address_line_1", "address_line_2", "address_line_3", "postcode", "country", "telephone_number", "business_category"])
#dynamic_coordinates_data_entry()