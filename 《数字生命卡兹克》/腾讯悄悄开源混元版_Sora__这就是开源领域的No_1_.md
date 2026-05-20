     腾讯悄悄开源混元版「Sora」，这就是开源领域的No.1。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

腾讯悄悄开源混元版「Sora」，这就是开源领域的No.1。
=============================

原创 数字生命卡兹克 数字生命卡兹克 2024-12-03 15:05 北京

> 原文地址: [https://mp.weixin.qq.com/s/kalNwoQP07lccluKPo0DzQ](https://mp.weixin.qq.com/s/kalNwoQP07lccluKPo0DzQ)

今天，人又在腾讯混元发布会的现场。

上个月5号，他们宣布开源大语言模型混元Large和3D大模型Hunyuan3D-1.0。

仅仅一个月时间，他们又从深圳奔赴北京，邀请了一些老朋友，又开了一次私密的闭门会。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrzW0NQLbCGhpbHr4Wm6rd6iaOwXVEojjeEQ0Ggj4YzU1uoNYLDnf1biasdKHwDsaK4Qy9TVWzZWEeA/640?wx_fmt=png&from=appmsg)

而这一次的项目，就是被N多人期待了很久的，腾讯混元视频生成模型。

同样，现场宣布，直接，开源。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrzW0NQLbCGhpbHr4Wm6rd6qJu3c4nh9cKggk2UYicXbj9gtribxkl2MQVb6GSKt8gtIaiaNbDHO4rAg/640?wx_fmt=png&from=appmsg)

腾讯也活成了，马斯克心中，那个OpenAI的模样。

聊聊这个腾讯混元的AI视频模型，我已经先行测试了一周，跑了几百个case。

先说结论：**偏科战神，强的部分强到没边，弱的地方也急需优化，但是瑕不掩瑜，综合来看，闭源模型中排在T1附近，开源AI视频中，无可争议的T0。**

开源地址：https://github.com/Tencent/HunyuanVideo

普通用户也可以去腾讯元宝APP，进入AI应用，就能看到这个AI视频了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrzW0NQLbCGhpbHr4Wm6rd6nmO261uibmoGkTQEciaicf3gV5ej5Wsk9KXVfUkhS4Merns0K5wO3iaR8Q/640?wx_fmt=png&from=appmsg)

可能普通用户需要资格申请，但是以腾讯的速度，应该非常快，看了群友的反馈，有的申请了不到一会就拿到了体验资格。

我先放几个我跑的Case，再来细说。  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pyy1m9vpkjkpTmn7H5UWGgGw2RP1l6qapr0QHLVXhSiceF4GdbiblvLPw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pOYI0YshPHrZJLIFl7YJaNYRh3viaibVEibpjCqBCyk3pwCRGCKibUX0xtQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pyN1iaEuh26fE1QlLAVWbUyq9vLZ3z8ZU9qEfoePXs8rEZfJKAlbBKCg/640?wx_fmt=gif&from=appmsg)

很有意思，很特别的模型。  

如果让我来总结混元的3个特点，那就是：

**超强的真实质感，很强的语义理解，可以切换镜头。**

一个一个来说。

  

**一.****超强的真实质感******

说实话，混元的真实感，是非常惊艳到我的。

有点当年Flux出来的时候，那种既视感。  

那种光影，那种质感，那种色彩，就是会让你感觉，这是现实场景，就是很真。  

而且，几乎没有任何的AI视频中的柳絮抖动的那种质感，稳的一笔。

比如：**两个女人面对面哭泣**。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pM2icuUUNXlov0wl8G6IfscVicvYibXuxEX1Tg0Mup9AAV7zuvxwa1zUeQ/640?wx_fmt=gif&from=appmsg)

你就感觉，像在看电视剧。

下属跟老板打架也是。  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pnGIh09k6jpuUCt0fqqJSUTpZzhYKIeE2dUsDDakMAAWL4RuRcSkYicg/640?wx_fmt=gif&from=appmsg)

这光影和稳定性，实在是强到有点飞起了。

除了现代的戏，古装也是真实到不可思议。  

比如：**长焦特写，一位紫衣宫女在月下绣花。银光洒在锦缎上，针线穿梭。后景是雕花窗棂，氛围静谧优雅。**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2paZ8wpf6pM2jprG51XwIY3eS8tsXCAtY4jsD4xYicp6ZGibz8oPWiaTunw/640?wx_fmt=gif&from=appmsg)

我愿称之为，最具有“电视剧质感”的AI视频大模型。

第一次，能看到，做中国古装，服化道和真实质感，好到如此程度的。

不只是国人，外国人的真实质感，也极强。  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2p9ib5n4mzLiabNsYBcgB6egW7licVOa2nuya6KweMSQNzVpcNOpicMO8DuA/640?wx_fmt=gif&from=appmsg)

像拍的，不像生成的，实话。

但是，但是来了。

混元AI视频的写实质感，可以拉满，我可以说，就是现在的No.1。

但是，我开头说它个超级偏科战神，就是因为，它如果不做超写实，做一些偏幻想的风格，或者2D、3D之类的，那个审美，真的有点丑= =

这就仿佛一个学生跟你说，他语文吊炸天，150分考了149分，然后你问他英语多少，他支支吾吾的跟你说：不告诉你。。。

另外有一点，是需要狠狠夸混元的。

就是跑过AI视频的人都知道，一旦人物的脸，在画面上占比一小，很多都会糊脸，五官是一坨，看不清。

但是我用混元跑的几百个case里，有不少是脸很小的，但是几乎都非常准确，甚至还是动嘴型说话。可以看下面这个例子。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2ppmD9WXib7J1wdIhI6QsibGM5T7w2QvIUYFn5EVnGPibtdlFcH7icS87xSg/640?wx_fmt=gif&from=appmsg)

开门的那个女人，脸没糊，那么小的面积，你都能看到她的神情，看到他的嘴形，这个点，太牛逼了。

  

**二.很强的语义理解**

混元的语义理解，是我觉得在所有的AI视频大模型里，都能排到前列的。

看这个Prompt：  

**一只银渐层在游乐园里奔跑，跳到一个小女孩的怀里。**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pYtfyiabI1w6H500r4j3DDjexawASqOr2V0GQjDt3Wic2icU9f2TW6Rscw/640?wx_fmt=gif&from=appmsg)

看着简单，但是其实蛮多坑。

银渐层、游乐园、奔跑、跳、小女孩、怀里。

这些个关键词，其实都不好理解，更别提跑着跑着跳到小女孩怀里这种操作了。  

首先要准确识别出银渐层这个特定品种的猫，还得理解它在游乐园这个复杂场景中的运动轨迹。

更难的是，模型需要精准捕捉从奔跑到跳跃的动作转换，还要准确把握跳入怀中这个互动场景的空间关系。

这个能完美还原，就挺牛逼的。  

还有这个case：  

**45度俯拍，一位紫衣女修在竹林中抚琴，琴音化作七彩音符在空中飘荡。翠竹摇曳，月光如水。**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2p08BO9icL166VqoRtQz9HM1fAyedicSzOwtKIJSht7xqnlyPSZO01nKbg/640?wx_fmt=gif&from=appmsg)

虽然这个七彩音符加的吧，总会让我想起一些非常古早的渐变PPT，但是咱们忽略审美的事，你会发现，混元都给你还原出来了，45度俯拍、紫衣、抚琴。

还有那句最重要的：琴音化作七彩音符在空中飘荡。

你如果用其他AI视频都把这个Prompt跑一遍，你就知道，能精准的出现七彩音符这事，有多难了。

还有一个我超级喜欢的case：  

**星系边缘，宇宙战舰引爆反物质引擎。能量涟漪以光速扩散，撕裂周围星体。**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pz9BZ8fScia7CWjzS1UTCppzyGvZdaNzIApMwc7vs40esyuwTFt41s5Q/640?wx_fmt=gif&from=appmsg)

这个镜头，是我幻想过，在科幻片里看到的一幕。  

而现在，是由AI，给我精准的还原出来了。

就是我心中的，奇点爆炸。

当然，在我测的几百个case中，并不是说，什么语义他都能理解。  

翻车的也有很多，但是整体成功率，还是相比于其他我用过的，高出不少。但是带来的负面也很明显，有的视频，那个审美真的挺差。

语义理解和审美之间，其实一直需要找一个平衡点，语义理解强，就代表着可控性很强，也代表着用户对AI的干涉非常强，一旦用户自己随心所欲的去创作，也可能会让出来的美感，没有保障。

典型的就是Midjourney，它的语义理解，我觉得到现在为止，都可以说是一坨屎，包括可控性也是一坨，ControlNet说了一年了，到现在也没加。

而他们给出的理由，就是如果让用户对AI的生成干涉过多，就会影响审美，让出来的东西变丑，作为一家有审美洁癖的公司，这个是他们不可接受的。

所以就一直拖一直拖。

混元的AI视频，走到了Midjourney的反面，给用户的自由度很高，但是这时候就又吃用户自己对于画面的理解了，换句话说，就是：  

**上限很高，下限同样，也极低。**

  

**三.可以切换镜头**

混元这个，跟PixelDance是目前全世界唯二，可以自主控制切镜头的。

比如：**广角镜头，破碎的镜子碎片漂浮在空中，每片镜子里都映照着不同的时空画面。画面中央是一位银发时空术士，他穿着暗纹长袍，双手编织时空之线。**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pGYvNMjYeQGfa5FYkGicIBVfAibJcxOhjq78iaPoXMYUKnwaicWiboV1WHYg/640?wx_fmt=gif&from=appmsg)

我其实没有写类似于镜头切换的关键词。

但是混元在理解完我的Prompt后，给我切镜了。而切镜完的效果，确实张力好一些。

最重要的是，人物、场景几乎完全一致。这点，就很酷。  

还有士兵看信这个case。  

**战场废墟中，一位士兵跪地，颤抖着手打开战友留下的信。然后镜头切换到信件的特写。远处炮火映红天际，烟尘在空中飘散。战争片风格。**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURprbltiaMuDMHlDOYoPyKN2pBGL80UvKPJiautmDxoM78rNclXcuxSnm7d8cDkcUNp6aG78N4VJU3vg/640?wx_fmt=gif&from=appmsg)

这次我是主动说了“镜头切换”这个词，混元理解的非常好，场景、人物一致性也堪称完美。  

这一点，我非常喜欢。  

  

**写在最后**

AI视频这个行业，我一直觉得对于创业者或者小公司来说，不是特别友好。  

不友好的点在于，获取高质量数据的难度，相比于文本、图像啥的，太高了。

大厂啊，护城河还是太高、太深了。  

最关键的是，腾讯用这个自己深厚的家底，先把这个模型的v1版本做完了，然后，直接开源，免费送。

这尼玛，谁顶得住。  

目前混元AI视频模型，只支持文生视频，不过他们说图生视频也很快就会上线了，马上就做完了。

文本大模型、AI绘图大模型、3D生成大模型，再加上这次的AI视频大模型。

如果再来一个AI声音模型，腾讯就是，真正的全系开源了。

只能说，腾讯对于自己的市场定位和核心竞争优势，也有着极度明确的认知。  

腾讯的城堡，还在向天空挺进。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言