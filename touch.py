# -*- coding: UTF-8 -*-
from locust import HttpLocust, TaskSet, task
import json
import requests
import random
import queue


class UserTask(TaskSet):
    # # 手机号验证码登录
    # def on_start(self):
    #     for index in range(100):
    #         # mobile = str(random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
    #         #     random.choice("0123456789") for i in range(8)))
    #         # 手机号密码登录
    #         mobile_end = 1000000 + index
    #         mobile = "1585" + str(mobile_end)
    #         with self.client.post("/token/_verifyMobile",
    #                               headers=self.locust.header,
    #                               data={"mobile": mobile, "smscode": "123456"},
    #                               catch_response=True) as response:
    #
    #             if response.status_code == 200 or response.status_code == 201:
    #                 content = json.loads(response.content.decode("utf-8"))
    #                 data = {
    #                     "accessToken": content["accessToken"],
    #                     "refreshToken": content["refreshToken"],
    #                 }
    #                 self.locust.accessToken_queue.put_nowait(data)
    #             else:
    #                 response.failure(response.content)
    @task
    def get_access(self):
        try:
            queueData = self.locust.accessToken_queue.get()
            self.locust.accessToken_queue.put_nowait(queueData)
            with self.client.post("/token/_verifyMobile",
                                  headers=self.locust.header,
                                  data={"mobile": queueData['mobile'], "smscode": "123456"},
                                  catch_response=True) as response:

                if response.status_code == 200 or response.status_code == 201:
                    content = json.loads(response.content.decode("utf-8"))
                    data = {
                        "accessToken": content["accessToken"],
                        "refreshToken": content["refreshToken"],
                    }
                    # print(data["accessToken"])
                else:
                    print(response.status_code)
                    print(response)
                    response.failure(response.content)
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)


class User(HttpLocust):
    # host = 'http://apiv1.touchair.cn'
    hostBase = 'http://192.168.1.57:9000'
    header = {"Authorization": "Basic ZDBmNzg1ZWE1N2IzNDFhM2ExMTRiZWIxNmNlZjFiOTc6bnVsbA==", "X-Client": "User"}
    sceneId = '09aba2a9-3245-405a-92c4-d6695a1b24b1'
    # mobile = str(random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
    #     random.choice("0123456789") for i in range(8)))
    i = 0
    accessToken_queue = queue.Queue()

    for index in range(1000):
        # mobile = str(random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
        #     random.choice("0123456789") for i in range(8)))

        mobile_end = 10000000 + index
        mobile = "158" + str(mobile_end)
        data = {
            "mobile": mobile,
        }
        accessToken_queue.put_nowait(data)

    openId = "daxinghai"
    externalId = 2
    userId = 1
    refreshToken = ''
    accessToken = ''
    other_actorId = 10001
    actorId = 10001
    atrId = 680
    other_userId = 1
    tagCode = '91'
    task_set = UserTask
    questionId = 1
    questionnaireId = 1
    selectionId = 1
    zoneId = '001'
    min_wait = 1000
    max_wait = 1000
