#Part 1
#students = [
     # {'first_name':  'Michael', 'last_name': 'Jordan'},
     # {'first_name': 'John', 'last_name': 'Rosales'},
     # {'first_name': 'Mark', 'last_name': 'Guillen'},
     # {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

#for item in students:
         #print item['first_name'], item['last_name']
users = {
'students' :[
     {'id':1,'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'id':2,'first_name' : 'John', 'last_name' : 'Rosales'},
     {'id':3,'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'id':4,'first_name' : 'KB', 'last_name' : 'Tonel'}
],
'Instructors': [
     {'id':1,'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'id':2,'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for title, people in users.items():
    count = 1
    for person in people
    name = person["first_name"] + "" + person["last_name"]
    print count, "-", name.upper(), len(name)-1
