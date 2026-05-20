     揭秘AI背后的神秘代码 - Token究竟是什么？ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

揭秘AI背后的神秘代码 - Token究竟是什么？
=========================

原创 数字生命卡兹克 数字生命卡兹克 2023-06-16 11:58 天津

> 原文地址: [https://mp.weixin.qq.com/s/Fzgg265eBepLpYIS-ZWImA](https://mp.weixin.qq.com/s/Fzgg265eBepLpYIS-ZWImA)

前两天，OpenAI来了个大活，更新了函数和GPT3.5的16K版本。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURowVceohpIGOrkx7dAYOsia9cKyNcVZpIzRDhuhhNUVlEBsdf0zF7YlJZIBGcAnBd6OuZNqhDl2l8g/640?wx_fmt=png)

函数不具体说了了，对Langchain和想做API调度中台的是一锤子暴击。

重点说说GPT3.5的16K Token版本。

正好作为一个伪科普作者，也想借这个机会，给大家用大白话简单科普一下到底什么是Token，为什么想提高Token的上限这么难。  

先说一下16k的价值。

**众所周知，旧有的3.5是4096Token，我们在做开发时，无数的地方受制于这个4096Token。**

比如说，用户对着我们韭圈儿AI发了一句话：

> “帮我挑选5只去年收益排名在前20%，且最新季度持仓不含白酒的消费类基金，并全部加到我的自选，然后做一个等权组合，生成一个组合诊断分析报告。”

我们一共有100个左右的API，比如查询收益、查询持仓行业占比、筛选基金、构建组合、组合诊断、加自选是分别不同的API，我们会让GPT自主挑选使用什么API来处理这个用户的问题。

而受制于4096，我们一次对话大概只能灌30个左右的API给GPT，另外70个API会丢失，这肯定不能这么任性瞎搞。

所以我们会同时开4个对话进行并发，最后把挑选的API合并在一起，但是大模型吗，你懂的，可靠性并不总是那么强，特别是4个对话并发最后合并，那特么就更麻烦了。。。所以我们又需要额外的做数据提取再合并等等。。。

**而现在，有16K，还并发还合并还提取个屁。  
**

**一个对话窗口全部解决。省了无数的心。**

同时，推理能力也比3.5强几个量级，直观感受可能叫GPT3.75更为合适。价格也仅仅只比GPT3.5贵一倍，相当香了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURowVceohpIGOrkx7dAYOsia9ibSXpBiaKV9P0oAUDXKpXlsQNI4ExYMaax5tKo81QXjZe7LXzuR9ZOXw/640?wx_fmt=png)

回到4k和16K上，为什么16K比4K难做的多，导致以OpenAI的技术，也现在才放出来16K的3.5版本？而Token到底又是个啥呢？  

我先浅显易懂的解释一下到底什么是Token。  

在自然语言处理和计算机科学中，“Token”是一个非常基本的概念。

简单来说，一个Token可以看作是数据的一个单元。

**在自然语言处理中，Token最常见的定义是一个语言的基本组成单元，如单词、字、甚至是标点符号。**

当我们要让机器理解和生成自然语言时，首先需要进行的就是“分词”（Tokenization），即将连续的文本划分成一个个Token。

我们可以用一个有趣的测试来证明字和Token的区别。

比如，我要将“_卡兹克今晚要去按摩然后吃炸鸡_”这句话倒写。  

正常来讲人类语言应该是：

_“鸡炸吃后然摩按去要晚今克兹卡”_

但是对于计算机，用Token来处理就是：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURowVceohpIGOrkx7dAYOsia9K4hfSibSA8r25zWmyoSmKWllS2L8bFAicibnzTmBic4mkqNHrfc1YVZIxg/640?wx_fmt=png)

完全就可以发现，一个字可能是token，一个词组也可能是token。

Token，就是机器所理解的数据单元。

明白了Token，我们再来回答另一个问题，为什么16K的Token版本比4K难做的多。

我用一个有趣的例子来解释。  

派对。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURowVceohpIGOrkx7dAYOsia9j3MxNMwiaIonSo36ic1JvVK8me9dYsoy93GTGcsZBPo3icsicSXEPeMibjQ/640?wx_fmt=jpeg)

假设你正在举办一个盛大的派对，你邀请了4000位宾客（这就是我们的4K，同时为了方便计算，后面4k=4000,16k=16000）。

你要尽量确保每个人都有人陪伴，所以你要安排每个宾客和其他所有的宾客都至少打个招呼。你能感觉到这是个挺大的工程，对吧？

现在，试想一下，如果你的派对规模翻了4倍，你邀请了16000位宾客（也就是我们的16K）。你仍然希望每个人都被照顾，所以你又要让每个宾客和其他所有的宾客打招呼。

你能想象到这是多恐怖的工程吗？

这就是处理16K的Token比处理4K的Token难得多的原因。

**在大模型的核心算法Transformer中，这种“打招呼”叫做注意力计算（attention calculation）。**

在注意力机制中，每个Token都需要与其他所有Token进行一次计算。这就意味着，当Token的数量增加，需要进行的计算就会呈平方级增长。

对于4K的Token，我们需要进行大约**16百万次（4000乘以4000）**的注意力计算。

而对于16K的Token，我们需要进行大约**256亿次（16000乘以16000）**的注意力计算。

这就是为什么16k比4k难做的多的原因，同理，32K，那就更恐怖了。  

希望我的这篇文章，能让大家明白一些大模型背后简单的原理。

最后。  

让我们向每一个参与这场科技盛宴的开发者，研究者，创新者致敬。

他们改变了寻常事物。他们推动着人类前进。

我相信，他们，才能够真正的改变世界。

**以上，既然看到这里了，如果觉得不错，随手点个赞和“在看”吧，感恩。**

  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言