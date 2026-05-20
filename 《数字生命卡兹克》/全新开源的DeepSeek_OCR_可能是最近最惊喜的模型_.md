     全新开源的DeepSeek-OCR，可能是最近最惊喜的模型。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

全新开源的DeepSeek-OCR，可能是最近最惊喜的模型。
==============================

原创 数字生命卡兹克 数字生命卡兹克 2025-10-21 09:30 北京

> 原文地址: [https://mp.weixin.qq.com/s/QjRW9yZylSmPSO1LEg\_UFA](https://mp.weixin.qq.com/s/QjRW9yZylSmPSO1LEg_UFA)

AI圈虽然天天卷，但是很多的模型，真的越来越无聊了。

每天就是跑分又多了几个点。

直到昨天，DeepSeek久违的发了一个新模型。

DeepSeek-OCR。

这玩意，是真的有点酷。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo7cRcgyiazZCwYlOjYEgfl7qxT5xsbLM9Bic8CP2MyVkR6uSLeH1t1icHkDPx8t8nXibUIuElemLQ5pw/640?wx_fmt=png&from=appmsg)

首先，不要被这个名字骗了。

虽然说它名字上有个OCR，但是你说它真的就只是个OCR模型吗。

我想说，是，也不是。。。

说它是，很简单，就是因为这玩意，干的确实也是传统OCR的活。

传统的OCR任务其实特别纯粹，就是把那些图片上字啥的啊，变成你电脑里可以**编辑**可以**复制粘贴**数字文本。

以前没有OCR的时候，你想想，你看到手上的书上有些字特别好，你想录到电脑里，你会咋办？答案就只有一个，一个字一个字的敲上去。

敲几句话还行，让你敲个合同或者一本三体你试试看，是个人都绝逼要疯。

后来OCR来了，就特别方便了，直接拍个照片，就能把里面的文字全部提取出来，很简单。

所以DeepSeek-OCR确实也有OCR的功能，也能干OCR的活，而且还挺强。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo7cRcgyiazZCwYlOjYEgfl7o4BKWIYlDwtNZcRHNwJv3bsUBISB6JvOSMhicX09J9tsAPFrth6DGRA/640?wx_fmt=png&from=appmsg)

比如这是一张典型的金融研究报告。，里面有文字，有图表，有各种复杂的排版。

你让一个传统的OCR软件去看这张图，它可能会非常精准地，把里面所有的文字，都抠出来，变成一个TXT文档。

然后就没有然后了。

但是DeepSeek-OCR，它看完这张图，会直接，生成一个Markdown文档。

在这个文档里，文字是文字，标题是标题，最关键的是，那些图表，被它用代码，也重新画了一遍，变成了一个可以被编辑被引用的表格。

这个很牛逼了。

但是吧，这玩意又不只是我们传统意义上理解的OCR。

他还有一个很重要的功能，就是，压缩。

可能会有点难以理解和抽象，我尽可能的用通俗易懂的话来讲明白。

在说压缩之前，我们得先搞明白，现在所有大语言模型，从GPT-3.5到我们现在的各种模型，都面临着一个共同的几乎无解的噩梦，就是长文本处理。

你别看它们现在能写一堆乱七八糟的能当朋友跟你聊天还能用嘴画图，但你只要丢给它一篇稍微长点的内容，比如一本几十万字的书，让它去理解，去总结，基本上都要炸。

因为AI理解文字的方式，跟我们不一样。

我们看书，是一目十行。

AI读文字，它需要把每个字，每个词，都转换成Token。你可以把它简单的理解成一个一个的“字节”，是数据里面的那个字节，不是字节跳动的字节。

现在主流AI架构的缺陷是，它在读每一个新词的时候，为了理解上下文，它需要把这个新词和前面所有出现过的词，都建立一次联系。  

所以处理这些Token的计算量，是随着文本长度的平方增加的。

比如我举一个Party的例子，现在这个Party上有10个人，每个人都跟其他人贴贴一下，那大概需要45次贴贴，还行对吧。

但如果来了100个人，每个人都要跟其他人贴贴，就需要将近5000次贴贴，这基本就属于废了。

这就是技术上常说的计算复杂度是N的平方。

这个成本，是指数级增长的，谁都扛不住。

所以，长久以来，整个AI界都在死磕一个问题，怎么让AI，能又快又便宜的搞定上下文的问题？

大家想了很多办法，什么滑动窗口、稀疏注意力，各种各样的算法优化。但这些，都像是给一辆漏油的破车，换更好的轮胎，贴更骚的膜。

但是它，解决不了发动机的根本问题啊。

然后DeepSeek这次，它根本没管你那个漏油的破逼车，而是，直接给你买了一辆，新能源。

它说：“我们为什么，非要让AI一个字一个字地读呢？我们能不能让它，像我们人一样，看？”

就是我不再把一本300页的书，转换成几十万个Token的文本文件，喂给AI。

而是，我直接把这300页书，拍成一张张照片，变成一个图像文件，然后，让AI去看这张图。

你可能觉得，这不是脱裤子放屁吗？照片不也是由像素组成的吗？信息量不是更大了吗？

对，但你忽略了最关键的一点：

**图像，是二维的，而文字，是一维的。**

一维的文字，就像一根无限长的薯条，你想吃它，智能从头吃到尾，一个字节都不能少。

而二维的图像，就像一张大饼，你一眼扫过去，整个饼的全貌，尽收眼底。

DeepSeek-OCR，干的就是这事，把所有的文字，全部压缩成图像。

这个过程，在他们的论文里，叫“上下文光学压缩”（Contexts Optical Compression）。

我给你举一个**真正的应用场景案例**，你就全明白了：

比如假设你正在跟一个AI助手聊天，你俩已经聊了三天三夜，聊了 1000 轮，可能占几十万甚至几百万的Token。

对于以前的大模型来说，当你问：“哎，我三天前跟你说的第一件事是啥？”，大模型就必须把这1000轮的全部聊天记录都装进它的记忆区也就是上下文窗口里，才能去查找。

这会撑爆它的内存和算力，所以现在的AI，很多的聊着聊着你就感觉它失忆，因为有的，真的只能记住最近的几十轮对话。

**而DeepSeek-OCR的解决方案呢，是这样的。**

**AI助手只把**最近10轮**的聊天记录，用`文本`的形式记在脑子里。**

**但是，它把那更远一点的990轮的`文本`聊天记录，**自动渲染成一张或着几张长长的图片，**就像你给聊天记录截了个屏。**

**然后，它立刻调用内部的**DeepEncoder编码器**，把这张包含海量文字的截图，压缩成大概只有原来10分之1的视觉Token，然后一起扔到上下文中，记到脑子里。**

**当真正要用的时候，比如你还是问那个问题，“我三天前说的第一件事是啥？”**

**它现在的上下文里装的是**10轮聊天记录的文本token `+ 990轮聊天记录的``视觉token`**。**

**然后，它的解码器，DeepSeek-3B，一个激活参数为570M的MOE模型，已经通过 OCR 任务，学会了一看到这种`视觉token，就能把``它``解码还原成`原文的能力。**

**于是，他看了一眼那一圈视觉Token，找到了三天前的第一句话，然后回答了你。**

**这，就是DeepSeek-OCR的整个架构。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo7cRcgyiazZCwYlOjYEgfl7lDtdvmdibpgwFTKCZHXXVFPwH6yhQNCDUlfaeGAkfQHu4E15OI43tSQ/640?wx_fmt=png&from=appmsg)

**所以啊，别被名字骗了，这真的不止是个OCR啊。。。**

**这是纯粹的关于上下文的新范式。。。**

**所以虽然跟百度的那个PalddeleOCR-VL一样名字也有OCR，但其实，两个，真的不是一个东西= =**

**DeepSeek-OCR，这，即是压缩。**

论文里给出的数据是，在保持96.5%的识别准确率的前提下，压缩比可以达到惊人的**10倍**。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo7cRcgyiazZCwYlOjYEgfl74OoMZteKPtJgvQ2lgkucsMf1nB2GD4flibh92ticpkWT2zC43jXspfFg/640?wx_fmt=png&from=appmsg)

压缩比 = 原来的文本token总数 ÷ 压缩后视觉token总数。

而20倍的压缩比，还能保留60%的准确率，虽然这个准确率确实不咋地，但是，这也是给未来留下了非常值得优化的方向。

说实话，这个东西确实很新，真的很有意思，可能是我为数不多的最近看到的最好玩的模型论文。

一图胜千言，可能说的就是如此吧。

而且细细想来，其实这种压缩之法，也确实没啥毛病。

我们总觉得文字是信息传递的巅峰。

但从整个人类历史和生物进化的角度看，**视觉，才是我们一直处理信息的最重要的手段。**

在文字诞生之前的几十万年里，我们的祖先就是靠看来生存的。

看天色，看猎物，看同伴的表情，看亲手刻下的壁画。

在纸张和印刷术普及之前，人类是怎么记录宏大叙事的？是壁画，是浮雕。

埃及金字塔里的象形文字，敦煌莫高窟里的经变画，它们本身就是一种压缩。古埃及人把复杂的祭祀、律法、历史，压缩在一幅幅画里，等待别人去解压。

从这个角度看，DeepSeek-OCR干的事，和当年的人类，其实也没什么两样。

但是当我觉得，最头皮发麻为之一振的话。

其实是论文的最后，他们写的一点点希望讨论的。

DeepSeek说，对于那些更古老的上下文，我们可以**逐步缩小渲染出的图像，以进一步减少令牌消耗**。

**这个假设的灵感，来自于一个非常自然且深刻的类比：**

**人类的记忆会随着时间的推移而衰退，****人类的视觉感知会随着空间距离的拉远而退化。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo7cRcgyiazZCwYlOjYEgfl7sAaXc02oRvQcbp4m6eqxjbjuNribN7zVaGDbdTcl1ibuROT2X0jwcdRA/640?wx_fmt=png&from=appmsg)

**这种现象，它们都表现出了相似的、渐进式的信息丢失模式。**

**他们可以用“上下文光学压缩”的方法，**实现了一种记忆衰减形式。****

****比如图表里，最左是 Text token，也就是不压缩的纯文本，信息保真；往右是把文字渲成图再编码成视觉 token 的不同模式，Gundam 比较豪华、细节多、花销大，Large 再次之，Base、Small、Tiny 依次更省 token、也更模糊。  
****

****它几乎，完美地镜像了生物的遗忘曲线**。**

**在这个机制下，最近的信息保持着高保真度，而遥远的记忆则通过不断提高的压缩率，自然地褪色和淡忘。**

**这个机制，实在是太酷了。**

很像是在探讨，一种“数字生命”的可能形态。

我们一直以来追求的AI，是什么样的？

是一个拥有无限记忆、绝对理性的“神”。

它不会遗忘，不会犯错，像一台完美的机器。

但我们自己是这样的吗？

不是。

遗忘，恰恰是人类智慧最重要的组成部分。

我们之所以能够创新，能够抓住重点，能够在复杂的世界里做出决断，正是因为我们的大脑懂得，放下。

我们会忘记那些不重要的细节，我们会模糊那些久远的伤痛，我们会把宝贵的认知资源，留给当下最重要的事情。

遗忘，还有错误，真的不是bug，是我们这个物种能够延续至今的核心算法之一。

**就像西部世界里的那句经典台词。**

**在福特的理论中，**进化形成了这个星球上有情感和知觉的生命体，“用的唯一工具，就是错误。”****

****![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo7cRcgyiazZCwYlOjYEgfl7quPO5Sia58OTdv35O1yokgbIYaSSl0nNwZxGyOwPeNpNpkp86vo0IXQ/640?wx_fmt=jpeg&from=appmsg)****

****遗忘，也是那个“错误”。****

****对DeepSeek-OCR感兴趣的，可以去他们的项目网址看一看，体验一下。****

https://github.com/deepseek-ai/DeepSeek-OCR

但是，我也非常强烈的建议，大家也可以，去读一读这篇论文的原文。

不需要看那些很技术的原理和数学，只要看方法，还有范式，其实就能学到很多东西。

我把论文原文也放在公众号后台了，你对着后台私信“OCR”，也会自动的发给你。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo7cRcgyiazZCwYlOjYEgfl7IFv4QOQ3zwTnheXVLQCW6hcIGDbVdCy03u5YcI0SdrfJpMialIzpdAw/640?wx_fmt=png&from=appmsg)

感谢DeepSeek。

惟愿我们。

国运昌隆。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言