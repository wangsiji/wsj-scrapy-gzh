     美团也开源了大模型，但我觉得他们的野心是通用生活Agent。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

美团也开源了大模型，但我觉得他们的野心是通用生活Agent。
==============================

原创 数字生命卡兹克 数字生命卡兹克 2025-09-04 09:00 广东

> 原文地址: [https://mp.weixin.qq.com/s/CdjSv1CGetZqn79TrL7lHA](https://mp.weixin.qq.com/s/CdjSv1CGetZqn79TrL7lHA)

起猛了，美团这下真的开始明牌干AI了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURox5iaAicmibcgTK4LM300hoYxB0LwcgRodyicRQ87Xntbk4496wrICwz69plw0x04IgQEbcpYI6A8oGQ/640?wx_fmt=png&from=appmsg)

居然，发布并直接开源了560B参数的MoE模型LongCat-Flash-Chat。

好家伙，WAIMAI里有两个AI，这次成真的了，美团真发大模型了。

开源地址：https://github.com/meituan-longcat/LongCat-Flash-Chat  

也有线上体验地址：https://longcat.ai

我自己去体验了一下，整体模型能力，中规中矩，但是快，是真的快，能把560B的模型，在推理的时候搞得这么快，是真的有点牛逼的。

我直接录了个屏给大家看一下。

这里我们可以直观对比一下LongCat和DeepSeek V3的输出速度，API其实更好，但是这里就直接用的网页版了，更C端用户一些，能直观的看到效果，他两也都是MoE，而且参数量差不太多。

为了更公平的竞争，用了同一个问题，并关闭了联网搜索来避免搜索干扰。

先来看DeepSeek。

DeepSeek每次还是需要原地转圈圈思考一会儿，然后才一个一个的往外吐字，挺急的。

耗时整整33秒。

再来看LongCat，这刷新率不用多说了吧。

像机关枪一样哒哒哒的五六秒就输出完了。

这是LongCat和DeepSeek的另一个case，DeepSeek思考的功夫，LongCat答案快写完了。

非常直观的对比。。。

我又测了一下写作和代码。

先是做了一个新的小游戏，弹射线游戏，核心玩法是操作小球来躲避不同方向，不同速度的避弹射线，存活时间越长分数越高。

整体还行，这UI以及弹射线的设计还是很有艺术感，碰壁反弹也遵循了正确的物理规律，甚至在碰撞时会迸发好看的火花。

然后，我让LongCat写了篇小说。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVryvOott00J9xBCe0nYYELoCWibn3UqKMsQRhGwl9tbfXmGlZpUSTjHQ/640?wx_fmt=png&from=appmsg)

全文比较长，我把完整版贴在这里，大家可以看看。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVZj5rGgIflglKicf8aXCK9KWGJRLR4LHicVoueRKiaHGzQ8d6nictTkfyrw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVhbK8X3NaSZib9ZnCYzYsTV9ibHYRTTgib4BnEwCvia3uBhkiaJRv6xBQebg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVIUUzFQdFo0HsAlSopwLffTrpxqKYA4wGW6DXRKRHRniaturutibg9Mcw/640?wx_fmt=png&from=appmsg)

我还挺喜欢它写的那句话的：在宇宙的尺度下，孤独是一种常态。

我还让它写了一个北京美食地图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVuMicR2icoskf6j1u4D409hCicaaQS6qI3ukVEQ70mjvSIpAhEeo40IicLw/640?wx_fmt=png&from=appmsg)

不愧是美食世家出身的大模型，写的很细。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVh5hHEuedicTRCS4a2HQFM8If9GqJgudS9ygDfU3icamddCnEyV41zNqg/640?wx_fmt=png&from=appmsg)

但是，我觉得最有趣的东西，其实是他们技术报告里的。

Agent能力。

很多人都在说LongCat快，确实，它的速度极快，但是，他们的Agent能力，也极强。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfnJRgPibLH6Ak4QJtPLNkp7EzleiajwVcHiapU5CbIibdjyS3WUfUbPEqdAUH4LSvickmJxNDuYIyrlQ/640?wx_fmt=png&from=appmsg)

直接登顶了。

我自己一直在说，AI现在很多时候，离我们普通大众太远了。

大家都在卷生产力，卷写报告，卷做PPT，卷科研，这些东西当然很重要，但，它离我们真实的生活，总感觉还隔着一层。

大家都生产属性了。

但是美团做一个Agent能力如此之高的并且超级快的大模型，我个人觉得，他目标就是为了服务自己的业务去的。

为了服务所有C端用户的生活场景。

有些事，你得连起来看。

不知道有些人知不知道，你在美团点开搜索框，现在是有AI模式的搜索的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVSGyoQkn1HANKchDCpb7fyCWnOUQlWwM4n5NOY2lgib34hnicypTSMClw/640?wx_fmt=png&from=appmsg)

它跟你传统的搜索完全不一样。

你不再需要去想“火锅”、“烤肉”这种关键词。

你可以直接跟它说人话，比如：“我想找个适合哥们儿几个喝酒撸串、人均一百左右、离我最近、现在还开着的烧烤店。”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKV0AoxvJ3qGY3ic2ZibNreu6R9XO1tcIeqokzpWk0c0xAIwAL9iaF2WhmPw/640?wx_fmt=png&from=appmsg)

你看，它会立刻理解你这个复杂的需求，然后把最符合条件的店铺，直接推给你。

而且，前段时间，他们也开始内测一个对我们社恐人士非常非常有用的新功能。

AI帮订座。

你找到一家想去的餐厅，点一下那个“AI帮你订”的按钮，然后输入你的需求，比如“今晚7点，4个人，要个靠窗的座”。然后，就没你事了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVdvcnNK1MVcTHrVxyyicmkm0KgkFXgBDv05go7kx3snnEhKhalS0HA9w/640?wx_fmt=png&from=appmsg)

  

美团的AI，会自己打电话给餐厅的前台。你没看错，是真的打电话，点开沟通明细，就能看到它跟前台是怎么说的。

真的会用一个听起来几乎和真人一模一样的声音，去跟前台沟通，帮你预定。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoR7yXv7CWgybpJZpsxclrrEhaIzlRdWWIBPoxzDrYng9k42gRxZX3NDtEXib0LXhHYAGhvhcr6LSA/640?wx_fmt=jpeg)

  

还有美团里的AI开发票，也是一个逻辑。

你点完外卖，不再需要跟商家打电话，直接让AI去帮你搞定。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8djAybhNZaKlkAy5pZLKVB53QZD6491hy7mQ1IMfQwrYYHMlyGcopNustC4L9JSfL0eLONlX7Mg/640?wx_fmt=png&from=appmsg)

  

这些，所有这些已经在美团上落地、或者正在内测的AI功能，它们有一个共同的特点：

全都是为了C端用户，为了生活场景，为了解决我们这些普通人，在日常生活中那些最具体、最琐碎的痛点而服务的。

这一切的布局，感觉都像是一块块拼图，正在拼出一个巨大的、清晰的图景。而这个图景的目标，就叫：

通用生活Agent。

放眼整个国内，好像确实也没有比美团更适合来做这个产品的公司了。

AI最缺的是什么？场景和数据。

OpenAI做Agent，它很牛逼，但它能帮你订一张从北京到上海的、下周二的、靠窗的高铁票吗？它能帮你找到你家楼下那家新开的、评价最好的兰州拉面吗？

它不能，因为它没有这个数据，更没有打通上下游的交易系统。

但这玩意，美团可太擅长了。

它的背后，是全国几百万家真实商户的实时菜单、库存、营业时间。是几亿C端用户每天产生的真实交易、真实评价。是几百万外卖小哥每天在城市里穿梭，构成的最鲜活的、动态的物理世界数据。

换句话说，别人是拿AI，辛辛苦苦地去找应用场景。而美团，是用无数个真实的应用场景，反过来，去养它的AI。

这是一个正向的、可以无限循环的飞轮。用户在美团上用AI的次数越多，它的AI就越懂你的需求，推荐就越精准，服务就越贴心。而服务越好，你就越离不开它。

现在，我们再回头看美团发布的那个560B参数的MoE模型，LongCat。

你就能瞬间明白，这个特点就是快和Agent能力的模型，背后的深意。

为什么要把它做得那么快？

因为生活场景的交互，是即时的。你点外卖，你订酒店，你打车，你不能等。

古典的交互设计师可能都知道，你设计产品交互时，最接受不了的，就是产品的卡顿和延迟。

一秒钟的延迟，都可能让用户直接关掉App或者放弃这个功能，快，是C端产品能够被用户接受的生命线。

只有足够快，用户才不用等。

而模型为什么突出Agent能力？

因为生活服务，本质上，就是一连串复杂任务的组合。

订一顿餐，背后需要理解你的口味、预算、位置，然后调用餐厅信息，规划外卖路线，最后完成支付。

订一张票，背后需要理解你的时间、目的地、偏好，然后调用票务系统，完成预定。

这些，都不是简单的知识问答，这全都是需要理解、规划、调用工具、执行任务才能完成的Agent行为。

还有一点，就是便宜。

LongCat的输出成本5元/百万 token。换句话说，它不希望用户花几百块的成本全网比价，而是只做几块钱的生意。

所以，当你把所有的点练成线，就可以看到，美团几乎就是在明示天下：

我们做大模型，从第一天起，瞄准的就是ToC的通用生活Agent，而不是所谓的，知识问答。

所以啊。

我觉得，别小看一个做本地生活起家的公司，更别小瞧那个每天给你送外卖的平台。

它可能，比任何人都更懂，人类真实的需求和期待。

它不是要带我们去火星，也不是剑指AGI。

它是要让我们，在这个地球上。

活得。

更像一个被照顾得无微不至的人。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、Qodicat、水杉

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言