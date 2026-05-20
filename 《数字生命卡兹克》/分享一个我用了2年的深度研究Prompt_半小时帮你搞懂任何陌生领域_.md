     分享一个我用了2年的深度研究Prompt，半小时帮你搞懂任何陌生领域。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

分享一个我用了2年的深度研究Prompt，半小时帮你搞懂任何陌生领域。
===================================

原创 数字生命卡兹克 数字生命卡兹克 2026-04-13 10:08 北京

> 原文地址: [https://mp.weixin.qq.com/s/Y\_uRMYBmdLWUPnz\_ac7jWA](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA)

前两天办完大会，然后昨天周末跟一个朋友吃饭，聊着聊着他突然放下筷子看着我说了一句，不是哥们，你怎么什么都懂一点？

我说我不懂啊，我懂个屁。

他说怎么感觉啥你都能聊一聊，什么Harness、什么Claude Code、什么心理学、什么杀戮尖塔2、什么克苏鲁神话，你怎么还有时间玩宝可梦popakia，你到底一天有多少个小时？

我当时就愣了一下。

因为坦率的说，聊天吹牛逼归吹牛逼，我真的没觉得自己什么都懂，我只是对很多东西好奇，然后有一套办法能让我很快地把一个陌生的东西摸个七七八八。

他又问，什么办法？

我说，一个我自己搞的研究框架，加上AI，半小时能出一份一两万字的研究报告，能帮你贼迅速的入门。

他筷子又放下了。

然后他说，“你把这个东西写出来”。

于是就有了今天这篇文章。。。

我也不知道对所有人有没有用，但这确实是我自己三年前还在金融行业的时候，研究公司和行业用的方法论，然后后面AI来了，各种各样的深度研究也出来了，我自己又把这套方法论稍微迭代了一下，封装成了给很多AI的深度研究功能用的Prompt，能适用于我研究任何东西，说实话，我觉得这就是这两年用得最顺手的东西之一。

不敢说这玩意出来的研究有多透彻，但至少能让我快速建立起一个相当完整的认知框架，然后在这个框架上再去深挖。

这个方法论，我之前把它称为。

横纵分析法。

我先说说这玩意是个什么东西。

其实特别简单，就两条轴。

第一条轴，纵向。就是沿着时间线，把一个东西从诞生到现在的完整故事给还原出来。它怎么来的？谁做的？中间经历了什么？为什么在某个节点突然爆发了，或者突然掉头了？你把这条线理清楚，你就能理解一个东西大概的历史与因果。

第二条轴，横向。就是在当下这个时间点，把它跟同赛道的其他东西放在一起比。它跟竞品比有什么不同？用户为什么选它不选别的？它在整个赛道里是什么位置？你把这个切面看清楚，你就能理解一个东西的位置和差异。

然后最关键的一步，是把这两条轴交叉起来看。

纵向告诉你它是怎么走到今天的，横向告诉你它今天站在哪。两条轴一交叉，你就能看到一些单独看任何一条轴都看不到的东西。比如它今天的某个优势，其实是三年前一个不起眼的决策慢慢积累出来的。比如它今天的某个短板，其实是当初一个合理的选择变成了包袱。

纵向追时间深度，横向追同期广度，最后交汇出判断。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUu5RbHcthicLhybbJjI0Nrxp7ibZ2LzdAfju1lA8iaMSdjmPkp0UJFxmwy4Sdvllq7dGyNWwLyLic5AjEeqSLFDaGNXXibsXdRTpqU/640?wx_fmt=png&from=appmsg)

就这么简单。

也是我这两年用的最顺手的一套方法。

这个方法其实脱胎于社会科学和语言学的一些经典研究视角。

语言学里面有一个非常经典的分析维度，是索绪尔提出来的，叫历时分析和共时分析。

就是你要研究一个东西，可以从两个维度入手，一个维度是时间维度，看它从过去到现在是怎么一步步演变过来的，另一个维度是当下维度，看它在某一个时间点上，处在一个什么样的系统和比较关系里。

社会科学里面也有类似的研究视角，叫纵向研究和横截面研究。纵向就是追踪一个对象的变化轨迹，横截面就是在某个时间点上观察它的截面状态，并做横向对比。

我就是把这些学术界已经用很久的研究视角抽离一下，再结合了一些商业和竞争战略分析的思路，搞成了一套用AI来跑的通用研究框架。

现在有Prompt版本和Skill版本。

也全部开源在我的Github仓库了：

https://github.com/KKKKhazix/khazix-skills

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXE1hZTaCPz9k9fvX0icFs3IlibsaeK5w5ozhPyqwyf0op67Q1sFqia0ibXZ0xesxhLibuh2IbpibN0SxiblTh12Tgn0lsQzfmgGdicpLo/640?wx_fmt=png&from=appmsg)

Prompt版本配合一些有深度研究功能的AI效果会特别好，比如ChatGPT的DeepResearch、Claude的深度研究、豆包的专家模式、DeepSeek的专家模式啥的，都行，并且我特意优化了行文风格，使用了部分卡兹克写作skill的能力，保证这份报告出来以后，你能读的下去，而不是如果嚼难啃的天书一般。。。

我把Prompt放在这里，有需要的朋友直接复制，也可以去Github仓库自取：

    # 横纵分析法 Deep Research Prompt

使用方法特别简单，把那个研究对象等式后面那个词组，直接改成你想要的研究对象就行。

比如最近很火的hermes agent、比如Harness、比如CLI、比如Anthropic对于SaaS股有什么冲击等等等等。

甚至你想研究《洛克王国世界》、《王者荣耀世界》、伊朗跟美国的战事、川普的反复无常等等等等。

什么都可以。

我用最近最火的Harness+Claude的深度研究来举个例子吧。

我直接把那个Prompt改了一下，等式里面换成了Harness，然后打开了Claude的深度研究模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqV8iaY8ZrDhSO2DJiaACxmwW8ticPGnPEoO1zWKoibFxyKNNbbgyibjnqEEayicCXnnEw7V5P576gpiagoBGyUHMYA4AHauRlF9pjnvFs/640?wx_fmt=png&from=appmsg)

直接发送。

然后Claude会跟我确认一下Harness到底是个什么东西，我就补充了一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXPC9d3ibicGD8nsZicNRrrboNAKLHWwwQOAmBzica8JwtXez6YWL91U6W34XSficRt0ejJXhlNVY7ldb8YWaZJVJxbAOA1cOAa8ia2k/640?wx_fmt=png&from=appmsg)

然后就直接开始了。

13分钟以后，这篇关于Harness的研究报告就写好了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUvufs4gOeUvk2HjMpVstdX33KfbYOl26jDjV538a9HYfXDf1kEkXyVEkBvFv3CahXxRsYBbZTR8rBlhCiceJjWR0ka5RhQReibg/640?wx_fmt=png&from=appmsg)

可以看看效果，纵向分析我觉得写的还不错，历史给你拉的非常清楚，什么时候诞生的，什么时候爆发的，有哪些关键节点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqV7R3D5qoT8VAyUEA9HbnW27bIOHNUYiccf7HBwjtibPAUEHGwSFwhTjM1t0icFgPsAmibA2rkic6ibPpiaQYHnSNgahMVvx2LoicvQbIA/640?wx_fmt=png&from=appmsg)

为什么是这个时间点爆发也非常的有道理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVY9xiauAwz6azsoNic7VI31acPAiaBGj5ce4NSWTaaFiaR1yNma1BdWgeUHNsW5OcVGokQf9Fj4fymT82VvfWPuXJZibflw95ViaUGI/640?wx_fmt=png&from=appmsg)

而在横向研究上，对比的是Prompt Engineering、Context Engineering和Agent Engineering。

我相信任何一个懂Agent的，都不会质疑它对比的不专业对吧，你可以非常快速的理清跟一些同类概念的区别。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqV5yAbiciaopVTgpcxS3mvgRic54m9c6ajQ1LB0LGmAtevelRBKjdbOspNA3go4hJhdFchU6BX4U2icJwYHLlL0engKYrPl6McLZRg/640?wx_fmt=png&from=appmsg)

还有最后的未来演进方向。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVPmgaseia5saOecmlPoHzntTrTjykPfxgOOuHOq1VL3KAticQPgibNbrgSQwsKtVs3oMqTs8VcZsIBqrIsOqBF4l8EBONT5icJvG8/640?wx_fmt=png&from=appmsg)

这整篇报告大概一万字，相信我，如果你是对Harness感到好奇，想最快速度尽可能全面的了解关于它的一切，这篇研究报告，几乎比你看到的大多数的汇总文章，都要好。

全面且易读。

研究对象可以是一个产品，比如Cursor、Claude Code、Hermes Agent。可以是一个公司，比如Anthropic、字节跳动。可以是一个技术概念，比如MCP协议、RAG。甚至可以是一个人，比如某个行业里的关键人物。

Prompt会根据研究对象的类型，自动调整纵向和横向分析的侧重点。研究产品就重点看版本迭代和功能对比，研究公司就重点看融资历程和商业模式，研究人物就重点看职业轨迹和同领域人物对比。

如果你平时喜欢用用Cowork、Claude Code或者Codex等等Agent啥的，我还把这个方法论做成了一个Skill，叫hv-analysis，也放在我的Github仓库里开源了。

装上之后你直接跟Agent说「帮我研究一下xxx」，它就会按照横纵分析法的框架去做。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVHmxicAzlhozDEcNUzAf4e3nHRHWy0fNwkH2HLRibX4lVNOQHX4FILxO46sWl2cAs8MAdfEOUtgLPydggh9h6moOcWW2ia1lP024/640?wx_fmt=png&from=appmsg)

而且这个Skill版本还会自动联网搜索信息、还包了arxiv的API，会在你研究一些学术问题的时候自主去查询论文，最后还会生成一份排版好的PDF研究报告，文风也会更易读，比Prompt版本更自由丰富一些。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVsRd2tTh2otEqT1VF49xn9Kr5ZrD9TvyuUPHLcMAmRVSV2q15mGra70MgFJKLEyahhU05GPjAhsXOFqribNibOGYmk0xG3ugxeI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWK8AiaQVsFvA4T21Upnl0oric0At4wbeuJ5nyZfCArgVL0rc1tSA8mbXicSZcHicqvl1HLw7rI7JKib4zfGHmTCxBZhaZVxHjY9cDE/640?wx_fmt=png&from=appmsg)

当然，我得坦诚的说一下这个方法的局限。

它不是万能的。

它能帮你在很短的时间内建立一个相当完整的认知框架，但它替代不了真正深入的、亲自下场的研究。

并且AI搜集到的信息虽然现在AI的模型幻觉已经非常非常低了，但是还是可能会出现不准确的情况。

所以你不能拿到AI产出的报告就直接当结论用，它更像是一个你对这个领域研究的起点，帮你快速建立地图，然后你再根据这个地图去做更深入的探索。

另外一个问题是，AI生成的报告质量跟你用的模型和工具有很大关系。用支持DeepResearch或者深度研究的工具效果通常比较好，因为它们会真的去联网搜索、验证很多信息，一次任务通常都在10分钟以上。

但是如果你只能用支持普通联网搜索的AI工具，一次就不到一分钟，那效果可能确实会大打折扣。

我自己的做法是，拿到报告之后，先快速通读一遍建立框架，然后针对我觉得有疑问的点或者特别感兴趣的点，再深入去搜更多资料。

这个就是横纵分析法生成的AI报告 + 自己深挖的组合，比从零开始的效率高太多了。

毕竟这年头，在已经有了AI的情况下，真的没必要硬生生自己去挖，那真的是没苦硬吃。

我有时候觉得，这个时代做研究，真正稀缺的不再是信息，而是你对这个世界有多好奇。

其实你要说我真的有多博学或者多专业吗，那肯定也不是，我只是对这个世界，多了一点点的好奇而已。

就是脑子里随时随地会冒出来一堆问题。

这个东西是怎么来的？为什么是现在出现的？它跟那个东西是什么关系？做这件事的人之前在干嘛？这些问题如果我想到的时候，没有答案，我就真的难受，我不知道大家有没有这种感觉，就是那一种，此刻、立刻，我就要得到答案的感觉。

信息已经像洪水一样了，AI让你获取信息的成本趋近于零。

但你要问什么问题、从什么角度去看、怎么把散落的信息组织成有意义的判断，这些东西AI帮不了你，或者说，AI只能在你给出方向之后帮你执行，但方向本身得你自己定。

横纵分析法其实就是我给自己定的一个提问框架。每次面对一个陌生的东西，我不需要临时想我应该从哪几个角度去了解它，这个框架已经帮我想好了。

纵向追时间，横向追空间，最后交汇出判断，三步走完，认知框架就搭起来了。

它让我不用再跟几年前一样，花三天时间去搜集信息，现在，半小时就能把框架搭起来，然后把剩下的时间花在真正有意思的地方，就是看着这些信息慢慢拼成一幅完整的图，然后突然「啊，原来是这样」的那个啊哈的瞬间。

那个瞬间太爽了。

说实话我也不确定这个方法适合每个人。

但如果你也是那种，脑子里经常冒出一堆问题，又嫌搜集信息太慢的人，可以试试。

古希腊人说，哲学始于惊奇。

我觉得吧，研究也是，始于你对一个东西真的好奇，方法和工具都是后面的事，好奇心在前面。

没有好奇心，有再好的方法论也是摆设。

有了好奇心，哪怕方法笨一点，你也总会找到答案的。

只不过现在，找答案这件事，确实比以前快多了。

快到你可以对更多的事情。

保持好奇。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言