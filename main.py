import os
from fastapi import Form
from fastapi import FastAPI,Request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
# from pydantic import BaseModel
from fastapi.responses import HTMLResponse
templates =Jinja2Templates(directory="templates")
app=FastAPI()
username=os.environ['username']
password = os.environ['Password']
uri = f"mongodb+srv://{username}:{password}@wecbot.ra9zx6y.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
 # Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db=client['WEC_Discord_Bot_DataBase']
@app.get("/", response_class=HTMLResponse)
async def welcome_message(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/submit", response_class=HTMLResponse)
async def submit(request: Request):
    return templates.TemplateResponse("submit.html", {"request": request

                                                      
#SIGS
@app.get("/sigs", response_class=HTMLResponse)
async def sigs(request: Request):
    return templates.TemplateResponse("sigs.html", {"request": request})
@app.post("/create_sig")
async def create_sig(name: str = Form(...),description: str = Form(...) ):
    sig_collection = db['SIGs']
    sig_data = {
            "name": name,
            "description": description
        }
    sig_collection.insert_one(sig_data)
    return {"message": "Form data processed successfully"}
@app.post("/update_sig")
async def update_sig(name: str = Form(...),description: str = Form(...) ):
    sigs_collection = db['SIGs']
    query = {"name": name}
    new_values = {"$set": {"name": name,"description": description}}
    sigs_collection.update_one(query, new_values)
    return {"message": "SIG updated successfully"}
@app.get("/read_sigs", response_class=HTMLResponse)
async def read_sigs(request: Request):
    sig_collection =  db['SIGs']
    sigs = list(sig_collection.find({}))
    return templates.TemplateResponse("sigs.html", {"request": request, "sigs": sigs})


#UPCOMING EVENTS
@app.get("/upcoming_events", response_class=HTMLResponse)
async def upcoming_events(request: Request):
    return templates.TemplateResponse("upcoming_events.html", {"request": request})
@app.post("/create_upcoming_event")
async def create_upcoming_event(request :Request,name: str = Form(...), date: str = Form(...),venue: str = Form(...),time:str = Form(...),description: str = Form(...) ):
        upcoming_event_collection = db['UPCOMING_EVENTs']
        event_data = {
                "name": name,
                "time": time,
                "date":date,
                "venue":venue,
                "description": description
            }
        
        insert_result=upcoming_event_collection.insert_one(event_data)
        if insert_result.acknowledged:
            return templates.TemplateResponse("submit.html", {"request":request})  
        else:
            print("Failed to add member to the database")
        return {"message": "Form data processed successfully"}
@app.post("/update_upcoming_event")
async def update_upcoming_event(name: str = Form(...), date: str = Form(...),venue: str = Form(...),time:str = Form(...),description: str = Form(...) ):
    upcoming_event_collection = db['UPCOMING_EVENTs']
    query = {"name": name}
    new_values = {"$set": {"name": name, "date": date, "time": time, "venue": venue, "description": description}}
    upcoming_event_collection.update_one(query, new_values)
    return {"message": "Event updated successfully"}
@app.post("/delete_upcoming_event")
async def delete_upcoming_event(name: str = Form(...)):
    delete_event_collection = db['UPCOMING_EVENTs']
    event =  delete_event_collection.find_one({"name": name})
    if event is None:
        return {"message": "Event not found"}
    delete_event_collection.delete_one({"name": name})
    return {"message": "Event deleted successfully"}
@app.get("/read_upcoming_events", response_class=HTMLResponse)
async def read_upcoming_events(request: Request):
        upcoming_event_collection = db['UPCOMING_EVENTs']
        events = list(upcoming_event_collection.find({}))
        return templates.TemplateResponse("upcoming_events.html", {"request": request, "events": events})



#PAST EVENTS
@app.get("/past_events", response_class=HTMLResponse)
async def past_events(request: Request):
    return templates.TemplateResponse("past_events.html", {"request": request})
@app.post("/create_past_event")
async def create_past_event(name: str = Form(...), date: str = Form(...),venue: str = Form(...),time:str = Form(...),description: str = Form(...) ):
        past_event_collection = db['PAST_EVENTs']
        event_data = {
                "name": name,
                "time": time,
                "date":date,
                "venue":venue,
                "description": description
            }
        past_event_collection.insert_one(event_data)
        return {"message": "Form data processed successfully"}
@app.post("/update_past_event")
async def update_past_event(name: str = Form(...), date: str = Form(...),venue: str = Form(...),time:str = Form(...),description: str = Form(...) ):
    past_event_collection = db['PAST_EVENTs']
    query = {"name": name}
    new_values = {"$set": {"name": name, "date": date, "time": time, "venue": venue, "description": description}}
    past_event_collection.update_one(query, new_values)
    return JSONResponse(content={"message": "Event updated successfully"})
@app.post("/delete_past_event")
async def delete_past_event(name: str = Form(...)):
    delete_event_collection = db['PAST_EVENTs']
    event =  delete_event_collection.find_one({"name": name})
    if event is None:
        return {"message": "Event not found"}
    delete_event_collection.delete_one({"name": name})
    return {"message": "Event deleted successfully"}
@app.get("/read_past_events", response_class=HTMLResponse)
async def read_past_events(request: Request):
        past_event_collection = db['PAST_EVENTs']
        events = list(past_event_collection.find({}))
        return templates.TemplateResponse("past_events.html", {"request": request, "events": events})




# TEAM 
@app.get("/team", response_class=HTMLResponse)
async def team(request: Request):
    return templates.TemplateResponse("team.html", {"request": request})
@app.post("/add_member")
async def add_member(request: Request,name: str = Form(...), position: str = Form(...),gmail: str = Form(...),github:str = Form(...),linkedin: str = Form(...) ):
        team_collection = db['TEAM']
        member_data = {
                "name": name,
                "position": position,
                "gmail":gmail,
                "github":github,
                "linkedin": linkedin
            }
        # team_collection.insert_one(member_data)
        team_collection.insert_one(member_data)
@app.post("/update_member")
async def update_member(name: str = Form(...), position: str = Form(...),gmail: str = Form(...),github:str = Form(...),linkedin: str = Form(...) ):
    team_collection = db['TEAM']
    query = {"name": name}
    new_values = {"$set": {"name": name, "position": position, "gmail": gmail, "github": github, "linkedin": linkedin}}
    team_collection .update_one(query, new_values)
    return {"message": "Event updated successfully"}
@app.get("/read_member", response_class=HTMLResponse)
async def read_member(request: Request):
        team_collection= db['TEAM']
        members = list(team_collection.find({}))
        return templates.TemplateResponse("team.html", {"request": request, "members": members})
