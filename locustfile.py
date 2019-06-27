from locust import HttpLocust, TaskSet, task
from locust import seq_task

class myTest (TaskSet):
    def on_start(self):
        print("nova instancia do usuar")

    @seq_task(1)
    @task(2)
    def login(self):
       response =  self.client.get("/")
       print(response.status_code)
    
    @seq_task(2)
    @task(2)
    def about(self):
       self.client.get("/about")
       print("a")

    def on_stop(self):
        print("cancela nova instancia do usuar")

class usuars (HttpLocust):
    task_set = myTest
    min_wait = 5000
    max_wait = 15000

#RUN WITHOUT UI WEB
# locust -f locustfile.py --no-web -c 10 -r 10 --run-time 20 --host http://example.com