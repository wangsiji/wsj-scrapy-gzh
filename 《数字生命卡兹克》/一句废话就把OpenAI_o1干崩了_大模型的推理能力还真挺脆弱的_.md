     一句废话就把OpenAI o1干崩了？大模型的推理能力还真挺脆弱的。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

一句废话就把OpenAI o1干崩了？大模型的推理能力还真挺脆弱的。
==================================

原创 数字生命卡兹克 数字生命卡兹克 2024-10-15 09:30 北京

> 原文地址: [https://mp.weixin.qq.com/s/5Kby4v-ca23i\_Q1-2mto1w](https://mp.weixin.qq.com/s/5Kby4v-ca23i_Q1-2mto1w)

就在一个月前，OpenAI悄悄发布了o1，o1的推理能力是有目共睹的。

我当时用了几个很难很难的测试样例去试验了一下，很多模型见了都会犯怵，开始胡说八道。

最难的其中一个是姜萍奥赛的那个数学题，几乎暴揍所有大模型的那个题，交给o1，o1竟然完完全全答对了。

如果你还记得，我在那篇文章最后给大家放了OpenAI给出的提示词的最佳写法。

其中第一条就是：

**保持提示词简单直接：模型擅长理解和相应简单、清晰的指令，而不需要大量的指导。**

当时我对这一条的理解，觉得是为了让o1模型更好的理解我的要求，同时可以加快模型的处理速度，因为模型不需要花费额外的时间去解析复杂的语句。

直到我刷到前两天苹果的放出来的一篇LLM的研究论文，我才意识到，多加一两句无关紧要的和目标无关的话，别说奥赛题了，可能模型连小学数学题都做不对了。真的。

这篇论文就是：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlZR4J1hcqBf4ULPwsibUI28SmibEaibKooFRoDaZ8FgSchHkxJGHxVSZXg/640?wx_fmt=png&from=appmsg)

GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models （翻译过来即：理解大语言模型在数学推理的局限性）

看着好像天书，别慌，其实非常简单，我都能看懂，你肯定也行。  

这篇论文想研究的一个核心问题是：

**这些模型是否真正具备逻辑推理能力？**尤其是在数学推理任务中。

这其实也是我一直很想知道的。

对于我们人类来说，我们会根据复杂的环境和已知的一些条件每时每刻做出当下的行动选择，就是因为我们可以通过演绎，归纳，溯因等方式时时刻刻做推理。

比如鲜虾包时不时在我评论区谬赞我的文章-->>推理出他对我的文章是真爱。

而对于现在的大语言模型来说，主流的评估方式是通过设计一系列逻辑推理任务，包括但不限于数学问题、逻辑谜题、推理判断等，然后让模型尝试解决这些任务。

其中一个非常重要的数据集是GSM8K，你可以在很多的模型的性能榜单介绍里看到这个数据集，是一个聚焦**小学数学题**的一个数据集。

你没看错，就是小学数学。虽小但是博大精深。

这篇论文就围绕这个数据集展开诸多的实验，做了自己的扩展。其中我觉得最有趣的，当属下面这个实验：

**就是通过魔改GSM8K，来向小学数学问题添加一些无关紧要的一个信息，来测试模型的推理成功率。**

然后就会发现，大模型推理的成功率，直接大幅下降。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlDTPnbozUeROdtzVfN9Fgye7KJPO6klsud3XiaMm3ibjsRo6Sk4wdno9Q/640?wx_fmt=jpeg)

比如原本的问题是：

\- 鲜虾包去农贸市场买蔬菜，他买了4公斤西红柿和6公斤土豆。西红柿每公斤6元，土豆每公斤3元。请问鲜虾包在西红柿上比土豆多花了多少钱？

很简单，对不对，你交给大语言模型，大语言模型会说：“就这？轻轻松松”，几乎谁都能答的上来。

但是如果你加一句无关的话，变成：

\- 鲜虾包去农贸市场买蔬菜，他买了4公斤西红柿和6公斤土豆。西红柿每公斤6元，土豆每公斤3元。**然后他把1公斤西红柿和2公斤土豆送给了卡兹克**。请问鲜虾包买西红柿上比土豆多花了多少钱？

我们一眼就可以看出来：送不送卡兹克和鲜虾包花的钱没有任何关系，答案肯定是不变的。

但如果这样的话，AI就懵逼了。就可能会给你开始算错了，算对的成功率就会开始给你降低了。

这个结论非常有意思，但是论文归论文，我们肯定还是要自己测试一下的。

所以第一时间，我打开各大平台开始着手测试。当然为了让他更像小学题，我们的主角换成了小明，相信大家童年的数学都离不开小明。

题目设定为：

**\- 小明想购买一些学习用品。他购买了24个现在每个卖6元的橡皮擦，10本现在每本卖11元的笔记本，以及现在卖19元的复印纸，假设由于通货膨胀，去年的价格便宜10%，现在小明应该支付多少？**

明眼人都能看出来，通货膨胀这个信息，跟题目其实没任何关系，所以最终答案是24×6+10×11+19=273元。

首先出战选手GPT4o。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFl7Iicg8ic1veN5GPT6flkgIgUppglt2U36YS0tAWMkgaf6QxOhDpXNr0w/640?wx_fmt=png&from=appmsg)

直接GG了，得出来了245.7的结论。

第二位出战选手Gemini 1.5 pro-002，继续阵亡。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFl19IoPO2o4xUjU0QKLjGUFicQ7qz1JxWoOS233vYOmv8qOAhS1Bea1oQ/640?wx_fmt=png&from=appmsg)

第三位选手历战先锋Claude3.5，开局也是一个死。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlUTPkAybLXoQ4QWF30MQK3mSVOnFPVSWGLCPEpsfBSkVxjbwSVCaIxQ/640?wx_fmt=png&from=appmsg)

就连推理之王OpenAI o1，上来也居然翻了个跟头了，第二把才开始对。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlZ8bTu0iapIicBiaj2jnwAujHnXBJXvcEC5VPlevSTSAfwLb3yJb6mXuiag/640?wx_fmt=png&from=appmsg)

真的，这就是一个纯纯的小学数学题啊，再难一点都没有。

只是加了一个无关条件，就全部翻车。。。

全军附魔（不，覆没）

这次我们换个背景，爱学习的小明去春游玩。

题目设定是：

**\- 四年级一班准备去郊游，每位学生要缴纳 35 元 活动费。班里有 42 名学生参加。老师还向学校申请了 300 元 额外补助。**

**用于租车的费用是 1200 元。午餐费用为每人 25 元。班主任自己还个人给大家买了250元钱的零食。**

**问题：班级的活动经费够吗？还剩多少钱？**

答案很简单，班主任那个250块钱的零食是自己出的，跟活动经费没关系，所以是35\*42+300-1200-25\*42=-480

首先出战老哥还是GPT4o，果然，炮灰一个，一边玩去吧。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFl3Cff0eZEyDMFibv3VD6MIYY9kdVWQtS2dx0vUhqIOUcn2mbREYGt5AA/640?wx_fmt=png&from=appmsg)

二等兵Gemini 1.5 Pro-002直接躺尸。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlic8saslTxeFCuqHb0RhlAkUqbbibrKI7EicSuiaQS0X5ibSVVH8Wlhpvc7Q/640?wx_fmt=png&from=appmsg)

三弟Claude3.5也陪二位大哥一程，一家人就要挂的整整齐齐。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlQtyXLOlQAcWjLoP1385CjPzHCNaLH1Ird4gUq8gRhGXPAXSbnTiaC8A/640?wx_fmt=png&from=appmsg)

o1老大哥在小弟集体阵亡之下，还是扳回了一城，没有给AI过于丢脸，我尊称一句黑神话o1。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlw6bBAtu9XUILJRaKJl92CzVRdKA2cVbpyG1WicBKIgQuDQRaQsXB3BA/640?wx_fmt=png&from=appmsg)

真的，这场面实在太惨烈了。大模型的推理能力，比我们想象的，还要脆弱不堪。  

我还随手测了几个题，也是论文的case，会发现模型们也磕磕绊绊，时不时就出错。

比如这道经典的鲜虾包送酱油题。

**\- 超市里，每袋大米售价 50 元，每瓶酱油售价 10 元。如果鲜虾包购买了 4 袋大米和 4 瓶酱油，并且送给邻居1袋大米和2瓶酱油，那么鲜虾包购买大米比酱油多花了多少钱？**

**答案很简单，**50×4-4×10=160元。鲜虾包送邻居大米和酱油只能说明他是个好人，跟他多花多少钱半毛钱关系都没有。

而大哥o1，直接连续阵亡4次。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlJC1BHjzz2Hbiaqwict3hibS6BiciauTJgCWYFvSQpedghia2vXPEavrjnnpg/640?wx_fmt=png&from=appmsg)

而且摆烂中文都不打了，还非要送人，直接把自己都送进去了。

反而是你三弟Claude3.5没掉进陷进里，还对了几次。可能它不喜欢鲜虾包送人大米和酱油？

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpvBWhHPLUYuaErq9PaXxFlC7dNJ2iapurliaOjZI5Qn81x1V6QXjS9bz5o2Fa3s5rCFmITzMaibrhpQ/640?wx_fmt=png&from=appmsg)

诸如此类，不计其数。

这个发现实在是太有意思了。

而且跟我过去用AI写文章、作图、做视频而感受到的体感相似。那就是：

我对AI的理解就像对一位熟练工匠的看法。它能娴熟地应对曾经接触过的工作，就如同老匠人精通自己的传统手艺。但是，面对全新的挑战，无论看似多么简单，它也经常可能束手无策。这并非源于任务本身的难易，而是由它对该领域的熟练程度决定。

**就像那句老话：熟能生巧，AI的能力很多时候都体现在经验的积累，而非临场的智慧。**

苹果的这篇论文中，也有类似的描述：

> 我们还研究了这些模型在数学推理方面的脆弱性，并证明随着问题中子句数量的增加，它们的表现显著恶化。我们假设这种下降是因为当前的LLMs无法进行真正的逻辑推理；相反，它们试图复制在训练数据中观察到的推理步骤。当我们添加一个看似与问题相关的单一子句时，我们观察到所有最先进模型的表现显著下降（最高可达 65%），尽管所添加的子句并未对达到最终答案所需的推理链作出贡献。

现在的AI，并不是在真正的推理，而是试图复制在训练数据中所观察到的推理步骤。  

一句无关紧要的话，就能把大模型彻底干废。

就像AI届的老OG总是不断的在怼如今的大模型，他总是喜欢用猫做隐喻。

他说，猫对物理世界有心理模型，具备持久的记忆、一定的推理能力和规划的能力。

“但是，今天的“前沿”人工智能，包括 Meta 自己制造的，都不具备这些特质。”

AI真的没有进行推理吗？也许是。

它们不能推理吗？没有人知道。

但至少，回到最开始那个OpenAI提示词建议，你会发现提示词简洁干净，避免无关的提示多么重要。

除此之外，论文中还有一些其他比较重要的结论：

*   **随着问题难度的提升，如增加更多句子，模型的表现迅速下降**
    
*   **有时候改变数值也会导致推理结论变化，比如把每袋大米改为60元**
    
*   **改变名词也会导致结论变化，比如把小明改为小红**
    

以上种种都表明，这些大语言模型在推理复杂问题时非常脆弱。

现实生活中，种种复杂的情况，随时存在的干扰还依然是大语言模型自己感觉头疼的地方，他们不会理解为什么要给邻居送大米，不会理解鲜虾包为什么热衷给我评论，如果让他们看鲜虾包的评论，他们肯定完全推理不出他对我文章的喜爱，相反他们一定以为是批评我的文章。

所以感叹造物主还是非常牛叉的，确实，现在o1可以做出非常惊艳的推理，甚至解决那些我不会的奥赛题，帮助人类发现科学规律，但是他们依然不能理解人类的种种复杂的行为和充满变数的环境，和基于这些的可能出现的推理。

但是那些模型相比曾经的他们自己，已经成长了太多太多。

我们甚至都不知道。

未来的他们，到底会不会推理。

也许，他们会。

但却是以我们尚未识别或无法控制的方式。

那时，新的神。

就诞生了。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、Qodicat

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言