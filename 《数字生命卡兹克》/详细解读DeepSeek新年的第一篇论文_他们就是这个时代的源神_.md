     详细解读DeepSeek新年的第一篇论文，他们就是这个时代的源神。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

详细解读DeepSeek新年的第一篇论文，他们就是这个时代的源神。
=================================

原创 数字生命卡兹克 数字生命卡兹克 2026-01-04 09:18 北京

> 原文地址: [https://mp.weixin.qq.com/s/e9ULrG8RUYkoN8PDrZjiCQ](https://mp.weixin.qq.com/s/e9ULrG8RUYkoN8PDrZjiCQ)

2026年新年第一天，DeepSeek又开卷了。

发了他们新年的第一篇论文。

《mHC: Manifold-Constrained Hyper-Connections》

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgFibcrNgKP6hrLNmtE46S1AkJYAGASZOqs7hASviam2uHqrsjOGUgGWwXg/640?wx_fmt=png&from=appmsg)

感觉是DeepSeek-V4的铺垫，当然一些小道消息，不保真，我也不懂，我只是拍脑袋预测一下，有问题别找我。

就是V4，大概在1月中下旬或者1月底，然后呢，有多模态输入，没有多模态输出。

就酱，回到论文。

这篇论文我是说实话，有点过于硬核了。

但同时，传递出来的信息量和对AI界的改变，又是巨大的。

在给自己放了一天假，然后啃了一天以后（这玩意比我想象的难啃多了。。。）我还是想，用最通俗易懂最有意思的方式，来跟你聊聊，这篇论文的有趣之处，以及，是如何对现在的生态进行一些新的输入的。

当然也给我自己叠个甲，我不是算法出身，我只是读完以后觉得很棒想分享给大家看，如果能激发部分人对AI的兴趣或者对原论文的好奇，那就更棒了。我对这篇论文的理解和乱七八糟的各种名词解释，都是我自己民科瞎JB自学的，部分措辞也有为了能让大家更好理解而做的部分简化，如果有我理解的错误或者事实性错误的地方，欢迎大佬们在评论区指正讨论，感谢。

话不多说，我们，正是开始。

在最开始之前，我想先问大家一个问题，就是大家认为，一个要处理图片、声音、文字这么多乱七八糟信息的新模型，它最需要的是什么？

是一块更强的GPU吗？是一个更大的内存吗？

而DeepSeek这篇文章，给出的答案，其实，是一个极其稳定、高效的、模型内部的信息流转系统。

要理解这个玩意，我们先得穿越回去，穿越回2015年，也就是十年前，从一个男人和一个伟大的想法说起。

这个故事，要从盘古开天，啊不，要从何恺明盖楼开始聊。

对，何恺明盖楼。

我们都知道，大模型是神经网络对吧，现在，你可以把一个神经网络，当成一家开在101大厦里的超级公司。

数据，就像一份客户需求，从一楼的前台进去，然后呢，先交给销售部分析，在传给二楼的市场部包装一些，接着送到三楼的产品部进行需求评审。。。

客户的需求，也就是数据，就这样坐着楼梯，一层一层往上爬，每一层都对这份信息做一点点加工和提炼。

最后，这份被层层解读过的报告，会送到顶楼的CEO办公室，由CEO拍板，给出最终决策，比如“没问题咱就这么干！”。

理论上，公司的楼层越多，部门分工越细，那这家公司专业度就越高，也越牛逼，处理复杂问题的能力就越强，对吧。

但在2015年，全世界的AI大佬们，都碰到了一个鬼故事，就是，这栋楼，它特娘的盖不高啊。

最多盖到二三十层，就到头了。

再往上盖，整个公司就直接罢工了。

因为信息在传递过程中会失真。

不知道你们有没有玩过类似于王牌对王牌里面那种传声筒游戏。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgFgQfBGeWosVbR0TbZbricECGdwWAMFF2LiaicHR5GBAyrj4845uslQkbgg/640?wx_fmt=jpeg&from=appmsg)

就是第一个人接到信息以后，在有限时间内，往后传，最后一个人复述出来，看看还能复述多少字。

这个游戏巨搞笑，因为最后一个人说出来的跟第一个人往往风牛马不相及。

在这个101大厦的公司里，也是一样的。

就比如一楼销售部明明说的是“老板想喝咖啡”，传到十楼就变成了“老板喜欢吃咖啡壶”，传到二十楼成了“老板去中国有嘻哈上唱了首咖啡壶我的Baby”，等传到三十楼CEO耳朵里，可能已经变成了“老板觉得自己是只屌炸天的咖啡壶”。

这就完蛋了。

CEO根据这个离谱的信息做出的决策，肯定是灾难性的。

在AI里，这个现象有个高大上的名字，叫梯度消失。

说人话就是，信号在深层网络里传来传去，衰减得一干二净，脑子直接短路了，这破活干不了一点了。

然后呢，就在整个AI界都对着这现象一筹莫展的时候，当时还在微软的何恺明，就站了出来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgFDb7LrYK3z8h6yl6Od3rYN2FKRlJYI4KoLWMRFZFD4VsUCxzMwI4a3Q/640?wx_fmt=png&from=appmsg)

他做了一个看似简单，却直接改变世界的决定。

他在大楼里，修了一部VIP直达电梯。

这部电梯，从一楼前台，可以直达任何一个楼层，包括顶楼的CEO办公室。

于是，流程变成了这样。

客户需求文件进来后，依然需要一层一层地坐楼梯往上爬，接受各个部门的加工，但与此同时，前台会把这份文件的原件复印件，放进这部VIP电梯，直接嗖地一下，送到CEO的办公桌上。

这样一来，CEO在看下面部门交上来的那份可能已经被传得面目全非的报告时，他可以随时拿起旁边那份原件复印件来对比一下。

“哦，底下人说老板是咖啡壶，但原件说的是老板想喝咖啡，那肯定是底下人传话传错了”。

信息，就这样被保真了。

这部天才的电梯，就是残差连接（Residual Connection）。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgF2IhCmpoekHJH3jyZVaKja88vyhf27dWBxyS1npExQsGOFaRzj2cqXw/640?wx_fmt=png&from=appmsg)

它像一根定海神针，贯穿了整栋大楼，让最原始的信息可以在不同楼层间无损穿梭，时刻校准着整个公司的前进方向。

可虽然这部电梯很伟大，但它也有一个致命的毛病。

就是，它太TM窄了，它是一部只能容纳一个人的小电梯，一次只能送一份文件。

时间快进到今天，AI公司已经不是当年那个只处理文字需求的小作坊了。

它成了一个要处理图片、视频、音频、代码的超级巨无霸。

CEO每天要处理的信息，从一份文件，变成了一卡车的资料。

只靠一部小小的VIP电梯来回送复印件，运力严重不足。

这条曾经的VIP电梯，现在成了全公司最堵的羊肠小道。

咋办呢。

于是，一群更激进更年轻的大佬，一拍桌子说，靠，一部电梯不够，咱们把整面墙都砸了，修一个电梯井吧，把一条单行道，直接拓宽成双向八车道，让信息流淌起来不就完了？

这个狂野的想法，就是超连接（Hyper-Connections）。

来自2024年字节Seed发的一篇论文。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgFKKNf32HJk6Lnp7POs4HyNicctyj45iaOyNqicRCNwBYIe20fE8dpACLzw/640?wx_fmt=png&from=appmsg)

以前，信息是一条单线流动的信息流。

现在，他们把这条信息流，强行扩容成了四条、八条并行的信息流VIP电梯。这就好比以前公司里只有一个信使，现在搞了一个8人信使送货团，8个人一起拎着大包小包一起送信。

这下牛逼坏了，信息通量瞬间指数级暴增，模型的性能也确实立竿见影，蹭蹭往上涨。

你看，电梯多了，聪明的智商又占领高地了，对吧。

但是，但是又来了。

就像所有恐怖故事的开头一样，好景不长。

这条宽阔的八车道VIP电梯，很快就开始闹鬼了。

你想啊，这个8兄弟，他们是人，不是机器。

他们在路上会互相聊天，会交流情报，人多嘴杂，就导致他们不再是单纯地传递信息，这几个人，开始在信息流里自由发挥了。

于是，各种诡异的事情发生了。

就比如说，一楼前台收到消息说市场部小王今天可能要请假。

信使A听了，觉得这事儿挺重要，告诉了信使B。

信使B觉得可能这个词不确定，就跟信使C说市场部小王今天要请假。

信使C一琢磨，觉得得强调一下严重性，就跟信使D说市场部整个组今天都要罢工。

最后传到CEO耳朵里，就变成了：

市场部全体员工已经卷款跑路了！！！

CEO：？？？？？？？？

一个无关紧要的小信息，在多条信道里被反复共振、放大，最后酿成了一场灾难。

这就是，信号爆炸。

再比如，一份十万火急的服务器着火了的文件，被分成了八份，交给八个信使，让每个信使都去送信。

但是呢，每个信使都觉得，这么重要的事，其他七个人肯定会送到的，我不如出去挣个外快先去送个外卖。

结果，谁都没送。公司直接烧成了灰。

这就是信号消失。

整个公司的信息系统，陷入了一片混乱。

这就导致，模型训练到12000步的时候，突然性能就断崖式下跌，跟跳楼似的，比心电图还心电图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgFxuUTGMIpUlBr0LmjCp2J8ZvfE2bpwicrRwWlXJE60Xt6HQ3WfmhlunQ/640?wx_fmt=png&from=appmsg)

这模型就算废了，直接训崩了。

这就是HC技术最大的命门。

它为了追求信息通量，牺牲了信息的保真度和稳定性。

好了，铺垫了这么久，DeepSeek的mHC终于要登场了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgFJJsYYvKXrzBkKRQXJfhjVIKSK8a8Q9WRX2FbsylKzcLtpfX0Bia2ZXA/640?wx_fmt=png&from=appmsg)

对，我们今天的主角，是mHC。

只不过为了让大家理解，mHC到底为了解决什么问题，所以，花了这么大的篇幅，给大家讲了背景故事。

mHC，全称Manifold-Constrained Hyper-Connections，流形约束超连接。

注意这个词，约束。

DeepSeek他们干了个啥事呢，他们没有开掉那几个信使，也没有砸掉电梯说劳资要用火箭送用个鬼的电梯。

他们只是给这个8人送信小队，制定了一套极其严格、甚至有点变态的信息传递纪律。

这套纪律的核心，在论文里叫双重随机矩阵约束。

咱们还是说人话，举例子。

你可以理解为，他们设立了一个叫做内部审计部，由一个究极不近人情的德国老太太领导，权力大到吓人。

这个审计部咧，给每个信使都发了一本小册子，上面印着两条铁律。

第一条铁律，我们称为信息能量守恒定律：作为一个信使，你从上一站收到的所有信息，其信息能量总和为100%。那么在你把信息传递给下一站的队友时，你传递出去的所有信息的信息能量总和，也必须不多不少，正好是100%。

回到上面信息爆炸那个案例。就比如说，信使A收到了小王请假这个信息，我们假设它的信息能量是10个单位。

这时候，信使A想添油加醋告诉信使B一个更夸张的版本。

但审计部的系统会立刻报警，因为信使A私自加信息了，导致他的输出能量（比如20个单位）大于了他的输入能量（10个单位）。

他这是在无中生有暗度陈仓顺手牵羊，严重违反了信息能量守恒定律，结果就会是，信使A当场被开除。

在这套铁律下，信使们依然可以交流，但任何放大和夸张的行为，都会在数学上被立刻识别并禁止。

谣言的传播链，从根上就被斩断了，信号爆炸的问题，就此解决。

第二条铁律，我们称为团队责任绑定定律：对于任何一个需要被送达的信息，比如服务器着火这份文件，最终抵达目的地的信息能量总和，必须不多不少，正好等于它出发时的信息能量总和。

就比如还是刚刚的那个服务器着火的事。

信使A想：“这么多人呢，我不送也没事吧？” 于是他选择了摸鱼，他贡献的信息能量是0。

信使B也想：“总有傻子会送的。” 他的贡献也是0。。。

如果八个人都这么想，那么最终抵达CEO办公室的，关于服务器着火的信息能量总和就是0。

审计部的系统立刻就会拉响最高级别的警报，因为它发现出发时明明是100单位的能量，抵达时却变成了0。根据团队责任绑定定律，整个信使团队都将面临重罚。

为了避免这种情况，信使们就必须互相补位。如果A不干，B、C、D……就必须分摊他的工作，因为最终的那个总和是死命令，必须凑够。

责任扩散的可能性，在数学上就被杜绝了。

信息，必须被送达。

信号消失的问题，也就此解决。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgF3icURzMYGs8bSe40KiaWw2RcUYKhWvjZNaC7gvUWUPHsqlHnRo1jzylA/640?wx_fmt=png&from=appmsg)

这两条铁律合在一起，就是所谓的双重随机矩阵约束。

它没有禁止信使们交流，八车道高速公路依然车水马龙，信息依然可以在其间自由组合。

但所有的自由，都被约束在了一个能量守恒的流形之内。

这就是mHC的精髓。

在这约束之下，给你自由。

那最后的终极问题来了，这玩意，解决了HC的不稳定问题之后，到底有什么用？

我先说两个数字。

第一个，就是这套所谓的审计系统，会带来大概6.7%的额外训练开销。

第二个，就是在能力上，确实有部分提升，相对HC额外多出约2个点。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgF7BSOCSPEfp33niceaZXyHgA1xWZLaPrjt4XArPCPc4DwSu9BgDGmBsg/640?wx_fmt=png&from=appmsg)

看着是不是好像有点投入产出不成正比？这生意听起来，好像有点亏啊。

但是，别被表面骗了。

在模型训练里，还有一个很核心的词，叫稳定性。

比如之前HC架构的那个公司，会有各种信息爆炸的问题，如果我原来的信息能量初始值是1，在信息传递过程中，最高的时候，信息能量到CEO办公室的时候，能干到3000。

你就能想象到，有多失真。

这个恐怖的失真，有时候就直接变成了摧毁模型训练的一场风暴。

而DeepSeek的mHC。

在铁律之下，几乎全部做到了100%保真，最高也不过才1.6。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpIs9PW9jy4jLH0xl92rDgFjvMxoMlEnuhIAgrxicDFC1alWrNQBwHrjvJiawZeauicpQDhZ0N9GTtNg/640?wx_fmt=png&from=appmsg)

3000:1.6。

直接降低了3个数量级，对，不是3倍，是3个，数量级。

这就是mHC，最牛逼的地方，太尼玛吓人了。

而这个稳定性，带来的好处，显而易见。

它用额外6.7%的开销成本，让你模型训练瞬间崩盘的3000倍的系统性风险，直接摁死到了可以忽略不计的1.6倍。

要知道，模型训练，太贵了，对于一家AI公司来说，训模型每一秒烧掉的钱都是触目惊心的。

任何一次过程中训练的崩盘，那损失的，就不只是6.7%的额外开销了，那是100%的建造成本，所有的一切，全特么重头再来。

有可能就是数千万的成本，还有好几周的时间。

这就是HC系统那个心电图背后，极高的、不可预测的、灾难性的失败风险。

他确实提高了模型的效率，但是这个不稳定性，几乎很难接受。

现在，我们再回来看mHC那6.7%的额外开销。

你现在还觉得它贵吗？

你把他当一份保险看，你就觉得，一丁点也不贵了。

仅仅6.7%的额外开销，就能为一项千万美元级别的投资提供近乎百分之百的安全保障，这在任何一个金融模型里，都是一笔划算到笑出声的买卖。

而且，性能还是更强的，这买卖，好到离谱好吧。

稳定、高效、还更强。

这三者通常是一个不可能三角，你只能取其二。

而mHC，用一个精巧的数学设计和极致的工程优化，把这三者全占了。

这就是为什么我说，这篇论文虽然低调，但意义重大。

DeepSeek。

真的就是我们这个AI时代的源神。

每一篇论文，都能给行业，一些小小的震撼。

赞美源神。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言