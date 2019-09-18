from locust import HttpLocust, TaskSet
from locust import task, seq_task

class myTest (TaskSet):
    def on_start(self):
        print("New Usuar Instance")

    def on_stop(self):
        print("Cancel Usuar Instance")

    @seq_task(1)
    @task(50)
    def login(self):
       response =  self.client.get("/")
       print(response.status_code)
    
    @seq_task(2)
    @task(2)
    def about(self):
       self.client.get("/about")

class vUsuars (HttpLocust):
    task_set = myTest
    min_wait = 1000
    max_wait = 5000

# RUN WITHOUT UI WEB
# locust -f locustfile.py --no-web -c 10 -r 10 --r20s --csv=testeMeetup --host http://example.com
# --no-web = Run Locust without ui interface
# -c = Number of Locust users to spawn
# -r = Number of users to spawn per second
# -r = Set the timeout for the test
# --csv = Retrieve test statistics in .CSV format