import poplib,os
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email

def shutdown_pc():
    sent_server = smtplib.SMTP("smtp.163.com")
    sent_server.login("13156126936@163.com", "Woaibwngdi11")
    to = ["13156126936@163.com", "1659101919@qq.com"]
    content = MIMEText("")
    content["Subject"] = "shutdown"
    content["From"] = "1356126936@163.com"
    content["To"] = ",".join(to)
    sent_server.sendmail("13156126936@163.com", to, content.as_string())
    sent_server.close()

def restart_pc():#网易邮箱不稳定，很有可能报错，过一会再试就好了，不是代码的问题。垃圾网易。。。
    sent_server=smtplib.SMTP('smtp.163.com')
    sent_server.login('13156126936@163.com','Woaibwngdi11')
    to=['13156126936@163.com','1659101919@qq.com']
    content=MIMEText('')
    content['Subject']='restart'#此处大写开头小写开头都可以，但是必须要有这三大要素，否则将会被识别为垃圾邮件，被系统拦截，导致整个程序报错
    content['From']='13156126936@163.com'
    content['To']=','.join(to)
    sent_server.sendmail('13156126936@163.com',to,content.as_string())
    sent_server.close()

#restart_pc()

def read_email():
    read=poplib.POP3('pop.163.com')
    read.user('13156126936@163.com')
    read.pass_('Woaibwngdi11')
    statistics=read.stat()
    print(statistics)
    str=read.top(statistics[0],0)
    str2=[]
    '''接下来的编码实质是：
    read这封邮件得到的一堆只能机器看懂的乱码
    然后首先转化为字节（byte）形式即str
    再从str转化为message，人们能看懂的信息
    譬如下面代码中调用了message_from_string()函数
    '''
    for x in str[1]:
        try:
            str2.append(x.decode())
        except:
            try:
                str2.append(x.decode('gbk'))
            except:
                str2.append(x.decode('big5'))
    msg=email.message_from_string('\n'.join(str2))
    title=decode_header(msg['subject'])#此处实际上是读取之前的三大要素，不用必须和之前统一大小写，都能读取到
    print(title)
    if title[0][1]:
        title2=title[0][0].decode(title[0][1])
    elif not title[0][1]:
        title2=title[0][0]
    print(title2)
    return title2
read_email()

#接下来编写主程序循环
if __name__=="__main__":
    if read_email()=='shutdown':
        os.system("shutdown -s -t 50")
    if read_email()=='restart':
        os.system("shutdown -r")







