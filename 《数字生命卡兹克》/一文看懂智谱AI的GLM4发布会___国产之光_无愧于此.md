     一文看懂智谱AI的GLM4发布会 - 国产之光，无愧于此 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

一文看懂智谱AI的GLM4发布会 - 国产之光，无愧于此
============================

原创 数字生命卡兹克 数字生命卡兹克 2024-01-16 14:03 天津

> 原文地址: [https://mp.weixin.qq.com/s/ZAK3JBilKRmLyEmuqI6Ugg](https://mp.weixin.qq.com/s/ZAK3JBilKRmLyEmuqI6Ugg)

众所周知，国内的大模型公司，我一直很喜欢智谱AI。  

不只因为他们学术气息浓厚，技术底蕴深。

更是因为这家公司的真诚、开放的态度，前端时间他们给AI创业者提供的“Z计划”，更是让我感叹他们的格局。  

今天，他们终于正式召开了他们的发布会，但是这个发布会的结构还是非常“智谱”。  

标题叫：

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoEBYAYG5W94e0AMxIXx2sy0snwgGs8EeZniaFG11vLf7T1CqkFzhLhXs8ho2gfNm7UcchC9lBrFUg/640?wx_fmt=jpeg&from=appmsg)

符合他们一贯作风，上午发布GLM4、ALL Tools、多模态大模型CogVLM3

、代码大模型CodeGeeX3、汇报技术进展，下午圆桌讨论讲干货。

核心还是GLM4的发布，这个应该是国内所有AI相关人员，都在关注的东西了，其意味不亚于去年大模型GPT4的发布。  

毕竟，中国，也真的需要自己的，真正属于自己技术路线的大模型。  

这块多说一句，GLM是跟GPT完全不同的技术路线，具体的可以看这张图。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syoznLnBoQAMG6InhRbibyYicaGflgaHApDiaRmu3o2WDoLKchC2W0dSQcg/640?wx_fmt=jpeg&from=appmsg)

基于Transformer架构的模型有三种：仅编码器架构（Encoder-only）、仅解码器架构（Decoder-only）、编码器-解码器架构（Encoder-Decoder）。

GPT走的是仅解码器架构，而智谱是借了编码器-解码器架构思想走的自己的路，这也是我为什么一直很关注他们。

他们之前开源的GLM6B，在国际上掀起了多少的风浪，也相信不用我多说了。  

回到今天的GLM4发布会。  

我觉得可以用3个点来总结掉：  

1\. 基座模型的性能提升。

2\. All Tools。  

3\. GLMs。  

从整体上看，智谱AI毫不避讳的直接对标OpenAI，用他们的话说，我们还在不断的追赶OpenAI，追赶GPT，他们有的，我们都要有。  

一条一条来说。

**一.GLM4基座模型的性能提升** 

首先是基座的评分：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syd9TDzH2rDhvic7fjLvluxEicEkgvXjO4NklO677PsbAfbjNNGuClvRIw/640?wx_fmt=png&from=appmsg)

几个比较主流的评测任务。我简单的介绍一些这些评测集的代表意义吧，让大家知道GLM4在哪些地方效果好，哪些地方跟GPT4还有一些差距。

1\. MMLU(Massive Multitask Language Understanding)：这个测试是一个大规模多任务语言理解测试，主要评估大模型的对于知识的理解的，可以看到目前GLM4是81.5分，GPT4是86.4分，目前能达到GPT4的94%。

2\. GSM8K (Grade School Math 8K)：主要是测试数学能力，基本就是小学数学和初中数学水平。GLM4打到GPT4的95%。

3.MATH：跟GSM8K 有点类似，也是偏数学，但是会更难更复杂一点，涉及到一些比较难的逻辑推理。目前GLM4只能达到GPT4的91%。

4\. BBH (Big Bench Hackathon)：偏综合测试，有一堆综合类的任务，比如翻译、语言理解、逻辑推理等等乱七八糟的。这块GLM4很强，基本跟GPT4打平，能到99%。

5\. HellaSwag：偏常识测试的任务，看看大模型有没有人类的常识。这块是目前GLM4对比GPT4最弱的一个，只能达到90%。

6. HumanEval: 纯粹的编程任务。评测大模型在算法、代码、编程层面的效果。这块是GLM4唯一超越GPT4的任务，非常强，程序员有福了。。。

从这些里面，你就能大概知道GLM4目前是个啥水平了，智谱也很实诚，从来不会说全面超越GPT4这种鬼话，不弄虚做假，客观的承认差距，然后努力追赶，这点我非常非常喜欢。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syL1UJ0IHgM3sib8B0ibUmkEZjkxH3QG4INla27TytDYS5xpjD8OnjpQmA/640?wx_fmt=png&from=appmsg)

基座能力第二个方面就是指令跟随上，通俗点说，就是理解Prompt和Instruction的能力上。GLM4目前大概都在GPT4的88%左右。

GPT4的语义理解和吃Prompt的能力，我相信大家都知道，基本是冠绝全球，不要以为88%所以不咋地，你要看跟谁比。。。国内的很多的所谓全面超越GPT4的大模型，你能达到60%我就愿意给你磕一个。。。。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syV4ZTeIjft5yqC5XfzHeAoELRPA3cPYEqE16yVmh7ICF4dQQE3e1mhg/640?wx_fmt=png&from=appmsg)

中文的能力，各方面都比GPT4强一点，这个正常，毕竟GPT4就那么点中文预料，超过是正常事。但是可以看到，在推理这块，受限于大模型本身的底层能力，还是差了一点点。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syiaQUIp1RNZhXibRP4jHo9Y0eeib3HmYzpIDPHf0DOpl2UAAt8drTlNFrg/640?wx_fmt=png&from=appmsg)

GLM4终于也上了128K的长文本，大概等于一次性灌300页吧，最好玩的是智谱自己也做了一个“大海捞针”的测试，很有意思。  

我之前写过一篇关于[GPT4和Claude2.1的“大海捞针”测试](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647660485&idx=1&sn=4b73724a8e669281e065dbdd2068bbf9&chksm=f007cb92c77042849fb25fd1c982d4c305448ab79ea018664c8cb53ee6dd6169589a54058b90&scene=21#wechat_redirect)，有兴趣的可以去看看，看完你就知道，全绿是个多离谱多牛逼的事了。

**二.ALL Tools**   

ChatGPT有一个能牛逼的玩意，我相信用过的人都知道，就是他们的All Tools，在一个任务里，可以同时调用联网、画图、识图、代码解释器。形成一个小型Agent，能做很多很有意思的事情。  

目前国内还没有一个能真正把ALL Tools搞出来的，智谱是第一个。  

其实他们的识图能力其实早就有了，代码解释器也有了，这次主要是新增了画图的部分，也就是CogView3。再将它们全部打包在了一起。

比如我说一句：“搜索一下过去7天北京的天气，然后给我处理成一张表格让我可以下载”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2sybQlaiaWzeN759HcdnYasAQ4cjXIicfHIEdicLFx15XRtQsJFEPqFP14iaw/640?wx_fmt=png&from=appmsg)

直接就给我处理完了，非常爽。第一次，在国产大模型上用上了ALL Tools。要知道，GPT4的联网搜索默认都是外网，那些个结果，很多时候真的特娘的水土不服。。。

然后智谱也上线了他们的绘图大模型CogView3。  

有一说一，之前智谱的画图模型，真的，有点丑emmmm.....

但是这次得到了大幅的加强，至少，能看了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2sybUibYGpSlnMLskdRNlqGnwl6f4U74W5hHrmNOxuEtjfdhQLa7dGTyZQ/640?wx_fmt=png&from=appmsg)

你要是拿它跟MJ比那就有点欺负人了，但是至少画出来的东西不丑，能用，并且最好的一点是，可以用自然语义去做微调。  

比如说，我先让他画一只“短脚柯基在公园里奔跑”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syeaiag0c9MXLicsIeeQEaeG0caoWhbjTpxbn4Wicic6lyEHQicQLrUtwcspg/640?wx_fmt=png&from=appmsg)

画的还不错，挺可爱的。然后我们再说一句：“给它旁边加几只蝴蝶”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2sybP9UH7Aicm1SHJufKHx9l9p0IcA5f2YmFKyPibGMbF87fRtVZMN4U0RQ/640?wx_fmt=png&from=appmsg)

小蝴蝶就加上了，这种感觉还是很爽的。说实话，我还是喜欢用这种自然语言作画。。。  

然后再放几个他们的参数，从数据层面对标一下GPT4，这块我就不去做过多详细的解释了，有兴趣的可以自己去用智谱清言识图，让他给你解释一下。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syWFLxdSn8W8dBRbuuqIAxhYpP0qOmVqhSiciaSG8zhID6yOWZbHmm6ib1Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syj6oAnWlgqoibKMeWF9BeSJFlhWnMlxLtj6icVViaaY4HdI69K7kbDNx1A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2sylum3aiaCvQYIPYFHU7OqHY13vkSMiaq5zKrDh5qIfApJXwv0SYpeXybQ/640?wx_fmt=png&from=appmsg)

他们自己官方也放了两个例子，可以简单看下：  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2sySgVI5AKlKTBxUTfrsLxiadR1uju9Xv6IUsW2d5heX6CFF6oXuCgwGFg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syl2RbxRsypAAnzGQKgibbHWRib2BZPn49tgIOTiapCVH6W56RnR40JULrA/640?wx_fmt=png&from=appmsg)

**三.GLMs**

众所周知，OpenAI上线了他们的GPTs，前几天也上线了GPT store，被各种人吹为下一个APP store。当然，到底是不是，那就是另一个话题了...

现在智谱也正式上线了他们的GLMs和智能体中心。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syjvd62kXSeFj5eDdh3UnCOl7TdVu4icwvZQJxfsuFMbic8tzlEQXsjz7w/640?wx_fmt=png&from=appmsg)

目前没有搜索，只有官方推荐的，基本能保证这些GLMs的质量，毕竟GPTs那玩意，真的鱼龙混杂。。  

而在整个GLMs的创建页面上，智谱这次挺致敬的（笑。跟GPTs基本一摸一样，你用过GPTs创建智能体的话，就会很容易上手了。直接用自然语义来，来说人话，就OK。你做完了以后，也可以分享给朋友。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syD3XItZjKwgt2FxACQGJlIHyu9zcbXicpEpeZJh5UGFztUksx95B6udw/640?wx_fmt=png&from=appmsg)

他们也即将公布创作者分成计划。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syhHCibmwuv7psoGRstBABfVPDbHJU3FOMibMV6YZMBsTvPpUy6GjItncg/640?wx_fmt=png&from=appmsg)

期待一下后面的生态，看看智谱要怎么运营这块。  

**写在最后**

说一个有趣的小故事。

早上智谱CEO张鹏在演讲讲一半，即将开始现场演示时，直接宣布GLM4已经正式上线，大家可以立刻在线上使用了。

（PS：这里放个他们的网址：https://chatglm.cn/，或者下载APP智谱清言）

然后才开始的现场演示。  

然后，就，翻车了。。。当时在画一张图，我记得好像是个狗还是啥，愣是加载不出来。

如果这是别的国产大模型公司，可能就各种冷嘲热讽就开始了。

然而在群里，大家在看到翻车后，画风完全不一样：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syWxSIU7ibc7EuicwaseV3bpSFfIjiaq7iboSKl1iatt4ibjtM1b3iamcqyiavGg/640?wx_fmt=png&from=appmsg)

你的口碑、你的真诚，是会被所有人看到的。  

这是绝对的，长期的力量。  

智谱的开源、贡献，国内AI行业肯定都是看的到的。  

比如他们又成立了大模型科研基金。  

掏1000张GPU、1000万人民币、1000亿的Token，来支持开源开放的大模型软件开发。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoEBYAYG5W94e0AMxIXx2syA5Z5U93ibXKvSB0jsATiahltvKticZDQRSMOyqFQ3o9eCVwNvXYp0IPVQ/640?wx_fmt=png&from=appmsg)

我觉得，这就是中国AI，龙头的格局吧。  

我不是什么AI圈的大牛，更不是什么KOL。  

我就一普通写文章的，也没什么力量。

但是我真的在这里，还是想再吹一波智谱AI。

国产之光。  

无愧于此。

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言