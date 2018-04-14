# -*- coding: UTF-8 -*-
from locust import HttpLocust, TaskSet, task
import json
import random


class UserTask(TaskSet):
    # 用户名密码登录
    def on_start(self):
        with self.client.post("/token/_verifyMobile",
                              headers=self.locust.header,
                              data={"mobile": self.locust.mobile, "smscode": "123"}, catch_response=True) as response:
            print response.json()
            print response.status_code
            if response.status_code == 200 or response.status_code == 201:
                response.success()
                content = json.loads(response.content)
                self.locust.accessToken = content["accessToken"]
                self.locust.refreshToken = content["refreshToken"]
            else:
                response.failure(response.content)

    '''
        登录模块
    '''

    # # 获取验证码
    # @task
    # def verify_code(self):
    #     with self.client.get("/sms/verifycode?mobile=%s" % self.locust.mobile, headers=self.locust.header,
    #                          catch_response=True, ) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)

    # # 退出登录
    # @task
    # def delete_token(self):
    #     with self.client.delete("/token", headers={"Authorization": "Bearer %s" % self.locust.accessToken},
    #                             catch_response=True, ) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)

    # # 微信登录
    # @task
    # def verify_wechat(self):
    #     with self.client.post("/token/_verifyWechat",
    #                           headers=self.locust.header,
    #                           data={"openId": self.locust.openId}, catch_response=True, ) as response:
    #         if response.status_code == 200:
    #             content = json.loads(response.content)
    #             self.locust.accessToken = content["accessToken"]
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)
    #
    # # 刷新token
    # @task
    # def refresh_token(self):
    #     with self.client.post("/refreshtoken",
    #                           headers=self.locust.header,
    #                           data={"refreshToken": self.locust.refreshToken}, catch_response=True, ) as response:
    #         if response.status_code == 200:
    #             content = json.loads(response.content)
    #             self.locust.accessToken = content["accessToken"]
    #             self.locust.refreshToken = content["refreshToken"]
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)

    '''
        用户信息
    '''

    # 获取用户信息
    @task(2)
    def user_profile(self):
        with self.client.get("/user/profile",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取别人信息
    @task(2)
    def other_user_profile(self):
        with self.client.get("/users/%s/profile" % self.locust.userId,
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 更新用户信息
    @task(2)
    def update_user_profile(self):
        with self.client.post("/user/profile",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                              json={
                                  "city": "三明",
                                  "company": "苏州触达",
                                  "country": "中国",
                                  "department": "软件部门"
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # # 绑定微信号
    # @task(2)
    # def bind_wechat(self):
    #     with self.client.post("/user/profile/wechat",
    #                           headers={"Authorization": "Bearer %s" % self.locust.accessToken},
    #                           json={
    #                               "openId": "xinghai"
    #                           },
    #                           catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)

    # 绑定设备号
    @task(2)
    def bind_device(self):
        with self.client.post("/device",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                              json={
                                  "id": "8C8D885C-2577-4467-9780-E643118801B0",
                                  "model": "meizu"
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    '''
        我的朋友
    '''

    # # 添加展商为好友
    # @task(2)
    # def friend_actor(self):
    #     with self.client.post("/friend/actor",
    #                           headers={"Authorization": "Bearer %s" % self.locust.accessToken},
    #                           json={
    #                               "id": "%s" % self.locust.other_actorId
    #                           },
    #                           catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)
    #
    # # 添加用户为好友
    # @task(2)
    # def friend_user(self):
    #     with self.client.post("/friend/user",
    #                           headers={"Authorization": "Bearer %s" % self.locust.accessToken},
    #                           json={
    #                               "id": "%s" % self.locust.other_userId
    #                           },
    #                           catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)

    # 设置对单个用户免打扰
    @task(2)
    def user_dnd(self):
        with self.client.put("/friend/user/dnd",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             json={
                                 "userId": "%s" % self.locust.other_userId,
                                 "state": True
                             },
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取我的朋友中展商列表
    @task(2)
    def get_friend_actors(self):
        with self.client.get("/friend/actors",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取我的朋友中用户列表
    @task(2)
    def get_friend_users(self):
        with self.client.get("/friend/users",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # # 好友列表中删除展商
    # @task(2)
    # def del_friend_actor(self):
    #     with self.client.delete("/friend/actor/%d" % self.locust.other_actorId,
    #                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
    #                             catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)
    #
    # # 好友列表中删除用户
    # @task(2)
    # def del_friend_user(self):
    #     with self.client.delete("/friend/user/%d" % self.locust.other_userId,
    #                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
    #                             catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)

    '''
        经停点
    '''

    # 根据经停点获取展商列表
    @task(2)
    def transit_point(self):
        with self.client.post("/transitpoint",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                              json={
                                  "actorIds": ["10001", "10002"]
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取感兴趣的展商列表
    @task(2)
    def interested_actors(self):
        with self.client.get("/interestedactors",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             json={
                                 "actorIds": ["10001", "10002"]
                             },
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 根据经停点获取展商列表
    @task(2)
    def interested_actor_ids(self):
        with self.client.get("/interestedactorids",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    '''
        系统推荐
    '''

    # 获取推荐的展商
    @task(2)
    def recommend_actors(self):
        with self.client.get("/recommendactors",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取推荐的展品
    @task(2)
    def recommend_products(self):
        with self.client.get("/recommendproducts",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取推荐的用户
    @task(2)
    def recommend_users(self):
        with self.client.get("/recommendusers",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # # 获取推荐的消息
    # @task(2)
    # def delete_recommend(self):
    #     with self.client.delete("/deleterecommend/1",
    #                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
    #                             catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)

    # 获取推荐的消息
    @task(2)
    def system_notices(self):
        with self.client.get("/systemnotices",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

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
            else:
                print response.content
                response.failure(response.content)

    # 添加自己的标签
    @task(2)
    def post_user_tags(self):
        with self.client.post("/user/tags",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken, "X-Client": "User"},
                              json={
                                  "codes": ["91", "92"]
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取自己的标签
    @task(2)
    def get_user_tags(self):
        with self.client.get("/user/tags",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken, "X-Client": "User"},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取别人的标签
    @task(2)
    def other_user_tags(self):
        with self.client.get("/user/%s/tags" % self.locust.other_userId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取某个标签下的所有用户
    @task(2)
    def tag_code_users(self):
        with self.client.get("/tag/%s/users" % self.locust.tagCode,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    '''
        位置模块
    '''

    # 上传用户位置信息
    @task(2)
    def post_user_location(self):
        with self.client.post("/userlocation",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken},
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
            else:
                print response.content
                response.failure(response.content)

    # 获取用户位置
    @task(2)
    def poi_user_location(self):
        with self.client.get("/poi/user/%s" % self.locust.other_userId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取用户去过的展商
    @task(2)
    def users_actors(self):
        with self.client.get("/users/%s/actors" % self.locust.other_userId,
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 到过我展台的所有观众
    @task(2)
    def stayed_users(self):
        with self.client.get("/actor/%s/stayedusers" % self.locust.atrId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取某个标签下的所有用户
    @task(2)
    def current_stayed_users(self):
        with self.client.get("/actor/%s/currentstayedusers" % self.locust.atrId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 此时展馆内所有观众
    @task(2)
    def scene_users(self):
        with self.client.get("/sceneusers/%s" % self.locust.externalId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    '''
        问卷调查
    '''

    # 获取问卷
    @task(2)
    def questionnaires(self):
        with self.client.get("/questionnaires",
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()

            else:
                print response.content
                response.failure(response.content)

    # 获取单个问卷的问题
    @task(2)
    def questionnaire_questions(self):
        with self.client.get("/questionnaire/%d/questions" % self.locust.questionnaireId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取单个题目的回答
    @task(2)
    def question_selections(self):
        with self.client.get("/question/%d/selections" % self.locust.questionId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 一次性返回所有数据
    @task(2)
    def questionnaire_compact(self):
        with self.client.get("/questionnaire/%d/_compact" % self.locust.questionnaireId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 用户提交问题
    @task(2)
    def answers(self):
        with self.client.post("/answers",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                              json={
                                  "selectionId": self.locust.selectionId
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 一次性提交所有答案
    @task(2)
    def answers_compact(self):
        with self.client.post("/answers/_compact",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken},
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
            else:
                print response.content
                response.failure(response.content)

    '''
        搜索
    '''

    # 根据关键字搜索
    @task(2)
    def search(self):
        with self.client.post("/search",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                              json={
                                  "keywords": "苏州",
                                  "tagCode": "hpt"
                              },
                              catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 搜索附近的人
    @task(2)
    def search(self):
        with self.client.post("/poi/_nearby",
                              headers={"Authorization": "Bearer %s" % self.locust.accessToken},
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
            else:
                print response.content
                response.failure(response.content)

    # 获取PoiActor
    @task(2)
    def search(self):
        with self.client.get("/poi/actor/%s" % self.locust.actorId,
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取PoiUser
    @task(2)
    def search(self):
        with self.client.get("/poi/user/%s" % self.locust.userId,
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    '''
        参展报告
    '''

    # 获取参展报告文字内容
    @task(2)
    def user_trace_report(self):
        with self.client.get("/usertracereport",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取参展报告图片
    @task(2)
    def user_trace_report_image(self):
        with self.client.get("/usertracereportimage",
                             headers={"Authorization": "Bearer %s" % self.locust.accessToken},
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    '''
        聊天图片
    '''

    '''
        其他
    '''

    # 获取区域卫星坐标信息
    @task(2)
    def get_consts(self):
        with self.client.get("/consts/%s" % self.locust.zoneId,
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 获取app的初始化配置
    @task(2)
    def app_config(self):
        with self.client.get("/appconfig",
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # 热词
    @task(2)
    def hot_words(self):
        with self.client.get("/hotwords",
                             headers=self.locust.header,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                print response.content
                response.failure(response.content)

    # # 根据蓝牙获取信息
    # @task(2)
    # def location_by_blue(self):
    #     with self.client.get("/locationbyblue/2",
    #                          headers={"Authorization": "Bearer %s" % self.locust.accessToken},
    #                          catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             print response.content
    #             response.failure(response.content)

    '''
        eastFair
    '''


class User(HttpLocust):
    host = 'http://apiv1.touchair.cn'
    header = {"Authorization": "Basic ZDBmNzg1ZWE1N2IzNDFhM2ExMTRiZWIxNmNlZjFiOTc6bnVsbA==", "X-Client": "User"}
    sceneId = '09aba2a9-3245-405a-92c4-d6695a1b24b1'
    mobile = str(random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
        random.choice("0123456789") for i in range(8)))
    openId = "daxinghai"
    externalId = 2
    userId = 1007
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
    max_wait = 3000
