     实测完DeepSeek发布的新模型，我觉得AI编程的全民普惠时刻到来了。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

实测完DeepSeek发布的新模型，我觉得AI编程的全民普惠时刻到来了。
====================================

原创 数字生命卡兹克 数字生命卡兹克 2025-03-25 06:08 北京

> 原文地址: [https://mp.weixin.qq.com/s/fxzb8m-THjyzdOlXPuCFnQ](https://mp.weixin.qq.com/s/fxzb8m-THjyzdOlXPuCFnQ)

DeepSeek深夜偷袭。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2EN3Kh0vbkOZpP14KLwye9Tx9W2yvxjN2tq7RgYcAMWvEFebcOHSqiaOtw/640?wx_fmt=png&from=appmsg)

昨天晚上，他们的v3模型，有了一波更新，版本号到了DeepSeek-V3-0324，而且是直接开源的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENic0rZRgGHCiayg24ichaIptYOGCwUd4PHwKaqVjXp0n7T4aAJZic1SbhPA/640?wx_fmt=png&from=appmsg)

没有跑分，啥也没有，就直接裸上的。

我第一时间实测了一波。

自己部署肯定不可能自己部署的，参数量不是我这种5080的垃圾卡能跑的动的，然后本来想着用硅基流动，结果他们没上= =

最后用的方案，是OpenRouter+ChatWise。

OpenRouter第一时间提供DeepSeek-V3-0324的模型支持，卷的起飞。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENjXMC7ibs0GNcwF5d2nhBj4tAQTlv6BzBibLqJpqGHaAdhKSv8nWiawibLQ/640?wx_fmt=png&from=appmsg)

而ChatWise当前端界面，用它的原因特别简单，它不仅能接入各种API。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqttBqFBufy1WlOlonvRic8awDuMZj7MHVSSGlG2c7uZwAIHXO5UtHs3SbPyXW1ibto7nepzfaia60DA/640?wx_fmt=png&from=appmsg)

还有一个很有趣的功能，叫做Artifacts。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENmaKicOqrd8D518nfoPxTnSe38VMjGibeY6ApYP5iajaPwZ0kRULUaGwYw/640?wx_fmt=png&from=appmsg)

跟Claude那个右边预览的窗口是一样的。

能做到指哪打哪，所见即所得。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENzc7Tl8wn6djTeQWicsdGTwhQL0XczJ6eGsvK6jVTX27A7Zkx0xBfqdQ/640?wx_fmt=png&from=appmsg)

这两个产品的网页在此：

https://openrouter.ai/

https://chatwise.app/

有需要的朋友可以自取。

目前OpenRouter上的DeeSeek-V3-0324是免费的，可以随便用。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENERwiaicrwNkIEU32zTibsiauecRic9dgichVPRNdt9MxEVX9U9q7bZWl3gAA/640?wx_fmt=png&from=appmsg)

再来说说DeeSeek-V3-0324的更新结论。

参数层面几乎都没有变，比如原来的v3是128k上下文，现在还是128k上下文。

最牛逼的进化，是新v3的代码能力。

生成的前端代码质量和审美，效果甚至能追上一点Claude3.7了。

能力大概在Claude 3.5 Sonnet到Claude 3.7 Sonnet之间。

我用一个朋友@洛小山的case举例子。他是做游戏出身的，所以在模型的代码能力上，非常喜欢用游戏来做case。

这是他的一个弹球游戏的Prompt：

    创建一个红白机风格的"像素弹球大师"游戏，包含自动演示AI功能，使用纯HTML/CSS/JavaScript实现为单文件：

先给大家看目前的AI编程王者Claude 3.7的效果。

游戏网址在此：https://jyt0pm2v2l.yourware.so/

超级酷，UI正确，规则正确，有特殊道具，1个球还能变成3个球，声音和AI模式也都加进去了，路径的规划也超级无敌，我看的最爽的解压时刻，其实就是接住3个球的时候，一个都不漏。

而且有一个特别特殊的规则，它也写进去了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENhVCkPsvDEhvtiaXfgsgbAn6ibeSGkacyuLIftQxibYQYH7IgfvEn7YQUQ/640?wx_fmt=png&from=appmsg)

就是偶尔的不完美。

所以你才会看到，它有时候刻意在漏球，刻意接不住。

Cluade 3.7，不愧是王。

我们再来看看DeepSeek新版v3做的。

说实话，在效果上，肯定是跟Claude 3.7有一些差距的，这个需要承认。

包括在游戏UI的美观上，AI模式还有BUG拖不动，特殊道具也没有等等。

但是它完成了，是一个游戏，是一个能玩的，而且还不错的游戏。

在这一点上，就已经很酷了。

而且游戏，毕竟是非常难的case了，再看看其他的实测。

比如我要做网页，我想让它整个活，做一个牛马时钟。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENoAruva7NxyCMmsykgqicXFjj142XJ1SKt4hqWPPfoAVrfaNFuuvwdVw/640?wx_fmt=png&from=appmsg)

而这个牛马时钟，做出来非常的搞笑，非常的抽象。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENzcsq3kKLkfwpIhNXDqvMDWv6UqLDMyP56A4w4NQt8PRNibd9YQMsAsQ/640?wx_fmt=gif&from=appmsg)

真的就是牛马来回切换啊。。。

非常的符合牛马时钟的题意。

又或者，可以让DeepSeek v3，直接生成一个有趣好玩的背单词html页面。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURo1gtyAAsdySwFhPBiavw2EN33uy0wZCCVcMY73LXSaCNjRfwQibw25rgjuSkZvBeJvq8CEWIYCzfAw/640?wx_fmt=gif&from=appmsg)

不仅做到了游戏化界面，甚至还有N多动效。

最酷的是，甚至这个背景图，都是它自己写出来的网址。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENFaHOSgggn4KvVXDaAy3lmmETmq31ClWEwzNXwveTLJiaOiavnaleADFg/640?wx_fmt=png&from=appmsg)

太牛逼了。

这些是比较难的互动部分，Claude3.5刚出来的时候，那时候我记得最火的东西，是李继刚的“汉语新解”，我不知道还有没有人记得，那个东西长这样。

![图片](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoCMf7ia5pRqbKLovyXfsFYu1QictFDNYYNu4pXicp25MHV1HHzCW1THVKYDB7b2yzicDdtbvMaOmPooA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

而现在，DeepSeek新版V3，在审美上，也可以做到这种效果了。

这张图，由DeepSeek新版V3直出。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENSWMgzdDXwiajhE3LKY6OgaRpSo4aU5urBUOlVzibOGYhdNMDJ2gHYXrw/640?wx_fmt=png&from=appmsg)

无敌棒好吧。

网页的审美，也很棒，终于不是之前土不啦叽的审美了。

比如我说一句特别简单的prompt：“写一个精美的落地页，内容是deepseek v3发布。”

这是上一版v3干出来的效果。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENibL0ar5sPudCl9Z3zX8xzG8HPHbueNvgicOan818831TefUyw1sdDD6g/640?wx_fmt=png&from=appmsg)

真的，丑的我不忍直视。

而DeepSeek-V3-0324，不说是那种专业级的UI设计师的级别，但是至少是好看的，能看的，是有设计感的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENkFjRmB6dNJSvt2cDSWhmHUGn63rciaQY9cjC7Ja6e2M6p0Hbia4u7tSA/640?wx_fmt=png&from=appmsg)

这差距，一眼就能看出来，没有什么比视觉效果，更直观的对比了。

前段时间很火的文件转可视化网页，很多人看了教程，但是苦于必须用Claude3.7，找不到门道，没法用。

但是现在，DeepSeek新版v3，直接完美复刻。

比如我之前用的这份吃瓜文件。

![图片](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoARicLpj3qOz9iaONsjxELGAvEc1W0KkibZaYmJU8PlzXeia4zibxmJbIhib83AqlAZkM6X02pjVWm0LSA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

直接把PDF传到ChatWise里，选用DeepSeek-V3-0324，加上藏师傅的这段超棒的Prompt：

    我会给你一个文件，分析内容，并将其转化为美观漂亮的中文可视化网页：

你就能得到一个，超酷超级好看的吃瓜时间线的可视化网页。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENunrZkngR1ZRaVySDnZK93dREW3TicQZ5ZgHH3QVanvpOaChoyywiapQw/640?wx_fmt=png&from=appmsg)

在这个关键的时间点，DeepSeek又用自己的技术和硬实力。

把AI编程的发展和普惠，往前推了巨大的一步。

要知道，Claude 3.7效果虽好，但是先不说封杀国内，即使你能用上，价格也是真的不便宜。

而DeepSeek新版v3，不仅价格没变，他们甚至还有深夜优惠时间段。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENWibXaY8e330QKJ1GUzge0Ou75n1dvkMHtj4kJiafTtSibICfrlhESZjQA/640?wx_fmt=png&from=appmsg)

良心过头了。

我们对比一下Claude3.7和DeepSeek v3的价格（deepseek-chat就是DeepSeek v3）。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo1gtyAAsdySwFhPBiavw2ENrjkLPOY9045kq8gTiaBN7wR25tichRAEjcjIcNZnZJSNiby6S75icFeiaqQ/640?wx_fmt=png&from=appmsg)

输入是DeepSeek v3的**10倍以上**。输出则是13.5倍（标准时段）和**27倍（优惠时段）。**

**这还只是官方API，可别忘了，这个模型，是开源的。**

**作为企业，你有算力完全可以自己部署，更别提还有很多部署完，免费给大家用的三方平台。**

对于绝大多数的普通人来说，我们为什么要忍着被封号的痛苦、付着高昂的价格，去用Claude 3.7？

当所有的三方模型，再一次批量接入DeepSeek新v3的时候，AI编程的普惠，一定会前进一大步。

人人皆可实现自己的梦。

我真的非常的兴奋，也非常的开心。

这一刻，仿佛整个AI世界的夜空同时亮起了万千烟花。

它凶猛、热闹，却也公平且慷慨。

冯骥那一天，说的没错，DeepSeek就是国运。

我们必定。

国运昌隆。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、dongyi

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言