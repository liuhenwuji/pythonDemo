from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    # @task
    # def post_user_tags(self):
    #     with self.client.post("/user/tags",
    #                           headers={"Authorization": "Bearer %s" % self.locust.accessToken, "X-Client": "User"},
    #                           json={
    #                               "codes": ["91", "92"]
    #                           },
    #                           catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         elif response.status_code != 0:
    #             print(response.status_code)
    #             print(response.content)
    #             response.failure(response.content)

    @task(1)
    def task1(self):
        with self.client.get("/actors/10001",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken, "X-Client": "User"},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    @task(1)
    def task2(self):
        with self.client.get("/user/profile",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken, "X-Client": "User"},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    @task(1)
    def task3(self):
        with self.client.post("/search",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken, "X-Client": "User"},
                              json={
                                  "keywords": "苏州",
                                  "tagCode": ""
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)


class WebsiteUser(HttpLocust):
    accessToken = '5208A41C57F969E5'
    # accessToken = '1198EEA82966D885'
    task_set = UserBehavior
    min_wait = 10
    max_wait = 10
