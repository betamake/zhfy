import pymongo
from bson.objectid import ObjectId
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client.testDb
collection = my_db.testJson

json = {
        # "_id":"e00803ec-1be3-11ea-894f-c7a24e790205",
        "base_infomation":{
            "type_of_anJian":"案件类型"
        },
        "ms":{
            "t_msys": {
                      "c_ajmc":"案件名称",
                      "n_jbfy":"经办法院",
                      "c_baah":"本案案号",
                      "c_qsay":"起诉案由",
                      "n_bdse":"标的数额",
                      "c_laay":"立案案由",
                      "n_sycx":"适用程序",
                      "c_jaay":"结案案由",
                      "n_jabdje":"结案标的金额"
                  },
            "t_msysdsrhzysar":{
                    "n_xh":"序号",
                    "n_lx":"类型",
                    "c_shtyxydm":"社会统一信用代码",
                    "n_dsrjzysarlx":"当事人及主要涉案人类型",
                    "n_dlrlx":"代理人类型",
                    "n_bhrlx":"辩护人类型",
                    "c_xm":"姓名",
                    "c_bm":"别名",
                    "c_zym":"曾用名",
                    "c_gbhdq":"国别或地区",
                    "n_sfzjlx":"身份证件类型",
                    "c_qtsfzjmc":"其他身份证件名称",
                    "c_sfzhm":"身份证号码",
                    "c_qtsfzjhm":"其他身份证件号码",
                    "c_lxfsnr":	"联系方式内容",
                    "c_zdqsr":"指定签收人",
                    "c_qrsddz":"确认送达地址",
                    "n_xb":"性别",
                    "d_csrq":"出生日期",
                    "n_zasnl":"年龄_作案时",
                    "n_spsnl":"年龄_审判时",
                    "n_mz":"民族",
                    "n_zzmm":"政治面貌",
                    "n_xwnlzk":"行为能力状况",
                    "n_xszrnl":"刑事责任能力",
                    "n_hyzk":"婚姻状况",
                    "n_hjszd":"户籍所在地",
                    "n_jcjzd":"经常居住地",
                    "c_xzz":"现住址",
                    "n_whcd":"文化程度",
                    "n_sf":"身份",
                    "n_jx":"军衔",
                    "n_jghwzgbjb":"军官或文职干部级别",
                    "n_tsslhbl":"特殊生理或病理",
                    "n_ldry":"流动人员",
                    "n_jtcf":"家庭成分",
                    "n_gzdwlx":"工作单位类型",
                    "n_jglx":"机关类型",
                    "n_sfzygjjg":"是否中央国家机关",
                    "c_gzdwmc":"工作单位名称",
                    "c_zw":"职务",
                    "n_zj":"职级",
                    "n_sfrddb":"是否人大代表",
                    "n_sfzxwy":"是否政协委员",
                    "c_rdzxcj":"人大_政协层级",
                    "n_zwcj":"职务层级",
                    "n_sfsq":"是否涉侨",
                    "n_sqlx":"涉侨类型",
                    "c_sqgbhdq":"涉侨国别或地区",
                    "c_dwmc":"单位名称",
                    "n_dwlx":"单位类型",
                    "n_sffrdw":"是否法人单位",
                    "n_zzlx":"证照类型",
                    "c_zzhm":"证照号码",
                    "n_dwzt":"单位状态",
                    "n_zcdjdgbhdq":"注册登记地国别或地区",
                    "c_zcdjd":"注册登记地",
                    "c_zybsjgszd":"主要办事机构所在地",
                    "c_fddbr":"法定代表人"
            },
            "t_msysdsrlxfs":{
                "c_stm_msys":"案件实体码",
                "n_xh":"序号",
                "n_xh_dsrjzysarbs":"当事人及主要涉案人标识",
                "n_lxfslx":"联系方式类型",
                "c_lxfsnr":"联系方式内容"
            },
            "t_msysdsrsddz":{
                "c_stm_msys":"案件实体码",
                "n_xh":"序号",
                "n_xh_dsrjzysarbs":"当事人及主要涉案人标识",
                "c_zdqsr":"指定签收人",
                "c_qrsddz":"确认送达地址"
            },
            "t_msysdsrxx":{
                "c_stm_msys":"案件实体码",
                "n_xh":"序号",
                "n_dsrbs":"当事人标识",
                "c_dsrajdw":"当事人案件地位",
                "n_dsrlx":"第三人类型"
            },
            "t_msysfddlrxx":{
                "c_stm_msys":"案件实体码",
                "n_xh":"序号",
                "n_dsrbs":"当事人标识",
                "n_fddlrbs":"法定代理人标识",
                "n_ydsrgx":"与当事人关系"
            },
            "t_msyslsjbxx":{
                "c_stm_msys":"案件实体码",
                "n_xh":"序号",
                "n_xh_dsrjzysarbs":"当事人及主要涉案人标识",
                "c_lsxm":"律师姓名",
                "c_lsmc":"律所名称",
                "c_lszcd":"律所注册地",
                "n_sfflyz":"是否法律援助",
                "c_lszyzgzh":"律师执业资格证号"
            },
            "t_msyssdxx":{
                "c_ssdr":"受送达人",
                "n_sdfs":"送达方式",
                "d_zjsdrq":"直接送达日期",
                "d_qsyjrq":"签收邮件日期",
                "d_dzsdrq":"电子送达日期"

            },
            "t_msyswbwj":{
                "c_stm_msys":"案件实体码",
                "n_xh":"序号",
                "n_stlb":"实体类别",
                "n_stbh":"实体编号",
                "c_xsmc":"显示名称",
                "c_wjmc":"文件名称",
                "n_wjdx":"文件大小",
                "c_wjdz":"文件地址",
                "c_md5":"MD5",
                "n_cjrbs":"创建人标识",
                "d_cjsj":"创建时间",
                "n_zjxgrbs":"最近修改人标识",
                "d_zjxgsj":"最近修改时间",
                "c_tjr":"提交人",
                "n_sfdsrtj":"是否当事人提交",
                "d_tjrq":"提交日期",
                "d_jsrq":"接收日期",
                "c_jsr":"接收人",
                "c_bz":"备注"
            },
            "t_msyszjxx":{
                "c_stm":"主键实体码",
                "c_stm_msys":"案件实体码",
                "n_xh":"序号",
                "c_zjmc":"证据名称"
            }
        }
}
base_infomation = {
    # "_id":"e754f1ea-1be4-11ea-894f-c7a24e790205",
	"base_infomation":{
		"type_of_anJian":"testtest"
	}
}
t_msys = {"ms":{
	        "t_msys": {
              "c_ajmc":"123",
              "n_jbfy":"经办法院",
              "c_baah":"本案案号",
              "c_qsay":"起诉案由",
              "n_bdse":"标的数额",
              "c_laay":"立案案由",
              "n_sycx":"适用程序",
              "c_jaay":"结案案由",
              "n_jabdje":"结案标的金额"
          }
        }
}
data_dict ={'ms':
                {'t_msys':
                     {'c_ajmc': '123',
                      'n_jbfy': '123',
                      'c_baah': '123',
                      'c_qsay': '123',
                      'n_bdse': '123',
                      'c_laay': '立案案由',
                      'n_sycx': '适用程序',
                      'c_jaay': '结案案由',
                      'n_jabdje': '结案标的金额'
                      }
                 }
            }
data_dict_test = {'ms': {'t_msys': {'c_ajmc': '123', 'n_jbfy': '经办法院', 'c_baah': '本案案号', 'c_qsay': '起诉案由', 'n_bdse': '标的数额', 'c_laay': '立案案由', 'n_sycx': '适用程序', 'c_jaay': '结案案由', 'n_jabdje': '结案标的金额'}, 't_msysdsrhzysar': {'n_xh': '序号', 'n_lx': '类型', 'c_shtyxydm': '社会统一信用代码', 'n_dsrjzysarlx': '当事人及主要涉案人类型', 'n_dlrlx': '代理人类型', 'n_bhrlx': '辩护人类型', 'c_xm': '姓名', 'c_bm': '别名', 'c_zym': '曾用名', 'c_gbhdq': '国别或地区', 'n_sfzjlx': '身份证件类型', 'c_qtsfzjmc': '其他身份证件名称', 'c_sfzhm': '身份证号码', 'c_qtsfzjhm': '其他身份证件号码', 'c_lxfsnr': '联系方式内容', 'c_zdqsr': '指定签收人', 'c_qrsddz': '确认送达地址', 'n_xb': '性别', 'd_csrq': '出生日期', 'n_zasnl': '年龄_作案时', 'n_spsnl': '年龄_审判时', 'n_mz': '民族', 'n_zzmm': '政治面貌', 'n_xwnlzk': '行为能力状况', 'n_xszrnl': '刑事责任能力', 'n_hyzk': '婚姻状况', 'n_hjszd': '户籍所在地', 'n_jcjzd': '经常居住地', 'c_xzz': '现住址', 'n_whcd': '文化程度', 'n_sf': '身份', 'n_jx': '军衔', 'n_jghwzgbjb': '军官或文职干部级别', 'n_tsslhbl': '特殊生理或病理', 'n_ldry': '流动人员', 'n_jtcf': '家庭成分', 'n_gzdwlx': '工作单位类型', 'n_jglx': '机关类型', 'n_sfzygjjg': '是否中央国家机关', 'c_gzdwmc': '工作单位名 称', 'c_zw': '职务', 'n_zj': '职级', 'n_sfrddb': '是否人大代表', 'n_sfzxwy': '是否政协委员', 'c_rdzxcj': '人大_政协层级', 'n_zwcj': '职务层级', 'n_sfsq': '是否涉侨', 'n_sqlx': '涉侨类型', 'c_sqgbhdq': '涉侨国别或地区', 'c_dwmc': '单位名称', 'n_dwlx': '单位类型', 'n_sffrdw': '是否法人单位', 'n_zzlx': '证照类型', 'c_zzhm': '证照号码', 'n_dwzt': '单位状态', 'n_zcdjdgbhdq': '注册登记地国别或地区', 'c_zcdjd': '注册登记地', 'c_zybsjgszd': '主要办事机构所在地', 'c_fddbr': '法定代表人'}, 't_msysdsrlxfs': {'c_stm_msys': '案件实体码', 'n_xh': '序号', 'n_xh_dsrjzysarbs': '当事人及主要涉案人标识', 'n_lxfslx': '联系方式类型', 'c_lxfsnr': '联系方式内容'}, 't_msysdsrsddz': {'c_stm_msys': '案件实体码', 'n_xh': '序号', 'n_xh_dsrjzysarbs': '当事 人及主要涉案人标识', 'c_zdqsr': '指定签收人', 'c_qrsddz': '确认送达地址'}, 't_msysdsrxx': {'c_stm_msys': '案件实体码', 'n_xh': '序号', 'n_dsrbs': '当事人标识', 'c_dsrajdw': '当事人案件地位', 'n_dsrlx': '第三人类型'}, 't_msysfddlrxx': {'c_stm_msys': '案件实体码', 'n_xh': '序号', 'n_dsrbs': '当事人标识', 'n_fddlrbs': '法定代理人标识', 'n_ydsrgx': '与当事人关系'}, 't_msyslsjbxx': {'c_stm_msys': '案件实体码', 'n_xh': '序号', 'n_xh_dsrjzysarbs': '当事人及主要涉案人标识', 'c_lsxm': '律师姓名', 'c_lsmc': '律所名称', 'c_lszcd': '律所注册地', 'n_sfflyz': '是否法律援助', 'c_lszyzgzh': '律师执业资格证号'}, 't_msyssdxx': {'c_ssdr': '受送达人', 'n_sdfs': '送达方式', 'd_zjsdrq': '直接送达日期', 'd_qsyjrq': '签收邮件日期', 'd_dzsdrq': '电子送 达日期'}, 't_msyswbwj': {'c_stm_msys': '案件实体码', 'n_xh': '序号', 'n_stlb': '实体类别', 'n_stbh': '实体编号', 'c_xsmc': '显示名称', 'c_wjmc': '文件名称', 'n_wjdx': '文件大小', 'c_wjdz': '文件地址', 'c_md5': 'MD5', 'n_cjrbs': '创建人标识', 'd_cjsj': '创建时间', 'n_zjxgrbs': '最近修改人标识', 'd_zjxgsj': '最近修改时间', 'c_tjr': '提交人', 'n_sfdsrtj': '是否当事人提交', 'd_tjrq': '提交日期', 'd_jsrq': '接收日期', 'c_jsr': '接收人', 'c_bz': '备注'}, 't_msyszjxx': {'c_stm': '主键实体码', 'c_stm_msys': '案件实体码', 'n_xh': '序号', 'c_zjmc': '证据名称'}}}
# id = collection.insert(json)
id_query = {"_id":"1"}
# data1 = collection.find_one(id_query)
# base_update = {
# 	"base_infomation":{
# 		"type_of_anJian":"base_update"
# 	}
# }
data = collection.update_one(id_query,{"$set":data_dict_test})
count = collection.find().count()
print(data.modified_count)