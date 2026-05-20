     Skills的最正确用法，是将整个Github压缩成你自己的超级技能库。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

Skills的最正确用法，是将整个Github压缩成你自己的超级技能库。
====================================

原创 数字生命卡兹克 数字生命卡兹克 2026-01-21 10:16 北京

> 原文地址: [https://mp.weixin.qq.com/s/JER462B3dVYlwVYl6rTmzw](https://mp.weixin.qq.com/s/JER462B3dVYlwVYl6rTmzw)

昨天写了一篇关于在[扣子上使用Skills的文章](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647679068&idx=1&sn=6b3ae5770982ec685d57fe8a006e6317&scene=21#wechat_redirect)。

里面用的案例，特别简单，就是把Github上一个非常经典的开源项目，封装成一个Skill，方便我们以后进行调用。

![图片](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrCo6BdbjkzCLanc3Qic2MdgRBhOrNZ15X8jMo0rx3z7t5hzp8XS4x2LIt8yMicVYJ7W0ylPGdRKiazg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

这么做的原因特别简单，就是我一直觉得，重复造轮子是一件特别呆逼的事情，互联网三十年，开源世界大神这么多，其实你能想象到的绝大多数需求，都有大佬和真神们，在前方铺路，做出了现成的产品，然后开源了出来，给非常非常多的人用。

其实现在非常非常多的一些商业APP，特别是一些所谓的格式工厂、压缩之类的，绝大多数都是把一些大佬的开源工具，做个前端，给大家用。

之前我觉得没啥问题，确实，Github上面很多的开源项目，都是没有GUI的，全部需要部署，部署以后还是用命令行操作，真的，光环境这一条，就能卡死绝大多数的普通用户。

我自己，之前就是被挡在门外的普通用户。

有太多太多好玩的、实用的、很屌的开源项目，我用不了了。

比如格式转化这破事，没有AI之前，我每次就是去Google搜，MP3转WAV...

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBQbsK0pm13hkDic3ickPoznYY3BQyXLdTrxjKo4dvAhzNWqpKunibbh9VQ/640?wx_fmt=png&from=appmsg)

然后就看着各种各样你也不知道是不是有刺客的链接，在向你招手。。。

所以，Skills一来，从文件结构上，它是可以把脚本和Prompt打包在一起的，这一点，跟单Prompt或者脚本完全不一样，再加上现在一些Coding能力强的基模和Agent，我觉得，它天然的擅长把很多的大佬们的开源项目Skill化，从而在Agent里面，为我所用。

而且你要相信那些历史悠久的经典开源项目，经历了无数的时间和使用者的鞭打，不管是成功率还是稳定性还是效率，都远超绝大多数的你根据需求，让AI临时去写的一些代码...

所以就搞了这么个东西，其实不止Coze，当你在OpenCode或者Claude Code这种支持Skills的产品里，只要你装了那个Claude官方那个能生成Skills的Skill，也就是skill-creator，打包Github上的开源项目，也是完全没问题的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpC92KictnrYXV7jWfAoB5ujEh5p3NjnQ57wJCbyeESFt4KeYlX7IQb7wVavRZTFntQptllViagXpeA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23)

这种方式，就能最快速度，越过所谓的本地整合包，变成一个类似于Agent的产物，让你能快速的用上。

比如昨天扣子文章中，我把视频处理的开源项目FFmpeg和图片视频处理项目ImageMagick，封装成了一个多模态素材处理的Skill，它大概就是这个效果。

![图片](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrCo6BdbjkzCLanc3Qic2MdgD00PrEkiapfuEr2hicQ3KGaLHLTaRAUsIrVgScohfFUK27Ty0NqJozHg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

然后呢，在文章中一个有趣的评论，引起了我的注意。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBNiagHkKiaeQyuj1jBp9IL1Ien58pnuJykMRicbbjgJCB3GjdFPNDVXbhg/640?wx_fmt=png&from=appmsg)

这个评论的问题没啥毛病，因为github上那么多开源项目，离大众肯定还是非常的遥远，我因为知道有特定的项目可以去处理特定的事，所以封装成Skill就特别的简单，但是大多数的普通人，可能连github是什么都不知道，那怎么封装呢？

这确实是个问题。

我当时想了两分钟，然后我一寻思，不对啊，这不都有AI了吗...

于是，我就回了一句：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gB4lgGjlbfAQEd8KzazYZ3OtaAdSFsjyQ8NclRfrfvrAAAnv2h0Lu8NQ/640?wx_fmt=png&from=appmsg)

没想到，引起了好几个朋友非常正向的反馈。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBlgzWic3hvv9xcKxghARcwlOHicsr7BCQN8kVJE9mvIeHVDttgwZGjaiaw/640?wx_fmt=png&from=appmsg)

这个时候，我才意识到，其实，我的很多的小技巧，对于蛮多人来说，还是挺有价值的。

所以这块，我觉得我觉得可以单独拎一篇文章，来给大家讲一讲，普通人怎么把整个github，当成自己的弹药库，做成skill，让自己真正的，变得三头六臂无所不能。

比如，我自己现在，就已经封装了很多的skills。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBNqFv9hZJR4A36xRVMzC41Ofia9nUvkVbTez7NDkvnaX4WHMiahSaMn1g/640?wx_fmt=png&from=appmsg)

哦这个管理skills的skill，也是我自己建的一个skill，要不然感觉每次进到文件里看太麻烦了，我就可以直接用这个skill，对我本地的所有skill进行卸载删除修改优化操作...

举一个例子。

我相信大家经常都有一个需求，就是去各种视频网站上，下载视频，比如Youtube、B站等等。

我自己也有。

那我们就可以直接打开ChatGPT，选中GPT-5.2 Thinking（目前我认为搜索能力最好、幻觉程度最低的模型），当然，你用别的也行，一般来说问题都不大。

然后直接提出你的问题：

有没有那种就是去各种视频网站上，下载视频，比如Youtube、B站等等的github上的开源项目。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBBNK104uSicBIgOYXGO7FRgJJzKvpveLpvB4que5sEp62h7lWZF4TOQg/640?wx_fmt=png&from=appmsg)

在GPT搜索了一阵子以后，就会给你推荐一个，在github上，几乎封神的项目。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBe4e9HDf7cCTjG7VfBNZkYicnUeAcVTHttDU4ybkp2CNCb3TsZwzoZRw/640?wx_fmt=png&from=appmsg)

它叫做，yt-dlp。

github上143k的star，说是真神，也不为过。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gB8PHFbj2ia4HAHPnBGosSEQl5c0CkZLfTyuesTV6VgCic86QOpaWxOE5Q/640?wx_fmt=png&from=appmsg)

支持上千个网站。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBia27HN40q0FyCQPaXGH6eUua4PuGHaeczEAxWWxO4kLcB5LUuoG2ibuA/640?wx_fmt=png&from=appmsg)

这，就是yt-dlp，我觉得最伟大的项目之一。

你要相信，在这个世界上，在这个互联网上，有无数的大神和前人，已经为你铺好了前路。

你要相信，你的需求，永远不是这个世界上第一个提出这个需求的人，也绝对不是最后一个。

你要相信，人类在这几十年所积攒的历史，几乎覆盖了世界所有的领域，互联网，永远都是那个最深、最广的宝藏。

你要相信，在这一刻，你搜出来这个开源项目的这一刻，这就是人类开源精神的涓涓长河，在你面前展开的绝美的画卷。

我时常赞美这世界上，每一个愿意开源、每一个无私的将自己的知识分享出来的前辈们，正是因为他们，才让我们，能站在他们的肩上，去摘更美的星辰。

我们直接复制yt-dlp的github链接。

然后把这段Promtp发给你装好了skill-creator的OpenCode或者Claude Code：

帮我把这个开源工具https://github.com/yt-dlp/yt-dlp打包成一个Skill，只要我后续给出视频链接，就可以帮我下载视频。  

这块如果还不懂或者不知道的skill-creator是啥的，可以去看我之前的那篇文章：

[一文带你看懂，火爆全网的Skills到底是个啥。](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647678672&idx=1&sn=c3510896d2de19b5c5ab6805c27182e5&scene=21#wechat_redirect)

一般我的做法对打包，是先让Agent进行规划，然后再去写整个的Skill，这样我自己感觉，成功率会高一点、后期稳定性也会更强一点。

相对应的，OpenCode就是开启Plan模式。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBWib1Iw4zeiaepGlvFBlW61GTNtsMhSyTkHgnlk0fGrzac3C7qL8QxG1A/640?wx_fmt=png&from=appmsg)

然后，Agent就会开始调用skill-creator这个生成器，开始分析yt-dlp这个项目，然后开始规划要怎么打包封装成一个Skill。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBnXWVHu9HxqvYvB9hd5DKKqweRbhw7Poyjr0aCpBE6OWMbXYOz2AMhg/640?wx_fmt=png&from=appmsg)

规划了一通以后，OpenCode就分析完了，向我提出了几个问题。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBnWn23QQGWCWzyWl3b1tYJtAQQdxT2jfQL9LAJEt0AvqXQEQef0iawcw/640?wx_fmt=png&from=appmsg)

我也给出了我的回答。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBjdhIibNjMh7ib7bhDLnpiaO1JPcByMv5McD0XmByibYg1FDSFufgR4AZ3Q/640?wx_fmt=png&from=appmsg)

然后它就会继续规划，最终给我一个非常明确的计划。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBWibUs6ZqFf5SyCKzZibxhl4TqZ8oicv8iaOyuFcQ1RibqAjiba0ReAL8SGBA/640?wx_fmt=png&from=appmsg)

我觉得没有问题了，这个时候，我就会切换到正式的开发模式。

也就是这个模式，然后发一句话，开始开发！

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBKPpAswJuibs2lbsviarAs9Wnd1vWu3AZvc4WibBHVLVLWBZIia6ySTIoFQ/640?wx_fmt=png&from=appmsg)

OpenCode就会开始了。

过了一会，大概2分钟以后，这个基于yt-dlp的视频下载Skill，就开发完成了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gB13puYmlaSukiaYItVffHCLl6pIEPVjpxGroTibWWRXXt3oEibDaJBLILw/640?wx_fmt=png&from=appmsg)

我们试一试。

比如OpenAI刚刚出的Youtube访谈视频，我想下载下来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBTwictX7OoC3ibiaWG7DX3eE1TqPBqUGXwhPIAFJwcwq50qMmJXAFicR0bg/640?wx_fmt=png&from=appmsg)

直接就把链接扔给OpenCode就行，这里可以注意一个小技巧，就是所有的涉及到这种需要运行程序的Skills，在第一次运行的时候，都无脑推荐在OpenCode里使用GPT 5.2 Codex（如果你有的话），体验会比Claude 4.5 Opus好N倍。

大概就是：构建Skills的时候Claude 4.5 Opus，如果这些开源项目封装好了，在第一次运行的时候用GPT 5.2 Codex，后续就无所谓了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gB7BS0iaXI6JshicB1FiaicQfHWLwbqhLfMVMC8sCyFOTjkJOhicrrrk0RmBA/640?wx_fmt=png&from=appmsg)

第一次运行，其实会遇到很多问题，比如说Youtube防爬机制很强，需要你装个浏览器扩展导出Cookie，比如要安装一些其他的项目等等，不过这些AI都会指导你干好。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBmPiaNCqPWSialglVEIGQYeibppFSVCicNdC3enibh8DAIJhjicR8ibjxKQ98w/640?wx_fmt=png&from=appmsg)

然后一顿操作，这个项目，就下载好了，全程大概也就几分钟。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBXTW0GgNQJaJKass0qjcLY9wOmz4hAl93132asR6lA6TxOyKSHbe2Zg/640?wx_fmt=png&from=appmsg)

之所以是几分钟，还是因为，这是第一次。

而后续，只需要，十几秒。

这时候，其实你还可以做一个事，就是，把前面的那些为了下载视频而做的一些事情和经验，直接跟AI说：

把这些经验，都更新到video-downloader这个skill里，下次就别这么慢了。  

然后，它就会自己对他的Skill文件进行修改，下次，这些事情，就不用干了，随开随下，快到起飞。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBWmedQ5RicqPibeHV3aAhiaBn41QrE7NFYvMIKZl4kyATxEAEWicMbqOAvg/640?wx_fmt=png&from=appmsg)

这就是我的自己纯为了自己方便的一个skill全流程：

根据一个需求，用AI搜索github上得开源项目，把开源项目使用AI进行Skill化，首次运行后，寻找BUG和问题，重新迭代Skill，至此，Skill固化，形成我的主Agent中一个可靠的技能。

不止是一个下载视频的需求。

还可以是，把一个web项目，打包成一个轻量级的桌面APP。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBjwicWTiaFiaLZxulYRnDz4iaM0ThG3icNowBBicUoVp2sIX2jQhb66S37iaRA/640?wx_fmt=png&from=appmsg)

于是，找到了Pake。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBqAwnAib2PJBI6LpS1GIEAmH9Xx881bRqj6SXcNwUIKxgwGbLxkL9B9A/640?wx_fmt=png&from=appmsg)

Github上一个45k的超棒的项目，那就，直接Skill化，以后，你的网页开发完，直接就可以用Pake skill，一句话变成桌面APP。

你还可以，直接做一个究极万能的格式转化工厂。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBdeurdBS9oIibz5Hq0jMB4iaVz2G44d2BQ0stWF2ibe5PrM2nsOkSTEqzA/640?wx_fmt=png&from=appmsg)

直接把这些最牛逼的格式转化项目，直接封装在一起，做成一个万能的格式转化Skill。

从此，你无需各种奇怪的格式转化器，一个skill，解决所有。

你还可以，把ArchiveBox转成Skill，从此，你有想保存下来的网页，都可以发送给ArchiveBox Skill来以无数种你想要的格式，帮你保存下来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBWouvhIJ6DvzoAkCyKPJ6bYuQgsQpujCRhsDq3hsnKZLxicdWviclegMg/640?wx_fmt=png&from=appmsg)

支持N种格式，真的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gBCPFKVgrmLOgmJQLoScONPJ1wQFibjrxwnXnwDibqBcIkL3GwItTODWIQ/640?wx_fmt=png&from=appmsg)

甚至，你可以把著名的Ciphey，转成一个Skill。

从此，你就可以，在你的本地，配合Agent，直接破译密码。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqgBBAMRyFuzOtGuo68h9gB6KpyIG8ken9hzxgVvOVzMYGIa3Lhue1fw30uJoeL3PK2XAv5DabAuA/640?wx_fmt=png&from=appmsg)

这些，全部都可以Skill化，全部都可以加入到你的Agent之中，成为，你最坚实的技能，成为，你最恐怖的弹药库。

而我提到的这些，仅仅只是Github上开源项目的冰山一角。

Github上牛逼的开源项目，那些人类的经验、人类的光芒。

本就灿烂如星海。

因为Skills的诞生，因为Agent的强大，现在，每个人、每个普通人，你的背后，都是全人类过去数十年的积累，只要你想，他就可以为你所用。

你无需三头六臂，你无需头上长角，你已经拥有了海量的知识和技能。

如果回到3年前的你的面前，你觉得，他跟你如今可以做到的事、如今的能力边界，还有任何可比性吗？

朋友，这样璀璨、这样伟大、这样能让你成为超人的时代。

真的不会让你兴奋吗？

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言