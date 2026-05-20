     5分钟教你用AI做表情迁移，让一只猫萌萌哒的唱歌。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

5分钟教你用AI做表情迁移，让一只猫萌萌哒的唱歌。
=========================

原创 数字生命卡兹克 数字生命卡兹克 2024-08-09 12:08 云南

> 原文地址: [https://mp.weixin.qq.com/s/v4vxVK0Umji\_Br9tcnADCw](https://mp.weixin.qq.com/s/v4vxVK0Umji_Br9tcnADCw)

昨天在群里看到海辛发的一个视频，直接给我萌化了。

喜欢到爆炸。  

视频是这样的。  

猫唱歌！！！而且唱起来这么可爱这么呆萌！！！

很多人在问是怎么做的，其实真的蛮简单的，毕竟是AI，AI的东西，一般就是有手就行，你懂的。

这个项目，就是WAIC期间，快手开源的那个表情迁移的玩意：  

**LivePortrait。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrnfmOkJYEgW70RPTfppxLJ3KgaQDzJ0k1WzloGHQW5ib4h7vBT87KKhB9qzSmXiaXRlrH7fHRH2RIw/640?wx_fmt=png&from=appmsg)

网址在此：https://github.com/KwaiVGI/LivePortrait?tab=readme-ov-file

跟之前的那种照片说话啥的不一样，那种是给一段音频，然后让照片根据音频动起来。阿里的EMO就是一个典型。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrnfmOkJYEgW70RPTfppxLJmXJtdGsBQica8xeib4PMbb7tpAup7h1ZOLE5bWIAnhU8oicv5kkCypM0Q/640?wx_fmt=gif&from=appmsg)

而快手的这个LivePortrait，是视频驱动照片或视频，可以直接把视频里面部的表情，一模一样毫不违和的复刻到另一段照片或视频里。

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrnfmOkJYEgW70RPTfppxLJicDwIVOia5sicEjfmicmMq5opbrzeoxm4alTkyL5svnIKkF9BKZoO1ibpOw/640?wx_fmt=gif&from=appmsg)

不仅是正面，对于一些45度角的侧脸，效果支持的也很好。  

但是如果只是这样，那其实也没有那么好玩，因为这样的效果，一个海外现在非常成熟的迁移产品Viggle也能做到。

它不仅能迁移表情，还能迁移动作。  

而LivePortrait我觉得最牛逼的就是，他们把迁移能力，泛化到动物身上了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrnfmOkJYEgW70RPTfppxLJIVaNsqMiccmUEKYdgnjKtLdbakXhLWgiaM7f2wpYuWG0HQJtmn3CokbQ/640?wx_fmt=png&from=appmsg)

不是，你就说，谁特娘的看了满屏的可爱的猫猫狗狗的，不动心啊！

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrnfmOkJYEgW70RPTfppxLJ0icwBsicxv9DXUILt3JrN0ohg5tAxa2ico3PHAk2RtEQJeEia060RJdncA/640?wx_fmt=gif&from=appmsg)

这一下，我不知道你们，反正我是心动的笑死。  

我太喜欢萌萌的宠物了。。。

而想跟海辛一样，做个让小动物挤眉弄眼唱歌的小视频，也非常的简单。  

快手这个老铁，在8月5号的时候，发了一个本地傻瓜整合包。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrnfmOkJYEgW70RPTfppxLJJpsdyRMqH7m2FggEaoLaxpomNa86z4ibGanVoibia0a7GL0d1cEZg1csg/640?wx_fmt=png&from=appmsg)

所以，你也不用用那复杂的ComfyUI或者本地部署跑了，你直接把这个整合包下载下来，本地就可以直接跑，而且巨简单。

配置要求也挺低的，8G显存就能跑。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrnfmOkJYEgW70RPTfppxLJETrnXnCvzaj0RbAC1OTnibWbXvZAiaw786m7E8qkicyghVqAuDOp6XMdw/640?wx_fmt=png&from=appmsg)

这个整合包，为了方便大家下载，我也扔到后台了，**你直接对着公众号私信"LP"，就会自动发给你了。**

是个解压包，解压出来以后，你就可以在文件夹里看到这两个文件。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrnfmOkJYEgW70RPTfppxLJHhD2v2ztoHzPup5QXDf4CYZYjapor6iahibh28flOdA7JFUwtJBRrTdg/640?wx_fmt=png&from=appmsg)

run\_windows\_human.bat是人类模式，也就是把表情迁移到人脸上用的。

run\_windows\_animal.bat是动物模式，把表情迁移到动物脸上去的。

**一定，一定，一定不要运行错了。**

比如我们要去跑上面的猫猫唱歌视频，那你一定要双击运行run\_windows\_animal.bat！！！绝对不要运行另一个。

第一次运行时间可能会久一点，等个大概一分钟，你就能看到自动打开的界面了。  

说实话，我还是喜欢GUI这种图形交互界面，因为真的很傻瓜很小白，上手即用。  

界面也很简单，左边就是传你要被迁移的图，右边上传要迁移的视频素材，左右两边最好都是传1:1的图片或视频，自己先在手机相册或者美图秀秀或者剪映里面剪裁完，这样效果最好。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryJ3eia8s81WUSA4H1pAZHRXjmrpF40vqKicAWovqgBGdupeHVBR43qMR4PtTpxPn9b2j8p0C1TwzA/640?wx_fmt=png&from=appmsg)

**这里还有个坑要注意，你上传的文件，命名一定不要是中文名，要不然会报错。**

当你传的是1:1尺寸的时候，下面这个do crop记得关掉，要不然会给你做旋转剪裁。如果你懒得裁，传的不是1:1的，那这个地方再给他勾上吧。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryJ3eia8s81WUSA4H1pAZHR1qzbN34aB8zn9P8uia9UcVMahZeOib2vPgXOCWS27w4rsNA6AU1emxPg/640?wx_fmt=png&from=appmsg)

我找了一个很可爱的猫猫来做一个演示，要让这个猫猫动起来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURryJ3eia8s81WUSA4H1pAZHRX9b03LmiaPuiaJPIBkFuq74ByklPAAbUicYura7Y2VdBovibSAq0ZzYYcA/640?wx_fmt=png&from=appmsg)

我就自己录了一段唱两只老虎的小视频。  

我唱歌天生跑调，所以大家不要嘲笑。  

点击Adnimate之后，下面的进度条就会嘟嘟嘟的开始跑了，我是4060，十几秒的视频大概跑70秒左右就可以出来，大家可以参考一下速度。  

很快，你就会得到一个可爱的小猫，唱两只老虎的视频了。

或者，如果你有孩子的话，也可以用萌宠，给他唱一首，《生日快乐》。

是不是非常简单？真的5分钟就会。

还可以去做好多好多有趣的东西。  

当然，除了萌宠之外，你也可以启动Human人类模式，去做更专业的表情控制。  

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURryJ3eia8s81WUSA4H1pAZHR2gMo6wTWWbWAV1iazTicsbAhgib4RFrBNWCuar6FaG7UvmOSGkYgheZicw/640?wx_fmt=gif&from=appmsg)

一个可以精细控制的表情和嘴型，在AI视频中，想象力有多大，能做到什么程度，想必所有的AI视频创作者，应该懂得都懂。

这就是LivePortrait。  

**来自朴实无华的快手老铁的项目，发布即开源，还在不断的迭代更新，甚至给你做整合包。**

用户体验属实是拉满，建议所有国内公司，在开源的项目上，都向快手学习，不发期货，不只开源Readme，照顾普通用户的使用体验。

LivePortrait的整合包不想去Github上下的我也放到网盘里了，即下即用，**你对着公众号后台私信"LP"就有了。**

希望也能看到大家，更多有趣的视频产出。

下一期的5分钟教程系列，大家想看到用AI来解决什么问题呢？欢迎在评论区留言，说出自己的需求，说不定下一期，就可以5分钟用AI来解决你的问题哦😉～

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言