     DeepSeek开源第四天，一文看懂今天发的两个猛货。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

DeepSeek开源第四天，一文看懂今天发的两个猛货。
===========================

原创 数字生命卡兹克 数字生命卡兹克 2025-02-27 12:11 北京

> 原文地址: [https://mp.weixin.qq.com/s/0X8P9yCYFAWZXxF82\_NIzg](https://mp.weixin.qq.com/s/0X8P9yCYFAWZXxF82_NIzg)

最近肝到爆，一直以为昨天是账号建立两周年。然后回溯了下历史，才发现原来是前天。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnW8RB8QicefRpc0BOicmnGRVSBuUYeWjmjQpgltIB8opL6k0cLqH1q74ZQ/640?wx_fmt=png&from=appmsg)

我说25号是什么黄道吉日呢。。。

发了这么多篇文章，唯独把我自己忘了。

感谢DeepSeek的开源连击，真的感谢。。。

从FlashMLA、DeepEP再到DeepGEMM，开源的世界里真就闯进来一位大神。

老黄辛辛苦苦多年建起来的商业护城河上，DeepSeek居然明目张胆地开始架桥了。。。

但是说实话，DeepSeek的所有开源的项目，全部都是基于英伟达的生态做的，虽然大家戏称说DeepSeek比老黄更懂显卡，但是这些项目开源出来，我咋感觉大家跟英伟达绑定的就更深了呢。。。

说回今天（第四天）。  

他们又一口气开源了俩东西，还有一个性能分析数据库。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnWNcWJhShapmRTIfnAkSEc7lzjQNicBTbeWYSoqxt7IkSpSo1lGYUJVNw/640?wx_fmt=png&from=appmsg)

数据库就不提了，主要看另外两个。

一个能把硬件资源，再度榨干到极致的双头流水线DualPipe。

还有一个能平衡所有任务，把效率拉爆的EP调度器EPLB。

开源链接在此：

**DualPipe**

https://github.com/deepseek-ai/DualPipe?tab=readme-ov-file

**EPLB**

https://github.com/deepseek-ai/eplb

说DeepSeek牛逼已经说麻了，只能跪着给他们鼓掌了。。

先说DualPipe。

  

**一. DualPipe**

这玩意儿是一种贼新的双向并行算法，在DeepSeek v3的论文里面其实已经出现过了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnWCpania84hC79IF0PnzUnpqVSkjsJN5ic6HwOzHicMbtpR228ddHb1JbSg/640?wx_fmt=png&from=appmsg)

我用一个做面包的例子给大家解释一下这玩意到底干啥用。

比如说你家里是开面包店的，叫X利来，每天都要卖好吃的面包给大家吃大家也很喜欢你。

你家里呢，有一条面包生产线，就像工厂里那种流水线一样。

面包从揉面、发酵、整形、烘烤到包装，需要很多道工序，而且每道工序都要排队依次进行。

如果是那种单向的传统的流水线就会有一个非常der的问题：比如说一个人先把面揉好然后送给下一个人发酵，等发酵好了再送给下一个人烤，烤好了再送给下一个人包装。。。

这就导致每个人在等待之前那道工序结束的时候，可能都要等上一会儿。如果有几道工序比较耗时，那么后边的人就只能干等，没法同时干点别的，这就拖慢了整体产量。

所以为了提高效率，你就就会想，能不能让前面的操作和后面的操作同时进行？比如这个人一边揉面，另一边又有人可以烤前一批次的面包，不至于让所有人都卡在同一个步骤上面。

这其实就类似最基本的流水线并行思想，也是现在很多工厂的流水线方式，简称，工业化。

可是，这样也会产生一种所谓的“气泡”，就比方说等你揉面的人实在太多了，而烘烤那边一时没得可烤，或者反过来，烘烤还没结束，就阻塞了包装，一来一回会浪费一些时间空档。

这个浪费的空档，形象点说就像流水线上两个工序之间充了空气的“气泡”，它还是没有完美的提升效率，会让人有摸鱼的“气泡”空间。

普通的流水线并行，还会遇到一个问题，就是你的搬运。

比如说你家工厂太大，揉面机在一楼，烤炉在八楼，中间还没电梯。有时候揉面好了要送到烤炉，这个来回搬运也得干死个人，但是又不得不做。

所以，你还在加上搬运的工序，也就是在搬运的同时，炉子、揉面机啥的也都不能闲着。

你现在可以歇一会，来考虑一下他们的计算量，是不是非常的恐怖。

但是相比于大模型的计算，面包厂这个case的复杂度，就是小巫见大巫了。

而DeepSeek掏出来的DualPipe，就是解决这个问题的，就是如果带入我们自己的话，你就可以把它想象成一个非常黑心但又非常聪明的资本家。。。

DualPipe这东西，中文可以叫“双管并行”或“双向流水线”，它直接把整套的逻辑和计算设计，都给你做完了，找到了最优解，你不用想着每个工序怎么安排了，你直接用就完了。

它就是，调度之神。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnW2squGhSeyvENvQ4wPx3fdc3BWVicdejbTgMfJILcj1DKS7ZB6DYTfzA/640?wx_fmt=png&from=appmsg)

所以，DualPipe到底能把干活的人发呆的时间，降到什么程度？

来看下面这个表。

DeepSeek真是把一切数据都开源。

这其实就是一个干活效率对比表。

主要有几个数据：流水线气泡（浪费的时间）和参数（用的资源）、激活（额外用的内存）。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnWFZNGQm5bfoquIOSOGWYd3EicUNiaaHxNSMEwsf3QlSlKyHwzdkwTehtw/640?wx_fmt=png&from=appmsg)

能看得出来，效率最高，浪费时间最少。但用了更多资源（参数翻倍，空间多占一点）。

可能是为了适合需要超快速度的大任务，代价就是资源稍微多点。

快速使用方法，也给出来了，不过需要自定义一下。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnWkVqQf4JAAFxw0LyAS0DkQpGKxQ2qdWenicIgwsqbbgamhYDdA9LlM7Q/640?wx_fmt=png&from=appmsg)

我还记得老黄说自己是全世界最好的CEO。确实，一路给市值干到顶峰的人物。

但现在，DeepSeek要冲上山，走一条之前无人问津的羊肠小道，拔下那把勇者的宝剑了。

AI的世界，变化就是这么快。

没有谁是必须打到的怪物。

但挡在路上的永远不会是下山的神。

在开发者那一栏，还有个非常好玩的是，真大佬亲自下场了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnWbRIXwuPW0ZficBGhXY3iclcCiapA27mNswd24tw1XHmXMMOc3wsicfPsPQ/640?wx_fmt=png&from=appmsg)

  

**二.EPLB**

再说今天DeepSeek给的第二份大礼：**EPLB。**

Expert Parallelism Load Balancer，翻译过来可以叫“专家并行负载均衡器”，你也可以说是EP调度器。

还是举例子吧。  

比如说一个学校，现在要一起办2周年学校庆典。

一旦搞起这个庆典，我相信大家懂得都懂，就很繁琐。

会涉及到不少项目：布置会场、教室卫生、文艺汇演彩排、音响灯光调试、食堂伙食安排、礼仪接待……

各个项目可能都由不同的老师或同学去负责。要是这些项目的难度或工作量不一样，有些老师就会被忙得不可开交，而另一些可能比较清闲，这就不公平，也不高效。

那么这个所谓的“专家并行”就意味着，每个老师或同学都可以看作某个“专家”，专门负责一部分工作。

比如语文老师可能负责写文案，音乐老师负责排练合唱等等。

可是总会有一些专家特别抢手，比如PPT做的好的老师，那你肯定懂的，这绝壁是最抢手的专家。

于是这个专家就累死累活。要是能再安排两个PPT专家，这样就可以分担一部分压力，这个就叫“冗余专家”。

EPLB做的事情就是，根据统计到的每个专家最近一段时间的工作量，推测哪几个专家可能会特别繁忙，然后赶紧给它们“复制”一下，也就是直接给PPT大拿来几个复制人。

这样当需要调用这个专家时，一部分请求可以排到复制人那里执行，大家就不用都挤在同一个人那里里，工作可以被分散出去。

这就是影分身之术。  

然后还得考虑你的学校有不同的教学楼对吧，教学楼之间的距离比较远（类似节点之间用IB连接）。

同一个教学楼里的人肯定近的多（类似节点内用NVLink），所以让同楼里老师之间的合作肯定比跨楼去合作更方便。

EPLB就希望那些经常一起合作的“专家组”能放在同一个楼里，避免来回跑的浪费。比如有几个老师最常交流合作，那就得把他们都排在一个楼层，就能减少在楼间奔跑。

相当于在DeepSeek里就可以减少节点间的数据通信。

所以，总结一下，学校庆典马上开始了，EPLB会先数一数每个专家上个庆典忙了多少，比如看历史统计，某个专家被调用了100次，另一个才10次，差距很大，就说明前者更忙，需要复制，直接就火速复制10个数字人。

然后它要决定这些复制的专家该放到哪张GPU卡上。如果有两张卡特别空闲，就把繁忙专家的复制人放到这两张卡上，以便一旦有请求过来，不管发到哪张卡都能快速处理。

它也会尽量把同一组的专家都放到同一个节点（同一个楼），减少跨节点的大量通信。

这，就是EPLB。  

超级调度器。  

同样，DeepSeek并不只为了开源而开源，还给出来详细的接口和例子。

下面这串代码，就是这群聪明人，怎么安排工人干活的。

复制就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnWVIqPhgYpreBV8NHaav3wb7Ma3huez7qliaY2NobXYZufEAItz0Y390Q/640?wx_fmt=png&from=appmsg)

下面这个图就是他们，在专家少的情况下，做调度的策略（分层负载均衡策略）。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnWKBmqexvMG23mUYz4jhgiaZ4eaT4GPE0fxUVqpSfaDI9d8QGiaibWQCnkQ/640?wx_fmt=png&from=appmsg)

  

**写在最后**

早上这两发完以后，看到这，一堆在技术中摸排滚打的群友坐不住了。。。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoHuxVWU1JqCJU0iahwWtTnWictx8pbQBnkEs7oYpdGXUsXn0QVUUHV5clU76O7gDDeic9lHVSOxVjsw/640?wx_fmt=jpeg&from=appmsg)

已经懵逼。

DeepSeek这群人。

其实就像DeepSeek在X上的官方签名：

用好奇心解开AGI的奥秘，用长期主义回答本质问题。

DeepSeek开源的魅力就是。

能让所有人都品尝到AI这颗大树上开出的果子。

花木逢春。

中国，要春暖花开了。

感谢DeepSeek。

谢谢你。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、芝兰山

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言