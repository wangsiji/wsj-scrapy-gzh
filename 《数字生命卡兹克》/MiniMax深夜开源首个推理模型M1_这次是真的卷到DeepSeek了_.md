     MiniMax深夜开源首个推理模型M1，这次是真的卷到DeepSeek了。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MiniMax深夜开源首个推理模型M1，这次是真的卷到DeepSeek了。
=====================================

原创 数字生命卡兹克 数字生命卡兹克 2025-06-17 09:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/Geqqign1Q0dtpEpXjd5EEA](https://mp.weixin.qq.com/s/Geqqign1Q0dtpEpXjd5EEA)

不知道还有多少人记得，AI行业的六小虎。

行业内都在说，他们已经寂静好久了。

上一次相关的项目发布，还是前一段时间我写的MiniMax声音模型的更新，Speech-02。  

而昨晚凌晨将近12点的时候，又是MiniMax，居然在X上，预告了他们一整周的发布计划。

给我整不会了，不是，为什么总是选择这么阴间的时间点发布啊。。。

而第一天（也就是昨天），发布了他们MiniMax Week的第一个项目：开源MiniMax首个推理模型M1。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiadEoW3A3bEcCDRFwk3jSicEnwcEJAJjKMdJ69SibUBt1swmm6mCYuzKgA/640?wx_fmt=png&from=appmsg)

出手就开源，还是秀的，看看跑分。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaX7LM5B1ZcRngN36guLOg9wMk1yicKwg1LzuPdsxupZiaH40JZSy8icN6Q/640?wx_fmt=png&from=appmsg)

我先说结论：“MiniMax M1的上下文能力，就现在全球最屌、最牛逼的、足以媲美Gemini 2.5 Pro的开源模型。”

我愿敬称为新一代源神。

在AIME 2024逻辑数学题目上（偏奥数思维）和LiveCodeBench编程题上、还有SWE-bench Verified（真实世界代码补全+修改），MiniMax M1的表现只能说中规中矩，有弱的、有强的。

而TAU-bench（需要理解任务目标、推理动机的场景），M1 准确率62.8%，开始媲美开源模型。

但是，最离谱的来了，最后一个，MRCR（4-needle）。

这个直接，屠榜了，真的就一瞬间，一柱擎天，直接跟Gemini2.5Pro肩并肩，我相信用过Gemini 2.5 pro的伙伴，都知道，这玩意的上下文有多离谱，而现在，MiniMax M1作为一个开源的大模型，首次，在这个评测集上，能跟Gemini 2.5 Pro并驾齐驱了。

我特么。。。

很多人不知道MRCR（4-needle）是个啥，我简单解释一下。

AI圈之前一直有一个测上下文能力的测试，叫做“大海捞针”。

我23年的这个测试刚出来的时候我就写过：[花7000块实测Claude2.1 - 200K Token的超大杯效果究竟怎么样？](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647660485&idx=1&sn=4b73724a8e669281e065dbdd2068bbf9&scene=21#wechat_redirect)

X上一个大佬Greg Kamradt，为了弄明白当年Claude2.1的200K Token，究竟实测效果怎么样，就调用Claude 的API做了个压力测试，从一段不同长度的文本中，捞出特定的信息，而这个测试，花了他1000美金。

这图我现在还有。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURricMgzcl9V8BnIROd3wBKrMw22PIsxTF9oCg9dFT8YSHfHuct8oWMNKyNky4mNtwwibeayNibplMWOA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

Claude-2.1当时红了一片，200K几乎没有蛋用，巨水无比。

而那一次，Kimi在我的文章下留言，说自己内部测了一下，全绿。

后面的故事，大家也就都知道了。

后来呢，Gemini觉得这个大海捞针测试太初级了，于是自己搓了一个新的测试方法，叫做Michelangelo。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaBqsrMnZWxoTOqzhic8lKBAzabNriaXic9PpUmVN8f0eoQKEiaqvbTXBQpg/640?wx_fmt=png&from=appmsg)

在这个论文里，他们提出了Michelangelo的几个评估任务，有Latent List、IDK，而第三个，就是MRCR。

全称叫Multi-Round Co-reference Resolution，翻译成中文叫多轮共指消解，反正非常拗口。

它主要考察一个模型在处理较长的、多轮对话时，能否准确地理解和区分用户要求中具体指的是哪一次对话、哪一个内容。

比如用户和AI进行了一系列对话，用户要求AI写一些东西，比如诗、谜语、文章。在这些对话中，会刻意插入多个看起来类似的话题（比如多首关于企鹅的诗）。

然后再让AI回头去重新找到某一次特定的话，比如用户要求“再重复一遍第二首写企鹅的诗”，此时模型必须精准识别这个“第二首”指的具体是哪一次回答的内容。

这个事其实不简单，因为对话很长，涉及多个话题和文体，非常考验模型的上下文理解力。

![已上传的图片](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaKciauPiaJ9ibvKLMesGGbwS6KIkSlVjRVIdFvicR66hDMTq6RFcRwtSTOw/640?wx_fmt=png&from=appmsg)

有些内容在主题和格式上极其相似，比如“关于企鹅的第一首诗”和“关于企鹅的第二首诗”。模型必须能清晰区分、精准回溯。

后面OpenAI在发GPT-4.1的时候，也在blog里面提到，自己魔改了一个难度更高的MRCR的评测集，用来评估模型的上下文性能。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiamQbAc8aIQGj0cjB4icSahCJEcOicfkbYKMMpQqE26gpP3gOrwoD1UqyA/640?wx_fmt=png&from=appmsg)

而“4-needle” 指的是，在同一段超长上下文里同时埋下 4 个“针”（关键信息片段），然后在后续对话里以交错的方式把这 4 根针全部翻出来。

在这个任务下，MiniMax-M1，吊打了一切，只跟Gemini 2.5 pro，差了那一点点的距离。

我翻了下技术报告，M1之所以在上下文有这个性能，核心点还是在于他们之前开源的基座模型MiniMax-01。

得益于MiniMax-01 Lightning Attention线性注意力机制的应用，M1的时间和空间复杂度随序列长度增加**近似线性增长**，不像传统Transformer那样呈平方级膨胀。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiazB7wBqnhPDJPPYUtb3ialRbiboP9bnx89QEkDfBicpb4YZgu5YpEO7vJg/640?wx_fmt=png&from=appmsg)

因为Lightning Attention机制，在推理生成长度64K token时，FLOPs消耗不到DeepSeek R1的一半。

当生成长度达到100K token时，M1仅消耗其约25%的FLOPs。

非常的离谱。

而这个MiniMax-M1，跟之前开源的基座模型MiniMax-01一样，也是456B参数，MoE架构，实际激活45.9B。

最长上下文长度为100万字，也就是1M，是DeepSeek-R1的8倍。

这次开源了两个上下文长度的推理模型，40K和80K。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaNptFfLVj4kX648gicyGYoVNBAIrYXDjz4FS34mBovicLOEicw6f6TY6nQ/640?wx_fmt=png&from=appmsg)

80K版本是在40K版本基础上进一步训练得到的增强版本。

这里注意一下，80K和40K指的不是上下文长度，上下文长度是1M，80K和40K指的是Extended Thinking的上限。

GitHub: https://github.com/MiniMax-AI/MiniMax-M1

Hugging Face:https://huggingface.co/spaces/MiniMaxAI/MiniMax-M1

目前在MiniMax的官网上也上线了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaWCJhNeRUuG0t8Gricvk5pD1AyJL27ZMBxe2yHYoV5pVhp2QjJ55rOEg/640?wx_fmt=png&from=appmsg)

网址在此，可以直接用。

https://chat.minimaxi.com/

我也第一时间，上去测了一下。

我的第一个任务，就让我开了眼，因为我只是，小小的尝试一下，没想到效果，比我预期的还要好，我直接把MiniMax-M1的技术报告扔了进去，让它，给我逐字翻译。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaamEZCsSUqmmEZJNnsVtO5fyqLq32Dl5QBPCwgNy1aic0oVVt1dRW8pQ/640?wx_fmt=png&from=appmsg)

现在看着还比较正常对吧。

但是，马上，离谱的事情来了。

他居然把图，也给我...带出来了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiafVacvK7K2iajgDH95FyCS4Ffkjh0k0wE2cX4icq4YnNxuzoNE6NBpTJg/640?wx_fmt=png&from=appmsg)

甚至不仅有图，还有，公式。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaULanmnZBudnUalwURUvAStSibh6nwaYgGsnMp7dmZC8o8IJayCCicD6A/640?wx_fmt=png&from=appmsg)

还把表格，直接拎出来翻译了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiarAtKQTxHjnpe3iaglIk8tTeygtw3UtBf0qsBSEriaFaOORIGJWyfIpnA/640?wx_fmt=png&from=appmsg)

这效果，这体验，真的无敌。

虽然中间，有部分的图表丢失，还没有达到100%的完整度，但是这个效果，也已经非常非常好了，关键的是文字，一个不落，全部都整整齐齐的给我翻译出来了。

最搞笑的是，他还自作主张，在最后，可能觉得参考文献翻译出来没什么用，直接自己给省略了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaVC5lCjBYANhyibJaH54OxBibS3icBkQic9C3M6oYicfhYlEm5zicy4iaD5D4A/640?wx_fmt=png&from=appmsg)

我说实话，这个参考文献，占了5页，对我来说，确实没啥用。。。

在翻译上，我又试了一个更有趣的场景，我扔了一个文档过去，然后说：

“翻译成中文，在括号里标注一些符合我英语水平的原文英文词汇或短语。我英语水平是大学六级。”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaQjRzLXOUic6H6VAe4oEAEtowI49z3lvcZl4sPcjEUBvAWBlJ6LXG4FQ/640?wx_fmt=png&from=appmsg)

太有意思了，这个上下文准确性，是真的牛逼。

然后我又做了一个测试，把我群里这一周的聊天记录，导出出去也扔给了MiniMax-M1，让他把绛烨的聊天记录都找出来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaWrDHYExGkFt184ujRicibLveUjIwrmr0zfCeJrZxmLAtEKyOzGL9OfwA/640?wx_fmt=png&from=appmsg)

他准确的识别除了绛烨的微信ID，然后找到了他的微信号，扒出了他的所有聊天记录。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaeEdT34MFicJ1zP0VZycDWqlRyWkkLVyJlaklBoH4FgVWc4epvxibia4RQ/640?wx_fmt=png&from=appmsg)

这些链接，是真的能点的，我惊了，他还做了样式重构。。。

因为超长超准的上下文，你还可以，跟大模型玩一局，真正的文字冒险游戏，因为他不会忘记你的出身，他会记得，一切。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiavzp3PxbhrlQa9HLZlebYUB6jhicvwF4ohlUBSibcPCSX2BkBKh1q1o4Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaonANdxq3YR3hhlA7LmmKaZHOhialmGod7QVIFDxc4hU3jkDLRvWfc3A/640?wx_fmt=png&from=appmsg)

推理模型+超长且精准上下文的扩充，确实会带来，很多不一样的花活玩法。

比如我还有一个特别狠的测试。

就是我手上有一个34个刘慈欣老师的小说的合集，因为大刘除了世人皆知的三体之外，他其实还写过特别多的科幻中短篇小说，也特别好看。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uia7KZajibFN177GsTL6oEdoAYZKsiblPtGGbvI2MIn18DeSjxHC5ISvlAQ/640?wx_fmt=png&from=appmsg)

比如我最爱的《山》。

我现在，想把这些故事，安利给我的朋友们，我想，让AI根据这34个故事，每一个故事都写一段故事总结+推荐语。

这个任务，你要是扔给DeepSeek。

你就会得到一个非常离谱的提示，DeepSeek只阅读了8%。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiaoXOBiaB1mYraXw3upWibJJiasF4q8sRoTL5fhXA3mXlDXI2g51dEmOibtw/640?wx_fmt=png&from=appmsg)

而MiniMax-M1，出色的完成了任务。

  

超长上下文的魅力，此时体现的淋漓尽致。

不过我有一个更变态的任务，还是给MiniMax-M1干宕机了。

就是...我让它数本草纲目里一共有多少药材= =

数了8分钟，最后跟我说，有400中种，但其实答案是1892种= =

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uia0icz5cwrB19eCN5KevubcFx5zib5Klxos1qiatPfs2UQU2CNsN8W6DefA/640?wx_fmt=png&from=appmsg)

不过我也能理解，这个任务，确实实在是太变态了。。。

除了上下文之外，我也测了些写作、编程、数学。

写作和数学就不详细提了，写作这块中规中矩，数学的高考题实在没空完整做了，我觉得我需要抽空写一个脚本。

不过测了两道大题，目前是都对的。

最后稍微吐槽一下编程这块，就是前端审美，感觉还是有一些进步空间的。

就...有一点，不好看啊。

比如我昨天下午去参加了飞书多维表格的闭门会，会议特别有价值，我想做个可视化网页。

这是Gemini生成的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiakcLXz5sba7Cl3RO8JYibECOxuPms6Q4ic0tAFq2s0bU8TxSf0UPcAowg/640?wx_fmt=png&from=appmsg)

这是M1生成的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uia2tUgiazBh2o39rCQzwa1iblYSObaVuFDx7SLjUSpERSRAYKz8SM3v5OQ/640?wx_fmt=png&from=appmsg)

咱就是说，可以不这么直男审美的= =

总体来说，M1模型，还是让我有一点惊喜的，他们自己的新研究，确实卷出了一些很有意思的特性，也把开源领域的模型水平，又拔高了一个层级。

还有4天时间，我现在有点期待MiniMax会继续掏出什么有意思的大货了。

以我对MiniMax的了解，视频模型总归要来一个的吧，已经有一段时间没更新了，Video 01-Director已经是几个月前的事了。

你Hailuo 02（0616）都去打榜了，那你这5天里，得掏一下吧。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo68knKhbmDib0KGXENqt4uiah5zpwNjNteXTWxqSoFDaJZA6bWJM9DKeicWAXGWfuFdhMTFDePKnTbQ/640?wx_fmt=png&from=appmsg)

  

海螺的人物情绪表演、动作表演，至今依然是我心中的白月光。

极度期待Hailuo 02，在人物表演上，会带给我什么样的震撼。

声音模型估计不发新的了，因为一个月前Speech-02才发。

图片和3DMiniMax不做，那在掏个音乐模型？这个符合MiniMax的气质。

这一周，希望MiniMax尽情撒货吧。

让AI的这一把火。

烧的更热烈些。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言