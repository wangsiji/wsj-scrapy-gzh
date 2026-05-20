     【有手就行】5分钟教你把ChatGPT接入QQ，搭建你的专属聊天机器人 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

【有手就行】5分钟教你把ChatGPT接入QQ，搭建你的专属聊天机器人
===================================

原创 数字生命卡兹克 数字生命卡兹克 2023-05-31 23:08 天津

> 原文地址: [https://mp.weixin.qq.com/s/kKWPw6HO-YEncoP0niP6GQ](https://mp.weixin.qq.com/s/kKWPw6HO-YEncoP0niP6GQ)

最近OpenAI对魔法封的严重，而且ChatGPT用起来最近挺慢，没事还卡一卡，麻烦。

所以为了自己的顺畅体验，干脆直接把ChatGPT接进QQ里面去了。  

用起来就轻松加愉快，私聊群聊都行~  

大概就是这种效果：  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMexhgVdsRBt35qPrHAbP7ib1zHug2B2DuIzcoUua55kaCrwpeP959OlOQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMe4ZyxcWIuuarpK0aNSoIz57sfl2Q0MMoNib7SOZwIZEJYsOtQTsy9nYg/640?wx_fmt=png)

**接下来，就教大家徒手接一个，真的，有手就行，5分钟解决战斗。**

我使用的项目是ChatGPT for Bot，Github源址在此：

https://github.com/lss233/chatgpt-mirai-qq-bot

你需要准备的东西：  

1.  魔法（这个不解释了）  
    
2.  1个QQ号（别作死用自己的大号）
    
3.  OpenAI的API key
    
      
    

OK，我们正式开始。  

首先，你需要先下载这个项目的一个整合包。毕竟没程序跑个屁哈哈~

**我也给大家准备好了，关注并私信我Q，就直接自动回复你下载链接了。**  

下载完解压到本地，我就直接解压到D盘的新建文件夹里了。可以看到包里有这么些东西。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMeycKsQewSCHiba4pfyfTu9FLkiauujwescFMVIDL0zm2HKHGXyicYxZ7bQ/640?wx_fmt=png)

我么直接双击运行初始化~

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMeHPIytJXokqCQMnD6AGUicntqibiblVoYq3sjniaCnIBpncaQXqjVUUdV0w/640?wx_fmt=png)

敲一下回车，就会让你输入你想配置的机器人的QQ号了，**再强调一下，别用自己的大号，虽然封号概率很低，但是万一封了就得不偿失了~**  

输入完QQ号后，再敲一下回车，就会开始跑脚本，嘟嘟嘟的几秒十几秒就完事了，此时会自动给你弹出一个长这样的文本文件。这就是我们需要修改一下的配置文件，也是最麻烦的一步，后面就一马平川了~  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMeC38XrY802KyveQLEoe8HIrYLlwWJPW1ZcJ5qtIn8xumOlPwfIxcoyQ/640?wx_fmt=png)

因为这次只接ChatGPT，所以模版我已经写好了。大家把我的代码复制进去，然后把我标注的地方给改成自己的就行~

_\# 这里是 ChatGPT for QQ 的所有配置文件_

_\# 请注意：以 "#" 开头的文本均为注释_

_\# 不会被程序读取_

_\# 如果你想要使用某个设置，请确保前面没有 "#" 号_

  

_########################_

_\# 配置文件编写教程：_

_\# https://chatgpt-qq.lss233.com/_

_########################_

  

_\[onebot\]_

_qq=请填写机器人的 QQ 号_

_manager\_qq = 请修改为机器人管理员的QQ号_

  

_\# ==== OpenAI 部分开始_

_\[openai\]_

_\# OpenAI 相关设置_

_\# 自定义 OpenAI 的 API 接口基础地址_

_api\_endpoint = "https://chatgpt-proxy.lss233.com/v1/"_

  

_\# 以下是 GPT3(.5) 和 GPT4 的模型参数_

_\# 在使用 API 调用时有效_

  

_\[openai.gpt3\_params\]_

_temperature = 1.0_

_max\_tokens = 4000_

_top\_p = 1.0_

_presence\_penalty = 0.5_

_frequency\_penalty = 0.5_

_min\_tokens = 1000_

_\[\[openai.accounts\]\]_

_\# 你的 API key，可以在这里看：https://platform.openai.com/account/api-keys_

_api\_key="sk-xxxxx"_

_\# 如果你在国内，需要配置代理（端口写成自己的）_

_proxy="http://127.0.0.1:7890"_

_#支持的变量：{session\_id} - 此对话对应的上下文 ID，若产生在好友中，则为好友 QQ 号，若产生在群聊中，则为群号_

_title\_pattern="qq-{session\_id}"_

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMedwWhVkXWdt18zcn2BQq7mklbwGLh8pLNzl3E1WgB3YNp6N4Crf0ZsQ/640?wx_fmt=png)

这几个地方需要更改。QQ就不说了。

OpenAI的API Key如果忘了的话，去这个网址：

https://platform.openai.com/account/api-keys

登录后，新建一个Key，以前的key你也没法复制，就新建一个存下来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMenTuZNcPzT3JfCoIJUKsLGzOrEVTYcwiadAMjAb2QCvaTjDuHps8LJGw/640?wx_fmt=png)

而端口那块，打开你的魔法，我的这个7890就是，每个人的可能都不一样，默认的一般就是7890。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMelWlLCzKyzwcB64jQhQVIOK32nCI1tibJdUgvyiatr3UvQ8zX0YydwUnQ/640?wx_fmt=png)

**全部设置好以后，我们把配置文件和刚才的窗口都关了。最难的一步完事了！**

我们找到根目录中的启动ChatGPT。双击运行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMe0vyCGrg0lHM7icniaWgk4EcPoyMLBewbfk9zad6x8NI0ewBIRibmXPYAA/640?wx_fmt=png)

看到这些消息后，说明ChatGPT启动成功。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMeZzKVu9fkM8WmUosHcGf808nsxNArwqA5fqnY8twfFJlgSibmSEicyxSA/640?wx_fmt=png)

这个窗口千万别关。我们回到文件夹里，再找到启动go-cqhttp，双击运行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMeJBjHfsFc13ia7rbfpibPOU1n6FzcmjhLrD94NibopL7lFm2ibc3bVAZBCA/640?wx_fmt=png)

弹出一个窗口，等个几秒以后，就会出现一个巨大的二维码，此时，打开你的手机QQ，登上你的小号，直接扫码登录。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMe2NbRvAItFp5AL72sT2mEEicbwiconSmbDEd9jlbZOwO15h29sqcotU2w/640?wx_fmt=png)

**提示登录的是手表QQ，没毛病，因为用的就是手表QQ的协议，**直接手机确认登录。看到这些提示后，就说明登录成功，

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMeKZbyJlbkk3T6y20yG8PZrVzzR4DoCWk7bY7TGOeIIh41J5tbdQHs0A/640?wx_fmt=png)

所有程序全部完成。QQ接入ChatGPT成功，我们去对话一下试试~

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURq2XT5PWodd3hR2MiaxicFvMeoj5K6ibhLRTCDqmsLXev7TgzuoAlcMPE4qNN0XHgibDsGNRPGNvUnWTg/640?wx_fmt=png)

一切都没毛病，愉快的玩耍起来吧~

**关注并私信我Q，就直接自动回复你整合包啦。**

**另，明天儿童节啦，祝大家六一快乐~**

以上，创作不易，有用的话请点个在看并给我设个星标⭐，感恩。

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言