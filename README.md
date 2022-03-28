# 开发环境配置及部署说明

## django配置

* 安装python3.5及以上版本

* pip安装django，版本要求3.2.10否则可能出现版本改动的未知错误

  * ```bash
    pip install django==3.2.10
    ```

## 数据库配置

* MySQL

* 新建任意数据库

* 在django的setting文件中配置信息

  * ```django
    DATABASES = {
        'default':
        {
            'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
            'NAME': 'study', # 数据库名称
            'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1
            'PORT': 3306, # 端口
            'USER': 'root',  # 数据库用户名
            'PASSWORD': 'xxxxx', # 数据库密码
        }
    }
    ```

* 安装PyMySQL

  * ```bash
    pip install PyMySQL
    ```



## 数据库迁移

```bash
#第一次使用该系统需要迁移数据库
#执行如下指令
python manage.py makemigrations
python manage.py migrate
```



## 数据库视图创建

由于django无法创建视图，需要使用视图需自己添加，本系统所需的视图创建代码已打包， 直接使用即可

==一定要在执行以上迁移操作之后再创建视图==



## 本地环境部署

```bash
#在本地部署只需输入以下代码即可运行
python manage.py runserver
#执行完成后默认端口为8000即访问127.0.0.1:8000即可
#你也可以使用以下代码来自定义端口
python manage.py runserver 127.0.0.1:[port]
#拥有admin后台
#使用需创建超级管理员账号
python manage.py createsuperuser
```

