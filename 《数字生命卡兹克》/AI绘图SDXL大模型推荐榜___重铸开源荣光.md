     AI绘图SDXL大模型推荐榜 - 重铸开源荣光 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI绘图SDXL大模型推荐榜 - 重铸开源荣光
=======================

原创 数字生命卡兹克 数字生命卡兹克 2023-10-02 15:32 安徽

> 原文地址: [https://mp.weixin.qq.com/s/iFofSAWxJraJxQa\_0\_fpUQ](https://mp.weixin.qq.com/s/iFofSAWxJraJxQa_0_fpUQ)

7月份我写过一篇SDXL1.0大模型的评测：

[SD全新开源模型SDXL1.0评测 - 留给Midjourney的时间不多了](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647659092&idx=1&sn=9c5a8461ea95f2c77b7052713410b30e&chksm=f007ce03c77047153e1c24300bd71c1fbe0057b1016d5cce4f2eb0b0fa95f5f1768864411def&scene=21#wechat_redirect)  

前两周Stable Diffusion WebUI1.6.0发布了，新增了很多对SDXL生态的支持。

而ControlNET也对SDXL的支持也逐渐稳定。  

SDXL的生态终于有一点起色了，我也觉得是时候，可以来写一篇SDXL的大模型推荐了。  

在推荐之前，以免大家混淆，所以这里再做一个简单的小科普：

现在的所有的SD的大模型，都是基于stability.ai发布的开源模型Stable Diffusion进行微调的，而Stable Diffusion本身有很多个版本。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpKCz3FAibas3Csrpib1ENb49cT9kB33lGkO4VJTJ4PuFcqdm7zqVbqc9ZIyZ4l8U0JNUsNS40SxFkw/640?wx_fmt=png)

对，有这么多，但是基本都没人玩，只有SD1.5屹立不倒，你不管在Civitai还是一些其他的模型站上，99%都是把SD1.5当底座进行微调或者融合的。

而SDXL1.0是今年7月新发布的大模型，参数量比SD1.5大将近7倍，语言模型也“抄”了OpenAI的CLIP可以写大长句，他的上限比SD1.5高太多太多了。

现在，我就来盘点一下我最近使用下来，认为很棒的基于SDXL1.0微调出来的模型推荐。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpexK6oPzPfmCicQV2B25a0ib6hFibEJf2ibuicE0x0vib6JCvDkoY5B0VWg5A/640?wx_fmt=jpeg)

**大模型：**  

1.  DreamShaper XL1.0（通用写实，对标MJ5.2）
    
2.  SDXL\_Niji\_Special Edition（通用卡通，对标Niji5）
    
3.  LEOSAM's HelloWorld 新世界 SDXL（亚洲真人）
    
4.  DynaVision XL（通用3D）
    
5.  Microsoft Design SDXL（UI图标）
    
      
    

**LoRA：**

1.  Juggernaut Cinematic XL LoRA（电影感）
    
2.  InkPunk XL LoRA（墨水朋克）
    
3.  Voxel XL LoRA（体素风格）
    

老规矩，我已经帮大家全部都打包好了，对着我**公众号****私信“SDXL模型”**，后台就自动发你模型整合包了。

  

**大模型**  

**1. DreamShaper XL1.0**

DreamShaper可以说是SD生态里面的顶流和常青树了，SD各种模型起起伏伏，只有DreamShaper屹立不倒，至今为止最为全能的SD大模型。

DreamShaper XL1.0直接可以对标Midjourney 5.2，也是我现在用的最多的大模型，没有之一。

SDXL1.0版本与基于SD1.5训练的DreamShaper模型相比，DreamShaper XL1.0在图像生成质量和清晰度方面均表现极佳，可以直接看我下面跑的效果图。推荐必装。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpgsibVpN1tH0ktRataXprxGDgs9SfwnoD1JqIibgbAfbPBItUqnbPYCTQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpQpvEZaaWslPIQpgIVicm8CbJ13yo96cfTedMgJaW4hqlHzaHCGGu64g/640?wx_fmt=png)

**2. SDXL\_Niji\_Special Edition**

如果说DreamShaper XL1.0是直接对标的Midjourney 5.2，那SDXL\_Niji想必你也能猜出来，是对标啥的了。

相比Niji5，有过之而无不及，SD生态里表现最好的卡通大模型，精通所有卡通风格，你的每一个创意，都能在SDXL\_Niji\_Special Edition的世界里找到最完美的表达。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpWqO4XF8m2N47MDGcCiaLPPjCxaUSWDc5zjzYTs0jNxoXyl8AYpqgpfA/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpvr6ib1SjeICIHzyKiaVbgN2QEHlPYaLQG59r2AtQnOzxlg6rNGICPia6Q/640?wx_fmt=jpeg)

**3. LEOSAM's HelloWorld 新世界 SDXL**

“HelloWorld”一个全新的逼真的SDXL基础模型系列，拥有极高的肖像的真实感和电影般的质量。用作者的原话说就是：

“由于SDXL的信息量和文本理解能力远远优于SD1.5，HelloWorld是一个旨在逼真描绘所有事物的基本模型，或者换句话说，我希望使用HelloWorld逐步构建一个虚拟摄影世界”  

**需要在prompt上写上“leogirl”进行模型触发**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpEwtlNNPkS8kOMTmMRtM5zic2svtj97zWRr5zDDMcjNZDy9sGv0iaokrA/640?wx_fmt=jpeg)![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpjgYcKqsDfwZZuSI3oxfsoGLccsx2RzBiauOxtDILpSYX6CIoG0ibzYiaQ/640?wx_fmt=jpeg)

**4. DynaVision XL**

3D特化模型，对于风格化3D模型输出表现极佳，如皮克斯、梦工厂、迪士尼等等。比较有特点的是对于动物的处理也很好。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpXehEC3iaOazRd01vfhH2H3IJ1DZf6925ibuL76mLfy8P6ps8UJpsXOPg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hphIvwb7EcZVIQ1hps94nZicmntd6asF5My2xw3PQicYgvY8TuKsKibTrgA/640?wx_fmt=jpeg)

**5.Microsoft Design SDXL**

很少会见到针对UI领域特化的SD大模型，Microsoft Design SDXL是国人针对3D UI图标专门训练的模型，偏微软风格，弥散的色彩。

虽然整体风格泛化能力目前较为单一，但是出图质量较高，且填补了这个领域的空白。依然推荐。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpictT2p6xtqHsFuPQfkVIJTW40zLxE9empUzM0I2GdGJfbBohHypicv8Q/640?wx_fmt=jpeg)

  

**LoRA**  

讲道理现在SDXL的LoRA生态真的还挺不完善的，两个SD1.5生态的顶流神中神：Detail Tweaker LoRA（细节调整）和epi\_noiseoffset（增强光影）没有一个做了SDXL生态适配的。此处只能推荐了3个偏风格化的LoRA，也实属无奈之举，功能化的LoRA我自己测了十几个，没一个能用的，还是得等大哥回归。

**1. Juggernaut Cinematic XL LoRA**

电影LoRA，旨在为图片增加电影质感的光照、对比、色彩、皮肤质感等等。我自己测了几十张图，整体审美很棒。

还在早期阶段，刚推出1.0版本，后续可以持续关注。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpMuWicpayyIBHPiaVKHCVPEAMFk9yUcM4Tl3xRywEAg3eV4CUYXzNOj2A/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpubzoia1BHqTXXxUNiau2Xw8iaauphhs8J2ibgQKF8YWjSGTRwJYF0Vb0jw/640?wx_fmt=jpeg)

**2. InkPunk XL LoRA**

墨水朋克。一个很有意思的艺术风格，前卫+复古。

出来的场景和画风很有特点，我个人挺喜欢的，有视觉识别度。最好的使用方式是Prompt开头加上“inkpunk style illustration”，然后用LoRA权重作为结尾。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpmJsicgNBo6XyCcQAJufImibpYE4baQmQNGPQFJYfj57nV6FuIYLjPw5w/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpAdf0rxWWIuN4VhDVNJIzjITSotyPjI4EHylK6ON1spzUsxZDemmzAQ/640?wx_fmt=jpeg)

**3. Voxel XL LoRA**

我很喜欢的体素风格，6年前我第一次学C4D的时候，一个建模就是体素小人哈哈。《我的世界》就是这种风格的。

能把整个世界都变成一个一个小方块，很有意思。

并且，体素风格+Pika有奇效。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpLcGaGIBuN4XibdROe04rD7OTRpRfFpOL0lhjWvSJPkGJjycujamNrJg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hp7M1jUNM9cLiaNuCfAy4yicGmC0bPGDJFkjicPSOcAicK7aWWUQErH1WGbQ/640?wx_fmt=jpeg)

这些，就是这一期的SDXL大模型推荐了，5个大模型，3个LoRA。

对着我**公众号******私信******“SDXL模型”，**就有所有模型的整合包下载了。

不过有一说一，SDXL的硬件要求确实太高，不一定大家都跑得动。所以我在仙宫云上也部署了一个我搭好的有这些模型和各种插件齐全的SDXL镜像。网址在此：

https://www.xiangongyun.com/register/V76GG5

在部署时后，在社区镜像里面搜“卡兹克”就有了。实在不会用的去看我以前的这篇文章：[你奶奶都会的云端SD部署教程 - 白嫖4090、无需代码、一键启动](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647659270&idx=1&sn=c8ed154119f8d37eb8458bf05f83b9fc&chksm=f007cf51c770464703de115eb4c2461ceba429d4a55ccc3cf94617f9de8daaf52b40e1be585a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoyjZn7n0XDPYCL7R7g22hpibCf9Xz6vtugBIKzjv169SZAvxibjEXBNMupAFo53ykqCqaYLs2NpCSw/640?wx_fmt=png)

最后我想说一句，AI绘图三足鼎立的势态基本已经成型了。

拥有极强审美和泛化能力的Midjourney，拥有最强语义理解能力和多模态能力的Dalle3，拥有最强控制能力和蓬勃生态的Stable Diffusion。

这三者，至少未来一年，都是三足鼎立，都是不同的用户群，不同的擅长方向。

他们完全是可以互补的，都可以为我所用，不是谁就必须要干掉谁，谁一下就干死了谁。微信干死了QQ吗？京东干死了淘宝吗？抖音干死了快手吗？  

拥有一颗炙热的心，保持一个包容的心态。  

对世界永远充满好奇。

或许会更好。

**以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，并给我个星标⭐～感恩。**

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言