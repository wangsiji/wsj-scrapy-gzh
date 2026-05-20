     DeepSeek开源最后一天，大鹏今日同风起。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

DeepSeek开源最后一天，大鹏今日同风起。
=======================

原创 数字生命卡兹克 数字生命卡兹克 2025-02-28 10:49 北京

> 原文地址: [https://mp.weixin.qq.com/s/pOPOGNbXbUkBir\_uA\_tpbg](https://mp.weixin.qq.com/s/pOPOGNbXbUkBir_uA_tpbg)

弄完OpenAI的GPT-4.5，已经是7点多了。

但是感觉我真的有罪，我居然熬夜就为了看这个大垃圾。

虽然很想睡觉，但，今天可是DeepSeek开源的最后一天。

之前，连续4天，5个硬核项目，FlashMLA、DeepGEMM、DeepE、DualPipe、EPLB，两万多个Github星星，这都是全世界开源小伙伴们的倾情贡献。

既然已经肝了4天了，那最后一天，我才不要错过。

等到早上9点，DeepSeek如期而至。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryhAvm1EamqQic08J4qwomeCr0GVvRjRic5KldncOcYJIlVkRUutciabV8yn6R7wmzYcNBJ49uO30vg/640?wx_fmt=png&from=appmsg)

这次，他们开源的东西还是极度硬核：

**3FS（Fire-Flyer** **File System****）**

链接在此：https://github.com/deepseek-ai/3FS

还给了一个基于3FS的数据处理框架：

**Smallpond。**

https://github.com/deepseek-ai/smallpond

先说3FS。

简单来说，3FS就是一个专门AI模型和推理做的文件系统，只不过，它是分布式的，性能太强了。

昨天是面包厂，那我今天，在用奶茶工厂来给大家举个例子。

比如，你是一个奶茶世家，经营着一家超大规模的超级奶茶原材料工厂，开的贼大，专门给喜茶、霸王茶姬、CoCo、茶百道、蜜雪冰城等等全国各大奶茶品牌供应原材料。

每天有上万家门店等待着你的各种果汁、茶汤、蔗糖、珍珠、椰果啥的全都得从你这儿以极快的速度输送过去。

因为一旦原材料供不上，各家奶茶店就没法及时出茶，排队的顾客就得锤门店，门店就会来捶你。

而切大家的配方比例是要严格控制的，一旦某些配方仓库搞混数据，比如喜茶家的葡萄果肉和茶冻比例调错了，或芭乐瓶里面的原料配比发错了，又可能要被顾客捶。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryhAvm1EamqQic08J4qwome6P3ibXjYGbhh5keUWbJJlcGgqBAP1aGy2tnAdoqpxDic2lxXESeaHNJg/640?wx_fmt=png&from=appmsg)

所以你可以想象，这工厂听着就很牛逼很复杂对吧。  

所以你为了保持整套工厂是靠谱的、准确的，不会被各大家品牌方捶，你就需要一个无比宽敞、极度智能的流水线+库存网络。

这就是你的究极智能奶茶原料分发系统。

而3FS（Fire-Flyer File System），就是你的这个究极分发系统。

每天都有成千上万的奶茶店要来仓库调取、回传各种信息，比如店家库存不足时要申请更多原材料，原材料运到门店后又需要登记消耗情况，遇到新品上线还要紧急调度不同产线来增产。

所有这些海量数据读写都得在极短时间内完成，否则延时太高就会造成门店断供或生产线浪费。

3FS不仅能把所有的分发全部处理掉，而且延时极低。

核心技术就在于，我们在厂区里安插了大量全新的高速自动化储物柜（这就是SSD），这些储物柜随时能被调度，门店的所有配方、原材料需求等信息都是数字化的，一按按钮就能知道哪里还剩下多少牛奶，哪里的茶叶正处在发货阶段。

而且，我们还造了一堆的光速传送带（RDMA），不需要过多的中转，一旦原料从储物柜那边这边发出，直接可以到达对应的节点，而不用像传统的先装车，然后普通货车开一大圈，再交给搬运工二次处理。

效率拉满。

同时，我们这个工厂，把原材料加工区和原材料存储区分开，还把各种茶叶处理流水线和配料混合区都搞成了独立模块。

当某天喜茶或者蜜雪冰城研发了一个新品，门店突然给你下单了一个全新的配方，需要一种新的组合了，也没关系。

3FS让你不必关心这个原料是存在哪个仓库、由谁负责加工，因为在逻辑上，你可以看作整个工厂就是一个大同心圆，任何角落都能直接访问存储资源。这叫 locality-oblivious（不用再因为地理位置不同而做繁琐的调度），相当于你只要告诉工厂我要一批A茶叶和B奶盖，系统就能自动把所有加工、分发环节安排好。

对你来说几乎毫无感知，就像整个工厂是一个统一的池子。

这就是3FS的“分离式架构”。

现在再回去看DeepSeek给出的介绍，是不是就大概能看懂，知道这玩意是个啥了？

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryhAvm1EamqQic08J4qwomeYMgQ1h1iaJJJhBpia277icePicwySuvZoRLFuchskXOv7j1gibE3ic4LfQWw/640?wx_fmt=png&from=appmsg)

再看看3FS的实际表现。  

也比较炸裂，性能直接拉满。

现在我们假设，你家的这个奶茶工厂，有180个高速自动化储物柜（存储节点），16个超大容量（14TB）的冷冻箱（NVMe SSDs），还有两个超快的光速传送带（200Gbps InfiniBand网卡）。

那在3FS的加持下，这个奶茶工厂，它1秒钟能送出6.6TiB的原材料。。。（1 TiB约等于1.1TB，有个有个换算关系，1TiB=1024GiB，1TB=1000GB）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryhAvm1EamqQic08J4qwomeTFjniaXViaISdKDPhPzhCyqSlEq88t4zS5WmC3oAzrl7Gduibf8x3NzSg/640?wx_fmt=png&from=appmsg)

这吞吐量是啥概念呢？

约等于你可以一次性加载数千部高清乃至4K影片，一部 1080p 高清电影大小在2~3GB，4K电影大概10GB往上跑，以6.6TiB/s的吞吐来说，一秒钟就可以把几百到上千部电影打包塞进内存。

6.6 TiB/s已经属于往里塞东西时，硬盘都来不及转，网络都快成瓶颈的级别。

在现实的大规模分布式集群里能跑到这种速度，说明它已经把SSD和 RDMA网络的优势榨到极致，远超一般人日常认知的网速或存储吞吐。

然后还有一个KVCache，其实就是优化大模型推理过程的技术。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryhAvm1EamqQic08J4qwome9icDPhcyxXrAhQ4ibaB6XiacRW8iaMMgqJp15MSpnwcoFKohOtTicWAhclQ/640?wx_fmt=png&from=appmsg)

KVCache 的读吞吐能飙到40GiB/s，也就意味着，当大量门店需要不断查询某些关键库存或实时交易数据时，3FS依然能挺住。

不至于像传统系统那样面对上万次请求就卡死。对比之下，其他系统要么没有足够的带宽，要么在同时进行移除垃圾或归档时会大幅拖慢读取速度。但在3FS这套工厂体系里，即使一边有人清理过期原材料（GC IOPS），另一边的订单读操作也能流畅进行，互不掣肘。

如果只看平均速度，那也稳的不能再稳了。这玩意儿最可怕的是，上下限都极高。

整个3FS就像DeepSeek开源的老作风，他们把所有使用教程统统给了出来，真是生怕我们不会用。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryhAvm1EamqQic08J4qwomemvAPicMxtQ1wjyibYkc3bahTLSeUZia3y6PPqicLHHAqCNgp9TNicVWz0uA/640?wx_fmt=png&from=appmsg)

我还发现个好玩的，除了上面这个使用操作，还有个说明书大礼包。

就在这。设计笔记、安装指南、API参考、详细参数表都一应俱全。

安装指南这部分，还给了一个测试集群，随便运行。

我甚至以为DeepSeek，不想把日子过下去了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryhAvm1EamqQic08J4qwome5t4haGDkRmZQxMpfpEibBVJzpAb9uUQkNKib0ibbBjMrBqNwnZO0x8UCQ/640?wx_fmt=png&from=appmsg)

再回过头，提一嘴开源的另一个东西，**Smallpond。**

简单来说，这是一个特别轻量化的、但确实厉害的数据处理工具，基于DuckDB和3FS打造的。

比如，你可能想知道，哪些门店最喜欢什么口味？要从几十TB的销售记录里跑SQL查询统计，这在过去可能得搭Spark、Hadoop又或者别的大型分布式系统。

但现在，smallpond就能搞定了。

特点一共三个：

处理数据太快了。

能处理PB级（也就是千万亿字节那种牛逼的级别）的数据。

用起来确实省心，操作简单不费脑子。

它背后最大的功臣，还是3FS提供的高并发读写和存储共享能力，以及 DuckDB提供的高效SQL执行引擎。

所以，smallpond+3FS就是绝配，一个负责调度数据加工，一个负责高速数据通道，让PB级别的数据处理变得像做一杯奶茶那么轻松，真的。

Python 3.8到3.12版本就能用。DeepSeek一并把操作链接放下面了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryhAvm1EamqQic08J4qwomefZCXHBQtgfZLNyLgoOlCOEvLJiahlal62Vtp6hfIJgH5hRl3vicPJypA/640?wx_fmt=png&from=appmsg)

总结下这几天。

这几天，DeepSeek对老黄的GPU，下多少猛料了？

在V3刚出来时，本来大家觉得。

一张好卡，是不是没那么重要了？

马斯克在孟菲斯的万卡集群是不是不用搞了？

但你回过头来看，会发现：

DeepSeek跟老黄的命运，扯的太深了。

英伟达的卡，尼玛有无穷的优化潜力啊。

这下，为期五天的DeepSeek开源节正式华丽落幕了。

但是，新的英雄之旅说不定现在才刚刚开始。

路漫漫其修远兮。

吾将上下而求索。

深度求索DeepSeek。

想必也是抱着这个信念。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、芝兰山

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言