---
bibliography: [./ref.bib]
---
摘要

随着我国经济社会的发展和人民生活水平的不断提高，城市垃圾的产生速度也在飞速增长，如何妥善处理和利用城市生活垃圾成为国家和地方政府部门的重要议题。垃圾桶作为居民生活垃圾与垃圾处理厂之间的接口，在垃圾回收中承担重要的角色。目前部分城市已在部分社区部署智能化的垃圾桶，取得了较好的效果。通过智能垃圾桶终端实时获取垃圾桶状态，可以极大地提高社区垃圾桶地清理和回收效率，提高管理便捷性。
本设计以STM32F103RET6单片机作为控制核心，加之温湿度传感器，称重传感器，桶满（红外）传感器等多种传感器和推杆等外设，实现了实时采集垃圾桶内部的状态信息，且可通过推杆控制桶盖的自动开启，构成了一个集状态监测和智能控制功能为一体的智能垃圾桶数据采集和控制终端。
终端系统通过传感器采集的数据暂存在单片机的内部RAM中，运行在安卓系统上的上位机系统通过Modbus协议与之通信以读取垃圾桶状态数据。上位机系统将垃圾桶状态数据可视化处理并以一定时间间隔向服务端上传，服务端根据通信协议解析数据，并将之存储在数据库。
数据库中存储的垃圾桶实时状态数据可以驱动多种应用，本设计平实现的“智慧城市垃圾桶信息化台”就是一种。平台将来自各垃圾桶的状态数据在地图上可视化，形成一个直观的垃圾桶状态监测系统，方便管理人员实时掌握垃圾桶状态。当有垃圾桶状态异常或功能故障时，平台还会主动发出警告提醒工作人员对其进行检查，大大提高了城市垃圾桶维护效率。

关键词：物联网，智慧城市，嵌入式系统，大数据

ABSTRACT

With the development of the economy and society and the continuous improvement of people’s living standards, the rate of urban waste generation is also rapidly increasing. How to properly handle and utilize urban domestic waste has become an important issue for national and local government departments. As the interface between the household garbage and the garbage treatment plant, the trash can plays an important role in the garbage collection process. At present, some cities have deployed intelligent trash cans in some communities and achieved good results. Obtaining real time status of the trash can through the smart trash can terminal can greatly improve the efficiency of cleaning and recycling the trash can in the community, and improve the management convenience. 
This design uses STM32F103RET6 microcontroller as the control core,  with temperature and humidity sensors, weighing sensors, full (infrared) sensors and other peripherals such as push rods, etc., to achieve real-time collection of status information inside the trash can. And the lid can be controlled be the push rod automaticly, make it an intelligent trash can data collection and control terminal integrating state monitoring and intell control functions.
The data collected by the terminal system through the sensor is temporarily stored in the internal RAM of the microcontroller, and the upper computer system running on the Android system communicates with it through the Modbus protocol to read the trash can status data. The upper computer system visualizes the status data of the trash can and uploads it to the server at a certain time interval. The server parses the data according to the communication protocol and stores it in the database. 
The real-time status data of the trash bin stored in the database can drive a variety of applications. The "Smart City Trash Bin Information Platform" implemented in this design is one of them.The platform visualizes the status data from each trash can on the map to form an intuitive trash can status monitoring system, which is convenient for managers to grasp the real-time status of the trash can. When there is an abnormal state or malfunction of the trash can, the platform will also take the initiative to issue a warning to remind the staff to inspect it, which greatly improves the maintenance efficiency of the urban trash can.  

KEY WORDS: Internet of Things, Smart City, Embedded Systems, Big Data


# 绪论

## 背景及意义

  生态环境与每个人都息息相关，它的好坏将不仅仅关乎动植物的生存，也会直接或间接地影响人类的身体健康[@kumar2016]。习近平总书记在党的十九大报告中指出：绿水青山就是金山银山，更是揭示了生态环境对于人类生产生活的重要作用。
随着经济的发展和人们生活水平的日益提高，人们对于工业产品的依赖也日益增强。为了满足人们的生活需要，大量的工厂开动，将自然资源生产成为各种商品。大规模的生产和大量的消费不仅消耗了自然资源，还产生了大量的废弃物，这些废弃物如不得到妥善的处理，势必对生态环境造成伤害。因此，垃圾回收处理是十分必要的，不仅能保护生态环境免遭破坏，让我们的生活环境更加美好，也实现了资源的再生利用，减少了自然资源的使用。
世界许多发达国家已经在几十年前实施了垃圾分类回收制度，且取得了明显的效果。中国政府自2002年起开始鼓励垃圾分类，但是未取得明显成果。2019年1月31日，上海市第十五届人大二次会议表决通过《上海市生活垃圾管理条例》，《条例》规定居民生活垃圾需分类投放。同时，北京，西安等多个城市均出台新政策鼓励居民积极参与垃圾分类回收，这表明中国的垃圾分类即将进入新的时代[@zotero-84]。


## 国内外研究现状

## 本文主要工作

## 论文组织方式