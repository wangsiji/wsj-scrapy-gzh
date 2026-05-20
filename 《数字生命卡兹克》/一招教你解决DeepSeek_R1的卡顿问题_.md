     一招教你解决DeepSeek R1的卡顿问题。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

一招教你解决DeepSeek R1的卡顿问题。
=======================

原创 数字生命卡兹克 数字生命卡兹克 2025-02-05 09:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/BVxgmGS4BfW4oe2NaZBZBw](https://mp.weixin.qq.com/s/BVxgmGS4BfW4oe2NaZBZBw)

整个过年，DeepSeek给我用的都卡炸了。

我自己在官方app和网页里，到现在也还是10条回复有8条是“服务器blabla，请稍后重试”。

每次见到这句话，我都想脑溢血。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2IgiaYo9Mp8F7QmS6W6d0NJf6r292oXBFSibu58pOrEKDB8r5GW072p5g/640?wx_fmt=png&from=appmsg)

坦率的讲，你指望DeepSeek官方来给你提供一个非常良好的体验服务，我觉得有点不现实，人的目标是AGI，不是云服务。所以宝贵的算力资源得用在探索模型上，而不是保障几亿用户的推理需求。

再加上DeepSeek R1本身就是开源的，人人皆可部署，所以啊，官方R1很卡，那我们不如换个思路，直接用别人部署的R1的第三方服务不就行了。

反正模型都是一个模型，没差。

这里可能有人会问，为啥不在我们自己电脑上部署一个，自己用多爽。

我想说，R1的模型参数是671B，差不多需要1300个G的显存，你才能跑得动满血版的R1，这是啥概念呢，我们普通人一般的显卡在这个时代，4060这种级别的偏多，这种显卡的显存只有6G。。。

即使你上A100 80G，也要16张卡才能部署的下来。  

现在很多人所谓的本地运行R1教程，你可以理解为都是部署的7B的蒸馏版模型为主，那玩意说实话，如果跟满血R1比，用四个字评价就是：**又笨又慢。基本没法用。**

所以，用第三方服务，几乎成了最优解。

现在国内几乎所有的云都支持了DeepSeek的API调用，比如百度云、腾讯云、华为云、阿里云等等，昨天下午，火山引擎也直接宣布加入战斗。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2tdQkSdFlNqq0iaeYkPHECe20OB5s6SMPreYwfobPdw2LkPRxS7Qt9pw/640?wx_fmt=png&from=appmsg)

但是，我觉得最好用、最适合小白的，还是**硅基流动+Chatbox AI**的组合。

真的，体验无敌，还约等于不要钱。

硅基流动负责部署完DeepSeek R1然后提供一个API key，属于后端。  

Chatbox AI相当于前端的对话产品，你把硅基流动的API key输入进去，就可以对话了，而且它是目前唯一支持自定义API Key且有Mac、Win、安卓、IOS四端产品的。无敌好吧。  

真的，你需要准备的只有一部手机或者一台能跑扫雷的电脑、一个+86的手机号。就能得到一个再也不断线的**满血DeepSeek**。

话不多说，直接开始教程。

一共两大步。  

第一步，你需要搞到一个硅基流动的API key，第二步，下载Chatbox AI然后粘贴进去。完事。  

是不是很简单。

  

**一. 搞定硅基流动的API Key**

首先，注册and登陆硅基流动官网。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2iaWRrM63ZibfNmTNdP17Or3bYQbC0t90mRVd6ZWriaGhHX3N7o0XRUfkA/640?wx_fmt=png&from=appmsg)

这里注意一下，硅基流动正在搞活动，你可以直接用我的邀请链接注册，这样咱俩都可以白嫖14块钱的额度，几乎够你高频使用2周到1个月了（不是广告）：

https://cloud.siliconflow.cn/i/dcAIgVea

登陆之后，直接就进入【模型广场】了。排在第一位的模型就是R1。

但是你不用管，直接看最左边的导航栏，找到【API密钥】，点进去，再点右上角的新建API密钥。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2Q5xvgUBYGmwb7RgGhVspzwHicgWHutOLKU2ykyj3YIUNAFibyVfDSWKw/640?wx_fmt=png&from=appmsg)

密钥描述这块可以随便写，你可以建多个密钥，别忘了这个密钥是干啥的就行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2QNg2QHJ4TxOkpIBo0JhVuClia14yLMr6U20ItymXxHLIkEDt1dicvDQA/640?wx_fmt=png&from=appmsg)

新建完成之后，你就会得到一个看着是加密的API Key了，这就是你的密钥，点击密码那块就能复制。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2ztnPVch95d4OsdicwjdBKQ4YKia9muB8fBgjx23icB210BvmGdsOgDF0Q/640?wx_fmt=png&from=appmsg)

至此，你的API key就到手了，可以开始进行下一步了。

这里我也提醒一下，这个API key绝对不要给别人，绝对绝对绝对不要。要不然你会发现你账户里的钱怎么一会直接干光了。。。

  

**二. 下载Chatbox AI**

一个我自己非常喜欢、很棒的AI神器。

网址在此：https://chatboxai.app/zh#download

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2RKic4OB0ibIwTWuen1sh3rb2NiaZ4ibMFCvRrkTWHia4zte0k2ZSEBfQt9w/640?wx_fmt=png&from=appmsg)

你可以直接下载你需要的客户端，比如我自己手机和两台电脑就全装了。苹果用户直接去AppStore下载就好，其他的记得来官网下载。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2Hr51nhRknzpVmxZcyanXpNG37SvsCicNSnfpwYW5I9T1RNicsicMiahCsg/640?wx_fmt=png&from=appmsg)

这里我用mac客户端举例（手机上的都是一样的，操作没区别）。

打开以后，你就能看到一个非常熟悉的空白对话界面。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn22UZGGPqb6L4JuuqjNpFRVgXd4DzDrrqBiao1uFmKuZicMXWUDGxVIeicw/640?wx_fmt=png&from=appmsg)

不用管，直接点击左下角的设置按钮。  

在模型提供方里，找到这个SiliconFlow API，这个就是硅基流动的英文名。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2NIC926tCCxkbiaRYTiaXFNVPz4Y1HHVcmj9YQLG0UnmvgfgjgYAPOrtg/640?wx_fmt=png&from=appmsg)

在API密钥里，输入上一步咱们复制下来的API key，直接粘贴进去，粘贴完以后，下面模型下拉框就会出现一堆数据了，全部都是硅基流动部署的模型，我们直接拉到后面选DeepSeek R1模型就行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2Zabr2TaP5iajOruPA0qYl9drAmkmW0ALIEkBfDyE7CUpENtFZYKNUdA/640?wx_fmt=png&from=appmsg)

然后保存。

你没看错，这就算全部完事了。

我们就可以随便问一句来测试一下，比如：  

“用LOL祖安老哥的方式给我描述一下特朗普”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqc9icp8P55Zn3icmefFuKSn2sQC6YYrYGS4s68ibr7cAJdK0GUruY3bZHoRzNw9xsy1g7FXwAd3ge1A/640?wx_fmt=png&from=appmsg)

完美出现，而且最难能可贵的是，ChatBox AI的界面，是带有思考过程的。。。喜极而泣。

至此，你就拥有了一个你专属的DeepSeek。

妈妈再也不用担心我的DeepSeek断线了。

  

**三. 写在最后**

DeepSeek实在太火了。

火到这两天流量甚至把硅基流动都有点冲爆了，偶尔也会出现卡顿的情况。不过总体我体验下来，还是能比官网那个卡顿好接受的多。  

感谢硅基流动和华为，在春节期间不眠不休的加班加点。

未来我相信，也许还能有更多云厂商和算力租赁加入战场，让这些开源模型，跑得更稳、更快。

好啦，教程也说完了，剩下的就交给你去冲浪了。

上班的第一天。

记得用AI摸鱼哦。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言