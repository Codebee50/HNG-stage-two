# Hng stage two task documentation

## Getting started 
Request should be made from a valid client such as postman or a python client, to test that all endpoints works you can run the **testscript.py** file located withing the py_client folder using `python testscript.py`, this makes a test call to all the endpoints

api domain => codebee.pythonanywhere.com

# GET -> Retrieve the details of a person

``````
http://codebee.pythonanyhere.com/api/<id>
 
 ``````

### Path variables 
 * id -> The id of the person to be retrieved

### Returns
`{
    "detail": "Not found."
}` with a status of 400 if the no person matches the provided id 

`{
    "id": id,
    "name": name
}` with a status of 200 if the request was succesfull 


# POST -> Add a person 
``````
http://codebee.pythonanyhere.com/api/
 
 ``````

### Body 
name -> the name of the person to be added

### Returns
`{
    "name": [
        "The name name already exists"
    ]
}` and a status code of 400 if the provided name is found in the database

`{
    "id": id,
    "name": name
}` with a status code of 201 if the person was created succcesfully

# PATCH -> update a person 

``````
http://codebee.pythonanyhere.com/api/<id>
 
 ``````

 ### Path variables 
 * id -> The id of the person to be updated

 ### Body 
name -> the new name of the person 


 ### Returns
`{
    "name": [
        "The name name already exists"
    ]
}` with a status of 400 if the name provided is already present in the database

`{
    "detail": "Not found."
}` with a status of 400 if the id provided is not found 


`{
    "id": id,
    "name": name
}` if the person was updated succesfully


# Delete -> Remove a person
``````
http://codebee.pythonanyhere.com/api/<id>
 
 ``````

 ### Path variables 
 * id -> The id of the person to be deleted

  ### Returns

`{
    "detail": "Not found."
}` with a status of 400 if the id provided is not found 


`{
    "detail": "name deleted succesfully"
}` if the person was deleted succesfully








