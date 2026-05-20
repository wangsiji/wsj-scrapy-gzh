     Google又发布了一篇可能改变AI未来的论文，这次它教AI拥有了记忆。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

Google又发布了一篇可能改变AI未来的论文，这次它教AI拥有了记忆。
====================================

原创 数字生命卡兹克 数字生命卡兹克 2025-11-25 09:18 北京

> 原文地址: [https://mp.weixin.qq.com/s/h81ycKFhxcO17r0t1-zghQ](https://mp.weixin.qq.com/s/h81ycKFhxcO17r0t1-zghQ)

前两天，Google发了一个非常有趣的论文： 

《Nested Learning: The Illusion of Deep Learning Architectures》

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6tebcibLwAsOFCTq5cxqqwd8htdXCIhvNhI4Exh7mibK95MVrkLRSh332Zg/640?wx_fmt=png&from=appmsg)

非常有意思，很多人戏称，这篇论文，是《Attention is all you need (V2)》。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6tefNu9hzhMTamoQOYhZg5ehZCVgCdicYp3phxSQuG4HMHJJPqicMCbTdgw/640?wx_fmt=png&from=appmsg)

《Attention is all you need》，神中神。

这篇论文提出的Transformer架构，现在是几乎所有大模型的底层，比如GPT、Gemini、Claude、Qwen、DeepSeek等等等等。

2017 年的论文，到了 2025 年，引用次数已经 17 万+，进入 21 世纪被引用最多的论文前十名，被正式称为现代 AI 的奠基工作之一。

而现在，所谓的《Attention is all you need (V2)》虽然是个纯粹的戏称，但是也能看出来，如今的大模型发展到了个瓶颈，也急需一种新方法突破的阶段了。

所以，《Nested Learning: The Illusion of Deep Learning Architectures》应运而生。

有趣的是，2017年的来自于《Attention is all you need》来自于Google Research，这次，依然是Google Research。

遥相呼应了属于是。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6teqvibDbR0KUtNZ1VNQlpPXFTpGomca04T2pH1nTTOsBDJl1tDLOz7IIQ/640?wx_fmt=png&from=appmsg)

在我花了一些时间读完这篇论文后。

我觉得我还是学到了非常多的东西，有一种我之前看DeepSeek-OCR那篇论文的美感。

我尽可能的用大白话，来聊聊这篇论文到底说了个啥，以及它为啥可能这么牛逼。

话不多说，直接开始。

要理解这篇论文的牛逼之处，我们得先理解现在的大模型有个非常致命的缺陷。

这个缺陷，就是：

失忆。

更准确地说，是：

顺行性遗忘症。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6te3Nib8Ifkp7XsafRMgA8u9ynJnicRRiblr8nTcDPZLrBL1Of83nvO8eLTQ/640?wx_fmt=png&from=appmsg)

我们常说，人脑这东西，最厉害的一点，从来不是计算的多又快，有多省功耗，而是能记多久，又能多聪明。

你肯定见过那种经典的神经科普。

比如告诉你，大脑有短期记忆、长期记忆，短期记忆大概能同时存 7±2 个东西，然后很容易忘掉，长期记忆存得久，但写入很慢，要反复出现、要睡觉巩固、要和别的东西勾连，你才能记很久很久很久。

然后呢，现在的神经科学也会提到一个观点，就是说：

记忆是分阶段巩固的，有在线的那一段，也有离线的那一段。

大概就是你白天学的东西，会先在海马体里写个草稿，晚上睡觉的时候，大脑会在各种脑波里反复replay，慢慢把重要的东西刻进皮层，变成真正的长期记忆。

所以啊，睡眠不好，会让你的记忆力越来越差，不是没有根据的，我现在就能明显的感觉到，记忆力越来越差了。。。

但是啊，如果你的这里出问题，就会出现我们在上文说的那个很典型的病。

顺行性遗忘症。

这类病人以前的记忆都在，但从某个时间点以后，新东西统统写不进长期记忆。

他们的世界只有“很久很久以前”和“刚刚这几分钟”，剩下的时间一片空白，每一天都像被困在刚刚发生的循环里。

不知道大家有没有看过诺兰的一个很经典的电影《记忆碎片》。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6teg2PM9aJIBZSBleYdnw5FaCPmZOAhNGYbL9wucLiabQQQIcYyFMvibpdw/640?wx_fmt=png&from=appmsg)

主角只能记住几分钟内发生的事，一旦超过这个时间，记忆就清零了，只能靠身上的纹身和纸条来提醒自己。

他知道自己是谁，知道自己过去的一切，但他无法形成新的、长久的记忆。

现在所有的大模型，GPT-5.1也好，Gemini 3 pro也好，再牛逼的模型，现在本质上都是《记忆碎片》的主角。

它们那个庞大的、包含了半个互联网知识的模型参数，就是主角过去的人生记忆，也是他的长期记忆。

而我们跟它聊天时的那个上下文窗口，就是他那几分钟的短期记忆。

你在一个对话里教它一个新知识，它能记住，还能举一反三。

但只要你关掉对话框，重新开一个，再问它，它就一脸无辜地看着你：“咱俩之前聊过这个吗？”

这里咱们不聊ChatGPT和Gemini里面那种记忆的能力，那个本质上是RAG，不能算从模型层面，真的记住了那些你说过的知识。

所以，我们其实可以看到，大模型的知识，被永远冻结在了预训练结束的那一刻。

从那以后，它就失去了形成新长期记忆的能力。

每一次对话都是一场绚烂的烟火，美则美矣，但消散后，什么都不会留下。

所以，这也意味着，现在你能用到的

AI，也永远无法真正地成长。

它无法从与你的互动中真正地了解你，也无法从解决了一个新问题后把经验固化下来。

所以，其实我们每次跟AI开启一个新的对话，都是在和一个全新的、只有出厂设置的AI打交道。

这里还是再强调一下，我说的一直都是模型层面，不是ChatGPT上面的那种记忆功能，那是工程层面，跟模型本身没啥关系。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6tengvOWg4DxGb0icJesrzz1YQJexIr5ThhlhSia1K2QdtAgtwdPAZuhMow/640?wx_fmt=png&from=appmsg)

讲到这里，我相信大家，都已经理解了，在现在的AI架构之下，这个致命的弊端。

就是，顺行性遗忘。

所以，这篇《Nested Learning》（嵌套学习，简称NL）的论文，就是冲着这个根本问题来的。

他们关注到了人脑里，一个特别有意思的现象，就是脑电波。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6teIYOJQbNTHIqR8WzuUlibP4YCSkDredibS2EBcYZHnbNEgjUJfpD3oJ5A/640?wx_fmt=png&from=appmsg)

我们的大脑里，其实是有各种不同频率的脑电波，他们各自骑着不同的作用。

比如睡觉时的Delta波（0.5-4Hz），放松时的Alpha波（8-12Hz），专注时的Beta波（12-30Hz）等等。

这些不同程度的脑电波，其实都代表着不同的神经元在处理一些不同的任务。

比如有些神经元在飞速地处理眼前的信息，像电脑的GPU一样，这是高频活动。

有些则在慢悠悠地整理、归纳、存储信息，把短期记忆变成长期记忆，这是低频活动。

所以，我们的大脑，其实一直是一个非常复杂的多频率多层次协同工作的系统。

我用开车这事来举个例子，比如你正在学开车。

你的最高频系统，是你的手脚肌肉记忆。

方向盘往左打多少，油门踩多深，这个反应得非常快，几乎是毫秒级的。这是最表层的、最快的学习。

你的中频系统，是你的战术决策。

比如“前面红灯了，我该踩刹车了”、“旁边有车要并线，我得让一下”。这个决策过程比肌肉反应要慢，可能是秒级的，你需要一点点时间来处理路况信息，这是中频。

你的低频系统，是你的战略规划。

比如“我今天要去A地，导航显示这条路堵车，我应该换一条路走”。

这个学习和决策过程就更慢了，你可能在出发前就想好了，路上还会根据情况调整，这是低频。

你的最低频系统，是你的核心驾驶理念和能力。

通过几个月的练习，你从一个新手变成了老司机。

这个学会开车的过程，彻底改变了你大脑中关于驾驶的神经连接，而这个变化是非常缓慢的，是以天、周、月为单位的，用AI的话说，就是，你的驾驶模型被重塑了。

从这个学会开车这么一个小事上来说，你应该能发现，

我们人类的学习，天然就是嵌套式的，也是分层次分频率的。

我们不会用思考人生哲学的脑回路去控制踩刹车的肌肉，也不会用肌肉记忆去规划一次长途旅行。

现在的以Transformer为首的大模型架构，问题就出在这。它虽然有很多层，但本质上，它是个单频系统。

在训练的时候，所有参数的更新节奏基本是一致的，训练结束后，整个系统就被锁死，所有频率都归零了。

他再也没有办法学习了。

而再《Nested Learning》这套框架下，论文又提出了一个新的模型模块 ，HOPE，名字非常好听，叫希望。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6temTEwdKdPwBeC4vzpVDczHdJ2HNjw0Fp0DUjbqfLdY22MnTQ5J2j0Lg/640?wx_fmt=png&from=appmsg)

HOPE里面，混了两个东西，一部分是会自我修改权重的序列模型，一部分是多时间尺度的连续记忆带（Continuum Memory System）。

从而，让HOPE，拥有了带自我更新机制的记忆单元。

它要把一个AI模型，明确地拆分成不同更新频率的层级。

再这套框架下，AI在跟你对话的时候：

它的高频层，在飞速处理你说的每个词，理解你的意图，生成回复，这部分记忆是临时的，对话结束可能就忘了。

它的中频层则在以一个稍慢的速度，分析你这整个对话的主题、你的情绪、你的知识盲区，试图形成一个关于这次互动的概要记忆。

它的低频层则更慢，它在整合过去一段时间里，跟你的所有互动。它可能会发现：“哦，这个用户最近总是在问关于古典音乐的问题，而且他似乎对巴赫特别感兴趣。我应该把‘该用户是古典音乐爱好者’这个标签存入关于他的长期档案里。”

这个过程，就非常非常像人脑的记忆巩固机制了。

我们白天经历了很多事，这些都是碎片化的短期记忆，储存在我们大脑的海马体里。

到了晚上睡觉的时候，大脑会像放电影一样回放这些记忆片段（再论文里叫offline consolidation），把重要的信息筛选出来，然后写入到大脑皮层，成为稳定的长期记忆。

嵌套学习，就是给了AI一个睡觉和反思的能力。

可以让AI，成为一个可以日积月累、不断沉淀的学习者。

讲到这里，你可能立刻会有一个疑问。

就是这个ChatGPT的记忆。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6tengvOWg4DxGb0icJesrzz1YQJexIr5ThhlhSia1K2QdtAgtwdPAZuhMow/640?wx_fmt=png&from=appmsg)

你可能会说：“等等，现在的大模型不是已经有记忆了吗？我告诉它我是一个素食主义者，它就能记住，下次会给我推荐素食餐厅。这不就是你说的那个低频层在起作用吗？”

但这个地方，我想说，这其实是个随身带个笔记本和记在了脑子里的根本区别。

你看到的ChatGPT的记忆功能，本质上就是一个笔记本，当你告诉它一个信息，比如“我是个大呆逼”，它并没有真正把这个信息学进它那个巨大的神经网络大脑里去。

它的核心模型，那上万亿个参数，一个子儿都没动。

它做的是，把“用户是个大呆逼”这个事实，提炼出来，存进一个外挂的数据库里，这个就是非常常见的一个技术，叫检索增强生成，也就是RAG。

下次你跟它聊天，它会先在这个数据库里迅速翻一下，找到跟你相关的信息，然后把“已知该用户是个大呆逼”这句话，悄悄地、自动地塞进你们对话的背景信息里，再来回答你的问题。

所以，它的大脑本身还是那个失忆的大脑。

它只是拥有了一个越来越厚的、关于你的外部参考资料库。

它不是真的记得，而是在每次对话前，都先看一遍笔记再来回答，仅此而已。

这很强大，非常实用，但它有极限。这个极限就是，它无法将这些零散的知识点内化为真正的理解或直觉。

而《Nested Learning》提出的设想，是真正地去重塑大脑。

当它的低频层运行时，它不是往外挂数据库里写一行字。

它是用你和它的互动数据，去微调和更新它自己神经网络内部的参数。

这其实就像我们自己学习新技能，通过反复练习，大脑里负责这项技能的神经突触被真正地加强、重塑了。

再举个例子，一个钢琴家。

给他一本新乐谱，他可以看着谱子（外部记忆）弹出来，弹得可能很准，但也许没啥感情，你把乐谱拿走，他就弹不出来了，这就是现在ChatGPT的记忆。

但，如果这位钢琴家花了一个月的时间练习这首曲子，他早就已经扔掉乐谱，曲子已经融入了他的肌肉记忆和情感理解，他的大脑和手指的神经也完全紧密连接。

他不仅能弹，还能即兴变奏，还能跟你探讨这首曲子背后的情感。这就是嵌套学习所追求的境界。

所以，你看，这完全是两个层面的事。

现有记忆，是一种行为上的模拟。它通过外部工具，让AI看起来像有记忆，但其实AI的世界观和底层逻辑是纹丝不动的。

而这个嵌套学习的方法，是一种结构上的成长。它能让AI的神经网络本身发生改变，把新的信息和经验，从零散的数据点内化成模型自身能力的一部分，从而，让知识，真正变成了智慧。

这就是为什么这篇论文，为啥让我如此令人兴奋的原因。

这才是未来，真正的AI。

一个真正懂你的个人助理，你不用每次都跟它重复你的个人偏好和背景信息，它记得你上次跟它聊过你的宠物狗，记得你对猫毛过敏，记得你正在筹备下个月的旅行。

它跟你的互动越多，就越懂你。

这才是真正的。

Personal AI。

而在真正的评测里，论文作者拉来了Transformer++、RetNet、DeltaNet、Titans那些模型，在同样的参数量和训练数据下，HOPE在一串常见评测上，平均成绩都是第一档。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrfdsEwFPxsK9d7RlQ2L6teftXd5cEmjEely00vBTuanMYwUiboKrKf7ZZy3gwAOzsKzNzNH2xrE4A/640?wx_fmt=png&from=appmsg)

这条路，是有可能成功的。

万物皆是嵌套。

一个细胞的生命周期，嵌套在一个器官的运转中。

一个器官的运转，嵌套在一个人的生命里。

一个人的生命，嵌套在一部家族史里。

一部家族史，又嵌套在一个文明的兴衰中。

每一层都有自己的节拍和韵律，它们彼此影响，共同构成了这个复杂而美妙的世界。

也许，我们大脑几百万年进化出来的学习机制，可能真的，非常地道。

而AI要做的，也许不是另起炉灶，而是更谦卑地去模仿这种嵌套的、多层次的、充满韵律感的智慧。

也许，当AI真的学会了遗忘，学会丢弃不重要的信息，学会了沉淀，学会了巩固重要的记忆，学会了在喧嚣中保持一份缓慢的思考时。

它才真正开始拥有智能的幻觉。

甚至。

灵魂的雏形。

这条路还很长，但想想就让人激动，不是吗？

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言