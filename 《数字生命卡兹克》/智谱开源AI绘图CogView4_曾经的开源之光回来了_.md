     智谱开源AI绘图CogView4，曾经的开源之光回来了。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

智谱开源AI绘图CogView4，曾经的开源之光回来了。
============================

原创 数字生命卡兹克 数字生命卡兹克 2025-03-04 14:06 北京

> 原文地址: [https://mp.weixin.qq.com/s/dgWIxkrIx5\_zSj62UCCaZg](https://mp.weixin.qq.com/s/dgWIxkrIx5_zSj62UCCaZg)

昨天连更两篇，今天想休息一下，结果。。。

真的快肝吐了，感觉自从DeepSeek开源统治地球之后。

开源的世界，迎来了究极繁荣。

上周DeepSeek连续5天开源硬核技术，阿里开源万相2.1，Qwen的推理模型推出预览版，但是肯定马上也要开源。  

而今天，智谱这个曾经的开源之光，在昨天官宣拿了杭州10亿融资之后，在官宣文章里如此写道：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMW6MVbdomAbyfEQicIwnXcjYMibezgic2w4iaFcEUT5oJQJYqTgqIViaFdicIofVtMOqloC4wibkia51H7A/640?wx_fmt=png&from=appmsg)

我知道智谱今年会大力开源，但是没想到，开源年的第一棒，来的如此之快，就在第二天。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csyjEX4Acm36fjhZykTOgoibCwzxfCwkibGUzpOicHOzz7wbebq4sMjKWeg/640?wx_fmt=png&from=appmsg)

我。。。不是，让我歇会吧。。。

今天智谱和清华团队直接开源了他们的AI绘图模型，CogView4。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMW6MVbdomAbyfEQicIwnXcRWDccTX44RC7NqOicEsOGA8lms7uLOcoIWQoZ7X1jHp3tAMqZh3cJMw/640?wx_fmt=png&from=appmsg)

这下，真的快补上2025年开源届的拼图了。

模型链接在此：https://github.com/THUDM/CogView4

模型尺寸6B，在BF16和batchsize=4d的情况下，GPU需求如图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMW6MVbdomAbyfEQicIwnXcgQtUDia3Yia1AdZiaTNO9rbicfuvoQn5r5dhG02ibg9nZlaicosgpYc54BYw/640?wx_fmt=png&from=appmsg)

最低估计一张12G的显卡就能跑起来。  

我们也在第一时间，把模型下载下来，反手在AutoDL上开了一台A800-80G的显存，部署测试了一下。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMW6MVbdomAbyfEQicIwnXceh0rf1pdw9AmYl1SFlHmqwCQzCVT27jKCtwjMh2y8vN7VRmFHicQkHw/640?wx_fmt=png&from=appmsg)

我自己测试下来，一张1024\*1024的图大概70s左右，AutoDL的云机器会慢一些，本地应该会快不少。

当然如果你们想直接体验，也可以用智谱官方自己搭好的在线服务：  

https://modelscope.cn/studios/ZhipuAI/CogView4

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMW6MVbdomAbyfEQicIwnXcHCARqby43F4orLdDWQV7ib8dTMbUqzsapqT1q43yAdjS6tEbu1radMg/640?wx_fmt=png&from=appmsg)

在跑了一小时后，我觉得CogView4，有两个比较有意思的点。

一个一个说。  

**第一个点就是，CogView4支持中英文字直接生成**，跟我之前写过的即梦2.1还挺像的，但是智谱的CogView4，是开源的。  

这也是开源的AI绘图模型里，第一个支持同时生成中英文字的。

我跑了些case，大家可以直接看看。  

比如这些Promtp：

1\. 一只布偶猫举着牌子，牌子上写着中文字体的“起来嗨’。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csVWDvcdPEeQVXKSicMYr8jUIQOjHS4mdVPYl3dgibVJjzU6uLy8BpFTFA/640?wx_fmt=png&from=appmsg)

2. 一幅极简主义风格的冬季插画，以"小雪"节气为主题。画面采用清新的浅蓝色调，上方用简约的白色中文字体写着"小雪"二字。构图主要分为三个层次：天空、雪山和铁路。背景是连绵起伏的雪山剪影，呈现出柔和的曲线；中间是一列橙红色的火车，在茫茫雪原上形成鲜明的视觉对比；整个画面点缀着飘落的雪花。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csHLiaHsx3MsfTT60KWVdZyzicZP8XCUc1SfXsIJOTwP546xl2R9YTic7WA/640?wx_fmt=png&from=appmsg)

3\. 电影宣传海报，画面中间是韦小宝，四周是宫女，标题文字“重生之我是韦小宝”。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csic2QNGov4ds6DvJB73jKnx4bkSA7cg8JthmUTcs0Y1IuHEBQZCtEuPQ/640?wx_fmt=png&from=appmsg)

4\. 画面顶部英文标题：“I NEED YOU”，复古美漫动漫，画面中央是一个小孩在电视机前玩游戏的背影。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csodajHfXAmcIuXicYx7c1S5ZTEwkvThRmHjzWkwCARjhRHA4ZG5vgIRw/640?wx_fmt=png&from=appmsg)

非常坦率的讲，整体效果和审美，是没有市面一些主流模型好的，中文字的错误率很高比英文大不少，审美和色彩，也有一点差距。  

我测下来，感觉他们是没有把文字拎出来单独做处理，而是非常实诚的直接塞给模型直接处理了，所以中文错别字比例会高一些。

但是优点也很突出。

那就是，这玩意开源啊！唯一一个能生文字的开源。

就智谱的Cogview4的效果来看，我觉得，他们技术肯定是没问题，最大的问题，还是数据集这块，审美确实差不少，但是如果你就把它当个底座，来重搞数据集，微调一个很牛逼的电影海报设计模型，那真的不是不可能。

**第二个特点，就是它的语义理解，还是真的有点东西的。**  

比如这些Prompt：

1. 8K超宽幅画卷，分四区域： 左侧：唐代城门，朱红城墙，商队骆驼穿行，匾额题“朱雀门”； 中左：西市胡商集市，丝绸瓷器摊位，人群熙攘； 中右：曲江池畔，仕女泛舟，柳树垂岸； 右侧：大明宫殿群，飞檐斗栱，晨雾缭绕。整体风格为工笔重彩，绢布质感。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csNYgktuKFeWbnyvxVJTMO1X0aib96EiavggpDjBDYx3FKSJlHCr0cWQgA/640?wx_fmt=png&from=appmsg)

2\. 一幅横向长卷，从左到右依次是远古狩猎营地、古埃及金字塔群、中世纪市场、工业革命工厂、当代摩天楼、未来垂直花园城。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4cs7FvGooIliaAu1lDicBmUSsXWbl2YBaYo2n4J2kvqqVhdS3c7DeZsCenA/640?wx_fmt=png&from=appmsg)

3. 一笼刚出笼的上海小笼包，皮薄馅嫩，汤汁丰富，摆放在精致的竹制蒸笼中。旁边是一碟香醋和一双竹筷，背景是木质的餐桌和一壶绿茶，体现出江南的细腻和雅致风格。江南风味，精致，雅致

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csKnoOyUokr0NEV39HiaJWKfml3yLhS7KU36U5NKTn0OL548QxQWp73tQ/640?wx_fmt=webp&from=appmsg)

4. 野径云俱黑，江船火独明。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4cswhGUO4RJPZVjU3ic3h10qicAuYnc1E9x3JpU9zliarow7WkTWkZ6mZ4cQ/640?wx_fmt=png&from=appmsg)

5\. 一张照片级真实感的奇幻毛茸茸汽车，车身完全覆盖着厚实柔软的白色绒毛，明亮灵动的车灯宛如一双友善的大眼睛，轮胎隐藏在浓密蓬松的毛发之中，夜晚散发出温暖柔和的光晕，呈现出魔法生物般的风格，细节精致，质感极度逼真，充满梦幻气息与温馨感，电影级灯光效果

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csiaMXW2KiaFSj29kicDicPGqnvApsUjvvHEYZf8NAygHwd4EZZCCSP3TYMg/640?wx_fmt=png&from=appmsg)

可以看到，美不美的另说，但是画的，是真的准确。

这块还是得益于，他们把T5换成了GLM4，这个还是爽多了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpMW6MVbdomAbyfEQicIwnXcHJ7o4rzHGaZdt5uCIviag93ErccEhiaPeiaw4aOO8gfBibs30mwCwIjjjA/640?wx_fmt=png&from=appmsg)

目前他们在出图的分辨率上，也没限制特定比例，2048以下几乎都可以无极调节，这一点还是比较爽的。  

后续，他们也会支持ComfyUI和ControlNET套件，还有微调的脚本。这个还是比较重要的，用CogView4来当基座模型微调的话，应该能玩出不少的花活。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4cs3ddBgYNYOczk6lxdncPBiaxdzlHpOibMY5S68Aiba6Ycuh1qmI8PRfXwA/640?wx_fmt=png&from=appmsg)

目前开源的这个模型支持Apache2.0协议，而给普通用户用的版本，也会在3月13日上线在智谱清言上，到时候可以蹲一下。

最后，我想聊聊智谱这个公司。

国内我之前有一个非常主观不客观的评价，我把五家公司放在一起，并称为开源五虎。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csN2Euwl3eC8edtwRv6GHLUtWA75ypmcX8GCJP8sjqDZkMTg1ia63XpiaQ/640?wx_fmt=png&from=appmsg)

其实在DeepSeek还没成立的时候，智谱就已经在kuku开源模型了。  

如果是2023年就开始玩大模型玩AI的，应该见过这个风靡一时的基座模型，ChatGLM-6B。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csH5KhIGVoSX2pVBWPcswicLNW5IWczno6Y5FSFpicQ3desmaDjRRgdFgg/640?wx_fmt=png&from=appmsg)

4w的星标，在Github上意味着啥相信大家懂得都懂。

那个时候，我还在公司里面做项目，微调了好几个不同的GLM6B，串成工作流来执行任务。

后续，他们又开源了非常非常非常多的模型，比如GLM-4、GLM-4-Voice、CogVideoX v1.5、CogAgent等等等等。

时光匆匆，一晃眼，两年了。

这两年，感觉到了智谱的纠结、智谱的挣扎，还有他们的摇摆。  

虽然在2024年的后半程，他们靠着AutoGLM和智能体，在整个AI圈杀出了一条自己的血路，但是在开源世界的声量，好像也被通义和DeepSeek压了过去。  

老骥伏枥，志在千里。  

在今天CogView4的仓库里面有这么一张官方生成的Demo图。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpbj9xtdNCicvwR8eqczP4csNmwloDDYNkT7R1U2ico8Sn3tSyx6J9CLcFkJObH9EBBArjtoFTl8dcg/640?wx_fmt=png&from=appmsg)

他们把2025年，定义为智谱AI自己的开源年。

不破不立，破而后立。

期待智谱拿下更多超级融资的同时，也能在开源路上越走越远。

毕竟，对我们所有人而言，每一家厂商的进步，都是让中国AI越发闪耀的灯火。

祝愿这片风云激荡的江湖，燃得更盛吧。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言