#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
from flask import Flask, render_template
from flask import request
import WeblogicScan

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/WeblogicScan', methods=['GET'])
def search():
    return render_template('search.html')

@app.route('/WeblogicScan', methods=['POST'])
def regis():
    try:
        res_str=''
        ip=request.form['ip']
        port=request.form['port']
        res=WeblogicScan.run(ip,port)
        for i in range(len(res)):
            res_str=res_str+str(res[i])+'<br>'
        # return render_template('result.html',ip=ip,port=port,result=res_str)
        return '''
        <head>
        <meta charset="UTF-8">
        <title>WeblogicScan</title>
        <link rel="shortcut icon" href="static/images/AboutU.ico">
        </head>
        <div align=center><img src="static/images/WeblogicScan.jpg" width="30%"></div>
        <body>
        <div align="center">
        <h1>WeblogicScan</h1>
        <h3>Weblogic一键漏洞检测</h3>
        </div>
        <div style='margin-left:50px;'><h3>您本次扫描结果如下:</h3><h4>本次目标: http://{}:{}</h4><h5>{}</h5></div>
        </body>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <footer>
        <div align=center>Copyright © 2019 Power by <a href="https://rabbitmask.github.io">RabbitMask</a></div>
        </footer>
        '''.format(request.form['ip'],request.form['port'],res_str)
    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=521, debug=False)