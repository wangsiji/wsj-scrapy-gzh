     Midjourney全新模型V6 Beta版上手评测 - 终于到来的语义革命 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

Midjourney全新模型V6 Beta版上手评测 - 终于到来的语义革命
======================================

原创 数字生命卡兹克 数字生命卡兹克 2023-12-21 17:58 天津

> 原文地址: [https://mp.weixin.qq.com/s/XfEDTAd\_ZjAJdlaQC\_iUUw](https://mp.weixin.qq.com/s/XfEDTAd_ZjAJdlaQC_iUUw)

有点意外，Midjourney猝不及防，北京时间下午13:56，老美那边大概夜里10点，发布了新版的V6 Beta模型。。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vMvkDswWBBibWM22BuvhCd17GPERiajibnZza7M1Un538JYKoFicdp4mrQA/640?wx_fmt=png&from=appmsg)

他们是想趁着还没回家过圣诞，赶紧先发了。然后让大家一边过圣诞，一边给他们打黑工帮他们测模型。

这一下子给我发的，是着实的有点猝不及防。  

现在，你使用/setting命令，在模型选择框中，就可以看到V6 Beta版。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vb2DNibZM80k6lpjXu7uM4CXViaH4Srls172YDuV4FiasVzyW95z2OZ7eA/640?wx_fmt=png&from=appmsg)

按照Midjourney的话说：“This is an alpha test. Things will change frequently and without notice”

“这是一个阿尔法测试。事情会经常发生变化，恕不另行通知。”

包括提到了“速度、图像质量、连贯性、提示跟随性和文本准确性将在接下来的几周内得到改善”  

我猜测模型完成度在85%左右，剩很多对齐工作没搞完。

官方说的目前V6 Beta的更新内容：

_1\. 更准确的提示跟随以及更长的提示。_

_2\. 提高连贯性和模型知识。_

_3\. 改进的图像提示和重新混合。_

_4. 较小的文本绘制能力（您必须将文本写在“引号”中，并且 --style raw 或较低的 --stylize 值可能会有所帮助）_

_5. _改进的升级器，具有 'subtle ' 和 'creative ' 模式（分辨率提高 2 倍）__

有点太废话，我翻译成人话就是：能容纳更多的词语token了、语义理解更强了、图像质量更好了、能嵌入一点英文单词进去了、图像能放大更多了。

我跟上百个群友一起跑了三个多小时，整体感受最大的变化其实还是两部分：

**图像质量的提升与语义理解的加强。**

我拆开聊。  

 **一. 图像质量的提升** 

图像质量我关注的是以下几个纬度：细节密度、材质质感、色彩表现、光影表现、构图表现、结构真实性。

Midjourney V6 Beta在细节密度、材质质感、光影表现、结构真实性上，都有巨幅提升。构图表现和色彩表现有小幅提升。

直接放对比图，没啥可说的了，部分图片来源于好基友@鲜虾包、@猫宅V酱、@大峰AI绘画。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vHe5FjCt06fAFZGOBR8Tvx1t9AicyzbhSEwsHAtLWRmSibpicsql5t40Vw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vyJDguITaicxib1jY1bGJWnCoHtxWecf80CDd1Kpvqib2hDuia9hpWowncg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vdoxF8Vm6ibtDeY0UC1TZSh0Wc9ZSPtk9ghDXvia3jjibtsN4579ic6FwoQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33v22nMibLwDmVYnl0iafSHYhKGDtKK2CnEb9sMbMQ0XLME2YcibuUzzCVuQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33viaFAnPuEW38RydQlN8DqZCDo4frtvNhNKFQHicuPfUXNdiaV9Jg8qicODg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vGXqZ6fE2OtCmqXr65hHmCg7viaDHiaNIk8dvsNPy9oHNQuwJkpichdpjQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vQ6pODb2w4w3Fu4R4nom8RPWPbvSrdz4pwcwfWCGqgX6cPib2KSNMPMg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vAB7lF92s18AI02a48xHhicPWfj3xfAYqMCBcibvvicuAnOnV7CdE9RIiaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURrGVvhk80NYW55ib8paVE33vsKMkaSibcVBGoetbDOJkPiaU2CsXXT3Dr9IkOK3PiaRHwJcQcTxVd9FBQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vYe7ya6FevibtnWEadvkBh3GDeZTX07HM3znzEiaZLjLTkkjx6rgjCYMg/640?wx_fmt=png&from=appmsg)

就不放太多了，反正核心思想就一个：图像质量up up 还是up。  

知道在细节密度、材质质感、光影表现、结构真实性上，都有巨幅提升就行了。

下面一趴的语义理解才是最核心的重点。

  

 **二. **语义理解的加强**** 

我重点来聊聊语义理解这块的变化。  

我曾经毫不避讳的骂过Midjourney，他的语义理解就是一坨屎。让我在做过往的AI作品时，无数次的带上痛苦面具想砸电脑。

但是这一次，Midjourney V6 Beta对于语义理解的加强，终于到了中上游可用的地步，注意我用的词是“可用”。跟Dalle3这种逆天的还没发比。

首先请忘掉所有的SD式的写法，不要写tag，不要写“photorealistic, 4k, 8k”之类的垃圾词，他们对于新版V6 Beta没有任何蛋用。  

**不要写tag，不要写tag，不要写tag，重要的话我说3遍。**

更别直接用v5.2的prompt直接拿来复制粘贴，请重新学习新版V6的写法。

整体上，我觉得更强调把细节说清楚的能力。我推荐的结构是：

场景+主体+细节+美学风格。

比如我的这段Prompt：

三个不同的美女朋友坐在沙滩上面向镜头微笑。中间的是一个开朗的金发白人女性，穿着短裤和红色背心。左边的朋友是一个黑发美国女孩，穿着比基尼和透明的裙子。右边的朋友是一个红发英国女孩，穿着比基尼。背景可以看到海，海上有船和飞翔的海鸥。Agfa Vista 200拍摄的中景镜头。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vMfF584O5I0H6JA8kPU1Rw4ibho64bnZPD9OwoX0pib8XBa5lr1JjEtJw/640?wx_fmt=png&from=appmsg)

非常复杂，但是我几乎都是以长句子去写的，清晰的描述场景和主体以及部分衣服细节。  

再看看v5.2，可以就语义理解上，做一个清晰的对比。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33vib9kbF7gCGUn5fz8Y8GQV7O1qicTIZfjPzsJfQsVj6pkY3ZET8PcBAibA/640?wx_fmt=png&from=appmsg)

在新版prompt的写法上，我说一些我认为有趣的技巧：  

**1\. 你可以指定任何细节。**

不要吝啬你的想象力，更不要吝啬你的笔墨，用一切有逻辑、有结构的语言，把你想要的细节指定出来。她穿了什么衣服、衣服是什么材质、什么颜色。写明白，写明白比一切都重要。  

比如：

漫威黑寡妇的半身特写镜头。黑寡妇穿着蜘蛛侠的黑色紧身衣，她的左手拿着美国队长的盾牌，右手拿着雷神之锤，她很悲伤。--ar 16:9

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33v8C1rE6kbAYHquDDZPFwXiccj0XIB6ThjzdSNHBpUVH8LnkV1obY0icCQ/640?wx_fmt=png&from=appmsg)

**2. 你可以使用语言控制构图。**

在V6中，现在很容易用语义去定位事物之间以及与相机的关系。这个在V5中几乎是难以想象的。

现在我们可以用短语描述一个通用的图像，以这个通用图像为焦点。围绕它填充细节。

比如：

客厅的桌子上有三个装满水果的篮子。中间的篮子里装有草莓。左边的篮子装满了橘子。右边的篮子装满了芒果。背景是一个带有圆形窗户的空白蓝绿色墙壁。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33v0vjsia5BMw904uHFH1Kmcm6wMc1yGuuiajovglzTFqBwBxrD2piafFICQ/640?wx_fmt=png&from=appmsg)

**3. **你可以向你的图像中添加文本**。**

Dalle3的老传统了。可以给你图像添加文本，将需要嵌入图片的文字放在 “引号”内，并且保证你描述的画面上适合嵌入文本。比如你非说要在她鼻子上写个“shabi”，那写不上去你也不能怪MJ对吧。

比如：  

特朗普在苹果发布会上的特写镜头。他在人群中举着一块写着“SHABI”的牌子。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrGVvhk80NYW55ib8paVE33v4GGjg8k9ZWAKR6vHxO0mp0hOXNDcfBPbE08NM93n2Tv58icOIIOG0xw/640?wx_fmt=png&from=appmsg)

  

 **写在最后** 

Midjourney V6 Beta带来的有趣是一定的，对真实感和图像质量的加强，基本到了现在所有AI绘图的颠峰，再配上独一档的审美，以及史诗级的语义增强。

可以看到，Midjourney未来正式版V6的推出，一定又会开始“遥遥领先。”

诚然，问题还很多，比如对于其他的风格加强好像并不明显。  

比如很多功能都还不支持。

但是瑕不掩瑜。

Midjourney V6 不是AI绘图的最后一步。

而是又一次AI历史长河中的丰碑。  

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言