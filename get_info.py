# -*- coding: utf-8 -*-

"""
@Auth:                  jackie.yuan
@Email:                 13772002022@163.com
@Description:           get godaddy's domains infomation
"""

import json,time
from datetime import datetime
from godaddypy import Client, Account


# 填写用户名称
admin = "xxx"+"'s domain info"

# 存储文件路径
set_path = "xxx"

# 获取认证，需要的是api的key和对应的secret
my_acct = Account(api_key='xxx', api_secret='xxx')
client = Client(my_acct)

# ----------------------------- 当代码已经完美运行之后，只需要修改上面带x的部分就好了

# 获取账户的域的信息(默认100 个，即少于100时直接用这个)
# Domains = client.get_domains()

# 获取账户的域的信息（limit为需要的数量，或者为用户域的数量，官方规定为0-1000）
Domains = client.get_domains_withlimit(1000) #需要添加
# 因为这个库不提供带修改限制的方法，所以要在库函数client.py中添加这个方法：
"""
    def get_domains_withlimit(self, limit):
    # Returns a list of domains for the authenticated user. add limit
    
        url = self.API_TEMPLATE + self.DOMAINS + u'?limit={}'.format(limit)
        data = self._get_json_from_response(url)

        domains = list()
        for item in data:
            domain = item['domain']
            domains.append(domain)
            self.logger.debug('Discovered domains: {}'.format(domain))
    return domains
"""


# 存放指定域名要求获取的对应信息
def Specified_info(i):
    domain_info = client.get_domain_info(i)
    # expires_date = domain_info["expires"]
    if client.get_domain_info(i).has_key("expires"):
        expires_date = datetime.strptime(domain_info["expires"],"%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")
    else:
        expires_date = "None"
    if  client.get_domain_info(i).has_key("contactRegistrant"):
        organization = client.get_domain_info(i)["contactRegistrant"]["organization"]
    else:
        organization = "None"
    # organization = domain_info["contactRegistrant"]["organization"]
    Auto_renew = domain_info["renewAuto"]

    try:
        datetime.strptime(domain_info["createdAt"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")
    except  ValueError:
        create_date = datetime.strptime(domain_info["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y/%m/%d")
    else:
        create_date = datetime.strptime(domain_info["createdAt"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")
    STATUS = domain_info["status"]

    return expires_date, organization, Auto_renew, create_date, STATUS


# 写入属性
with open(set_path, "a+") as f:
    f.write("\n" + admin + "\n")
    f.writelines(" domain , expires , organization , Auto-Renew , create_date , status\n") #用逗号分隔是为了可以直接存储在excel中。


# 对应每一个域名的信息分别存储
for i in Domains:
    if i == "bigtrafficgenerator.info": continue
    # Domain_Info_Specified = json.dumps(client.get_domain_info(i))
    # Domain_Info_Specified = client.get_domain_info(i)
    expires_date, organization, Auto_renew, create_date, STATUS = Specified_info(i)
    with open(set_path, "a+") as f:
        f.write(i+",")
        # f.writelines(Domain_Info_Specified + "\n")
        # f.write("到期日 : ")
        json.dump(expires_date, f)
        f.write(",")
        # f.write("所属公司 : ")
        json.dump(organization, f)
        f.write(",")
        # f.write("Auto-Renew : ")
        json.dump(Auto_renew, f)
        f.write(",")
        # f.write("分配时间 : ")
        json.dump(create_date, f)
        f.write(",")
        json.dump(STATUS, f)
        f.write(",\n")
        f.flush()
        print "get domain {} info success...".format(i)
    time.sleep(0.5)                             # 这个非常重要！！ 不然客户端有可能会识别为类似DDOS攻击，时间自己把控
with open(set_path, "a+") as f:
    f.write("\n")

print "get all {} finished  ! ".format(admin)






if __name__ == "__main__":
    pass

