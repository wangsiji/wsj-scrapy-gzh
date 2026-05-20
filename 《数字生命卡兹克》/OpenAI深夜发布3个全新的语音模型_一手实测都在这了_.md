     OpenAI深夜发布3个全新的语音模型，一手实测都在这了。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

OpenAI深夜发布3个全新的语音模型，一手实测都在这了。
=============================

原创 数字生命卡兹克 数字生命卡兹克 2025-03-21 06:08 北京

> 原文地址: [https://mp.weixin.qq.com/s/GjzPPANJktEE8HomAnTtIQ](https://mp.weixin.qq.com/s/GjzPPANJktEE8HomAnTtIQ)

OpenAI最近总是喜欢搞突袭。

昨晚11点的时候突然发了一个预告，4秒钟的音频的大概意思，就是太平洋时间10点我们发个产品。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dmhSy0OEcWWjHaXD0icuuicW50qpE1ykAX7zoKSrHaYPaT3mp0hefydlA/640?wx_fmt=png&from=appmsg)

然后就在北京时间凌晨1点，开了一场直播，发了一些新玩意。

总结一下就是：

2个比Whisper更好的语音转文本的STT模型：gpt-4o-transcribe和gpt-4o-mini-transcribe，1个文本生成语音的TTS模型 :gpt-4o-mini-tts。这些模型都提供了API的接入方式。没了。

一个一个说。

  

1\. STT模型：gpt-4o-transcribe

gpt-4o-transcribe和gpt-4o-mini-transcribe说是两个，其实也就是一个了，后者是前者的小参数版。

这个模型的作用跟当年的Whisper是一样的，跟大家在剪映里用的一键生成字幕的作用也是一样的，就是把一段语音，转成对应的正确的文本。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dFib3hRyNfNchPTS2yicxCgX7sGEfbupeJeddgRD33hcaChUtzQMzPI3g/640?wx_fmt=png&from=appmsg)

我们一般把他们称为，STT（Speech-to-Text）模型。

这个模型的核心，就是就是识别文字的准确率有多高，我相信大家在用剪映生成字幕的时候，一定会出现很多文字识别错误的情况，所以评判一个ASR模型效果咋样，就看正确率。

他们的跑分是这样的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dT2P4cXiatsiaZx9RibRqgkYq3ia7tc44iaQ8ic1376z3xKj5Kr2VRpUfcxwQ/640?wx_fmt=png&from=appmsg)

这个是OpenAI的几个STT模型在FLEURS数据集上的词错率（Word Error Rate, WER）的对比表现。纵坐标表示词错率，越低代表模型的转录准确性越高；横坐标代表不同语言。

词错率的意思就是用于衡量语音识别系统的准确性，它通过计算模型转录文本与人工参考文本之间的错误比例来得出，错得越少，WER越低，模型的表现也就越好。

中文是从左往右数第五个，cmn，可以看到突出了一个小山丘，错误率一下子就都上来了，比隔壁几个都要高一些，中文还是难。。。

最后那几个一柱擎天的语言都比较小众，比如bn是孟加拉语、mr是马拉地与、最高的那个ml是马拉雅拉姆语。。。

他们除了跟自己比外，又放了一个跟别人家模型相比的图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00d8KmthVDsvg5fkF5DjhR2jFSXHrraOllR9XJwQh4CEiahmqziapB2YicYQ/640?wx_fmt=png&from=appmsg)

Gemini是google的，scribe是Anthropic的，在对比的这些里面，确实达到了SOTA，但是不知道没比的模型里面，有没有比OpenAI更强的。

我自己也做了一下实测，把我的两个口播视频去识别了一下，识别出来的效果在此，大家可以对比一下。标红的就是识别错误的地方。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dnjCql7pkIiaNicqCUXhomSBJw5WpyQJeOHicns1ibTQLq9YxdtoPiblD21Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dxm7iaFfTsuuknpA0Rb05jXiaEIEMOibIicNulqiaBepwlyKOJl6icZpfNVlQ/640?wx_fmt=png&from=appmsg)

其实都大差不差，这么一看，GPT-4o-mini-transcribe的性价比感觉非常突出。

GPT-4o-transcribe这个系列的两个模型，有一个蛮不错的特点，就是会自动清噪和去除非主线人物的语音识别。

比如这个案例。

这个片段是剪辑完的成片，所以有音乐，甚至在19秒以后，还有BGM里面的别人唱歌的声音，这些其实都是噪音，GPT-4o-transcribe几乎全部剔除了，在整个转录里，我几乎没看到什么错误，除了把我的名字，卡兹克识别成了卡斯克。。。

我又试了一段粤语的，效果居然还可以，大致的好像是对的，就是细节这块我不太能验证了，有懂粤语的朋友可以看一下。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00delLbmEbPI8WAQu7clianm92EPaLpbjbkdtGr4Hz3icd6CN9Cch9jo4Dg/640?wx_fmt=png&from=appmsg)

最后价格这块提一下。

gpt-4o-transcribe是每分钟大概$0.006，也就是人民币0.04元/分钟；

gpt-4o-mini-transcribe是每分钟大概$0.003，也就是人民币0.02元/分钟.

整体不算贵了。

  

2\. TTS模型：gpt-4o-mini-tts

OpenAI的一个新的TTS模型。

在英语效果和声音上，听了下，还算不错，不过毕竟这是国内，所以其实我更关注的是中文的生成效果。

我随手跑了一个，就，你们听听这个效果。。。

情绪什么的其实讲道理，还可以的，就是这个中文发音，真的一股子大佐味，这到底用的什么数据集啊。。。

11Labs也有这个问题，中文根本没法听，太违和了。

对比一下海螺（现在产品也更名叫Minimax了），他们的Audio生成出来的同文字的中文是这个效果。

在发音上，根本就不是一个级别的，中国人的语音模型，还是得看中国制造。。。

英语上，感觉很纯正，日语发音上，也感觉有点怪怪的。。。

这次OpenAI给gpt-4o-mini-tts做了一个小小的功能演示网站，约等于免费给大家用了。

还挺有意思的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dXcqb2gk5qJRSk4ARbiaP8MvhWmlQ2ZUicZsXCrlNTfAbAEP7GVkSPv3w/640?wx_fmt=png&from=appmsg)

网址在此：https://www.openai.fm/

最上面的VOICE是固定的音色，音色你是没办法克隆也没办法自定义的，所以只能选这些。

下面的VIBE比较有意思，大概的意思就是情绪基调，有N多的预设模板，同时你也可以用Prompt自己捏。

OpenAI给了官方模板，是这个样子的：

    Voice: High-energy, upbeat, and encouraging, projecting enthusiasm and motivation. 

翻译过来就是：

**声音（Voice）**：充满活力、热情洋溢且积极鼓励，声音要能传递出热情与动力。

**标点（Punctuation）**：使用短小有力的句子，并通过适当停顿，保持兴奋感和清晰度。

**语速（Delivery）**：语速较快、富有变化，并用升调增加节奏感与吸引力，确保听众持续投入。

**措辞（Phrasing）**：直接明了、强调行动，使用鼓励性的语言来推动听众积极参与。

**语调（Tone）**：积极向上、充满能量与力量感，营造鼓励与成功的氛围。

所以我们是能看到，有5个可以自己去捏的参数。你可以随便自定义。

但是这玩意，说实话写起来也非常麻烦，我试了一下后，不如直接交给AI，这玩意谁特么手搓啊= =

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dzvqpycWgRe59GTOzrje8jqXERibfzp6udNEHxjUB5Eb2Qib9G4sqa0xA/640?wx_fmt=png&from=appmsg)

几秒钟，一段定制好的prompt就OK了，我们扔到之前的网页里。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dLWZBbprBL4kuSzJLbVIYibHUKAO4LhpoibFKoGtiaEaBbc5KiaSWu4muibQ/640?wx_fmt=png&from=appmsg)

再用一段我很喜欢的《反叛的鲁鲁修》里面的台词去试一下。

大家自己判别吧。

在价格上，gpt-4o-mini-tts是$0.015/分钟，大概1毛钱人名币1分钟，说实话，已经几乎是最低价了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dWC0NicZoKnOO7dN4XCCXKJo8Kx4JJtXicUu45UoxB71K6QEEwpLSohgQ/640?wx_fmt=png&from=appmsg)

11labs的价格大概是每分钟1块3人民币。

Minimax已经算是价格屠夫了，大概也要1毛8人民币1分钟。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrSNRqXGZxc1erUoHIuN00dTkC5Mz9b5BJpmxocAicGcpqajzPfQLlkPJgaBuF3uMicbN6FlyE4Yd8Q/640?wx_fmt=png&from=appmsg)

  

写在最后

这就是OpenAI今天的发布了。

如果你是开发者，想知道怎么接入，一切都在他们的API文档里。  

https://platform.openai.com/docs/guides/audio

这次还蛮方便的，10行代码就可以接了。

STT模型gpt-4o-mini-transcribe我还是蛮推荐用的，实测下来感觉性价比最高，差距不是很大，价格还低一半。

TTS模型gpt-4o-mini-tts如果你是做英文场景的语音，还是值得一用的，毕竟便宜是真便宜，效果也还不错，中文的话不推荐用，因为没法用，中文我还是无脑推荐Minimax的Audio模块，不仅中文效果好，性价比高，海外版还可以语音克隆。

网址在此：https://www.minimax.io/audio

很久以前我也首发安利过一次，现在依然有效：[30秒就能完美复刻你的声音，这就是当今最强的中文AI语音克隆。](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647667095&idx=1&sn=b7c79eed641ea11617e6371f1616049f&scene=21#wechat_redirect)

以上就是这一次OpenAI的全部发布了，熬夜肝完，为大家带来最新鲜的实测。

好了，我要去睡两小时了，预约的早上9点医院做手术![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Hurt.png)...

大家晚安~

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、dongyi

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言