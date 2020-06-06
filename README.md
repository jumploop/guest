# 发布会签到系统


介绍： 本项目为《Python Web接口开发与测试》一书的项目代码。代码实现的一个较为完整的发布会签到系统。 最主要的是它包含了丰富的测试代码:

本项目改用python3和django最新的版本进行开发。

## 开发环境

    windows10系统
    python3.7.7
    Django3.0.6

## 第一章 Django入门

### 1.1创建项目

    D:\pydj>django-admin startproject guest #创建 guest 项目

为该项目命名为“guest” 。 项目结构如下：

    guest/
    ├── guest/
    │ ├── __init__.py
    │ ├── settings.py
    │ ├── urls.py
    │ └── wsgi.py
    └──manage.py

guest/__init__.py： 一个空的文件， 用它标识一个目录为 Python 的标准包。

guest/settings.py： Django 项目的配置文件， 包括 Django 模块应用配置， 数据库配置， 模板配置等。

guest/urls.py： Django 项目的 URL 声明。

guest/wsgi.py： 为 WSGI 兼容的 Web 服务器服务项目的切入点。

manage.py： 一个命令行工具， 可以让你在使用 Django 项目时以不同的方式进行交互。

### 1.2 创建应用

    D:\pydj>cd guest # 进入 guest 项目目录

    D:\pydj\guest>python3 manage.py startapp sign #创建 sign 项目
创建“sign” 应用。

migrations/： 用于记录 models 中数据的变更。

admin.py： 映射 models 中的数据到 Django 自带的 admin 后台。

apps.py： 在新的 Django 版本中新增， 用于应用程序的配置。

models.py： 创建应用程序数据表模型（对应数据库的相关操作） 。

tests.py： 创建 Django 测试。

views.py： 控制向前端显示哪些数据。

### 1.3 运行项目

现在我们要把项目运行起来， Django 提供了 Web 容器， 只需要通过“runserver” 命令就可以把项目运行
起来。

    D:\pydj\guest>python3 manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    June 05, 2020 - 12:15:46
    Django version 3.0.6, using settings 'guest.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

Django 默认会通过本机的 8000 端口来启动项目， 如果你的当前环境该端口号被占用了， 也可以在启动
时指定 IP 地址和端口号。

    D:\pydj\guest>python3 manage.py runserver 127.0.0.1:8001
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    June 05, 2020 - 12:17:20
    Django version 3.0.6, using settings 'guest.settings'
    Starting development server at http://127.0.0.1:8001/
    Quit the server with CTRL-BREAK.

其中“127.0.0.1” 为指向本机的 IP 地址， “8001” 为设置的端口号。
打开浏览器， 访问： http://127.0.0.1:8001/

![Image](https://pic4.zhimg.com/80/v2-8603df9728b90ab827d6eb4efecc40e3.png)

如果你在浏览器中可以看到如图的页面， 那么说明 Django 已经可以工作了。

### 1.4、 Hello Django！

大多编程语言的教程， 第一个例子总是会教你如何打印“Hello xxx！ ” ， 我们也不免俗套， 接下来和我
一起开发一个“Hello Django!” 的页面。
在此之前， 我们首先需要配置一下 guest/settings.py 文件， 将 sign 应用添加到项目中。

```python
……
# Application definition
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'sign', #添加 sign 应用
] …
…
```

接下来想一想， 我们应该用哪个路径来显示“Hello Django!” 。 命名一个/index/路径。 在浏览器地址栏输
入： http://127.0.0.1:8001/index/

![Image](https://pic4.zhimg.com/80/v2-25123cc0692cde88e0163ae51922bff8.png)

显然， 我们访问的路径并不存在， 如图， Django 提示“Page not found(404)” ， 不要害怕， 这并不是
一个严重的错误， 只是因为我们访问了一个不存在的路径而已， 认真读一下页面上的提示， 将会得到不少有
用信息：

Django 在项目中的 guest 子目录下通过 urls.py 文件来定义 URLconf。

但是， 在 urls.py 文件中只找到了一个 admin/的路由配置。
当前网址 index/， 并没有匹配到。

根据本 Django 的提示， 再接下来打开 guest/urls.py 文件添加该目录。

```python

……
from django.conf.urls import url
from django.contrib import admin
from sign import views #导入 sign 应用 views 文件
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
]
```

等等！ 这次项目在启动的时候就报错了。

    D:\pydj\guest>python3 manage.py runserver
    Performing system checks...
    ……
    File "D:\pydj\guest\guest\urls.py", line 22, in <module>
    url(r'^index/$', views.index),
    AttributeError: module 'sign.views' has no attribute 'index'

再次启动 Django 时， 出错了！ 提示在 views.py 文件中并没有 index 属性， 确实如些。 那么接下来
打../sign/views.py 文件创建 index 函数。

```python
from django.http import HttpResponse
# Create your views here.
def index(request):
return HttpResponse("Hello Django!")
```

定义 index 函数， 并通过 HttpResponse 类向页面返回字符串“Hello Django!” 。

HttpResponse 类存在 django.http.HttpResponse 中， 以字符串的形式传递给前端页面数据。

![Image](https://pic4.zhimg.com/80/v2-00526be4147ef6def2e7d570065227b0.png)

如图， 页面成功出现了“Hello Django！ ” 。 开心一下吧！ 你的第一个 Django 程序已经成功了。

### 1.5 使用模板

现在要用 HTML 页面来替代“Hello Django！ ” 字符串， 那么处理方式也会有所不同， 你可以认为这是
一次重构。

在应用 sign/目录下创建 templates/index.html 文件。 （读者需要注意该 HTML 文件的所在路径， 不要弄错
噢！ ）

```html
<html>
<head>
<title>Django Page</title>
</head>
<body>
<h1>Hello Django!</h1>
</body>
</html>
```

关于 HTML 超文本标记语言， 请读者参考其它资料学习， 本书将不做过多介绍。

修改视图文件 views.py

```python
from django.shortcuts import render
# Create your views here.
def index(request):
return render(request,"index.html")
```

这里抛弃 HttpResponse 类， 转而使用 Django 的 render 函数。 该函数的第一个参数是请求对象的， 第二个参
数返回一个 index.html 页面。
再次刷新页面， 查看 index.html 中所展示的内容

![Image](https://pic4.zhimg.com/80/v2-9e34c7af9fc0fa39741266c0fa85a3f8.png)

## 第二章 Django 视图

以需求来驱动学习是笔者一直使用的学习方式， 就是在学习一项技术之初， 就确定好需求， 要以该项技
术实现一个具体需求。 所以， 我们一开始就已经定好了目标， 就是要使用 Django 开发一个发布会签到系统。
所以， 做为一个系统， 那么用户登录功能必不可少。 这一章， 我们将要开发一个用户登录功能。 不要小看这
个登录噢！ 它包含了不少需要学习知识点。

### 2.1 来写个登录

继续在上一章的基础上开发， 不过这一次， 我们先从前端页面写起。 打开.../sign/templates/index.html 文
件， 修改代码如下。

```html
<html>
<head>
<title>Django Page</title>
</head>
<body>
<h1>发布会管理</h1>
<form>
<input name="username" type="text" placeholder="username" ><br>
<input name="password" type="password" placeholder="password"><br>
<button id="btn" type="submit">登录</button>
</form>
</body>
</html>
```

启动 Django 服务， 访问： http://127.0.0.1:8000/index/

![Image](https://pic4.zhimg.com/80/v2-f79446e63fe523d7116cab2571aae9d0.png)

虽然在页面上已经看到了一个登录功能， 但它目前还并不可用。 要想真正实现登录还需要思考以一些问
题。 当点输入用户名密码并点击“登录” 按钮之后， 表单（form） 中的数据要以什么方式（GET/POST） 提交
系统？ 系统如何验证得到的用户名密码？ 如果验证成功应该跳转到什么页面？ 如果验证失败如何将错误提示
返加给用户？

### 2.1.1 GET 与 POST 请求

当客户机通过 HTTP 协议向服务器提交请求时， 最常用到的方法是 GET 和 POST。
GET - 从指定的资源请求数据。
POST - 向指定的资源提交要被处理的数据

**GET 请求**

先来看看 GET 方法是如何传参数， 给 form 添加属性 method="get"。

```html
……
<form method="get">
<input name="username" type="text" placeholder="username" ><br>
<input name="password" type="password" placeholder="password"><br>
<button id="btn" type="submit">登录</button>
</form>
……
```

然后保存在 index.html 文件， 重新刷新页面。 输入用户名、 密码， 点击登录。
查看浏览器 URL 地址栏：

http://127.0.0.1:8000/index/?username=admin&password=admin123

GET 方法会将用户提交的数据添加到 URL 地址中， 路径后面跟问号“？ ” ， username 和 password 为
HTML 代码中`<input>`标签的 name 属性值， username=admin 表示用户名输入框得到的输入数据为“admin” 。
password=admin123 密码输入框得到的输入数据为“admin123” 。 多个参数之间用“&” 符号隔开。

**POST 请求**

同样是上面的代码， 再将 form 表单的中的属性改为 method="post" 。 重新刷新页面后， 再次输入用户名
密码， 点击“登录”

![Image](https://pic4.zhimg.com/80/v2-2161b0b751eab0cb5b4585f4b4a23a36.png)

“CSRF verification failed. Request aborted.”

这个提示非常有意思， 而且被许多初学 Django 的同学问到。 如果你仔细阅读上面的帮助信息， 那么将会
知道这个错误的原因， 并且找到解决办法。 然而， 新手往往面对错误提示时显得恐慌和手足无措， 从而忽略
掉页面上的提示信息。

如果你从未听说过“跨站请求伪造” （ Cross-Site Request Forgery， CSRF） 漏洞， 现在就去查资料吧。
Django 针对 CSRF 的保护措施是在生成的每个表单中放置一个自动生成的令牌， 通过这个令牌判断 POST
请求是否来自同一个网站。

之前的模板都是纯粹的 HTML， 在这里要首次使用到 Django 的模板， 使用“模板标签” （ template tag）
添加 CSRF 令牌。 在 from 表单中添加{% csrf_token %}。

```html
<form method="post">
<input name="username" type="text" placeholder="username" ><br>
<input name="password" type="password" placeholder="password"><br>
<button id="btn" type="submit">登录</button>
{% csrf_token %}
</form>
```
然后， 刷新页面并重新提交登录表单， 错误提示页面消失了

![Image](https://pic4.zhimg.com/80/v2-b95896887b31e9288ab49ede287ee80a.png)

借助谷歌浏览器开发者工具进行查看 POST 请求。F12，然后点到network，如图

![Image](https://pic4.zhimg.com/80/v2-a7a9bd241cde1894911f2ef3ab2db14a.png)

 你会看到除了 usrname 和 password 参数外，
还多了一个 csrfmiddlewaretoken 的参数。 当页面向 Django 服务器发送一个 POST 请求时， 服务器端要求客户
端加上 csrfmiddlewaretoken 字段， 该字段的值为当前会话 ID 加上一个密钥的散列值。
如果想忽略掉该检查， 可以在.../guest/settings.py 文件中注释掉 csrf。

```python
……
MIDDLEWARE = [
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
#'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
] …
…
```

### 2.1.2、 处理登录请求

现在了解了将表单中的数据提交给服务器的方式（GET/POST） ， 那么将登录数据提交给 Django 服务器
的谁来处理？ 可以通过 form 表单的 action 属性来指定提交的路径。

```html
index.html
……
<form method="post" action="/login_action/">
……
```

打开../guest/urls.py 文件添加 login_action/的路由。

```python
from sign import views
urlpatterns = [
……
path('login_action/', views.login_action),
]

```

打开 sign/views.py 文件， 创建 login_action 视图函数。

```python
from django.shortcuts import render
from django.http import HttpResponse
……
# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            return HttpResponse('login success!')
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

```

通过 login_aciton 函数来处理登录请求。

客户端发送的请求信息全部包含在 request 中。 关于如何获取 request 中包含的信息， 参考 Django 文档。

https://docs.djangoproject.com/en/1.10/ref/request-response/
首先， 通过 request.method 方法得到客户发送的请求方式， 判断其是否为 POST 请求类型。

接着， 通过 request.POST 来获取 POST 请求。 通过.get()方法来寻找 name 为“username” 和“password”
的 POST 参数， 如果参数没有提交， 返回一个空的字符串。 此处的“username” 和“password” 对应 form 表
单中`<input>` 标签的 name 属性， 可见这个属性的重要性。

再接下来， 判断 POST 请求得到的 username 和 password 是否为“ admin/admin123” ， 如果是则通过
HttpResponse 类返回“login success!” 字符串。 否则， 将通过 render 返回 index.html 登录页面， 并且顺带返回
错误提示的字典“{'error': 'username or password error!'}” 。

但是， 显然 index.html 页面上并没有显示错误提示的地方， 所以， 需要在 index.html 页面中添加 Django
模板。


```html

……
<form method="post" action="/login_action/">
<input name="username" type="text" placeholder="username" ><br>
<input name="password" type="password" placeholder="password"><br>
{{ error }}<br>
<button id="btn" type="submit">登录</button>
{% csrf_token %}
</form>
……
```

此处又使用到了 Django 的模板语言， 添加{{ error }}， 它对应 render 返回字典中的 key， 并且在登录失败
的页面中显示 value， 即“username or password error!” 信息。 好了， 现在来体验一下登录功能， 分别看看登录
失败和成功的效果。 

![Image](https://pic4.zhimg.com/80/v2-9a98c08564adc7f58f54001a2a814846.png)

![Image](https://pic4.zhimg.com/80/v2-49fb508ab44b2e731eb1e1a0507884ed.png)

### 2.1.3、 登录成功页

显然， 登录成功返回的“login success!” 字符串只是一种临时方案， 只是为了方便验证登录的处理逻辑，
现在没有问题之后， 需要通过 HTML 页面来替换。
我们要开发的是发布会签到系统， 那么我希望登录之后默认显示发布会列表。 所以， 首先创
建.../templates/event_manage.html 页面。
```html
<html>
<head>
<title>Event Manage Page</title>
</head>
<body>
<h1>Login Success!</h1>
</body>
</html>
```

修改.../sign/views.py 中的 login_action 函数。

```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
……
# 登录动作
……
if username == 'admin' and password == 'admin123':
    return HttpResponseRedirect('/event_manage/')
……
# 发布会管理
def event_manage(request):
    return render(request,"event_manage.html")
```

此处又用到的一个新的类 HttpResponseRedirect， 它可以对路径进行重定向， 从而将登录成功之后的请求
指向/event_manage/目录。
创建 event_manage 函数， 用于返回发布会管理 event_manage.html 面页。
最后， 不要忘记在../guest/urls.py 文件中添加路径 event_manage/的路由。

### 2.2 Cookie 和 Session

接下来继续另外一个有意思的话题， 在不考虑数据库验证的情况下， 假如用户通过“zhangsan” 登录，
然后， 在登录成功页显示“嘿， zhangsan 你好！ ” ， 这是一般系统都会提供的一个小功能， 接下来我们将分别
通过 Cookie 和 Session 来实现它。

**Cookie 与 Session**

Cookie 机制： 正统的 Cookie 分发是通过扩展 HTTP 协议来实现的， 服务器通过在 HTTP 的响应头中加上
一行特殊的指示以提示浏览器按照指示生成相应的 Cookie。 然而纯粹的客户端脚本如 JavaScript 或者 VBScript
也可以生成 Cookie。 而 Cookie 的使用是由浏览器按照一定的原则在后台自动发送给服务器的。 浏览器检查所
有存储的 Cookie， 如果某个 Cookie 所声明的作用范围大于等于将要请求的资源所在的位置， 则把该 cookie 附
在请求资源的 HTTP 请求头上发送给服务器

Session 机制： Session 机制是一种服务器端的机制， 服务器使用一种类似于散列表的结构（也可能就是
使用散列表） 来保存信息。

### 2.2.1、 Cookie 的使用

继续修改.../sign/views.py 文件：

```python

……
# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user', username, 3600) # 添加浏览器 cookie
            return response
        else:
            return render(request,'index.html', {'error': 'username or password error!'})

# 发布会管理
def event_manage(request):
    username = request.COOKIES.get('user', '') # 读取浏览器 cookie
    return render(request,"event_manage.html",{"user":username})
```

当用户登录成功后， 在跳转到 event_manage 页面时， 通过 set_cookie()方法来添加浏览器 Cookie。

这里给 set_cookie()方法传了三个参数， 第一个参数“user” 是用于表示写入浏览器的 Cookie 名， 第二个
参数 username 是由用户在登录页上输入的用户名， 第三个参数 3600 用于表示该 cookie 信息在浏览器中的停
留时间， 默认以秒为单位。

而在 event_manage 视图函数中， 通过 request.COOKIES 来读取 Cookie 名为“user” 的值。 并且通过 render
将和 event_manage.html 页面一起返回给客户端浏览器。

修改.../templates/event_manage.html 页面， 添加<div>标签来显示用户登录的用户名.

```html
……
<div style="float:right;">
<a>嘿！ {{ user }} 欢迎</a><hr/>
</div>
……
```

重新再来登录一次， 将会看到页面如图

![Image](https://pic4.zhimg.com/80/v2-c0db08443a5eb0002f6c94b8d1b6ee46.png)

![Image](https://pic4.zhimg.com/80/v2-c56784a3f0fb06e22a18028dcce28fe3.png)

### 2.2.2、 Session 的使用

Cookie 固然好， 但存在一定的安全隐患。 Cookie 像我们以前用的存折， 用户的存钱、 取钱都会记录在这
张存折上（即浏览器中会保存所有用户信息） ， 那么对于有非分想法的人可能会去修改存折上的数据（这个
比喻忽略掉银行同样会记录用户存取款的金额） 。

相对于存折， 银行卡要安全的得多， 客户拿到的只是一个银行卡号（即浏览器只保留一个 Sessionid） ，
那么用户的存钱、 取钱都会记录在银行的系统里（即服务器端） ， 只得到一个 sessionid 是没有任何意义的，
所以相对于 Cookie 来说就会安全很多。

在 Django 中使用 Session 和 Cookie 类似。 我们只用将 Cookie 的几步操作替换成 session 即可。

修改.../sign/views.py 文件， 在 login_action 函数中， 将：

    response.set_cookie('user', username, 3600)

替换为：

    request.session['user'] = username # 将 session 信息记录到浏览器

在 event_manage 函数中， 将：

    username = request.COOKIES.get('user', '')
替换为：

    username = request.session.get('user', '') # 读取浏览器 session

再次尝试登录， 不出意外的话将会得到一个错误。

“no such table: django_session”

这个错误跟 Session 的机制有关， 既然要服务器端记录用户的数据， 那么一定要有地方来存放用户
Sessionid 对应的信息才对。 所以， 我们需要创建 django_session 表。 别着急！ Django 已经帮我们准备好这些常
用的表， 只需要将他们生成即可， 是不是很贴心。

    D:\pydj\guest>python3 manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying sessions.0001_initial... OK

通过“migrate” 命令进行数据迁移。

等等， 我们好像并没配置数据库啊， 为什么数据库已经生成了表呢？ 这是因为 Django 已经默认帮我设置
sqlite3 数据库。 打开.../settings.py 文件， 查看 sqlite3 数据库的配置

```python
……
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
} …
…
```

另外， 在 guest 项目的根目录下会生成一个 db.sqlite3 文件。 关于数据的操作我们会放在下一章讨论。 此
时， 先来验证 Session 功能是否生效， 重新登录。

![Image](https://pic4.zhimg.com/80/v2-fe93a6809e893c4a0ece31a60b396dd7.png)

### 2.3 Django 认证系统

到目前为止， 虽然实现了登录， 但显然用户登录信息的验证并未真正实现， 目前的做法只是简单的用 if
语句判断用户名和密码是否为“admin/admin123” ， 所以， 我们并没有完整的用户数据。

### 2.3.1、 登录 Admin 后台

在上一小节执行 manage.py 的“migrate” 命令时， Django 同时也帮我们生成了 auth_user 表。 同时， 我们
可以通过 URL 地址： http://127.0.0.1:8000/admin/ 来访问 Django 自带的 Admin 管理后台。 在此， 之前先来创
建登录 Admin 后台的管理员账号。

    D:\pydj\guest>python3 manage.py createsuperuser
    Username (leave blank to use 'fnngj'): admin #输入用户名
    Email address: admin@mail.com #输入邮箱
    Password: #输入密码
    Password (again): #重复输入密码
    Superuser created successfully.

创建的超级管理员帐号/密码为： admin/admin123456

![Image](https://pic4.zhimg.com/80/v2-de2e1572adbeeafe8fb507449017834f.png)

![Image](https://pic4.zhimg.com/80/v2-1c9211d93ffff88874e90fb45d3ac95f.png)

如图 ， 通过创建的管理员账号登录 Admin 后台， 尝试点击“Add” 链接添加新的用户， 并且用
新创建的用户再次登录后台。 尝试一下吧！ 相信你可以做到。(添加用户之后，需要给用户分组，并授予权限才能登陆成功)

### 2.3.2、 引用 Django 认证登录

既然 Django 已经帮我们做好用户体系， 那么就直接拿来使用好了。
打开.../sign/views.py 文件修改 login_action 函数。

```python
……
from django.contrib import auth
……
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录
            request.session['user'] = username # 将 session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html', {'error': 'username or password error!'})
```

使用 authenticate()函数认证给出的用户名和密码。 它接受两个参数， 用户名 username 和密码 password，
并在用户名密码正确的情况下返回一个 user 对象。 如果用户名密码不正确， 则 authenticate()返回 None。

通过 if 语句判断 authenticate()返回如果不为 None， 说明用户认证通过。 那么接下来调用 login()函数进行
登录。 login()函数接收 HttpRequest 对象和一个 user 对象。

重新使用 admin 管理后台创建用户账户来验证登录功能吧！

### 2.3.3、 关上窗户

“上帝为你关上了一扇门， 也一定会为你打开一扇窗户” ， 我们为系统开发了一个需要用户认证的登录，
然而， 我们不需要通过登录也可以直接访问到登录成功的页面。

现在， 尝试直接访问： http://127.0.0.1:8000/event_manage/

看！ 是不是直接打开了登录成功页， 那为什么还需要通过登录来访问这个页面呢？ 所以， 我们要把这些
“窗户” 都关上， 使用户只能通过登录来访问系统。

再来感受一下 Django 的强大之处吧！ 一秒钟让你关好窗户。

```python
views.py
……
from django.contrib.auth.decorators import login_required
……
# 发布会管理
@login_required
def event_manage(request):
    username = request.session.get('user', '')
    return render(request,"event_manage.html",{"user":username})
```

是的， 就是这么简单， 如果想限制某个视图函数必须登录才能访问， 只需要在这个函数的前面加上
@login_required 即可。

你可以再次尝试访问/event_manage/目录（千万不要忘记清理浏览器缓存再试！ ） ， 看看还能否直接访问
到。

![Image](https://pic4.zhimg.com/80/v2-f2d54bea460d9fb13405ccdf95f36974.png)

如图 ， Django 会告诉访问的路径并不存在（404） 。

如 果 你 细 心 ， 会 发 布 在 访 问 被 @login_required 装 饰 的 视 图 时 ， 默 认 会 跳 转 的 URL 中 会 包 含
“/accounts/login/” ， 为什么不让它直接跳转到登录页面呢？ 不但要告诉你窗户是关着的， 还要帮你指引到门
的位置。

接下来修改.../urls.py 文件， 添加以下路径。

```python
……
from sign import views
urlpatterns = [
path('', views.index),
path('index/', views.index),
path('accounts/login/', views.index),
……
```

当用户访问：

    http://127.0.0.1:8000/
    http://127.0.0.1:8000/index/
    http://127.0.0.1:8000/event_manage/

默认， 都会跳转到登录页面。 但是， 如果你访问的是其它不存的路径， 比如/abc/， 依然会显示图 3.11 的
页面。 这个时候需要设置默认的 404 页面， 本书会在项目部署的章节来添加这个页面。

## 第三章 Django 模型

在 Web 应用中， 主观逻辑经常牵涉到与数据库的交互。 以数据库驱动网站在后台连接数据库服务器， 从
中取出一些数据， 然后在 Web 页面用漂亮的格式展示这些数据。 这个网站也可能会向访问者提供修改数据库
数据的方法。 许多复杂的网站都提供了以上两个功能的某种结合。

对于我们的发布会签到系统来说， 也是以数据管理为主的网站， 主要管理发布会和嘉宾数据。 有一个观
点， 对于数据驱动的 Web 系统， 数据库表的设计完成， 就相当于 Web 系统已经完成了一半， 可见数据库表的
设计难度， 以及在 Web 开发中的重要性。

### 3.1 设计系统表

Django 提供完善的模型（model） 层主要用来创建和存取数据， 不需要我们直接对数据库操作。

Django 模型基础知识：

每个模型是一个 Python 类， 继承 django.db.models.model 类。

该模型的每个属性表示一个数据库表字段。

所有这一切， 已经给你一个自动生成的数据库访问的 API。

打开.../sign/models.py 文件， 完成表的创建

```python
from django.db import models
# Create your models here.
# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=100) # 发布会标题
    limit = models.IntegerField() # 参加人数
    status = models.BooleanField() # 状态
    address = models.CharField(max_length=200) # 地址
    start_time = models.DateTimeField('events time') # 发布会时间
    create_time = models.DateTimeField(auto_now=True) # 创建时间（自动获取当前时间）
    def __str__(self):
        return self.name

# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE) # 关联发布会 id
    realname = models.CharField(max_length=64) # 姓名
    phone = models.CharField(max_length=16) # 手机号
    email = models.EmailField() # 邮箱
    sign = models.BooleanField() # 签到状态
    create_time = models.DateTimeField(auto_now=True) # 创建时间（自动获取当前时间）
    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname
```

对于产品发布会来说， 显然它是一个事件。 那么时间、 地点、 人物等要素必不可少。 数据库表的设计需
要围绕着这些要素进行。

关于发布会表（Event 类） 和嘉宾表（Guest 类） 的每一个字段， 在代码中已经做了注解。 有些字段的设
计需要做一下简单的说明。

首先， 发布会表和嘉宾表中默认都会生成自增 id， 而我们在创建模型时不需要声明该字段。

其次， 发布会表中增加了 status 字段用于表示发布会的状态是否开启， 用于控制该发布会是否可用。

再次， 嘉宾表中通过 event_id 关联发布会表， 一条嘉宾信息一定所属于某一场发布会。

最后， 对于一场发布会来说， 一般会选择手机号作为一位嘉宾的验证信息， 所以， 对于一场发布会来说，
手机号必须是唯一。 除了嘉宾 id 外， 这里通过发布会 id +手机号来做为联合主键。

`__str__()`方法告诉 Python 如何将对象以 str 的方式显示出来。 所以， 为每个模型类添加了`__str__()`方法。
（如果读者使用的是 Python2.x 的话， 这里需要使用`__unicode__()`） 。
Django 数据类型， 如下表：

![Image](image/django%20模型和字段%20.png)

进行数据库迁移：

    D:\pydj\guest>python3 manage.py makemigrations sign
    Migrations for 'sign':
        sign\migrations\0001_initial.py
            - Create model Event
            - Create model Guest


    D:\pydj\guest>python3 manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions, sign
    Running migrations:
        Applying sign.0001_initial... OK

## 3.2 admin 后台管理

在第三章 2.3.1 小节， 通过 Admin 后台管理用户组/用户表非常方便。 那么， 我们创建的发布会和嘉宾表
同样可以通过 Admin 后台去管理。
打开.../sign/admin.py 文件。

```python
from django.contrib import admin
from sign.models import Event, Guest
# Register your models here.
admin.site.register(Event)
admin.site.register(Guest)
```

这些代码通知 admin 管理工具为这些模块逐一提供界面。

登录 admin 后台： http://127.0.0.1:8000/admin/ （admin/admin123456）

![Image](https://pic4.zhimg.com/80/v2-62edf4b61800c0bbb1c696ed87d9e230.png)

现在点击“Add” 添加一条发布会（Event） 数据。

![Image](https://pic4.zhimg.com/80/v2-be73a50229464ecbe559e95b81f77fe1.png)

如图 ， 显示的是一条发布会数据， 然而只有发布会名称， 如何才能显示表中的更多字段呢？ 继续修
改.../sign/admin.py 文件。

```python
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time','id']
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
```

新建了 EventAdmin 类， 继承 django.contrib.admin.ModelAdmin 类， 保存着一个类的自定义配置， 以供Admin 管理工具使用。 这里只自定义了一项： list_display， 它是一个字段名称的数组， 用于定义要在列表中显
示哪些字段。 当然， 这些字段名称必须是模型中的 Event()类定义的。

接下来修改 admin.site.register()调用， 添加了 EventAdmin。 你可以这样理解： 用 EventAdmin 选项注册
Event 模块

然后， 对 Guest 模块也做了同样的操作。
保存代码后， 重新刷新 Event 列表， 如图 

![Image](https://pic4.zhimg.com/80/v2-57fdb7d941cf7d2c1c6aca918b33e760.png)

再接下来， 点击“Add” 添加一条嘉宾（Guest） 数据。 如图

![Image](https://pic4.zhimg.com/80/v2-9b457136b8abf1346be1c5c89794cb23.png)

除此之外， Admin 管理后台提供了的很强的定制性， 我们甚至可以非常方便生成搜索栏和过滤器。 重新
打开.../sign/admin.py 文件， 做如下修改。

```python
……
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time','id']
    search_fields = ['name'] #搜索栏
    list_filter = ['status'] #过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']
    search_fields = ['realname','phone'] #搜索栏
    list_filter = ['sign'] #过滤器
……

```

search_fields 用于创建表字段的搜索器， 可以设置搜索关键字匹配多个表字段。 list_filter 用于创建字段过
滤器。

查看 Event 列表或者 Guest 列表， 如图

![Image](https://pic4.zhimg.com/80/v2-844cdf14d7dffbb77788d97484ad685f.png)

![Image](https://pic4.zhimg.com/80/v2-e48d608b44721099618286fa0687e223.png)

### 3.3 基本数据访问

这一小节跟着我来练习数据库表的操作， manage.py 提供的 shell 命令， 可以在该来模式下练习数据库表
的操作

    D:\pydj\guest> python3 manage.py shell
    Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>>

虽然， 这看上去很像 Python 的 shell 模式。而该 shell 模式由 Django 特供版， 只有在该模式才能操作 Django
模型。

    ……
    >>> from sign.models import Event, Guest
    >>> Event.objects.all()
    <QuerySet [<Event: 小米10发布会>]>
    >>> Guest.objects.all()
    <QuerySet [<Guest: jack>]>


>from sign.models import Event, Guest

导入 sign 应用下的 models.py 中的 Event 表和 Guest 表。

>table.objects.all()

获得 table（Event、 Gues 表） 中的所有对象。

### 3.3.1、 插入数据

    >>> from datetime import datetime
    >>> e1 = Event(id=2,name='红米 Pro 发布会',limit=2000,status=True,address='北京水立
    方',start_time=datetime(2016,8,10,14,0,0))
    >>> e1.save()
    H:\guest\venv\lib\site-packages\django\db\models\fields\__init__.py:1368: RuntimeWarning: DateTimeField Event.start_time received a naive datetime (2016-08-10 14:00:00) while time zone support is active.
    RuntimeWarning)

因为 start_time 字段需要设置日期时间， 所以导入和 datetime.datetime()方法。 但是， 我们收到了一行警告
信息“RuntimeWarning: DateTimeField Event.start_time received a naive datetime (2016-08-10 14:00:00) while time
zone support is active.”

这跟 UTC 有关， 如果读者感兴趣可以百度 UTC 是什么？ 这里， 我们暂时忽略掉这个问题， 最简单的方
式就是在.../settings.py 文件中设置： USE_TZ = False。

修改 settings.py 文件保存后， 需要执行“quit()”命令退出 shell 模式， 并重新执行“Python3 manage.py shell”
进入， 刚才的设置才会生效。

如果你觉得创建和保存分两步完成过于麻烦， 也可以通过 table.objects.create()方法将两步合为一步， 方
法如下

    >>> Event.objects.create(id=3,name='红米 MAX 发布会',limit=2000,status=True,
    address='北京会展中心',start_time=datetime(2016,9,22,14,0,0))
    <Event: 红米 MAX 发布会>
    >>> Guest.objects.create(realname='andy',phone=13611001101,email=
    'andy@mail.com',sign=False,event_id=3)
    <Guest: andy>

需要说明的是， 表的 id 字段已经设置了自增， 所以， 该字段为空可以添加数据， 但在创建嘉宾时数据时
需要指定关联的发布会 id。 Event 表指定了 id=3， Guest 表指定 event_id=3， 所以嘉宾 andy 对应的是红米 MAX
发布会。

### 3.3.2、 查询数据

查询无疑是数据库表中使用频率最高的操作。

table.objects.get()方法用于从数据库表中取得一条匹配的结果， 返回一个对象， 如果记录不存在的话， 那
么它会报 DoesNotExist 类型错误。

通过 name='红米 MAX 发布会' 做为查询条件：

    ……
    >>> e1 = Event.objects.get(name='红米 MAX 发布会')
    >>> e1
    <Event: 红米 MAX 发布会>
    >>> e1.address
    '北京会展中心'
    >>> e1.start_time
    datetime.datetime(2016, 9, 22, 14, 0)
    >>>
    >>> Event.objects.get(name='红米 MAX 发布会').status
    True
    >>> Event.objects.get(name='红米 MAX 发布会').limit
    2000
    >>> Event.objects.get(name='发布会').address
    Traceback (most recent call last):
    File "<console>", line 1, in <module>
    File "H:\guest\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
        return getattr(self.get_queryset(), name)(*args, **kwargs)
    File "H:\guest\venv\lib\site-packages\django\db\models\query.py", line 417, in get
        self.model._meta.object_name
    sign.models.Event.DoesNotExist: Event matching query does not exist.

因为 name='发布会' 并没有完全匹配到发布会名称， 所以会抛出 DoesNotExist 异常， 但更多的时候希望
使用模糊查询。

table.objects.filter()方法是从数据库的取得匹配的结果， 返回一个对象列表， 如果记录不存在的话， 它会
返回[]。

    >>> e2 = Event.objects.filter(name__contains='发布会')
    >>> e2
    <QuerySet [<Event: 小米10发布会>, <Event: 红米 Pro 发布会>, <Event: 红米 MAX 发布会>]>

在 name 和 contains 之间用双下划线。 这里， contains 部分会被 Django 翻译成 LIKE 语句。

接下来， 通过嘉宾信息查询其关联的发布会信息。 查看 phone='13611001101' 这位嘉宾所参加的发布会信
息：

    ……
    >>> g1 = Guest.objects.get(phone='13611001101')
    >>> g1.event
    <Event: 红米 MAX 发布会>
    >>> g1.event.name
    '红米 MAX 发布会'
    >>> g1.event.address
    '北京会展中心'

### 3.3.3、 删除数据

查询 phone='13611001101' 的嘉宾， 通过 delete()方法删除。

    ……
    >>> g2 = Guest.objects.get(phone='13611001101')
    >>> g2.delete()
    (1, {'sign.Guest': 1})
    >>> Guest.objects.get(phone='13611001101').delete()
    (1, {'sign.Guest': 1})

### 3.3.4、 更新数据

查询 phone='13611001101' 的嘉宾， 更新 realname='andy2' 。

    >>> g3=Guest.objects.get(phone='13611001101')
    >>> g3.realname='andy2'
    >>> g3.save()
    >>> Guest.objects.select_for_update().filter(phone='13611001101').update(
    realname='andy')
    1

### 3.4 SQLite 管理工具

可视化的 SQL 工具可以方便我们管理数据库。 接下来会介绍一种款常用的 SQLite 管理工具

### 3.4.1、 SQLiteStudio

SQLiteStudio 是一款 SQLite 数据库可视化工具， 是使用 SQLite 数据库开发应用的必备软件， 软件无需安
装， 下载后解压即可使用， 很小巧但很好用， 绿色中文版本。 比起其它 SQLite 管理工具， 我喜欢用这个。 很
方便易用， 不用安装的单个可执行文件， 支持中文。

SQLiteStudio 是一个跨平台的 SQLite 数据库的管理工具， 采用 Tcl 语言开发。

下载地址： http://sqlitestudio.pl/

![Image](https://pic4.zhimg.com/80/v2-741ceb022c9dce14b089f974a845509d.png)


### 3.5 配置 MySQL

前面用的数据库是 Python 自带的 SQLite3， 这种数据库并不适用大型的项目。 除 SQLite3 之外， Django
还支持以下几种数据库：

- PostgreSQL (http://www.postgresql.org/)
- MySQL (http://www.mysql.com/)
- Oracle (http://www.oracle.com/)

本节以 MySQL 为例， 介绍 MySQL 的安装， 以及在 Django 中的配置。

### 3.5.1、 安装 MySQL

下载 MySQL： http://dev.mysql.com/downloads/mysql/

![Image](https://pic4.zhimg.com/80/v2-b56f359755e4639e4d5cdd5e52a761d4.png)

双击运行安装程序， 如图， 根据提示一步一步进行安装， 作者这里就不再详细介绍每一步的安装过程
了， 请参考其它 MySQL 安装手册。

进入 mysql

在 Windows 命令提示符下进入 MySQL。

    C:\Users\fnngj>mysql -u root -p
    Enter password: *****
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 8
    Server version: 8.0.20 MySQL Community Server - GPL

    Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql>

登录的用户名为 root ， 密码在安装 MySQL 的过程中设置， 如果没填写默认为空。

mysql 基本操作

查看库与表：

    mysql> show databases; #查看当前数据库下面的所有库
    +--------------------+
    | Database          |
    +--------------------+
    | information_schema |
    | mysql             |
    | performance_schema |
    | test              |
    +--------------------+
    4 rows in set (0.00 sec)
    mysql> use test; # 切换到 test 库
    Database changed
    mysql> show tables; # 查看 test 库下面的表
    Empty set (0.00 sec)

查看 mysql 端口号：

    mysql> show global variables like 'port';
    +---------------+-------+
    | Variable_name | Value |
    +---------------+-------+
    | port          | 3306 |
    +---------------+-------+
    1 row in set (0.00 sec)

创建数据库：

    mysql> CREATE DATABASE guest CHARACTER SET utf8;
    Query OK, 1 row affected (0.00 sec)

创建 guest 库， 用于我们 Django 的 guest 项目

### 3.5.2、 安装 PyMySQL

这里遇到小小的分歧， 如果读者使用的 Python2.x 版本， 那么连接 MySQL 数据库可以使用 MySQL-python。
但是， MySQL-python 只支持 Python2.x 版本， 并在 2014 年 1 月之后就不再更新了， 但这并不影响对该库的使
用。 目前 Django 默认使用的是该驱动。

下载地址： https://pypi.python.org/pypi/MySQL-python

而 且 如 果 读 者 使 用 的 操 作 系 统 是 Win 64 位 ， 还 需 要 单 独 查 找 安 装 64 位 版 本 的 安 装 包 ，
mysql-python-1.2.5.win-amd64-py2.7.exe。

而当前我们使用的是 Python3.x 版本的 Django， 所以这里推荐使用 PyMySQL 驱动。

下载地址： https://pypi.python.org/pypi/PyMySQL

PyMySQL 同样支持 pip 命令安装

    C:\Users\fnngj>python3 -m pip install PyMySQL

关于 PyMySQL 的使用， 简单的例子：

```python
# mysql_test.py

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,create_time) VALUES("alen", 18800110001, "alen@mail.com", 0, 1, NOW());'
        cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
    # Read a single record
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('18800110001',))
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()


```

connect() 建立数据库连接。

execute() 执行 SQL 语句。

close() 关闭数据连接。

### 3.5.3、 Django 配置 MySQL

那么 Django 如何链接 MySQL 数据库， 需要在.../guest/settings.py 文件中修改数据库相关配置。

```python
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'guest',
        'USER': 'root',
        'PASSWORD': '123456',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

```

配置信息从上到下依次是驱动（ENGINE） ， 主机地址（HOST） ， 端口号（PORT） ， 数据库（NAME），
登录用户名（USER） ， 登录密码（PASSWORD） 。

关于， sql_mode 的设置， 请参考 Django 文档。

https://docs.djangoproject.com/en/1.10/ref/databases/#mysql-sql-mode

注意： 切换了数据库后， 之前 Sqlite3 数据库里的数据并不能复制到 MySQL 中， 所以需要重新进行数据
库同步， 使数据模型重新在 MySQL 数据库中生成表。

    D:\pydj\guest>python3 manage.py migrate
    Traceback (most recent call last):
    File "H:\guest\venv\lib\site-packages\django\db\backends\mysql\base.py", line 16, in <module>
        import MySQLdb as Database
    ModuleNotFoundError: No module named 'MySQLdb'

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
    File "manage.py", line 21, in <module>
        main()
    File "manage.py", line 17, in main
        execute_from_command_line(sys.argv)
    File "H:\guest\venv\lib\site-packages\django\core\management\__init__.py", line 401, in execute_from_command_line
        utility.execute()
    File "H:\guest\venv\lib\site-packages\django\core\management\__init__.py", line 377, in execute
        django.setup()
    File "H:\guest\venv\lib\site-packages\django\__init__.py", line 24, in setup
        apps.populate(settings.INSTALLED_APPS)
    File "H:\guest\venv\lib\site-packages\django\apps\registry.py", line 114, in populate
        app_config.import_models()
    File "H:\guest\venv\lib\site-packages\django\apps\config.py", line 211, in import_models
        self.models_module = import_module(models_module_name)
    File "D:\Program Files\Python37\lib\importlib\__init__.py", line 127, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
    File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
    File "<frozen importlib._bootstrap>", line 983, in _find_and_load
    File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
    File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
    File "<frozen importlib._bootstrap_external>", line 728, in exec_module
    File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
    File "H:\guest\venv\lib\site-packages\django\contrib\auth\models.py", line 2, in <module>
        from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
    File "H:\guest\venv\lib\site-packages\django\contrib\auth\base_user.py", line 47, in <module>
        class AbstractBaseUser(models.Model):
    File "H:\guest\venv\lib\site-packages\django\db\models\base.py", line 121, in __new__
        new_class.add_to_class('_meta', Options(meta, app_label))
    File "H:\guest\venv\lib\site-packages\django\db\models\base.py", line 325, in add_to_class
        value.contribute_to_class(cls, name)
    File "H:\guest\venv\lib\site-packages\django\db\models\options.py", line 208, in contribute_to_class
        self.db_table = truncate_name(self.db_table, connection.ops.max_name_length())
    File "H:\guest\venv\lib\site-packages\django\db\__init__.py", line 28, in __getattr__
        return getattr(connections[DEFAULT_DB_ALIAS], item)
    File "H:\guest\venv\lib\site-packages\django\db\utils.py", line 207, in __getitem__
        backend = load_backend(db['ENGINE'])
    File "H:\guest\venv\lib\site-packages\django\db\utils.py", line 111, in load_backend
        return import_module('%s.base' % backend_name)
    File "D:\Program Files\Python37\lib\importlib\__init__.py", line 127, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
    File "H:\guest\venv\lib\site-packages\django\db\backends\mysql\base.py", line 21, in <module>
        ) from err
    django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
    Did you install mysqlclient?

出错了！ 这是因为 Django 在连接 MySQL 数据库时默认使用的是 MySQLdb 驱动， 然而我们没有安装该
驱动， 因为它并不支持 Python3， 我们现在安装的是 PyMySQL 驱动， 如何让当前的 Django 通过 PyMySQL 来
连接 MySQL 数据库呢？ 方法很简单。

在.../guest/__init__.py 目录下添加：

```python

import pymysql
pymysql.install_as_MySQLdb()
```

重新执行数据库同步报错

    D:\pydj\guest>python3 manage.py migrate
    Traceback (most recent call last):
    File "manage.py", line 21, in <module>
        main()
    File "manage.py", line 17, in main
        execute_from_command_line(sys.argv)
    File "H:\guest\venv\lib\site-packages\django\core\management\__init__.py", line 401, in execute_from_command_line
        utility.execute()
    File "H:\guest\venv\lib\site-packages\django\core\management\__init__.py", line 377, in execute
        django.setup()
    File "H:\guest\venv\lib\site-packages\django\__init__.py", line 24, in setup
        apps.populate(settings.INSTALLED_APPS)
    File "H:\guest\venv\lib\site-packages\django\apps\registry.py", line 114, in populate
        app_config.import_models()
    File "H:\guest\venv\lib\site-packages\django\apps\config.py", line 211, in import_models
        self.models_module = import_module(models_module_name)
    File "D:\Program Files\Python37\lib\importlib\__init__.py", line 127, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
    File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
    File "<frozen importlib._bootstrap>", line 983, in _find_and_load
    File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
    File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
    File "<frozen importlib._bootstrap_external>", line 728, in exec_module
    File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
    File "H:\guest\venv\lib\site-packages\django\contrib\auth\models.py", line 2, in <module>
        from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
    File "H:\guest\venv\lib\site-packages\django\contrib\auth\base_user.py", line 47, in <module>
        class AbstractBaseUser(models.Model):
    File "H:\guest\venv\lib\site-packages\django\db\models\base.py", line 121, in __new__
        new_class.add_to_class('_meta', Options(meta, app_label))
    File "H:\guest\venv\lib\site-packages\django\db\models\base.py", line 325, in add_to_class
        value.contribute_to_class(cls, name)
    File "H:\guest\venv\lib\site-packages\django\db\models\options.py", line 208, in contribute_to_class
        self.db_table = truncate_name(self.db_table, connection.ops.max_name_length())
    File "H:\guest\venv\lib\site-packages\django\db\__init__.py", line 28, in __getattr__
        return getattr(connections[DEFAULT_DB_ALIAS], item)
    File "H:\guest\venv\lib\site-packages\django\db\utils.py", line 207, in __getitem__
        backend = load_backend(db['ENGINE'])
    File "H:\guest\venv\lib\site-packages\django\db\utils.py", line 111, in load_backend
        return import_module('%s.base' % backend_name)
    File "D:\Program Files\Python37\lib\importlib\__init__.py", line 127, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
    File "H:\guest\venv\lib\site-packages\django\db\backends\mysql\base.py", line 37, in <module>
        raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
    django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.

报错是因为我使用的mysql数据库版本为：Server version: 8.0.20 MySQL Community Server - GPL，如果是5.7的版本就没有问题。
解决办法：

将文件H:\guest\venv\lib\site-packages\django\db\backends\mysql\base.py的36和37行注释掉

```python
# if version < (1, 3, 13):
#     raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```
重新执行数据库同步

    D:\pydj\guest>python3 manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions, sign
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying sessions.0001_initial... OK
    Applying sign.0001_initial... OK

另外， 因为更换了数据库， 所以， Admin 后台超级管理员账号（admin/admin123456） 也需要重新创建。

    D:\pydj\guest>python3 manage.py createsuperuser
    Username (leave blank to use 'fnngj'): admin #输入登录用户名
    Email address: admin@mail.com #输入用户邮箱
    Password: #输入登录密码
    Password (again): #再次输入用户密码
    Superuser created successfully.

### 3.5.4、 MySQL 管理工具

关于 MySQL 的管理工具很多， 与 IDE 工具的选择一样， 有很强的个人习惯问题。 最常用的应该是 Navicat
了， Navicat 是一个强大的 MySQL 数据库管理和开发工具。 如图 。

![Image](https://pic4.zhimg.com/80/v2-6b2910d5e39d271700da3db25d3b7bde.png)

另外， 再推荐一款笔者正在使用的 MySQL 数据库管理工具---SQLyog， 如图

![Image](https://pic4.zhimg.com/80/v2-ce2cf5adaf4f2297d4322e7b8d210616.png)

## 第四章 Django 模板

回顾当前开发进度。 当前已经开发好了登录模块， 并且数据库及表的设计已经完成， 那么， 本章的重点
将会开发发布会管理、 嘉宾管理页面。 虽然前面使用 Admin 后台来管理发布会和嘉宾数据非常方便， 然而，
它扩展起来非常困难， 所以， 我们需要自己开发管理页面。 最后， 最最重要就是需要开发一个嘉宾的签到页
面。 来吧！ 到了最有意思的阶段。

这一章将会涉及到不少前端代码， 我知道你照着书上敲大段的代码是颇为痛苦的事儿。 所以， 我已经将
整个项目的代码放到的 GitHub 上面： https://github.com/defnngj/guest

不过， 千万不要盲目的拷贝粘贴， 认真阅读本章， 理解代码为什么要这样写。

### 4.1 Django-bootstrap3

本章将使用 Bootstrap 前端框架结合 Django 来开发 Web 页面。

![Image](https://pic4.zhimg.com/80/v2-3ad69eafea66123d08e1e6e6695dd9a6.png)

什么是 Django-bootstrap3？

Django-bootstrap3 项目是将 BootStrap3（3 表示版本号） 集成到 Django 中， 作为 Django 的一个应用提供。
这样做的好处是在 Django 中用 bootstrap 会更加方便。

Django-bootstrap3 pypi 仓库地址： https://pypi.python.org/pypi/django-bootstrap3

1、 通过 Python 的 pip 命令安装：

    C:\pydj\guest>python3 -m pip install django-bootstrap3
    Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple                                                         
    Collecting django-bootstrap3                                                                                         
    Downloading https://pypi.tuna.tsinghua.edu.cn/packages/9b/88/bef0cbec3ded6b7fe98017a26cc5b9cbf87f9926b20a8ee58a049e
    404b84/django_bootstrap3-12.1.0-py3-none-any.whl (27 kB)                                                             
    Installing collected packages: django-bootstrap3                                                                     
    Successfully installed django-bootstrap3-12.1.0                                                  

2、 在.../guest/settings.py 文件中添加“bootstrap3” 应用。

```python
……
# Application definition
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'sign',
'bootstrap3',
] …
…
```

### 4.2 发布会管理

本小节将会开发发布会管理列表与发布会名称搜索。

### 4.2.1、 发布会列表

继续回到视图的开发中， 打开.../sign/views.py 文件， 修改 event_manage()视图函数。

```python
……
from sign.models import Event
……
# 发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request,"event_manage.html",{"user": username,
"events":event_list})
```

Event.objects.all() 用于查询所有发布会对象（ 数据） ， 通过 render()函数附加在 event_manage.html 页面
返回给客户端浏览器。

打开并编写.../templates/event_manage.html 页面。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% load bootstrap3 %}
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <title>Guest Manage</title>
</head>
<body role="document">
<!-- 导航栏 -->
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="/event_manage/">Guest Manage System</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">发布会</a></li>
                <li><a href="/guest_manage/">嘉宾</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">{{ user }}</a></li>
                <li><a href="/logout/">退出</a></li>
            </ul>
        </div>
    </div>
</nav>
<!-- 发布会列表 -->
<div class="row" style="padding-top: 80px;">
    <div class="col-md-6">
        <table class="table table-striped">
            <thead>
            <tr>
                <th>id</th>
                <th>名称</th>
                <th>状态</th>
                <th>地址</th>
                <th>时间</th>
            </tr>
            </thead>
            <tbody>
            {% for event in events %}
                <tr>
                    <td>{{ event.id }}</td>
                    <td>{{ event.name }}</td>
                    <td>{{ event.status }}</td>
                    <td>{{ event.address }}</td>
                    <td>{{ event.start_time }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>
</div>
</body>
</html>
```
对于 BootStrap 框架来说， 它主要通过 class 属性来设置 HTML 标签的样式。

{% load bootstrap3 %}

{% bootstrap_css %}

{% bootstrap_javascript %}

加载 Bootstrap3 应用， CSS 和 JavaScript 文件。 ｛ % %｝ 为 Django 的模板标签， Django 的模板语言将会
在该标签下编写。

<title>Guest Manage</title>

设置页面标题为 Guest Manage。

`<li class="active"><a href="#">发布会</a></li>`

`<li><a href="/guest_manage/">嘉宾</a></li>`

设置页面导航栏， class="active" 表示， 当前菜单处于选中状态。 href="/guest_manage/" 用于跳转到到嘉
宾管理页， 我们稍后完善该页面。

`<li><a href="#">{{ user }}</a></li>`

`<li><a href="/logout/">退出</a></li>`

{{ }} Django 的模板标签， 用于定义显示变量。 这里将会通过浏览器 sessionid 获取到对应的登录用户名，
并显示。 href="/logout/" 定义退出路径， 稍后完善该功能。

```html

 {% for event in events %}
    <tr>
        <td>{{ event.id }}</td>
        <td>{{ event.name }}</td>
        <td>{{ event.status }}</td>
        <td>{{ event.address }}</td>
        <td>{{ event.start_time }}</td>
    </tr>
{% endfor %}
```

Django 模板语言， 用于循环打印发布的 id、 name、 status、 address 和 start_time 等字段。 Django 模板语
言与 Python 有所不同。 for 语句需要有对应 endfor 来表示语句的结束， 同样， if 分支语句也需要 endif 来表示
语句的结束。

![Image](https://pic4.zhimg.com/80/v2-3cfb72f4798ad77774b52fbc737c5576.png)

如图， 发布会管理页面， 通过对 Django-bootstrap3 应用的使用， 可以非常轻松的创建出漂亮的网页。

### 4.2.2、 发布会搜索

对于列表管理来说， 搜索功能必不可少， 接下来开发针对发布会名称的搜索功能。

这一次， 先在.../templates/event_manage.html 页面上创建搜索表单。

```html
……
<!-- 导航栏 -->
……
<!--发布会搜索表单-->
<div class="page-header" style="padding-top: 60px;">
    <div id="navbar" class="navbar-collapse collapse">
        <form class="navbar-form" method="get" action="/search_name/">
            <div class="form-group">
                <input name="name" type="text" placeholder="名称" class="form-control">
            </div>
            <button type="submit" class="btn btn-success">搜索</button>
        </form>
    </div>
</div>

<!-- 发布会列表 -->
<div class="row">
……
```

查询表单和我们前面开发的登录表单一样。 所以这里不再做过多介绍。 不过需要注意的几个地方，
method="get" HTTP 请求方式； action="/search_name/" 搜索请求路径； name="name" 搜索输入框的 name 属性
值。

不要忘记在.../guest/urls.py 文件中添加搜索路径的路由。

```python
……
from sign import views
urlpatterns = [
……
path('search_name/', views.search_name),
]
```

打开.../sign/views.py 文件， 创建 search_name()视图函数。

```python
……
# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username,"events": event_list})

```

通过 GET 方法接收搜索关键字， 并通过模糊查询， 匹配发布会 name 字段， 然后把匹配到的发布会列表
返回到页面上。 查询功能如图

![Image](https://pic4.zhimg.com/80/v2-26b67163fdd6074bd93d8b33dbd0e883.png)

### 4.3 嘉宾管理

关于嘉宾管理页面的开发与发布会管理页面基本类似， 接下来继续和我一起完成这个页面吧！

### 4.3.1、 嘉宾列表

创建.../templates/guest_manage.html 页面。

```html
<!-- 导航栏 -->
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="/event_manage/">Guest Manage System</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
                <li><a href="/event_manage/">发布会</a></li>
                <li class="active"><a href="#">嘉宾</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">{{ user }}</a></li>
                <li><a href="/logout/">退出</a></li>
            </ul>
        </div>
    </div>
</nav>

<!-- 嘉宾列表 -->
<div class="row" style="padding-top: 80px;">
    <div class="col-md-6">
        <table class="table table-striped">
            <thead>
            <tr>
                <th>id</th>
                <th>名称</th>
                <th>手机</th>
                <th>Email</th>
                <th>签到</th>
                <th>发布会</th>
            </tr>
            </thead>
            <tbody>
            {% for guest in guests %}
                <tr>
                    <td>{{ guest.id }}</td>
                    <td>{{ guest.realname }}</td>
                    <td>{{ guest.phone }}</td>
                    <td>{{ guest.email }}</td>
                    <td>{{ guest.sign }}</td>
                    <td>{{ guest.event }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>
</div>
```

与 evevt_manage.html 页面结构基本相同。 不过， 读者依然需要注意两个地方。

`<li><a href="/event_manage/">发布会</a></li>`

`<li class="active"><a href="#">嘉宾</a></li>`

当前处理嘉宾管理页面， 所以， 设置嘉宾按钮的处于选中状态（class="active"） 。 为发布会按钮设置跳转
路径（href="/event_manage/"）

```html
{% for guest in guests %}
    <tr>
        <td>{{ guest.id }}</td>
        <td>{{ guest.realname }}</td>
        <td>{{ guest.phone }}</td>
        <td>{{ guest.email }}</td>
        <td>{{ guest.sign }}</td>
        <td>{{ guest.event }}</td>
    </tr>
{% endfor %}
```

通过 Django 模板语言的 for 语句循环读取嘉宾列表， 并显示 id、 realname、 phone、 email、 sign、 event
等字段。

在.../guest/urls.py 文件中添加嘉宾路径的路由。

```python
……
from sign import views
urlpatterns = [
……
path('guest_manage/', views.guest_manage),
]
```

打开.../sign/views.py 文件， 创建 guest_manage()视图函数。

```python
……
from sign.models import Event,Guest
……
# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html", {"user": username,"guests": guest_list})

```

嘉宾管理页面如图

![Image](https://pic4.zhimg.com/80/v2-5bf8ef75bd698cf8e1ef3d3fa8b084fa.png)

关于嘉宾管理页面的搜索功能， 这里不再介绍， 来吧！ 参考发布会管理页面上的搜索功能完成， 你可以
的。 接下来， 我们将开发另外一个常见的功能分页器。

### 4.3.2、 分页器

对于嘉宾管理页面来说， 特别需要一个分页功能， 一场大型的发布会可能需要几千条嘉宾信息， 如果将
所有的嘉宾信息不做分页的显示在页面上， 首先页面的打开速度会受到严重的影响， 其次， 页面一次显示几
千条甚至几万条数据并不方便查看。

Django 已经为我们准备好了 Paginator 分页类。 所以， 只需要调用它即可完成列表的分页功能。 分页功能
略为复杂， 首先进入 Django 的 shell 模式， 练习 Paginator 类的基本使用。

    D:\pydj\guest>python3 manage.py shell
    Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from django.core.paginator import Paginator # 导入 Paginator 类
    >>> from sign.models import Guest # Guest 下的所有表
    >>> guest_list = Guest.objects.all() # 查询 uest 表的所有数据
    >>> p = Paginator(guest_list,2) # 创建每页 2 条数据的分页器
    >>> p.count # 查看共多少条数据
    5>
    >> p.page_range #查看共分多少页（每页 2 条数据） 循环结果为 1， 2， 3（共 3 页）
    range(1, 4)
    >>>
    ##########第一页#############
    >>> page1 = p.page(1) # 获取第 1 页的数据
    >>> page1 # 当前第几页
    <Page 1 of 3>
    >>> page1.object_list # 当前页的对象
    [<Guest: andy>, <Guest: jack>]
    >>> page1 = p.page(1)
    >>> for p in page1: # 循环打印第 1 页嘉宾的 realname
    ... p.realname
    ...
    'andy'
    'jack'

    ##########第二页#############
    >>> page2 = p.page(2) # 获取第 2 页的数据
    >>> page2.start_index() # 本页的第一条数据
    3>
    >> page2.end_index() # 本页的最后一条数据
    4>
    >> page2.has_previous() # 是否有上一页
    True
    >>> page2.has_next() # 是否有下一页
    True
    >>> page2.previous_page_number() # 上一页是第几页
    1>
    >> page2.next_page_number() # 下一页是第几页
    3>
    >>
    ##########第三页#############
    >>> page3 = p.page(3) # 获取第 3 页的数据
    >>> page3.has_next() # 是否有下一页
    False
    >>> page3.has_previous() # 是否有上一页
    True
    >>> page3.has_other_pages() # 是否有其它页
    True
    >>> page3.previous_page_number() # 前一页是第几页
    2

通过对 Guest 表的练习， 现在已经学会了 Paginator 类的基本操作， 那么下面就来实现分页面吧！

打开.../sign/views.py 文件， 修改 guest_manage()视图函数。

```python
……
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
……
# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,"guests": contacts})
```

paginator = Paginator(guest_list, 2)

把查询出来的所有嘉宾列表 guest_list 放到 Paginator 类中， 划分每页显示 2 条数据。

page = request.GET.get('page')

通过 GET 请求得到当前要显示第几页的数据。

contacts = paginator.page(page)

获取第 page 页的数据。 如果当前没有页数， 抛 PageNotAnInteger 异常， 返回第一页的数据。 如果超出最
大页数的范围， 抛 EmptyPage 异常， 返回最后一页面的数据。

最终， 将得到的某一页数据返回到嘉宾管理页面上。

在.../templates/guest_manage.html 页面也需要添加分页器的代码。

```html
……
<!-- 嘉宾列表 -->
……
<!-- 列表分页器 -->
<div class="pagination">
<span class="step-links">
{% if guests.has_previous %}
    <a href="?page={{ guests.previous_page_number }}">previous</a>
{% endif %}
    <span class="current">
Page {{ guests.number }} of {{ guests.paginator.num_pages }}.
</span>
    {% if guests.has_next %}
        <a href="?page={{ guests.next_page_number }}">next</a>
    {% endif %}
</span>
</div>

```

![Image](https://pic4.zhimg.com/80/v2-3e4fc0e3f74fff083cf5471c89fa65c3.png)

最后， 如果读者开发的搜索功能， 不要忘记在搜索视图同样需要分页功能。

### 4.4 签到功能

既然是产品发布会签到系统， 怎么能没有签到页面和相关功能呢？ 继续开发签到功能。

### 4.4.1、 添加签到链接

对于签到功能页面来说， 它应该所属于某一场发布会， 所以， 在打开签到页面之前， 我们应知道这是针
对哪一场发布会的签到。 所以， 最好的方式是在发布列表中， 每一条发布会都提供一个“签到” 链接用来打
开对应的签到页面。

在.../templates/event_manage.html 页面， 增加签到列链接。

```html
……
<!-- 发布会列表 -->
……
<thead>
    <tr>
        <th>id</th>
        <th>名称</th>
        <th>状态</th>
        <th>地址</th>
        <th>时间</th>
       ** <th>签到</th>**
    </tr>
</thead>
<tbody>
    {% for event in events %}
        <tr>
            <td>{{ event.id }}</td>
            <td>{{ event.name }}</td>
            <td>{{ event.status }}</td>
            <td>{{ event.address }}</td>
            <td>{{ event.start_time }}</td>
           ** <td>
                <a href="/sign_index/{{ event.id }}/" target="{{ event.id }}_blank">sign</a>
            </td>**
        </tr>
    {% endfor %}
</tbody>
……
```

当点击 sign 链接时， 路径会默认跳转到“/sign_index/{{ event.id }}/” 路径。 其中{{ event.id }} 为发布会
的 id。 target="{{ event.id }}_blank" 属性表示链接在新窗口打开。

在.../guest/urls.py 文件中添加路径路由

```python
……
from sign import views
urlpatterns = [
……
path('sign_index/<int:event_id>/', views.sign_index),
]
```

此处与我们之前添加的路径在匹配方式上略有不同。

`sign_index/<int:event_id>/`配置二级目录， 发布会 id， 要求必须为数字。 而且匹配的数字， 将会作为 sign_index()
视图函数的参数。

### 4.4.2、 签到页面

打开.../sign/views.py 文件， 创建 sign_index()视图函数。

```python
from django.shortcuts import render, get_object_or_404
……
# 签到页面
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})
```

创建.../templates/sign_index.html 签到页面。

```html
……
<!-- 导航栏 -->
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">{{ event.name }}</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
                <li><a href="/event_manage/">发布会</a></li>
                <li><a href="/guest_manage/">嘉宾</a></li>
            </ul>
        </div>
    </div>
</nav>

<!-- 签到功能 -->
<div class="page-header" style="padding-top: 80px;">
    <div id="navbar" class="navbar-collapse collapse">
        <form class="navbar-form" method="post"
              action="/sign_index_action/{{ event.id }}/">
            <div class="form-group">
                <input name="phone" type="text" placeholder="输入手机号"
                       class="form-control">
            </div>
            <button type="submit" class="btn btn-success">签到</button>
        </form>
    </div>
</div>
……
```

`<a class="navbar-brand" href="#">{{ event.name }}</a>`

将页面标题设置为发布会名称。

`<li><a href="/event_manage/">发布会</a></li>`

`<li><a href="/guest_manage/">嘉宾</a></li>`

设置发布会与嘉宾导航链接。

`<form class="navbar-form" method="post" action="/sign_index_action/{{ event.id }}/">`

签到表单会通过 POST 请求提交到/sign_index_action/{{ event.id }}/ ， 二级目录会以发布会 id 替换。

签到页面， 如图

![Image](https://pic4.zhimg.com/80/v2-535c24ab9d9151217d5686038b16c29d.png)

### 4.4.3、 签到动作

继续开发签到功能， 接下来考虑， 当在签到输入框中输入手机号， 点击“签到” 按钮之后， 改动作要如
何处理？

首先， 打开.../guest/urls.py 文件， 添加签到路径的路由。

```python
……
from sign import views
urlpatterns = [
……
url(r'^sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action),
]
```

打开.../sign/views.py 文件， 创建 sign_index_action()视图函数。

```python
……
# 签到动作
@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone','')
    result = Guest.objects.filter(phone = phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,'hint': 'phone error.'})
    result = Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event,'hint': 'event id or phone error.'})
    result = Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,'hint': "user has sign in."})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event,'hint':'sign in success!','guest': result})
```

对于发布会的签到动作， 做了以下条件的判断。

首先， 查询 Guest 表判断用户输入的手机号是否存在， 如果不存在将提示用户“手机号为空或不存在” 。

然后， 通过手机和发布会 id 两个条件来查询 Guest 表， 如果结果为空将提示用户“该用户未参加此次发布会” 。

最后， 再通过手机号查询 Guest 表， 判断该手机号的签到状态是否为 1， 如果为 1， 表示已经签过到了，
返回用户“已签到” ， 否则， 将提示用户“签到成功！ ” ， 并返回签到用户的信息。

修改.../templates/sign_index.html 页面， 增加 sign_index_action()视图函数返回的提示信息的位置。

```html
……
<!-- 签到功能 -->
<div class="page-header" style="padding-top: 80px;">
    <div id="navbar" class="navbar-collapse collapse">
        <form class="navbar-form" method="post"
              action="/sign_index_action/{{ event.id }}/">
            <div class="form-group">
                <input name="phone" type="text" placeholder="输入手机号"
                       class="form-control">
            </div>
            <button type="submit" class="btn btn-success">签到</button>

            <font color="red">
                <br>{{ hint }}
                <br>{{ guest.realname }}
                <br>{{ guest.phone }}
            </font>
        </form>
    </div>
</div>
……
```

如果签到失败， 将会显示 {{ hint }}提示信息； 如果签到成功， 将会显示{{ hint }}提示信息和用户名称，
及手机号。 如图

![Image](https://pic4.zhimg.com/80/v2-03a7de4320640a00b8dd0cf95df202ba.png)

### 4.5 退出系统

之前留了一个坑， 在发布会管理页面和嘉宾管理页面的右上角有“退出” 按钮， 但我们一直没实现登录
的退出。 现在是时候该填补上它了。

打开.../urls.py 文件， 添加退出目录的路由。

```python
……
from sign import views
urlpatterns = [
……
path('logout/', views.logout),
]
```

打开.../sign/views.py 文件， 创建 logout()视图函数。

```python

……
# 退出登录
@login_required
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/index/')
    return response
```

Django 不单单为我们提供了方便的 auth.login()函数用于登录， 还为我们准备了 auth.logout()函数用于系统
的退出， 它可以帮我们清除掉浏览器保存的用户信息， 所以， 我们不用再考虑如何删除浏览器 cookie 等问题
了。

### 本章小节

本书用第二章到第五章的内容， 开发一个发布会签到系统。 当然， 真正投入使用， 还需要经历严格的测
试。 以及相关功能的完善。 如果读者对 Web 开发有足够的兴趣， 那么接下来相信你一定会将该系统做得更好。

接下来的本书将会把重点放到测试上面来， 如果， 你是一名软件开发人员， 可以重点跳到项目部署章节
继续学习， 如果你是一名软件测试人员， 那么我们的学习的重点才刚刚开始， 当然， 后面的内容同样也适用
于软件开发人员。
