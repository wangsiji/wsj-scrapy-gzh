     这才是现在最强的AI声音模型。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

这才是现在最强的AI声音模型。
===============

原创 数字生命卡兹克 数字生命卡兹克 2025-05-16 09:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/O8cTsoOjsDbo\_jSdePxkxg](https://mp.weixin.qq.com/s/O8cTsoOjsDbo_jSdePxkxg)

几个月前，我写过一篇MiniMax的AI声音模型。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dBvrnbxaQpGj9Zcibm137KDkibg59LyKmMmvic69yZm1PKvN0lCdLT3VsQ/640?wx_fmt=png&from=appmsg)

我说，那就是当时最强的中文AI音频。数据也有点小爆。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dYP53tsWB0o4oDlEyC0ufibjFVHpNs0HKRcbs7eXzFVoKGyFOq9CEic9g/640?wx_fmt=png&from=appmsg)

而在去年12月之后，至今将近半年时间，在AI声音模型这块，我觉得还是没有能超越MiniMax的。

直到昨天，我看到MiniMax在X上发了他们新一代声音模型的技术报告，Speech-02来了。看来想突破Speech-01的上限，还是得他们自己。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dibEBjNJ8GTNrUVuG0BqR3g2kBm1SetthpGFibbKrhDUSkD0RNa0nq1eg/640?wx_fmt=png&from=appmsg)

不过就是这数据是真的惨淡，看来大家最近关注的都是Agent、MCP，AI音频关注的人，是真的少。。。

我大概翻了一下，跑分确实牛逼不少，主要是WER和SIM这两数据。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dMx916flI92EfyrYvaz38EjQKmlMChOiaiaSlzgHWfrd7W9YdsQhSJRkw/640?wx_fmt=png&from=appmsg)

两个维度，左边是WER，越低越好，代表这个模型讲出来的话，有多准确。右边是SIM，越高越好，代表这个模型讲出来的声音，有多像原声。

你可以简单的理解成，左边看的是AI说的对不对，右边看的是AI像不像本人。

WER的数据，除了一些欧美的小语种，主流语种几乎都压了目前世界公认最被推崇的11Labs一头，特别是周边的亚洲国家，日本、越南、泰国，几乎都是纯碾压姿态，所有语种的WER指标几乎平均都在1~4之间，很牛逼，他们这是正儿八经在多语种上发力了

而音色相似度上，上一代其实做的没有11labs好，海外的很多反馈都是声音没有11Labs像，但是这一次，实现了全面超越，32个语种，每一个在跑分上都比11Labs要强，我自己实测，也能明显感觉到，相似度已经比11labs好了。

我又去看了一下AI音频领域的盲测竞技场。

意外的发现。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9d1IEjBzmO9VBLx76yaJibq6o6t7pzhgOme8NN6bWVXhpcv0ruEE4YMiag/640?wx_fmt=png&from=appmsg)

MiniMax这个新模型。

登顶了。。。

现在，这个新模型，MiniMax Speech-02，已经可以在MiniMax官网用了，目前只有海外版有声音克隆，别问我为什么只有海外版有。

网址在此：https://www.hailuo.ai/audio

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dVam09ODek38zHMhp35MH8gmHUCWyeh5LKf8CdyptSShLFicthhYLSng/640?wx_fmt=png&from=appmsg)

我随手用MiniMax+即梦大师版，搓了一个有趣的郭小纲动画，给大家直观的感受一下，MiniMax的Speech-02有多强。

我就扔了一段不到1分钟的原声进去复刻，说实话，这音调，这起伏，这音色，强的有点不像话了。

我第一次听到的时候，真的感觉真假难分。

不仅郭小纲，还能让，周小伦，来夸一夸我。

太像了。

你闭着眼睛，你是真的能感觉到，是周董，在你面前挥舞着手臂，用那独特的强调跟你说，你还挺屌的。

还有之前万艾尔登法环，预告片里面菈妮的配音我一直很喜欢。

我也让MiniMax复刻了一下。

这是上一代Speech-01-hd的效果。

而这是，Speech-02-hd的效果。

我相信，一定能非常轻松的感受到，情绪的差距。

说说咋用。

进入Minimax的Audio官网后，点击左边的Voices。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dYATUqa7n2vvoAcryFg5veIYibccTdXW10sicJBuELMz46JtesibSQficnw/640?wx_fmt=png&from=appmsg)

免费用户，可以免费克隆3个声音。

我是开了5刀的会员，所以可以创建10个。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dHql9lqMEYK9DyiarNwiaUmTqjsxKsvw1pia6E4oArFQZcvbiacOpmqnIfQ/640?wx_fmt=png&from=appmsg)

点进去以后，直接上传你的素材，然后正常命名，选素材的主语言就行，超级简单。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dqzX1BxlBQ9ugIic7ATQI3VeACVB0wqdvgbrBgqRribA2sy1ONKOGs2UA/640?wx_fmt=png&from=appmsg)

上传的语音最少上传10s的音频片段就可以克隆了，不过这个样本其实不是特别够，**所以我一般推荐音频素材最好在30s左右**，当然你也可以更长，不过一般不需要超过5分钟。

然后只需要十几秒，一个新鲜的声音模型，就克隆好了。

后续使用的时候，直接在右边的声音选择界面里面找到自己的tab，正常使用就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dzO6h3AoVNA2QUYwxKpwnqQLmFI3iad3EKiadXgqYNktrhSibtmEzXX9Rw/640?wx_fmt=png&from=appmsg)

一代的时候，这个声音模型，只支持12种语言，分别是：

**中文、**粤语、**英语、韩语、日语、印尼语、西语、葡语、法语、意大利语、俄语、德语。**

**但是这一次的2代，支持了32种语言。**

而且在混合语种上，有更好的效果了。

比如我之前看到一个非常有意思的挑战。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dibl10icmbVxEff4oeOibIYkz93B6L9l9vDrKlly4zIJ7OwkcbO9GlL0xw/640?wx_fmt=png&from=appmsg)

文字是这样的：

“皆さん，我在网络上面看到有someone把三个国家的 language 混在一起去 speak 。我看到之后 be like これは我じゃないか，私も try one  try です”。

非常离谱。

我克隆了我自己的声音，然后去试着念了一下。

这是上一代Speech-01-hd：

我保证，你听完以后也不知道它到底念了个啥，我就听到一个Speak。。。

再来听听2代的。

虽然日文那还有一点奇怪，但是，已经是能完整的区分出来念的明明白白的了好吧，这已经是，史诗级进步了。

我又搞了一个更复杂的，小皇四郎。

文本是这样的：

> “妈的，最烦装逼的人了。刚回国，问他论文咋样，他说：
> 
> “我要 restructure 一下 framework。”
> 
> 我翻了个白眼，结果他又来一句：
> 
> “Ah non, pas de sucre, merci~”
> 
> 然后切日语：「これはマジでイラっとするわ〜」
> 
> 再来西语：“¡Qué pesado! Pero suena perfecto.”
> 
> 最后还补一句英语：“Seriously. Stop pretending you’re special.”
> 
> 我都想说：你到底是人，还是 AI？
> 
> 哦，他是 MiniMax Speech two，新模型。”

真的，实在太好玩了。

虽然最后的中文，念的还是冒出了翻译腔，但是进步已经巨大了。

而且，还有一个超级屌的点是，他们在讲故事的场景中，如果你只用一个声音的话，在一些不同角色那里，它甚至会有不同的音调变化和情绪变化。

这是我的一份故事文稿。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9djh30WxWBfEgB5n5icveJhgu1DAxMeia6DLCPQBoaicefchgyPPqRkB0fA/640?wx_fmt=png&from=appmsg)

我直接让Speech-02-hd一键直出，然后我自己稍微剪了下，加了点音效，大家可以听一听这个情绪，还有角色的变化。

文稿中标黄的那几句，大家应该能明显的听出来，是刻意压低了音调，改了情绪。这可不是我处理的，是MiniMax直出的，这就非常牛逼了。

除了C端产品之外，我看了一眼API，发现，他们已经第一时间把Speech-02给支持了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9dmkYZFamk8f9suENoJYGmZtnqOsts7ZwHPWBZ0rS1GANcoJicWRicia6Jw/640?wx_fmt=png&from=appmsg)

甚至，MCP也弄好了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpBjn7We3QNcX2ZZ3M8Ck9diacT4lO7iaw3F6zAhPhcR0tqBe0YRgiciciaQQic3LIwaflEolYfrklDjiamA/640?wx_fmt=png&from=appmsg)

现在，你可以在任何Agent产品里，也可以接入这个逼真到爆炸的语音模型了。

我们也可以自豪的说一声。

**之前，中文AI语音，我们做到了世界最强，但是现在，可以把中文去掉了，整体上，我们都已经做到了世界最强。**

这是一个被所有人低估的战场。

大家都在盯着谁做出第一个像人一样思考的Agent，却没看到，那些AI说话的声音，其实早已变得越来越跟真人无异。

而且，这一次，还是我们做出来的。

**在12月份的那边MiniMax AI音频的文章中，我在最后写道：**

**“也许，这就是属于中文世界的AI时代的序章。而这一切，才刚刚开始。”**

**然后就是波浪壮阔的春节。**

**随后的故事，大家也都知道了。**

**一语成箴。**

现在的AI世界，再也不是英语的独角戏了。

我们从配角，走向主角。

然后不仅仅止步于起。

像MiniMax，也用AI，给世界，尽可能的带来语言平权。

那些过去没被在意的语言，过去只能在家族里、在小巷里、在庙宇里才能听到的声音，现在终于有机会，能被世界听见了。

AI没有带来统治。

反而是把人类的多样性。

放进了未来。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言