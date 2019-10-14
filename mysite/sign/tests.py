from django.test import TestCase
from django.contrib.auth.models import User
from sign.models import Event, Guest

# Create your tests here.
"""
django测试不会在数据库中写入数据，也不会从数据库中读取数据
"""
#测试模型model
class EventTestcase(TestCase):
    def setUp(self):
        Event.objects.create(name="华为P20发布会", limit="300", status=True, address="深圳",start_time="2019-12-12 09:00:00")

    def test_select(self):
        event = Event.objects.get(name="华为P20发布会")
        self.assertEqual(event.address,"深圳")

    def test_update(self):
        event = Event.objects.get(name="华为P20发布会")
        event.address = "上海"
        event.save()
        event = Event.objects.get(name="华为P20发布会")
        self.assertEqual(event.address,"上海")

    def test_delete(self):
        event = Event.objects.get(name="华为P20发布会")
        event.delete()
        event = Event.objects.filter(name="华为P20发布会")
        self.assertEqual(len(event), 0)

    def test_add(self):
        Event.objects.create(name="小米8发布会", limit="500", status=True, address="深圳",start_time="2020-12-12 09:00:00")
        event = Event.objects.get(name="小米8发布会")
        self.assertEqual(event.address,"深圳")

#测试视图
class IndexViewTest(TestCase):

    def test_Index(self):
        response = self.client.get("/sign/index")
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "index.html")


class LoginViewTest(TestCase):

    def setUp(self):
        #调用django自己的数据库，创建用户
        User.objects.create_user("admin", "fang@mail.com", "123456")


    def test_login_isnull(self):
        user = {"username":"", "password":""}
        response = self.client.post("/sign/login",user)
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "login.html")
        #断言页面提示是否正确
        self.assertIn(b"username or pasword miss",response.content)

    def test_login_isincorrect(self):
        user = {"username":"qqq", "password":"123"}
        response = self.client.post("/sign/login",user)
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "login.html")
        self.assertIn(b"username or password incorrect",response.content)

    def test_login_success(self):
        user = {"username":"admin", "password":"123456"}
        response = self.client.post("/sign/login",user)
        print(response.status_code)
        self.assertEqual(response.status_code,302)#登录成功后重定向302


class ManageViewTest(TestCase):

    def setUp(self):
        Event.objects.create(name="华为P20发布会", limit="300", status=True, address="深圳",start_time="2019-12-12 09:00:00")

        #调用django自己的数据库，创建用户
        User.objects.create_user("admin", "fang@mail.com", "123456")
        user = {"username":"admin", "password":"123456"}
        response = self.client.post("/sign/login",user)

    def test_manage_page(self):

        response = self.client.get("/sign/manage")
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "manage.html")
        #断言页面提示是否正确
        self.assertIn(b"P20",response.content)




#测试html页面，通过selenium实现
