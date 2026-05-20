     用SVC做特定人物AI配音 - 你奶奶都会的AI声音教程 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

用SVC做特定人物AI配音 - 你奶奶都会的AI声音教程
============================

原创 数字生命卡兹克 数字生命卡兹克 2023-10-12 20:39 天津

> 原文地址: [https://mp.weixin.qq.com/s/b01gfQa7SqL-xbEC0GXDIQ](https://mp.weixin.qq.com/s/b01gfQa7SqL-xbEC0GXDIQ)

前几天我又做了一个《流浪地球》的二创，其中台词配音用了李雪健老师的声音，很多人来问我，这个声音是怎么实现出来的。

其实几个月之前，我写过AI声音的几篇教程，不过这眨眼间，小半年过去了，现在的AI声音质量已经有了质的飞跃，体验也已经简单很多了，也属于你奶奶都会的级别了。

所以我想再写一篇教程，有手就行的带大家来训练一些特定人物的声音模型，这个东西我个人认为在一些影视、音乐和配音领域还是蛮有用的。  

先简单的说一下这个技术，SVC，你就把它简单的理解成一个特定人物声音的变成器，你自己先录一段音频，然后把这个音频扔给AI，AI就自动产出另一个人声音的音频了。  

比如我这个视频，我是自己先念了一段台词：  

然后用AI转成了李雪健老师的声音：

你们可以听一下，大概就是这样的效果。

训练这样的声音模型整体需要3步：

1.  准备声音数据集。
    
2.  在云上训练模型。
    
3.  在云上使用AI声音。
    
      
    

我们一步一步来，**不用发怵，我都能做出来，你也一定能**。  

  

**一. 准备数据集**

这个其实没有一个固定的方法，只要你能找到5~10分钟左右的干净的人声就行，我是直接从李雪健老师过往的影视作品中选了他的片段。  

然后扔到剪映里，把他的声音单独剪出来，最后导出的时候只导出WAV格式的音频就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbHwiaJswd5cGFWsgeCY5XoHXCSgTIXH3lKJkPYTvgtj2x0fpVia3EBJEg/640?wx_fmt=png)

理论上30分钟到2小时的数据集这个量肯定是最好的，但是你要是实在搞不到那么多，5分钟10分钟的迷你数据集拿去训练也不是不行，但是一定要干声，要干净，别有乱七八糟的混响声音之类的。  

这块我建议还是用神器UVR5去一下你的伴奏和混响。**要用的工具我都打好包了，对着后台私信"S"就行。**

UVR5分两步，第一步先去伴奏，把你的声音素材input进去，参数如下，直接Start，注意UVR5不要跟剪映同时开，会爆显存。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpfC1RvIRlO2P2GllicqxRJCH7d8fOrg131T9VSTuRjBVYVnK9sicT2fjlNkYEnz77V5cJs8hJmW8Iw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

成功了以后，我们去到我们设置的输出目录下，就能看到两个文件，有一个后缀带有Vocals的，再input到UVR5中，按如下参数设置，去掉混响。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpfC1RvIRlO2P2GllicqxRJCvHxBa4eYs2MEBmvXu8LDzXzpOQtCvCPzuwMa1AhuuWpiauOYkYOMV9A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

最后你还会得到一个XX\_Vocals\_Vocals的文件，就是一个非常干净的人声了。  

再使用整合包里的工具Audio Slicer（音频切分）将其剪裁成10秒左右的分段文件，因为你1个小时的文件直接拿去训练是必爆的，所以我们需要将他拆成10秒左右的1小段1小段。

打开整合包中的工具Slicer-gui。然后把Minimun Length那一项改成8000，把我们需要处理的音频直接拖到左边窗口，在右下角选择输出路径。**同时此处注意，任何路径和文件命名，都一定不要带有中文和特殊的比如空格之类的字符！！！**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpfC1RvIRlO2P2GllicqxRJCCiaCpTA8UzibU86v4ZoCQEvV8baZ7VeVibIoaN1bAAuIDYJqjCOqy27aA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

这样数据集就处理完毕了。接下来就是轻松愉快的训练。

  

**二. 在云上训练模型**

打开我们的老朋友AutoDL，https://www.autodl.com/

注册好账号以后，自己充值，10~30块就差不多了。然后我们点击控制台 - 容器实例，来到这个页面，再点击租用新实例（实例你可理解为就是一台电脑的意思）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbd5bcHwTctRZFq0y5m1iaNyeibM2qib2k4LFBMOhHmvbrre8qSIM9WxeLg/640?wx_fmt=png)

直接选北京C区，V100-32G，在下面的社区镜像中搜so-vits，选这个**svc-4.1，V10版本的。**  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbGoygZnN8PJOon2ibhvAgNEveLNExHFIu5yYu7fotFTkdIYqb8cNHAUw/640?wx_fmt=png)

然后创建，第一次稍微等一会，毕竟这个镜像20个G，有点大，下载还是要一段时间的。  

等好了后，直接点这个JupyterLab。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbLYaaxfexbUVVgAe6boyXBrysyeGxHiav5XD6tfPK4W7DmxRHSYJE7GQ/640?wx_fmt=png)

进去以后，点一下左上角这个。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbQ1RMuJqQKBv9zOBia7L07o48DKWeHR1NQCx7hzWXLo3XvzFUTDAt24w/640?wx_fmt=png)

再然后里面的东西其实都很详细了，你跟着教程点点点，真的就是有手就行。前面那一大堆玩意不用看，直接往下拉。找到这个#移动项目文件夹，点顶上的三角播放。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbC0C2sZiboqBUGzNBJSqzCI93FQTdNmibw9BUuTrGb0QFKW5O35PFGk1w/640?wx_fmt=png)

等右上角这个实心圆变成空心圆，就说明这一步跑好了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbIQISz9bzkCiachllgSD0gQvibVxbQvGPE3jnUOLshFxqK7ticnHibVenEQ/640?wx_fmt=png)

然后再运行进入项目文件夹那个代码块。  

这块点完要小停一下，我们需要把我们的数据集传上去。  

在左边的文件管理器里，进入autodl-tmp/so-vits-svc/dataset\_raw，先新建一个文件夹，比如我就新建了一个叫lixuejian的。

再把你刚才切出来的数据集文件直接全部都拖进去就行。  

这样数据集就传好了，再运行这个代码块。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbdTB7wuIaZx0NgQ8AnG5OsAAQQYDKJQG7fmZ3j2pBz1RmIatqdyjgAg/640?wx_fmt=png)

1s就运行完了，运行完之后，在下面**选vec768l12编码器**，再运行代码块。下面那几个就不用管了，这个编码器是6选1。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbgnAAuzKptcdS3YeJV1LD8CcEUsEuGWIVGRLuljPxoE7p6BNAFF5JaQ/640?wx_fmt=png)

运行完后下滑，找到f0预测器。删掉第二条rmvpe预测器前面的那个#号，**！感叹号不要删，只删这一个#符号就行**，这其实也是个6选1。然后一样点左上角三角按钮运行代码块。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbYuHxn54ZmocflH4JNkic4icGfITF7Cn0qQ0yYhZGYCV5GvsrJdFdeXtg/640?wx_fmt=png)

完事了以后，下面的其他的代码块先不用管，去到左边文件管理器，按这个路径autodl-tmp/so-vits-svc/configs，找到config.json文件。

右键，打开方式-Editor。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbBo7ZAicfdKAWLwBdXz2xKY3h7r1icQSEsxSOyMiaBJTgkPMNiaxnHKu2ug/640?wx_fmt=png)

然后改几个参数。  

**"batch\_size": 6改成12；**

**"learning\_rate": 0.0001改成0.0002；**

 "keep\_ckpts": 3改成10；（从最多保存3个模型变成最多保存10个模型）

改完以后，Ctrl+S保存。关掉。

保持在当前在svc这个目录下，点右上角的加号，新建1个终端。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbX2Cs0iaxH7qKzrc1DibSqlVv3va88GSUvECRMGyhVlhiasXLxVlBt6ATg/640?wx_fmt=png)

在终端里输入我这块的代码

    python train.py -c configs/config.json -m 44k

训练就正式开始了。你一步一步按我的来，基本不会有任何报错。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbYT64yTAueIkiccZClQa9w2wRlWt1shzZTj7TNlENwMXBjicjISlgp8Mg/640?wx_fmt=png)

  

**三. 在云上使用AI声音。**

模型训练开始后会有步数提示，每训练800步会保存一个模型，基本3000步左右的那个模型你就可以去听听了。

可以稍微注意一下一个叫loss（损失值）的参数，越低越好，一般是在28左右，如果给你保存的那个是在22啥的，那就是还不错的模型了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbcgv2xkGhGz9vmoN1QeB74u9g6udeh0IbSogbPCia4L5BOlkYeu3GEFg/640?wx_fmt=png)

模型保存在autodl-tmp/so-vits-svc/logs/44k这个目录下，这些D和G开头的就是。后面的编号一般都是800倍数，比如800、1600、2400等等。我从别的地方直接拽了一个已经训练好的模型当示意。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbtwKGNULEskFEBMJzIaZjQIEUWIhV3icC2AyRulu2xLF4JrHtOZ1Wpyg/640?wx_fmt=png)

你要是觉得模型质量不错，可以下载到本地，一样，都通用。

然后就是推理了。  

还是保持在当前在svc这个目录下，再新建一个终端，输入我这个代码  

    python app.py

 你就能看到多出来两个链接  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbrwEOFfbVTC716uJ88iafj3AVnic0ZbrBpLnVVRs53pEEGngvbCOGRrvw/640?wx_fmt=png)

把第二个复制粘贴到你的网页。  

就能看到WebUI了。  

然后把这两个下拉选项选成你的模型就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbibt7pdtR2LDkY0ibc1ENBpwBQEyibW1fObuW2zibfONxiaHIcbF6rIRCxXg/640?wx_fmt=png)

每几秒钟，你就能看到这么一条提示，你的模型被加载了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrb9ia8ato7kKE03GJicdR5OiaxkwjsJAzgSgDSZ1ibQXe9wBsR3m8jBH69Zg/640?wx_fmt=png)

再然后，传上你自己的音频，勾选上自动F0预测，F0预测器选择之前的rmvpe，愉快的点击音频转换就可以啦~

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMkWC60ibJ5Aq2XjgsGUvrbDvbGfqkJnDeLdfgibNyVPOdXSQxM4579V1nsv2LbBp0dib7LkWG6IVjg/640?wx_fmt=png)

得益于V100的算力和大显存，2分钟的音频都不会爆，直接推理就行。大概十几秒后，就OK啦！  

接下来，你就自己去见证奇迹吧哈哈。  

  

**写在最后**

从2月到5月，从5月到10月，不知不觉，我已经写了8个月了。

时间真如老狗，跑的真特么让人追不上。  

AI的进化速度和新工具的出现速度，也让我这种普通人难以企及，别说学懂研究透，我耗尽了我所有的时间，能勉强跟上它的变迁，我已经是觉得非常艰辛了。

前一段时间看了稚晖君的视频，我真的挺感慨。人跟人的学习能力实在是差距太大太大了。

那种神一样的学习能力和知识海，我可能这一生都无法企及。

而在AIGC领域，我更不是什么大牛，在真正的大佬面前，我就是一个很小的小卡乐咪。  

但是看完他的视频，我也突然明白了自己的定位。

我就是AI世界的一个小小的门童，用各种稀奇古怪的作品和奶奶都会的教程，让没见过这个世界的人，看一眼这个世界的玄妙。

如果能引领他们走进AI的殿堂，那我这个门童的使命，也就真正达成了。

人嘛，总是要给自己找点价值，不是嘛。  

现在，我找到了。

**以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，并给我个星标⭐～感恩。**

  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言