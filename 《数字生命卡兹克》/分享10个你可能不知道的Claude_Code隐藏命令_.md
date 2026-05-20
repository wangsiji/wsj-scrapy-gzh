     分享10个你可能不知道的Claude Code隐藏命令。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

分享10个你可能不知道的Claude Code隐藏命令。
============================

原创 数字生命卡兹克 数字生命卡兹克 2026-03-20 10:08 上海

> 原文地址: [https://mp.weixin.qq.com/s/XopaISgwzSgoqZctym\_Ajg](https://mp.weixin.qq.com/s/XopaISgwzSgoqZctym_Ajg)

最近发现一个很有意思的现象。

我们公司很多很多的小伙伴，都在用Claude Code，因为这玩意，在很多时候，确实就是最牛逼的通用Agent。

但，公司的小伙伴，大家的用法差异巨大。

有的人已经能开Agent Team并行跑任务了，有的人到现在还在每步挨个确认，然后不知道在命令行里怎么换行。

昨天眼看到小伙伴发现Prompt写错了没发现，然后开发完了面目全非，准备开始重来的时候，我随口提了一句，说你咋不用回退。

他来了一句，啥是回退。

然后我就懵了，我就在公司里问了一下，知道在Claude Code里按两下Esc可以回退代码的举个手，结果在场七八个人，只有一个知道。

我当时就觉得很有意思，我觉得很值得来聊一聊。

因为我自己Claude Code最近用的非常多，里面有很多隐藏命令，其实能让你的体验究极加倍。

而且，Claude Code这玩意儿更新实在太快了，快到什么程度呢，日本有个开发者写了篇文章吐槽说，你上班的时候它在更新，你睡觉的时候它还在更新，甚至，有些功能我在在更新日志里是真的没有看到，还是开发团队的人在Twitter上随口一提我才知道的。。。

所以我今天把自己用了这么久的Claude Code的，觉得最有用的一些命令整理了一下，不是什么大而全的教程，就是我自己实际用下来觉得很实用的，给大家分享一下。

希望能对大家有点帮助。。

话不多说，我们开始。

  

**一. /btw**

/btw这个命令是今年3月11号才出的。

Claude Code负责人Thariq在Twitter上发了个帖子介绍，直接两百多万的阅读量，你就知道，大家有多需要这个功能了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUaQs0ZiaPT7cL0NNCVlL3ZaOVAZdt5bPVqpsGwxa5zvibpJKkNPXCzibgUl20qQwE5uP6NbKMzYQuOf56luWaln4zdb3eybRmb6U/640?wx_fmt=png&from=appmsg)

/btw是干嘛的呢，它让你在Claude正在干活的时候插一个问题进去，但这个问题不会被加入对话历史。

以前你让Claude Code重构一个大模块，干着干着你突然想到一个问题，比如"诶那个测试文件在哪个目录来着"，你一问，Claude停下来回答你，然后上下文窗口里就多了一段完全不相关的对话，它重新开始干活的时候可能就跑偏了。

这就是所谓的上下文污染，用Claude Code时间长的人应该都被坑过。

要不然就是呆呆的，等到整个任务跑完，再去问，但是其实也是污染。

现在打/btw，然后说一个问题，比如我在执行过程中，突然想知道现在我这个项目的抓取流程是啥，我就可以直接敲/btw。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVhuhKYC3MrG3PrCtxvb2N2vRmLlzF1qIygccxblBBYmCHjNdoCiaqtLFx8O2wl6kBQsRic6ibhIE7TjwUAvMZ6cvhSeVsd93WIlk/640?wx_fmt=png&from=appmsg)

你在敲一下空格，就可以直接在后面写问题了，然后发送。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqX8D13sibNhv422YdibKxUDvFZ5HGUc0YFdXZ5vV1ZDTRKyb1wGF6evH0OiajpGX3MIk7tn3p4jHxjRXMwPac7QYQve7VXbwfqicM8/640?wx_fmt=png&from=appmsg)

这个回答，完全不会中断你之前发送的任务，上下两个进程，是纯粹的并行状态。

回答完以后，哦我知道了，那这段就没用了，你就可以按空格或者回车，直接把这一段消除掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUUEUcRiaiaibJ8V1dl1FqGGCovTJk2eXgHrbTQUl7FHKllXC5hlPGdPFFLBOiav5yYN37S2NdcJCiawxk447T5LIiblIHIyen4TryqQ/640?wx_fmt=png&from=appmsg)

之前的Claude的任务还是该干嘛继续干嘛，对话历史里干干净净，跟什么都没发生一样。

而且几乎不费token，因为复用了当前的提示缓存。

究极好用，真的，我现在每个长会话里都会用好几次，属于用了就回不去的那种。

  

**二. /rewind**

/rewind，也就是我开篇提到的按两下Esc，你可以把他理解成撤销或者回退，也就是很多设计软件里面的Ctrl+Z。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXyULug6VibuUnZvLPyd9olHKvzkOOZleVdAibZbqL60xliaHBxZctMQyXkDiaMLsdvUYsbpKjFdlC5Joiaa7odB0ZLJicsLS7AZAZ5A/640?wx_fmt=png&from=appmsg)

这个命令之前就有，但2月的时候，升级了一个关键能力，就是代码和对话可以分别回退。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUaHtqwRlm5caKgwP7t12p9eEtGa4JhB1b2bX6XjMhb1cmYg1RUcXGwdWKiaynKsNlIj1m3zVNEr3ia3b9EkKjbBwy9bAYW9JDo0/640?wx_fmt=png&from=appmsg)

就以前你可能跟Claude说"比如试试这种写法"，改完发现不行，只能整段对话一起回退，连你之前的讨论也没了。

而现在，打/rewind会弹出菜单让你选，是只回退代码还是只回退对话。

比如我现在我开发了一个功能，我觉得不好，想撤销，我就可以先打/rewind，然后把这个会话里面的历史拽出来。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqW6If4GRAEI6a84dgmCsCZIVB40jia2TGEz8Bhic17zrV8Mxvj1mUo3N0aTPFatmaT04RgUib7LeIEHCc7DTu4e1o96w15TxjCQNw/640?wx_fmt=png&from=appmsg)

然后我就点击之前的会话。

就会弹出一个菜单。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWpakG7DNI5SMImIaUdrJibKAGGcM4nalYG6YtMzvZU9gEnZSwHkgHX0M0wgguvRQk4V0ibw2F3xyAj4GPVMMMoveic6fklqk9Qa8/640?wx_fmt=png&from=appmsg)

分别是回退代码和对话、回退对话但保留代码、回退代码但保留对话，在、将从该点开始的对话压缩释放上下文窗口空间。

这就特别适合做实验。

就是让Claude试一种新方案，不行的话，代码回退，对话留着，这样Claude还记得你刚才聊了什么，知道这条路不通，可以直接换方向，不用重新解释一遍需求。

真的，以前经常含泪git reset，我又没那么懂，搞得乱七八糟。

现在/rewind就回来了。

贼好用，推荐大家一定要用。。。

  

**三. /insights**

/insights这个命令是我觉得被严重低估的一个。

它会生成一份HTML报告，分析你过去一个月使用Claude Code的习惯，包括你最常用哪些命令，你有哪些重复性的操作模式，然后给你推荐一些自定义命令和Skills。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWkTkTfsRoag85cteqAD7EKEOI195fxausl8da42CI1Syc80ysKNjEgHBBdDsB65piaR0DWrRWuA2eROqTJCZD4R5hibJ55DOa3U/640?wx_fmt=png&from=appmsg)

其实，就是Claude Code在反向观察你。

你直接打这个命令以后，他就会给你一份做好的本地HTML网页。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVRtEicFJ7NVhfU0C8icxokOpkakvAPnRWngEaibAdia5dDKMONhKsYI5GIMcpiblWme25toSOfdhdSib4s9lBpx4kNwJlEN2RfIMibGA/640?wx_fmt=png&from=appmsg)

做的非常详细。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVsPicL47lick8KS7FlibZ7Pz7nSSWuPqCDSz5nFr8JpT8xhrSETjGaick0Nnbpq4RGl3pOdLDXsz4gLuo1wdNeU2kDGIWNkG3pCZM/640?wx_fmt=png&from=appmsg)

还有翻车现场。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUxOgAkkN0gWV2qwo44SxbOnwPFlFY5CNWA5JCAAlicobAQAjGpDIjfqj4mWlKSEmaMecUevibNYzfBXwLkQafspHic67JATGlFNo/640?wx_fmt=png&from=appmsg)

还推荐我改一下记忆。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXuMAYWC68MC0300LtibT3aXMXfUIsIyELnecJZGz06UImmOz2hqp5qRbJ2Pv5f3VEpbJOWerKYsgFyN1QtxaAwqohvBpaSCuvQ/640?wx_fmt=png&from=appmsg)

建议我怎么用。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWbgC3GLmFDCa2ibuUVo4abfCyo4FBlQk3qw3BfVXzicyZpKhiclicxoumb4KG54pMH0b0qAAJ5XDYTvhAYFdAhub5VsVs5icoibPyibA/640?wx_fmt=png&from=appmsg)

当时还有个抽象的事，他给我改服务器的链接，然后。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVxYicl4FSO4oK0rIA4w969dXpP0oLOtCr937g0GUDJxt22eO3BZw3dLniccsYXYqwZZJMdXxg2hiaouqPX4e1oxRRSmeenaqtsIM/640?wx_fmt=png&from=appmsg)

这种小事都记着了，很有趣。

真的建议大家每个月跑一次/insights，它会让你重新认识自己的一些习惯，非常有意思。

  

**四. /model opusplan**

这个功能我觉得对20刀的Pro订阅用户来说特别重要，就是/model opusplan。

会在需要复杂推理时自动以plan模式使用Claude Opus 4.6，然后切换到Claude Sonnet 4.6进行执行。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWhgIuU8f6ScCpcVrSdUfkEXVmwjyfVKQgCRdckibJT1yXlRgfgLqjaXThvgiaPfmNX1aTUnoguCPOu8woq7QRhTtPJmJj2U1MjY/640?wx_fmt=png&from=appmsg)

而且这是正儿八经的隐藏命令。

你直接/model切换模型，可是没有这个模式的。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVW4hvfL4fCfibLKscwc49MOsbjTribuj9wF7ARXPqWaYZj0loKXNCCgtKSG3Vo0QASkNt8F3a2qiaLZOBMbytOtYxs9sl51CB8ibg/640?wx_fmt=png&from=appmsg)

非常牛逼。

这对每个月20美刀Pro订阅的用户来说简直是福音。

道理很简单，Pro用户的Opus额度是有限的，真的很少，我现在都是Max才够用。

你20刀的Pro会员，全程用Opus写代码，可能干到一半就开始被限速了。但规划和写代码对模型能力的要求是完全不一样的。

规划需要深度思考，需要理解整个项目的架构和各种依赖关系，这种事情Opus确实比Sonnet强很多。

但到了具体写代码的环节，其实一些小的项目，Sonnet真的完全够用了，而且快得多。

如果你是那种确实只开20刀Pro会员的轻度用户，或者确实要省一些钱，那我真的建议开/model opusplan这个，真的，两全其美。

  

**五. /simplify**

这是今年2月底才出的内置Skill，Boris之前发了个帖子介绍说他自己每天都在用。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqU7ibPGMIFhPjbExvic647y1laJRO2RxTeYxRBIXQh9viadu6j8LRVLYLE5B7jzD7MQGSEzaOswN8WkB36HDUXQMwQVo41ZuGygbY/640?wx_fmt=png&from=appmsg)

但是我记得好像之前1月就开源过了，只不过是2月底才集成到Claude code里面去的。

/simplify可以理解成一个三合一的代码审查工具，本质上其实是个Skills。

你输入/simplify之后，Claude Code会同时启动三个平行的Agent，分别从代码复用、代码质量、运行效率三个角度审查你的改动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVZutXNibFVLxl6WTR3YHvMPNmQdfeQw9EbArOwWMsA8IVctB02ZL9kDeJW7NEA3MbibRAQDh4LSBxOLK8poNICOsZJ0ibJ9qhF6g/640?wx_fmt=png&from=appmsg)

然后汇总结果告诉你哪些地方可以优化，我是因为之前跑过了，所以比较干净。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqU1RdWD9ZibVzJFI30kAv1Kib7YxLxywYb4sWIwpJOvkTT6rJu5w3btf3vrFpMGHGgtV3gz0CxAhjL4VrUyk1qPQk4QQDob3A4cc/640?wx_fmt=png&from=appmsg)

以前的/review命令现在几乎感觉已经没用了，我感觉/simplify好用的多。

我现在的习惯是，每次跟Claude code对话了很多轮，写了几个大的功能更新之后，都顺手跑一遍/simplify。

AI写的代码经常会有一些微妙的冗余，多余的import、重复的逻辑、可以用更简洁写法替代的地方，/simplify基本上都能挑出来。

相当于找了三个同事帮你同时review。

还是很香的。

  

**六. /branch**

这个命令以前叫/fork，现在改名成/branch了，打/fork还是能用，会自动跳到/branch。

其实就是可以把当前对话分叉出一个新会话，原来的会话不受影响。

其实就有点像ChatGPT的这个新聊天中的分支。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXoEQh6ia9sf7QdYfCSZa3ic3SoaKwRCT7y7fuy1NGNstpew3gk1ibgZZfOhEOFnOA4XuAzUgWyNghhRPa9uUVqB3aM2HibnuZP6Ng/640?wx_fmt=png&from=appmsg)

这个适合你在跟Claude聊到一半，突然想试另一个方向，但又不想丢掉当前对话进度的时候。

比如Claude刚帮你梳理完一个方案的思路，你想沿着这个思路试两种不同的实现方式，/branch一下，两个会话各走一边，最后挑效果好的那个。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWW6ibJsKzzDibU530aLsa3YMG0KribcNsgGqefaiaPCaibeLZBcicBMI5XbtJIvrM4vFzwoCjsvoCiaD1vJicEMTqEibibnRgkA2skT3kPY/640?wx_fmt=png&from=appmsg)

跟/rewind的区别是，/rewind是回退，/branch是分叉。

你可以理解成，一个是后悔药，一个是平行宇宙。

  

**七. /loop**

/loop也是最近才出的。

可以让Claude定时重复执行某个任务。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXcbFGDFvJl24NpnVKWRiaoY1Te8hYEpn8RvyozcNjWZq3GT0kuR8n7xkZQrAX0Mu3GXSy71iabxmSGdQtFfGAn0x1zfEh3aW5n8/640?wx_fmt=png&from=appmsg)

用法是/loop后面跟时间间隔和你要它做的事情。

比如/loop 5m 检查一下部署状态，它会每五分钟帮你跑一次，不用你自己盯着，默认间隔是10分钟。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqX0OUtlw8ciaeLeJy5yaSictecCLpvyrav84IicFwUzXrmtWxEaeOxxJQQHv5Js5AaJVJIYZiaJn0OmmUibf3ekHxL9So2nNibX6Mx1I/640?wx_fmt=png&from=appmsg)

有点类似于OpenClaw的心跳机制，Claude code以前确实不行。

/loop的好处是结果直接在对话上下文里，Claude可以基于这些结果做判断和后续操作。

然后因为很多任务其实都是短期循环的，所以Claude Code定期任务在创建3天后自动过期。

任务会最后触发一次，然后自我删除，这其实就限制了被遗忘的循环能运行的最长时间。

如果你希望一直运行下去，Claude给到的方式，是使用桌面版。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXXaKFh9X5WFJqzARYggsHvGw8ZtGMjib9gENfib7UtSs4BxNJ0CgiaYVtrt0Ab2ZfBic6xDfyQnTb6MMnNM6XoR7UbDps3YD0uESQ/640?wx_fmt=png&from=appmsg)

  

**八. /remote-control**

**这个功能是今年2月底出的，我觉得是Claude Code比较实用的功能之一。**

**我当时甚至特意写了一篇文章来讲：**

**[Claude Code更新，你终于可以随时随地在手机上Vibe Coding了。](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647680144&idx=1&sn=f42a52a245825f106c9e40225db0a9a5&scene=21#wechat_redirect)**

**你在终端里打/rc，或者打完整的/remote-control，它会生成一个URL。**

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXj6xlS62fZKPuW3kQs7JWib32TibZxJqACYrU45O9cVg0ltkC7icl5UCysib7NBjAwljNH7pohAhz8bKseL8ugeV1ND7w6s2pWyWM/640?wx_fmt=png&from=appmsg)

**你用手机打开这个链接，你的整个Claude Code会话就出现在手机上了。**

**而且是完全同步的，你在手机上发一条指令，终端那边也能看到，你在终端上操作，手机上也会实时更新。**

**两边可以交替使用，对话历史完全一致。**

**代码始终在你的电脑上跑，手机只是一个遥控器，你的文件系统、MCP服务器、项目配置，全部还在本地，手机只是给你提供了一个远程操作的窗口。**

**所以除了方便之外，也非常的安全，很好用。**

**九. /Export**

**这个命令很简单，打/export，当前的整段对话就会被导出成一个Markdown文件。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWrlH1fhc0wKvTjzuyl7JTOOQSZSUxX3fyIuNYwJ4Lhib0QaZRGicIr4ZMW217FbDibia1G8jdDAvP1ib5I31MunNmnwnKibHicSIQO0E/640?wx_fmt=png&from=appmsg)

听起来没什么大不了的对吧，但有的时候你会发现这个功能还挺重要。

Claude Code里很多有价值的东西是在对话过程中产生的。

比如说你跟Claude讨论了半小时某个架构方案，中间有很多来回的推敲和判断，最后达成了一致。

这些讨论如果不保存下来，你后面找起来就非常非常的麻烦了，不如导出，存下来，作为未来的更加详细的context。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqX10WeVribla0UFPNG2ibxAQ32TFQLPYr2elf5bjBGQ79hhoUosiamsic81aUsVLc1M3PKMVsLOj2JNoXXVrd63tYlsYNEGkYbHtE8/640?wx_fmt=png&from=appmsg)

**而且还可以拿去跟Codex协同之类的，比如直接导出，然后扔给Codex，说，你看看Claude Code那个呆逼改了半天没改好，你帮我看看到底错在了哪。**

**有的时候，这种互相导一下，还挺有用的。**

**十. 快捷键**

**除了这些命令之外，其实，还有很多好用的快捷键，大家不知道。**

**所以，我也顺便推几个我用的习惯的，非常好用的快捷键。**

**Ctrl+V可以直接粘贴截图，不需要先保存成文件再拖进去。**

**debug的时候遇到报错，直接截屏粘过去，Claude看图说话。**

**Mac用户注意，这里是Ctrl+V不是Cmd+V。**

**别再傻傻的每次把截图保存到本地再拖进去了。。。**

**Ctrl+J，Mac用户也可以Option+回车，都可以直接实现换行。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVzdEYDv7VYR9OlvzvoFoF5qPxa7sd8v4KZX94Ryc7eKficBru5m1zWSBoVib9U32ibe6T2QKN6vIAAq7rxbKmBL4bmZqDicrmfVuA/640?wx_fmt=png&from=appmsg)

Ctrl+R，可以搜索你之前输入过的所有prompt历史。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqWUpdlKBRtdfSMcONib2dibRe2Lqqp9tQLhUsUrTqNynvhytnGKfLEO00cmJTdGyEGicSEoaAZtD2nFMvBNLYYh8cKc5MAEdu7cS4/640?wx_fmt=jpeg)

Ctrl+U，可以删除整行输入。

大概就是这几个。

  

**写在最后**

写这篇文章的时候我有一个很深的感受，突然有一种感觉。

就是Claude Code的更新速度已经快到了一种让人焦虑的程度。

上面这些功能，有些是三月份刚出的，有些是二月底出的。。。

太快了，在AI加持之下，产品的进化速度，太快了。

因为更新的这些功能，绝大多数还都很有用，让体验大幅增加，所以我还真的比较建议你，可以追一下Claude Code的更新。

他们把更新历史，都是放在这里了：

https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUnZkWmGVxNHRdOJfjhxP9AuYEIfdBoHQYR3twlVFJhyqqMkjwevd0SPSia7vtm6nFW42uXwap4V4IMfjXATx2c619VsyG5usmI/640?wx_fmt=png&from=appmsg)

同时我也比较建议你做三件事。

也可以关注一下Claude Code的开发团队在Twitter上的动态，他们经常会很随意地提到一些新功能，比官方文档还要快。

反正这个东西，大家自己去试吧。

有什么新发现的好用功能，也欢迎来评论区告诉我。

Coding愉快～

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言