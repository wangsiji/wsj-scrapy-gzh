     当我用AI去复活文物 - 只想再看一眼千年前的它们 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

当我用AI去复活文物 - 只想再看一眼千年前的它们
=========================

原创 数字生命卡兹克 数字生命卡兹克 2024-04-08 21:32 天津

> 原文地址: [https://mp.weixin.qq.com/s/Q5mOUZ0N-eE5GvOCUrc7lQ](https://mp.weixin.qq.com/s/Q5mOUZ0N-eE5GvOCUrc7lQ)

好久不见。  

这是我写公众号以来，第一次断更了将近一周。

主要原因是一直在做一个新的片子，做了很久，真的很久。不眠不休肝了快10天了。

当然，过程中又有无数新的经验和工作流，可以分享。

大的工作流我觉得可以等片子放出来后，后续再来详细拆解。

但是今天，我觉得可以先拎一个案例和技巧出来写，是一个非常好玩的案例。

**用AI，复活文物。**

我说的复活文物，不是用ControlNET啥的把文物照片一笔一画画出来。而是真的在此基础上，给他一个新的形象。

因为文物，很多都是从墓葬里发掘出来的，这些东西，大部分都是陪葬品，它的属性，也就是：器具，或艺术品。

这些器具和艺术品，古人在创作他们的时候，一定都有参考物，不一定是现在生活中真实存在的，但大概率也存在与口口相传的故事里。

而这次我们想要做的，就是去把那些参照物，做出来，来看看他们用AI做出来，到底是什么样子。

我用荆州博物馆的漆木彩绘蟾座凤鸟羽人举例。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg299KTjia1TxxBt0fcq6ZjwxfILXHjJ4IOVniaIniaCOJykN0E3iasXrG8pA/640?wx_fmt=png&from=appmsg)

这是一件非常非常牛逼且著名的藏品。

> 时代：战国（公元前475—221年）
> 
> 来源：天星观二号楚墓出土
> 
> 级别：国家一级文物
> 
> 羽人是楚地巫风最盛时代最具创意的木雕作品。由上部羽人、中部凤鸟和下部蟾蜍状底座三部分组成，其中羽人为人鸟合体，立于凤鸟之上，造型奇特，形象优美，制作精致。羽人被当作天上的神灵，蟾蜍代表月亮之精，凤鸟是飞翔于天地之间的神鸟，羽人又是变化莫测的神人，三者合一，寄托楚人遨游九天，羽化成仙的愿望。

最开始，我们在还原的时候，愁破了脑袋。  

上部羽人、中部凤鸟、下部蟾蜍。  

我不得不佩服古人的想象力，真的。有一种别致的美感。  

但是还原的时候，真的愁。

我们最开始还原的时候，本能的还是上了SD。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2zxjicNCYPIAZRiaxiapnrxlIpukVLLBdJNTzNBnP5TAoL46loyoPZ8iavw/640?wx_fmt=png&from=appmsg)

这个东西，它就很奇怪....  

三部分，你直接让AI上，它真的很难理解。  

然后海辛决定，上辛苦活。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg24MAj7HOB5ewibrf5wFBh0h8qQw6micnaA48rkHfUmiapR0YMW8uyib9k0Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2KM4m24UqMaKtOEZEjSB2PYWicIgqdJsV4HJP9khwqfNC7aO1Ntnsuqg/640?wx_fmt=png&from=appmsg)

一部分一部分的重绘，然后，再拼起来。

我隔着屏幕都能感受到海辛的崩溃= =  

在十几分钟之后。  

海辛给我发来了这么一张图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2l8xXtksrkFk8T7g9WRsKCWwu4FNNdiczl3R77ScvRIpzzXMF9tj9QbA/640?wx_fmt=png&from=appmsg)

我：。。。  

海辛：。。。

确实还原，但是也是真的别致。。。

我们陷入了非常深了焦虑中。  

直到，阿文发出来了这么一张图：  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2FyRZHmTQ8FFacpuZkKnIUhaN0ibXKK7lAFHchZpO618upFUQz04O9wg/640?wx_fmt=jpeg&from=appmsg)

我：卧槽。

海辛：卧槽。

我们都懵了。

这玩意，并不是原封不动的还原，而是在文物的基础之上，还原了结构，保留了神韵，用现代化的审美，对文物的过去，进行了完美的诠释。  

这才是我想要的还原。

我们立马冲过去问阿文，到底是咋做的了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2SqMkl8mgHefPn3QFfKb4OrleRkic4ribRPxuZUCmRI0QoribqTFz6Iv0w/640?wx_fmt=png&from=appmsg)

再一次刷新了我对GPT+Dalle的组合的上限的认知。

我也自然，去如法炮制了。  

这一次，我给的是荆州博物馆里，著名的漆木彩绘双头镇墓兽。

> 时代：战国（公元前475—221年）
> 
> 来源：天星观一号楚墓出土
> 
> 级别：国家一级文物
> 
> 内涵：镇墓兽头插鹿角，睁目吐舌，狰狞恐怖，是经过夸张或组合而成的形象，显示其引魂升天的神威

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2gRiaouJgmAkRVbxAvgVf9IicjiaGKUjcZdYo9zOw4c4l3icNh4cNHAGsYA/640?wx_fmt=png&from=appmsg)

然后，Dalle给我画了这么一张图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2hv54dQibrqeLSCMh7nbuASicp12IpUSGLrghNUYRWdRmSUD1HjFaBiaUg/640?wx_fmt=png&from=appmsg)

说实话，这就是我心中的荆楚文化中的镇墓兽。

他就得长这个样子。  

于是，我又让GPT给我描述了一下这个生物。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg24wHSSWAruFWwTG399FyRnTqoqvSRiaVqTUXYWHzvFS4icZBTxSBYBNyQ/640?wx_fmt=png&from=appmsg)

然后我自己再精炼总结了一下，扔到了Midjourney里（Dalle3的质感和审美太差）。  

我的镇墓兽，就出来了。虽然还有很多一致性问题。

但，这就是我喜欢的，想要的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2zWiblMfX2xFZ0EUF0feS4uEYR3j1cyRIszgaHxuFKtYLCV5GkG5re5Q/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2BSlLzvnusrjMpR6bOobhBYNibhhyhoicZbicSEklXO1erfWzcgI1L0icHg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2o2Rg4XdZRQfOV3NVDuH5UU6uyAMRyK5OZyXI8oFibq3bxk6OBTwoy5g/640?wx_fmt=jpeg&from=appmsg)

当然，除了镇墓兽之外，我又继续用AI，复活了很多其他的文物。

后面有机会的话，可以放一系列。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2e67Tb8FwTzufia9ruDt2ibOjf3Bibe5iaukhS4Cz6r08C2QMsKrR7CwPDQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2qt2a6mtsHwc0NyugnAgZVAd4iblcjP40DuVLza8CAtDs46Sg7nQ1NXQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2MkbkN9RuZB442If2DSc40VRzAnqPnslfxepCTtTwNn1dxKjb0RLf9Q/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo83ypLo0ZicqDWhfGJtkGg2KaEibLsicsrgJm4Vv0wNmnYmvDMJ8FnK5FsuU8PyZ6Mz5YMEHVAstExw/640?wx_fmt=jpeg&from=appmsg)

或者说不叫文物。

应该叫，我们中国，独有的，“神兽”。

他们，是活在我们的历史里，活在我们的记忆里，活在，我们的血脉里。

所以。

我想看到他们时隔千年，再出出现在我的眼前。

看一眼，那跨越千年的梦。

我爱它们。  

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。******

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言