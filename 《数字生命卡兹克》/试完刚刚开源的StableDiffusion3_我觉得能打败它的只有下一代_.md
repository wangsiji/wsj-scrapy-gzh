     试完刚刚开源的StableDiffusion3，我觉得能打败它的只有下一代。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

试完刚刚开源的StableDiffusion3，我觉得能打败它的只有下一代。
======================================

原创 数字生命卡兹克 数字生命卡兹克 2024-06-13 12:08 北京

> 原文地址: [https://mp.weixin.qq.com/s/EmKIfmCiTTwSePyb3EHrSA](https://mp.weixin.qq.com/s/EmKIfmCiTTwSePyb3EHrSA)

Stable Diffusion 3，终于开源了。

当初SD3 API放出来的时候，他的公司Stability AI已经出现大大小小很多的裂缝了。

先是在今年3月23日，Stability AI的CEO Emad Mostaque宣布辞职。

第一季度结束的时候，Stability AI的营收不到500万美元，亏损超过3000万美元。此外，他们还拖欠云计算供应商和其他公司近1亿美元的账单，可以说，Stability AI已经乱成一锅粥了。

即便这样，Stability AI顶着大家评论他商业模式稀烂的舆情压力的情况下，依然不时地开源一些模型，给你一些小惊喜。

比如代码模型Stable Code Instruct 3B、3D视频模型Stable Video 3D、3D模型TripoSR、音频模型Stable Audio Open等等...

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6XYNN8xoYt8a8ew6yB9aht47ibgmUxJhGD40YicmUTJGmkRqYxuWUibeoA/640?wx_fmt=png&from=appmsg)

不过Stability AI毕竟是以AI绘画出圈的，绘图模型是核心业务，所以大家还是更期望看到他的绘图模型Stable Diffusion发出来。不过看一眼Stability AI的惨状，大家都觉得，SD3开源无望了。

果然，SD3来了，意料之中的是，是付费API的形式。

不过广大网友没有放弃，还是抱着一些微弱的希望，在Stability AI官方推特下面求开源模型哈哈哈。

结果，万万想不到的是，千呼万唤始出来。Stability AI大手一挥说，那行，**继续开源！**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6yMX1WMVBxRAvzdhBlRmlETRjy6hDw2bYo2ejx1mpxwDaxOqr5xicNYA/640?wx_fmt=png&from=appmsg)

这次给了一个**中型版本的SD3，20亿参数**，Stable Diffusion 3 Medium。

有些人可能觉得中型不够意思，但是我觉得刚好，毕竟再大了本地也跑不动啊= =

他们官宣的是6月12号，于是我就等啊等，12号从中午等到晚上，终于，等到了Stability AI把模型放出来了。在huggingface上开源。

网址在此：https://huggingface.co/stabilityai/stable-diffusion-3-medium

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6btsmxO4MCkia0NVBheNRA1yiaqHyQibNrMlsQb8RicY9fDapPcArvzibztQ/640?wx_fmt=png&from=appmsg)

第一时间，我跟我我的小伙伴@祁珏瑜 对比了SD1.5，SD2.0，SDXL，SD3 Medium四个基础模型，来给大家看一下SD这么长时间，直观的进化。也给大家看看，SD3 Medium，有多强。

先说一下测试的大背景。

我们知道对于SD的话，需要很多的提示词，一般SD提示词两部分组成：内容描述提示词+画质描述提示词。

之前SD很烦的是，你必须要加一些冗余的画质提示词，比如best quality, high resolution,  8k之类的，正向反向都得加，不加的话则出图质量会差很多。

那我觉得既然SD3了，你就别欺负前面的弟弟了。

所以我给前三个模型SD1.5，SD2.0，SDXL提示词评测都加了正向画质提示词和反向画质提示词，（后面每一个都加了，为了避免重复就不写出来了）

1.5和2.0 的正向反向画质提示词

> best quality, high resolution,  8k,masterpiece, highly detailed, UHD,
> 
> bad proportions, low resolution, bad, ugly, terrible, render, watermark, logo,

sdxl 的正向反向画质提示词（因为xl和之前的画质提示词有些不同）。

> score\_9, score\_8\_up, score\_7\_up
> 
> score\_6, score\_5, score\_4, source\_pony, low quality, normal quality, lowres,logo, watermark,

那SD3呢，我不给他加任何的画质提示词，直接裸奔。

所以其实最开始评测是有些不公平的，不过，真正的强者不需要我们的特殊照顾。直接来看效果。

1\. 第一组内容提示词，看一下语义理解能力。

> a cat,a destroyed badly damaged space ship,beautiful beach,broken windows, grass and flowers grow around,sunny,ocean（一只猫，一艘被摧毁的严重受损的宇宙飞船，美丽的海滩，破碎的窗户，周围长着草和鲜花，阳光明媚，海洋）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6WmyGGcG8YS9bzXvibfadcgDytMIgLzHc2miatClDF0FpSicQ0LTDXicvbg/640?wx_fmt=png&from=appmsg)

**SD1.5**：emmmmmm，这怎么成两张了，小猫咪看起来不太高兴啊，挎着个脸，海滩不太美丽雅，阳光呢？

**SD2.0**：不是，小猫怎么从船里长出来了，还有月亮你是怎么回事儿？不是说好的太阳吗。

**SDXL**：整体还行，但画面有点昏暗，配色不是很舒服。

**SD3**：王炸！语义理解能力极强，阳光明媚，美丽的海滩，鲜花……关键细节什么的都很好，画面也很和谐。

\-

2. 再来测一下相对位置关系理解，这个更加考验模型能力。

> a dog,hold hot dog,outdoors,grass（一只狗，叼着热狗，户外，草地）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6GIOOWR4OVLOnauc7f8WnMJgibQClFUEhzyjIxo1Y2lNOEjxvmYHFdxQ/640?wx_fmt=png&from=appmsg)

**SD1.5**：emmmmmm，这小狗的热狗怎么悬空了啊？你的热狗怎么成香肠了？

**SD2.0**：SD2.0比较聪明，他直接把热狗放到了地上，哈哈这样你就挑不出我毛病了吧，但是语义理解不对啊大哥。

**SDXL**：基本理解了我的意思，但是这个画风，以及这个舌头衔接太奇怪了吧。

**SD3**：王炸！光效衔接都非常自然，小狗很可爱，热狗也很有食欲。

\-  

3.测试一下二次元动漫人物。

> ((anime style)),1girl, indoors, sitting on the sofa, living room, pink hair, blue eyes, from back, from above, face towards viewer, playing video games, holding controller, white shirt, short, parted lips, anime production（（（动漫风格）），1女孩，室内，坐在沙发上，客厅，粉红色的头发，蓝眼睛，从后面，从上面，脸朝向观众，玩电子游戏，拿着手柄玩游戏，白衬衫，短，分开的嘴唇，动漫制作）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6DrE17BLMc501uLt3Oia5XXb48C6ttddGAUzfTmDAGFibb2WibfWxGpBKQ/640?wx_fmt=png&from=appmsg)

**SD1.5**：底模过于抽象。。。很多细节都丢失了，对比着看一下吧，从头发到眼睛。

**SD1.5**：千手观音？

**SDXL**：有点感觉了，但是你的画风画质很难评

**SD3：**没的说，依然是王炸！从头发到眼镜，从整体画质，到细节，No1！

动漫还做了另一组对比图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe62bVibKR5UTKsGAf4cjdvqcr8k9dVm6PAlYSnJhS4oLXoiaVqNfGL1urA/640?wx_fmt=png&from=appmsg)

你懂的= =

\-  

4\. 再测试一下不同的科幻风格

> robot droids, in the desert , colorful, dutch angle（机器人， 在沙漠中， 五颜六色）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6gQyU83DDQUq1ef8w7qLNZLlqXib5HjzatozNvHpHic7S9xL5aIH7yJlQ/640?wx_fmt=png&from=appmsg)

**SD1.5**：这机器人，是营养不良吧？哈哈哈  还有说好的五颜六色呢？

**SD2**：右边这哥们你的手臂掉了~其他不必多说了，懂得都懂嘿嘿

**SDXL**：还行，但是这个机器人怎么这么丑呢，三条腿不对称

**SD3**：同样很Nice，依然是王炸，除了这颜色跟我理解的五颜六色不太一样。

\-  

5\. 再测一组真人图片，难度也蛮大的，要求在水下。

> 1boy,underwater,green eyes,white skirt,looking at viewer（1个男孩，水下，绿色眼睛，白色裙子，看着观众）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6v2ALTXfL9W1bBqMP1pUQuaBicYuvAxiceU3y06HicEvVibsraHZ2MW4sHw/640?wx_fmt=png&from=appmsg)

**SD1.5**：恐怖片。。。

**SD** **2.0**：更恐怖了，有点像泡开的奥特曼。。

**SDXL**：还可以，凑合能看，就是这绿的啊。

**SD3**：非常NIce！

再测另一组真人的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6N61yNHVJj6Irf45OZjzkiaquIicGDWjYxse9Dms2qHMDTvOYiagvr5mwg/640?wx_fmt=png&from=appmsg)

\-

6\. 来一组风景。

> universe,stars,moon（宇宙、星星、月亮）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6TRcJFSaw5PRUMfAYvmZ90icnSUz9AiaibBVC0Licoc6LeXtDiaAeDYAv53Q/640?wx_fmt=png&from=appmsg)

**SD1.5**：有点像我爸的微信头像。。。

**SD** **2.0**：凑合，就是构图雪崩。

**SDXL**：SDXL是真的好容易画卡通。

**SD3**：这氛围就到位了。

\-

7.最后一个SD3最棒的，文字嵌入。

> Cyberpunk style,urban,1 robot,an electronic screen with“ Khazix”（赛博朋克风格，都市，1个机器人，一个带有“卡兹克斯”的电子屏幕）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6BHOZqRBu96XD1Fr99tzibniaskSS3WZvsQeQD85hN9oWff5cZcpD2a3w/640?wx_fmt=png&from=appmsg)

这个就不评价了，因为过往的SD模型，都不支持文字嵌入，目前SD3是独一份。  

上面简单对比完之后，你可以直观感受到SD3的威力了，也能感受到，Stable Diffusion这个模型，一路以来的进化史。

我都不敢想象加了高质量提示词，配合开源社区的微调等强大的生态，这模型可以有多强。

最关键的是，它开源，所以，他免费。现在他可以直接在你自己的电脑里用跑了。

不过我上面的测试都是在ComfyUI里做的，没错是这个样子。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe6uaicyXVVz8ZcuQXWhbXEtRNgT9bGvNgFjyADQNswzcJs8sibnPQCCdicQ/640?wx_fmt=png&from=appmsg)

我其实一直都没咋写过ComfyUI，不是觉得他不行，而是他太行了。所以他上手门槛比较高，对于普通用户来说，不如Webui直观好用。

就在我想该怎么让大家更方便用上的时候，小伙伴甩给我了Stability AI官方已经放出的一个Webui，叫做StableSwarmUI。

https://github.com/Stability-AI/StableSwarmUI

他实际上是建立在ComfyUI的基础上进一步封装的一个UI，非常快捷，导入工作流之后就可以直接使用了。

关键是，官方已经提供了一键配置环境文件（甚至提供了mac电脑和linux环境配置文件），也就是模型运行环境什么的都不需要我们自己去配置。

我们在这个的基础上，帮大家下载好了SD3模型并放置好了模型，简单弄了个整合包，可以直接打开使用。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe67sa42S65hQwueecLicypuKNaibyb57T1uvFNUbmQjBNuFYn13buiaQeFQ/640?wx_fmt=png&from=appmsg)

整合包我扔公众号后台了，**对着公众号私信“SD3”这个英文字母就有，使用教程太长，我也直接扔整合包里面去了。**

实测我的小4060，8GB的显存即可运行。

更骚的是，Stability AI为了让更多人能用上SD3，他们甚至跟AMD谈了合作，现在，AMD的显卡也能跑SD3了。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURormaDwyHtDicXJBmib9Jzoe634uLldgFfINPl5AkHaQ49nicFM5kxbxiarAQ7lpcKWfPbvCKLnusqg9w/640?wx_fmt=png&from=appmsg)

真的是非常亲民，从模型本身到模型运行的环境，Stability真的做了很多。

Midjourney虽然确实牛叉，但确实对很多国内的人来说，架起了高高的围栏，很多普通人可能连去给Midjourney支付会员的方式都没有

这时，Stability AI站了出来，说，“我来！”

Stability AI花了极高的成本训练了Stable DIffusion，开源了Stable DIffusion系列。

这也才有了之后灿烂的开源绘画社区，大家才可以把AI绘画模型实实在在下到自己电脑上，切切实实感受绘画的魅力。

昨天有一个小插曲，LUMA发布了他们的AI视频Dream Machine，宣传片是真的酷，激动的我在各大群里乱叫大家别睡了，但是上手一测，好像...也就那样...并没有太多额外的惊喜。

但反过来看SD，我属有点泪目了，每一个工作都是实打实的，从来也不过分宣传，时不时还给你小惊喜，比如前段时间的47s的音频模型也非常好用。

可能商业上，Stability AI做的很一般，被人们所诟病。

但是在开源生态上，他真的极大推动了AI界的发展。

可以这么说：

**Stability AI，在我心中。**

**才是那个真正的。**

**OpenAI。**

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言