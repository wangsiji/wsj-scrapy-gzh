     我们花了3个月时间，给基金AI整了一个大活 - ChatFund \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

我们花了3个月时间，给基金AI整了一个大活 - ChatFund
================================

原创 数字生命卡兹克 数字生命卡兹克 2023-07-03 18:39 天津

> 原文地址: [https://mp.weixin.qq.com/s/UOw7hG5TdgBnF5JXqiRgMg](https://mp.weixin.qq.com/s/UOw7hG5TdgBnF5JXqiRgMg)

在2月ChatGPT和NewBing大爆发的时候，我们尝试去让AI评价基金评价基金经理筛选基金。

但是得到的结果却非常不尽人意，数据全是错的。

错的就算了，关键还说的一板一眼，很难去验证这个数据到底是真是假，很麻烦。

这就导致生成式大语言模型在基金领域的应用上，基本一无是处。

在被他们反复折磨后，3月底我们决定：

我们韭圈儿，自己做一个AI应用，让所有基金从业者、基民们通过AI，使用自然语言，就能超级快速、准确的分析基金，筛选基金。

**“做投顾的投顾，做基民的基助”**  

我们花了整整3个月时间，从一开始的扒OpenAI官方文档、到微调、研究嵌入、匹配数据、写Prompt、分析场景、实验AgentGPT、写Plugin...鬼知道趟了多少的坑。。。

但是今天，我们也能自豪的宣布。

**韭圈儿AI - ChatFund。**

**正式开启内测了！**  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0XaeIQuAozokEbVueTW5NYicd7NKlqE9QzoODAuBmQBBFXF8h0JcGmww/640?wx_fmt=png)

网址在此：https://chat.funddb.cn/

目前开放申请，因为后端服务器和Token压力，我们会逐步开始发放名额～

ChatFund1.0首批上线8大功能，分别是基金分析、经理分析、持仓诊断、季报巡检、灵感选基、每日收评、每日早报、知识问答。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV04RMjN3mo8YqGkGDLdWNbg9yd2Dhc7XkvDg1dUlhfE2ybXQqagrCP2A/640?wx_fmt=png)

从各个场景来为基金从业人员、普通基民赋能，颠覆交互体验，提升效率。

重点给大家介绍下基金分析、经理分析、持仓诊断、每日收评、灵感选基这5个功能。  

  

**01\. 基金分析**  

ChatFund可以一键快速的生成一篇基金分析报告，并且我们在ChatFund上，也集成了韭圈儿APP，当你问某只基金的时候，**韭圈儿APP就会跳转到APP页面，可以让你图文并茂结合着看，也能让你快速验证数据的准确性**（PS：对数据准确性这块我们有绝对的自信）  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0GyEc4FDVKQFr19xn9Z3ibf4MMwBnwd7voeb5t3sGNkUtahAZ4qZiamUg/640?wx_fmt=png)

你也可以直接查询某只基金的所有信息，比如问万家品质生活的近一年收益率、最新持仓、最新季报观点、规模变化等等。ChatFund都有准确无误的数据来给你回答。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0rg07icwb65PJLDAD6rzl5hCpxFye20xmk2vyo25ThCOF0ibWewKOzH2g/640?wx_fmt=png)

当然，你也可以问一下骚问题...比如用小红书风格，给我列易方达蓝筹的5个缺点...kunkun对不起🧎。。。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0nCLMIg5B7kt4DZWErmBJOYicz5yWgH8icMtdhN0t6Ona2bSKaqFMX5ibw/640?wx_fmt=png)

  

**02\. 经理分析**

跟基金分析类似，同样的，输入经理，就可以全面的多角度的为你生成基金经理的分析报告，韭圈儿APP会自动跳转到经理详情页，方便你查看更多详情，以及验证数据。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0rxInJic65iacibEE7rhldzVmjFWjjst6ElXURa1ic6w0ehg8aPwia4MmdYQ/640?wx_fmt=png)

同样的，基金经理的任何信息都可以让ChatFund给你回答，比如查询杨鑫鑫的获得奖项、问在管规模等等。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0q1PL3vKt89XbNtqn8NbRSfm32Bc4TjtLWFqc2QvRakGVWVicReu1lsQ/640?wx_fmt=png)

当然，你也可以问一点进阶的问题，比如聊聊莫海波的持仓行业变化，看看他的持仓变动是咋样的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0IOrYicguibdnnX1dA7zTQiaOv9L95ZjceraE3bhj8cQRru50iaTswXZR8Q/640?wx_fmt=png)

  

**03\. 持仓诊断**

如果我们让AI给你做持仓诊断，并给你生成诊断报告呢？

我们韭圈儿APP有一个功能叫做账本，我们直接集成了过来。你现在，可以对你的账本做一个诊断，看看你的资产配置怎么样了。

在ChatFund的对话中，选择你的账本，然后确定一下你的投资目标。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0gLdL9YNHAPsQCyvYJU67JNejmVtkSNptD5xCJjVEBPpL6GulFblFGw/640?wx_fmt=png)

他就会嘟嘟嘟的为你生成一篇诊断报告，右边同理，会有我们的韭圈儿的账本诊断界面，给你全新的阅读体验。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0PhRGux4AZiaBCO6ghbK77EqO5e8fzGEAlotibxNQlhiaNHpsUuIxADficQ/640?wx_fmt=png)

  

**04\. 每日收评**

相信大家并不是每天都能去盯盘，或者看一遍市场。特别是基金从业者们，有时候还需要花1、2个小时的时间去写一篇收盘点评。

现在，ChatFund可以1分钟用最新的市场数据，为你生成一篇收盘点评。**想用什么风格都可以，比如典型的小红书风格。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0jz9Sr1bW7liabM62On5dGAApc8JV22CbjhJPyibXI47ZPCZBJUnKpngw/640?wx_fmt=png)

  

**05\. 灵感选基**

最后，得隆重介绍一下我们的王牌功能，灵感选基。

在这个时代，基金筛选越来越复杂、越来越头疼的情况下**，AI的出现，给整个选基金的体验带来了降维打击。**

“给我找今年收益率大于10%，且持仓中不含白酒的消费基金”  

“我给列5个能涨抗跌的基金”  

“给我找2021年夏普率最高的5只权益型基金，告诉我今年收益率最高的那个”  

这些问题终于成为了可能。  

比如你也可以问：“帮我找经理投资年限大于10年，得过金牛奖的权益型基金，列5个”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV00t7icTZCR7Y7QbkwgPTicCrBia2MAgEdR9QnpaHB6BTayb1XmVrvyEXjg/640?wx_fmt=png)

筛选的基金直接跟我们韭圈儿的基金筛选器打通，条件直接录入，列出了所有符合条件的基金，你可以快速查看，修改等等。

当然，除了筛选器，你也可以通过股票选基金，比如最近火电涨的不错，我想挑出来买了华能国际、大唐发电、上海电力的基金。章恒的万家颐和勇夺第一。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0lPqU5ZwODKfibvCnibHMuGCgiaQAkLGQv7m60on9vPPj9vicQxyT5ZhXmw/640?wx_fmt=png)

**当然，我们还有One more thing。**

**筛选出的基金，你直接补一句：帮我做一个组合回测。**

**这个组合就做好了，比如我的条件，万家直接包场。。。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV06BYtqWYwU1gFda4crdfiax7o9Dcfj0lHeQOqjchx8dDufpLkcwJrH3A/640?wx_fmt=png)

未来，还能跟加自选、社区发帖等等全面打通。尽情期待吧！

  

**写在最后**

韭圈儿AI - ChatFund终于要见人了，我们也做了一个邀请海报，你可以通过链接：https://chat.funddb.cn/加入体验，也可以通过海报扫码申请。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrvwFUL9kE3sRSLCGM3iaBV0YtQxJk7nohRlibYXLrIOQghnzwxiaqTWEhkcxHjjjciboZFyyjsFpwsDQ/640?wx_fmt=png)

3个月的时光。

致坚守。  

致热爱。

致各位真诚的陪伴。

致我们心中永不磨灭的创新。

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言