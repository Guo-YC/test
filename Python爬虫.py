import re
import  json
import urllib.request
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url="https://leetcode-cn.com/api/problems/all/", headers=headers)
data=urllib.request.urlopen(req).read().decode('utf-8')
#读取页面数据存入data
fh=open("leetcode_题目.txt","w")
pat='"question__title_slug":"(.*?)"'
#正则表达式 筛选出题目
questions= re.compile(pat).findall(data)
print(len(questions))
for i in range(0,len(questions)):
    hhh = "https://leetcode-cn.com/problems/"+str(questions[i])
    #生成题目链接
    print(hhh)
    fh.write(str(hhh)+"\n")
    #题目链接写入文档

headers = {
    "cookie": "a59vnkjXTMfNWuCc8s9Bc4Dr1ofizQv5DIdgBuidoVyNxOmP8trAWRS52zq0ZPF4",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3739.400 QQBrowser/10.5.3846.400",
    "Request URL": "https://leetcode-cn.com/graphql/",
    "x-csrftoken": "a59vnkjXTMfNWuCc8s9Bc4Dr1ofizQv5DIdgBuidoVyNxOmP8trAWRS52zq0ZPF4",
}
data={
    "Remote Address": "47.99.228.218:443",
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

req = requests.post("https://leetcode-cn.com/problems/longest-palindromic-substring/", headers=headers,data=data)
print(req.text)
