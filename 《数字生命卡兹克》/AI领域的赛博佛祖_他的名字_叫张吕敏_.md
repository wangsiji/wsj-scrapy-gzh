     AI领域的赛博佛祖，他的名字，叫张吕敏。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI领域的赛博佛祖，他的名字，叫张吕敏。
====================

原创 数字生命卡兹克 数字生命卡兹克 2024-06-04 12:08 天津

> 原文地址: [https://mp.weixin.qq.com/s/ryCWgvtv2ichJLFXK5lKaQ](https://mp.weixin.qq.com/s/ryCWgvtv2ichJLFXK5lKaQ)

前两天，AI绘图圈的赛博佛祖张吕敏，又出手了，发了一个挺牛逼的新项目，叫Omost。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhutqErT3uB5BkWnNcAsibsx1bV0ObY2KxU1LtFWzeSX7289KvrDIic8Q8g/640?wx_fmt=png&from=appmsg)

简而言之，Omost的作用就是，把简单的一句话，扩展成非常牛逼、详细且精准的Prompt，然后挨个画出各种不同的区域，最后合成在一起。  

注意，是**合成，**所以精准可控能力极强。

非常牛逼的自动绘图的Agent，从此，**人人都可以不被所谓的Prompt困扰，普通人用一句话，也能生成很不错的图片**。  

有一个东西跟Omost用的是同样的技术路线，它叫Dalle3。

但是，Dalle3毕竟是OpenAI的玩意，你只能付费氪金用，没有开源。

但是Omost，开源。

我的小伙伴@祁珏瑜第一时间做了一个本地整合包扔给了我，在我玩了2天后，只能感叹一句：

太强了。

比如我想画一个飞船，我就在输入框中直接输入“太空中的未来飞船”，他就会开始哐哐给我写代码。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuYPibooPaxiaHER6ApduPuY3EOYATQpTLib7RK3myq8w4oCjhNVfNhk7fA/640?wx_fmt=png&from=appmsg)

这些代码可能很多朋友看不懂，我翻译成中文的你们就知道了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuW9yFMO8MPibco5YmH5GVV68Mw1J0Mib3nfUuzjy1HYxS9ZCQr4ibPKT6g/640?wx_fmt=png&from=appmsg)

可以理解成把画面拆成了了九份，九宫格，画面中心是什么，画面左上方是什么，右下方是什么，然后挨个去绘制，最后合在一起。

当把所有的代码输出完后，我们直接点渲染就行，一幅飞船图就出来了~  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhukibbYyPD2OT4W8TgYCLfPU1VoMwldlpk5PUuaeKJZWEtkicX3qicHluXQ/640?wx_fmt=png&from=appmsg)

也可以跟Dalle3一样，再进行对话式的区域修改，比如把背景从太空换成海洋等等。

但是目前还没法接入到SD生态里去，大模型也是封装好的。

大语言模型用的是Llama3-8b，绘图模型用的是RealVisXL V4.0。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhu3XpHUbgUF3DtM7wWubKbdB0kPibZ44hffvIFH92tW6VGJQDhSXU6E8Q/640?wx_fmt=png&from=appmsg)

本地有8G显存就能跑起来。

整合包我扔公众号后台了，**对着公众号私信“O”这个英文字母就有**。下载下来解压完后，第一次先运行env.bat，然后再运行run.bat就行了。以后每次打开，就只需要运行一下run.bat。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURqus1mVo8Ya2POResFa7XRrj59Sb8PWkRG1cthxkeu1ZtQERA7sE9ibia8HR8o0EcZmZbqibKAS4Wk1g/640?wx_fmt=jpeg&from=appmsg)

不过Omost毕竟开源了，肯定会有无数大佬，基于Omost上进行魔改，接入到WebUI和ComfyUI也肯定指日可待。  

Omeost强是强，但是让我更感慨，觉得更强的，是Omeost的作者。

**赛博佛祖，张吕敏。**  

可能有些小伙伴对这个人名非常陌生，但是如果我说一个他最著名的开源项目，相信只要是玩AI绘图的，肯定都不会陌生了。

那个项目，叫**ControlNET**。

让AI生图实现多种手段自主可控，一举将SD生态推向了繁荣，让AI绘图进入N多B端工作流，实现全面商业化的始作俑者。说它是SD生态最大的功臣也不为过。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuEFNKvkKW6ufTTUqZ8skvmC373Np2Rg5DwcUzMTsCQnqjrSFvBIj1KQ/640?wx_fmt=png&from=appmsg)

（图片来源：小红书）

这些，全都是ControlNET干的，可以说，ControlNET是AI行业精准控图的爹。

而张吕敏，是ControlNET的爹。  

而张吕敏的工作，除了ControlNET这种爆炸性的项目之外，还有面向普通人的傻瓜且小白的AI绘图产品Fooocus，开源的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuV90U4auvnp37S4UxpYP0lXuvYWAP3JeqGdNuVj61Bz2PheLjAFVXfQ/640?wx_fmt=png&from=appmsg)

后面又发了一个Fordge UI，对原生的SD WebUI推理进行加速等各方面优化。在6G低显存上可以提高60-75%的生成速度，8G显存上可以提高大约 30~45% 的速度。让AI绘图的门槛进一步被拉低。

还有LayerDiffusion，一个可以用AI直接生成原生的带有透明背景的PNG图片的插件，效果比生产完再用PS啥的抠图的效果完美多了，甚至连玻璃的透明效果都能直接生成出来，重点还是：开源的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuAibibTvxZauGoEJxKxzGrtITfS8oKEAVhyCTib39zCiaIAzHoATuqxVYcQ/640?wx_fmt=png&from=appmsg)

IC-Light，可以重新打光，让人物和背景光线完美融合，实现主体与背景迅速统一在同一光源，还是：开源的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuqH3p4sCibGUqCbnAl2oEoLQYTF1zibKtYvzbicxCjf97I8IY0ngrId47w/640?wx_fmt=png&from=appmsg)

等等等等。

他在Github上，有无数的star，而头像，是一个很反差很喜感的英短。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhu6RCuN1dmzCsb1j8nSn8yAwyVmzansvtJt00zd1sZQGw7ZLncQ9ibd0A/640?wx_fmt=png&from=appmsg)

可以说，张吕敏他本人，就是整个AI绘图领域的，赛博佛祖。

本人也非常的年轻，2021年本科毕业于苏州大学，现在在斯坦福大学计算机科学专业读博。

但是他，在18年，可能还没进入大学校园时，就已经在研究人工智能了。

18年，他发了两款AI绘图产品，一个叫Mangacaft，给黑白漫画AI一键上色。一个叫**Style2Paints**，给线稿用AI一键上色。

在19年，我跟Style2Paints，还有过一段很有趣的交集。

那时候在公司，我们设计团队发起了一个项目，是做一个小游戏，类似于王权那种左滑右滑做抉择的。想法很美好，但是现实很骨感，游戏卡牌的插图，我们全得自己画，有整整将近400张。

那时候没有什么AI，真的全得靠人。

我们的几个插画师，不眠不休肝了一两个礼拜，肝出来了近400张线稿，然后我们对着这400张线稿犯了难，毕竟还要上色。。。那是一个比画线稿还恐怖的工作。

我一度觉得这事不该人干，于是就去网上翻，翻到了lks的视频，他推荐了一个很有趣的AI上色工具，就叫：Mangacaft。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuN7ib7mOeo5WpCa3jY6MCnUJBhqib9mJuQkfGgXl08zmhB9K0cdaa0fWA/640?wx_fmt=png&from=appmsg)

我顺着这个产品，找到了张吕敏的Github，找到了他的符合我需求的另一款线稿AI上色工具：**Style2Paints**。

然后用这个产品，就花了几天时间，帮我直接搞定了属于我的所有的上色任务，然后，开开心心的摸了很多天的鱼。

那时候，我还不知道他叫张吕敏，那个时候，我也更是想象不到，6年后的今天，全世界都知道了他的名字，他成了我们心中的，神。

这六年，他的初心，好像也从来没有变过。  

六年前，他的Mangacaft和Style2Paints就是在线服务免费给大家用。

而Mangacaft，收益很凄惨。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhu7fL2NicFx1hB87QDW8za1COM0j7DBJwHibuhEYBh3Vgllib5kia0A6BKfQ/640?wx_fmt=png&from=appmsg)

他也有过迷茫。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuvMFdtb5pruOSAC25FxKnMrdHsKUrBMiccZqBRicurwuGfhIWqfZicCYfw/640?wx_fmt=png&from=appmsg)

也有抓耳挠腮的时候。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhuLPjHm2YIhcrib6msuJUnic2DJLXNzDv0ibIhYC4k7OuYEjjp29WHlib3Iw/640?wx_fmt=png&from=appmsg)

网站关了开，开了关，但是还是一直在开心的做着自己喜欢的事情。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhu0yTPib2VeUwjpjvBJLccKj3z1JM0FZqwliaDxWOOQhx3UXSDIltUy8IQ/640?wx_fmt=png&from=appmsg)

就这样，一直做，一直做。  

然后，他做出了ControlNET、做出了LayerDiffusion、IC-Light、Fooocus，也做出了Omost。

现在，他成了张吕敏，成了我们心中的，赛博佛祖。

18年，24年。  

我非常佩服他，更是非常的羡慕他，他能做到那么多人都做不到的事，把心中的美好带给所有人，那一股子初心和激情，我非常的羡慕。  

我也想成为那样的人，但是也清楚，我实在太菜了。所以也只能做一点，我自己力所能及的小事，去尽可能的追逐他们的背影吧。

最后，我想用张吕敏曾经转发过的一句话做结尾，那句话，最近也挺火。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpztjwXriaIPCeCwwV8iayZhurzHZr9iaI5YdsCw0dhGvukhRS4vUPicung8sqxEch0Vmze3jiczn8dukA/640?wx_fmt=png&from=appmsg)

**为天地立心，为生民立命，为往圣继绝学，为万世开太平。**

我想，这就是，最大的意义吧。

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言