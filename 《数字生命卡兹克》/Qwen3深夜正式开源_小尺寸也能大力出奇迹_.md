     Qwen3深夜正式开源，小尺寸也能大力出奇迹。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

Qwen3深夜正式开源，小尺寸也能大力出奇迹。
=======================

原创 数字生命卡兹克 数字生命卡兹克 2025-04-29 08:05 北京

> 原文地址: [https://mp.weixin.qq.com/s/NeW0tTACl1zZtzTOKFL8ew](https://mp.weixin.qq.com/s/NeW0tTACl1zZtzTOKFL8ew)

小道消息一直在说，昨天深夜或者今天凌晨，阿里会发Qwen3。

然后我特意早早的睡了一两小时，凌晨1点起床，就为了等Qwen3发。

结果这一等，就是好几个小时。。。

不过，功夫不负有心人。

凌晨5点，我眼睛都睁不开的时候，终于等到了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRRXF26JAzmyMDQBcoFfPjDv0MJL57tK8pk2UWaQheV2gdfbuEO27UnQ/640?wx_fmt=png&from=appmsg)

Qwen你赔我睡眠。。。

把报告看完，我总结一下，觉得最大的亮点有6个：

1\. 模型能力登顶全球，这个没啥可说的，就是No.1。

2\. 第一个开源的混合推理模型。

3\. 8个不同尺寸的模型，几乎覆盖了所有场景。

4\. 成本很低，旗舰模型235B参数部署成本只要DeepSeek R1的三分之一。

5\. 支持MCP协议。

6\. 居然还支持了119种语言。

一起说吧。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRKFvUTqzJtp6e2CYSuQ7PkWVLUVEq6nTvv7Fl3yQDv8OmHuoibjWlAiaw/640?wx_fmt=png&from=appmsg)

这次发了8个模型，Qwen3-0.6B、1.7B、4B、8B、14B、32B，这6个都是Dense稠密模型。

还有两个重量级MoE模型，Qwen3-30B-A3B，和旗舰版的Qwen3-235B-A22B。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRLKhIR1avtNKhG6YuT0rjB54V1jQwkcro4s6Zbzv6MdOmXEmZnP54Kg/640?wx_fmt=png&from=appmsg)

这次Qwen采用了新的命名方式，Qwen3-0.6B、1.7B、32B这种没啥可说的，大家都理解。

两个MoE模型，把激活的参数写在后面，Qwen3-235B-A22B的意思就是235B的参数，但是在推理时只激活22B。

Qwen3-30B-A3B就是总参数量为30B，激活参数3B，这个还蛮有意思的。

而且，所有的模型，都是混合推理模型。

大概的意思就是，你既可以把它当不会长思考没有思维链的普通模型用，也可以直接开启推理模式，变成一个推理模型。

可以简单的理解为，把DeepSeek V3和R1直接揉在了一起。

就像我们其实都知道，DeepSeek这个深度思考，你打开的时候，是R1模型，但是你关掉，其实用的是v3来给你回答。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRRdmVXV6j34D8PJlwBQ67oXPDrI9XpnEURibV3JPjFCRtBE0GL9K42Gg/640?wx_fmt=png&from=appmsg)

但是Qwen3，是一体的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YR2F5ic1vEyNp8fWwYyicsqyicm7NvkA2MQATcibe6XfIciaWyD2UXiaibESfxw/640?wx_fmt=png&from=appmsg)

是一个模型，只不过支持了两种模式，这个不管对于开发者还是使用者，都方便很多。

整体上，8个模型，诚意足到爆炸，小到0.6B，大到235B，能打手机端侧，也能打旗舰体验，全部一次性开源了，而且都是Apache 2.0协议，想怎么用就怎么用，想商用就商用，没啥顾虑。

Qwen3-0.6B~4B的最大Token都是32K，其他的都是128K。

性能上，稍微有点离谱。

Qwen3-4B的小模型，就已经能和上一代QwQ-32B这玩意打得有来有回。而Qwen3-30B-A3B，更是几乎就比QwQ-32B全方位的强。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YROic1xLlOz0B5ROjvBeeHkrpqp5ZRsHD87PFaGfiaxJTQtF60LKgFnibKw/640?wx_fmt=png&from=appmsg)

至于最牛逼的那个Qwen3-235B-A22B，他们甚至没只跟开源模型比，比的全都是最顶级的闭源模型。

最主要的是，这玩意部署成本，大概只有DeepSeek R1的三分之一啊。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRn18OxrtzfoTHP4xLkE6ic1hicsoml64PpWpIk5gC9Fib3AfCYaRiapcE9A/640?wx_fmt=png&from=appmsg)

什么叫便宜大碗，这就是。

但是这么一对比，忽然发现，Gemini2.5-Pro，好像有点猛。。。

同时，在性能水桶式提升的背景下，也有了更强的Agent能力，也支持MCP了。

他们官方自己放了一段视频。

我也随手把即梦接了进去，可以直接用Qwen3来调用即梦画图了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YR4dnogTacBiaL5GVkibTmWf0blPXxDuxEBrvWlKghEDBEDia0Hma3Rgg9g/640?wx_fmt=png&from=appmsg)

就还真的，挺好玩，你的下一个即梦，又何必是即梦呢（狗头。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRy26j4UvsEDvs6f9h0VjxOlQvCte4g1jUbuEDv66ibQNFG5CGa2gejOg/640?wx_fmt=png&from=appmsg)

除了这些模型的能力，Qwen3这次还有一个很有趣的东西。

就是语言。

上一代的Qwen2.5，只支持包括中文、英文、法文、西班牙文、葡萄牙文、德文、意大利文、俄文、日文、韩文、越南文、泰文、阿拉伯文等 29 种语言。

而这一次，支持119种语言了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRO97pE5OmA4ryd1RETSDAg7XEVdDEKMTzp4LicwDibYNR1qM9ibYp1OIIQ/640?wx_fmt=png&from=appmsg)

不是，到底谁才是真正的OpenAI啊。

这妥妥是为世界人民谋福利好吧。。。

项目地址都在这了。

Blog: https://qwenlm.github.io/blog/qwen3/

GitHub: https://github.com/QwenLM/Qwen3

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRXTM66tibYgrrnEb6jE7twciacINlteA9nX85IyHOCeynnUiamTfBpf5wQ/640?wx_fmt=png&from=appmsg)

你牛逼的话可以自己部署，我5080勉强跑个Qwen3-8B，实在跑不起。

想体验的话，可以直接去通义和Qwen Chat，都可以。

通义：https://www.tongyi.com/qianwen/

Qwen Chat：https://chat.qwen.ai/

我自己直接在Qwen Chat上面实测了一波，一进来左上角就默认是旗舰版Qwen3。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRNR6ox8LZZ9THV2t4biaAZtAwOfhfibjzgeUibWX6pe4KEotQjuldMaNjA/640?wx_fmt=png&from=appmsg)

嗯，就是比较抽象的是，提示语都居然都变成早上好，卡兹克了。。。

你可以在左上角，切换3个这次Qwen3比较有代表的模型来进行对比。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YR9bjFMPyyovYLzIVLHadHxtFayAic7ksIJljxYBKTnANzAnogowWWejg/640?wx_fmt=png&from=appmsg)

左下角的深度思考，就能是否开启推理的开关。

而且这个开关还能拖动滑块，决定它的最大思考长度，虽然这个功能很极客，但是还有意思。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRdZ0GuDbT5bIYFYlyoY7DRvian7p2lR7uPWoDIT82PfSQqJ86XCekX8g/640?wx_fmt=png&from=appmsg)

我自己的实测结论就是：水桶级别，中等偏上。

比如让它给我生成一个登录页。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRfuUpIvcW93aLy7vQibibbxgkqS0RNKlNobXuHGlVN7k4Gokfx0OjTEOQ/640?wx_fmt=png&from=appmsg)

效果很不错，能直接干出一个很酷的界面。

https://us4mpg09fz.app.yourware.so/

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRUB4KQp3LT3OBh2Vc9abnDGXEV7ArDMLTKvIZ4KlIpBjsERFIWcrR0A/640?wx_fmt=gif&from=appmsg)

或者做藏师傅搞得可交互的网页，把吃瓜PDF变成在线时间线。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRbmdaMr6n9TYfnU5AqnvMAZoBtIT5g5LnufnF1KTeWBrDDfRWCNcMcw/640?wx_fmt=png&from=appmsg)

这时候你就会发现，审美会差一点，丰富度也会不是特别狗，稍微有一点点勉强了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRCuiaegTYktDm9ibkL95ZIVib1B3f4NMQt8dPch87E8gbfO1Rqmiaia0Xn8g/640?wx_fmt=png&from=appmsg)

藏师傅之前的可视化网页Prompt如下：：

    我会给你一个文件，分析内容，并将其转化为美观漂亮的中文可视化网页作品集：

而如果再让它写一个之前我在文章里放的洛小山的弹球游戏。就确实没有那么亮眼，在游玩的时候还有一些些BUG。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YR6IqfYJtFnED28BeSSX7d2gHLhbPiaBOmxzQaoGATgcAtYPbJFljzSXg/640?wx_fmt=png&from=appmsg)

但是毕竟这个游戏还是太复杂了，人模型的尺寸也没那么大，也没法既要又要。

如果是做稍微简单一点的连连看游戏，就还是比较简单了。

    <!-- 生成一个记忆翻牌游戏，要求：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRa7hIocgk1pXRkee54icgqW6Mt9FwRCqE2nnzLoibib9kphUAicpxsQfxeA/640?wx_fmt=png&from=appmsg)

除了代码，逻辑问题，现在基本也不太能难道现在的推理大模型了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRnedZMicqH1M8fykLU4MbyV1EqyOtZkoIaqPU8VlTRv1GI5xAkrsBsXw/640?wx_fmt=png&from=appmsg)

不过在遇到一些非常离奇非正常的测试prompt时，还是会有一点点掉智。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YR4SSL3f4woqvE3bQPNibnaamtFfyQsRmacRyIfpMw27Mv5kpoE06xrtw/640?wx_fmt=png&from=appmsg)

文笔的话，亲测会比DeepSeek好一些。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRFu47mjyy6zCcCZEPaEtwCvKRtsXuTMXuQV0amQQkb2CkDJEoz3K0mg/640?wx_fmt=png&from=appmsg)

但是略逊于GPT-4o。

如果你还想玩一点花活，还能跟即梦打通做结合。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRZINW5Hk6sOVxibNEywU3RyUkt8NXqEnFhdOu5Lebe16Fib64PzoLicOxQ/640?wx_fmt=jpeg&from=appmsg)

就能实现类似于那种原生多模态模型，图文混排的效果。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrgmcHYkNoia5nWWl1FCD5YRZNh5fs8SmH6Vqurv44cGY7JaJkAP6vgiazic2SbPr0PH90StUMkc11og/640?wx_fmt=png&from=appmsg)

还是超级有意思的。

总之，这次Qwen3的发布，真的有点像是深夜街头，突然亮起的那盏霓虹灯。

不仅亮，还便宜。

不仅便宜，还能库库的切换颜色。

这一波下来，阿里确实是拿出了一种很阿里的态度。

8点了，天也亮了。

该去睡觉了。

最后。

Qwen3，欢迎来到这个荒诞又灿烂的时代。

咱们，下个奇点见。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、dongyi

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言