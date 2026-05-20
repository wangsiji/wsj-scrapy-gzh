     AI绘图傻瓜指南 - 5分钟教你做出绝美的AI二维码 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI绘图傻瓜指南 - 5分钟教你做出绝美的AI二维码
==========================

原创 数字生命卡兹克 数字生命卡兹克 2023-06-29 20:14 天津

> 原文地址: [https://mp.weixin.qq.com/s/9AgkkJy81jJ2wO-xa3Fcgg](https://mp.weixin.qq.com/s/9AgkkJy81jJ2wO-xa3Fcgg)

事情是这样的。  

粉丝看到一个很炫酷的二维码，在另一个群里问了一句，有没有教程，然后对方说星球有，加星球就能看。。emmm

这个东西前段时间我正好研究过，这不巧了。

于是我就来写一篇关于AI炫酷二维码的喂饭教程。  

实现的效果大概是这样的。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrD5By2YyoOBJdfibTbvDEXaFnlff4OnicBpkWBic82PDYc6LtbXcHGqO0B2Yk17yYsAGUK8zI5YgVjA/640?wx_fmt=png)

还有这样的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrD5By2YyoOBJdfibTbvDEXaH3TjXZueEJ6ZNUcQ4sgnp20r7rrr2wZ2icjBm0XpTeIBibgZmSsqfZsg/640?wx_fmt=png)

思路和做法简单来说，就是用草料生成一个二维码，然后用StableDiffusion+ControlNET进行定点重绘。没用HG上封装好的那种是因为没法用自己的模型和LoRA，实在太丑了。。。

**步骤和参数已经调好了，不需要太玄学的抽卡，成功率60~70%左右。**

话不多说，直接开始。

首先我们先去草料上生成一个二维码，网址在此：

https://cli.im/  

按你自己的需求生成一个什么样的二维码，教程案例就是给我自己的公众号做。  

这里我说一点能让二维码更容易被识别的小技巧。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURr7w3MkqYqtYhW4RMjpx1Xjic96IgZhO48PJ84Sudz0J4KmsxiaDCMcQjYZugtcHFRicLovC5BZWZxkw/640?wx_fmt=png)

这块的容错改成30%，尺寸改到500\*500px。

然后重点的来了。

**点进去二维码美化，把码边距改成4个色块，你会发现二维码的白色边距变大了。**  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURr7w3MkqYqtYhW4RMjpx1XjQNUHrsyLvLaQaficOZHwCatoRocVj5ibE9uQJ70hCkCnS1Y0VRjiae4Rw/640?wx_fmt=png)

这个小操作，能提升很多最后扫码成功率。你们也可以日常中也可以回想一下，有时候离得太近了，二维码扫不出来，但是把手机拉远，是不是就行了？一个道理。  

想要二维码变好看不用这个大正方形的，也可以自己去设置里面改，比如我就生成了圆形的。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURr7w3MkqYqtYhW4RMjpx1XjOn0XI2yZJev2roU23FguG1GWx67q9AgbtsCGpwKSrcRYGn0ibF33msA/640?wx_fmt=png)

OK，二维码准备完毕，**接下来我们需要下载两个SD的ControlNET模型，我已经打包好了，关注我，后台私信QR就自动发你了。**  

如果不懂SD和Control的，请去看我之前的两篇教程，虽然写的有点早，但是一个样。  

[AI绘图傻瓜指南 - 5分钟带你生成你的专属AI妹子](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647657700&idx=1&sn=5b873ca094b1b968de6964cd2045fdc3&chksm=f007d0b3c77059a5fea876d9379579114a942b302b1bd0c164a438ebd6829518e9de61e8704b&scene=21#wechat_redirect)  

[AI绘图傻瓜指南 - 5分钟教你用ControlNET让妹子摆出你想要的pose](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647657853&idx=1&sn=51752aa058de04d582ff2719f3fceace&chksm=f007d12ac770583ce11b85badbfcf67a759675787f71254bf83442817ea1fc5f87c37fe39a18&scene=21#wechat_redirect)  

ControlNET模型下载下来目前基本都是放在这个路径下：

sd-webui-aki-v4\\extensions\\sd-webui-controlnet\\models

打开我们的SD。  

正常选择我们的模型输入我们的咒语，模型我直接就用的我挺喜欢的GhostMIX。  

这里有几个关键参数注意以下：

**迭代步数 (Steps)设置到15，采样选择DPM++ 2M Karras，图像大小设置到768\*768。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURr7w3MkqYqtYhW4RMjpx1XjE5HbhXVc4tXMpCD13veNX7DLZE2OC7ZQ53j8StVFGr8UCC72oBWHGg/640?wx_fmt=png)

设置好以后，我们打开我们的Control，把二维码传上去，然后我们需要用到**两层Control**去控制，参数我已经调好，照抄就行。  

第一个Control，允许SD重新着色，用以下参数：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURr7w3MkqYqtYhW4RMjpx1XjB1KEbGH14jugiakick4y50lrXAgNUjDic6cKtoIia4fia8IToozxV712pjQ/640?wx_fmt=png)

预处理器：空  

模型：control\_vlp\_sd15\_brightness

权重：0.3

介入时机：0  

终止时机：0.2

\-

第二个Control，生成图像，用以下参数：  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURr7w3MkqYqtYhW4RMjpx1XjCEtdXPFDHOlGMxnsKuLibGiauQv2e6AiaaHpI8pviaVgmsic0ceoF5NMNKg/640?wx_fmt=png)

预处理器：inpaint\_global\_harmonious

模型：control\_vlp\_sd15\_qrcode  

权重：1.1~1.3  

介入时机：0.15  

终止时机：1

OK，一切准备就绪，我们直接开跑一张。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURr7w3MkqYqtYhW4RMjpx1Xj0fryMDiaC1GmZ0YiaWwMibNNAL5Iia2KtTa2QCDHxGPyOgzSYT12GdcJEg/640?wx_fmt=png)

扫扫试试。一把成~

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURr7w3MkqYqtYhW4RMjpx1XjFd6Y4Ib9CsmDwteM9rgk30KnSSq2EfWDSXibVX3csKYiasV18TRvpjAQ/640?wx_fmt=png)

  

你们也可以去做自己喜欢的二维码~在这个新奇的年代，这种二维码还是很有趣的，至少很吸睛。  

但是回到实际，AI二维码的实际应用场景，除了好玩、新奇，我认为千万不要偏离了他最核心的作用 - **提示用户这是个二维码，这是可以扫的**，千万不要做的过于艺术，让人都意识不到这是个二维码，反而降低了扫码率，那就有点得不偿失了。

希望大家都能做出自己喜欢的炫酷二维码~

**以上，既然看到这里了，如果觉得不错，随手点个赞和“在看”吧，并给我个星标⭐，感恩。**

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言