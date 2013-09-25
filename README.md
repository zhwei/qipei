qipei
=====

汽配商城

开发环境
----------------------
+ python2.7.3  
+ django1.5

依赖包
-----------------   
+ django-mptt
+ addons文件夹下所有
+ django1.5
+ <s>PIL</s> 用pillow代替了，其安装见下面
+ django-pagination
+ django-upload-avatar
+ django-notifications-hq

    pip install django-notifications-hq

### pillow 安装

> pillow的安装需要添加对jpeg的支持，否则会出现`IOError: decoder jpeg not available`错误
>
> 需要先安装 libjpeg8-dev  
>
>     sudo apt-get install libjpeg8-dev
>
> pillow源码已放在addons文件夹中，x64位可用， 32位需修改其setup.py文件
> 将250行注释，252行取消注释。
>
> pilloｗ链接 [link](http://pan.baidu.com/share/link?shareid=3925930322&uk=3642093566)
> 不要使用官方安装，修改后才能用。

前端框架
-------------------
+ 百姓网UI库 Puerh

部署
----------------
使用 nginx + uwsgi

备注
----------------------
+ 分页使用`django-pagination`,详见[七步教你实现Django网站列表自动分页](http://django-china.cn/topic/53/)
	- 模板在`templates/pagination/pagination.html`, 现已适应`百姓网UI`和 `Bootstrap`
