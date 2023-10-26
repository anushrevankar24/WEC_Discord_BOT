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
check out the working video of my project  
https://github.com/anushrevankar24/WEC_Discord_BOT/assets/129506519/0feb7033-0a25-449d-99f0-a4cf51d8ff5d

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

