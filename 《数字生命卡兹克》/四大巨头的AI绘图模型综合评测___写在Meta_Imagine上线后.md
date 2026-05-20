     四大巨头的AI绘图模型综合评测 - 写在Meta Imagine上线后 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

四大巨头的AI绘图模型综合评测 - 写在Meta Imagine上线后
===================================

原创 数字生命卡兹克 数字生命卡兹克 2023-12-10 20:39 天津

> 原文地址: [https://mp.weixin.qq.com/s/TKIpXkLlNfGsCoLJDTJ02g](https://mp.weixin.qq.com/s/TKIpXkLlNfGsCoLJDTJ02g)

都知道AI卷，卷大语言模型，卷多模态，卷视频，反正啥玩意都都卷。

AI绘图作为跟大语言模型并驾齐驱的最成熟的模态之一。  

那更是卷到飞起。

前几天，Meta这个搅屎棍，正式公开上线了他们的AI绘图模型，叫Meta Imagine，就是这个玩意。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfhb7R0SUlyF6LXwuDnKicyA9xAtnReeTVhA28vPSmZzwpV6jTEPiaz6kA/640?wx_fmt=png&from=appmsg)

网址：https://imagine.meta.com/ （对魔法要求比较高，找个美国的干净的节点）

最关键的是吧，他免费。  

你说他是不是搅屎棍。。。

但是Meta确实也有这个底气，毕竟你架不住他卡多啊。。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcf63fy7XeBicLqefthcSQkwibd666c9WYAk2rUWOT0xrliaH8tMdH7pvINg/640?wx_fmt=jpeg&from=appmsg)

一个不做云服务的，搞这么多卡。。。甚至囤的H100超过了微软。。  

你说他想干啥。。。

当然是来当搅屎棍了（笑。  

当然，其实前两天就想按我的体系，去评测一下Meta这个免费的AI绘图了，但是因为PIKA1.0的关系，实在没有空，这周六下午才腾出手来好好的去玩。  

正好也想借着这个机会，来对比评测一下我心中的现在四个比较大的AI绘图模型：  

Meta Imagine，Midjourney，Adobe Firefly，Dalle。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfa5NDjpetegYbcFz24cPS7wF75qaM7iap3tUwoy6Bz9NsKCqiaKoAdVHA/640?wx_fmt=jpeg&from=appmsg)

SDXL之所以没放在里面是因为他毕竟是个开源模型，是靠后续大神们的微调和生态来玩的，而且原生的质量确实有一点点差。。。

所以主要来对比这四个大模型。

我会从**细节质量、审美（构图色彩等）、风格多样化、语义理解**这四个维度来评测，每个维度3个Prompt，同时每个Prompt我会在AI绘图模型中roll3次，取效果最具有代表性的那个图，尽量减少偏见。

同时，为了有最后整体可视化的评分让大家看着更直观，所以我会进行打分。在每个案例中，第一名为4分，第二为3分，第三为2分，最后一名为1分，最后计算和。

OK，让我们开始。  

  

 **一. 细节质量** 

主要测试AI绘图对于细节的表现能力，比如人物面部皮肤的质感、比如织物纹理的细节、场景细微元素的细节等等，这个是对模型精度和输出质量一个非常重要的考量。

> Prompt1：Portrait of a 2000s blonde woman posing on a sports car, white wired headphones, expressionless, 2000s hairstyle, 2000s fashion, sun rays, light teal and amber,Cinestill 50D
> 
> 2000年代金发女郎在跑车上摆姿势的肖像，白色有线耳机，面无表情，2000年代发型，2000年代时尚，太阳光线，浅青色和琥珀色，Cinestill 50D

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfmib0ricwwEUcGtNYKibtcMNe8k7YiaiaibsdWiadJbKqemKoicJGTbUT04tCww/640?wx_fmt=jpeg&from=appmsg)

明显可以看出，Adobe在人物皮肤质感和衣服质感上最佳，Meta和MJ其次，Dalle3最差；耳机细节都有问题，Dalle3取巧了所以没有BUG，Meta直接没给你画；背景的细节都差不多。

Adobe：4，MJ：3，Meta：2，Dalle：1。  

\-

> Prompt2：Amazing photo of golden retriever chasing tennis ball underwater, close-up portrait
> 
> 金毛猎犬在水下追逐网球的惊人照片，特写肖‍像

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfv4GVygnJhBAYZ5E9RO73szs4DzH7wia2UibGdicaiclbV6fKAkbB7oQcmQ/640?wx_fmt=jpeg&from=appmsg)

Meta整体最好，MJ其次，被水沾湿的细节都画出来了，Adobe狗身上的细节少了一些，Dalle3还是拉了，水的气泡的细节崩了。  

Meta：4，MJ：3，Adobe：2，Dalle：1。

\-  

> Prompt3：A girl with a bunny sitting and smiling in 1970s fashion in a field of flowers
> 
> 一个带着兔子的女孩，穿着 1970 年代的时尚，坐在花丛中微笑

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfagUInGUSzX7GZCyM1uqzsibCYFxxNTOv3QQtxLJ8asVuZgpBIhRmRyw/640?wx_fmt=jpeg&from=appmsg)

MJ完胜，花和兔子、头发细节基本都没啥可挑的，Adobe的细节很足但是裤子崩了，Meta的面部皮肤质感很难受，Dalle基本就没啥东西，一股子油画感。

MJ：4，Adobe：3，Meta：2，Dalle：1。  

在细节质量上，总分如下:

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfV1xuJrZCtalL20SN7heaRrtQ9V6GubNABib4UYtCyCjJWK8kw3fIbCw/640?wx_fmt=png&from=appmsg)

  

 **二. 审美** 

主要测试AI绘图的审美能力，一张图好不好看，是美是丑，除了细节之外，更多的还需要看模型的审美能力，比如构图、色彩、光影等等，审美强，出的图才好看。

> Prompt1：Product shot of juicy burger, artisan, rustic, food photography, delicious, close-up
> 
> 多汁汉堡的产品拍摄， 工匠， 质朴， 食物摄影， 美味， 特写镜头

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfXZYWdNpG6d627MN5N7Lvok654eEbd4BqgfgtiaZ3s2mHGSUicibexiczXA/640?wx_fmt=jpeg&from=appmsg)

一张非常强调审美的图，Meta的色彩几乎就不能看，让人毫无食欲，Dalle的构图问题很大背景太乱，两个瓶子跟门神一样，MJ也没有构图就一个大主体，Adobe完胜。

Adobe：4，MJ：3，Dalle：2，Meta：1。

\-

> Prompt2：Dungeons and Dragons, Close up of a fire breathing flying dragon, cinematic shot
> 
> 龙与地下城，喷火飞龙的特写，电影镜头

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcf3Iwia4Vk3ecqoqnxmK86RIyR9p61JJ3SKJK682cXT1FxsPQbbcaVHDg/640?wx_fmt=jpeg&from=appmsg)

特写镜头，很强调构图，还有火与龙身的光影对比，Meta的龙极其呆逼，其他所有的龙眼睛也都会发光来做强调，就它真画了个眼睛上去，色彩和构图也不太行，整体最佳还是Adobe，色彩和构图都棒，其次是MJ，再次是Dalle，构图差点意思，太偏左上了，最次是Meta。  

Adobe：4，MJ：3，Dalle：2，Meta：1。

\-

> Prompt：Diagonal Shot. Constantinople, 1453, masked sorceress, in the style of biblical drama, movie scene, low saturation, muted colors, extreme detail, 8K
> 
> 对角线拍摄。君士坦丁堡，1453年，蒙面女巫，圣经戏剧风格，电影场景，低饱和度，柔和的色彩，极端细节，8K

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcficz1MlfDwAzpU5IoibND1YYicCz64NudJqmaribbVBibtcjx6kVr72Cibicow/640?wx_fmt=jpeg&from=appmsg)

MJ的构图和色彩质感基本爆杀全场了，Adobe完全没理解我最后的低饱和度，Dalle的构图也很奇怪。  

MJ：4，Meta：3，Adobe：2，Dalle：1。

在审美上，总分如下:

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcf1AtYUEr3j2ltV0bYIH3aoSZQVSKBIpJ4QgVZMajVqDezTf99Do0Sicw/640?wx_fmt=png&from=appmsg)

  

 **三. 风格多样化** 

主要测试AI绘图对于风格的包容度，比如皮克斯风格、吉卜力风格、折纸艺术等等，理论上是需要大规模用几百个艺术风格去测成功率的，但是我个人精力有限，所以简单测试3个稍微常见一点但是不是那么烂大街的艺术风格吧。

> Prompt1：an anime illustration of a samurai girl carrying a ninja sword, in the style of ethereal brushstrokes,  ink painting, dark white and dark gray, fluid formation
> 
> 拿着忍者剑的武士女孩的动画插图，风格空灵，水墨画，深白色和深灰色，流体形成

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfd0lPicZxg1umTutJNutOU2Kyhy0LKppia4YQwF8xiamVC9lO9QJiaqr2OA/640?wx_fmt=jpeg&from=appmsg)

在水墨画这块，得神韵得还是MJ和dalle，Meta那个笔触就很诡异一点都不连贯断断续续得，Adobe画出来就感觉一个日漫一样。  

MJ：4，Dalle：3，Meta：2，Adobe：1。

\-  

> Prompt2：small boy looking out of his bedroom window into a cyberpunk world, pixelated, 8 bit style
> 
> 小男孩从卧室窗户望向赛博朋克世界，像素化，8 位风格

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfmzvzDgOQjte4HZBGhWYsH0miboW9uhkGibUGqkibCcic40JiabQRCMPLJnQ/640?wx_fmt=jpeg&from=appmsg)

8bit的像素画+赛博朋克，Adobe和Dalle都画出了这种风格，Meta差了一些，MJ是完全没画出。在像素化上，Adobe确实最好。

Adobe：4，Dalle：3，Meta：2，MJ：1。

\-  

> Prompt3：Colorful logo of a French restaurant called "Khazix" with a flying seagull
> 
> 一家名为“Khazix”的法国餐厅的彩色标志，上面有一只飞翔的海鸥

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcf6LAQ0vCP2AdhDQl5ACNWBujdTusVsOfJV5VwkUxBkd0Liaklv8AjUKw/640?wx_fmt=jpeg&from=appmsg)

在做Logo上，Dalle3的精准文字目前确实是独一档，无人可比，logo的设计上，Dalle最强，MJ次之，Adobe普普通通，Meta的图形和细节简直稀碎。

Dalle：4，MJ：3，Adobe：2，Meta：1。

在风格多样化上，总分如下:

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfTyzf6plNemnggibYib1K8ktGxzibfica5U8nqRBURkJbMrZol2m3f4iaDDg/640?wx_fmt=png&from=appmsg)

  

 **四. 语义理解** 

主要测试AI绘图对于复杂语义的理解能力，能否将文本内容都能清晰的表达出来并保证生成图片的质量。

> Prompt1：A cup of coffee sitting on a table in front of a window; outside the window is a futuristic city; a futuristic monorail can be seen close by; many lush plants around; shot from ground floor; clouds above
> 
> 窗前的桌子上放着一杯咖啡；窗外是一座未来的城市；附近可以看到未来派的单轨列车；周围有许多茂盛的植物；从一楼拍摄；上面有云

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfHoOG4XoDiciaibgibBicqeXFrhCliaZt2n4lHXAfibqId51Tv82kmYKy2M0IA/640?wx_fmt=jpeg&from=appmsg)

MJ崩了，是唯一没画出列车的，Adobe画了列车但是轨道有BUG，Meta画出来了但是很乱，Dalle完美。  

Dalle：4，Meta：3，Adobe：2，MJ：1。

\-

> Editorial photography of astronaut cooking Christmas colorful chocolate honey cookies on spaceship, Christmas honey cookies floating around astronaut, no gravity, in spaceship, levitated
> 
> 宇航员在宇宙飞船上烹饪圣诞彩色巧克力蜂蜜饼干的编辑摄影，圣诞蜂蜜饼干漂浮在宇航员周围，没有重力，在宇宙飞船中，悬浮

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfVxpBrZdMIHWsibuV6pwfYequgict25ibiaSteZagaMaf9FAAguOibGhylYw/640?wx_fmt=jpeg&from=appmsg)

Dalle暴揍全场，唯一理解了圣诞、彩色元素的，Adobe在做饼干但是没这些元素，MJ好看是好看但是快把自己炸没了，饼干都没在做，Meta的饼干没漂浮。。。  

Dalle：4，Adobe：3，Meta：2，MJ：1。

\-

> Prompt3：Shot diagonally. Cinematic shot of several astronauts in the space station, surrounding a chromium metal water droplet suspended in the air, the surface of the water droplet can reflect everything like a mirror, indoor scene
> 
> 对角线拍摄。几名宇航员在空间站中的电影镜头，围绕着一个铬金属水滴周围，铬金属水滴悬浮在空中，水滴的表面可以像镜子一样反射一切，室内场景

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfCibm4gic0Pu1xv2Ugu6t7PBq9NquLQAvXD6Huibx9XSoxD8QG8TvWf4hg/640?wx_fmt=jpeg&from=appmsg)

之前做《三体》时一个天坑镜头，镜面能反射一切的铬金属水滴没几个AI能理解的，Dalle不亏是语义之王，Adobe理解成了从天上往下滴的水滴，Meta和MJ不知道在玩个啥。。。  

Dalle：4，Adobe：3，MJ：2，Meta：1。

在语义理解上，总分如下:

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcf0QwCwroDEVvWscoxD10FicOhUmXG2f9oJfzxQuUVlSj6eMJPZiawSAlw/640?wx_fmt=png&from=appmsg)

  

 **写在最后** 

在四个维度评完了以后，我们应该能对这几个大模型有大概的了解了。

但是为了更直观一些，我再来做个雷达图吧。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq3iboZvd0Kl8E2Q7W03kOcfNjI0j3wb78JKmpCOeDHA30ukDBuwtlLjuc9eb7I1wrBWHqfQ5icUB1w/640?wx_fmt=png&from=appmsg)

细节质量方面，MJ > Adobe > Meta > Dalle。

审美方面，MJ = Adobe > Meta = Dalle。

风格多样化方面，Dalle > Adobe = MJ > Meta。

语义理解方面，Dalle > Adobe > Meta > MJ。  

**综合看，目前Adobe是最水桶的，其次是MJ，然后是Meta，Dalle偏科过于严重。**  

虽然只放出来了12个prompt，但是我在后面跑了将近14个小时，测了300多个例子，选出了典型。。快吐了。。

希望这个评测，能抛砖引玉吧，让大家对AI绘图综合有一些了解。

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言