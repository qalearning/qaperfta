from locust import HttpUser, TaskSet
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

def index(l):
    l.client.get("/")

def query(l):
    l.client.get("/" + random.choice(PATHS))

class UserBehavior(TaskSet):
    tasks = {index: 1, query: 4}

    def on_start(self):
        pass

class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 9000
