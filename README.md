# MoewCave

_No English version because of my poor vocabulary, sorry._

## 关于项目

学习建设一个基于`Flask`的轻论坛的过程。

主要参考的是[新版The Flask Mega-Tutorial教程](https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh)，
代码~~剽窃~~借鉴了[flaskbb](https://github/com/flaskbb/flaskbb)、[university-bbs](https://github.com/weijiang1994/university-bbs/)代码。
在此非常感谢他们的付出以让我们得到了参考。

### 代码结构

根目录：

- `/meowcave`：应用本身
- `/migrations`：数据库的迁移脚本巴拉巴拉
- `/test_code`：为存放测试用的代码 ~~，但是根本没用上~~

应用内的每一个子项目：

- `__init__.py`：告诉系统这是一个可以被`import`ed 的库
- `forms.py`：存放表单
- `models.py`：存放其他地方会用到的模型
- `view.py`：视图函数，和`template`下的内容对接，其中蓝图在此注册

### 功能与期望

因为主要目的是学习而非搭建完整可用的项目，所以显的相当简陋。
如果存在问题，还敬请指出。

目前已经实现的功能：

- [x] 用户的注册
- [x] 用户的登录与登出
- [x] 发帖（在`UserPost`下，单纯的「动态」）

短期内期望的功能：

- [ ] 注册时加入输入邀请码的表单
- [ ] 邀请码的生成
  - [ ] 增加后台的第一个功能————**邀请码的相关设定**
- [ ] 用户个人信息的修改
- [ ] 进一步精简代码以及合理化项目结构

长期规划（`MeowCave`的内容）：

- Markdown的引入
- 评论系统
- 像样的后台
- 建立与个人动态相独立的「圈子-板块-贴子-楼」的内容结构
  - 内容的组织
  - 圈子的*管理员*————上任机制与权力
- 多媒体内容（图片、音频以及视频等）在网站上的引入
- 用户生产内容的版权声明以及「演绎」

正式部署相关（广义的）：

- MySQL
- 网络安全相关
- 前后端分离与API接口

## 运行项目

代码很烂，凑合者看。

下载下来，然后：

```
$ cd <File-location> # 使bash到达项目的位置
```

如果没有安装`virtualenv`（安装后跳过即可）：

```
$ pip install virtualenv
```

开一个虚拟环境：

```
$ virtualenv vvrenv # 后面的名字随便起，你甚至可以叫它为 ilovebingchiling
```

在进行一些简单的设定：

```
$ pip install -r requirements.txt
...
$ export FLASK_APP=meowcave
$ export FLASK_ENV=development # 不会有人用production来运行这玩意吧？不会吧
```

开始运行

```
flask run
```

~~然后疯狂报错~~
