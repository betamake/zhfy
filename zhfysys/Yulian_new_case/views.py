import  os
import sys
from django.shortcuts import render,HttpResponse
from . import models
import json
import pymongo
from bson.objectid import ObjectId
import datetime
sys.path.append(os.path.realpath('.'))
from zhfysys import settings
# Create your views here.
"""连接mongodb"""
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client.testDb
my_collection = my_db.testJson
def get_base_massage(request):
    """存储案件基本信息并且返回id"""
    data_dict = {}
    response={}
    count = my_collection.find().count()
    count +=1
    index = str(count)
    date_time =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace("-","")[0:8] #格式化时间
    anhao = date_time+" "+"民演"+"("+str(count)+")"+"号"#拼接案号
    data_dict["_id"] = index
    if request.method =='POST':
        print(request.body)
        received_json_data = json.loads(request.body)  # 把json转为字典
        type_of_anJian = received_json_data['base_infomation']
        username = received_json_data['username']
        data_dict["username"] = username
        type_of_anJian = type_of_anJian['type_of_anJian']
        data_dict.setdefault("base_infomation", {}).update({"type_of_anJian": type_of_anJian})
        #插入
        try:
            id = str(my_collection.insert(data_dict))
            response["id"] = index
            response["code"] = "0"
            response["anhao"] = anhao
        except:
            response["id"] = "0"
            response["code"] = "1"
            response["anhao"] = "0"
        response = json.dumps(response)
    return HttpResponse(response)


def get_ms_t_msys(request):
    """民事一审案件主表"""
    data_dict = {}
    t_msys = {}
    response={}
    if request.method =='POST':
        received_json_data = json.loads(request.body)  # 把json转为字典
        id = str(received_json_data['id'] ) # ID
        print(id)
        # id_received = ObjectId("{}".format(id))
        #获取json数据。
        ms = received_json_data["ms"]
        t_msys = ms["t_msys"]
        t_msysdsrhzysar = ms["t_msysdsrhzysar"]
        t_msysdsrlxfs = ms["t_msysdsrlxfs"]
        t_msysdsrsddz = ms["t_msysdsrsddz"]
        t_msysdsrxx = ms["t_msysdsrxx"]
        t_msysfddlrxx = ms["t_msysfddlrxx"]
        t_msyslsjbxx = ms["t_msyslsjbxx"]
        t_msyssdxx = ms["t_msyssdxx"]
        t_msyswbwj = ms["t_msyswbwj"]
        t_msyszjxx = ms["t_msyszjxx"]

        #定义需要更新的查询条件
        id_query = {"_id":id}
        print(id_query)
        find_resulit  = my_collection.find_one(id_query)
        print(find_resulit)
        #拼接插入数据
        data_dict.setdefault("ms",{}).update({"t_msys":t_msys})
        data_dict.setdefault("ms", {}).update({"t_msysdsrhzysar": t_msysdsrhzysar})
        data_dict.setdefault("ms", {}).update({"t_msysdsrlxfs": t_msysdsrlxfs})
        data_dict.setdefault("ms", {}).update({"t_msysdsrsddz": t_msysdsrsddz})
        data_dict.setdefault("ms", {}).update({"t_msysdsrxx": t_msysdsrxx})
        data_dict.setdefault("ms", {}).update({"t_msysfddlrxx": t_msysfddlrxx})
        data_dict.setdefault("ms", {}).update({"t_msyslsjbxx": t_msyslsjbxx})
        data_dict.setdefault("ms", {}).update({"t_msyssdxx": t_msyssdxx})
        data_dict.setdefault("ms", {}).update({"t_msyswbwj": t_msyswbwj})
        data_dict.setdefault("ms", {}).update({"t_msyszjxx": t_msyszjxx})
        update = my_collection.update_one(id_query,{"$set":data_dict})
        #判断是否插入成功
        print(data_dict)
        if update.modified_count != 0:
            response["id"] = id
            response['code'] = "0"
        else:
            response["id"] = "0"
            response["code"] = "1"
        response = json.dumps(response)
    return HttpResponse(response)
def upload(request):
    """
    上传文件
    :param request: 请求
    :return: 文件上传结果
    """
    if request.method == "POST":
        object = request.FILES.get("file")
        try:
            file = open(os.path.join(settings.MEDIA_ROOT,"upload",object.name),"wb")
            for chunk in object.chunks():
                file.write(chunk)
            file.close()
            result = {"file_data_uploaded":"yes","filename":object.name,"media_root":os.path.join(settings.MEDIA_ROOT,"upload")}
        except:
            result = {"file_data_uploaded": "no", "filename": "0",
                      "media_root": "0"}
    return HttpResponse(json.dumps(result))