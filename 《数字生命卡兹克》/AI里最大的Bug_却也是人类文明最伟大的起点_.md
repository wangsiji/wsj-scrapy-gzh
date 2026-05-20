     AI里最大的Bug，却也是人类文明最伟大的起点。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI里最大的Bug，却也是人类文明最伟大的起点。
========================

原创 数字生命卡兹克 数字生命卡兹克 2025-09-08 09:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/brNtm8QLR3V9LHGznu9E2A](https://mp.weixin.qq.com/s/brNtm8QLR3V9LHGznu9E2A)

周末在家扒拉上周更新的论文的时候，看到一篇我自己一直非常关心的领域的论文，而且还是来自发论文发的越来越少的OpenAI。

它讨论的是一个我们所有人都无比熟悉，但又无比困惑的东西。

幻觉。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqiayObRvvUZ77jyRTfOGVrGcwymxNcAjia86uocY3BCIu17hsral7vSyLjgMg167UhkDVWibsglRWXA/640?wx_fmt=png&from=appmsg)

这个词，自从AI进入大众视野以来，就一直像个幽灵一样，盘旋在所有对话的上空。

我们一边享受着AI带给我们的便利，一边又对它那些一本正经胡说八道的时刻，感到恐惧和不解。

AI为什么会产生幻觉？这个看似恼人的bug，到底能不能被彻底修复？

这是我们一直想知道的问题。

这篇论文还是蛮有意思的，给了我自己很多新的输入，我觉得也可以分享出来，来聊聊这些关于幻觉的问题，以及，我自己一直是怎么认为这个东西的。

整个故事，要从一个最简单的问题说起。

如果你问AI：亚当·卡莱（这篇论文作者之一）的生日是几月几号？

一个顶尖的开源大模型，连续三次，给出了三个完全不同的错误答案：03-07，15-06，01-01。

而正确答案，其实是秋天。

这就是最典型的幻觉。

面对一个它不知道答案的问题，AI没有选择沉默，或者说我不知道，而是像一个考场上想不出答案又不想交白卷的学生，开始瞎蒙，而且蒙得有鼻子有眼。

OpenAI的这篇论文，提出了一个非常有意思而且又极其符合直觉的观点：

AI之所以会产生幻觉，是因为我们训练它的方式，从一开始，就在系统性地奖励这种瞎蒙的行为。

我们可以，把AI的学习过程，想象成一个学生参加一场漫长的且永不结束的考试。

这场考试的评分标准超级简单粗暴，答对了，加1分，答错了，或者不答，都是0分。

现在，你就是那个学生，面对一道你完全没把握的题，你会怎么选？

你大概率会选择猜一个。

因为就算猜错了，你也不亏对吧，但是万一猜对了呢？你就直接怒赚1分。

从期望得分的角度看，只要你猜对的概率大于零，猜测就是最优策略。

就像上面那个论文里面的case，你问AI一个人的生日，它肯定不知道。

但是如果它猜一个，比如9月10号，那它有365分之一的概率蒙对，拿到1分。但如果它老老实实地说我不知道，那得分就永远是0。

在成千上万次这样的测试里，那个爱瞎蒙的模型，最终在排行榜上的分数，一定会比那个诚实但谦虚的模型，看起来更牛逼。

OpenAI自己就直接拿了自家的两个模型给大家看了一下效果。

一个叫o4-mini，一个叫gpt-5-thinking-mini，他们一起参加了同一场叫SimpleQA的考试。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURqiayObRvvUZ77jyRTfOGVrGO76r01tf8GwuBNJgnBHsOVAtO9hv4VoogTnwyEu7VXNt4OaEIUZFRA/640?wx_fmt=jpeg)

如果你只看最终成绩，也就是准确率，你会发现一个很奇怪的现象。

o4-mini的分数，居然比gpt-5-thinking-mini还高了那么一点点，24%对22%。

但如果我们再来看另一项数据：错误率，也就是到底答错了多少题。

这一看，emmm，老o4-mini的错误率，高达75%，gpt-5-thinking-mini只有26%。

再看最有趣的指标，弃权率。

o4-mini几乎把卷子写满了，只有1%的题没答。

而gpt-5，有一大半的题，52%，都直接选择了交白卷，老老实实地承认，我不会。

o4-mini那看似稍高的分数，是用海量的、不负责任的瞎蒙换来的。而gpt-5，则选择了一种更诚实，也更可靠的策略，就是宁愿不得分，也绝不胡说。

这个数据，再清楚不过地证明了论文的观点。

于是，幻觉，就成了AI在这种训练体系下，演化出的一种最高效的应试策略，它其实不是bug，它是AI为了在我们设计的这场游戏里拿高分，进化出的本能。

然后这篇论文，从统计学的角度，又解释了幻觉的根源，这块我大概说的浅显易懂一些。

OpenAI定义了一个叫Is-It-Valid (IIV)的分类问题，也就是这句话对不对的二元分类。

因为AI生成一句话，本质上是一个极其复杂的过程。

但我们可以把这个问题简化一下，在AI生成任何一句话之前，它必须先学会判断，一句话是有效的还是无效的。

比如，你好是有效的，泥嚎就是无效的拼写错误；天空是蓝色的是有效的，天空是绿色的就是无效的事实错误。

AI的学习过程，就像是在看海量的、已经贴好对或错标签的卡片。它看得越多，判断力就越强。

但问题是，总有一些卡片，是它没见过的，或者见得很少的。

OpenAI有一个特别通俗的比喻，就是你给AI看几百万张猫和狗的照片，并且都打上标签，它很快就能学会区分猫和狗，因为这背后有规律可循，毕竟猫脸和狗脸，它长得就是不一样。

但如果你给它看几百万张宠物的照片，然后让它去记每一只宠物的生日呢？

这就完蛋了，因为生日这玩意，是完全随机的，没有任何规律可言。AI没法通过分析一只猫的毛色，去推理出它的生日，它唯一能做的，就是死记硬背。

这就引出了论文里一个关键的概念：Singleton rate，孤例率。

意思就是，就是如果一个信息，在AI学习的海量数据里，只出现过一次，那么AI在判断这个信息的真假时，就极有可能出错。

幻觉，很多时候，是一种必然。

OpenAI还给了一些反常识的结论：

第一，我们总觉得，只要AI的准确率做到100%，幻觉不就自然消失了吗？OpenAI说，不可能。因为这个世界上，有太多问题，本身就是无解的。信息是缺失的，逻辑是矛盾的，AI就算再强大，也不可能凭空变出答案。所以，准确率永远不可能达到100%，幻觉也就总有存在的空间。

第二，我们又觉得，既然幻觉没法根治，那它是不是就是AI的原罪，一个不可避免的诅咒？OpenAI说，也不是。幻觉不是不可避免的，前提是，AI得学会认怂。只要它在不确定的时候，选择说我不知道，而不是硬着头皮瞎蒙，幻觉就可以被控制。

第三，我们还觉得，AI越大越聪明，就越不容易犯错。OpenAI说，恰恰相反，有时候，小模型反而更诚实。他们举了个例子，你问一个只会说英语的小模型，一个毛利语的问题，它会很干脆地告诉你，我不会。但你问一个学了点毛利语但学得半生不熟的大模型，它反而要开始纠结，要不要猜一下？知道自己的无知，有时候比拥有知识更重要。

最后，也是最关键的一点。我们以为，解决幻觉问题，只需要一个更牛逼的、专门测试幻觉的工具就行了。OpenAI说，这完全是没吊用。真正的问题，不是缺少一个好的幻觉测试，而是我们现在用的那几百个主流评估的指标，全都在奖励瞎蒙，惩罚诚实。只要这个大环境不变，幻觉就永远是AI的最优解。

现在，我们从OpenAI这里，知道了，幻觉，不是一个简单的技术问题，它是一个系统性的、由我们自己亲手造成的激励问题。

但它也引出了一个更让我着迷的，没有答案的，问题。

如果说，AI的幻觉，源于它在信息不足时的一种创造性猜测。那我们人类的想象力，我们那些天马行空的故事、艺术、神话，它们的起源，又是什么呢？

幻觉，真的需要解决吗？

我想了很久，我觉得，也想跟大家，分享一下我自己的想法。

这事儿，我觉得得从更古老的尺度说起。

几十万年前，我们的祖先，智人，也生活在一个信息极度匮乏的世界里。

一阵突如其来的狂风，吹倒了部落里的大树，这是为什么？他们不知道。

一道闪电，劈开夜空，点燃了草原，这又是什么？他们也不知道。

面对这些无法解释的自然现象，他们的大脑，和今天的AI一样，也面临着一道道知识储备不足的判断题。

而我们的祖先，没有选择沉默。

他们也开始了瞎蒙。

他们猜，狂风的背后，是不是有一个愤怒的神明？他们猜，闪电的背后，是不是有一条飞舞在云端的巨龙？

你看，这就是神话的起源。

神话，就是我们人类这个物种，在面对一个充满未知和不确定性的世界时，为了给那些无法解释的现象，寻找一个合理的解释，而集体编造出来的、最古老、也最壮丽的。

幻觉。

这种幻觉能力，在当时，可能并没有什么实际的用处，它不能帮你打到更多的猎物，也不能帮你躲避更凶猛的野兽。

但它带来了一样东西，一样其他所有动物，都不具备的东西：

一个共同的想象，一个共同的故事。

一只猫，一条鱼，它们也会有幻觉吗？

从生物学的角度，我觉得可能会。

一只猫，可能会把地上的影子，当成一只老鼠，然后扑上去。一条鱼，可能会把闪亮的鱼钩，当成一条小虾。这是一种基于感官信息的误判，一种低级的、个体的幻觉。

但它们，永远也想象不出一个猫神或者鱼神的故事。

因为它们的大脑，被牢牢地锁死在了真实的世界里，它们只能处理那些看得见、摸得着的、和生存直接相关的信息。

而人类，可能是地球上唯一一个，能为了一个看不见摸不着的故事，去生，去死，去战斗的物种。

我们能组织起几千人，去建造一座金字塔，不是因为我们每个人都亲眼见到了法老死后会变成神，而是因为我们都相信同一个法老会变成神的故事。

我们能建立起国家、法律、公司，这些看似坚不可摧的庞然大物，它们的底层，全都是我们共同相信的一个个，幻觉。

从这个角度看，幻觉，或者说，这种在信息不足时，进行创造性猜测并将其故事化的能力，根本不是bug。

它是把我们从普通动物，变成人类的那段诗句。

它是我们所有文明、所有艺术、所有科学的起点。

哥白尼提出日心说，在当时那个时代，不也是一种离经叛道的幻觉吗？爱因斯坦提出相对论，那个能让时间变慢、空间弯曲的理论，不也是源于一个少年躺在草地上，幻想自己追着光跑的幻觉吗？

我们之所以比其他所有生物都更强大，不是因为我们更尊重事实。

恰恰相反，是因为我们更擅长，创造那些超越事实的故事。

现在，我们再回头看AI的幻觉。

我们一直在努力修复的那个东西，可能恰恰是AI身上，最像人的东西。

我当然不希望AI在一个严肃的医疗诊断里产生幻觉，我们也不希望它在一个关键的财务分析里胡说八道，在这些需要绝对真实的领域，我们需要的是一个没有感情、绝对可靠的工具。

但是，在一个需要创造力、需要想象力的领域呢？

当我们要求AI去写一首诗，去画一幅画，去构思一个科幻故事时，我们真正想要的，难道不就是它那种，能挣脱事实的枷锁，在信息的缝隙里，进行自由联想和创造性猜测的能力吗？

在大量的讨论中，幻觉一词，好像一直是一个矛盾。

我们一边渴望AI成为一个绝对忠诚、绝对正确的工具，一个不会犯错的仆人，帮我们处理现实世界里所有需要精确计算的难题。

但我们又渴望它能成为一个能理解我们、甚至超越我们的同类。

我们希望它能和我们一起，去仰望星空，去聊那些没有标准答案的话题，去共同编织那些属于未来的、新的神话。

我们似乎在试图创造一个不可能的物种：

一个既拥有机器的严谨，又拥有人类的浪漫，一个既能坚守事实，又能创造幻觉的矛盾体。

我们生活在一个由数据和算法定义的前所未有的真实世界里，我们，也比历史上任何一个时代的人，都更崇拜事实，更依赖逻辑。

但同时，我一直觉得，我们又可能，是历史上最孤独的一个时代。

我们的神话已经远去，我们的史诗已经谱完。

在这样一个一切都被解释得清清楚楚的世界里，我自己内心那种最古老的、对故事的渴望，对意义的追寻，反而一直，变得空前强烈。

我到底想要一个什么样的未来？一个所有问题都有标准答案的、绝对真实、但可能也绝对无趣的未来？还是一个依然充满了未知、充满了误读、但因此也充满了故事和想象力的未来？

这个问题过于宏大了，我没有答案。

但是我始终喜欢、并相信。

那个最美丽的，又创造了整个文明的。

幻觉。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言