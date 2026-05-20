     ChatGPT新功能Code Interpreter评测 - 何以为神 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

ChatGPT新功能Code Interpreter评测 - 何以为神
===================================

原创 数字生命卡兹克 数字生命卡兹克 2023-07-09 18:20 天津

> 原文地址: [https://mp.weixin.qq.com/s/zjAtzmb9fb5n21HKFfw0JA](https://mp.weixin.qq.com/s/zjAtzmb9fb5n21HKFfw0JA)

前几天，OpenAI直接甩出来一个王炸，Code Interpreter面向所有的ChatGPT Plus会员开放。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuxPvVv2RIJbUuQ4bIIvlauALVpASaE2pYgle3eMHqXubNZQRvV6spfQ/640?wx_fmt=png)

当时我在上海参加WAIC，这两天只能断断续续的使用，但是使用过程中，心里的激动一浪高过一浪。

今天回到天津，终于有空坐在电脑面前，好好码码字，聊聊Code Interpreter。

Code Interpreter如果仅仅理解成代码解释器我觉得不太恰当，他更像是一个目前只能使用Python的AutoGPT，这是OpenAI在自主代理方面的全新的尝试。

**我觉得它也可以对标另一个电影中的人工智能助手。**

**它的名字叫做，贾维斯。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuaiaEALpErvCdRJgFEPjKqWmrxXDShH82fdTcOyNI562fHylVVUElc2g/640?wx_fmt=jpeg)

我列出了6个这两天我自己使用的一些案例，用这6个案例，直观的告诉你他能做什么。以及未来它的上限有多恐怖。  

当然，第一件事，你得先把这个功能打开。  

只要你是ChatGPT Plus会员，点击左下角头像，进入设置页，找到Beta Features，把里面的Code Interpreter打开就行了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuJpQtibrvbFGmviaTe8WjECewmAWC9opwcm4icoXdKCmKfVR6UXM3doPjg/640?wx_fmt=png)

以下是我的6个案例：

**1.数据分析**

数据分析未来可能要被永久的改变了。

人人都能做数据分析，不是说说而已。扔给他一个原始Excel，然后你就可以根据你的业务需求随便分析。

比如我想看看每当我发文章，当天有多少用户看到我的文章会分享，你让我自己处理，还是挺麻烦的，现在，1分钟完事。直接得出我的结果，0.1，即平均来说，每阅读100人，有大约10人会进行分享。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuNbr7fallhxANvPxOYNFZdtIBbMmcrqJicMZqXibCvA416WQmgZJnq4gA/640?wx_fmt=png)

**数据分析，从来没有如此的方便快捷！！！这特么是真正的生产力！！！**

**2.生成可视化图表**

Code Interpreter可以生成任何类型的可视化图表。

以前生成可视化图表费死了劲，特别是一些复杂的，比如热力图、散点图，还得自己拿Python画，现在直接一键生成，还是用我上文的Excel的例子，我想看我阅读次数的折线图，以及渠道分布。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsu8CQRUuObceyIMVwGUfDbnvOe8tgeruZ0nRIgGQTyl4f210eJXzn0icw/640?wx_fmt=png)

虽然翻车了，因为中文并没有显示出来，但是我反而觉得更特么的牛逼了。**因为他会自己找出错误，当他发现自己解决不了这个问题时，会给你另一种解决方案，来确保你完成任务！**  

**这特么的才是真正的人工智能！**

**3.从图片中提取文字（OCR）**

我有很多论文PDF，全都是英文扫描件，导致我阅读起来极其不方便。

毕竟，我的英语真的很差。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuAwGkEuGrD3EWx3AsIADuUa1ZaXA6ATSicGSguP41EpHdjZvImshib35Q/640?wx_fmt=png)

但是现在，我直接可以让Code Interpreter给我提取出来，虽然我还想让他自己翻译，但是他自己去调用翻译API，然后发现自己没法联网调不了...

**4.处理图片**

对非设计人员来说，用Code Interpreter处理图片简直好用到爆炸，你再也不用去下载恶心的PS，或者用那些蹩脚的设计工具了。比如我的这张图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuyqkq4NoSOVIfUicVr4pM1C5cjk1VQcNnmsuzwsTwtesySDjYRkxww2g/640?wx_fmt=png)

一句话，直接让Code Interpreter处理成灰度图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuxicvFvD4ia4bOQRaZXPyhyRmraa8wOgth1H0CibpsP0FDBuyraibnuojpA/640?wx_fmt=png)

再让他处理成像素风格的图。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsu3iarrudYllhZ0ibibbqGtpL6dc3Lhib2SszborK34PDL8nmdZ1dav3Lqew/640?wx_fmt=png)

至于什么修改图片大小，修改分辨率，压缩等等，那更是手到擒来！

**5**.转换格式****

以前，改文件格式是我非常痛苦的一件事，比如MP4转GIF，比如MP3转WAV，比如PNG转ICON等等等等。  

有了Code Interpreter，那些智障的工具和网站我再也不会用了。

比如这个MP4转GIF。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuEcqEWADvV1ksibA5fa4TcunnHWb5ELSZ2iauhd1nic5qoibhicibBTwyYc0g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuiaiadWicm60nG8jxx9uGPKf8ia7r1TgbJ5Jd3ktibrvb2rThpYvpN4michmA/640?wx_fmt=gif)  

比如这个WAV转24000采样率的MP3。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsukGmJanR6bIXG5U6hjlXlA9595m1eSsw7GrLVhlfFmLMYPh5PlazNPg/640?wx_fmt=png)

真的，喜极而泣。

****6.生成二维码****

生成QR二维码就是OpenAI官推的一个案例。

比如，我要把一句话变成二维码。

直接发过去就完事。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrUDQoQWSQe39K8bBIstMsuUK8E6XmFFIicXEpunc4rGNwofe8CO47hUYcgDYrOAAjLm3u11je6u3Q/640?wx_fmt=png)

**写在****最后。**  

好多个月没有这种感觉了，那种因为新东西，而兴奋的睡不着觉的感觉。

就像那些科幻电影中的情节，我们终于拥有了一个可以理解人类语言，还能按照我们的命令完成任务的智能助手。

终于，拥有了自己的贾维斯。  

想无穷无尽的去发挥自己的想象，去探索自己做为人类的边界。

我的这几个案例，仅仅只是入门级别的冰山一角，但是希望能为大家抛砖引玉。

Code Interpreter。

是能够与ChatGPT并驾齐驱的产品。

是人工智能史上新写下的一串名字。  

是从OpenAI手上，诞生出的又一个。

大师之作。  

****以上，既然看到这里了，如果觉得不错，随手点个赞和“在看”吧，并给我个星标⭐吧，感恩。****

  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言