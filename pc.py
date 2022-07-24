import urllib
import urllib.request
from lxml import etree
import requests

# 请求url
def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    print(html)
    return etree.HTML(html)

# url
def post_task_id():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    url = 'http://www.gdzwfw.gov.cn/portal/api/v2/item-event/getAuditItemDetailCur'
    params = {
        'TASK_CODE': '12440100741854396C3442014055017'
    }
    res = requests.post(url, params=params, headers=headers)
    return res.json()

# 获取信息
def get_task_info(res):
    info = res['AUDIT_ITEM']
    data = {
        'matter_name': info['CATANAME'],
        'matter_AREA_CODE_TEXT': info['AREA_CODE_TEXT']
    }

    return data


print(get_task_info(post_task_id()))
# print(get_task_info(
#
#     get_html('http://www.gdzwfw.gov.cn/portal/api/v2/item-event/getAuditItemDetailCur?TASK_CODE=12440100741854396C3442014055017')
#
# ))
#
