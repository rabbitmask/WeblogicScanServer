<div align=center><img src=static/images/WeblogicScan.jpg width="60%"></div>

# WeblogicScanServer
开启WeblogicScanV3.*系列，采用Server部署，支持远程Weblogic漏洞扫描

# 项目停止维护，相关功能合并至https://github.com/rabbitmask/WeblogicScan

	软件作者：Tide_RabbitMask
	免责声明：Pia!(ｏ ‵-′)ノ”(ノ﹏<。)
	本工具仅用于安全测试，请勿用于非法使用，要乖哦~
	
	V 3.0简介
        V3.*系列版本是继WeblogicScanV1.*系列单体综合扫描器、WeblogicScanV2.*系列批量扫描器之后发布的一款server版本，
        V3.0是本系列的初次尝试，部分功能可能存在不健全或不稳定的情况，欢迎大家提供反馈。
        很重要的一点本项目切忌部署在互联网，一是相关政策的忌讳，二是V3.0作为测试版本并未屏蔽内网地址，后果你懂的。
        期待随着笔者flask、python的学习能让这个项目变得更佳美观、稳定，感谢支持，鞠躬！
        什么？关于首页的邪王真眼？这种东西我没法跟你解释的，邪王真眼是最强大的！还有哦，九头蛇万岁！
		
	V 3.0功能：
	提供一键poc检测，收录几乎全部weblogic历史漏洞。
	详情如下：
	
        #控制台路径泄露
        Console  
        
        #SSRF：
        CVE-2014-4210      
        
        #JAVA反序列化
        CVE-2016-0638  
        CVE-2016-3510   
        CVE-2017-3248   
        CVE-2018-2628 
        CVE-2018-2893
        CVE-2019-2725
        CVE-2019-2729
        
        #任意文件上传
        CVE-2018-2894   
        
        #XMLDecoder反序列化
        CVE-2017-3506
        CVE-2017-10271 
        
Usage:	
=
`python3 WeblogicScanStart.py`

默认端口521，如需变更，请自行更改

Software using Demo:	
=
	__        __   _     _             _        ____
	\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __
	 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \
	  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
	   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|

						By RabbitMask | V3.0


	Welcome to WeblogicScan.Have a good time~
	 * Serving Flask app "WeblogicScanServer" (lazy loading)
	 * Environment: production
	   WARNING: Do not use the development server in a production environment.
	   Use a production WSGI server instead.
	 * Debug mode: off
	[+]Task Loading Successfully：http://127.0.0.1:7001
	[+]End of Task Execution：http://127.0.0.1:7001

Software running Demo:	
=

控制台：
=
<div align=center><img src=demo/console.jpg width="80%"></div>

网站主页：
=
<div align=center><img src=demo/index.jpg width="80%"></div>

查询交互：
=
<div align=center><img src=demo/search.jpg width="80%"></div>

查询结果：
=
<div align=center><img src=demo/result.jpg width="80%"></div>
