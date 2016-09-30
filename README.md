# maizi-downloader
麦子课程下载器

## 我为什么要写这么一个项目？

最近由朋友介绍一个不错的学习网站 － 麦子学院，我一看觉得视频质量挺高的，老师都是工作多年的老司机，应该经历过很多大型的项目，在某些点上（比如说怎么处理需求，大型网站的优化），他们思维方法和处理手法都能给我带来不少启发，唯一一个不足就是他们的语速都是比较慢，我一般都要开2倍速来听课，有的老师的语法快一点的就开1.5倍速，但每个人语速都是有差异的，有的老师开2倍速就太快，开1.5倍就觉得慢了，而且麦子学院的播放器偏偏是没有1.75倍的，只有1.5倍和2倍，那我就寻思能不能把视频下载到本地电脑上看，自己电脑上的播放器是任意调速度，那我就可以以自己喜欢的节奏听课了。

---
## 项目开始（坐稳，司机开车了~）

### 需求分析
本项目核心需求无非以下几种：

1. 爬取课程主页的*html*的内容  
2. 解析*html*获取相关的信息  
  1. 每节课的*url*  
  2. 每节课的名称  
3. 下载课程的视频  
  1. 新建一个文件夹来保存一个课程的所有视频  
  2. **下载视频**  
  3. 重命名（视频的文件名是不规则的）  
  
4.自动化处理  

### 选择工具
1. 爬取*html*虽然可以用`urllib`标准库，但是我选择`Requests`！
2. 解析DOM虽然可以用`re`正则表达式，但是我选择`BeautifulSoup`！
3. 其实拿到每节课的*url*还是要爬取解析的，但是我选择`you-get`！

### 迁移到python3
版本混用的门槛太高了，写了一个纯python3的版本，不推荐用fabfile的方法下载，我也就不删除了，留着纪念。

### 使用方法
先确认你安装好`python3.5`和以下第三方库：
- beautifulsoup4==4.5.1
- bs4==0.0.1
- requests==2.11.1
- you-get==0.4.555

你也可以把这个[requirements.txt](https://github.com/moling3650/maizi-downloader/blob/master/requirements.txt)下载了，然后cmd执行`pip install -r \path\to\requirements.txt`，最后下载好[maizi_downloader_v3.py](https://github.com/moling3650/maizi-downloader/)，就在cmd执行 `python maizi_downloader_v3.py [课程的序号]`，`课程的序号`可以接收一个参数，也可以是多个参数，也可以是间接参数，也可以是混合参数，用空格分隔。

example:
```
python maizi_downloader_v3.py 111
python maizi_downloader_v3.py 111 112 113 114 115
python maizi_downloader_v3.py 111~115
python maizi_downloader_v3.py 111~113 117 120~123
```

### 注重！！！
不支持虚拟环境*virtualenv*。
