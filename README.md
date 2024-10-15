# 新手教程
## 运行教程
首先在本项目打开终端

安装依赖:
`pip install -r requirements.txt`
输入命令:
`uvicorn main:app`

## 代码结构
### main.py
主程序入口，负责启动FastAPI应用，并设置一些全局的配置和中间件。
### cardRouter.py
定义了与Card相关的API路由，包括获取卡片、创建卡片、删除卡片和更新卡片。
### database.py
负责数据库的初始化和获取数据库会话。
### card.py
定义了Card模型，用于与数据库中的card表进行交互。
### cardDAO.py
定义了与Card模型相关的数据库操作函数，如获取卡片、创建卡片、删除卡片和更新卡片。
### cardSchemas.py
定义了与Card模型相关的数据验证和序列化模式，用于API请求和响应的数据结构。
### ReadMe.md
项目的说明文档，包括运行教程和代码结构。


## pull request的规范和约束(必看)
首先下载一个github desktop
https://desktop.github.com/download/
这是它的教程:
https://docs.github.com/zh/desktop/overview/getting-started-with-github-desktop
请严格按照步骤行事:
1. 打开 https://github.com/TFboy1/Time_Courtyard  点击Fork
2. 打开github desktop
3. 点击clone项目，选择Time_Courtyard
3. 点击current branch，点击new branch，输入你要写的模块的名字比如user_manager
3. 提交代码,点击commit
4. 推送分支,点击push,在右上角
5. 新建 Pull Request
6. 等待管理员审核
以上这些请仔细阅读教程之后操作
https://docs.github.com/zh/desktop/overview/getting-started-with-github-desktop

## 代码规范(必看)
1 变量采用驼峰命名法

2 理解模块
在本项目中，card_manager这个文件夹 就是一个模块
因此在pull request时，请确保你的代码符合以下规范:
例如，我现在编写user模块，那么请在modules文件夹下新建一个user文件夹，并在其中编写代码
不可以改动任何其他代码，仅仅可以增加自己的模块
不可以改动任何其他代码，仅仅可以增加自己的模块
不可以改动任何其他代码，仅仅可以增加自己的模块
不可以改动任何其他代码，仅仅可以增加自己的模块
不可以改动任何其他代码，仅仅可以增加自己的模块
非常重要，一个空格也不能动

3 然后
所有代码写完之后，使用命令为当前模块生成依赖项目录:
`python -m pip freeze > requirements.txt`
