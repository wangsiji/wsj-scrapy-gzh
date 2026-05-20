     AI时代的生成式3D大模型全面评测 - “ChatGPT时刻”的前夜 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI时代的生成式3D大模型全面评测 - “ChatGPT时刻”的前夜
==================================

原创 数字生命卡兹克 数字生命卡兹克 2023-12-24 19:04 天津

> 原文地址: [https://mp.weixin.qq.com/s/BNeSLZ5qxTmJvFrWd0kvEQ](https://mp.weixin.qq.com/s/BNeSLZ5qxTmJvFrWd0kvEQ)

在我过去的所有文章中，我一直把AI分成四个模态去进行分类：  

AI文本（大语言模型）、AI绘图、AI声音、AI视频

而在我最近的交流和访谈中，有一个游离于这四模态之外的存在，被反复提起。

**AI 3D。**

12月20号，这个星期三的晚上，我在接受一个朋友的采访很开心的聊了一个小时，在结束之际，他突然问了一个大纲上没有问题：“你怎么看AI时代的3D？”

说实话我当时有点懵，这个问题我从来没去认真的想过，随便说了一点自己的理解就搪塞过去了。

但是，这不是第一个跟我交流这块的人，在最近一个月里，AI 3D在我各个信息渠道里，都被N次提起。

所以，我也决定写下这篇文章，来聊聊我心中的第五大模态：AI 3D，还有这个领域的现状。

话不多说，开始吧。

目前这个AI 3D这个领域大概有5个主流玩家：Tripo、Meshy、sudoAI、CSM、LumaAI。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURprdiaSPhoF7RbC7Zcm9NZsv913Gjw0hiaJ4ooAeOgQFY2jhaHVOttUosROM8HibZfNoBVvkGNoTxWOA/640?wx_fmt=png&from=appmsg)

CSM和Luma是很老牌的公司了，Luma之前主要做实景扫描的，我一直在玩，前段时间他们搞了一个文生3D的产品Genie，目前还寄生在Discord上，暂不支持图生3D；CSM搞了个实时绘图转3D，但是不支持文生3D。

Meshy做的也比较早，我记得7、8月份就出产品了。Tripo和sudo发的比较新，特别是Tripo，前几天12月21号才发的。

而去聊AI 3D的产品，那绕不过的核心功能和痛点，自然就是建模了。

我简单说一下3D这块的工作流程，让大家有个概念。大概是概念设计 - 3D建模 - 纹理贴图 - 骨骼绑定 - 动画制作 - 灯光 - 渲染 - 合成。

你看到的那些影视特效，或者游戏里的场景，都是需要建模完做贴图然后渲染的。最开始的建模成品是一个素模，大概长这个样子。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURprdiaSPhoF7RbC7Zcm9NZsv7jKmHUWDdiaLgHDupeCZUYo0IsdtMoZZWnxOgb32b7620ScuqacTl2g/640?wx_fmt=png&from=appmsg)

有了模型以后，才能去做后面所有的事。

所以，建模是非常重要的，但是同时也是最费时的，很多时候甚至能占用总时长的30%~50%。在3D领域也没有什么比建模更重要，更枯燥，更需要AI优化的东西了。

几家的产品在AI生成建模上，功能都差不多，文生3D和图生3D。

文生3D和图生3D其实非常好理解，跟AI视频的概念是一样的，只不过在AI视频里是用文或图生成1个4s的片段，而在AI 3D里是生成1个模型。

那衡量大家的标准就非常简单了：**生成的模型质量和精度到底怎么样**。  

一般正常来说，我们用的最多的还是图生3D。  

所以我先用MJ V6跑了一张图：  

Basketball game assets, blender 3d model, obj fbx glb 3d model, default pose, PNG image with transparent background

篮球的游戏资产，Blender 3D 模型，obj fbx glb 3d 模型，默认姿势，具有透明背景的 PNG 图像

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURprdiaSPhoF7RbC7Zcm9NZsvfV1CvT95Yoh6tHAtoBW5KrXb8TUu1XXZzboLO0y0kArKcpqQH9FZgA/640?wx_fmt=png&from=appmsg)

（PS：我真不是因为鸡哥才选择先做的篮球）

然后我把这张图扔到了Tripo、Meshy、sudo、CSM里，因为luma现在不支持图生3D，所以不参与图生3D的对比了。

说实话，我本身对AI 3D的预期其实就不高，所以我一开始才选择上篮球这种非常简单的玩意，结果效果除了Tripo外，另外三个真的差强人意，而且CSM我真忍不住要吐槽一句，生成1个模型要近2个小时。。。。我。。。

我把模型都下载下来了，在Blender里渲染成了动画的GIF，所有摄像机、HDR、参数均统一。大家可以直观的感受一下四家产品的对比。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURqs45cgwgSvaITlP7pEiaMSc2fn7yFggpGDcemD60EUuMxzOMeugeBX6lDKKLt0q9J4bOziaWEZR8Tw/640?wx_fmt=gif&from=appmsg)

可以看到，只有Tripo一家真正的把篮球的纹理给连了起来，成为一个真正的篮球。Meshy和sudo明显看到贴图都崩了，而且这崩都不是忍一忍能用的崩，是彻底用不了的崩。CSM在背后也胡成了一坨。

再去Blender里看看建模细节。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURqs45cgwgSvaITlP7pEiaMScHIQvLZAVD4MMuR7VgpODiaWD6SxibvDG6PUplU2RqtlMiaict7Sicwv9p8Q/640?wx_fmt=jpeg&from=appmsg)

CSM把篮球的凹槽做出来了一点细微的影子，Tripo和sudo的建模中规中矩就是一个不是特别圆的球，还有一些瑕疵，但是能用，Meshy是彻底崩的用不了。

就篮球这个case，Tripo处于遥遥领先的状态。  

Tripo > CSM > sudo > Meshy。  

再多试几个例子。

1.卡通小龙人，毕竟龙年了。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURqs45cgwgSvaITlP7pEiaMScswduliaSecDHvQnGDicKWsIHDZ00AHbSVUicnDYSYVubPvkDHqP7JaZrg/640?wx_fmt=gif&from=appmsg)

Tripo继续很稳，Meshy的模型，有一堆洞。。。。sudo的贴图还行，但是下半身的建模和背后的尾巴结构全崩了。CSM转的那一下有两张脸，给我当时吓个半死，但是模型结构还行。。。

Tripo > CSM > sudo > Meshy  

2.毛衣。毕竟做衣服是做建模里面逃不开的一环。。。  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURqs45cgwgSvaITlP7pEiaMSclFHrEkxoHmoxFNxxmFEjSWW5CuuwLDKRQ9aBxg1ticLFnibKFuicPun2g/640?wx_fmt=gif&from=appmsg)

Tripo表现几乎完美，不管是建模还是贴图，你要是硬挑刺，那就是袖口那没开两个洞（笑。Meshy的建模一如既然的有破洞，而且他们的贴图我发现有一个很大的问题就是，永远是正面精致，但是背面有点崩了。sudo衣服模型的两侧依然有洞，且有不该出现的链接。CSM的贴图和Meshy一个问题，背面和前面差异巨大。  

Tripo > CSM > sudo > Meshy

3.一只玫瑰花。花的建模是最恶心的之一，基本对现在的AI 3D来说是最难的级别，用玫瑰花来给图生3D做个收尾。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURqs45cgwgSvaITlP7pEiaMScJLuw9A1aR26CXADgDtzNicbU3lwnFdpibUxicF7CZQ26Wa4kyFNxbQyEQ/640?wx_fmt=gif&from=appmsg)

Tripo花的正反面模型结构合理，但是叶子的模型粘连崩了，多出了一些奇怪的东西。Meshy依然是面子工程，正面看着感觉还挺惊艳，一转过去就又是破洞了。sudo花朵上的细节崩了，基本看不到花的结构了。

至于CSM。。。。。。真的别问我那一坨是什么东西，我也不知道，但我知道那玩意一定不是花。  

从这四个例子看下来，至少**在图生3D这块，Tripo是断层式领先。**

**整体Tripo > sudo >** **CSM = Meshy。**  

再看一下文生3D，文生3D这块CSM不支持，但是LumaAI的Genie支持文生3D，所以这波对比只对比Tripo、Meshy、sudoAI、LumaAI这四家。

文生3D就真的很吃模型本身的底子了，毕竟图生3D这玩意，图是别人的图，所以展现的更多的是大模型的一个包容能力或者通用能力，你图生3D做的不好，可以有理由说MJ生成的图片风格，跟你3D大模型不契合，所以效果不好。而文生3D，就是扎扎实实看你的底子了，都是自己体系里的东西，再做不好那就是真的不太行了。

文生3D这块的流程有点像Runway的文生视频，runway是给一个prompt后会出4个第一帧，然后你选用哪个图去生成后面的视频。

而文生3D是会先用十几秒时间，根据你的prompt生成4个粗糙的预览模型，你可以自己决定用哪个去后后面的refine（精炼）。大概长这样。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqs45cgwgSvaITlP7pEiaMScwOjYqXrKoNWKBGIRh3Famwg0spX0YdqN3dwAJ22UxSncqbNNqTKkxA/640?wx_fmt=png&from=appmsg)

前置的预览模型会比较粗糙，但是可以让你大概去选自己想要的造型。

我先试第一个Prompt，毕竟马上圣诞了，给大家整个活：

spiderman dressed in christmas style with a christmas hat，highest quality（蜘蛛侠穿着圣诞风格，戴着圣诞帽，最高品质）

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURqs45cgwgSvaITlP7pEiaMScbNoakmQeW0Kh4OPsyB0wlOuialgeYoloUWu2OhtaalY8Fibyhnc6AMfg/640?wx_fmt=gif&from=appmsg)

Tripo和Luma的效果都非常好，Tripo整体更偏写实，Luma会偏一些卡通，Luma唯一的瑕疵就是膝盖多出来两块莫名奇妙的白斑。meshy干成葫芦娃了。。。sudo的贴图精度不太行，而且帽子衔接处有BUG。

Tripo > Luma > sudo > Meshy。  

再做一个猫女，毕竟，做3D怎么能缺了美女呢：  

an anime catgirl（动漫猫女孩）

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURqs45cgwgSvaITlP7pEiaMSckszmAMIW3xalpxMZ2VtpWnp1J9HoJez4BCsG9gMo0dPntEBiaWUKbqg/640?wx_fmt=gif&from=appmsg)

Tripo和Luma依然稳如老狗。Meshy，有点诡异，感觉这个贴图完全没有质感跟纸一样。。。sudo直接做了个抱枕。。。我特么。。。。  

Tripo > Luma > Meshy > sudo  

最后一个case，做个游戏的3D资产吧，黄金手枪：  

golden pistol, unreal engine, highest quality（黄金手枪，虚幻引擎，最高品质）

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURqs45cgwgSvaITlP7pEiaMSc8P4CZpaMsek5eOg54dPxfZc3We0F8DZricCIZR5E22QR4lrzEWwGXLg/640?wx_fmt=gif&from=appmsg)

手枪的细节具体的我就不评价了，大家自己看吧。Luma和Tripo还是强，枪口的细节上，Luma比Tripo精致一些些。

Luma > Tripo > Meshy > sudo  

文生3D，目前整体看下来，Tripo和Luma基本是断层式领先，在一些细节上，Tripo会优于Luma。

**而在图生3D和文生3D整体上，Tripo是目前绝对的王者。**  

Tripo网址在此：https://www.tripo3d.ai/

Luma的文生3D想体验的也可以直接去Discord里面，搜他们频道加入体验就行。

另外三个我就不推荐大家去试了，没太大意义。

但是你像Tripo和Luma，目前也依然有不少瑕疵，比如模型的布线有点乱、比如人物面部贴图大概率会崩、比如金属材质的渲染不够精致等等。  

不过我相信时间会解决一切，你像Tripo，一个刚出来3天的第一代产品，你指望他一步登天也不可能，更别提AI 3D这个领域也才刚刚开始卷。  

目前看下来，AI 3D的进程，以Tripo和Luma为首，大概等于AI绘图的Midjourney V2或者V3，其他家还处于V1的水平。

而Midjourney的大爆发，也是以V4为标志，开始颠覆整个行业，直到前几天的V6，爆杀全场。

**AI 3D，现在就是GPT时刻的前夜。**

爆发来临的那一天，可能比你我想象的都更快。

 **写在最后** 

2019年的时候，我曾经做了一幅3D作品，以纪念我一个游戏伙伴的离职。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURqs45cgwgSvaITlP7pEiaMSc740bkS63zHbibRx8ibwgLSia9yZwtYr0FbtpMpgRribJkSwWRlGyhxWQAA/640?wx_fmt=jpeg&from=appmsg)

当时我是这么说的：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqs45cgwgSvaITlP7pEiaMScj91U4jzYU9Y8UVfnw31OPic1Ryd6UVvOvwj8RT6ZOMImXG8uVd39eCg/640?wx_fmt=png&from=appmsg)

我做这张图，整整花了1月的晚上和周末。  

里面90%的模型，都是我自己徒手建模的，那个工作量，非常非常痛苦，建模耗去了我整体70%的时间。  

如果再让我来一次，我一定不会再去做了，我不想再经历一次那样的折磨。  

这只是我，一个不专业的设计师而已。  

而你知道在游戏中，在影视中，有多少需要建模的东西吗？

《艾尔登法环》为例，有上百个BOSS，还有无数的场景，无数场景里有无数的3D资产，大到BOSS、城堡，小到武器、盔甲、蜡烛、桌子。

以From Software的业界上游生产力和工业化水平，整整做了5年时间，才将老头环掏出来。

《博德之门3》，拉瑞安最顶峰时400人团队，开发了6年。  

《流浪地球2》，全流程制作周期，3年。  

我也跟很多影视后期从业者都聊过一个问题，他们现在最需要AI来优化的步骤是什么，答案出乎意料的统一：  

**建模。**

我极度看好AI 3D，并不是因为这个领域新，而是这玩意真的能切切实实解放内容创作者们的生产力，让他们用更多的精力，花在创作上，保护这些创作者的创作精力。  

建模只是其中一个环节，还有AI纹理贴图、AI绑定骨骼、AI动捕等等等等。

当用AI来重塑整个3D管线，打通全流程，那效率，起飞了。

而且并不是只有游戏和影视这种专业者需要。  

还有一个更大的家伙，3D资产是其中的基建，没有超高效率的AI 3D流程，没有AI的辅助建设，这玩意基本很难实现。

**这玩意就是：元宇宙。**

我从来不认为元宇宙是个噶韭菜的东西，他是我坚信的未来，只不过现在还离得有点太远，因为基建和产能跟不上，世界都没搭起来，元宇宙个屁啊。  

AI 3D，就是元宇宙最好的创作引擎。  

我一直相信未来的3D会内容无限扩大，每个人都可以成为超级创作者，像神一样创造新的世界，创作你自己的元宇宙。

那一天，不会太远。  

明年，我们估计就能见证，AI 3D那加速的未来。

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言