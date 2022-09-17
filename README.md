# 说明

本软件为了大家学习linux或者不想下载大型翻译软件的时候的小工具，初始开发，很多bug，望各位使用者提出宝贵意见

# 使用教程

1.在dist目录里面有打包好的软件，main.exe是windows下的，main是linux下的

2.将对应文件放到想要的目录直接运行即可，q是退出，h是帮助

3.只能翻译单词或者各种语言的词语，句子暂时不支持。

# 使用技巧

（将软件名称改为trs（translate的缩写））

linux下可以使用tmux将终端分屏，然后将软件放入环境变量直接trs遇到不会的单词直接翻译，很nice![36543517254618548a9fe95feb1c6ed](C:\Users\ADMINI~1\AppData\Local\Temp\WeChat Files\36543517254618548a9fe95feb1c6ed.jpg)

windows下放入环境变量，然后直接win+r trs就可以运行，很nice

![image-20220917200226779](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220917200226779.png)

# 代码解读

由于自己写就懒得注释了，代码很简单就是一个爬虫，大家可以看看，注释的代码是调试的部分，比如json文件等等，myslq.py是一个打包好可以把你不会的单词存到数据库里面，也可以使用。