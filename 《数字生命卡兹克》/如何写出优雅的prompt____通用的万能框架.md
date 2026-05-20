     如何写出优雅的prompt？ - 通用的万能框架 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

如何写出优雅的prompt？ - 通用的万能框架
========================

原创 数字生命卡兹克 数字生命卡兹克 2023-04-05 12:00 天津

> 原文地址: [https://mp.weixin.qq.com/s/o-Q86JT6ksPUxzq08SK02Q](https://mp.weixin.qq.com/s/o-Q86JT6ksPUxzq08SK02Q)

Prompt，绝对是现在最炙手可热的名词。

无论是ChatGPT，还是Midjourney，好像什么地方都绕不开这个词。

作为一个伪安利作者，在翻阅了大量资料以后，也想用最通俗易懂的话语让大家明白啥是prompt，以及到底应该如何写出好的prompt。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURqmtfTPicEUg5iarQApL6oz5LNDdwpay9n7chd1hqibQHDNbIcibFuhLRYJFfzz6AKC9RyArebFgwKR9A/640?wx_fmt=jpeg)

prompt翻译成中文，就是“提示”。但是在NLP领域里，prompt好像并没有特别权威的官方定义，可以理解为提示，也可以是线索、指令。  

**就是给预训练好的大语言模型一个提示，以帮助模型更好的理解人类的问题。**

可能还是有点难以理解，这里我用一个例子给大家解释：

你叫小帅，是一个卑微打工人。有一天，老板突然给你喊过去：  
  
“小帅啊，公司要新搞一个项目，要卖椰子鸡，你给我写个方案吧”  
  
你直接就懵逼了：“卧槽，老板，啥情况，我这啥也不知道啊。椰子鸡是啥？为啥突然要卖椰子鸡啊？我这方案咋做啊？”  
  
这时候老板告诉你：**“你个废物，啥都不知道，你好歹是一个策划专家。我们之所以要卖椰子鸡，是因为公司要进军餐饮行业，咱们以前是做椰子的，这正好契合。方案嘛，你就用公司背景、目标人群、地段租金、成本等等方面分析去写，最少2000字啊”**

如果老板不跟你说这些话，你能明白项目背景吗？你能知道要从哪些角度去写方案吗？那这方案能写得好吗？

我们把身份互换一下，小帅就是ChatGPT，你就是老板。你不说这些，十个ChatGPT都得懵逼。

“你好歹是一个策划...等方面分析去写，最少2000字啊”这一段，就是标准的prompt。

**prompt的作用不言而喻：提供给模型输入文本，指导模型生成合适的回答。**

在聊天交互中，用户可以提供一个问题或主题作为prompt，让ChatGPT生成相应的回答。而在文本生成任务中，prompt则可以指定一段前置文本，让模型在此基础上生成一段连贯的文本等等。

prompt如此重要，我们应该怎么去写一个好的prompt呢？  

这时候我们就需要请出github上的大佬，@Matt Nigh。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqmtfTPicEUg5iarQApL6oz5LXaKhgLSnfvNpCzO0hYTp7bpTsXCgE8sGFGEJ6fw7sSs6NuickcgicZPA/640?wx_fmt=png)

在ChatGPT3-Free-Prompt-List的项目上，他总结了一套prompt的方法论框架。这个框架的完备性非常高，直接套用就行，傻瓜又无脑。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqmtfTPicEUg5iarQApL6oz5L5KAuyCFcL9dIWEtbSjzKcdqkUo1qghFVvGR4ZEUAibmiauLibReVFmOnQ/640?wx_fmt=png)

CRISPE Prompt Framework，CRISPE是首字母的缩写，分别代表以下含义：

**CR：Capacity and Role（能力与角色）。你希望 ChatGPT 扮演怎样的角色。**

**I：Insight（洞察），背景信息和上下文。**

**S：Statement（陈述），你希望 ChatGPT 做什么。**

**P：Personality（个性），你希望 ChatGPT 以什么风格或方式回答你。**

**E：Experiment（实验），要求 ChatGPT 为你提供多个答案。**

这里用大佬的prompt举个例子（这里是为了大家看的懂翻译了一下，建议还是用英文做prompt）：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqmtfTPicEUg5iarQApL6oz5LW4WtialqJS1KbmTr2yGjroyayiam8ibpeAlDYXm0lLTxTwjicaqjftKYcA/640?wx_fmt=png)

组合起来就是：  

作为机器学习框架主题的软件开发专家和专业博客作者，本博客的受众是对最新的机器学习进展感兴趣的技术专业人员。提供最受欢迎的机器学习框架的全面概述，包括其优缺点。通过真实的案例和案例研究，说明这些框架在各行各业中的成功应用。在回答问题时，请结合Andrej Karpathy、Francois Chollet、Jeremy Howard和Yann LeCun的写作风格。请给我多个不同的例子

这样的例子其实有很多，github上的那prompt角色大全基本都是CRISPE框架。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqmtfTPicEUg5iarQApL6oz5Lh8dw5YGNSrMkia1aEK93TgcP3Jr0ETtrp4XeXia4k8gTgyZxTB4FHyUQ/640?wx_fmt=png)

**先定角色，后说背景，再提要求，最后定风格。一套齐活，是否生成多个例子可以看自己喜好。**

除了CRISPE框架外，在OpenAI的官方文档中：Best practices for prompt engineering with OpenAI API，也介绍了很多如何写好的prompt的小技巧和规范。  

包括“Instead of just saying what not to do, say what to do instead”、“Reduce “fluffy” and imprecise descriptions”等等，个人认为影响不大，感兴趣的可以去OpenAI官网看看，在此文章中就不做过多赘述了。

最后。  

prompt的真正故事和其底层专业性，在我以上的表述中，仅仅只是门外的惊鸿一瞥。“思维链”“ICL”等等，才是沉在水下的冰山，也是我这个门外汉，想去努力触碰的方向。

怎么说呢，在这个新时代，终身学习必然是未来永久性的思维。

**风雨同舟，愿与诸君共勉。**  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言