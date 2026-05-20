     分享10个我最常用的DeepResearch提示词模板和用法。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

分享10个我最常用的DeepResearch提示词模板和用法。
===============================

原创 数字生命卡兹克 数字生命卡兹克 2025-03-19 08:06 北京

> 原文地址: [https://mp.weixin.qq.com/s/WKPIFfkIAABq9UBkQtjmPg](https://mp.weixin.qq.com/s/WKPIFfkIAABq9UBkQtjmPg)

昨天写了一篇关于Gemini的文章，里面很大篇幅聊了关于DeepResearch，没想到把我非常喜欢的号小声比比都炸出来了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchumRTquWEqWX8y2Zt95iajwDNvDchaE4IqIgwPQUpibaaspUxRKvRHicGEw/640?wx_fmt=png&from=appmsg)

然后有朋友就在下面留言了：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchusM5D9AkalQZcVEXTLuaibiaFibxXVEggtEZRcee556ImvBt74iavPbNdhQ/640?wx_fmt=png&from=appmsg)

关于OpenAI的DeepResearch，我也有自己的一些使用方法和想说的，所以，不如我就来一篇，来跟大家聊聊。

这个非常牛逼的、甚至让我觉得真的值200美金一个月的功能。

DeepResearch。

我也准备用将近1w字的文章，用10个场景，和这10个场景的提示词，来给大家详细看看，他能用在哪，应该怎么用，最后一个场景，一定会给你惊喜，甚至是惊讶。

文章很长，看不完可以建议先收藏，后面慢慢看。

不过，在看这10个场景之前，我觉得还是有必要简单的快速的讲一下，OpenAI这个DeepResearch是个啥。

如果已经详细了解或者用过的朋友，直接跳过这一趴往后看就好。

  

**零. DeepResearch是啥**

DeepResearch是由OpenAI，在今年2月，推出的一个ChatGPT上的Agent功能。中文译名为深度研究。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuzDKA0f0JwZibhdwqucFuJk0ic4LKCkS5kSjAnGwfuP1Grm7V3w9X1hmw/640?wx_fmt=png&from=appmsg)

Pro会员和Plus会员可用，Pro会员一个月150次，Plus会员一个月10次。免费用户无额度。

作用很简单，深度研究你提出的问题，然后花10到30分钟时间，搜索全网数据，然后给你一篇详细且非常有深度的展示报告。

本质上，只是基于o3微调的一个端到端的Agent模型，按照规划 - 执行 - 合成的路径去完成任务，还会在过过程中，动态调整任务。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchus6wpytsnVOfAT6DuibaEoJbNicue6k1QJ5FT3JA18ehzDGcMib4bbxpMw/640?wx_fmt=png&from=appmsg)

而报告的质量，约等于一个研究员老手，干10个小时到1周生成出来的报告的质量。

他最合适的任务，就是整合多种信息来源、深入分析复杂数据、创建有据可查的报告、多步骤研究过程（涉及规划、查找、浏览、推理、分析和综合）、处理理解和推理大量信息。

这，就是DeepResearch。

接下来，我就会用10个DeepResearch的典型场景，来带大家看看，它的用法，同时，也会附上每个场景我觉得很棒的Prompt。

  

**一. 市场竞争分析  
**

**在Deep Research出现之前，很多创业者和市场分析师们要进行竞品分析往往十分痛苦。**

**需要手动搜集N家竞品公司的资料、新闻报道、用户评价等，浏览几百个网页、打开无数浏览器标签页、看无数分报告，再用自己的人脑，归纳总结整理要点。**

**借助Deep Research，你只需提出研究需求（例如：“分析中国在线教育行业主要竞品的优劣势和市场份额”），剩下的工作都交给AI代理完成。**

**它会自动搜索众多来源（官方网站、新闻、市场报告、用户评论等），聚焦你指定的领域，**在一次对话中整合信息，搞出一份连贯的分析报告。****

****创业者能快速了解行业格局，找到市场空白点；产品经理能洞察竞品功能优劣，优化自己的产品路线图；分析师则可以更高效地为报告收集数据。****

******白领们再也不用熬夜加班做竞品分析**，把省下的时间可以多睡会懒觉。****

****这里，我也整理了一个我自己觉得还不错的Promp模板，蓝字部分改成你自己的：****

    请帮我分析当前<在线教育>行业的主要竞争对手。具体要求：

比如我就可以把他改成奶茶行业的研究prompt。

报告结果前面是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuv4ialias8aFZ6cXRqKJUEmViceFicXUlCxHPnTBL7bBLibr3qowlosEXq9A/640?wx_fmt=png&from=appmsg)

10分钟，一份涵盖竞品概览、优劣势对比和战略建议的报告，就完事了。

  

**二. 学术文献综述**

**我有些做科研的小伙伴跟我说，他们在做课题时，最耗时的就是**文献综述。

要了解某个研究领域的发展，往往得阅读数十篇论文、查找各种文献综述和数据报告。

人肉检索不仅效率低，还容易漏，也许花几天时间看完文献后才发现遗漏了一篇关键论文。而且文献常常充满艰深术语，消化理解也需要耗费脑力。

现在，你只需要输入研究主题，例如“综述近5年深度学习在医学影像诊断领域的研究进展”，Deep Research会自动检索相关论文摘要、学术文章、学术博客等来源，把分散的信息整合成结构化的综述报告。

除了罗列重要研究成果和结论，最牛逼的是，还会**附上来源引用**，方便你追踪原始论文。

Prompt模板在此，****蓝字部分改成你自己的：****

    帮我调研：<近5年用于阿尔茨海默症早期诊断的机器学习方法综述>。

**Deep Research产出的报告：**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchutKqIbdX9Haz2biaOz5Ik2BbVQtDicsq85drhCxZg7kIZlw36BBhPU8EA/640?wx_fmt=png&from=appmsg)

**最后的文献参考：**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuEWS4PP2hJiao0ibPXpBINoUd2Cnia8ibia6s9EqXXXNJ5xP8gBAEQQflWJA/640?wx_fmt=png&from=appmsg)

我也挨个看了，确实有这些文献。

  

**三.股票投资研究**

如果做投资的人、或者是金融行业的人肯定知道，信息实在太多了，所以很多人才会说看长线、要去噪。

**毕竟信息太多，研究行业报告、公司财报、新闻公告、分析师研报……任何一个细节都可能影响你的投资决策。**

**以往要研究一只股票或一个行业，常常得耗费几天时间翻阅厚厚的年报、查询财务数据、收集市场消息，然后手工汇总分析。信息滞后或纰漏都可能带来损失。**

****普通白领如果想自己做投资调研**，我说实话难度真的难如登天，从纷繁复杂的信息中理清头绪，对精力和时间的要求实在太高了。**

**有了DeepResearch之后，你就可以让它调研某家公司的经营情况和投资前景，它会从财报摘要、新闻报道、行业分析等多渠道抓取信息。**

**例如，输入：“研究一下特斯拉当前的财务健康和未来增长点”，Deep Research可以自动汇总最近几个季度的关键财务指标、分析马斯克在财报电话会上的发言要点、提取华尔街分析师的观点（如X上的投资大V言论）等等，甚至还有他在政治上引起的各种方面的人的不满。**

**最终产出既包括**数据**（如营收增长率、利润率变化）又包含**定性分析**（如市场份额、竞争优势）的分析报告。**

**对于宏观经济或行业趋势，Deep Research也能整合多方预测，让你快速对世界有一个自己的了解。**

**人人都有分析师级别的情报可用，真的不再是幻想。**

**我自己最近超级加倍重仓的某个ETF，其实就是让**Deep Research分析完以后，挑出来的。****

**Prompt模板在此，****蓝字部分自己改：******

    请帮我用Deep Research完成以下任务：

******我用他分析一下阿里巴巴看看。******

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchupueuKibSbEIOO4WzKIq7bo5hq9KuEMA15MeHX7w15OhG5H1o1eE4hNA/640?wx_fmt=png&from=appmsg)

  

**四.历史事件深度考证**

作为作家、编剧、记者等等，任何需要写作的人，在写一些历史事件或人物的时候，可能都需要查阅大量史料和文章。

******以一个著名历史事件，它可能涉及多个年代的报纸报道、回忆录、学术论文等。**信息散落在不同年代和载体**，收集难度很大。而要拼出事件全貌，更需耐心梳理时间线，分辨不同来源的可信度。******

******但是如今，不论你在考证一桩悬案还是写一篇历史人物传记，只需提出你的研究问题，AI就会在茫茫互联网和数字图书馆中帮你找到线索。******

******更广泛地说，**大众对历史的认知将更加丰富准确**，因为AI可以帮我们把碎片化的史料拼接起来，避免偏听偏信单一来源。******

******虽然AI的幻觉虽然还是会存在，最后得到历史资料真伪也需要人来甄别一下，但Deep Research已经大幅提高了信息获取效率。******

******正如有人所说，**AI让时光之门向更多人敞开**，以前只有专业历史学家才能触及的资料，如今大众也能一探究竟。******

******Prompt模板在此：******

    我要深度研究<你想研究的>这一历史事件。请帮我：

比如我想研究一下大卫与歌利亚的故事。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchu8IamIZctzzEicA3zc1bhHiaUoA1NZ7JZ1eZjYwbomLTUnicSf5mW89Zqw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuWPmK8iaZuR58L1rQlkbod21QeJR9A91n2s6J0bGCHAv85ibHkFNURsYg/640?wx_fmt=png&from=appmsg)

你会发现，歌利亚的故事好像不只是圣经里面的神话，可能还真的是在历史上，真实发生过的，只不过，经历了很多轮的润色。

  

**五.事实核查和谣言粉碎**

坦率的讲，在这个信息爆炸的时代，各种传闻和“标题党”层出不穷。

对于媒体、科普作者或者很多希望求真的人来说，事实核查是一项重要却艰巨的任务。要证实或驳斥一个说法，往往需要翻阅大量资料、找权威来源支持，有时候还得亲自做实验或者请教专家。

现在，事实核查变得前所未有的高效。给******Deep Research一个待验证的声明，它可以******同时搜索支持和反对的证据，然后把它们呈现给你。

比如，你问：“长期使用微波炉加热食物对健康有害</span>是真的吗？”。

Deep Research会检索科学文献、食品安全机构的公告、科普文章等。一方面也许找到了世卫组织或FDA的声明说明微波炉辐射安全，另一方面可能引用一些小型研究或谣言的来源，然后给出综合判断：大概率告诉你“无可靠证据证明微波炉加热致癌”之类的结论，并附上关键来源。

这样，你不仅知道答案，还能看到背后的证据链条。

如果是比较严肃的调查，如新闻事实核查，它也能帮助列出时间、地点、人物证据，让你快速还原事实经过。

这项用法对于记者、科普作者、内容审核人员等等来说意义重大。

Prompt模板：

    我要核查一个说法：

如果我把问题改成：喝咖啡是否会导致骨质疏松，这个报告是这样的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchu5uQqfZreHrwwvbZiaoXOqWGe0z6yhznMmyCE2JvMat24IH7kLsR4gxw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuvHf11MFiaWHibstqQWOkqaG3GUPb5LAvO2N5KB1OKLqarmxZsoUTr11A/640?wx_fmt=png&from=appmsg)

**如果我们人人都能用事实说话，那该多好啊。**

**六.个人学习路线规划**

**我们想学习一门新技能或知识时，往往面临信息过载的困境。**

**拿学习Python编程举例，网上教程铺天盖地，有免费视频课程、博客文章、书籍推荐……**到底从何学起**让人犯难。**

**如果随便跟着感觉走，可能学了些皮毛就卡住，或者资料不系统导致知识漏洞。**

**为自己量身定制一个系统的学习计划并非易事，需要了解该领域有哪些必备基础、经典教材和练习路径，初学者通常很难搞定。**

**但是对于******Deep Research，它会综合互联网上无数学习资源和过来人的经验，给出**循序渐进**的建议。********

********例如：“我是一名市场营销人员，想用6个月时间自学数据分析，帮我规划学习路径。”******** 

********Deep Research可能会建议：第1个月学习Excel和基础统计，第2-3个月学习Python数据分析库（pandas等），第4个月实践几个小项目，第5-6个月进阶学机器学习基础，并推荐每阶段合适的课程或书籍名称。********

********有些热心网友曾整理过类似的学习路线博客，AI会参考这些再结合你的背景做调整。结果就是一份**高度个性化**的学习计划，让你少走弯路。********

********未来也许会出现“AI学习教练”这样的新角色，而Deep Research就是我认为的雏形。********

********Promp模板在此（这个得根据你具体情况去大改了，我只提供一个思路）：********

    背景：我是一名<视觉传达设计>应届毕业生，想转行做软件开发，但没有编程基础。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuYsiaiaoKBmWRG3cY6vRg5FeTD5HPpibDaZsGqwZob6N8SbQ7zzepmggpQ/640?wx_fmt=png&from=appmsg)

未来，不知道怎么开始学，真的不可能会再是借口了。

  

**七.**社交舆情与用户情绪分析****

**在市场里，品牌公关、市场营销人员需要时刻关注自己公司或产品在公众中的口碑。**

**传统上，大家都会用舆情监测工具抓取社交媒体和新闻，但**定性分析很多时候仍然要人工或者用部分AI去辅助完成。

比如一款新产品发布后，有成千上万的用户评价，要总结主要褒贬点并非易事。即使是热点事件中的民意走向，也需要看大量微博、论坛帖才能感受大家情绪。

手工完成这些工作费时费力，而且容易主观偏差。

而用Deep Research，你可以直接一句话：

“最近网上对我们XX产品的评价如何？”，它会搜索社交媒体帖子、产品测评、相关新闻评论，从中提炼常见观点和情绪倾向。

公关团队可以更快速地了解舆论脉搏，及时调整策略；营销人员能够发现用户真实的痛点和喜好，用于改进产品或制定宣传方案。

**可以让每个用户的声音都不会被淹没，真正做到“以用户为中心”决策**，而不只是凭感觉拍脑袋。

模板Prompt：

    帮我详细分析<某某事件>的用户舆论：

比如，我让它分析一下OpenAI发布GPT4.5之后的舆情。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuYl8jb8h4YjRhaCptjiamrzzLpQ5WEnMHeSsGyzjQxeul0p0HbdPZ9Ug/640?wx_fmt=png&from=appmsg)

真的非常的准。

  

**八.**产品对比****

****我不知道你们，但是我自己有选择困难症。****

****想买部手机，要比较不同型号的参数、评价；选一款主机电脑，更要看各家功能差异、价格、用户反馈。****

****过去，我们往往需要打开二十几个浏览器标签页或者刷几个小时的小红书，看测评文章、用户评论贴，再自己做笔记对比。****

****信息散落各处且观点纷杂，折腾几小时后脖子都要断了才做出决策，终于下定决心点了付款，反手又在小红书上刷到它的避雷贴。。。****

****而Deep Research除了正常的检索各大科技媒体评测、用户测评视频总结、论坛口碑等信息之外，还会跟根据你的信息量身定制。****

****比如你特别在意相机效果，它会重点对比相机评分；你关心价格，它会算每款的性价比。****

****真的还是很有用的。****

****Prompt模板：****

    帮我比较两款产品：

****比如我就对比一下Macbook Air和小米笔记本吧。****

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuOllaIvycLCEckials5M7XYJBUS7SCHhfMptz6mn2awNt2NvO90Sn0XQ/640?wx_fmt=png&from=appmsg)

****最有意思的是，****Deep Research居然抓到了关于国补的信息，这个就非常的强了。********

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuPdic5Kl7PlakLRfz9SoeAf4JJLjyBCU8n1axRzAnl9XjOR6y4xqibmww/640?wx_fmt=png&from=appmsg)

  

**九.**新闻整合****

****现在，每天都有海量新闻涌现，忙碌的白领很难全部跟上。****

****特别是当你需要了解**某个热点事件或行业动态的全貌时，更是困难。比如就单“AI影视”的话题，相关新闻散见于科技、财经、甚至娱乐板块，要获取全面视角，你可能得读几十篇报道、翻微博热搜、看行业评论，非常耗时。**

**而即便投入时间，也容易陷入信息过载，不知道哪些是可靠信息，哪些只是噪音。**

**而Deep Research堪称一位**超级编辑。它可以在互联网上快速爬取与某个主题相关的新闻、博客、社交媒体讨论，**过滤重复内容，提炼关键信息**，并最终形成一份纵览全局的总结报告。

甚至对热点事件（如某企业收购案、某大型事故），它还能能整理出**时间线**，列出事件的来龙去脉和关键节点。

Prompt模板：

    帮我汇总“全球AI行业最新动态”

报告非常有意思：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchufqqOBZMVSl5KfVCz20vBdz8oHJmSjCJicKwbqCfX4qjqynG35MnQqNQ/640?wx_fmt=png&from=appmsg)

在产品发布上，抓到了大量的国产AI产品动态。

甚至，在国内可以说是AI短剧里程碑的《心安岭诡事》，也被抓出来了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchugEkGVWQjgfXib8xqsgU1sjpiaEqYOWgWePb6CuwSvRmqjPiaqEXckpHjQ/640?wx_fmt=png&from=appmsg)

这真的是里程碑，因为标志着，AI短剧首次实现了盈利，虽然挣得不多，但是也代表，商业模式跑通了，这是短剧行业开天辟地的大事。

但是我相信，可能很多AI行业的人，完全都不知道这部剧。

Deep Research，已经比绝大多数从业者，在知识的广度上，要全面了。

  

****十.写小说****

****可能我是为数不多的，在用Deep Research写小说的人。****

越好看的故事，要求越强，逻辑要求越高。特别在影视剧本中，有一个非常经典的理论，叫做契科夫之枪。

大概意思就是，故事提及的每一个元素都应在后文出场，不然就没有必要提及：

“请将一切与故事无关的事物都从故事中移除。如果你说第一幕中有把枪挂在墙上，那么在第二幕或者第三幕中这把枪必须发射，不然就没必要挂在那。”

AI写故事也一样，写故事不是随机漫步，而是逻辑和创意共同碰撞出的灵光乍现。

而****Deep Research的底座o3，在逻辑推理上，真的强到没边。****

****也是为数不多的，能一次性生成几万字的逻辑耦合的小说。****

****我给大家看一下我的流，这个地方其实不太能做模板，因为过于个性化。****

****我写小说分为两步，第一步：找资料、写关键情节点，第二步，写完整的小说。****

****第一步我的Prompt如下：****

    我正在构思一部架空历史奇幻小说，背景类似于15-16世纪的欧洲文艺复兴时期，但我想加入一点炼金术与魔法元素。请你使用Deep Research，帮我完成以下任务：

最后产出的这一些参考和报告，实在是太牛逼了，实在太长了，我就不放全了，放一部分给大家看看。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchu94MzCMPPDibdO9Bic2AZMHxRR0biaGnXFyib6WkWWxDPJ1XLpXuicqBoLfQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuPYGvNevRIiakEduiadrTljhrFUHvMFd4hOokDS5D3IQ7FbHytGerybmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuPX39gWhAhibbtQh8kMwWgo1oFOtnwYQS3euMRqXWf0rkQ3CAEeOxViag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchupuZagVUia83Lo08fgck0Gy7ZYEU8eiajGTNrRNibB9SzbnibRYo0lBYJmw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuNCnJAqnDx2fuDHrzaNIib3mTXm5IWiaXCnGTlXjZAicoruO9woIyJ5Tqg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchu5bSvlqRxu5r6ibI7Y3vnlboka1aH9KK6y5M2NTVka9PRQzscwuKWN8w/640?wx_fmt=png&from=appmsg)

即使是一个短片故事，它也应该有大量的世界观和历史研究，把自己落在那个时代里，化成一片尘埃，去亲眼看那个世界的一切，这才是，一段故事的基础。

这才是，逻辑和事实，你的故事，才足够的鲜活。

当我有了这些素材之后，我就可以再跟****Deep Research说，根据上面的报告信息，帮我写出这篇3w字的短篇小说，就参考钢之炼金术师的风格吧，可以再融入一点点克苏鲁的那种不可名状的恐惧，作为故事的暗线。****

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuhUbia0a6qdtutchCLMGLiba2tg8icn3KFjzlUs5036aVZB0Km2BeedWjw/640?wx_fmt=png&from=appmsg)

**在整整32分钟后，这一部6章的短篇小说，终于完成了。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpx549lYQqsU1DDL3iamSchuuDX7os0grO82A53po4pmnCiaq5iajbsJfGk2H27jxaWcGFZAKTBmwicpQ/640?wx_fmt=png&from=appmsg)

**我不知道该用什么言语来形容这篇小说。**

**这可是一篇，3w字的小说。**

**我对于文字内容，特别是AI生成的内容，是极度挑剔了，几乎没有能让我明知是AI，但是我还读的下去的小说。**

**但是，****Deep Research写的，每次我都能读下来，而且是那种，牵引着我往下走的那种读下去，是我真的能感受到城市呼吸，感受到人物的性格，人物的挣扎，人物的成长孤光，还有那种时代之下，在教会这种庞然大物之下，小人物的绝望和挣扎。******

******前面的伏笔，在几章之后还能用上，原来是这样！原来前面出现的元素有这么大的用处！原来就是他！这是我在一边读的时候，一边发生的感叹。******

******这是优秀的故事，这是完美的故事，这是精心编排设计的故事，我实在实在实在太喜欢了。******

完整的全篇，因为实在太长，我放在飞书文档里了，如果有想看小说的朋友，可以移步过去观看。

https://datakhazix.feishu.cn/wiki/Tsl1wGzr0iKSYJkh4y9c4MWQnvV?from=from\_copylink

真的太好看了。

**写在最后**

这篇文章，即使在我已经用了很久，对****Deep Research比较熟悉的情况下去写，依然感觉，只能展示****Deep Research的冰山一角。********

****可能还有更多的、更有趣的玩法，埋藏在深处，在我也还没有发掘的地域上。****

****我越来越觉得，牛逼的AI就像一片大海。****

****我拼尽全力，也只能管中窥豹。****

****当你了解的越多，你只会觉得越来越感慨，为什么自己懂得这么少。****

****自己穷尽一生，可能也再也追不上AI进化的步伐了。****

****人之于天地，不过如蜉蝣一般渺小，观天色乍明乍暗，便已是朝生暮死。****

既生在这个时代，那又怎么办呢。

拼命奔跑、拼命学习吧。

在这个尽量不被时代所淘汰的道路上。

完。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言