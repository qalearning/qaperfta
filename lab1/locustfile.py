from locust import HttpLocust, TaskSet

def index(l):
    l.client.get("/")

def query(l, path):
    l.client.get("/" + path)

class UserBehavior(TaskSet):
    tasks = {index: 1, query: 1}

    def on_start(self):
        pass

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
