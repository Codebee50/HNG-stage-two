import requests
from rest_framework import status

domain = 'http://localhost:8000' #this is the domain where the project is currently hosted or running

create_endpoint = domain+'/api/'

def testDeleteEndpoint(person):
    #getting the id of the person to be deleted
    #this is the id of the person who was updated in the testUpdateEndpoint function 
    person_id = person.get('id')
    person_name = person.get('name')

    print(f'Deleting {person_name}...')
    
    #using the id to form an endpoint 
    delete_endpoint = domain + f'/api/{str(person_id)}'

    delete_request = requests.delete(delete_endpoint)
    print(delete_request.json())
    print('Test complete all tests passed!')
    


def testUpdateEndpoint(person):
    #getting the id of the person to be updated
    #this is the id of the person who was retrieved in the testGetEndpoint function 
    person_id = person.get('id')
    old_name = person.get('name')
    new_name = 'Onuh'


    update_endpoint = domain + f'/api/{str(person_id)}'
    print(f'Renaming {old_name} to {new_name}')
    data = {
        'name': new_name
    }
    update_request = requests.patch(update_endpoint, data=data)

    if update_request.status_code == status.HTTP_201_CREATED:
        print('User updated succesfully')
        print(update_request.json())
        testDeleteEndpoint(update_request.json())

    else:
        print(update_request.json())




def testGetEndpoint(create_request):
    print('Fetching user...')

    person_id = create_request.json().get('id') #using the id of the user who was just created to test the get endpoing
    get_endpoint = domain + '/api/' + str(person_id)

    get_request = requests.get(get_endpoint)
    print(get_request.json())
    if(get_request.status_code == status.HTTP_200_OK): 
        #updating the user who was just created
        testUpdateEndpoint(get_request.json()) 




def testCreateEndpoint():
    print('Creating a user...')

    data ={
        'name': 'Charles'
    }
    #Making a reqeust to the create user endpoint
    create_request = requests.post(create_endpoint, json=data)

    if create_request.status_code == status.HTTP_201_CREATED:
        print('User created succesfully.')
        
        testGetEndpoint(create_request=create_request)
    else:
        print(create_request.json())


#calling the test create endpoint function starts a chain of calling other functions
testCreateEndpoint()


    








