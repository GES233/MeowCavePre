# MoewCavePre

_No English version because of my poor vocabulary, sorry._

## 关于项目

学习建设一个基于`Flask`的轻论坛的过程。

`MeowCave`是在本人关于社群的一个想法催生（但没有生）的产物。

在写代码的过程中主要参考的是[新版The Flask Mega-Tutorial教程](https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh)，
部分代码或组织结构~~剽窃~~借鉴了[flaskbb](https://github.com/flaskbb/flaskbb)、[university-bbs](https://github.com/weijiang1994/university-bbs/)等项目。
在此非常感谢他们的成果让我们这些萌新在学习过程中得到了参考。

### 代码结构

根目录：

- `/meowcave`：应用本身
- `/migrations`：数据库的迁移脚本巴拉巴拉
- `/test_code`：为存放测试用的代码 ~~，但是根本没用上~~

应用内的每一个子项目（现有的是`auth`以及`user`）：

- `__init__.py`：告诉系统这是一个可以被`import`ed 的库
- `forms.py`：存放表单
- `models.py`：存放其他地方会用到的模型
- `view.py`：视图函数，和`template`下的内容对接，其中蓝图在此注册

### 功能与期望

因为主要目的是学习而非搭建完整可用的项目，所以显得相当简陋。
如果存在问题或硬伤，还敬请指出。

目前已经实现的功能：

- [x] 用户的注册
- [x] 用户的登录与登出
- [x] 发帖（在`UserPost`下，单纯的「动态」）
- [x] 注册时加入输入邀请码的表单
  - [x] 已登录用户的**邀请**界面
  - [x] 邀请码的生成

短期内期望的功能：

- [ ] 评论的显示与回复
  - [ ] 通过嵌套集实现树形结构
- [ ] 更灵活的邀请码设定
  - [ ] 更多的设置与定期失效
  - [ ] 增加后台的第一个功能————**邀请码的相关设定**（例如格式与有效期之类的）
- [ ] 用户个人信息
  - [ ] 修改以及改变形式（隐藏巴拉巴拉）
  - [ ] 导出
  - [ ] 删除
- [ ] 进一步精简代码、增加可读性以及合理化项目组织

长期规划（主要是`MeowCave`的内容，但是严格意义上来讲依旧属于玩具）：

- Markdown的引入
- 完整的评论系统
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
$ virtualenv vvrenv # 后面的名字随便起，你甚至可以叫它为`ilovebingchiling`
```

再进行一些简单的设定：

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
