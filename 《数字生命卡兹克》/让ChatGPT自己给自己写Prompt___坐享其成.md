     让ChatGPT自己给自己写Prompt - 坐享其成 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

让ChatGPT自己给自己写Prompt - 坐享其成
===========================

原创 数字生命卡兹克 数字生命卡兹克 2023-04-07 20:37 天津

> 原文地址: [https://mp.weixin.qq.com/s/X74zTQ2JnrSHqC3hDVkcPA](https://mp.weixin.qq.com/s/X74zTQ2JnrSHqC3hDVkcPA)

最近跟很多人交流Prompt。  

无论是我之前整理的Prompt大全：[我花了100个小时，整理并撰写了一份ChatGPT的超实用prompt大全...](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647658055&idx=1&sn=2dbf70e48f901b70571488cde509984d&chksm=f007d210c7705b06d1bdf78ae05667b96152c2ed5d9d9f6ab1010aa52139f74d06bf9e3d8361&scene=21#wechat_redirect)，还是刚写的CRISPE的Prompt框架：[如何写出优雅的prompt？- 通用的万能框架](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647658135&idx=1&sn=0c150d312dbfad69928bab63d9317d6e&chksm=f007d2c0c7705bd678a7cf5e8644cac62a6d108b216ab3220d8f66194432784be0c99280a561&scene=21#wechat_redirect)

都解决不了一个问题是：

**我只知道一个大的方向，可是我并没有细节的想法。所以我没有办法去实际落地。**

无论是Prompt大全还是CRISPE框架，都建立在你已经知道你想要什么的基础上。比如你明确的知道你有一篇文章，要把它转成小红书风格；你明确的知道你需要让ChatGPT一定要从哪些角度回答等等。

但是，并不是所有人所有事都是这样的。

例如今天刚有一个朋友问我说，我想写一个宣传片的视频脚本，有没有可以直接用的Prompt。

当时我走在街上，想了好一会，最后只能无奈的回答到，我并不了解你的具体业务诉求，也不了解宣传片这种形式，我也不知道怎么去写这种Prompt模板，抱歉。

**可是在我的认知中，现在大家所认知的Prompt只是一种中间态，是人与机器之间沟通的语言，仅此而已。一定有一种方法，让写Prompt不这么困难，让所有人都能愉快的写出实用、自定义性强、可落地的Prompt。**

ChatGPT可以根据一句话生成Midjourney的提示词。如果让ChatGPT自己写给自己的Prompt呢？

于是我去了OpenAI在Discord上的Prompt军火库里面找。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURokYcH3Y1ZhvDSXXKCvDrwAxiaTcOiaA4MtkXAMEhLhoOAAsRBeIZEkHAibuBgdunyKic1uTlq39fdIog/640?wx_fmt=png)

找啊找啊找啊找。  

终于找到一个有趣的玩意。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURokYcH3Y1ZhvDSXXKCvDrwApbSnTbbtIB4X07qyOCptoqOCmWaAVy3Zb5zPVldYyFygj5QMCwPUJQ/640?wx_fmt=png)

**Prompt Creator，提示创建者。由@gods\_software创建的通用性的模板。**

**作用就是你输入你的需求，然后通过“ChatGPT提问-你回答”的方式，把需求具体化和个性化，从而一步一步创建一个专业的、需求明确的prompt。**

话不多说，直接开始举例子。

现在，我们需要写一个某手机的宣传片视频的脚本。直接先把Prompt Creator复制到ChatGPT里。让后简单的说一句我的要求：“想让ChatGPT帮我写一个手机的宣传视频脚本”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURokYcH3Y1ZhvDSXXKCvDrwA82gdibicp2YxmhlchXeemjT2w0sBWJ2hsibSia2A6F2dHTzqvicibFbpTIyg/640?wx_fmt=png)  

我其实并不知道要写一个手机的宣传片视频，我要从哪些方面去写，ChatGPT根据我的描述，直接给我生成了一个Prompt：

你正在为一款全新的手机制作宣传视频，希望ChatGPT能够为你提供一个完美的脚本。请使用你的想象力，为这款手机设计一个引人入胜的视频。脚本需要突出这款手机的特点、功能和优势，同时能够吸引受众的眼球并激发购买欲望。

讲道理，这个Prompt其实已经很棒了，但是对于细节，还是不够。ChatGPT提出了三个问题，以帮助我们丰富这个Prompt。我们回答它。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURokYcH3Y1ZhvDSXXKCvDrwAiaeOjdqtf8aDXqyKhBGKiaibCLZQMrstRUkMoYEVpzsequkOKxVGTMRMQ/640?wx_fmt=png)

ChatGPT根据我们的回答，帮我们生成了一个改进的新的Prompt。接着ChatGPT又继续提出了3个全新的问题，风格是什么？是否要强调特定功能？是否要突出？我们继续回答。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURokYcH3Y1ZhvDSXXKCvDrwAjUZM8LWwlClK2KuibqliayE5wLQt1ycmsBzvFA5fMCh9Z0AYGNZ1Gjibg/640?wx_fmt=png)

又生成了改进的Prompt，已经基本完美符合CRISPE框架了。同样的，生成了3个新的问题，是我之前完全完全没有考虑到的，**实际应用中，你可以一直回答，一直改进，甚至可以来回10轮以上，直到你生成极其详细极其严谨可落地的Prompt。**

因为文章篇幅原因，我们就在这里直接选择结束，拿现在仅仅对话两轮的Prompt新起一个窗口，去试试效果。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURokYcH3Y1ZhvDSXXKCvDrwAkts9Yy6cXEP7wHEYXMfBiaLezcsMibB3dubEg2eTZ7DPDwUMRIM7tOIw/640?wx_fmt=png)

带有分镜，所有的场景全部考虑到，还有故事性。配上文案，已经是妥妥的完全可用的状态了。

**要注意：这仅仅只是对话了两轮，且我仅生成了1次的效果。**

**真正应用中，你们对话10轮，感受一下Prompt Creator的威力吧。**  

Prompt很长，我直接放在了之前的Prompr大全文档里，后台回复“P”直接获取，第一条就是。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURokYcH3Y1ZhvDSXXKCvDrwAoib4E2HcTebO8wLcAyicBBzZJAkId3B6v0YMzedow6668bpIgmft7S9A/640?wx_fmt=png)

**愿人人都能享受AI的魅力。  
**

**愿人人都能成为那完美的人。**

以上，创作不易，有用的话请帮忙点个关注和在看，感恩。

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言