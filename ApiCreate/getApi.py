#@Author: lokialone
# @Date:   2017-05-08 23:53:30
# @Last Modified by:   lokialone
# @Last Modified time: 2017-06-06 21:11:12
#get api from swapper
#!/usr/bin/python3
 
import requests
import os
from mako.template import Template

SWAGGER_URL = 'http://115.29.10.121:10010/api-docs'
api_all = {}
base = os.path.abspath('.')
os.chdir(base)

def deal_parameters(param):
    res_param = []
    for x in param:
       res_param.append(x['name'])

    if res_param is None or len(res_param) == 0:
        return ''
    else:
        return ','.join(str(d) for d in res_param)


def deal_path(path):
    #路径处理
    arr = path.split('/')
    arr.pop(0)
    count = len(arr)
    filename = deal_filename(arr[count-2])
    apiname = deal_apiname(arr[count-1])
    apipath = deal_apipath(arr)
    filedir = deal_filedir(arr)
    return {'filename': filename, 'apiname': apiname, 'apipath': apipath, 'filedir': filedir}

def deal_filename(name):
    if name.startswith('{'):
        name = name.replace('{', '_').replace('}', '')
    return name + '.js'


def deal_apiname(name):
    return name.replace('{', '_').replace('}', '').replace('.json', '')


def deal_filedir(path):
    arr = path
    arr.pop()
    arr.pop()
    res = []
    for x in arr:
        if x.startswith('{'):
            res.append(x.replace('{', '_').replace('}', ''))
        else:
            res.append(x)
    return '/'.join(res)


def deal_apipath(path):
    res = []
    for x in path:
        if x.startswith('{'):
            res.append('$'+ x)
        else:
            res.append(x)
    return '/'.join(res)

def file_headerString():
    return """import instance from '~api/_instance';\n"""

def template1():
    return """
function ${apiname} (${data}) {
    return instance({
        url: `/${apipath}`,
        method: '${method}',
        params: {${data}}
    });
}
    """


def tempate2():
    return """
function ${apiname} (${data}) {
    return instance({
        url: '/${apipath}',
        method: '${method}',
        params: {${data}}
    });
}
    """

def writeApi(path, method, params):
    res = deal_path(path)
    if not os.path.exists(res['filedir']):
        os.makedirs(res['filedir'])
    filepath = os.path.join(res['filedir'], res['filename'])
    if not os.path.exists(filepath):
        with open(filepath,'w') as f:
            f.write(file_headerString())

    with open(filepath, 'a') as f:
        mytemplate = ''
        if (res['apipath'].find('$') != -1):
            mytemplate = Template(template1())
        else :
            mytemplate = Template(tempate2())
        f.write(mytemplate.render(apiname=res['apiname'], apipath=res['apipath'], method=method, data=params))


def create():
    res_all = requests.get(SWAGGER_URL)
    print(res_all)
    api_all = res_all.json()['apis']
    print(api_all)
    # for x in api_all:
    #     res = requests.get(SWAGGER_URL+'/'+x['path'])
    #     apis = res.json()['apis']
    #     for y in apis:
    #         path = y['path']
    #         params = deal_parameters(y['operations'][0]['parameters'])
    #         method = y['operations'][0]['method']
    #         writeApi(path, method, params)

if __name__ == '__main__':
    create()





