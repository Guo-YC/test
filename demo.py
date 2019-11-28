import re
import  json
import urllib.request
import requests


url="https://leetcode-cn.com/graphql/"


headers={

    "cookie":"a59vnkjXTMfNWuCc8s9Bc4Dr1ofizQv5DIdgBuidoVyNxOmP8trAWRS52zq0ZPF4",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3739.400 QQBrowser/10.5.3846.400",
    "Request URL": "https://leetcode-cn.com/graphql/",
    "x-csrftoken":"a59vnkjXTMfNWuCc8s9Bc4Dr1ofizQv5DIdgBuidoVyNxOmP8trAWRS52zq0ZPF4",

}
'''
data={

    "Remote Address": "47.99.228.218:443"
                      
                 
    "origin": "https://leetcode-cn.com",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "authority": "leetcode-cn.com",
    "method": "POST",
    "path": "/graphql/",
    "Referrer Policy": "no-referrer-when-downgrade",
    "referer": "https://leetcode-cn.com/problems/longest-palindromic-substring/",
    "operationName": "questionData",
    "query":"query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { questionId questionFrontendId boundTopicId title titleSlug content translatedTitle translatedContent isPaidOnly difficulty likes dislikes isLiked similarQuestions contributors { username profileUrl avatarUrl __typename } langToValidPlayground topicTags { name slug translatedName __typename } companyTagStats codeSnippets { lang langSlug code __typename } stats hints solution { id canSeeDetail __typename } status sampleTestCase metaData judgerAvailable judgeType mysqlSchemas enableRunCode enableTestMode envInfo book { id bookName pressName description bookImgUrl pressImgUrl productUrl __typename } isSubscribed __typename } } ",
    "titleSlug":"longest-palindromic-substring"

}
'''
da={"operationName":"questionData","variables":{"titleSlug":"flip-equivalent-binary-trees"},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    book {\n      id\n      bookName\n      pressName\n      description\n      bookImgUrl\n      pressImgUrl\n      productUrl\n      __typename\n    }\n    isSubscribed\n    __typename\n  }\n}\n"}


#req = urllib.request.Request(url="https://leetcode-cn.com/graphql/", headers=headers)
#data=urllib.request.urlopen(req).read().decode('utf-8')
#print(data)
#rst=urlopen().get("https://leetcode-cn.com/problems/longest-palindromic-substring/",headers=headers)

req = requests.post("https://leetcode-cn.com/graphql/", headers=headers,data=da)
print(str(req))
print(req.text)
#hhh= json.loads(req)
#print(hhh)


'''
'''
strlist = '[1,2,3,4]'#json类型
strDict = '{"city":"长沙","name":"臭豆腐"}'
ptlist=json.loads("https://leetcode-cn.com/graphql/")
#loads 把Json格式字符串解码转换成Python对象
print(ptlist)
'''
'''
liststr= [1,2,3,4]
listDict= {"city":"长沙","name":"臭豆腐"}
pyDict= json.dumps(listDict,ensure_ascii=False)
pylist= json.dumps(liststr)

#dumps()序列化时默认使用ascii 码
print(pyDict)#type=str
print(pylist)

'''










headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url="https://leetcode-cn.com/api/problems/all/", headers=headers)
data=urllib.request.urlopen(req).read().decode('utf-8')
#data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode('utf-8')
fh=open("leetcode_题目.txt","w")
#print(data)
pat='"question__title_slug":"(.*?)"'#贪婪模式！！！
questions= re.compile(pat).findall(data)
print(len(questions))
for i in range(0,len(questions)):
    hhh = "https://leetcode-cn.com/problems/"+str(questions[i])
    print(hhh)
    fh.write(str(questions[i])+"\n")
    
