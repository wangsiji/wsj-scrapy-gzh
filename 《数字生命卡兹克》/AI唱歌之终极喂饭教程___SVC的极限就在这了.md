     AI唱歌之终极喂饭教程 - SVC的极限就在这了 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI唱歌之终极喂饭教程 - SVC的极限就在这了
========================

原创 数字生命卡兹克 数字生命卡兹克 2024-01-21 17:36 天津

> 原文地址: [https://mp.weixin.qq.com/s/fuftCdAFORXg-pztBsj4CQ](https://mp.weixin.qq.com/s/fuftCdAFORXg-pztBsj4CQ)

最近感觉AI文本、AI绘图、AI视频、AI 3D都没啥惊喜的项目了。

于是我又开始研究起了AI声音。  

前几天刚发了一个[中文声音克隆的TTS项目 - BertVits2](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647661122&idx=1&sn=3aae8eb822de159b97ad6d321df96b4c&chksm=f007c615c7704f03cc45af89e3f2c9354eb5de5d34c92a2bc436f04c395781b991e60a54226b&scene=21#wechat_redirect)

然后昨天又看到群里好朋友一直在问用SVC做AI唱歌的事，但是没人理，那怎么行，所以我就来了，英雄登场。  

这篇文章，为我的好朋友而写。

正好，离上次写SVC的教程，也快过了整整8个月的时间了，有兴趣想考古的可以去看看，虽然它已经没啥蛋用了：

[我把我的声音训练成了AI模型，并让它唱了一首歌...（附超全面教程，你奶奶看了都会用）](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647658355&idx=1&sn=0b1cec27677a8250585d43e0e69893a1&chksm=f007d324c7705a3296cf9bc19079e5f8378c0a183a5dc3c6e8db5228b839ca552459930efd39&scene=21#wechat_redirect)

当时还有很多问题，比如SVC自己的版本，高音部分很容易哑音、电流有点严重、音色不好、咬字不好等一堆问题。

而我的教程里，更是有很多错误，比如数据集的处理、人声分离的处理等等。

**AI一天，人间一年。**  

所以到了今天，我也打算再摸一下SVC效果的极限，写一个SVC的超详细的教程，让大家有手就行，不用任何修音，都能做出目前最好的AI唱歌的效果。

先给大家听一下，我把我的声音训练成了模型后，唱《模特》和《王妃》的效果。

这首歌直接模型直出，没有任何后期没有任何修音，具体什么水平，各位看官可以自己评判。

话不多说，教程开始。  

整体分为4步。  

1.  数据集的准备与处理。
    
2.  主模型的训练。
    
3.  最终推理与合成。
    
4.  保存模型下次使用。  
    

  

每一步我都会详细的说明，把我趟过的所有坑，一一写清楚，那毕竟，都是血和泪。

OK，开始吧。

  

 **一. 数据集的准备与处理** 

我一直说的一句话是：AI声音，90%的效果都是由数据集决定的。

所以，数据集的好坏，跟你最后的效果，呈绝对的正比。  

这里我多说一句，也是我之前教程的错误：  

**正常说话数据和唱歌数据，绝对绝对绝对不要混用！**  

你要那种正常说话比如念台词的SVC模型，你就传1个小时说话的干声。

你要是做AI唱歌的SVC，你就传1个小时覆盖了低中高音域的唱歌的干声。

不要混用，效果很差！  

同时，录音的时候，绝对要找个安静的地方，最好是类似录音室、直播间这种有吸音棉的地方，因为墙壁会反弹声音，会让声音有一点点混响的感觉。

收音的设备一定要好一点，用耳机或者麦，别对着手机就唱了。  

音域一定要广，建议唱个4、5首超高音的歌，比如死了都要爱之类的，可以跑调，无所谓，你拼命唱上去就行了。反正只要你录一次，坚持一下，很快就完事。

录完了以后，可以再扔到剪映里面优化一下。把响度统一、人声美化（开到50）、音频降噪全勾上。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqTOHFpHNlyBouZdgVBj9b8da8eOY0V8YpqlF1dWic12RvY5mycoeJ7K4666gTdVrSl6F9DeKibKFqA/640?wx_fmt=png&from=appmsg)

你的一手数据集就算完事了。

接下来是切分数据集。因为你直接扔1小时的数据集直接拿去训练，显存必爆，所以我们得做一个切分。这里还是推荐使用Audio Slicer（音频切分）将其剪裁成10秒~20秒左右的分段文件，你可以对着我公众号回复"SVC2024"，就有Audio Slicer的下载链接了。

我们把Audio Slicer下载下来，解压后打开Slicer-gui。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpfC1RvIRlO2P2GllicqxRJCjRTqia1DFicLwJMMy3x3w38Xjn9RYNlibZjJYnPDicAgQjRwJoauBicib0yA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

然后把Minimun Length那一项改成8000，把我们需要处理的音频直接拖到左边窗口，在右下角选择输出路径。

**同时此处注意，任何路径和文件命名，都不要带有中文和特殊的比如空格之类的字符！！！**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSGNZu46lhHXtKqU92JHSkeAIzhD6uEbkiaCwT2xGHIqYzJXCPBQkJmxA/640?wx_fmt=png&from=appmsg)

扔进去以后，我们直接点最右下角的Start。速度非常块，十几秒就切割完了。我们去我们选择的输出路径就能看到我们的文件。

然后我们选择时长排序，把低于2秒的，超过25秒的都给删了。

至此，前期的数据集就算是处理完毕了~

  

 **二. 主模型的训练** 

有了优质的数据集之后，我们正式开始模型的训练。

打开国际炼丹场AutoDL：https://www.autodl.com/home

没注册的自己注册去，我就不管了。  

在租卡页面，租一台北京C区的V100 32G。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSr0eUfboGt1kGwCaBD3caLC3CHIJFpxRog4e6bAESKbxuGhMQhZ1StQ/640?wx_fmt=png&from=appmsg)

然后去下面的镜像tab，在社区镜像中，搜so-vits-svc-4.1。在弹出来的搜索联想框中，选用v12版本，在此文发出后，镜像依然可能会持续升级，如果在你使用的时候，出现了比v12还要高的版本，请使用你能看到的最高的版本。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSkVuYVqw2RlnFF7Ee3O6m6UmYYuf7JYYFTZXCBzQ0hQticGhDCqGwx1w/640?wx_fmt=png&from=appmsg)

都完事后，点立即创建。  

你就会看到你的云机器在创建过程了，第一次创建拉取云上的镜像时间会久一点点，多等等就好。

当机器状态变成运行中的时候，点JupyterLab，进入操作系统。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSrmdLC3qqH7Um4UwmIOJtggxzyFn0ZgvGCPu6YibCLRZCgPq08lSibE2g/640?wx_fmt=png&from=appmsg)

正常应该是直接打开了记事本的这个页面，如果你进来发现是空的，没有任何文字，请双击一下点开这两个记事本文件，就有了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSjqvtxB137dns91EDwyvCVUIuLPjciar8RvLOwzDrU9llPwBY8ZgzTeA/640?wx_fmt=png&from=appmsg)

你如果想看一下具体的详情学一些知识，可以把这个有一堆文字的记事本看完，但是如果你懒得设置这么多东西看这么多字，可以直接点quickly这个笔记本，我们直接快速开始。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSgdl0aozdokVeYwribuCBeHHNTZXkTIIEibRqzdHbuHFlicMSHvQ0FxC3w/640?wx_fmt=png&from=appmsg)

进入quickly这个笔记本后，点击第一个代码块，也就是：#移动项目文件夹到数据盘以节约系统盘空间。然后点击上方的三角图标，运行代码块。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXS75dg8VzMYwiapX5wWoFL1e5vp2sibNq9ZfOTy2PHp21mGic6VyAarwQfw/640?wx_fmt=png&from=appmsg)

此时注意一下右上角的圆圈，空心圆则代表机器目前空闲状态没有正在运行的东西，实心圆则代表系统正在运行中。你运行代码块后，圆圈会从空心圆变成实心圆，运行完成后，实心圆会变回空心圆。

第一步移动项目文件夹运行完成之后，我们在左边的文件栏，进入这个路径：autodl-tmp/so-vits-svc/dataset\_raw，在这个文件夹里，新建一个文件夹，比如我叫Khazix，我那就新建一个Khazix的文件夹。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSS8dFM55NI8oeRNU8G9b5UwxepVYfeSj9LPibOofdnD9c5BJiaJrELD7A/640?wx_fmt=png&from=appmsg)

再点开这个Khazix的文件夹，把我们第一步处理完的所有数据集直接拖过来，传上去。（PS：我知道传压缩包再用解压命令速度更快，但是不是所有人都懂linux解压命令，所以别杠，我更喜欢让普通人都懂都直观没有思考成本的方式去写教程。）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSzFbgsScuPY9cYwesuApiaBDibribmpdmbviaJJDjZUJicAQoLW3aMOR1rcw/640?wx_fmt=png&from=appmsg)

当这个蓝条跑完并消失后，你的数据就已经全部上传成功了。  

回到右边的记事本，预处理这四部，挨个运行就行，注意下右上角圆圈状态，运行一个后，圆圈状态从实心圆变成空心圆后，再运行下一个代码块。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSeTasWOVPYZicp2Ra2keDwc9fmFVib4epVz4NRaE0dqco2Q5nmPAGunJw/640?wx_fmt=png&from=appmsg)

前三步：#进入项目文件夹、#重采样、#默认使用带响度嵌入的768成功运行后，就是我截图的这个运行反馈。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXS3CZl69NnD8Clia1ZVVD2fILx3dbVMxeV9kQSaF9qiclBiaerUdLJ5sL7A/640?wx_fmt=png&from=appmsg)

第四步：#默认使用rmvpe且带浅扩散，会跑的旧一点并且有进度条，运行成功以后，是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSJibMuCuicFpLxxHydh6EkjoIq2NsibWibl9t2YgMDM40OsaXtsbnqiac5wg/640?wx_fmt=png&from=appmsg)

OK，所有的预处理已经全部完成，接下来开始正式训练。

在训练这部分有两个，一个叫浅扩散模型，一个叫主模型。主模型是核心，也是需要先训练的，浅扩散模型属于扩展模型，能增强效果，但是会削弱不少音色。  

所以只进行主模型训练就行，所有的训练和推理都不要直接点笔记本的代码块直接运行了，不好管理。

保持左边路径是autodl-tmp/so-vits-svc里，点击右上角+号，在新页面中选择终端。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSiauEs0RHuibBdovDfLdTyQ00kxpszB4pjCUWbhqhHGJuzLwoiaAr7IL9w/640?wx_fmt=png&from=appmsg)

然后在命令行中输入命令：

    python train.py -c configs/config.json -m 44k

如果报错，请先看看你是不是在autodl-tmp/so-vits-svc新起的终端。

正式训练后，就长这个样子，左边的那些Epoch是轮数，没啥大用，主要看右边的步数，1w步左右可以去听，2w步差不多就可以用了，最多不要超过6w步。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSE9FcMCpv0NuOPz7hhmPCRMClp2uibl2cepbbI59PMYfsUFWicP95xozA/640?wx_fmt=png&from=appmsg)

至于如何判定模型效果好不好，在我实验下来，任何参数都没啥绝对的意义。

**请记住，用你的耳朵，你的耳朵，就是你最好的分辨器。1w步后的每个模型，用你的耳朵，推理后，去听。**

  

 **三. 最终推理与合成** 

模型差不多了以后，可以一边训练，一遍开启推理的WebUI界面，去做歌，试着听一听。  

跟训练的步骤类似，保持左边文件夹保持左边路径是autodl-tmp/so-vits-svc里，点击右上角+号，在新页面中选择终端。新建一个命令行页面。

输入代码：  

    python app.py

等一会后，你就能拿看到两个链接冒出来了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXS8AMOR2fd0wqzOkDzHgo6AtB06nxEPvIfr42r6ZE2kQxzMvhpR9OiadA/640?wx_fmt=png&from=appmsg)

只看第一个这个http://127.0.0.1:6006链接就行。

先别复制打开，因为你打不开。  

回到容器实例首页。点击自定义服务。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSAcibYH4Ty0gHpe6IlspcBZ2MHKq3uZPxCFGlPR7JALJ6bqFBdzCNUEQ/640?wx_fmt=png&from=appmsg)

就会弹出来弹窗，按的教程和要求来就行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXS2zhuWWiaJns01eMWH94fbJhl7t5dLLdmRrx8jkbrLlknJptkSjqjs7A/640?wx_fmt=png&from=appmsg)

等把代理挂上以后，你就能打开http://127.0.0.1:6006这个链接了。

打开以后，3个挨个点，模型那块选择具体是哪个模型。配置文件默认是 no\_config，不要忘了点开换成config.json。最后再点一下加载模型。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSc6dfpBnibJHrQFC0KZo8WZKMk8CftwGaHfHfgEef4IicgnpK3ibQia8lkg/640?wx_fmt=png&from=appmsg)

加载完了以后，你就可以看到反馈了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSlRxB6gVP03S3TGZYN7teUMJQPTxXlMHDhMx0fwJgaXyflUqN37gUAA/640?wx_fmt=png&from=appmsg)

扩散模型和聚类模型是两个扩展模型，聚类模型你炼说话模型时有用，会增加咬字，唱歌模型没啥大用，不用管，浅扩散模型可以修复部分哑音，但是会出现一些音色泄露问题，你数据集弄好。也不用管。

再下面，就是要传你的音乐的地方了。  

**一般流程是：下载音乐 - 分离人声与伴奏 - 人声推理 - 最后推理完的人声与伴奏合成。**  

下载音乐这块我推荐一个免费的贼牛逼的音域下载网站：  

https://tools.liumingye.cn/music

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXS9v5CcxdTFE8mPyGKiaObyCd2riaicKCtVkpvVBwoFr3Act81P7jGvLJLg/640?wx_fmt=png&from=appmsg)

没什么可说的，除了良心，还是良心，且用且珍惜。

下载下来以后，去剪映里分离人声和伴奏。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSPVkaTqKZCT4ibgDqSnTkG5nasBPQudrIUWAicnY287FoH4uyqsn9ibGicQ/640?wx_fmt=png&from=appmsg)

我其实想了很久，到底推荐大家用UVR5的MDX23C还是剪映。

最后我觉得还是剪映吧，剪映这个人声分离，能达到UVR5的MDX23C的90%左右水平，主要是真的有手就行，点一下就完事。。。。。。而你要研究UVR5的那些模型，能干吐你，而且大概率你显卡也跑不动。  

所以在剪映里，你分离两次，一次仅保留人声、一次仅保留背景音，还可以把那个人声再人声美化一下，最后，再把人声的那条单独导个WAV出来。  

注意，出来的人声WAV还是没法直接用，因为里面可能会带混响和和声。所以还是要用UVR5的VR 5\_HP去一下混响和和声。  

**你直接对着我公众号回复"SVC2024"，就有UVR5的下载包了。**  

正常安装完打开以后。按照我图片里的设置，把参数改一下，然后点那个Start。跑之前，记得把剪映关了，要不然很容易爆显存。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSI3jwzhgrYjQfPrJzPiaSQo9VK2CPr3FvWpbI6mQWa7RQ2nP7Sr3HmnQ/640?wx_fmt=png&from=appmsg)

分离完以后，你就有一个非常棒的干声了。  

最后回到SVC的WebUI页面，把你的干声直接传上去，传5分钟的都没事，不用担心爆显存。然后把这个f0预测器，换成rmvpe。其他的什么都不管，直接点击音频转换。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSA7LicyvIGAJ9bGwzdCKOQu1Ugc3xyqxeiaTlCO42eVYMBej7ibTCzEw6w/640?wx_fmt=png&from=appmsg)

几十秒后，你的歌曲就替换完成了。  

现在，你就是这首歌的，唱歌人了。  

（总感觉这话说的，像破壁人。。。）  

最后，去剪映里自己把人声和伴奏音轨叠一起，导出就完事了。这个我就不教了。要不然文章又奔着5000字去了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXS1jgT4x5LI7ABFcS1YC9J7iaH2oRUZ5LaWaNpWfRYIkJ7Frb66AjbDlQ/640?wx_fmt=png&from=appmsg)

  

 **四. 保存模型下次使用** 

云端的一大弊端就是，你弄完了，不及时保存的话，就全部白弄了。

所以，一定要把模型保存下来。  

来到这个路径：  

autodl-tmp/so-vits-svc/logs/44k

你就能看到你的模型了，你可以把这个两个模型下载到本地，万无一失的留着。下载再用的时候，直接再开台机子，把这两玩意，传到同样的文件夹里，就OK了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqOXORJAG9qcfeHez3McAXSthibH0yWvLDEGFjiah1iaWW6unc2VbWiaz1vKwZqVdrfnEhybg2QcbnzNw/640?wx_fmt=png&from=appmsg)

  

 **写在最后** 

说实话，做教程还是心累，因为默认得把所有人都当小白，尽量把所有我趟过的坑都讲到，让大家避免跟我犯同样的错误。还得写的不长篇大论，让大家跟着有手就行的就能做下去。  

但是希望花费的这些时间、精力。  

能对大家有一些用处。  

**但行好事，莫问前程。**

**那前路也永远会有意外的惊喜等着你。**  

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言