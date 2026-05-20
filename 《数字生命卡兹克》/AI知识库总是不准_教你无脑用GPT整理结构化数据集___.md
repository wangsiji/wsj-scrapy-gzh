     AI知识库总是不准？教你无脑用GPT整理结构化数据集... \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI知识库总是不准？教你无脑用GPT整理结构化数据集...
=============================

原创 数字生命卡兹克 数字生命卡兹克 2023-07-21 21:34 天津

> 原文地址: [https://mp.weixin.qq.com/s/1hcufhPJ7P1cXEsAZ7MdRA](https://mp.weixin.qq.com/s/1hcufhPJ7P1cXEsAZ7MdRA)

随着LLM的蓬勃发展，企业、个人知识库越来越火。

但是随之而来的，也是两个问题：

**一、搭建成本高。二：回答的内容结果不准。**

第一个问题，其实之前写过一篇文章，教大家如何使用Dify极其简单的搭建自己私人知识库。

[【有手就行】2分钟0代码，教你用Dify搭建专属AI知识库](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647658737&idx=1&sn=66d54195f97b6241cc8a9a755eabe97a&chksm=f007cca6c77045b0184f2fc63f78be4e839c5ac46dae6fe8816ce698f447d444f9e1fbb55b9b&scene=21#wechat_redirect)  

但是随着而来的，就是很多人跟我反馈的：答的乱七八糟。

其实知识库的原理很简单。比如典型的Langchain-ChatGLM的架构图，加载文件 -> 读取文本 -> 文本分割 -> 文本向量化 -> 问句向量化 -> 在文本向量中匹配出与问句向量最相似的top k个 -> 匹配出的文本作为上下文和问题一起添加到prompt中 -> 提交给LLM生成回答。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqMOMZynZic1qCXlFtI4Er6DmeUnGyzwbsRwtCNswFEWGmTzFUztxibH8thfQ13cF9fPV3ugNXy0fWg/640?wx_fmt=png)  

用大白话说，就是根据你的问题，去根据的你问题，去被切成N多块的文本块里，挨个搜索，找到一个或几个最相关的拿过来给大模型，让大模型根据这些搜出来的文本块作答。

而答得不准的原因，当然就是搜的不准。  

搜的不准的原因，就是数据集太脏了。

我见过太多直接就把小说、把几十篇乱七八糟的文章往里面灌的，也太高看现在LLM的能力了，那里面的数据都乱成一团，一堆乱七八糟的口语化的甚至是无效信息，能准吗？

所以就要做数据清洗，或者说，**做一个结构化的数据集。**  

结构化的数据现在一般是两种，一种是树形结构，一种是问答对结构。  

树形结构不多说了，适合超大型书或者一些超强的层级知识，这块推荐去看腾讯的teng大佬的文章：如何用 ChatGPT 搭建代码知识库，提升开发效率，写的很详细了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqMOMZynZic1qCXlFtI4Er6DvLPqTs0ZAGGLobgaI8ysOTXT5B43HPMDK4Ekp2CVKApGBlGB7dD03Q/640?wx_fmt=png)

而另一种，就是我们常见的问答对格式，这里放一个GLM2的官方示例数据集你们就明白了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqMOMZynZic1qCXlFtI4Er6DXeFOSyn30jFibrpkfmJRyeU2E91wJWpwhDL7Un38TNuawFoD9FdcaVg/640?wx_fmt=png)

我再写个示例  

{"content": "介绍一下卡兹克", "summary": "卡兹克其实是一个大智障，喜欢打游戏，任天堂死忠粉"}

这个就叫问答对，把碎片化的大段的文章，转成一个一个的问答对数据集。  

我到时候问卡兹克是谁，喜欢啥，大模型就不会瞎JB匹配，而是直接把这个问答对匹配出来，根据后面的答案进行回答，这样准确性就会高非常多。  

但是又有很多人犯难了，这特么一个一个整理，那特么不得累死我？  

那种微调质量的超高数据集，确实得一个一个手工处理。  

但是你这就做个私人知识库，没必要，这里我教大家一个賊无脑的方法。

直接拿GPT跑。

第一步，先让GPT对你的文档生成适合问答对的问题，第二步，让GPT根据生成出的问题和原内容，再按格式规范拼合成问答对。  

**我甚至都把Prompt写好了，直接拿去改吧改吧用就行。**  

这里直接用OpenAI的后台Playground跑了，因为有16K，而且可以锁system，方便。

https://platform.openai.com/playground

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqMOMZynZic1qCXlFtI4Er6Dx25n2pEwuw12uwVqdMM3oKD11kCYWicZlrN9qqlibYctqtT8Dsl9sK4g/640?wx_fmt=png)

右边选16K模型，温度拉到0.8，最大输出直接拉满。  

**第一步，先生成问题。**

system里面写我给的prompt。

_#01 你是一个问答对数据集处理专家。_

_#02 你的任务是根据我给出的内容，生成适合作为问答对数据集的问题。_

_#03 问题要尽量短，不要太长。_

_#04 一句话中只能有一个问题。_

_#05 生成的问题必须宏观__、价值，不要生成特别细节的问题。_

_#06 生成问题示例：_

_"""_

_权益型基金的特点有哪些方面？_

_介绍一下卡兹克。_

_"""_

_#07 以下是我给出的内容：_

_"""_

_{{此处替换成你的内容}}_

_"""_

在下面替换你的内容，Uesr那就是用户说的话，我就随便写了个生成8条问题。你想要10条、20条、40条都行。

然后我随便找了我以前写的文章，扔了进去，8个问题就出来了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqMOMZynZic1qCXlFtI4Er6D0ASg22rFlONzAksI677a1Sgc55u0aWSsqLXzz5qTNZ15SN4rDvgX4g/640?wx_fmt=png)

接下来这个窗口别动，也别关，我们新起一个一模一样的窗口。  

**第二步，根据问题和内容，生成问答对。**

右边同样的参数，再把这个Prompt扔到System里。

_#01 你是一个问答对数据集处理专家。_

_#02 你的任务是根据我的问题和我给出的内容，生成对应的问答对。_

_#03 答案要全面，多使用我的信息，内容要更丰富。_

_#04 你必须根据我的问答对示例格式来生成：_

_"""_

_{"content": "基金分类有哪些", "summary": "根据不同标准，可以将证券投资基金划分为不同的种类：（1）根据基金单位是否可增加或赎回，可分为开放式基金和封闭式基金。开放式基金不上市交易（这要看情况），通过银行、券商、基金公司申购和赎回，基金规模不固定；封闭式基金有固定的存续期，一般在证券交易场所上市交易，投资者通过二级市场买卖基金单位。（2）根据组织形态的不同，可分为公司型基金和契约型基金。基金通过发行基金股份成立投资基金公司的形式设立，通常称为公司型基金；由基金管理人、基金托管人和投资人三方通过基金契约设立，通常称为契约型基金。我国的证券投资基金均为契约型基金。（3）根据投资风险与收益的不同，可分为成长型、收入型和平衡型基金。（4）根据投资对象的不同，可分为股票基金、债券基金、货币基金和混合型基金四大类。"}_

_{"content": "基金是什么", "summary": "基金，英文是fund，广义是指为了某种目的而设立的具有一定数量的资金。主要包括公积金、信托投资基金、保险基金、退休基金，各种基金会的基金。从会计角度透析，基金是一个狭义的概念，意指具有特定目的和用途的资金。我们提到的基金主要是指证券投资基金。"}_

_#05 我的问题如下：_

_"""_

_{{此处替换成你上一步生成的问题}}_

_"""_

_#06 我的内容如下：_

_"""_

_{{此处替换成你的内容}}_

_"""_

把上一步的生成的问题，粘贴到#05那块，再把原本的文章，粘贴到#06那块。

然后Uesr随便写一句“拼成问答对”，直接开跑。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqMOMZynZic1qCXlFtI4Er6D8j6QWwFrE0Y00WfZYc4wiaF5YjWfAviaEYYBFzn4annicsNLFPT8fra2w/640?wx_fmt=png)

一分钟，你的问答对就生成完了，直接扔到txt里，灌给Dify或者Langchain-ChatGLM啥的，都行~  

你的知识库如果大的话，一次性肯定没法全扔进去，所以我们才需要开两个窗口，不断复制粘贴。  

**你也不用自己去费劲巴拉的自己写数据集了，你就是一个无情的复制粘贴机器。**

希望用GPT处理数据集的方式，能给大家抛砖引玉。  

让人人都提升效率，去做更有意思的事。  

**以上，既然看到这里了，如果觉得不错，随手点个赞和“在看”吧，并给我个星标⭐吧，感恩。**

  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言