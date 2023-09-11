# HNGx Backend track -STAGE TWO TASK SETUP GUIDE 

## Technologies 
* Python -> Django -> Django rest framework

# Steps to run

1. Clone the github repo
    * `https://github.com/Codebee50/HNG-stage-two.git`

2. Create a virtual environment 
    * From your terminal, navigate into the Stagetwo directory and create a virtual environment using `python -m venv venv`

3. Activate the virtual environment
    
    * Activate the virtual environment using `.\venv\Scripts\activate` on windows and `source venv/bin/activate ` for mac and Linux

4. Install requirements 
    * All requirements for this projects are located in the requirements.txt file, install all of them using the command `pip install -r requirements.txt` 

5. Run the server 
    * From your terminal, enter into the **backend** folder, this is the root directory for the project 

    * Run `python manage.py runserver <port>` to get the server running on your specified port or  `python manage.py runserver` to ge the server running on the default port which is **8000**

6. Access the api
    * Your api should now be accesible on `localhost:<port>/api`. For a detailed guide on how to use the endpoints in this project, refer to the **DOCUMENTATION.md** file located within this project 

7. Use test scripts
    * From your terminal, navigate into the py_client folder this contains a _testscript.py_ file which makes test calls to all the api endpoint to ensure proper functionality, the _testscript.py_ is currently configured to make requests to the online endpoint at 'https://codebee.pythonanywhere.com' In the case where you would like to make test calls to localhost, modify the _domain_ variable in testscript.py accordingly. Run the script using `python testscript.py` 


