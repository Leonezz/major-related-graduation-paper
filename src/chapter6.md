# 总结与展望

## 总结

自新世纪以来，我国的经济社会都迎来了飞速发展，国家的城市化进程和建设水平也在不断提高。城市居民生活水平提高的同时，日常消费也变得多姿多彩。但是与消费水平共同提高的还有生活垃圾的产生速度，为了解决生活垃圾的大量产生带来的垃圾处理速度不足的问题，我国以及国际各发达国家纷纷采取垃圾分类回收政策来提高垃圾的回收处理效率和资源利用率。

城市社区垃圾桶作为居民生活垃圾的集中地和回收点，一直在城市生活垃圾回收中起着重要作用。当前，物联网、云计算等信息化技术的飞速发展和传感器、自动控制领域的成熟经验推动了城市智能垃圾桶的发展。为了实现对城市社区垃圾桶的统一管理和状态监控，本文设计并实现了一种用于城市社区垃圾回收点的物联网智能垃圾桶系统，实现了对城市社区垃圾桶的数字化管理。本文的主要研究内容如下：

#### 对城市智能垃圾桶的研究现状进行了调查研究，详细考察交接了目前国内外相关产品和设计和使用情况，结合实际部署场景，对系统的功能和架构进行设计。

#### 结合传感器和嵌入式技术对系统的数据采集和控制终端进行硬件电路和软件系统的设计和开发，并对系统电路板和嵌入式控制软件进行测试，证明设计的可用性。

#### 通过Android上位机软件的设计和开发实现用户交互，垃圾桶状态数据采集和上传以及用户积分激励功能，实现了系统的物联网终端，为服务器端系统的设计和开发打下基础。

#### 结合云计算、数据库等技术，实现了系统的服务端部分，实现了分布式终端数据的采集存储和统一管理。同时设计了垃圾桶数据请求接口，为上层数据应用系统的设计打下基础。结合接口设计，本文还设计实现了一个简单的智慧城市垃圾桶信息化平台，利用服务端数据对城市垃圾桶分布做可视化处理。

## 展望

本文结合使用传感器、嵌入式技术、物联网、Android软件开发、服务器、数据库和数据可视化技术设计开发了智慧城市物联网智能垃圾桶系统，系统采集的垃圾桶状态数据可以实现城市垃圾桶的数字化管理，用户信息以及积分系统则可以对垃圾分类行为进行激励，提升居民的垃圾分类意识和积极性，为城市生活垃圾分类助力。就系统功能设计来看，本设计提出的系统确实解决了一些问题，但是系统的部分细节功能设计还过于粗放和简单，还有很大的深入研究的空间，如：

#### 功能设计上，垃圾桶终端系统采集了垃圾重量和桶满状态信息，可以判断出垃圾桶的“假满”现象，但是无法对其进行有效处理。可以结合压缩系统实现垃圾假满后的自动压缩功能，提高垃圾桶的空间利用率。

#### 用户交互设计方面，目前的上位机系统设计较为简单，只实现了数据采集展示以及上传等重要功能，垃圾桶状态的展示UI设计还比较简陋，可以结合动画技术、数据可视化设计等进行深入的设计。

#### 服务端系统方面，系统采集到的数据仅仅进行了简单的归类和存储，可以结合大数据、人工智能技术对数据进行进一步的分析，提取出更具价值的信息。如，可以对某地各时间段用户垃圾投递量进行分析，为管理人员规划出最佳的垃圾回收时间；还可以结合地理位置信息进行分析，为管理单位规划出最优的垃圾桶部署地图。

#### 在数据应用层面，本系统预留了数据请求的接口，在实现上仅仅实现了一个简单的数据可视化系统，可以利用该接口请求数据设计更多维度的数据分析或用户指导系统。如，可以结合GPS定位技术为用户推荐出距离最近的可投递的垃圾桶并且规划路线；还可以结合温度传感器的数据计算一个地区的温度分布等。