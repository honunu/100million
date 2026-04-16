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
    born_datetime:datetime.datetime
    planet: Optional[Planet] =None
    ticket:Optional[TicketToEarth] = None

    def from_mars(self):
        if self.planet=="Mars":
            return True

        return False

    def send_ticket(self, ticket:TicketToEarth):
        self.ticket = ticket

    def born_years_ago(self, years:int):
        years_ago = datetime.datetime.now() - datetime.timedelta(days=years * 365)

        if self.born_datetime < years_ago:
            return True
        else:
            return False





user = User()


if user.from_mars():
    if user.born_years_ago(10):
        user.send_ticket(TicketToEarth())
    else:
        print("Not born ten years ago")
else:
    print("Not born on Mars")