# Jarvis #
 
&#8195;&#8195;“贾维斯”是钢铁侠里的智能AI管家名字，我制作监控小车的目的是创造一个能够帮助主人在家值守的“管家”。它能自动巡逻，记录并及时上报异常状况。也能有主人控制小车的行驶，拥有绝对的控制权及无限的可玩性。

## 小车具备的功能 ##
- [x] 1.远程监控，镜头可调节角度。
- [x] 2.小车可远程控制行驶。
- [x] 3.循环录像，截图照片。
- [ ] 4.无线充电。
- [ ] 5.电机的转速检测及控制。
- [ ] 6.传感器配置（距离、温湿度、光照度、烟雾）
- [ ] 7.外壳设计，底盘设计（使用3D打印）
- [ ] 8.AI控制巡逻家庭。


## 实现方法 ##
### 1. 安装树莓派 ###
  自行百度即可。

### 2. 小车的控制 ###
1. 小车底层硬件的控制使用python库的RPi.GPIO，代码很简单。  
2. 为了实现远程的功能，使用了 bottle 这个轻量级的python web框架, 可以适配各种web服务器。  
3. 网页借用bootstrap快速设计出好看的界面。  
 
### 3. 摄像头安装 ###
1. 视频的传输使用MJPG-streamer，它是是一个优秀的开源project，延时极低，最多0.7s。（千万别用motion，延时极高，至少5s）。  
2. 我使用的是Raspberry Pi Camera，还需要解决V4L driver不支持的问题。

### 4. 开机自启动 ###
1. 修改/etc/rc.local文件，在exit 0 前加上  
`# start vehicle service`  
`python /home/pi/vehicle/index.py &`  
`# start camera service`  
`/home/pi/mjpg-streamer/startCamera.sh`



## 参考文献 ##
[Python 3 教程](https://www.runoob.com/python3/python3-tutorial.html "Python 3 教程")  
[树莓派GPIO控制](https://blog.csdn.net/chentuo2000/article/details/81051645 "树莓派GPIO控制")   
[树莓派上MJPG-streamer的安装过程](http://shumeipai.nxez.com/2017/05/14/raspberry-pi-mjpg-streamer-installation.html "树莓派上MJPG-streamer的安装过程")  
[树莓派小车-WEB按键控制](https://www.ncnynl.com/archives/201609/834.html)
[简单WiFi控制小车系统（树莓派＋python＋web控制界面)](https://blog.csdn.net/qq_41923622/article/details/85850780)
