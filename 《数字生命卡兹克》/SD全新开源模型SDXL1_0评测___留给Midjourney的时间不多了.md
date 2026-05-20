     SD全新开源模型SDXL1.0评测 - 留给Midjourney的时间不多了 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

SD全新开源模型SDXL1.0评测 - 留给Midjourney的时间不多了
======================================

原创 数字生命卡兹克 数字生命卡兹克 2023-07-30 17:58 天津

> 原文地址: [https://mp.weixin.qq.com/s/PcI5BGWeNSU7QJrEqhPDBA](https://mp.weixin.qq.com/s/PcI5BGWeNSU7QJrEqhPDBA)

在AI绘图上，一直有两个阵营。  

一派是以开源为首的StableDiffusion，一派是以封闭为首的Midjourney。

在过去，基于SD的生态蓬勃发展，出现了N多优秀的大模型，比如我经常极力推崇的MajicMIX还有GhostMIX等等。

但是这些大模型无一例外，都是特定画风或者特定场景的。从来没有那种比肩MJ5.2或者Niji5质量的通用大模型。

直到前几天，stability开源了他们的SDXL1.0，SD阵营在这一块的短板，终于被彻底补齐。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpaQvsgicnT7HQHTplLvo1cZReiaU925ib3H7MbNNT9dDfhbRkQtVzPmrY4yFP1fxOYf8q8FPPQbs4TQ/640?wx_fmt=png)

所有的SD玩家都特么的可以自豪的说一句：  

劳资也有通用大模型啦！MJ吔屎啦你！

然而最值得期待的，并不是SDXL本身。  

而是未来基于SDXL而发展起来的生态。

现有的C站、Liblib上的模型，基本都是基于SD1.5这个通用大模型微调来的。  

**通用大模型本身就是一个妹子的底子，而微调就是画一层妆。  
**

**SD1.5这个1分妹子，经过化妆后，都有将近7分的实力。**

**那SDXL1.0这个本身就已经5~6分的妹子，化完妆后，有多牛逼？这个想象空间太大了。**

像赫赫有名的DreamShaper，已经第一时间推出了基于SDXL1.0的微调版本。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1f8PibMfWO1onwRO1D4t53ZSzKPLghma0CibnRibBZkukndb9v9aaoibNRQ/640?wx_fmt=png)

我认识的几个挺有名的大模型作者，也已经开始在加班加点的做SDXL1.0的微调适配工作，未来一周内，可能就会有大量的超级模型出现。

但是有一说一，现阶段的原生SDXL1.0，离MJ还是有一些距离。

放一些随手生成的对比图。

prompt是完全一模一样，毕竟SDXL1.0现在对于长语义也有非常好的理解了，但是尺寸用的是SDXL1.0效果最好的1024\*1024。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1zFORvb7Ze2OUWicOanfaJxd2vEB53sVATExGvZnv288cibeDCr9Rb3Og/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1DBILPNDsr0FHO3ToTPibfpkibRyRGiaXyqC2gzlWmEprzibIjoicibVjnlCg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1HibLE6a6hn2c35wPvRBf7jKzZ2klpo9D7g4nrDYkAbicwcEuISday0ng/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM153Pz7xWjyD3oUuGhSuL13YJvgrWp2S1u2Am5Tdob8tl3qykUFhVpmQ/640?wx_fmt=jpeg)

可以看到，在一些超写实或者真是场景中，SDXL能跟MJ V5.2打的有来有回了，但是在审美上...个人觉得还是有很多差距，stability的审美真的就是那种很直男...

就比如这张，樱花落在北极熊身上...这构图、这光影、这色彩对比...

SDXL的简直不忍直视。

不过审美这玩意本身也不是stability这公司的强项，审美的东西还是让广大网友来微调吧...

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1bV4iaglDFB7rbzo8JTgH7HwCDibMLaxgfNGEW0NyuibbWF9UupkvBRyTg/640?wx_fmt=jpeg)

至于在插画、3D等领域，SDXL1.0跟MJ的Niji5比，那就稍微有点欺负SDXL1.0了。。。

目前还属于被摁在地上爆锤的情况。但是未来可期，毕竟网友人才多啊。。。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1zF6ODYUdPreXEW4j8uOMggqxoibH3MlsnLiaFU27G3cMib4y5F4Wk8HAA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1QIpTVq0qgeIUnK3UzoWicE06Oul7eo3mKW11A2hPCwStIAtyUZ6Gwicw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1FUIA9rWiaLIas2jzQdMCicKc3ubOiaYFV7ibZwkNQQicPx12WxSdJzObC8Q/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1rLyHwWagfVCkyuKeicQ3RnYJlJKlFVBwQeD5UTsXHHS6jml496FXlYg/640?wx_fmt=jpeg)

说下目前SDXL的用法。  

**现在有两种，一种是官方的在线SDXL，一种是老规矩的本地SD。**

有心的会留意到我上面的所有图片都有个Cilpdrop的水印。  

之前有一期给大家推荐过Clipdrop：[用AI一键抹除照片里的人物还原场景 - 极致体验](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647658275&idx=1&sn=24f8f46671bc27c619698a0d64da526d&chksm=f007d374c7705a622e17febfc41b5130a46bf819d52a4be60984e4bfe488f0d6aab4fa7c6407&scene=21#wechat_redirect)，这是stability的官方网站，集成了很多他们自己开发的应用。

网址：https://clipdrop.co/

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1gialQggibxheP85zZ92XPbFc9cdQM5FU25KKoibx7dAT4hwKNK14KrCHg/640?wx_fmt=png)

第一个工具就是SDXL1.0的在线版，直接手写prompt就可以，下面三个选项可以选择风格、尺寸，以及写负面提示词。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1mQ8aDRWzPcLnUGiamV9z2cqQR5XZ5aicQiaibd8P0rp7MV2M7cIEgzlYfA/640?wx_fmt=jpeg)

生成完的推荐大家去增强一下，提高分辨率。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1E97cJTwnH60QmhBH0LtdIicTDJF3micDw3XzQVY9SAs4C2ofvsrIUa7Q/640?wx_fmt=png)

目前每天可以带水印的跑400张免费图片。

如果你觉得水印麻烦，也可以使用哩布哩布的在线SD，目前每天也可以免费100张。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1VVflawhHUVgu3M4X7zKcPVacvnon1FDotk0g0ZAFRgoUev3P3HK7XA/640?wx_fmt=png)

他们也第一时间支持了SDXL1.0，记住，**如果你使用SDXL1.0，下面那个XL Refiner选项必须勾选！！！**  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1pRKKaZNPTAfzDOY1vtqibiblFRwXBHVsj4WuBmV0lkO2QnLALm2OicHLg/640?wx_fmt=png)

然后就是我们最常用的本地SD安装了。  

**需要下载3个模型，我已经全部打包好放到了网盘里，私信SDXL就有了。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1d3TCSv3CIL3ggMliajjLuaISUViaEkhAgsN4eJp9mjkicN9UhBfkDpAxQ/640?wx_fmt=png)

其中有两个大模型，base和refiner，一个VAE。

打开秋叶大佬的SD启动器，把版本更新到1.5.1，然后正常装模型和VAE就行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM10f44T6pqicGvTGg4XH93VE1oMBAOFZY3C2eYP5WtibyGUQeoD70NATZw/640?wx_fmt=png)

SDXL1.0的工作流和以前的流程不太一样，**需要先使用base做一遍文生图，而且尺寸必须是1024\*1024。生成完的图片再发送到图生图，切换到refiner模型再跑一遍。**这样才能得到最好的效果。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpQiaPHh1iasUkISO3Xs03vM1hbSCu2IvFxvXxibfHXGQaXK2KQPtlOoXEngVewYibCyTs6RmI6bqPssA/640?wx_fmt=png)

这块我提醒一句，SDXL对配置要求非常高，**大概需要32G以上的内存和12G以上的显存。**

我自己的电脑是16G内存，3060显卡。即使加了30G虚拟内存，SDXL1.0一运行必爆。

没有这个配置的，不用下模型了，直接Clipdrop或者liblib吧。

同时，现在的SDXL1.0因为刚出来，所以生态非常不完善，不支持SD1.5基础的所有LoRA，也不支持ControlNET。

我不太建议大家现在直接在本地跑，线上用用试试就得了。

等2~3周，生态、插件、体验完善，再开整也不迟。  

写在最后。  

SDXL1.0是SD的一次反击。

**SD从来不是靠通用大模型的质量去取胜，他靠的是生态，是百万开发者基于SD之上而构建起的超级生态帝国。**  

以前的SD1.5，本身质量太差，但是在这种质量的模型上，居然都演化出了N多能跟Midjourney掰掰手腕的大模型们。

而现在质量提高了无数数量级后的SDXL1.0，基于它之上的生态上限，无法想象未来有多么辉煌。  

留给Midjourney的时间，确实不多了。

AI绘图行业的格局，也该变天了。

**以上，既然看到这里了，如果觉得不错，随手点个赞和“在看”吧，并给我个星标⭐吧，感恩。**

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言