     AI绘图StableDiffusion最棒LoRA模型盘点 - 小样也能出奇迹 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI绘图StableDiffusion最棒LoRA模型盘点 - 小样也能出奇迹
=======================================

原创 数字生命卡兹克 数字生命卡兹克 2023-05-03 18:58 天津

> 原文地址: [https://mp.weixin.qq.com/s/Z7onNo09-7--9eGrbPe0wA](https://mp.weixin.qq.com/s/Z7onNo09-7--9eGrbPe0wA)

上期盘点了一下StableDiffusion的我认为最强的大模型。

这期来盘点一下我心目中最有意思的LoRA模型。

LoRA模型就属于百花齐放了，因为他精致小巧的特性，有无数的LoRA都能达到不错的效果。其中特定人物的LoRA模型最多。

**这里做个简单的小科普，LoRA模型到底是啥？**  

LoRA，全称Low-Rank Adaptation of Large Language Models，LoRA取的就是Low-Rank Adaptation这几个单词的开头，学名叫大型语言模型的低秩适应，看名字也知道，这玩意最先用在大语言模型上。

大语言模型动不动几百B几千B，为了让大语言模型执行特定任务，直接把这几百B的大模型拿来微调的话，贵+慢+重，性价比太低。所以出现了LoRA这种方式，直接把原来的大语言模型给冻结，在外面搞个额外的小插件来进行微调，不直接去动原有的大模型，弄完了再合并在一起。  

**又便宜又快体积还小，体积可以整整小一千倍。还跟插件一样，即插即用。**  

后来人们发现在绘画大模型上表现极好，拿来固定画风或者人物极其牛逼，于是一发不可收拾，直接起飞。

想更多的了解LoRA的，可以去读一读这篇论文：https://arxiv.org/abs/2106.09685

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQZkBpKianQf0OKSrzUnjn1xBQHYRWddI4ZZiconOkRXtSb0qImTQNkxPw/640?wx_fmt=png)

回到我们的StableDiffusion上的LoRA模型盘点，我给大家推荐8个LoRA，基本都是偏风格向，人物的就不过多推荐了，看自己喜好去Civitai上扒拉吧，见仁见智。  

这8个分别为：

**1.Korean-doll-likeness**

**2.墨心 MoXin**

**3.hanfu汉服**

**4.blindbox/大概是盲盒**

**5.Anime Tarot Card Art Style 塔罗牌**

**6.Gundam RX78-2 outfit style 高达RX78-2外观风格**

**7.M\_Pixel 像素人人**

**8.The Legend of Zelda: Breath of the Wild Style（旷野之息）**

模型老规矩，我也都整合好了，关注我私信L，就有了。  

  

**一.****KoreanDolllikeness******

人物LoRA领域，有无数。不错的，整活的，复刻明星的等等。比如Makima、Lucy、Liyuu等等，也在各种灰色地带不断游走。

但是最好用效果最稳定的，我觉得还是KoreanDolllikeness，3月因为一些舆论风波，KoreanDolllikeness被作者直接删库放弃。如今5月了，我依然首选KoreanDolllikeness。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQCwgSLVLWUyBQOqB6snpImrzDx9E0ibvpqEH8FOpzhibz4ibovTDz06mng/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQ8I7lfNPSzsKfUBKuEjcMyKxlNXSqsNUiaqe198BrrJcyqnCxw43mRnA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQd78p1gJ7fm00jKf6U5o7L4VTV74yiceJablMX4L9iaALfEcI5Ifhh1mw/640?wx_fmt=jpeg)

  

**二.********墨心 MoXin**********

**《墨心》—— 昔涓子《琴心》，王孙《巧心》，心哉美矣，故用之焉。**

我心中年度最佳，最强模型，没有之一。

目前Civitai所有LoRA模型中下载排No.4，让世界都感受一下中国水墨！

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQDGML2o7JP8EmdbIUzM7EfFfHOMNlSwh3gt0lnFuYx00hBRibFex3p6w/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQ8tBdxyQR9E81eTqz9podibnKEoPC7jSibQnWn71wso3ib7U4hDp4micjYA/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQuu1eaGlLXqmGBCWAe5UDZvaChWrTRvNVuCPakA2zRp3pQjAiaIBibAog/640?wx_fmt=jpeg)

  

**三.************hanfu汉服**************

目前Civitai所有LoRA模型中下载排No.7。

**与墨心并驾齐驱，中国文化对外输出典范，中国的汉服，真的很美。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQRiaH5VwolvLfrmbbFQvUXoH5akPmykhwULM94jPxdiaGpg8gT1zGZ3Uw/640?wx_fmt=jpeg)

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQaVD80h0Azfjyb6BMg2Zhfic05EyJ2ibsBKTHMQePRdxX8FrDZOjIcLFA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQA0smmeOzjOSgKzwPmG7Jk8680eJsib1icbs1auQ4lYVIAZ0eEBN45YBQ/640?wx_fmt=jpeg)

  

**四.****************blindbox/大概是盲盒******************

非常棒的盲盒LoRA，MJ的泡泡玛特风格火变了全网，带火了这种盲盒风格。

这是目前处理这种风格最好的LoRA模型，极其精致逼真，让你实现盲盒自由！

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQ5KAHYy945hWyGNdYmjBTnL4rzpCkOAJqPgoCpYcWAxX09eGAvbAmPA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQVnvLLqq69Z7HfjK30eNIOFv8t4RGExliazJ4Y8nDCWZIvppqgTRN6NA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQVln88EA9zgUCyICZancHgnsW4mTyW5Yxpia7p6CK5a68GJy9EPaP7Jg/640?wx_fmt=jpeg)

  

**五.********************Anime Tarot Card Art Style 塔罗牌**********************

很有趣的卡牌LoRA，把你的图片直接放在框里，让你有一种爱不释手的精致感，卡牌构图也是很经典的美。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQCnriaVjg69KySCfJx9OENyZZEgBR8q0fvTFLlQ7VpbBrbLo2Esh3pTg/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQSOkK3aibxe5r3k707W9c2BicIPY01VxHicVZVzDqcp0R7BaESkUFgaMxg/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQpJ8W6GuvL6J5IoZPNcm2KNwwJa1gSbBdrrxLfeR26M8fbPtadqIfGg/640?wx_fmt=jpeg)

  

**六.************************Gundam RX78-2 outfit style 高达RX78-2外观风格**************************

人人心中都有一个高达梦。谁不爱机甲，谁不爱高达呢！

机甲YYDS！高达YYDS！！

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQicht8koJZH4PFOZR365ajgnQ9FF2UEibOjlvnaVIjOtB4l50oiaiaV2GQg/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQOVzhLicAIk7ycpVqMC0GzIwkhEhsckziaPBA1ibW0qBys8KxagCxhwY1g/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQFc4JHrD9OiagL4FoDK9Fy790Z5pJesW1gNibEFiaIzX8qNHq2d0iaiamvCg/640?wx_fmt=jpeg)

  

**七.****************************M\_Pixel 像素人人******************************

像素画起源于上世纪末，是机能不足下妥协的产物。21世纪后，3D技术大行其道，同时像素画也作为一种风格继承了下来，由于细节的缺失，反而给人一定的想象的空间。以《歧路旅人》为代表的HD2D则是其现代精神继任者。

这个LoRA，以此来缅怀那个像素艺术的黄金年代。最好的像素模型。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQQkQWOrqezfjmNZOFDW0w7mXoBY8YRtaglV4X5DCCaFuSR8AzwCz5Ng/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQ9t6On1KwaBFT4kc2ZajhPTu8JJLJQibVNBwuRNCURqwiaDibl3W7P4oMA/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQiaMYUbCEtRkicnHkLzUUz8UUROm19qfpW5CQBNeyHF7lfQj2icm7oIrQQ/640?wx_fmt=jpeg)

  

**八.********************************The Legend of Zelda: Breath of the Wild Style**********************************

这个模型没什么好说的，我自己的私货。

作为一名任豚，作为一个塞尔达死忠粉，怎么能没有旷野之息那独特的风格模型呢！  

**塞尔达就是天！任天堂就是TMD的世界主宰！  
**

**5月12号的旷野之息2王国之泪，首发必须冲！**

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQC8cdfM8t36xN1D7zIiaAuUQssLa2KHOyD00zAsPKo1Y5N60ic92S7bcQ/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQQBXRQpib2YgxmJB7rYZb2iaUmEVyy6bUEr7vXrUmBRsXmt1HMEnaNd6Q/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo3Fk5oaWJ0lEibicKoROzEiaQP7wY5ddCQSTjHibf0xJjibibzNbNZJt6Yxh43ormB3EsFSnHRMTtmuh4g/640?wx_fmt=jpeg)

  

**写在最后**

以上便是我目前最喜欢也是我现在最常用的LoRA模型啦。

**也都放在了整合包里，关注我，后台回复L就有了。**

模型的迭代快如闪电，后续这个感觉可以当成栏目，有好玩的模型出现，也第一时间推荐给大家，或者每隔一段时间做个盘点哈哈~

上期SD大模型盘点：[AI绘图StableDiffusion最强大模型盘点 - 诸神乱战](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647658397&idx=1&sn=b545cddd6613e792d9a7c8df99c0dcf5&chksm=f007d3cac7705adcc2b753faf546d4d08d26e32068e393cd395342e2cd0c7d4614ab55348aa0&scene=21#wechat_redirect)

以上，创作不易，有用的话请点个关注并给个星标⭐，感恩。

  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言