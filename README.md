# Python Rotaeno Stabilizer

*Read this in [English](README_EN.md)*

![Python Rotaeno Stabilizer](images/stable.png)

这是一个基于Python的Rotaeno录屏稳定脚本，原理和Rotaeno官方提供的Adobe After Effects脚本一样，是基于直播模式下录屏画面四个角的颜色来旋转帧，从而达到稳定视频画面的目的。

## 功能特点

- 无需安装Adobe After Effects，一行命令即可渲染完成
- 支持批量处理视频

## 安装

1. 下载项目代码：
```shell
git clone https://github.com/Lawrenceeeeeeee/python_rotaeno_stabilizer.git
```
或者直接在本仓库界面点击Download ZIP下载然后解压

2. 安装依赖：
```shell
# 切换到脚本所在目录
cd python_rotaeno_stabilizer
pip install -r requirements.txt
```

## 使用方法

0. **注意！！！** 录屏前请在Rotaeno的设置中开启"直播模式"，开启后屏幕的四个角将会出现记录设备旋转角的色块。

1. 将待处理的视频放在`videos`目录下

2. 启动项目：
```shell
python main.py
```

3. 在`output`文件夹找渲染完成的视频

## 已知问题
- 尽管渲染后的视频帧数和帧率和原视频相同，但视频时长仍有差异，目前暂时无法解决，因此本项目生成的视频暂时没有音频，只能在剪辑软件里进行拉伸和音画同步校准。如果您有解决方案，欢迎fork本项目并提交您的修改。

## 联系作者
请在我的[Bilibili账号](https://space.bilibili.com/143784401)下私信我