import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

headers = {
    'Referer': 'https://yz.chsi.com.cn/apply/cjcx/t/14423.dhtml',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
}
url = 'https://yz.chsi.com.cn/apply/cjcx/cjcx.do'
xm = '你的姓名'
zjhm = '你的身份证号'
ksbh = '你的准考证号'
bkdwdm = '院校代码'
data = {'xm': xm, 'zjhm': zjhm, 'ksbh': ksbh, 'bkdwdm': bkdwdm}


def send(message):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "你的qq号@qq.com"  # 用户名
    mail_pass = "你的qq邮箱口令"  # 口令

    sender = '你的qq号@qq.com'
    receivers = ['你的qq号@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 邮件正文
    message = MIMEText(message, 'plain', 'utf-8')
    message['From'] = Header("你的qq号@qq.com <你的qq号@qq.com>", 'utf-8')
    message['To'] = Header("To whom it may concern", 'utf-8')
    message['Subject'] = Header('出成绩了！', 'utf-8')  # 标题

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())


while True:
    res = requests.post(url, data=data, headers=headers).text
    if "无查询结果" in res or "超时" in res:
        print("No " + time.ctime())
    else:
        send(res)
        break
    time.sleep(60)
