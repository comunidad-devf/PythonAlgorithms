"""Cruch Data."""
import json
import csv
import xml.dom.minidom
from dict2xml import dict2xml

users = []

with open('users_database.json', 'r') as js:
    users = json.load(js)
    users = sorted(users, key=lambda k: k['id'])

with open('users_database.csv', 'r') as cs:
    rows = list(csv.reader(cs))
    for row in rows[1:]:
        t_id = int(row[0])
        t_program = row[1]
        t_score = float(row[2])
        users[t_id-1]['program'] = t_program
        users[t_id-1]['score'] = t_score

DOMTree = xml.dom.minidom.parse("users_database.xml")
collection = DOMTree.documentElement
xml_users = collection.getElementsByTagName("users")

for user in xml_users:
    t_id = int(user.getElementsByTagName('id')[0].childNodes[0].data)
    t_first_name = user.getElementsByTagName('firstName')[0].childNodes[0].data
    t_last_name = user.getElementsByTagName('lastName')[0].childNodes[0].data
    users[t_id-1]['first_name'] = t_first_name
    users[t_id-1]['last_name'] = t_last_name

xml_file_content = dict2xml(users, wrap="users", indent="  ")
open('crunched_users_database.xml', 'w').write(xml_file_content)

with open('crunched_users_database.json', 'w') as cud:
    json.dump(users, cud, indent=2)

csv_file = open('crunched_users_database.csv', 'w')
csv_file.write('id,email,first_name,last_name,age,program,score\n')
for user in users:
    line = "{id},{email},{first_name},{last_name},{age},{program},{score}\n".format(
        id=user['id'],
        email=user['email'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        age=user['age'],
        program=user['program'],
        score=user['score']
    )
    csv_file.write(line)
