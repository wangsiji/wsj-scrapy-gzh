     用AI把微信聊天记录变成可视化报告，酷到封神。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

用AI把微信聊天记录变成可视化报告，酷到封神。
=======================

原创 数字生命卡兹克 数字生命卡兹克 2025-04-08 09:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/Z66YRjY1EnC\_hMgXE9\_nnw](https://mp.weixin.qq.com/s/Z66YRjY1EnC_hMgXE9_nnw)

我之前拉了一个AI自媒体的群，就...同行交流，互相学习。

很快就500人了，然后里面这群人，每天就话不停。

几小时不看，里面就是99+。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWma15iaVl0KBcMoTfsibz1sD4rFCicaZ28Jyh4mnibrf5ymoXfx4Zsz9tUQ/640?wx_fmt=png&from=appmsg)

真的，爬楼爬不动了，信息太多也是一种负担。。。（不是打广告，群已经满了，找我加也进不去。。。）

直到前几天，即梦3.0内测的那天，突然有个群友，在晚上11点，发了一张图出来。那张图是这样的。

是我们整个群一天的聊天记录汇总，还是可视化的，而且分门别类，还有每日金句和云图，超级有意思。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWBgIrU4vSzicoF5A1GM5fonE9zicVibELDT69GYSibVtm0aGibGvnCjGeRIw/640?wx_fmt=png&from=appmsg)

这个群友，叫@Simon的精神世界。

他说，他之所以想做这个东西，也是因为群里消息太多了。。。他是在爬楼爬不过来，那不如，就自己手搓一个。

我问他，是怎么做的，他直接给我开了个飞书会议，分享了20分钟。

在得到他的授权后，我也想，把这个做法，分享给大家。

不止可以总结群，你跟女朋友、领导、基友的聊天记录，也都可以总结。

真的，酷到封神。

做这样一个可视化的微信聊天记录总结，一共可以分为三步。

1\. 导出微信聊天记录。

2\. 让AI根据聊天记录生成网页代码。

3\. 将代码运行变成可视化网页/图片。

我们一步一步来说，保证手把手教会你。很简单的。

  

一. 导出微信聊天记录

中所周知，微信的聊天记录是加密的，很多人其实都卡在这一步，不知道怎么把微信的聊天记录导出出来。

同时，还怕会有数据泄露风险。

@Simon的精神世界给我推荐了一个很傻瓜简单的工具。

叫MemoTrace，留痕。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWIDicqwt2wic6tgwAMescaGNm15S9O27hDccXtqDxuud8AI266NOUPJdw/640?wx_fmt=png&from=appmsg)

数据风险肯定也是我非常关心的，所以在用之前，我把作者的播客、过往两年的资料还有一些评论信息全部在网上遍历了一遍，没看到啥负面，同时也进行了断网测试，也找了某实验室做安全的大佬看了一下，没发现有啥问题。

然后，我自己才敢用，也才敢在这里写出来。

项目网址在此：https://github.com/LC044/WeChatMsg/?tab=readme-ov-file

在项目中，可以进入官网直接下载，目前比较蛋疼是，mac不支持。

所以，需要有一台Windows电脑。在网页里面，下载2.1.1版本，上面大字写了，小白用户请不要下载测试版。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWgWrrTwSYZq1XyLXzYImZYdFetsCJZKZxxQrSviaF8SibJAzRa6ny1jzw/640?wx_fmt=png&from=appmsg)

正常下载完成安装。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWQyhXHRibJ8Bx8exvGxsZPIduWeZzaOLuI97GdbdOIV2w20ibQfeUXEyA/640?wx_fmt=png&from=appmsg)

在保持微信已经打开正在运行的状态，打开软件，你会看到一个没有那么精致的UI。

别看有那么多乱七八糟的信息，你其实根本不需要管那些东西，正常情况下你没魔改过微信的话，第一次使用，你只需要先点击获取信息。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWib1lVPbHPt8ls8mjVtalhZj0pUUanqf7RWcTHj0wf0RAd3NiaH5BUYVQ/640?wx_fmt=png&from=appmsg)

然后，你就会发现，你的手机号、昵称、微信的ID被抓出来了。紧接着，点解析数据这个按钮就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWqMoIKPoxbVHhlRKdKs9uKIK2R3xLxHI2MbEEJaoNGU2AlL8aicyPYPA/640?wx_fmt=png&from=appmsg)

速度一般很快，我是5080的显卡，几秒就全部解析完了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq166EfOXQEX4nJLzwJ6gyezTkcqS53KJ0qVpLPRP39ggp14O3MBQ2H09FAZ9jpzPO2MESujicZTIg/640?wx_fmt=jpeg)

然后，它就会给你复刻了一个，使用微信的UI界面。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWvicoG5lETfkB0yO68vkwtSfBjFIH231YnQJn7AzJfzFUmeib8CLbrD4w/640?wx_fmt=png&from=appmsg)

有一说一，虽然安装完刚打开的那个UI有点丑，但是这个界面，我还是真的很喜欢的，非常的直观，符合用户的预期，简直就是UI设计中所见即所得的典范。。。

第一个聊天框，就是那个天天刷屏的AI自媒体群。

我写这篇文章的时间是4月8日凌晨1点56，他们居然还有人在里面聊天。。。

我们直接点击群聊右上角的导出聊天记录，选择这个AI对话专用TXT。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWCwLCaHoVs3np77br5BTGeVVc24mSTgTJJmhxiavXtOnxbnhFuGn0GYA/640?wx_fmt=jpeg&from=appmsg)

这个专用的TXT，你可以理解为做了一些数据清洗，把一些跟AI对话无关的信息比如时间等等都给剔除了，只留了每天的日期信息，同时还做了一些格式的排列，让大模型更好识别。

所以，无脑导出这个就行，因为我们总结和可视化聊天记录，也不需要那些精确到几分几秒的时间信息，更多的是看每天的内容总结，这个时间维度几乎就够了。

点击以后，会弹出一个弹窗。可以选择消息类型和时间周期，我一般就会把除了文本、分享卡片、文件啥的都勾掉，那些变成文本以后本身也没用，都是垃圾信息。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWaP1I3URHWPYJs6gh22g2xicaJSgTCuuD3EGAG684Fsm4wEeF8zjeqpA/640?wx_fmt=png&from=appmsg)

时间的话你可以自己选，我建议还是圈定一下范围，不要一次性导出全部时间，要不然...你的电脑可能会卡死。。。

全部搞定以后，点击开始，没几秒就会给你一个弹窗。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREW2EDKPOpaicDTTh3fvvkE25lGFVPrQvRHxK1RhK7nlWpvEV4AES5DOhg/640?wx_fmt=png&from=appmsg)

你就可以点击打开，跳转到聊天记录存储的文件夹下面，看到那个聊天记录的txt文件。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWaz4Q1weKhHCoAejMHnR8XHLKccWq3fE4LKCn2a3ZICzdhRhLRCOozg/640?wx_fmt=png&from=appmsg)

双击打开，你就能看到，这个文件是这样子的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWVxJAMEwMHXunVAS3fklpZBv0CafhbHWuZZxBzLGjJENXwHscQm4RvA/640?wx_fmt=png&from=appmsg)

至此，第一步我们搞定。

你已经有了，能扔给AI最牛逼的原料，同时，最难的一步已经完成了。

后面的步骤，更加简单傻瓜。

  

2\. 让AI根据聊天记录生成网页代码

得益于之前Claude 3.7的更新，以及藏师傅的发明和教程，AI把任意信息，转成可视化网页这一流派发扬光大。

它能做到传统拼图或者总结，所远远达不到的精致效果。

而这次的思路，其实也是基于藏师傅可视化网页的基础上，继续生根发芽。

把聊天记录，给可视化。

只不过，跟之前的PDF、word等等不同的是，微信聊天记录信息太多了，在Simon的测试中，Claude 3.7、DeepSeek v3这些有能力做出漂亮网页的模型，几乎都吃不下微信聊天记录这么大的文本，更别提要按格式输出一段很棒的代码了。

但是有一个模型，却在这个场景上完美的不可置信。

这就是前几天发布，但是被GPT4o画图爆火给淹了的Google Gemeni 2.5 pro...

AI界汪峰实锤。

我们可以在两个地方用到Gemeni 2.5 pro，一个是他们的AI Studio，一个是Gemini助手官网。

AI Studio：https://aistudio.google.com/

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWFq8lv4NNP2ofiat8oU93KlzIic9KfvZibgad0WOiapYnnlWsHGpI0HOPvg/640?wx_fmt=png&from=appmsg)

Gemini：https://gemini.google.com/app

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREW479Bdib8vXbHoOetfAwQMuXjzJPuGa0wo1amPSuVaBGkn8xiaVxEPIIQ/640?wx_fmt=png&from=appmsg)

我个人还是推荐使用AI Studio。

一是Gemini上面不知道为啥，我给进去聊天记录和Prompt，这玩意就开始乱码输出，虽然最后的Html代码没啥问题，但是强迫症看着是真难受。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWQw5bLQTKFNQ6FiaoK1pGyugBcUHCJwHBHDU0WoicwSYw7yGATjGVI3cQ/640?wx_fmt=png&from=appmsg)

而是AI studio可以直接下载Html代码文件，而Gemini只能复制，保存成文件我还得打开Trae自己手动处理，就非常呆逼。

所以，我们打开AI studio，在右边把模型选成Gemini 2.5 pro。然后，把我们的聊天记录，和Prompt扔进去。

Prompt的话，Simon直接写了一个模板，为了固定样式，他直接把样式代码也写进去了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWe0hy6Ik1frDlXWDAbBVu5ic5iadENia38v1LL6MjzEhjSljcK5UVlsmKQ/640?wx_fmt=png&from=appmsg)

因为实在太太太太长了，763行，我就不贴在文章里面了，我给他放到了一个txt里。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWFa5Lshr4G1PQ8JuqribTeovfEth9HibDXPBAmQexAJVf8tP5bJcbkgfg/640?wx_fmt=png&from=appmsg)

你直接在公众号后台，对着公众号发送消息“wx”就会自动发给你了。

还记得我们在第一步里，导出的微信聊天记录txt吗。

直接把两个文件，一起扔进去就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWENDian6d2iaGVDunb3TeTWCJtMelDjUATzIibuPWusSjTGRzUBic5XUmjg/640?wx_fmt=png&from=appmsg)

啥都不用说，你就直接扔进去就完事了。

然后Gemini 2.5 pro就会自己嘟嘟的推理了，你啥也不用管，喝杯咖啡尿泡尿，回来的时候，他就把代码写好了。

你拉倒最后，有复制和下载两个按钮，直接点下载就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREW9F4vOna8ibKMLLeTRHbJydpV2AyVYFzwwkqPNBZJPEUdicP3Yic0xzbxA/640?wx_fmt=png&from=appmsg)

你的下载文件夹里，就会出现一个名叫code的HTML文件。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWzWsDFRHvvWdH8PAZzVmlK67FoicnDd9ZxSDVGBfbibjWTSkWRNCO9NHA/640?wx_fmt=png&from=appmsg)

至此，第二步完成。

  

三. 将代码运行变成可视化网页/图片

其实如果你装了Chrome的话，上面那个html文件，是可以直接双击点开运行的。

但是它有个很大的问题，就是是个本地链接，你想把这个东西分享给别人，要么从头到尾截一张长图，要么把这个文件发给别人让别人打开。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWRzdtoKR8kCganVfibYaJ96vPafjia49IsYPlcicdrRdjsITRuOv2HMSzQ/640?wx_fmt=png&from=appmsg)

怎么看怎么都不够优雅。

所以，我们有两种方式，分享给别人。

1\. 转成一个在线的网页。

2\. 直接把html文件转成一张长图。

转成在线的网页很简单，用之前我安利过很多次的小众产品yourwar就行。

网址在此：https://www.yourware.so/

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWMBgU6lUGMKs8SDSNcx7hLdWDvW4ocf63uaSxNIMibyeNOvCFOAVkicpA/640?wx_fmt=png&from=appmsg)

直接切换到Upload tab，把你的html文件上传上去。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWHITibiaRMcibo6uJnJNxTjtSXmncdX8zVv7vskLsBib2UfyJADZyByJibbQ/640?wx_fmt=png&from=appmsg)

几秒时间，一个在线的网页就搞定了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWmcJaGkENiacEIVmq34pHtsHl7hGVVicoibNMFzxCFGdKP1icAVc5dkAILQ/640?wx_fmt=png&from=appmsg)

直接点Share，就能把这个在线的网址，分享给你的朋友，你的朋友们，也都可以打开了。

比如我总结的4月7号的聊天记录，就是这样的，你们也可以打开看看。

https://z5gw1aprhd.app.yourware.so/

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWwG68OtH31yxNeGtpvDSWlTR7VdO06G10GtgXgQHVJXw6gCPOve7ODg/640?wx_fmt=png&from=appmsg)

另一种方式，是直接把html文件，转成长图，可以少几步操作步骤。

这个小公举也是在线的。

https://cloudconvert.com/html-to-png

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWrlYU4ia7cdYNTBtzic8QglIyRib3JRkGPZwTmcHANbMgHAiarpDtoKoMIQ/640?wx_fmt=png&from=appmsg)

你什么都不用管，只需要，把你的html文件，传上去。

点击Convert。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWXfQZUVclnATJBKAp9OWfvqYZpcpchbcYOTShmeTHwEEwVcOIa7DFdg/640?wx_fmt=png&from=appmsg)

等十几秒钟。它就会给你一个下载链接。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq9q1Gdu6nwAUOAhnNRicREWOgJ3bibibRm9AhVbb0ytOMibRev336YvP9NPsrmjqTJOLslPNN7BibPY2w/640?wx_fmt=png&from=appmsg)

主打一个方便快捷。

除了头部的emoji给我干没了，其他的都挺好。。。

  

写在最后

这个小教程，我个人还是觉得蛮有趣的。

感谢@Simon的精神世界提供的这么棒的点子。

让大家再一次眼前一亮，哇AI还能做这么好玩的事。

可视化的Prompt，别忘了直接在公众号后台，对着公众号发送消息“wx”就会自动发给你了。

希望大家，都能把AI玩出花来。

去做一些，属于自己的故事。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言