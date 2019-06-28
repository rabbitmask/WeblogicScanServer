#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import modules.Console
import modules.CVE_2014_4210
import modules.CVE_2016_0638
import modules.CVE_2016_3510
import modules.CVE_2017_3248
import modules.CVE_2017_3506
import modules.CVE_2017_10271
import modules.CVE_2018_2628
import modules.CVE_2018_2893
import modules.CVE_2018_2894
import modules.CVE_2019_2725
import modules.CVE_2019_2729

version = "3.0"
banner='''
__        __   _     _             _        ____                  
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __  
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_| 
                             |___/ 
                             By Tide_RabbitMask | V {} 
'''.format(version)

def modulesS(rip,rport):
    res = []
    print('[+]Task Loading Successfully：http://{}:{}'.format(rip,rport))
    try:
        res.append(modules.Console.run(rip, rport))
    except:
        res.append("[-]Target Weblogic console address not found.")

    try:
        res.append(modules.CVE_2014_4210.run(rip, rport))
    except:
        res.append ("[-]CVE_2014_4210 not detected.")

    try:
        res.append(modules.CVE_2016_0638.run(rip, rport, 0))
    except:
        res.append ("[-]CVE_2016_0638 not detected.")

    try:
        res.append(modules.CVE_2016_3510.run(rip, rport, 0))
    except:
        res.append ("[-]CVE_2016_3510 not detected.")

    try:
        res.append(modules.CVE_2017_3248.run(rip, rport, 0))
    except:
        res.append ("[-]CVE_2017_3248 not detected.")

    try:
        res.append(modules.CVE_2017_3506.run(rip, rport, 0))
    except:
        res.append ("[-]CVE_2017_3506 not detected.")

    try:
        res.append(modules.CVE_2017_10271.run(rip, rport, 0))
    except:
        res.append("[-]CVE_2017_10271 not detected.")

    try:
        res.append(modules.CVE_2018_2628.run(rip, rport, 0))
    except:
        res.append("[-]CVE_2018_2628 not detected.")

    try:
        res.append(modules.CVE_2018_2893.run(rip, rport, 0))
    except:
        res.append("[-]CVE_2018_2893 not detected.")

    try:
        res.append(modules.CVE_2018_2894.run(rip, rport, 0))
    except:
        res.append("[-]CVE_2018_2894 not detected.")

    try:
        res.append(modules.CVE_2019_2725.run(rip, rport, 0))
    except:
        res.append("[-]CVE_2019_2725 not detected.")

    try:
        res.append(modules.CVE_2019_2729.run(rip, rport, 0))
    except:
        res.append("[-]CVE_2019_2729 not detected.")

    print("[+]End of Task Execution：http://{}:{}".format(rip,rport))
    return res

def run(ip,port):
    return modulesS(ip,port)

if __name__ == '__main__':
    run('127.0.0.1',7001)

