# -*- coding: UTF-8 -*-
from locust import HttpLocust, TaskSet, task
import json
import requests
import queue
import random


# import resource


class UserTask(TaskSet):
    def get_access(self):
        try:
            # data = self.locust.accessToken_queue.get()
            # self.locust.accessToken_queue.put_nowait(data)
            # return data['accessToken']
            return self.locust.accessTokens[random.randint(0, 1999)]
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)

    # 获取用户信息
    @task(2)
    def user_profile(self):
        # print(self.get_access())
        with self.client.get("/user/profile",
                             headers={"Authorization": "Bearer %s" % self.get_access(),
                                      'User-Agent': 'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)'},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 更新用户信息
    @task(2)
    def update_user_profile(self):
        with self.client.post("/user/profile",
                              headers={"Authorization": "Bearer %s" % self.get_access(),
                                       'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1)'},
                              json={
                                  "city": "三明",
                                  "company": "苏州触达",
                                  "country": "中国",
                                  "department": "软件部门"
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # # 绑定微信号
    # @task(2)
    # def bind_wechat(self):
    #     with self.client.post("/user/profile/wechat",
    #                           headers={"Authorization": "Bearer %s" % self.get_access(),'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:4.0) Gecko/20100101 Firefox/24.0'},
    #                           json={
    #                               "openId": "xinghai"
    #                           },
    #                           catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print(response.content)
    #             response.failure(response.content)


    '''
        我的朋友
    '''

    # # 添加展商为好友
    # @task(2)
    # def friend_actor(self):
    #     with self.client.post("/friend/actor",
    #                           headers={"Authorization": "Bearer %s" % self.get_access(),'User-Agent': 'Mozilla/5.5 (Windows NT 6.0; WOW64; rv:.0) Gecko/20100101 Firefox/24.0'},
    #                           json={
    #                               "id": "%s" % self.locust.other_actorId
    #                           },
    #                           catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print(response.content)
    #             response.failure(response.content)
    #
    # # 添加用户为好友
    # @task(2)
    # def friend_user(self):
    #     with self.client.post("/friend/user",
    #                           headers={"Authorization": "Bearer %s" % self.get_access(),'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'},
    #                           json={
    #                               "id": "%s" % self.locust.other_userId
    #                           },
    #                           catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print(response.content)
    #             response.failure(response.content)

    # 设置对单个用户免打扰
    @task(2)
    def user_dnd(self):
        with self.client.post("/friend/dnd",
                              headers={"Authorization": "Bearer %s" % self.get_access(),
                                       'User-Agent': 'Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; Trident/5.0)'},
                              json={
                                  "id": "%s" % self.locust.other_userId
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 获取我的朋友中展商列表
    @task(2)
    def get_friend_actors(self):
        with self.client.get("/friend/actors",
                             headers={"Authorization": "Bearer %s" % self.get_access(),
                                      'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # # 好友列表中删除展商
    # @task(2)
    # def del_friend_actor(self):
    #     with self.client.delete("/friend/actor/%d" % self.locust.other_actorId,
    #                             headers={"Authorization": "Bearer %s" % self.get_access(),'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:9.0) Gecko/20100101 Firefox/24.0'},
    #                             catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print(response.content)
    #             response.failure(response.content)
    #
    # # 好友列表中删除用户
    # @task(2)
    # def del_friend_user(self):
    #     with self.client.delete("/friend/user/%d" % self.locust.other_userId,
    #                             headers={"Authorization": "Bearer %s" % self.get_access(),'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:10.0) Gecko/20100101 Firefox/24.0'},
    #                             catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print(response.content)
    #             response.failure(response.content)

    '''
        经停点
    '''

    # 根据经停点获取展商列表
    @task(2)
    def transit_point(self):
        with self.client.post("/transitpoint",
                              headers={"Authorization": "Bearer %s" % self.get_access(),
                                       'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'},
                              json={
                                  "actorIds": ["10001", "10002"]
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 获取感兴趣的展商列表
    @task(2)
    def interested_actors(self):
        with self.client.get("/interestedactors",
                             headers={"Authorization": "Bearer %s" % self.get_access(),
                                      'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920)'},
                             json={
                                 "actorIds": ["10001", "10002"]
                             },
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    '''
        系统推荐
    '''

    # 获取推荐的展商
    @task(2)
    def recommend_actors(self):
        with self.client.get("/recommendactors",
                             headers={"Authorization": "Bearer %s" % self.get_access(),
                                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0'},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 获取推荐的用户
    @task(2)
    def recommend_users(self):
        with self.client.get("/recommendusers",
                             headers={"Authorization": "Bearer %s" % self.get_access(),
                                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # # 获取推荐的消息
    # @task(2)
    # def delete_recommend(self):
    #     with self.client.delete("/deleterecommend/1",
    #                             headers={"Authorization": "Bearer %s" % self.get_access(),'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'},
    #                             catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print(response.content)
    #             response.failure(response.content)

    '''
        标签
    '''

    # 获取所有标签
    @task(2)
    def get_tags(self):
        with self.client.get("/tags",
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 添加自己的标签
    @task(2)
    def post_user_tags(self):
        with self.client.post("/user/tags",
                              headers={"Authorization": "Bearer %s" % self.get_access(), "X-Client": "User"},
                              json={
                                  "codes": ["91", "92"]
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 获取自己的标签
    @task(2)
    def get_user_tags(self):
        with self.client.get("/user/tags",
                             headers={"Authorization": "Bearer %s" % self.get_access(), "X-Client": "User"},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 获取别人的标签
    @task(2)
    def other_user_tags(self):
        with self.client.get("/user/%s/tags" % self.locust.other_userId,
                             headers={"Authorization": "Bearer %s" % self.get_access(),
                                      'User-Agent': 'Mozilla/4.4 (Windows NT 6.0; WOW64; rv:22.0) Gecko/20100101 Firefox/24.0'},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 获取某个标签下的所有用户
    @task(2)
    def tag_code_users(self):
        with self.client.get("/tag/%s/users" % self.locust.tagCode,
                             headers={"Authorization": "Bearer %s" % self.get_access(),
                                      'User-Agent': 'Mozilla/4.5 (Windows NT 6.0; WOW64; rv:23.0) Gecko/20100101 Firefox/24.0'},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    '''
        位置模块
    '''

    # 上传用户位置信息
    @task(2)
    def post_user_location(self):
        with self.client.post("/userlocation",
                              headers={"Authorization": "Bearer %s" % self.get_access(),
                                       'User-Agent': 'Mozilla/4.6 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'},
                              json={
                                  "sceneId": "%s" % self.locust.sceneId,
                                  "location": {
                                      "position": {
                                          "lat": 31.26560817367096,
                                          "lon": 120.73635511100292
                                      }
                                  }
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)


                # 用户提交问题

    @task(2)
    def answers(self):
        with self.client.post("/answers",
                              headers={"Authorization": "Bearer %s" % self.get_access(),
                                       'User-Agent': 'Mozilla/4.9 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/30.0'},
                              json={
                                  "selectionId": self.locust.selectionId
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 一次性提交所有答案
    @task(2)
    def answers_compact(self):
        with self.client.post("/answers/_compact",
                              headers={"Authorization": "Bearer %s" % self.get_access(),
                                       'User-Agent': 'Mozilla/3.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/31.0'},
                              json=[
                                  {
                                      "selectionId": 1,
                                      "body": "hello"
                                  },
                                  {
                                      "selectionId": 7,
                                      "body": ""
                                  }
                              ],
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    '''
        搜索
    '''

    # 根据关键字搜索
    @task(2)
    def search(self):
        with self.client.post("/search",
                              headers={"Authorization": "Bearer %s" % self.get_access(),
                                       'User-Agent': 'Mozilla/3.1 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/32.0'},
                              json={
                                  "keywords": "苏州",
                                  "tagCode": "hpt"
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 搜索附近的人
    @task(2)
    def search(self):
        with self.client.post("/poi/_nearby",
                              headers={"Authorization": "Bearer %s" % self.get_access(),
                                       'User-Agent': 'Mozilla/3.2 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/33.0'},
                              json={
                                  "position": {
                                      "lat": 31.265618490699733,
                                      "lon": 120.7364271953702
                                  },
                                  "radius": 100.0
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)

    # 获取PoiUser
    @task(2)
    def search(self):
        with self.client.get("/poi/user/%s" % self.locust.userId,
                             headers={"Authorization": "Bearer %s" % self.get_access(),
                                      'User-Agent': 'Mozilla/3.4 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/36.0'},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code != 0:
                print(response.status_code)
                print(response.content)
                response.failure(response.content)


class User(HttpLocust):
    # host = 'http://apiv1.touchair.cn'
    hostBase = 'http://192.168.1.57:9000'
    header = {"Authorization": "Basic ZDBmNzg1ZWE1N2IzNDFhM2ExMTRiZWIxNmNlZjFiOTc6bnVsbA==", "X-Client": "User"}
    sceneId = '09aba2a9-3245-405a-92c4-d6695a1b24b1'
    # mobile = str(random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
    #     random.choice("0123456789") for i in range(8)))
    i = 0
    # accessToken_queue = queue.Queue()

    accessTokens = []

    for index in range(2000):
        # mobile = str(random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
        #     random.choice("0123456789") for i in range(8)))

        mobile_end = 10000000 + index
        mobile = "138" + str(mobile_end)
        # 手机号密码登录

        response = requests.post("%s/token/_verifyMobile" % hostBase,
                                 headers=header,
                                 data={"mobile": mobile, "smscode": "123456"})

        if response.status_code == 200 or response.status_code == 201:
            content = json.loads(response.content.decode("utf-8"))
            data = {
                "accessToken": content["accessToken"],
                "refreshToken": content["refreshToken"],
            }
            # i = i + 1
            # print(data["accessToken"])
            # print(i)
            # accessToken_queue.put_nowait(data)
            accessTokens.append(content["accessToken"])
        else:
            print(response.status_code)
            print(response.content.decode("utf-8"))

    print(len(accessTokens))
    print(random.randint(0, 2000))
    # print(resource.getrlimit(resource.RLIMIT_NOFILE))
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
