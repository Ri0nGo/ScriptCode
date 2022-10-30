
# 1. python 环境配置


## 1.1 Windows 环境安装

去官网下载直接安装即可，推荐去 pc.qq.com 下载


## 1.2 Linux 环境安装


### （1）编译安装

**下载linux版本的python文件**

以下为在 Unix & Linux 平台上安装 Python 的简单步骤：

- 打开 WEB 浏览器访问 [https://www.python.org/downloads/source/](https://www.python.org/downloads/source/)
- 选择适用于 Unix/Linux 的源码压缩包。
- 下载及解压压缩包 `Python-3.x.x.tgz`，`3.x.x`为你下载的对应版本号。
- 如果你需要自定义一些选项修改 Modules/Setup

以 Python3.8.5 版本为例：

![](https://atts.w3cschool.cn/attachments/image/20200918/1600394980732776.png#alt=Python3%E5%AE%89%E8%A3%85%E5%8C%85%E4%B8%8B%E8%BD%BDlinux%2FUnix%E7%89%88%E6%9C%AC)

```
# tar -zxvf Python-3.8.5.tgz
# cd Python-3.8.5
# ./configure
# make && make install
```

检查 Python3 是否正常可用：

```
# python3 -V
Python 3.8.5
```

**注意：**

如果出现报错情况：

- 
Q1：`configure: error: no acceptable C compiler found in $PATH`
<br />表示没有gcc环境，此时我们安装gcc环境即可
<br />`yum install gcc-c++`

- 
Q2：`-bash: make: command not found`
<br />表示没有make这个命令，我们使用yum安装即可
<br />`yum install make`

- 
Q3：`可能会存在依赖问题`
```
yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel gcc gcc-c++  openssl-devel libffi-devel python-devel mariadb-devel
```



**设置软连接**

因为有的Linux默认自带的是python2的环境，我们安装python3的环境需要区别开。

```
# 更改/usr/bin/python链接
  ln -s /usr/local/bin/python3.8 /usr/bin/python3
  ln -s /usr/local/bin/pip3.8 /usr/bin/pip3
```


### （2）yum 安装

```
yum install python3.8
```


# 2. 虚拟环境配置


## 2.1 虚拟环境介绍

之前我们安装python第三方库时，都是直接通过pip install xx的方式进行安装的，这样会使第三方库直接安装到Python系统环境中，同时默认安装的都是最新版本的第三方库

这样安装会存在一个问题：<br />
如果用Django 1.10.x开发了一个网站，同时有一个用Django 0.9开发的旧项目需要维护，但是Django 1.10不再兼容Django 0.9的一些语法。这时候就会碰到一个问题，如何在系统环境中同时拥有Django 1.10和Django 0.9两套不同的环境呢？

解决方案：<br />
我们就可以通过安装虚拟环境来解决这个问题，创建多个虚拟环境实现环境拆分，每个虚拟环境安装不同版本的库，从而满足不同的需求，各个虚拟环境之间相互独立、不对其它环境产生影响

**venv 虚拟环境工具**

官方推荐的工具，python3.4之后，默认自带的。

**virtualenv 虚拟环境工具**

以前的虚拟环境工具，python3.4之前官方推荐的工具，虚拟pip安装

**virutalenvwrapper 虚拟环境工具**

- 
Windows下
<br />`pip install virtualenvwrapper-win`

- 
Linux 下
<br />`pip3 install virtualenvwrapper`
<br />配置 .bashrc 文件
```shell
# 1.打开文件
vim ~/.bashrc

# 2.添加内容
VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.8		# 设置python解释器环境路径
export WORKON_HOME=$HOME/.virtualenvs					# 创建的虚拟环境所在那个目录下
source /usr/local/bin/virtualenvwrapper.sh				# 执行文件
```

<br />退出vim后，执行 `source ~/.bashrc` 。如下表示成功
<br />![image-20210805200828826](Z:\Study Note\Typora笔记图库\image-20210805200828826-1640259992558.png)

- 
使用
| **操作** | **命令** |
| :---: | :---: |
| **切换到摸个虚拟环境** | `workon [virutalenv name]` |
| **退出虚拟环境** | `deactivate` |
| **列出所有虚拟环境** | `lsvirtualenv` = `workon` |
| **删除某个虚拟环境** | `rmvirtualenv [virutalenv name]` |
| **指定python解释器** | `mkvirtualenv -p python3.8 test` |
| **创建虚拟环境** | `mkvirtualenv env_name` |



- 
指定创建虚拟环境的根目录
<br />在系统变量中创建 `WORKON_HOME` 然后指定目录，记得重新打开cmd窗口，输入 `mkvirtualenv Test_env`
<br />![image-20210806001712114](Z:\Study Note\Typora笔记图库\image-20210806001712114-1640259985670.png)


---


# 3. pip

pip 是一个python包管理工具，可以对python的包进行下载，删除等。pip是安装python解释器后自带的。

**使用**

- `pip install`

   - `pip install django`
   - `pip install django==3.1.0 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com` 一次性使用pip源
- `pip list`
- `pip remove`
- `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`     永久设置pip源
