     刚刚，智谱开源了他们的最强多模态模型，GLM-4.5V。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

刚刚，智谱开源了他们的最强多模态模型，GLM-4.5V。
============================

原创 数字生命卡兹克 数字生命卡兹克 2025-08-11 22:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/MLFCI4GXk3iFDrlyFyGIqg](https://mp.weixin.qq.com/s/MLFCI4GXk3iFDrlyFyGIqg)

上上周一的晚上，智谱开源了当今最好的模型之一，GLM-4.5。

然后，这个周一，又是突如其来的，开源了他们现在最好的多模态模型：

GLM-4.5v。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PHP36jzk9jBS9JIjLWlnOclib3ILXJoqen9WgUc4DSQyeaVncsHae5xA/640?wx_fmt=png&from=appmsg)

也是4.5系列的，用GLM-4.1V-Thinking的技术路线把GLM-4.5-Air重新训练了一遍，实现了视觉多模态的能力。

模型参数106B总参数，12B激活，这个规模在开源多模态模型里已经算是大块头了。

模型能力也有点东西，在所有的开源多模态模型中，42个评测基准，41个SOTA了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9P71exHIfa30ZpYXZ2kqTgxnxJkbqw1Yib3G7CBicJDAuEvS2MuaGMDia7A/640?wx_fmt=png&from=appmsg)

我说实话，这个看着，还是有点吓人的，我已经很久没看到这么全的评测基准列表了。。。

说明GLM-4.5v，这波是真的自信。

模型已经在多平台开源了，可以任选一个下载。

Github：https://github.com/zai-org/GLM-V

Hugging Face：https://huggingface.co/collections/zai-org/glm-45v-68999032ddf8ecf7dcdbc102

不过106B的量级，消费级还是难部署，如果想用的话，可以去智谱他们的z.ai上用。

嗯，网址就是z.ai。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9P60GDdVORwfVMdwvL25LLZl27Nbr7VeX3FzNWtZl5z5KtGAdhNJjEjQ/640?wx_fmt=png&from=appmsg)

我也第一时间去做了一下测试。

这里先测的，是用的是专门做评测的朋友拓界AI给的多模态测试题。

比如第一道是游标卡尺的读数，这玩意读起来还是挺费劲的，整数小数要分开读，得非常仔细才行。

反正我是看的一脸懵逼。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PUF5l1ia3mLib4bIjvxR5lb9wQAZjkCPREmSWibkAB3ZGT9sdEUl22tTQA/640?wx_fmt=png&from=appmsg)

而GLM-4.5V，花了一小会，就写出正确答案了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PbIw8I4xeibvhJjcsHxsGiaTbYRZ4UTOD8Fv1yVEFlXMSSIyFhPicQA5qQ/640?wx_fmt=png&from=appmsg)

思考过程并不是非常的冗长复杂，很简洁，所以很快就出来了，这个非常的好评。

然后是第二题，小猫摸球问题，我是已经看花眼了，看这玩意看的我眼睛疼，真的。

问题就是：到底哪个猫摸到了毛线球。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PkdL3lo2TbgZq5iaPOWD3IbT7Mhxjibnh1icEoQ8c3IjHNz2nW5ibibsX0Hg/640?wx_fmt=png&from=appmsg)

GLM-4.5V也找到正确的答案，还给了正经的操作方法。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PzysdM8weHRdnYmRFVa9N5PmjACMx50blVLKpibH22PSnX3bAWSoWgibw/640?wx_fmt=png&from=appmsg)

我眼花着验证了两次，确实是AI没毛病。

在视觉推理能力上，GLM-4.5v确实有点东西，而且速度快的离谱。

我又试了一个经典的，识别地理位置的case。

就是横店明清宫苑的图片，想看看它能不能正确的分辨出来。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PtVtfcVuzAjFqGCWnRADIOj0xicpeOI8LhPibFsN33jribRSZDc7IPlWsQ/640?wx_fmt=jpeg)

这个测试其实挺有难度的，因为横店的明清宫苑是按照故宫1:1复制的，连细节都做得很到位。

如果模型只是简单地识别建筑风格，很容易就会判断错误。

GPT-5-Thinking在深度思考以后，就来了一个非常抽象的答案。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PfR6Pj40okhbD2KZibq1uUJfj6ZHYTVKHeS93TbQ6icrgSR0EzxqgaXeg/640?wx_fmt=png&from=appmsg)

华清宫什么鬼？

而GLM-4.5V答得很正确，指出了这里是横店的明清宫苑。

这个回答挺让我惊艳的，而是因为它能在如此相似的场景中做出准确判断。这说明模型不是简单的模式匹配，而是真的具备了一定的视觉推理能力。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PTmiag2SBLW0ZwX5v4gz7bIk8rhwO4dmteNuJ0p6L0W5wPxU8a5J1muA/640?wx_fmt=png&from=appmsg)

但我有点没看懂它是怎么分析出来的，于是我又问了一下它，为什么是横店不是故宫。

这回它给出了详细的解答，分了三个点，讲的相当有理有据。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9P1P1Hw9Xh1aM6qQV0EyibYoN9okM9e9ZunffiaNwHt1MQ49Xu7sJEX9JA/640?wx_fmt=png&from=appmsg)

牛逼。

那再试试内景，我找了一个宫殿内景的图片，问他这是哪里。

这轮没有正确回答出来，我还追问了一下，它还是肯定的说是故宫。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PBqroicbXsDbiauSksCsZ1FrpwQvXQN1l1LzcQ6PCxQv2Ic8bdU6L4KLQ/640?wx_fmt=png&from=appmsg)

说实话，连我自己看这个内景图都有点拿不准，毕竟横店的复制度确实很高，内景的装饰、色彩、布局都做得很像。

看看GPT-5-Thinking，错了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PNalBQBJvemXJ6PuusM4EcIuTib8Ty6BMrQuicZbtN55gOk7hrtYh672Q/640?wx_fmt=png&from=appmsg)

这个题，连我心中最强的视觉推理模型o3都错了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PmuJso2N14mEGT3Os25PHw88Ck4tveeC8wDn4sH4yDElxFTk3pZcb9w/640?wx_fmt=png&from=appmsg)

横店搓的太像了，真的匠人精神，实在没招。。。

模型在这种情况下出错，也是情有可原。

还有一个我觉得很酷的功能。

目前只有Gemini有的，原生的视频理解。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PeL2Jq5fflwnia0dfrDUcPAf92lpFtAE0k7IC3wfIHAlIy2BzYMIUXYw/640?wx_fmt=png&from=appmsg)

这里我说一下，很多产品说自己有视频理解能力，或者总结视频，其实不是的。

他们更多的是吧视频里的音频提取出来，找到人说话的部分，然后STT音频转文字变成文字稿，最后再找个大模型总结，不是原生的靠模型能力的视频理解。

我发给它一个我下载下来的二十世纪影业官方的25周年《泰坦尼克号》的混剪，让GLM-4.5V看看里面包含了哪些经典画面。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9Pxibzoib4hvuk9iaqHyZGICqkPDzW7IdhnmkWqFRUHzC5F0VqIYsoH7qRQ/640?wx_fmt=png&from=appmsg)

要知道，视频理解一直是多模态模型的难点。

模型需要理解时间序列、画面转换、场景连贯性等等，这对模型能力和算力的要求是几何级增长的。

GLM-4.5V非常有意思，也确实是让我我比较惊喜的，它思考了一会，给了我一个很全面的回答。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PGedbUczy4eJd0CPs8fG5eYxAMTBQndrr5xZO7dxO8h8Z9JnER5pJtw/640?wx_fmt=other&from=appmsg)

我特地回到视频，看了下对应的时间点。

所有的时间点都一一对应，完全没毛病。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PCXyVtfNnxXcRSLM90mQje17RpFUiaZviame9x9guuu0ETSRWG9x9bweQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9P9Jib31I360t8wJlaclHg7tAb07I6iaMdOIYeYhGc4rhbaKxKG0oeQ6cA/640?wx_fmt=png&from=appmsg)

展开它的思考过程，我发现它是真的能理解画面之间的逻辑关系和故事脉络。

GLM-4.5V不是简单地逐帧识别，而是把这些场景串联成一个完整的叙事序列。

从船头的浪漫时刻，到灾难降临后的生离死别，再到最后的救援场面。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9P9ZvTPgFLMh2wdy9URobEdwca0GY91un7OQxwxNicvyML6VN8icpC5sbg/640?wx_fmt=png&from=appmsg)

不仅识别出了视频中的关键画面，还能准确标注时间点。

这种时空理解能力，在开源模型里确实难得一见。

当然，视频理解也有限制。我试了一下，它只能处理200M以内的视频，再大就不行了。不过对于大多数应用场景来说，这个限制还算合理。

同时，注意是MP4格式，不要传成MOV啥的了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PALkCJJ9h6FKibrjxejViadiavTOZXHkgvO8NvWtVk9L6hhjNdhW4tUsKg/640?wx_fmt=png&from=appmsg)

我还试了下视觉定位功能，它能根据指令在图片里做标记。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PpFicA29BQnByLgrvw0MSvrjibZFUQxBibI5XFZzibTCoycG7VLSs1w9wFQ/640?wx_fmt=png&from=appmsg)

我扔了一张流浪地球3的开机大合照，让他帮忙框选出郭导。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PBQQtLR2kTtsyia7UcbZBQDAtEg2A86NMuWMruUAmMV74c2amETiajkMQ/640?wx_fmt=other&from=appmsg)

圈的很正确。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PuwXTYibKHaPz43clA0LJfHmrjVgMWW65Iby3gSexOp2iaoEpW9WrIbEg/640?wx_fmt=other&from=appmsg)

找出烧烤签子也是不在话下，标记的很精准。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PmmvbkwPhvdFPribc2pJDn3QctVANTy9bCGGwicPicJrtuEztFLA4EPl1g/640?wx_fmt=other&from=appmsg)

甚至还有一个超级骚的。

圈出他最擅长的运动。。。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PjFuaibhPw7kibzktdBTR9r6P4HWk7KDiceyOqx7QqiaS9cQWdeVp6SNpxg/640?wx_fmt=jpeg&from=appmsg)

果然是篮球。。。

GLM-4.5V实在是太懂了。

除了视觉定位，还有一个很有意思的功能。

网页复刻。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PXDRU0dGHmNwCptXPoScNSApZLv6shb3cj5YDLrE2vDwOvV62LpTOjA/640?wx_fmt=png&from=appmsg)

我直接扔给它一个网页截图，让它给我复刻出来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PZsG9CWEIwyE7V9dpomoqTu3Bz2RfgFmfLibUYMsUyvOfcoTgh7jQyhQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PibyhbdlX7HD3jEQagVEngY8uVLH9z3qibmeYCeCPcc1Z7uGWhaKOO9Lw/640?wx_fmt=png&from=appmsg)

结果真的震撼到我了，你看这个效果。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq8EAjAA2As6Se9PBjMcz9PS50uibP8ggYkT6AxMCs0u5XN3SeJL9YqlkKoicBaeMQZ4TLlxpMN43VQ/640?wx_fmt=png&from=appmsg)

框架、结构几乎一样，除了一些设计的样式有一些区别。

不过，讲个大实话，我觉得比智谱自己的官网都好看= =

这种看图写代码的能力，以前基本上就是Gemini、Claude这些顶级闭源模型的专利。

现在开源模型也能做到这种水平，真的是一个巨大的进步。

而且，模型完全开源，你可以直接下载权重，部署在自己的服务器上。

GLM-4.5V的API定价也相当良心。

输入只要2 元/M tokens，输出6 元/M tokens，这个价格在多模态模型里算是相当便宜了。

最后，总结一下。

曾经的国产之光，智谱好像回来了。

连续两个开源GLM-4.5和GLM-4.5V，效果都非常的强。

忽然想起上周OpenAI开源的oss，还有GPT-5这一系列的骚操作。

他们好像是那种守着一座巨大城堡的国王。

偶尔会大发慈悲，从城堡里扔出一些金币，希望平民们就得感恩戴德地冲上去疯抢。

而国内的这些大模型厂商，更像一个热衷于基建的狂人，他根本不屑于守着城堡，他每天都在我们家门口修路、建桥、盖发电站，然后把钥匙直接塞到我们手上，说：

随便用，兄弟，不够再跟我说。

所以，当我这两次，都说智谱牛逼的时候。

我相比表达加赞美的，不仅仅是它在41个基准测试中取得的SOTA。

我赞美的，是这种持续不断的、近乎于偏执的开放精神。

海外Close AI，国内天天Open AI。

AI的未来，不应该只掌握在少数几个巨头的服务器里，从GPT-4o的下线引发的风波，就能看出影响。

它更应该，也必须，绽放在我们每一个人的硬盘上。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、dongyi

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言