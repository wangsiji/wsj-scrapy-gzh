     这个51K星标的开源神器，让任何Agent都能一键切换所有模型。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

这个51K星标的开源神器，让任何Agent都能一键切换所有模型。
================================

原创 数字生命卡兹克 数字生命卡兹克 2026-04-28 10:08 北京

> 原文地址: [https://mp.weixin.qq.com/s/0XkWwnrUNxc7Pto4SqVcpQ](https://mp.weixin.qq.com/s/0XkWwnrUNxc7Pto4SqVcpQ)

上周我一连发了好几篇模型评测的文章。

特别是上周五，直接化身鸡排哥一天三连发。

然后，很多朋友就在下面问我。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUzibsZiah3mhGHOsvlcHZxcpRIyCahuWAibRf1elyLhduO4GCeRl94pM3iaicaK8Eo3iafHSVl0sUAQwhOK2TtSaySVaLZD39pRs7Gs/640?wx_fmt=png&from=appmsg)

其实说实话，上周一我已经写了一篇超级详细的Claude Code使用教程，里面就有很大的篇幅，写的就是如何在Claude Code里接国产模型这件事。

不过说实话，其实大家都懂，就是那么长的教程文，其实看的后面的真的没几个。

所以，我也觉得，得把这个我自己真的用的非常多也超级好用的小工具，单独拎出来详细的写一篇，分享给大家。

毕竟，这个工具在我看来，他目前确实不仅是Claude Code里接国产模型，也还是其他的各种Agent产品比如OpenClaw、Hermes等等里面，切换模型最方便、最好用的一个。

他就是开源的大名鼎鼎的cc switch，至今在github上已经50k的星标了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVANCxwjFIaoRibRdvHQFexMeEwyoO0gt9rRfQGZ4FrjuT8O5h6yjGP8ic39RV5xPYC5czbwvyG6SSF8A8evqYKBt2U0af5icVmH0/640?wx_fmt=png&from=appmsg)

链接在此：

https://github.com/farion1231/cc-switch

它的工作原理也超级简单，就是直接帮你去改模型配置文件。

因为大家要知道其实要给Claude Code、OpenClaw之类的Agent产品，改你的背后的模型，其实对于非程序出身的绝大多数的普通人来说，是有一点麻烦的。

因为，你是真的要懂一点代码，知道啥叫配置文件，才能去手动修改的。

在Claude code里，这玩意就是settings.json文件。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWblXYbrRlhWMCeTPzeh2ibV0CiaOpUTmyHCN3gicrOqDRuEldw88qoNB5UO35aYt3RJ4jnDTQtHo8kCxvJicuk9I3ny3PDrkHp9Ig/640?wx_fmt=png&from=appmsg)

你只要自己手动改过一次Claude Code的settings.json，你就知道这事到底有多烦。

我到现在还记得，当初GLM-5刚发布的时候，我想试一下，把它接到Claude Code里面去用。

当时看文档，他让我找到Claude Code的settings.json，开始手填各种东西。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVtl1xv9zu7nkMJeqaNPKzSKO14utmWu8sL0lufxO1MES2SKGt1fHXl4Gf9ibpUibOv3DYRRvf5JzN7MPiaPzjUTcotGNJcpObFk4/640?wx_fmt=png&from=appmsg)

base\_url、auth\_token、model name各种字段。。。

我人直接炸了，真的，感觉这事太蠢了。

之前玩小龙虾的时候也是一样，每次出了新模型想试试，我就直接让它自己去给自己改模型。

结果我相信玩过小龙虾的都知道了，小龙虾GG的最常见的原因，基本就是换模型，经常就是模型切着切着，然后自己就崩了。

简直太呆逼了。。。

直到后面我实在忍无可忍，就去问了下Claude，有没有类似的可以便捷切换Agent产品模型的开源项目，当时还真挖到了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUGibQcKqThNibdJcsB9vayMAMwfcdHsquYlsFMCqSRFMebRf3CDxHCQ4x8TSC6TiajNm28ctrqEaHFr953uVYCK7YT2E2zOumXcc/640?wx_fmt=png&from=appmsg)

从那以后，我再也没为切模型这事烦恼过。

回到CC Switch本身。

它是一个桌面App，全平台也就是Windows、Mac、Linux都可以用。

目前一共6个Agent工具，Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw，前几天最新版还把 Hermes也加进来了。基本上你电脑上在跑的这类Agent工具，它都用得上。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXLiblMTpGSibFMO8X8bJTHxia6BkNonEWDhl340rvzqoMAqsvcPI6dIxCWcGSYv4WQoY3383tAjBmvnK7u3COicocxZ7D45uVhnn0/640?wx_fmt=png&from=appmsg)

因为是个纯粹的开源产品，所以信息啥的还是比较安全的，所有相关的数据都存在你本地的一个SQLite数据库里，路径是~/.cc-switch/cc-switch.db。

包括你添加的供应商配置，全局配置，模型定价之类的等等的东西。

你在用他切换供应商的时候，它会从这个数据库里读出对应配置，再帮你写到各家Agent的配置文件里，从而帮你无痛切模型。

直接进入项目的github，下滑找到Assets。

https://github.com/farion1231/cc-switch/releases

根据自己的系统找到对应的文件进行下载安装。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUtaoyqKuFUhVykLeRvm3YNNXicoclYjhUyiccPkLdicNOfD3obWiaBPcYTgpcAiaFg59eMicPs2H8ETGz6dG0cvsGFlg3a9hGZq8uDQ/640?wx_fmt=png&from=appmsg)

比如Mac，我们下载好红框中的文件。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUwheMcTHdzyRIFQvlibvr8rqpMUfV1bu40ybxWI1MiatHicXEqOXILJUlY850ssLicbpYdQl78iaxGjP5NykFSEFr5sUlV3ibx5hq5A/640?wx_fmt=png&from=appmsg)

直接双击运行，然后在App中我们就能看到这个logo和Claude极其相似，但颜色不一样的东西了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVEhJIBnUVBLYr7Jb95lx3V5UvWgoUwkaslmdOLbXYGUDAd1e6UARwQSLYApXB5hDqibeWiaw6gTgZ094cJTibsjOp74sUicOGzZHA/640?wx_fmt=png&from=appmsg)

安装好后，我们主要再来非常非常详细的说说他怎么用。

先来看怎么在Claude Code里接模型。

我们双击打开CC Switch。

在Claude图标下面点击右侧的加号。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXDCUJ8yzotWQV8VEyicMr86abdoe2oBTV1EE210aGcGhvuDktaDZWefAdUh5PdcjSLJmdk3rSlcyawUVAtsiaTb6NgAC6dMwxQ8/640?wx_fmt=png&from=appmsg)

它内置了40+家供应商的预设，智谱、MiMo、DeepSeek、千问、Kimi、MiniMax、DouBaoSeed、阶跃等等等等，反正国内主流的他基本都有。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWQbAmeYx6ykx4cAa1WmoqLz2I8Xjfia9T3UUT5SxfkpBFCcznW0jPrpwYzSM3DSUd4L9eGRiaX7eVsdMibCyDJPBBTR80W6m9VH4/640?wx_fmt=png&from=appmsg)

我们这里以GLM为例，选Zhipu GLM，你想用哪个模型就点哪一家就行。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXfzhzxooLDxwCxHccf3pz7v9EeGdsCWdIkiciacL3UBkEuiaBfhySHRRQgDmUU6PS1j1ibmTtoRvfwx4KOP0rt8yML789cpWLyTXk/640?wx_fmt=png&from=appmsg)

没选供应商的话，所有的配置都是空的。

选好供应商之后，除了API Key，剩下的字段它都帮你预填好了，完全不用你操心。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqW1xU7niassXnhr40EQuFMsJ52VhVdqEQRz006UnnOCavOx6lmdSrgaenqibWXHC5BqibavdsXAGxPpynCbtBhzXWZA9Nxjv5E3YU/640?wx_fmt=jpeg&from=appmsg)

API Key填进去之后，可以下拉看一眼CC Switch自动给你配的模型版本，不喜欢可以改。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVZuQRM3HXcCHhVuplDH0Yz9zwUVVlQz46fwtk1t5e6sKK1DGZAYj4yaGaHz9S63E8oiaj37ZreTIXibm6COPtfqJwccyMRoamb8/640?wx_fmt=png&from=appmsg)

你要是不清楚模型名字的话，就点右上角的获取模型列表。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXt4fvABlAVjWVcxj5L4PbNY3JXAuSMvXsjRqMQAEPbqxibaYicu1iaQEzzIqTlRuJqZXYKIEz1z6ZiaxD37Lib60RiaQlCVyQBB21UY/640?wx_fmt=png&from=appmsg)

然后你就可以看到厂商提供的所有可以调用的模型了。

这里需要注意一下，并不是每个供应商都支持查询列表，不支持的话就需要你手动填一下模型名。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXibKbdGoOj405sBPjWfpDTLXdWUpbCibhlZ5HnxXehwpcqqWkiazZSJJUzCgVSPe2xmmNo6aC1XiapIiagwCDQTM3tNBLdiaAZ9fBv4/640?wx_fmt=png&from=appmsg)

模型修改后，你能看到他给你写的配置文件代码是随你同步的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUIlWPoicp6YOQ5N9zgDE4u5iaPlfN1jrgay3MCXJtkBFnyruf6UGgCDWNSTPAdNslmNOUEZxG4Th6WuFlzhib7mWxiaR7Xox9lBOo/640?wx_fmt=png&from=appmsg)

这里的配置json文件，就是CC Switch会写进Claude code的settings.json里面的内容，但其实我们根本不用管。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXHhCvP33VFMdRDZ6pzPqOMnGVKHXL6vRw2wnfC2dHxUSk8s6Vn92tXRcSiaMUIAAib59icwjD99ibhJl5WdficPC5fZredwiaNDQxr4/640?wx_fmt=png&from=appmsg)

从头到尾我们做的就三步，选供应商、填API Key、选模型就行了。

格式啊兼容啊七七八八的问题，你都不用操心。

最后，点击右下角的保存。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWhYfscCybjKED5Ig2ArxRFbrfmFhE4PzSmAfcZHYSQtbOzWo3OUn0E2ic8OaDMJmQwNwBfUO0dWrhIBxrdias52DJyG59LIugMs/640?wx_fmt=png&from=appmsg)

这样，我们就能在首页的模型列表看见他了，直接点启用，就能在Claude code里用上了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWyLYrux9jnP1bWaw8Yljx39Pvyiamx08k6U49ncBBftlw9mg2NrnL35j14Cra6NlibADcXCvhBx4Bp4LllU8mFXchj0EY67CPBE/640?wx_fmt=png&from=appmsg)

其他家的模型，也可以同样的操作加进来。

甚至切换的时候我们都不用再点开主页面。

直接点击桌面右上方的图标，你想换哪个就点哪个，每个工具下面挂着自己的一套供应商列表，互不干扰。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqURHXvRSwHNWlKiaNmXCPDia2oTAPbeJPekPiaSqb0UMHFWgKc860covKOx9oU9NcdGK4aHf8fkFPphPh6BysvoJ4tnZloxcx2jsI/640?wx_fmt=png&from=appmsg)

这玩意装上以后有一个很爽的点就是，在Claude Code里面，热切换模型的操作变得无敌简单。

热切换，就是你不用重启终端，不用关掉Claude Code当前会话。

比如你正跑着东西，觉得这个模型不太聪明，你只需要等他回复之后，在菜单栏点一下CC Switch的小图标，选一个别的模型，切完就立刻生效。

下一轮对话直接就是新模型在回你了。

但是注意，你千万不要犯傻，非要在模型正在干活的时候切，那...必然会报下面的错。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVvEstt1j5WTHFtEt2d67xDGNhpOAkE92iamt9Chd806Z2ZdqsPoZrt4FUqZwdFlEC0vcOkiaBGVayJBSAL72EdMmj7NkERKAQbc/640?wx_fmt=png&from=appmsg)

这个功能用来做成本管理，贼爽。

因为其实我知道，很多朋友做一些日常任务，还有大项目里的部分小活儿，其实没必要上最贵最强的模型，挂个性价比高的模型，真的又快又便宜。

而做这个成本管理的操作成本，有了他几乎为零了。

但光是切模型这一个功能还只是基操，CC Switch里还做了很多功能。

比如，他还做了个用量追踪，可以快速看到，API key接入的余额，和coding plan的额度。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWYCiaP6XVASVOqwIh6R3RJx4E4wmdMErH8G2HBP9PHFCFhG7flUvmDpwkYTqohoPPiaZZq2hWT6sfxMibpy8bAbia1BmcJKF4moh4/640?wx_fmt=png&from=appmsg)

打开用量配置的操作也不复杂。

在模型列表点击配置用量查询。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUzNcicpgRIVxAibcibLBQPMPHcz2WZ04U6TxqJnwibq2L7DMfeT6FULjAhmgtgNtfAdSy5gfGKIhbkEdCONUganbsnD1KJYjTg2NI/640?wx_fmt=png&from=appmsg)

打开启用用量查询。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWarbKwRHodibmSGnpE4DD88cciavlwZlrQtxU5JZpVRvzDtWCiacXQtqcO1IpsoVphDOCbZ5niaI0wXkM3oMZXeenibcOR0ibTlGOgk/640?wx_fmt=png&from=appmsg)

如果你是走的API，这里点击官方，再点击保存配置。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqV1JZtLh8YC0pYwQKCDcA8HZTUmM95GNlIqvibvZ7M5MgcGlkWUyicFyYgRx74fN8k2RV5wpyeRetcMRYM372PDicus0w7msTIXa8/640?wx_fmt=png&from=appmsg)

如果你是买的token plan的话。这里我们不点官方，而是点token plan。

选择对应的模型供应商，点击保存配置。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWK1zCe2oZ2mgxKIyDxpfeY86ypUaTicjHdd5WtJkvkFZrcv0dVTFOy97msMb48QEHeBib0Dd35JOmXGgOl1NzmQHp78eLeJI6hY/640?wx_fmt=png&from=appmsg)

首页列表就能看到实时的消耗或者余额了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXkduibF6r8xkaU3mEbkXh3yYU2qGu3kKGZdrDq5cib4hL0LYS9G7Ric0xhJkahO4ADPSkPKFJurp8MmEYWvohjHfTj666QjhNoeg/640?wx_fmt=png&from=appmsg)

除了用量，CC Switch还提供了更详细的使用统计，可以更直观地看到每个时间段的成本消耗。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWCibPnBwzXhEqEGQCPzuCZ220ochibuAkvibIVVxaKEoCxw81K7WG7Vx11uSPxefAZ1CpcJCm0H7UyTpD1kdQkI3VPPV5bAGibzLo/640?wx_fmt=png&from=appmsg)

能明显的看到，过去一天我的用量高峰，基本都是下了班以后的凌晨，夜深人静，适合Coding。。。

就这个统计，真的非常的好用。

最后一个，也是一个非常实用的功能，特别适合一些使用多个国产模型搭配使用的用户。

就是，有的时候，你可能会睡前给agent派个大活，让他抓紧我睡觉的时候猛猛干活。

但是呢，你可能会遇到额度突然用完，或者魔法不稳定中断的情况，第二天起床一看，活儿压根没干完。

这种事用CC-Switch的本地代理带故障转移就能解决。

CC-Switch可以在你本地起一个代理服务，拦住你的CLI工具发出去的请求，帮你做API格式转换、故障转移和熔断保护。

翻译成人话就是。

你给同一个工具配了三家Claude Code供应商，比如GLM、MiMo、DeepSeek。

某天，某一家突然宕机了，或者额度用完了，或者请求半天没响应。

CC Switch会自动切到下一家继续跑，无痛迁移，不让你的等待变成白等。

详细的操作我也写在这里了。

我们点进左上角的设置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUFuFzqeiccuQiaKSicmOGAjYPdMEEYejiaDy91Quia3W111DWQfFrsTRenHEWWib27e00k9yPAbM0nm77wDsK9ptYMwsMFyCXjolnnY/640?wx_fmt=png&from=appmsg)

找到路由服务，先打开本地路由的开关，把本地代理服务跑起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWeGR9w19FlDqSnVnwfx2HYFuEpXlfXTUU6ndUjyibguvkibB0dNYj2L26DBjhib2g4Vfeiceeia5gFuPicGocYZqWgDXpkicJ1TGWxAA/640?wx_fmt=png&from=appmsg)

然后在应用路由区域启用Claude路由，把Claude Code的请求接到本地代理上。

这里建议也点开在主页面显示本地路由开关。这样我们在主页就能快速打开或关闭路由。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUicmnZYHickoWoqlSxKZM3KWWJeeoYaWky9XuY4KL37xPbqZDOt9JvViazFmIA1LKD5OJZCmtiaaBv3SwrOjJeDwbYqY24R1r4iafc/640?wx_fmt=png&from=appmsg)

然后我们打开自动故障转移，选择Claude，再点添加供应商，把你要做备用的几家加进队列。

但是这里需要注意，如果你用的是Claude的官方模型，那就别开路由，问题还是有点多的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUEsh5MhlCkcxmTq9mV0tuib9O69H7NkmllYUCHwruMDL6Eh2SjNq7OiazRRsicQhW2ibd0AgcrB9dVRiavbnlOlmLCgzErNEvBcySo/640?wx_fmt=png&from=appmsg)

最后我们可以在首页列表通过拖拽给他们排序。

这样CC Switch会优先列表上面的供应商进行路由，碰到故障就自动往下一家切。每个供应商卡片上会显示一个健康状态徽章。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVib0hiaOPvYW95hgZjb5OwoDp09Byia6NqI66HCVfK68YmT32qgxwmwbR3iaQUvY5dd0ptLyolf8SITX6ULlqoicTJxk9AB8rliauibQ/640?wx_fmt=png&from=appmsg)

要关闭的话，直接在主页把这两个按钮关闭就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWuO0lcGAIFqFAva5jdwzz14iamQf3Po89rbkIZYV7mK19fObM6NXn2bPibN9np9rfJiaPwbyibcynlNKCEiciaDP2qHWsAmbkGJaECI/640?wx_fmt=png&from=appmsg)

除了上面说的这些，CC Switch还有挺多其他功能可以细挖，比如会话管理。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVfklnniae1y0Y31eS3Indp803eZkdJ6iczbgaBEqJf1ZmKCt9NVibtnB8FtbEHwlWrDz38cTmeEImwMMetzibocm6NwwEOe05g4h4/640?wx_fmt=png&from=appmsg)

还有模型配置云同步等等，这里就不一一展开了。

官方提供了一份非常全面的用户手册，写得很详细，地址放在这里，有兴趣的朋友可以去翻翻。

https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/zh/README.md

感谢每一位可以看到这里的朋友。

说实话，这篇文章，我自己读下来是有点枯燥的。

但是作为一篇工具介绍的文章，我也确实写不出什么花来。

这类文章的完读率也一向比较低。

但如果能帮到其中，哪怕一个人。

那我觉得，这篇文章也就有价值了。

希望能对大家有那么一点点用。

剩下的，就交给屏幕前的你自己折腾了。

祝各位，创作愉快。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克，tashi

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言