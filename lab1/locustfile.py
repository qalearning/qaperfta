from locust import HttpUser, task, between
import random

PATHS = [
    "Atlanta_GA",
    "Boston_MA",
    "Charlotte_NC",
    "Chicago_IL",
    "Dallas_TX",
    "Denver_CO",
    "Detroit_MI",
    "Fort_Lauderdale_FL",
    "Houston_TX",
    "Las_Vegas_NV",
    "Los_Angeles_CA",
    "Miami_FL",
    "Minneapolis_MN",
    "New_York_NY",
    "Orlando_FL",
    "Philadelphia_PA",
    "Phoenix_AZ",
    "Portland_OR",
    "Salt_Lake_City_UT",
    "San_Diego_CA",
    "San_Francisco_CA",
    "Seattle_WA",
    "Tampa_FL",
    "Washington_D.C.",
]

class WebsiteUser(HttpUser):
    wait_time = between(2, 9)
    
    @task
    def index(self):
        self.client.get("/")

    @task(4)
    def query(self):
        self.client.get("/" + random.choice(PATHS))
