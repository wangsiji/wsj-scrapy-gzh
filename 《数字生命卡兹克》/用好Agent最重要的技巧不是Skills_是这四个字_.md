     用好Agent最重要的技巧不是Skills，是这四个字。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

用好Agent最重要的技巧不是Skills，是这四个字。
============================

原创 数字生命卡兹克 数字生命卡兹克 2026-04-14 10:08 北京

> 原文地址: [https://mp.weixin.qq.com/s/F7w9IWGSrCn2FbIgXoyvnA](https://mp.weixin.qq.com/s/F7w9IWGSrCn2FbIgXoyvnA)

今天这篇文章，来分享一下我自己最近几个月高强度使用Agent之后，我自己总结出来的怎么给Agent设定规则，如何让它Agent更好的工作更聪明的一个非常重要的心得。

就四个字。

约束先行。

就是在你让Agent干任何事情之前，先把规范定好，全局的规矩，项目的规矩，文件夹的规矩。

规矩从上往下穿透，一层套一层，没有规矩的地方，不动手。

就这么简单的一个道理，我真的用了好几个月才真正想明白，然后完整的落地，你可以说我很菜，花了这么久的时间，但是我觉得，我踩过了坑，我还是想把这个经验分享出来。

我为什么觉得这四个字比一切Prompt技巧都重要？得从昨天我的发生的一个很小的小事说起。

事情是这样的。

我这个人有一个毛病，就是完美主义强迫症。

一个东西如果不是井井有条的，我就浑身难受。

这可能跟我是处女座，也是交互设计师，同时还是重度模拟经营玩家有关。

《城市天际线》里路网没规划好我能推倒重来三次，《动物园之星》里动物园分区不合理我能纠结一下午，《双点医院》里如果有一个科室的动线设计得不顺，哪怕医院已经盈利了，我也会拆了重来。

我到现在还是记得我打《戴森球计划》的时候那没日没夜的规划生产线的日子。

我朋友经常说，我就是那种，对秩序有一种近乎偏执的追求。

虽然我很喜欢kk写的那本《失控》，我也赞同混乱中涌现一些智慧，但秩序和规范，可能就是我种在骨子里的东西。

所以昨天下午，当我无意中，发现我的一个Claude Code的工作文件夹里面越来越乱的时候，我是真的坐不住了。

我前几天新建了一个给Claude Code用的专门用来开发Skills的文件夹，结果我昨天打开一看，根目录散了十几个东西。打包文件跟源码混在一起，测试图片随便丢，评估报告的HTML文件找不到归属。

最离谱的是命名，test\_batch是哪个Skill的测试？test\_v2又是谁的v2？我自己做的东西，放了两天我自己都看不出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWbNFI5T9UPHwNpEibIq33s0AP3iaVgsfBF9tezJ0oLvmPBPUOcZHBdmFot49H5zYQCehRqaYARPt2DgMeX7MOxdRQ8ftn0j17IA/640?wx_fmt=png&from=appmsg)

我当时就有点应激了，真的，一时间无语凝噎，只能含泪打开Claude Code让它去给我规整了，然后直接给我定一个规范。

没过一会，他弄完了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXqNnFZHG2tHevL0Ck5C6PrZD3LkvP3UpicQoy5JS6lIBdH7KdBfqZAmzwOfX50jT4x7SQF6Picr2aAaDUSezibvc2Na4Aicg0ymia4/640?wx_fmt=png&from=appmsg)

然后写了一个这个项目级别的CLAUDE.md文档，你可以把这个文档，理解为这就是Claude Code进入到这个文件夹以后，第一个必须要读且要遵守的东西，就是它以后的行为准则。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqW6Q9rsGPJ0KY7tlOH2E0k6S4zaEVESEomOKicCgvI1ogk1o6yj0icibjLO8YIiamrHbGkIEMiaTPrxxclpT6WI5DxYqxcGJLDAymTQ/640?wx_fmt=png&from=appmsg)

规范还是挺全面的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVpaxh3fYxUdvoMlpXwPveVibZfd98HVxxaFyLufAwZQ9ByU3LbyQp8kbvXErmGE1ic6eHWxmiav2icwaweFXd18PH1gxgOgccDWUg/640?wx_fmt=png&from=appmsg)

有了这个CLAUDE.md文件以后，我的这个工作区，就可以不断的进行各种各样的Skills开发和实验了，每个新的Skills，都会自动给我新建一个文件夹，一些实验性的东西会放在\_sandbox里，里面的东西超过一个月就会删除。

再也不会再混乱的要死，而是按照文件目录，管理的仅仅有条。

就这个非常非常小的事情，让我好好反思了一下。

就是，为什么我的Claude Code进到一个新文件夹、或者开一个新项目的时候，自己不会给自己定这个规范呢？一定要我给他定呢？一定要乱七八糟以后我发现了才能去知道收拾那个烂摊子呢？

原因也特别简单，我给Claude Code的顶层约束没有做好。

也就是在最最顶层，无论是打开什么文件都会加载的全局CLAUDE.md文档里面，我并没有定好这一层约束。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXJRxJ92OH6ArguVQNWVpVmqmC2BV82d0MwWsnr8vRWJjxfDiaT0RyFCIicVYu1KOLibKJxXicKfy8GDk0Mswia4QtsMeP0t23O2efQ/640?wx_fmt=png&from=appmsg)

我自己脑子里过去在开发各种各样的项目的时候一直都有这个意识，一般我都会在每个项目里，让它先强制写好文档再进行开发。

但是还有很多是知识管理类的工作，不是开发，比如画图、比如创造skills、比如做研究报告等等，而这些工作，并没有开发类型的管理意识，所以一般都不会留下规范文档，而我自己也没发现。

而对于AI来说，你脑子里知道的东西，如果没有写进文档，就是不存在的。

Agent的短期记忆会丢失，对话框一关全忘了，下次打开，它唯一能看到的就是你留下来的文档和记忆文件。

你的文档里写了什么，是不是足够清晰，直接决定了Agent每一次醒来的时候，是清醒的还是懵的。

OpenClaw很多时候越用越蠢，其实就是他的规范和记忆体系真的就是纯种屎山，这点Hermes agent比它要做的好的多。

所以这也就是我今天想聊的核心，用好Agent的真正核心，其实我真的觉得，就是这一整套约束从上往下穿透的体系。

这里解释一下Claude Code的规则体系，其实包括Codex之类的很多Agent都是这样。

是一层一层叠下来的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUGyiaXS7hEQeq2k18c7niasKIeibFQFTicF2Ga386apDZ4h9ibrE9GTX6u7Ij8YJdYaSiaCEZTocwibed1dCM89wiaRMQdypx3vbqAZDQ/640?wx_fmt=png&from=appmsg)

最顶层，是全局CLAUDE.md。放在用户目录下面，无论你打开什么项目都会加载。这是最高指令和原则，你是谁、你做事的原则、你希望AI用什么方式跟你协作。

第二层，是项目级CLAUDE.md。进入到某个项目文件夹才加载。这是这个项目的宪法，目录结构怎么组织、命名规范是什么、什么文件放哪里。

第三层，是项目里的各种规范文档、设计文档、架构说明。

最底层，是记忆文件。比如Auto Memory啥的，还有对话记录，Claude自己给自己做的笔记。

约束从上往下穿透，一层管一层，一层约束一层。

跟治理公司是一样的，制度在最上面，部门规范在中间，具体操作流程在最下面，你不可能靠CEO每天挨个盯着员工干活，你靠的是制度穿透下去。

这就是「约束先行」的完整含义。

而如何设计这套体系，特别是顶层的制度规范，真的不是一个简单活，开过公司的人相信都能明白我在说啥，那真的是血和泪的教训。

而全局CLAUDE.md，对应的就是这个最高制度。

我的全局CLAUDE.md，其实已经迭代了好多个版本了。

去年最早的时候我也不懂，抄了很多开发大神的所谓的开发规则，然后又不断地往里面迭代经验，搞得后面特别臃肿。后来慢慢意识到适合自己的才是最好的，以及很多经验就不该在这一层，又开始一轮一轮地瘦身。

在今天补了规则之后，现在我的全局CLAUDE.md文档长这样，这里我也完整的给大家展示出来。

    ## 关于我

你会发现，这里面的每一条，其实现在我觉得最好的基于某种形式的约束。

比如第一性原理，是对思考方式的约束，不要因为惯例就照搬，要回到问题本身。

比如反谄媚，是对沟通方式的约束，不要拍马屁，给真实判断。

比如，交互设计原则。我是用户体验出身，所以我对从我手上出去的东西有一个执念，后端可以很复杂，但用户碰到的每一层必须丝滑。这不只是GUI的事，CLI也是交互，Skill也是交互，对话式AI也是交互。

现在这个年代，大家都在vibe coding，但我发现越来越多的人开始不重视用户体验了，很多产品都是能跑起来就行，管你用着爽不爽。

这个我是真的觉得不行。

所以我在全局规范里写了五条我总结的交互设计核心原则。写进去之后Claude做出来的东西确实不一样了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWGsJNVzN5uo4ibLtn5oQqccEiaUw1E8icYdL5SCzhMvcAkw21M40ZlYbfv1SqkqeLKfTw3blcY2ariat6FAy9WyGicrNa8fwv5SniaM/640?wx_fmt=png&from=appmsg)

而约束先行这条，它就两段话，但它解决的也是一个根问题。

    ## 约束先行

以前Agent进到一个新项目，因为特性，所以第一反应总是立刻开始干活。

现在，你定好了约束之后，它的第一反应是先看看有没有规范，没有的话先建规范。

后面那句需要调整规范时先改文档、再改实践不要反过来也很重要。

规则不是死的，但改规则也要走规则的路。

不然Agent为了赶进度绕过约定，事后你想补文档真的都不知道从哪补起。

写到这，我真的忽然觉得，引导Agent，真的，跟我现在管理公司的时候，真的好像没什么两样。

公司你也要部门、要制度、要SOP、要协同，要规矩，要一切，不一个样吗。

而且不只是开公司，很多真正玩模拟经营的人都知道一个道理。

游戏前期最重要的不是赶紧建建建，而是先把路网规划好。

路网一旦规划歪了，后面再怎么优化你都没招，只能一切全部铲了重来，我经历过无数血和泪的教训。

你的CLAUDE.md就是你的路网。

全局CLAUDE.md是城市主干道，项目CLAUDE.md是片区支路，主干道规划好了，支路自然就顺了。

你花一个小时把它写好，你相信我，后面能省无数个小时的返工。

今天分享的这些东西，你要说这算Harness Engineering，那也行，因为Harness本身就是约束。

你要说这不算，就是一些基本的项目管理常识，那也没错。

反正我觉得，名字不重要，最重要的，就是你有没有找到一套让自己跟Agent协作起来舒服的方式。

我有时候觉得吧，我这辈子做的事情其实都是同一件事。

做交互设计的时候，是在给用户行为建约束。

玩模拟经营的时候，是在给虚拟城市建约束。

开公司了，是在给业务和人建约束。

现在跟Agent协作，还是在建约束。

对象变了，方法却是一样的。

先想清楚你要什么，定好规则，然后在规则框架里做出最优解。

这就是最棒的方法。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言