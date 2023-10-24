# WEC Discord Bot MongoDB Database CRUD Operations
**This project is a web application that allows users to perform Create, Read, Update, and Delete (CRUD) operations on different collections in a MongoDB database. The application is built using the FastAPI framework and includes functionality for managing Special Interest Groups (SIGs), upcoming events, past events, and a team of members.**

## Features
Create, Read, and Update SIGs.  
Create, Read, Update, and Delete upcoming events.  
Create, Read, Update, and Delete past events.  
Add, Update, and Read team members.  

## VIDEO
check out the working video of my project video  
https://github.com/anushrevankar24/WEC_Discord_BOT/assets/129506519/bdf09ab6-77a7-497c-86f1-22ec2875f541

## TRY IT OUT 
 **Website is live**   
 CLICK HERE : [Website Link](https://curd-web-app.onrender.com)

## Prerequisites
Python 3.x installed.  
MongoDB server (You can use MongoDB Atlas for cloud-based hosting).  
Python packages mentioned in requirements.txt installed. You can install them using pip: pip install -r requirements.txt. 

**Installation**  
To set up this project locally, follow these steps:  
Clone the repository to your local machine:
```
git clone <repository_url>  
cd <repository_directory>  
```
**Create a Python virtual environment:**  
```
python -m venv venv
```

**Activate the virtual environment:** 
```source venv/bin/activate ``` 

**Install the required packages:**  
```pip install -r requirements.txt``` 
## Usage  
To run the FastAPI web application, use the following command:  
```uvicorn main:app --reload ``` 
This will start the application locally, and you can access it in your web browser at http://localhost:8000.  

### Database Configuration
The application is configured to connect to a MongoDB database using the pymongo library. You need to provide your MongoDB connection details in the code to make the application work. You can set the username and password environment variables, or directly specify the connection URI in the code.  

**Replace the following lines with your MongoDB connection URI:**  
```
username = os.environ['username']  
password = os.environ['Password']  
uri = f"mongodb+srv://{username}:{password}@wecbot.ra9zx6y.mongodb.net/?retryWrites=true&w=majority"
```
Make sure you have a MongoDB database named WEC_Discord_Bot_DataBase created.  

## API Endpoints
GET /: Home page with navigation links to different sections.  
GET /sigs: SIGs page with options to create, update, and read SIGs.    
POST /create_sig: Create a new SIG.    
POST /update_sig: Update an existing SIG.    
GET /read_sigs: Read the list of SIGs.    
GET /upcoming_events: Upcoming events page with options to create, update, and read upcoming events.    
POST /create_upcoming_event: Create a new upcoming event.    
POST /update_upcoming_event: Update an existing upcoming event.      
POST /delete_upcoming_event: Delete an upcoming event.    
GET /read_upcoming_events: Read the list of upcoming events.   
GET /past_events: Past events page with options to create, update, and read past events.    
POST /create_past_event: Create a new past event.      
POST /update_past_event: Update an existing past event.    
POST /delete_past_event: Delete a past event.   
GET /read_past_events: Read the list of past events.    
GET /team: Team page with options to add, update, and read team members.    
POST /add_member: Add a new team member.    
POST /update_member: Update an existing team member.    
GET /read_member: Read the list of team members.    

## Contributing
Contributions to this project are welcome. You can contribute by opening issues, making pull requests, or suggesting improvements.    

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.  

Note: Remember to set up your MongoDB connection and environment variables properly before running the application.  


