# Web Enthusiasts' Club Discord Bot
## WEC Discord Bot Logo
![WEC_logo](https://github.com/anushrevankar24/WEC_Discord_BOT/assets/129506519/54ed6c3e-dd8b-45d4-b4ba-3e0029530409)


## Introduction
Discord is a popular communication platform designed for creating communities. It's not only widely used by gamers but is also a versatile tool for various interest groups, businesses, and developers. This project focuses on the development of an interactive Discord bot for the Web Enthusiasts' Club (WEC). The bot is designed to provide information about the club, including upcoming events, Special Interest Groups (SIGs), past events within SIGs, non-technical events, and details about club members.

## Features
Hello Command: Greet the bot with a simple "Hello!" command.  
List SIGs Command: Get information about the Special Interest Groups (SIGs) within the Web Enthusiasts' Club.  
Past Events Command: Retrieve details about past events held within the club, including event name, date, time, venue, and description.  
Upcoming Events Command: Find out about upcoming 



events within the club, including event name, date, time, venue, and description.   
Team Command: Get to know the club's team members, including their names, positions, GitHub profiles, Gmail addresses, and LinkedIn profiles.  

## VIDEO
**Check out the working video of my project**     
[Video Link](https://drive.google.com/file/d/1Q0qZMuDsVy_Mtnjf1t3fvu80fCkRF5vg/view?usp=drivesdk)

## TRY IT OUT :
**IMPORTANT INSTRUCTIONS**    

**Step 1: Run the Replit Code**    

[Replit Code Link](https://replit.com/@AnushRevankar/WEC-Bot)
1) Click on the above provided link to access the Replit code for the Discord bot.    
2) Run the code by clicking the "Run" or "Start" button within the Replit environment. This action will initiate the bot and make it operational.
 
**Step 2: Invite the Bot to Your Server**  

After running the code successfully, the bot is now online       
1) To invite the bot to your Discord server, click on this link :  [Invite link](https://discord.com/api/oauth2/authorize?client_id=1163899289211240509&permissions=1084479764544&scope=bot)     
2) Choose the Discord server to which you want to invite the bot and follow the on-screen instructions to complete the invitation process.
   After completing the process the bot wll be successfully added to your server
    
**Once the bot is set up and running, you can interact with it using the following commands in your Discord server:**

**$hello** or **$HELLO** or **$Hello** : Greet the bot with a friendly "Hello!"

**$sigs** or **$SIGs** or **$list_sigs**  : Get a list of the Special Interest Groups (SIGs) in the Web Enthusiasts' Club. 

**$pastevents** or **$pevents** or **$past events** or **$past_events**  : Retrieve information about past events, including event name, date, time, venue, and description.  

**$upcomingevents** or **$uevents** or **$upcoming events**or **$upcoming_events** : Find out about upcoming events, including event name, date, time, venue, and description. 

**$team** or **$TEAM** or **$core** : Get to know the club's team members, including their names, positions, GitHub profiles, Gmail addresses, and LinkedIn profiles.


## Technologies Used
Discord.py: The Discord API wrapper that allows the bot to interact with the Discord platform.  

MongoDB: A NoSQL database used to store information about the Web Enthusiasts' Club, including SIGs, events, and team members.  

##  Installation and Setup
To set up this Discord bot, follow these steps:  

**Clone the repository:**  
Then run these commands in the bash terminal  
git clone <repository_url>  
cd web-enthusiasts-club-bot  

**Install the required Python packages:**  
bash
pip install -r requirements.txt   

**Set up your MongoDB database:**  
Create a MongoDB database on MongoDB Atlas.    
Obtain the connection URI.  
Set the username and password environment variables with your MongoDB credentials.    

**Set up a Discord bot:**  
Create a new bot on the Discord Developer Portal.  
Get the bot token.  

**Create a .env file in the project directory with the following content:**  
dotenv  
TOKEN=<your_discord_bot_token>  
username=<your_mongodb_username>   
password=<your_mongodb_password>  
Run the bot:  

## Contributing
We welcome contributions from the community. If you have any ideas or improvements to suggest, please follow these guidelines:

Fork the repository.  
Create a new branch for your feature or bug fix: git checkout -b feature/your-feature-name.  
Make your changes and commit them with clear and concise messages.   
Push your changes to your fork.   
Create a pull request to the main repository's main branch.   

## License  
This project is open-source and available under the MIT License.


# WEC Discord Bot MongoDB Database CRUD Operations
**This project is a web application that allows users to perform Create, Read, Update, and Delete (CRUD) operations on different collections in a MongoDB database. The application is built using the FastAPI framework and includes functionality for managing Special Interest Groups (SIGs), upcoming events, past events, and a team of members.**

## Features
Create, Read, and Update SIGs.  
Create, Read, Update, and Delete upcoming events.  
Create, Read, Update, and Delete past events.  
Add, Update, and Read team members.  

## VIDEO
**Check out the working video of my project**   
[Video Link](https://drive.google.com/file/d/1QAKrkHmouR2oB6LFRJLC70ACLvGa8pFp/view?usp=drivesdk)



## TRY IT OUT 
 **Website is live**   
 CLICK HERE : [Website Link](https://curd-web-app.onrender.com)  
 **Note** : The website may take some time to Load  

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


