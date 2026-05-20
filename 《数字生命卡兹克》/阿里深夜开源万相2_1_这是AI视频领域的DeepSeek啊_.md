     阿里深夜开源万相2.1，这是AI视频领域的DeepSeek啊。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

阿里深夜开源万相2.1，这是AI视频领域的DeepSeek啊。
===============================

原创 数字生命卡兹克 数字生命卡兹克 2025-02-26 06:08 北京

> 原文地址: [https://mp.weixin.qq.com/s/oOFxhXb3EwdiEKNIJ6EN7g](https://mp.weixin.qq.com/s/oOFxhXb3EwdiEKNIJ6EN7g)

昨天的AI新闻有点太密集了，肝快废了。

凌晨2点半，Claude发3.7 Sonnet，凌晨5点半，阿里发了推理模型QwQ-Max的预览版，早上10点DeepSeek开源了一个DeepEP代码库，然后晚上10点20，阿里的视频模型万相2.1，也来了。

而且，正式开源。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6ictRKVibX9wUibLjldbkicBCJc8OSPiaxLIDTvQvdZ6C1F5AS2wYriaicy3CQ/640?wx_fmt=png&from=appmsg)

2月25号是什么黄道吉日吗。。。  

万相2.1开源链接在此：

Huggingface的：https://huggingface.co/Wan-AI

GitHub的：https://github.com/Wan-Video/Wan2.1

阿里，真的也是“源神”。

这次上线的有四个模型，文生和图生各俩。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j63PqkD1OfDia1fH4ohLNWITkdKCVVESVT2mJZib1OUl6b9wCUpNY1YKog/640?wx_fmt=png&from=appmsg)

文生视频模型有1.3B和14B两个规格。图生视频模型都是14B，分辨率一个480P一个720P。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6y4a1EP8r7hxgWjKstO3pI54IdVEf0BzPq9KHp4DRzmAgCGad4akrog/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6h6Sxz8ibwTGWu9yMwTFWicBP13Wwc05FwlNrLqzdRKW108sGWXbh3oSA/640?wx_fmt=png&from=appmsg)

这回比较让人惊喜的是，低配置的模型真的小，1.3B的模型，只需要8个G的显存就能跑了，也就是说，本地的4060都能跑得动了。

如果你有4090，跑一条5秒钟的480P视频的时间大概只要4分钟。

说实话，在年前的时候，万相2.1就已经上线通义万相了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6NFtX4gRL2BYOicxBnib9062mYmc8gpJFfdLVafIGTY7LgencVRkRIicWQ/640?wx_fmt=png&from=appmsg)

只不过叫2.1专业和2.1极速版。

**这块在我测试下来，专业版和极速版其实都是14B的，只不过专业版感觉是原生720P，极速版是直出的480P然后超分到720P的。**

而1.3B是这次为了本地部署特意出的，所以线上目前还没有体验渠道，想用的话，只能自己部署。

我也第一时间跑了一些case，14B因为太大了，我直接用线上的通义万相来跑的。**1.3B我是直接在魔搭上部署了跑的，还是比较简单的。**

https://www.modelscope.cn/models/Wan-AI/Wan2.1-T2V-1.3B

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6uHMzLQDtpOkp5uGjUrwjnUVEKzvKUwadjeiawnyGK15nkd4POhZWrcw/640?wx_fmt=png&from=appmsg)

**整体效果上，语义理解、物理****真实性****、复杂运动**的表现，万相2.1 14B在开源视频模型里绝对是第一梯队，而1.3B别看小，但是使用门槛也低啊，在实力上也真的完全不含糊。

直接先上一点我们跑的case。

首先是长文本和Prompt的语义理解表现不错。一连串动作，都能按prompt顺序挨个儿给你实现。

Prompt：空镜从卧室顶部45度俯拍,一位女子躺在凌乱的床上。清晨阳光透过百叶窗在她脸上投下条纹状光影。她闭着眼，用手揉眼睛。然后睁开眼睛, 微笑。

**14B效果：**  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6pqOgZnDhTP555fdJkTTwgjtP70UzQI7FTxezxPJZN3rtEty9VXImqA/640?wx_fmt=gif&from=appmsg)

**1.3B效果：**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6zM6MkFo2qbMEoalDCicLib8Rt0AIONgwYUwUqq68AsiaF8FZr4lARvFYQ/640?wx_fmt=gif&from=appmsg)

物理规律和质感表现也挺不错，这个切柠檬的影子变化、刀面纹理，还有切下去的质感，真实感拉满。

Prompt：高速摄影拍摄一个新鲜柠檬被切开的瞬间。镜头推进，从中景到特写。锋利的银色水果刀从上方切下,柠檬汁飞溅而出,形成细小水珠。特写画面呈现柠檬的横切面和果肉纹理。

**14B效果：**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6PObzicqrv0KIb1W7fALicQgswvPPUiaWglnK6SRUtXIRPMvibiczRqOvJnw/640?wx_fmt=gif&from=appmsg)

**1.3B效果：**  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6uKuN7MKDzibSzjWHf4qXWZpetO9FtZofG5B22Pticg0yNc9nC8Hh2HEA/640?wx_fmt=gif&from=appmsg)

然后就是万相2.1刚上线通义的时候，不少人吹的运动表现。

我测下来，虽然还说不上是版本T0，但优点确实也挺明显。大幅度的动作、旋转还有动作的速度，都很猛。

Prompt：在冰面上，一位 18 岁的中国美少女明星短道速滑运动员熠熠生辉。她五官玲珑，神色自信，肌肤胜雪，高马尾充满活力。她身着一条薄荷绿的超短薄纱裙，裙摆随风飘动，上身搭配白色露脐运动背心。以全景镜头俯拍，通过轨道车拍摄跟行。柔和的淡蓝色灯光从斜前方洒下，光质轻柔，光比偏小，营造出清新的氛围。她身姿矫健地疾驰，临近终点时采用推镜头特写其坚毅的眼神和快速摆动的手臂。 

**14B：**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6k9ibPjI33SicSWCF4SmibrmowLvxmbmzPBOz8FafLDH71K5g1QWINo2VA/640?wx_fmt=gif&from=appmsg)

**1.3B：**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6C5HKhSVEusQWtWuYza65Qty8MaUp3iclHA1ohwBSICe9urDT9PX4Wqw/640?wx_fmt=gif&from=appmsg)

2.1还可以直接实现运镜效果，连复杂的遮挡物运镜都行。

Prompt：低机位拍摄图书馆书架，前景书本缝隙间闪过金丝眼镜的反光。当镜头水平移过三格书架，穿灰色毛衣的男生恰好转头，看向镜头，手中悬停的棕色书本封皮_。_

**14B：**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6HWiajMibj9JFCRGlseXeSiayVrGBSPU3eSYzicZx8KsL5sqbXDl6z0goJw/640?wx_fmt=gif&from=appmsg)

**1.3B：**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6X5AmLLia95olQfvIyzSMGOS1JOtKLxJAiaFrlv6DHTFA9hydGSkHbYpw/640?wx_fmt=gif&from=appmsg)

还有必须提一下的文字生成，万相是全世界第一个能直出中文字的，现在能在AI视频里，直接生成中文的AI视频模型太少了。

Prompt：以红色新年宣纸为背景，出现一滴水墨，晕染墨汁缓缓晕染开来。文字的笔画边缘模糊且自然，随着晕染的进行，水墨在纸上呈现「福」字，墨色从深到浅过渡，呈现出独特的东方韵味。背景高级简洁，杂志摄影感。

**14B效果：**

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6Zmk1styqcEibOXu806XsMnQjSUIxhgY30JUMS8CEt7hdiavQYoPcjAjQ/640?wx_fmt=gif&from=appmsg)

**1.3B效果：**  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j66C3sl534GicibPwZJmEIk1BDOIicFpe7hm3tT65wtTiaebv9QjT3daRUkA/640?wx_fmt=gif&from=appmsg)

不过文字生成还是有待改进，亲测目前只能支持生成非常简单的、笔画数少的中文，可以实现的字体也比较少，复杂点的文字内容还是容易出现乱码和鬼画符。不过没关系，这只是刚开始，万相继续加油吧，这个方向是非常实用的。

整体来说，万相2.1语义理解和物理表现都很稳，画面审美也在基准之上。

而且不要忘了，这玩意可是开源的。。。

对与生态的加持，想象空间太大了。

如果你现在想用万相2.1的话，有几种使用方式。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j60UKYC9ny0ZTh1KbTwUec3vFCRIamav2EktDPSfAcQAibEMorIbHOARg/640?wx_fmt=png&from=appmsg)

先说14B的，14B的你可以跟我一样，直接去官网免费用，每天签到有50灵感值，如果你在APP上跑一个视频的话每天可以再加50灵感值。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6l2SCoQDDkG3kIkoZNS5foKIxXykrYay2WFlic0EQENPUyk5Tynftmmw/640?wx_fmt=png&from=appmsg)

1个专业版（14B 720P）的视频，5灵感值，也就是说，你其实一天可以白嫖20个视频了。

然后就是Hugging Face上的demo，虽然是可以所谓的无限免费用，但是算力太少人太多，基本约等于用不了，可以直接放弃。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6lMub2rILEc42VSIsfqsIcdqG4OY8dwzfQthM85Ggj8AkeMonrc6reQ/640?wx_fmt=png&from=appmsg)

还有就是去阿里云百炼，接API用：

https://bailian.console.aliyun.com/model-market#/home

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6ReNzlgAEzuqWIdVRVRUl2KdvjDWOOtwskM7ApjNbVcAc5GT4n53W5g/640?wx_fmt=png&from=appmsg)

价格的话，Plus（2.1专业版）是每秒0.7元，Trubo（2.1极速版）是每秒0.24元。

然后就是1.3B，如果你本身有8G以上的显卡，那就无脑直接本地化自己部署就行了。

具体的可以去他们github上看。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j6QJuqu1wMtPKU1Wbl2e0tQibMeOlweV0gfPH98yiaTt8eNLom3fLdTLHA/640?wx_fmt=png&from=appmsg)

其实我最期待的，还是关于ComfyUI的集成，如果这能接进去，那就可以玩很多的花活了。

最后，我还是想表达一下对阿里的敬佩。  

AI领域的半壁江山，现在几乎都是阿里的。

Qwen作为老大哥遥遥领先，新秀万相补上AI视频的空白，现在全世界，都知道了阿里的名号。  

而且不止是AI圈，金融圈，更是因为阿里在AI上的策略，全世界的资本开始重新关注过来。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURrOaEK7KFPwQKJam6hZ76j69fHMER28Dhdx68nQevgFuUYm84vz1yiaLT6BWgIwtmBcMRU4fScx0zw/640?wx_fmt=jpeg)

你就看看阿里涨了多少吧，带着恒生科技和中概互联又飞了多少吧。  

中国资产的全面复苏。  

正是因为前几天阿里炸裂的财报，还有AGI的决心，让全球的投资者都认识到，中国的宏观、行业、企业在节点上，都已经完成了对齐。  

顺带也告诉全世界：  

**我们不只在跟跑，我们也开始在领跑了。**

未来肯定还会有更多挑战，但如今，我有理由对阿里，对DeepSeek，对整个中国的AI产业抱以更大的信心。

最后，用一句话收尾吧：

源神之名。

当之无愧。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、稳稳

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言