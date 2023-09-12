# Hng stage two task documentation

## Getting started 
All requests should be made from a valid client such as postman or a python client. To test that all endpoints works you can run the [testscript.py](/py_client/testscript.py) file located within the py_client folder using `python testscript.py`, this makes a test call to all the endpoints. The [testscript.py](/py_client/testscript.py) file is currently configured to test the online api endpoint, meanwhile if you want to use it to test the localhost, you can edit the _domain_ variable within [testscript.py](/py_client/testscript.py) and set it to the domain of your development server. Before running the testscript.py file ensure that you have the [requests](https://pypi.org/project/requests/) library installed, and your virtual environment activated (if any)

online api domain => http://codebee.pythonanywhere.com

For a step by step guide on how to configure the api on your local machine, refer to the [README.md](/README.md) file provided within this project 

# GET -> Retrieve the details of a person

``````
http://codebee.pythonanywhere.com/api/<id>
 
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
http://codebee.pythonanywhere.com/api/
 
 ``````

### Body 
```json
{
    "name": "Kyrian"
}
```


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
http://codebee.pythonanywhere.com/api/<id>
 
 ``````

 ### Path variables 
 * id -> The id of the person to be updated

 ### Body 

 ```json
  {
    "name": "Kyrian"
}
 ```


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
}` with a status code of 200 if the person was updated succesfully


# DELETE -> Remove a person
``````
http://codebee.pythonanywhere.com/api/<id>
 
 ``````

 ### Path variables 
 * id -> The id of the person to be deleted

  ### Returns

`{
    "detail": "Not found."
}` with a status of 400 if the id provided is not found 


`{
    "detail": "name deleted succesfully"
}` with a status code of 200 if the person was deleted succesfully








