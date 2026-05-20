     让ChatGPT根据你自己的数据库作答 - 新瓶装旧酒 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

让ChatGPT根据你自己的数据库作答 - 新瓶装旧酒
===========================

原创 数字生命卡兹克 数字生命卡兹克 2023-04-19 00:23 天津

> 原文地址: [https://mp.weixin.qq.com/s/75DoaM-6PaVoIB2M0oUO9Q](https://mp.weixin.qq.com/s/75DoaM-6PaVoIB2M0oUO9Q)

ChatGPT越来越广为人知之后，有越来越多人将他用在实际场景中。

但是ChatGPT也不是神，4096Token也如同梦魇般旋绕在头顶。

越来越多的问题暴露了出来：  

**比如，发现这玩意没有最新数据，问一些最新的数据毫无意义。**

**比如，一篇超长的PDF文档根本灌不进去。**

诸如此类。  

今天，想写一篇浅显的文章，跟大家聊聊OpenAI开放的能力，也是你们所见到的ChatPDF、ChatDOC、所谓Chrome联网插件等工具的原理。让大家人人都能将自己的数据灌给ChatGPT，让他根据你的数据来做答。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwANPBM0K4XtbxZ0QGpC3n6Ft7kNtrjUsmC0rcYRVBicLjjFNR9KdxiaIqw/640?wx_fmt=png)

**首先，非常推荐想研究的人去读一遍OpenAI的官方文档，里面很多东西其实已经写的非常非常傻瓜简单了，而且并不难。**  

在关于如何将自己的数据灌给GPT上，OpenAI官方提供了两种可以直接调用他们接口的做法：

**Fine-tuning（微调）和Embeddings（嵌入）**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwAaQRGHeDiaAVQzsK5yQLqqzWdDrC3AH37CoUia1DPMmCW6IMUSj83dmvQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwAZhLNo5g09HY7bDGM0Plg2BxJoUY4FXW6EwHGPHibJqky0XfiaqSQkP4w/640?wx_fmt=png)

两者的优劣简单概括如下：

**Fine-tuning（微调）只能基于GPT3的分类模型去训练，比如davinci、ada等等，是预训练模型，一次训练终身受益，适合很久知识都不变且数据集较小的情况。**

**Embeddings（嵌入）无需训练模型，是将自己的预设Pormpt+数据+问题打包，当作一整段话发送给GPT。让GPT根据这个预设的Prompt和灌给的数据再加问题做回答。适合数据量超大且实时更新的一些数据。**

在我实际使用中，嵌入方法可能更适合大多数场景一些。ChatPDF和所谓的那个假实时联网的插件也都是这种方式。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwAsztZjHjf21WA31SNBHtZWToO0GkOyauHnNFia0c8jxDKbOVW6g2bLxw/640?wx_fmt=png)

以下，我来举个小栗子：  

我现在有10000只基金的所有的最新的涨跌数据，在一个excel里，我想让ChatGPT在回答这10000只基金的相关问题时，使用我excel的数据来回答，别用他那老掉牙的21年的数据。  

这是我的需求，当然正常做法可能是去数据库里面扒数据，当然原理跟从excel里取数没什么本质区别。

现在，我想问“诺安成长这只基金怎么样？”

首先，先使用jieba分词，把这句话给拆了，变成“诺安成长”“这”“只”“基金”“怎么样”“？”  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwA8kcL4vNOSlcQ1cTG3ia9hQ4LhxoedNpnqvTUYz6XF3CFSPr03OhtJBw/640?wx_fmt=png)

然后拿这些分词出来的字段去跟搜索我们的分词表。然后发现跟分词表匹配上了，就去我们的excel里搜“诺安成长”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwAraqamnn57RTXibknD45ua20abiaBaGicg32vUaAVQevv4K3BuZqVGkpyg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwAicXIajke92iaZACSRYIMTnhgPOrYPVLAfPHWZ0OaicIMRnhv4DXKpuzUw/640?wx_fmt=png)

搜到了诺安成长这个基金之后，把整行数据提取出来，加上我们的prompt和这行数据和“诺安成长这只基金怎么样？”这个问题，一起送给GPT。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwA6HDTD6BMibadgnupyRtNQtrAoWM49CZDsNefuTajLRNS0dbO3kRiaPsw/640?wx_fmt=png)

这样，GPT就会根据我们这么长的一大段，用自然语义重新组装，给我们回答。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwA4Xn9ibsicHuhX88tVwX8XF37kZ2OWoaE8qMVMKRWzNxicQJicCHsOwnrQw/640?wx_fmt=png)

**其实，懂一点技术的就能明白，为了解决token的问题，在外面包了一层搜索，先搜索，再嵌入。**

现在很多的长文本的处理方式，也是如此。

比如我们常用的ChatDOC。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwAqVC5vDic3lMYOJm6YvKrqwEEdibCQJpjoNdbcuiatzMSk8bS5cfw5VuFA/640?wx_fmt=png)

**先做了一层语义搜索，然后用嵌入的方式去总结并做答。**  

而所谓的WebChatGPT，可访问互联网的ChatGPT。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwABwVI05BhAONEBlxordzO8rYodmDicibh6A35aFtfBgpcNY7RSawjvibFg/640?wx_fmt=png)

也是将网页里的HTML文字内容给扒下来，当作数据嵌入，让ChatGPT根据这扒下来的数据回答。实现假联网。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwAMtImib8xRRVMCTcgapFIuV3GrHQt3ibxrvqVTh8oIiaz4bKzXvGNnAn1w/640?wx_fmt=png)

说了这么多，相信大家对如何使用自己的数据库有一定的了解了，一篇文章，肯定不可能手把手教大家会，抛砖引玉，可以自己再去研究一下。知道该如何让ChatGPT根据自己的数据作答。

最后，因为4096token的限制，长文本处理一直是一个非常头疼的问题。  

嵌入，能解决部分问题。

**而长时记忆区，矢量数据库，我觉得才是解决的唯一真谛。**

**这也是OpenAI推荐的方式，更是大火的AutoGPT真正驱动核心。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrriaq3L0Fa2VhLaWVetJSwAynAawbicZBC5lvVFum5YjnbLQfWZ5IfB2Rfea8SntibY4bHNIiaicIhicmg/640?wx_fmt=png)

同时，也是我现在无法理解和触及的领域。

呵，记忆，真的是人类生命长河中，最深奥的殿堂。  

以上。  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言