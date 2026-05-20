     DeepSeek开源第二天，发了一个比OpenAI十二天直播还硬的硬货。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

DeepSeek开源第二天，发了一个比OpenAI十二天直播还硬的硬货。
====================================

原创 数字生命卡兹克 数字生命卡兹克 2025-02-25 11:45 北京

> 原文地址: [https://mp.weixin.qq.com/s/txsoPL-Hn1MzdIErsilq7Q](https://mp.weixin.qq.com/s/txsoPL-Hn1MzdIErsilq7Q)

刚肝完Claude 3.7 Sonnet，睡了两小时，马不停蹄的又起来看DeepSeek开源项目。

结果时间线上先刷到的是阿里的推理模型QwQ-Max的预览版。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6JWgia1H752R4yuCHPUqqaWWIJkXF1mPJMpkHicgFQwPXWEa1tAJHlGSw/640?wx_fmt=png&from=appmsg)

不是哥们，早上5点发，这也太抽象了。。。

但是毕竟阿里，是跟DeepSeek其名的“源神”，还是值得关注一下，反正他们跟我说，正式版很快了，而且也是全部开源。

有兴趣的可以先去线上版本https://chat.qwen.ai玩。

左上角选2.5-max，点上深度思考，里面模型用的就是QwQ-Max preview。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6nM1oPr3mEFOtW95CicM4qH41SvctGKcMWLKOSM6jbNx8NTqh9V6pyyg/640?wx_fmt=png&from=appmsg)

回到DeepSeek这边。

昨天第一天他们发的FlashMLA直接在H800上把性能榨干。短短一天过去，Github Star 就已经8.2k了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6fRSEElaPficpfF0QhLETLQPib0yibXfYiaibficI6RjVuRjYblMPu2k7MoibA/640?wx_fmt=png&from=appmsg)

而今天，他们带来的项目，放得招比第一天还大，承上启下算是用到极致了。

开源的是一个叫DeepEP的东西，它把电脑里的GPU性能再次拉满。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6osY84Q9uxXq0X0tZFQAV897C1DtwBib1dYliblGkNlcxuMhWCDEKYAdA/640?wx_fmt=png&from=appmsg)

开源地址在此：https://github.com/deepseek-ai/DeepEP

1小时左右，Github上已经斩获1000多颗星了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6yCmeLdGmCpMeq0VzLuFneMlErGvYGeqtVg8feMXO1sichqrMcsicpCZQ/640?wx_fmt=png&from=appmsg)

AI圈子里老说软件先行，硬件开路。但DeepSeek要的就是硬件效率，最低的硬件资源干出同水平更强的AI任务性能。

甚至，我感觉，DeepSeek比英伟达更懂怎么榨干GPU。。。

DeepSeek这回开源的技术，实在过于硬核，理解门槛太高，硬核的甚至我都有点看不懂了，但是还是硬着头皮学习了一波，也提前找了朋友蹲点，第一时间给我拆解了一下。

所以秉持着一个自媒体的原则，给大家简单科普下。可能会有点错误，如果出现，欢迎各位大佬莅临评论区进行指导。

我先用一个非常通俗易懂的例子描述一下这玩意。

**现在很火的2个****AI****领域的研究方向，一个是“混合专家模型”（****MoE****），另一个就是“专家****并行****”（EP）。这回开源的DeepEP ，就是它俩量身定制的通信库。**

在一个MoE模型里面，你可以简单的理解为里面有256个专家，给你干不同的事，有些擅长语言，有些擅长数学，有些擅长常识。这种模型叫做"混合专家模型"。

但是呢，过往的MoE模型里面，你可以想象成是这256个专家，都在一个房间里面，靠嘴通信，吵来吵去，要是所有人一起大喊大叫，这有多混乱，效率有多低下，你肯定能想象的出来。

而这个DeepEP呢，相当于设计了一个中间的沟通系统，把一群靠嘴巴沟通的地球人，变成了一群直接思想透明的三体人，靠电磁波交流，速度奇快无比。

**所有专家的信息都可以即刻被其他所有三体人专家接收，没有延迟。**（信息在不同GPU专家间以接近光速的方式传递，延迟低至186微秒）

**而且整个文明可以同时感知一个三体人的所有思想。**（支持"all-to-all"通信，一个专家的信息可以同时发送给所有其他专家）

**因为三体人的思想是透明化的，让信息无损传递，没有误解。**（数据在传输过程中保持完整性，支持FP8通信）

这就是大概的东西，虽然可能还是需要理解一下，但是我已经尽可能用我的知识来类比了一下。

所以说啊，这就是真正的，三体科技。。。  

回到DeepEP的技术和参数这块，我也列了3个点。

**1\. 开挂般的内核优化**

与DeepSeek-V3 论文一脉相承，DeepEP 提供了一组针对非对称域带宽转发的优化内核，把高吞吐量和低延迟又带到了一个新水平。不光让大模型训练更快了，推理效率也大幅增加了。

他们根据 DeepSeek-V3/R1 的预训练设置，在 H800 上测试了普通内核性能。

这性能表现，牛逼。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6FibQ9aH28CNzViaicYR93LHt3ibwymDzwgQE6ouhaWicSxk1MnTLDhEQmDA/640?wx_fmt=png&from=appmsg)

**2\. 低延迟**

对于另一种对延迟敏感的推理解码，DeepEP 包含一组纯 RDMA 的低延迟内核，以最大限度减少延迟。

看到这里，感觉DeepSeek又贴心又硬核，把DeepSeek-V3/R1的核心优化技术之一开源就是这么简简单单。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6mEETrlFknXPMFicUjhpnvbG6RVo1VKyiaQb6MoZxA1N9MFebaYicHqMOw/640?wx_fmt=png&from=appmsg)

**3\. 新的通信-计算重叠方法**

最后的最后，DeepSeek又给了个惊喜：一种基于钩子（hook based）的通信-计算重叠方法，牛逼的是，这种方法不占用任何 SM 资源。  

就比如你在翻书的同时，就能一目十行了，而不是翻到哪页看哪页。

DeepEP 就是这样，让 GPU 在传数据的同时还能计算，一点不浪费时间。

这让我想起DeepSeek-V3当时论文一发出来，性能效率比把全网都爆了的那种即视感。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6cG4nM8m1jaibQVmd5eqPZ34QZC4JZopk7Qbib5GoAoortayKD13lK1bw/640?wx_fmt=png&from=appmsg)

恍惚间，我又想起之前，整宿盯的OpenAI十二连弹产品发布会，产品未至，营销先行。

看完了以后，我基本就是一句话描述他们：

XX OpenAI，XX 奥特曼。

这回，DeepSeek的手笔，让我感觉才是真的牛逼。

就是给你个代码库，简简单单，一点套路没有。

直接把饭喂到你嘴边。

整体来看，这回的开源也是开箱即用，下载、部署和安装都一步到位。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6nKhpP6nu8cshVlqr6BCaiatQ7Nuuqad9czdibc7L8jKDnic9TkrJ1jFSA/640?wx_fmt=png&from=appmsg)

这是开源党的狂欢日，而这样的狂欢日还有三天。。。

就像DeepSeek在开源页上所说的那样。

他们正在 AGI 探索中挑战自己的极限。

仅仅作为开发者。

以完全透明的方式分享微小但真诚的进展。

DeepSeek。

把进化工具，平等地交到每个人手上。

让所有普通人都能够。

跨AI的海，越AI的山。

这一刻，看到DeepSeek做的大事。

才让我由衷地觉得，AI真好。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、芝兰山

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言