from locust import HttpLocust, TaskSet, task
import json


class UserTask(TaskSet):
    def on_start(self):
        with self.client.post("/token/_verifyMobile", headers={
            "Authorization": "Basic ZDBmNzg1ZWE1N2IzNDFhM2ExMTRiZWIxNmNlZjFiOTc6bnVsbA==", "X-Client": "User"},
                              data={"mobile": "15858489575", "smscode": "123"}, catch_response=True) as response:
            print(response.json())
            if response.status_code == 200:
                response.success()
                content = json.loads(response.content)
                self.locust.accessToken = content["accessToken"]
            else:
                response.failure('Failed!')

    @task(2)
    def login(self):
        with self.client.get("/user/profile", headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            print(response.json())
            print(response.status_code)
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')


class User(HttpLocust):
    host = 'http://apiv1.touchair.cn'
    accessToken = ''
    task_set = UserTask
    min_wait = 1000
    max_wait = 2000
