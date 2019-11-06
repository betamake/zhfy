from django.shortcuts import render
from  django.http import  HttpResponse
from . import models
import json
# Create your views here.
#brief:登录视图
def login(request):
    data_dict = {}
    if request.method =='POST':
        received_json_data = json.loads(request.body)#把json转为字典
        username = received_json_data['user_name']
        password = received_json_data['password']
        if username and password:  # 确保用户名和密码都不为空
            # 判断是否存在该数据
            try:
                user = models.User.objects.get(user_name=username)
                print(user)
                #密码是否一致
                if user.password == password:
                    data_dict["is_login_success"] = "yes"
                else:
                    data_dict["is_login_success"] = "no"
            except:
                data_dict["is_login_success"] = "no"
        else:
            data_dict["is_login_success"] = "no"
    else:
        data_dict["is_login_success"] = "no"
    data_json = json.dumps(data_dict)
    return HttpResponse(data_json)
#brief:注册视图
def register(request):
    data_dict = {}
    index = 0  #标志位，判断是否有重复字段，无则写入数据库。
    if request.method == 'POST':
        received_json_data = json.loads(request.body)  # 把json转为字典
        user_name = received_json_data['user_name']
        password = received_json_data['password']
        telephone = received_json_data['telephone']
        email = received_json_data['email']
        real_name = received_json_data['real_name']
        id_card_num = received_json_data['id_card_num']
        try:
            user_name = models.User.objects.get(user_name=user_name)
            data_dict["is_user_name_duplicate"] = 'yes'
        except:
            data_dict["is_user_name_duplicate"] = 'no'
            index+=1
        try:
            telephone = models.User.objects.get(telephone=telephone)
            data_dict["is_telephone_duplicate"] = 'yes'
        except:
            data_dict["is_telephone_duplicate"] = 'no'
            index+=1
        try:
            email = models.User.objects.get(email=email)
            data_dict["is_email_duplicate"] = 'yes'
        except:
            data_dict["is_email_duplicate"] = 'no'
            index+=1
        try:
            id_card_num = models.User.objects.get(id_card_num=id_card_num)
            data_dict["is_id_card_num_duplicate"] = 'yes'
        except:
            data_dict["is_id_card_num_duplicate"] = 'no'
            index += 1
        data_json = json.dumps(data_dict)
        if index == 4:
            user = models.User()
            user.user_name=user_name
            user.password = password
            user.telephone = telephone
            user.email = email
            user.real_name = real_name
            user.id_card_num = id_card_num
            user.save()
            return HttpResponse(data_json)
        return HttpResponse(data_json)
