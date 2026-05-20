     半个AI圈期待的Midjourney角色一致性首发评测 - 再入迷梦 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

半个AI圈期待的Midjourney角色一致性首发评测 - 再入迷梦
==================================

原创 数字生命卡兹克 数字生命卡兹克 2024-03-12 15:13 天津

> 原文地址: [https://mp.weixin.qq.com/s/KQU3uxXSOtizLn3oa1tPqA](https://mp.weixin.qq.com/s/KQU3uxXSOtizLn3oa1tPqA)

在MJ一鸽再鸽，鸽了N次之后，今天早上6点，他们终于决定把他们万众期待的功能放出来了。  

角色一致性。同步支持MJ V6和Niji V6。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6ibmY6WsMRNVX4UUJYHT829VbO6e6BddeEOHQniaiaSkZlY51yU6BqSYIg/640?wx_fmt=png&from=appmsg)

跟之前的风格一致性--sref命名基本一致，\--cref。

坦率的讲，风格一致性、角色一致性、场景一致性，是我觉得三个能真正进入生产管线的极度重要的可控性功能。其实现难度由低到高。

毕竟，你真要用MJ去带故事带场景的东西，这些一致性肯定是要的，要不然疯狂跳戏，那观感肯定奇差无比，这个妹子一会白头发一会红头发，一会圆脸一会方脸，你都怀疑你在看个什么异世界故事。  

之前有朋友也在群里疯狂吐槽过：

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6Jecfx91YHUaFUqSYOVaAVoSxLP3AL53xux1eK4mULibQcFMfQXfILUQ/640?wx_fmt=jpeg&from=appmsg)

风格一致性MJ有sref命令去做很好的解决了，而角色一致性，今早也终于放出来了，讲道理，他可以节省一半的工期了hhhhh。

\--cref背后参数--cw的值可以从0设到100, --cw 100是默认参数，此时会参考原图的脸部、头发和衣服，但是相应的，会非常的不吃Prompt。-- cw 0的时候，就只会参考脸部，大概就约等于一个换脸。

最近《沙丘2》挺火，上个小公主给大家当一下case。

原图是这样的：  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6Oh0SZeaIxhNKGDrCSs8wVe1EiatCAQicTxvsaTibdEgKHhRTw0u2cC5vA/640?wx_fmt=jpeg&from=appmsg)

使用--cref之后。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6urQfo8Q3FvuWTauoVPa87nZu7qXtSJUuBZWx3HBywibTgS1wyomIAxg/640?wx_fmt=jpeg&from=appmsg)

还是能明显看出区别的。--cw 100的时候，人物的头饰、衣服都是大差不差的；--cw 0的时候，发型和衣服就全变了。

至于用法，我比较习惯使用MJ的网页版，体验真不是好的一点半点，网址在此：https://alpha.midjourney.com/

登进去之后，传一张图片，就会发现图片的右下角有一个小icon，鼠标hover上去以后就能看到出现了3个icon，最左边那个小人的icon就是把这张图片当做角色参考，中间那个链接icon就是作为风格参考，最右边那个就是仅作为图片prompt，就是传统意义上的图生图。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6VbocyX128qmY8Xt6KSaRPeT2nZOibiaRlyOtoUxRggWFicaeFD3DlicyUA/640?wx_fmt=png&from=appmsg)

当然，你也可以按住shift，点这三个按钮，就能把这三个全部点亮，形成cref + sref + 图片prompt的超级组合拳。。。 

官方对于角色一致性，也给了一些简单的小Tips。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6EBQUmLofdwmLGvDwUic4Q5LORZT3tKkcDqbGicUl5TNP9HarlAFGUgIQ/640?wx_fmt=png&from=appmsg)

真人和照片肯定是最难的，毕竟需要关注的细节太多，而且"神韵"是一个非常玄学的东西，有时候你就会觉得明明五官是一样的，但是为啥就是不像。。  

而用在2D和3D角色上，那肯定就会好很多了，毕竟只需要抓住几个主要特征就行，所以从这个功能本身上看，也能猜到，Niji V6的表现，肯定会比MJ V6要好很多。

所以我会分成真人、2D&3D人物、动物，这三个维度，来做一些case，讲一些我摸索到的小技巧，让大家来直观的感受一下，他的用法和未来的可能性。  

  

**一. 真人**  

其实说实话，我跑了N多case，用真人照片直接去做参考的话，效果确实不咋地，只能保证相对一致性，但是绝对的完全一模一样，是不可能的。  

官方自己也非常明白：  

It's not designed for real people / photos

我放几个真人照片做参考的case，你们看一下相似度，就肯定明白了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6vhZOH9POyBibv9mFMFDy8H46oWVC0F2z7HLsvtSXib6qk57WfiaU1AWqw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6DcIuriardCwVQ5xKVLkVCDclfH4mdDVttDODrPpTe8IflW0VXXkT1SA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6OSGdczlUy37lic8LYGElcLIc7aAocyKw8y1MHwzroExQuic1V50A6B0A/640?wx_fmt=jpeg&from=appmsg)

属于是个人看了都想刀人的程度。  

但是如果直接用MJ生成的图去做参考，一致性会好一些，但是也就仅仅好一些了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6XORGVBJOS9wc50hCIZt6wOCGZ7vibNOIanEazp4tLkiaqxPNUPvoFTew/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK62V6dtD4gsBD4XDwdibM6h2n0XQ28omPGsy1FYa4IPETM6HIIyJAUD4Q/640?wx_fmt=jpeg&from=appmsg)

当然，也有很好玩的用法，2D转真人。比如我扔进去了一个我用Niji跑的二次元女生，然后转头用MJ V6去跑"穿着皮衣，在舞台中弹着吉他"的场景，效果意外的还不错。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6R5dyQ82XgNmxCLo3kcQbkJ88em6RZzxmrVWRlbibLwb7xStWxKRSzPQ/640?wx_fmt=jpeg&from=appmsg)

在真人这块，整体上，我觉得作用是有比没有好，能降低过去很多Roll图的时间，但是达不到所谓的完美或者摄影级的水准，但是这毕竟只是第一步，真人的一致性肯定是最难的，等待MJ的后续优化。

  

**二. 2D&3D**

当不跑真人，而是去跑2D和3D角色的时候，这就让我惊喜多了。

Niji 6 + cref + sref的组合拳，是我认为目前的最优解。

prompt写法也很简单，角色描述+角色动作+cref。  

比如我随手跑了一个人造人18但是换了衣服，再把提示词删了直接去用图片提示，可以看到角色一致性得到完美的保持，不管是面部、发型、颜色、衣服，甚至还有身材，都能完美还原...

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK68PhxaM572MWWLxqicRY1vKq3ay1FZGdYSRicUzUHNMgvtK1xxrNJ2mQw/640?wx_fmt=jpeg&from=appmsg)

如果换成--cw 0，再写一个运动服。可以看到衣服全变了，但是面部和头发都不变，用吉川的话说：头发才是二次元的本体。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6qjXfcDDOegkUN7neibibOMJTmG8hTvMRKptqj3GKWgTosSU9jaBkXZ5w/640?wx_fmt=jpeg&from=appmsg)

再比如，用我之前的橙头发妹子，直接跑一个穿皮衣弹吉他的图，  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6RlWZH55ticxWVHlCkFibhkwxH3xYozdfKnmXs4KNWLHJianRssbticmTYg/640?wx_fmt=jpeg&from=appmsg)

当然，除了弹吉他之外，她还可以做很多事情。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6KAzEEZpTrFUcE19SIibK0ibN0XVyiaKz3t65ZbawibocicAuEt0zwgj87Iw/640?wx_fmt=jpeg&from=appmsg)

而做3D角色也是同理，比如经典的泡泡玛特风格的IP。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6wCfXo4VWCibJx4aKEibMiafJGic0gDof9fibbfL9fnBOlYY6pgBbLPpxicHg/640?wx_fmt=jpeg&from=appmsg)

  

**三. 动物**

动物的一致性，比我想象的要好很多，因为我一直以为MJ的角色性，真就只有人物的，但是随手试了一下动物，居然意外的还不错。  

比如用坤哥的《山海奇镜》里面的狼当图片提示，让它来抓兔子。

原图是这样的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6dbmZDQQzNm9x33vwB8bXogRGKxBLXzlnV7hO1fMTQMIc3D7VkjQw8w/640?wx_fmt=jpeg&from=appmsg)  

让它去抓兔子以后，就意外的，非常好。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6Mf1iaKsM74LJfmr7JMOyF8LmCRNWkX8B2h8ic9WyaCrzw7EVhrwTVHRw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6vhLyJJ3MKpkRrHWicBFwWMNJ27DicolePSEYY3BrhvBQ1uYzPmWTgM1g/640?wx_fmt=png&from=appmsg)

比如用朋友的狗当prompt，也还原的差不多。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6qjoj5jczH86maPBTk7KMmK7otBzpfF8IscRQYET1BgSQE4rrxrtCZw/640?wx_fmt=jpeg&from=appmsg)

还有怪物，也很Nice。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURplD7z0JWc7KkkCTzIgAdK6wcjTfuI7IuvFVv8BMqVON2mZMj0OenMY9rQ8UIJeAWDnDDSA43gP7A/640?wx_fmt=jpeg&from=appmsg)

这种精度，去做个绘本，肯定是没问题了~  

  

**写在最后**

在角色一致性上，MJ终于踏出了坚实的一步。  

首当其冲的，肯定是所有非真人领域，比如游戏、漫画、动漫、绘本等等。

MJ的角色一致性精度，是一个很棒的杀器。  

可能他还达不到绝对一致性得标准，但是对于70~80%的工作，我觉得是有巨幅的效率提升的。  

同时它也不需要像SD一样，去高门槛、高成本的训练自己的LoRA，只需要一张图。

就完事了。

高可用性、极佳的用户体验、不错的效果。  

我觉得足够它在商业领域和专业工作流中。

有他的，一席之地。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。******

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言