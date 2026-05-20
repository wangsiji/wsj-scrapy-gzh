     【有手就行】2分钟0代码，教你用Dify搭建专属AI知识库 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

【有手就行】2分钟0代码，教你用Dify搭建专属AI知识库
=============================

原创 数字生命卡兹克 数字生命卡兹克 2023-06-12 23:00 天津

> 原文地址: [https://mp.weixin.qq.com/s/DDmT8g6S2tnUUNkptl1n\_Q](https://mp.weixin.qq.com/s/DDmT8g6S2tnUUNkptl1n_Q)

自从ChatGPT发布以来，已经过去了8个月了。

而基于知识库的问答产品，ChatPDF的发布，也过去很多个月了。  

随着越来越多人的接触到AI，基于ChatGPT和私有数据，搭建专属知识库的诉求越来越强。

毕竟，这玩意，可不是玩玩而已，是真的生产力啊。  

**比如智能AI客服，7\*24小时在线沟通，百问百答，没任何脾气，可同时服务数千客户咨询；**

**比如企业内部知识库，大家都做了那么多文档那么多SOP对吧，看那么多文件，脑袋都大了，这下好了，一句话全部解决。**

**比如你的搭建你的数字分身，学习、咨询一站式服务；**

当然，还能搞垂直行业的AI咨询师，比如律师、比如金融等等。

三头六臂，直接起飞。  

话不多说，今天带大家搭自己的知识库，用的项目是Dify。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqJCHBnSoTaVtDKJwZcbwkEYWp5iaG409O0EGXb88L0hgKYHAkSfKTvMg/640?wx_fmt=png)

首先要理解一下搭知识库的基本原理。  

**知识库并不是将几百页的文档全灌给了GPT，而是将文档全部转成向量，存到向量数据库中，当用户发起提问时，就将这个问题的向量去向量数据库里查，找到最相近的文本，给它取出来，并嵌入给GPT，让GPT根据这段取出来的文字进行回答。**  

这涉及到了很多知识，比如你要用API接入，你要做文本分割，你要做向量库，你要做嵌入等等...  

你不会代码的话，直接就可以回家玩泥巴了。。。

而现在，Dify横空出世，无需代码，无需那些乱七八糟的知识，真正的实现，有手就行。  

> Dify 是一个易用的 LLMOps 平台，旨在让更多人可以创建可持续运营的原生 AI 应用。Dify 提供多种类型应用的可视化编排，应用可开箱即用，也能以“后端即服务”的 API 提供服务。

网址在此：https://cloud.dify.ai/

一进来是一个非常简单的登录页面，用Google登录就好。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqtGqBibl5O1zZBtAibgvKntvicic1GibTCElJUSPHribhCMXfkQNIIncLvvhg/640?wx_fmt=png)

然后你会发现，你现在没有任何应用，是空空如也的状态。我们点击左上角，创建应用。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqYxp5HMb7Q4EicQsAGEPYtUsewsffQMhxm4JlmWCxqI0AaibPsU6ias3Ew/640?wx_fmt=png)

在弹出的框中，选择对话型应用，毕竟我们是要做一个对话知识库嘛。然后名字按照真实场景随便填。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqibWD40TjuyibEyq6FXMuK4zkpictKKWvWhlg66FeDSjorltIyTBiahGGibw/640?wx_fmt=png)

进入到一个数据统计页面后，说明我们的应用已经创建完成了，是不是很迅速？但是不急，我们还需要做两步操作，输入我们的OpenAI的Key，再上传我们的数据集。

我们先点头像右上角，点击设置。在弹窗里找到模型供应商，把OpenAI这块的Key，改成自己的账号的Key。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqv7PbpYfXCgsQjVLq6l6pDbJFk1dWnEgPkHyoC1IBVh2DzQSsJKY0Xw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqWz8jxHxiceRCjEDjiafPxKLmxNt4ryVI6WyS8xUsnPV6OR1gmSEdZADA/640?wx_fmt=png)

然后，我们点击数据集这个tab。再创建一个自己的数据集。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqtcxmPToQEzydd1f7Cs9TdUfX8tQQNLib0pK2uA1ic9wktZTXn6KmLC0A/640?wx_fmt=png)

目前Dify的数据集只支持文本上传，已支持TXT，HTML，Markdown，PDF，XLSX。对本地的文档支持的很全面了。**你要是有多个文件，就一个一个传。**

我随便弄了一个文档传上去了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqmTxiaIXjdFibv9asftxh4zWZgwZKGGiap7jo8tNtJWwFbUv6hwfMpqoOQ/640?wx_fmt=png)

然后这个分段与清洗的设置页面，如果你不太懂文本切割，你就无脑选自动和高质量就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqrKeENFAeTwxCYPCJ83gbU1Dbia68JwibS2PeGegkw9wSdBXAMr16NU3A/640?wx_fmt=png)

然后我们保存并处理，很快就好啦。  

处理完成之后，我们回到刚才所创建的应用页面。点击提示词编排。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqXH3aeqIlLgusZmbXHAW5Hew6HKLpBg2vzS6dv6gkpsVAiaQyibibRGt0g/640?wx_fmt=png)

**对话前的预设Prompt我就随便写了两句，大家可以根据自己的实际情况去写，比如智能客服跟法律顾问的Prompt肯定是不一样的。**  

在上下文关联那，把自己的数据集给添加进去。

我们点击发布！大功告成！

回到概览页，我们就可以把这个链接分享给朋友，或者懂代码的话，也可以直接接这个API。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqPibq0llEpHJX00llOL07vtHIe44ADcNYTP775QhbCbIibTF65WRUbQCw/640?wx_fmt=png)

我们打开网页，来问一下我上传的文档内容来试试看。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqR9JTQ8xS5QrLIcClp5Y8OfWS8uXic1WH8L63lcE0mXctXIWyvzZxkDg/640?wx_fmt=png)

当然，Dify的功能还不止于此。知识库只是冰山一角。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpZibcpLP6ib0oicx45nPB7OEqy4InCYAvbBEYdtGicThopicXkapHAwuyibeBDtrjFDiaMdcsiabYH9sVGGQ/640?wx_fmt=png)

大家对他们还感兴趣的话，以后可以慢慢写。

**以上，既然看到这里了，如果觉得不错，随手点个赞和“在看”吧，感恩。**

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言