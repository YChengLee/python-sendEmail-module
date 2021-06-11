# python-sendEmail-module
发送邮件模块，用于监控报警、爬虫监控等

# Usage
```
#只需要把mailSystem放入项目文件夹内即可
from mailSystem import MailSystem


mailSever = MailSystem()
yourName = "Your Name
recipientName = "Ricipitor Name"
recipientMailAddress = "Ricipitor Mail"
mailTitle = "2021年6月11日 通知公告(测试)"
mailContent = f"""
<p>{recipientName},你好:</p>
<p style="text-indent:2em;">你关注的网站已经更新，请及时查看。</p>
"""
mailSever.createMail(mailTitle,mailContent)
mailSever.addSendInfo(yourName,recipientName,recipientMailAddress)
mailSever.sendMail()
```