import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Planet:
    id: str
    planet:str

@dataclass
class TicketToEarth():
    id:str
    spaceship="SpaceX"

@dataclass
class User:
    id:str
    username:str
    registered_datetime:datetime.datetime
    planet: Optional[Planet] =None
    ticket:Optional[TicketToEarth] = None



def send_ticket_to_earth(user:User):
    user.ticket = TicketToEarth()

user = User()
ten_years_ago = datetime.datetime.now() - datetime.timedelta(days=10 * 365)

if user.planet == "Mars":
    if user.registered_datetime < ten_years_ago:
        send_ticket_to_earth(user)
    else:
        print("Not born ten years ago")
else:
    print("Not born on Mars")