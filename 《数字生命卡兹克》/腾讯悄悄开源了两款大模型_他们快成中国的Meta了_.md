     腾讯悄悄开源了两款大模型，他们快成中国的Meta了。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

腾讯悄悄开源了两款大模型，他们快成中国的Meta了。
==========================

原创 数字生命卡兹克 数字生命卡兹克 2024-11-05 16:31 北京

> 原文地址: [https://mp.weixin.qq.com/s/X\_3y8econbXoXgEBFUrh\_g](https://mp.weixin.qq.com/s/X_3y8econbXoXgEBFUrh_g)

今天，人在腾讯混元发布会的现场。

我就眼看着腾讯他们风尘仆仆的从深圳奔赴北京，开了一场非常私密的闭门发布会。  

而整场的核心，就是一个词：

**开源。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURonqcSuv0lpibVbgbUc58ATlCkRXbmZCbFAmQByS2KzHSFR4uEYQrscDZg08mO4Klk3XicwJNaVEeicQ/640?wx_fmt=png&from=appmsg)

而且不藏着掖着，直接开源了他们最好的模型，分别是MoE模型“混元Large”、混元3D大模型“ Hunyuan3D-1.0”。

现在，这些模型已经全面上线huggingface了，可以直接下载。

还有一个即将开源的长文本评测数据集“企鹅卷轴”。

我一个一个说。

**一. 混元Large**

可能是如今，开源出来的，参数最大、效果最好的MoE模型。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURonqcSuv0lpibVbgbUc58ATlia2eEjksFgkjVq8EQwmG1ibibUZ3gGmjbLCnccuGR7cC8eEY3nEESSBMQ/640?wx_fmt=jpeg&from=appmsg)

总参数量389B，激活参数量52B，上下文长度高达256K。实用性拉满。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURonqcSuv0lpibVbgbUc58ATlRPnUWdDMZxsE706YUv6n8xZhpUCYMY2wCExol3AkT4EYYj1VpE5lkw/640?wx_fmt=jpeg&from=appmsg)

要知道，这是MoE，训练起来本身就很麻烦，变量无数，混元能做到这么大，还能开源出来，这事本身就挺值得鼓励的。  

在数据集的跑分上，效果也很好。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoL7ape0GibqrMkm4K88FSfibQlHt8S7DpfQTrja7zSum6swxzeIL1ZxrT6NFT4CxSnREiaoQloaRaag/640?wx_fmt=png&from=appmsg)

在几个维度上，基本全面领先。

可能混元Large有些东西你看着有点懵逼，这里我正好借这个机会，简单科普一下啥是MoE。

**打个比方，模型就是一个巨大的医院，我们每次对话，就像到医院里面去看病。**

正常训练的大模型呢，比如Llama3.1，我们就把它称为第一羊驼医院吧，外面人说这个医院很牛逼，包治百病，但是这个医院里面有个特点。

就是你进去，你会发现只有一个医生坐在那接待。

这个医生是个神医，精通所有科室，牛逼到起飞，能解一切疑难杂症，每个病人来了他都能准确的给你回答。

这个第一羊驼医院的这个医生牛逼是牛逼，但是问题来了，每个病人这个神医都要接待啊，就他一人，压力太大太大了，效率也不咋地。  

那MoE的大模型呢，比如混元Large，我们就把它称为混元人民医院吧。这个医院同样的，名气很不错，包治百病。  

但是当你走进去，这个医院跟第一羊驼医院就呈现出了完全不同的面貌，你第一眼看到的是导诊台。你先要去导诊台挂号，然后它会告诉你去哪个科室看病。  

这就是MoE的特点，它的全称是混合专家模型，拥有路由和专家这个独特的机制。

当病人来到医院时（输入一个问题）：导诊台先判断病人的情况（路由器决定），然后把病人转给最合适的专科医生（选择合适的专家），只有需要的医生会出诊（只激活需要的参数）。

所以，才会有了混元Large的两个参数，总参数量389B，激活参数量52B。也就是这个医院虽然总医生数量有389个那么多，但是其实每次真正看病的医生，只需要52个，就能解决一切问题。  

**这个结果，其实就能看出来MoE的优势了，就是方便、快捷、推理成本低。**  

毕竟Llama3.1 405B那种怪兽，上来就是几百个G起步，这尼玛谁能用的起啊。

**而现在，混元Large，就是开源中，参数最大、性能最好的MoE模型了。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURonqcSuv0lpibVbgbUc58ATlw2LiceUBeRGr2bhRJESuduN5rq0Wia5DficdbBcgRguGumtx7kSZPyrUw/640?wx_fmt=png&from=appmsg)

模型网址在此：https://github.com/Tencent/Hunyuan-Large

**二. Hunyuan3D-1.0**

开源出来的AI 3D大模型，还真的是非常稀缺的。

在我印像中，上一次AI 3D开源有动静，还是TripoAI和StabilityAI联合开源的项目TripoSR，还有StabilityAI自己搞的那个SV3D。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoL7ape0GibqrMkm4K88FSfib7JPFxtZuAiayOXEjyRSXnpkHf4j7AuOG1ItIJ0nuk7iaUWIvoTfxc3qA/640?wx_fmt=png&from=appmsg)

但是这也都是6、7个月前的事了，然后就再无动静。

而这次，腾讯混元终于补上了这块的空白，宣布了他们的AI 3D大模型“ Hunyuan3D-1.0”，开源！

我爱腾讯，我爱混元。

Hunyuan3D-1.0支持文生3D和图生3D，这次开源的版本是两个，一个标准版一个轻量版，轻量版10s就能直接生成一个3D模型。  

我大概部署了一下，跑了跑看了下效果。  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURoL7ape0GibqrMkm4K88FSfibptME4WdGZ0wUtVR0BgGtXPuVRcsBlcN2EdRSZ7CIyUQDcibS6wLHPZA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURoL7ape0GibqrMkm4K88FSfibibHOyNw9fIE67h3rcdzh0NSQRqxX2S8y0ECIiazeUOjHvn2wdJOgSIOQ/640?wx_fmt=gif&from=appmsg)

不吹不黑，这是非常客观且真实的效果。

坦率的讲，离我心中最好的闭源3D大模型TripoAI，肯定还有一些距离，包括但不限于模型质量(特别图生3D时候的背面）、贴图质量、脸部精细度等等。  

但是，如果你不跟最好的TripoAI比，而是跟市面上其他的AI 3D比，那Hunyuan3D-1.0大概可以排在T1.5梯队附近。

但是如果你在开源领域比，那不好意思，Hunyuan3D-1.0就是真正的T0，最屌的，没有之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURonqcSuv0lpibVbgbUc58ATla102EqerCDTd5b13PfBibdQib8xlhAv3lqFEDEgaj3QtU3Y7PJeZfPvA/640?wx_fmt=jpeg&from=appmsg)

而且AI 3D模型，开源后，可以想象的场景就太多了。  

比如微调某一个游戏的AI 3D模型，比如微调一个科幻电影中的AI 3D模型，来进行一个在建模层面，定制化的全面的降本增效。  

去年这个时间点，我就写过：  

**“我极度看好AI 3D，并不是因为这个领域新，而是这玩意真的能切切实实解放内容创作者们的生产力，让他们用更多的精力，花在创作上，保护这些创作者的创作精力。”**

AI 3D对于创作者的意义，就是如此。

我在现场，腾讯混元还送了一个有趣的小玩具，是他们用这个3D大模型3D打印的小手办，还送了一盒丙烯颜料，可以让我们自己DIY，贼好玩。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURonqcSuv0lpibVbgbUc58ATlpHN6CXmLRUJvYVT6vq67bqkDhzVGfL2iajuE04ngLonGApnpXKasibdw/640?wx_fmt=jpeg&from=appmsg)

**希望腾讯这个开源的Hunyuan3D-1.0，能给这个AI 3D的模态，带来一些，不一样的火花。**

网址在此：https://github.com/Tencent/Hunyuan3D-1

**三. 企鹅卷轴**

一个超级有趣的项目。

之前其实主流的评测集有很多了，有MATH这种专门评测数学的，有MMLU这种这种评测各种知识的，但是在长文本的评测上，一直没有一个明确的评测数据集。

大家都在说自己200K、300K、甚至一个亿，但是只字不提自己在长文本上的准确定性。

之前有一个去年11月火起来的大海捞针测试，用来评测长文本的衰减，但是其实也偏民间，在真正评测长文本的能力上，其实还是有点以偏概全。

而这次，混元马上要开源一个关于长文的评测集，命名也挺好玩的，叫“企鹅卷轴”。有一股子游戏道具的感觉。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURonqcSuv0lpibVbgbUc58ATlwOziaYozpicZX7Tnj9aJJkuW1icSgnbuibib838IicicshlKLiciaSjP4ibNctQQ/640?wx_fmt=png&from=appmsg)

这个我觉得还挺有趣的。

马上就会开源出来，后续我可能会基于这个评测集，来对市面上的这些长文本大模型，来做一个评测。  

看看这些大模型的长文本能力，究竟如何。  

**写在最后**

对于每一个愿意开源，让社会、让开源社区，百尺竿头更进一步的公司。

我都永远报以最崇高的敬意，和最大的善意。

穷则独善其身，达则兼济天下。

上一次，腾讯开源了混元DiT，让AI绘图这个领域，有了另一种全新的可能。

而这一次，混元Large、 Hunyuan3D-1.0，算是补上国内开源社区的一大空缺。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURonqcSuv0lpibVbgbUc58ATlJZN801iaYemSFicFdz3kDfAohbUXI3ibG6QGXlgFQV3lhYeJORmg9fJlg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURonqcSuv0lpibVbgbUc58ATllmNG2C7NBt8EarqUYPPg8icSW2r6M0DQlKAzw20FEDGYr0VFLsE0EEg/640?wx_fmt=jpeg&from=appmsg)

一个腾讯混元，一个智谱。

真是国内，最有趣的两家AI公司。

不断为着这开源社区，贡献自己的力量。  

敬礼。  

我永远爱他们。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言