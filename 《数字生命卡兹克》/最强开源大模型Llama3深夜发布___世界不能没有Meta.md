     最强开源大模型Llama3深夜发布 - 世界不能没有Meta \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

最强开源大模型Llama3深夜发布 - 世界不能没有Meta
==============================

原创 数字生命卡兹克 数字生命卡兹克 2024-04-19 02:47 天津

> 原文地址: [https://mp.weixin.qq.com/s/J25GjbSp\_otsBCAvCsMBDg](https://mp.weixin.qq.com/s/J25GjbSp_otsBCAvCsMBDg)

其实昨天在微软的偷跑之后，就已经有消息说，Llama3要出了。  

这个消息的振奋程度，对于AI圈来说，甚至不亚于所谓的GPT4.5。  

毕竟，meta才是真正的那个"OpenAI"。

有多少大模型的生态，是建立在Llama上的，大家都懂。

而这个开源之光，被全世界无数人盯着的大模型，Llama3，在时隔近9个月之后的今晚。

终于正式发布了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986QgPKJv201uXAeRqzZwWOB8ZR2JdXGnTeHQjmrVts4aJXlfKauG7Omg/640?wx_fmt=png&from=appmsg)

我的几个朋友，都已经疯了，比如zR同学：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986nUIHlI3VFVWEaicmAVsRgBD1VbUwIOlfFutWDaUBS9uRlaV1b6847ow/640?wx_fmt=png&from=appmsg)

今夜无眠。

Llama3目前在自己的官网和huggingface上，模型已经上架：

https://llama.meta.com/llama3/

而且还是meta的老规矩，虽然写的是特定条件下商业使用（月活不得超越7亿），但是基本等于完全免费商用了。

这次开源了2个模型，8B和70B。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986mJ5JQicMnmycwNUChQoHcS5Bk9tehcerjrjsn5K3Zmoe1oJRNg3Jxbw/640?wx_fmt=png&from=appmsg)

然后就是大模型的传统艺能：跑分。

坦率的讲，他们这个跑分，有一点的离谱。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P9869ibDXJ5828fNyBnJhpX8OrrUibh2eRHBkx5ydIiaf5gJiaibE1RYbK532EQ/640?wx_fmt=png&from=appmsg)

5个评测集分别是MMLU（学科知识理解）、GPQA（一般问题）、HumanEval（代码能力）、GSM-8K（数学能力）、MATH（比较难得数学）

不管是8B还是70B，基本等于全线秒杀。  

8B这边，直接把同尺寸的摁在地上打。

曾经的Mistral 7B也是有过辉煌的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986PQRLMwSRftIYyZCjc8ujbBtdC4icHmsf9jQoS18GpBrhglRMib6L5x9A/640?wx_fmt=png&from=appmsg)

现在也被干成了时代的眼泪。

甚至，Llama3自己的8B模型，效果都比Llama2的70B要好，这事就非常的特么离谱。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986aiagBXXiaakAJqowFTG7UarloQic5KubpGB4QLQ93lUFrdx5e98zl7jhg/640?wx_fmt=png&from=appmsg)

而Llama3 70B那边，直接对标Gemini Pro 1.5（Gemini：我到底做错了啥）和Claude3 Sonnet。GPT-4逃过一截哈哈哈哈。

这个分数真的很恐怖了，毕竟参数量跟两玩意都不是一个量级的，Llama3只有70B，还能打的有来有回，虽然跟Claude3最牛逼的那个Opus还有一些差距，但是这特么是开源的啊！

他们还做了一个有趣的测试，搞了一个全新的高质量评估集。

里面包含 1800 个提示，涵盖 12 个关键用例，分别是：

寻求建议、头脑风暴、分类、封闭式问答、编码、创意写作、提取、塑造角色/角色、开放式问答、推理、重写和总结。

最骚的是，为了防止过拟合，甚至Llama3自己的建模的团队事先都不知道这玩意。然后针对 Claude Sonnet、Mistral Medium 和 GPT-3.5，对这些类别和提示进行人工评估。

结果就是：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986OtnOokAzTUEJcFiaYkEVTWz0WsSeaGIjUr4icuE10vTx3H8T8D9oUsqw/640?wx_fmt=png&from=appmsg)

很强。

不过也有两个很der的点。  

一个是知识库时间，一个是上下文长度。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986CstA9nggO0Tkic7mOIJVUyV5o0icc4gzLfQXiav1NM0yNE75CRP3RMFaA/640?wx_fmt=png&from=appmsg)

知识库这块，7B只到2023年3月，70B到了2023年12月。

上下文长度更是只有可怜的8K。

知识库的时间还好说，但是你这个上下文长度，在现在动不动200k的时代里，属实是有点不够看了。。  

Llama3的训练数据，用了超过15T词库的预训练，是Llama 2的七倍。包含的代码数量是Llama 2的四倍。预训练数据集含5%以上的非英语数据，覆盖30多种语言。

而且，他们还有个400B的离谱玩意还在训练中。但是我觉得400B的这玩意大概率不会开源。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986VK9mFpCcUqk01VdyA0aCiamP9ZuoPO9wgIsQm1OXIcgULYN2JuibK1yA/640?wx_fmt=png&from=appmsg)

再对比一下目前的主流的最强模型：  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURrpDjbmeEribRdp8QuM5P986QCicmicyskd9m0ABHbHyweW55X1NL1ialkK7X7GgictDZdxS1g06rorUcw/640?wx_fmt=jpeg&from=appmsg)

就...离谱  

直接跟Claude3 Opus和GPT4 Turbo差不多，爆杀了Gemini Pro 1.5。  

嗯。。。。无话可说。。。

现在可以直接在的官网用：https://www.meta.ai/

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986b70N0cfcDo3MlicZA4Mpv1WYhOiciczibXlpAv9hQCsQgrOeXzkQgApiceQ/640?wx_fmt=png&from=appmsg)

如果你没Meta账号的话，也可以在这用：https://llama3.replicate.dev/

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986EXTxteTgQO1I6UMYP3XKbKGPHzRI2xmjolTXQyyXh9Ru7B294NlhHA/640?wx_fmt=png&from=appmsg)

当然，我相信更多的人，还是会下载下来，本地部署+微调。

Llama3的中文还是不咋地，几乎就没啥数据，所以还是得靠大佬微调以后才能用，前提是必须遵守Llama 3社区许可证和可接受使用政策。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986tQ0EtW7QMY84rIFSKblib7ZKGWUvjFdkYibsr5m7Giakc7q5RrX1QDbrA/640?wx_fmt=png&from=appmsg)

而我们再跑了2小时后，我们发现很突出的一点是，代码能力太炸了。

zR跑了很多的case（都是英文）。  

比如一个经典的皇后问题。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986AVtTYYCvTJe7ZjAmicK5LNCFluqbuRAM0INuSGWFcobAvWqIdE6IQxQ/640?wx_fmt=png&from=appmsg)

Llama3-8B直接给出了解法：  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P9866lvtiadYZiaZpnL643rBRc2J6ibmmaylb81ZSLPAibF8XAFZKFZrQwucaA/640?wx_fmt=png&from=appmsg)

然后，运行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986nEdvCcc7NgbpLa6qicOiaD9ViaevEFyFWwSDicHiaNU8C4YH8AwjRO1re3Q/640?wx_fmt=png&from=appmsg)

这特么在Llama2中，基本是不可能的，只有专门的代码模型，才能搞定。

要知道，Llama3-8B，只是一个8B的通用大模型啊。。。

然后，我们又上了一个贼难的一题。按zR的话说，这就是leetcode上，最难的一题。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986ibPlB03pqdrSWPMREweibOibZegQANwfxhRKncq9Uhbf5J1UpfZkWmXhA/640?wx_fmt=png&from=appmsg)

题目是：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986eRKicAhXCYf4yHgFKI4xhbl4CSuUZxgm361MCDWrXPRMJ9cxqgicTFPQ/640?wx_fmt=png&from=appmsg)

然后跑了一次，报错了，给了报错和答案错误，对话三次后：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986ibZEuL5d3elZDicuSgaJdJ0fcibsbicpO5swUtRwt7ajE2HRkUUf8jZq8A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986ZlUoib66RqY7WpibJB74QYrLws9HHM6Iiaq7l6Ptrmyjp22PvTosxdSEA/640?wx_fmt=png&from=appmsg)

。。。  

他自闭了。

GPT4同样出错，享受跟Llama3-8B的同等待遇，还是没干出来。

但是Llama3-8B，干出来了。。。

太抽象了。。。

总结来说，Llama3这次，绝对是王炸级别的模型。

也可以当之无愧的说，就是最强的开源模型。  

Meta再次证明了，自己才是那个"OpenAI"，而那个OpenAI，只是个"CloseAI"。  

世界不能没有Meta。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrpDjbmeEribRdp8QuM5P986yLq9s3Y76cYkoWhhrK4sl0TxgsZJibFuHvvWQ7c0U8HBE6H1UloYt0w/640?wx_fmt=png&from=appmsg)

还有个小插曲是，今天还是吴恩达的生日。

所以话说回来，OpenAI你的GPT5还在等啥呢？  

快狙击啊。别怂。

赶紧的。

我们等你。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。******

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言