     AI春晚OpenAI开发者大会一文汇总 - 迈向通用AGI的第一步 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI春晚OpenAI开发者大会一文汇总 - 迈向通用AGI的第一步
=================================

原创 数字生命卡兹克 数字生命卡兹克 2023-11-07 04:26 天津

> 原文地址: [https://mp.weixin.qq.com/s/M6wUYGU1yOwhFFn8M29HVQ](https://mp.weixin.qq.com/s/M6wUYGU1yOwhFFn8M29HVQ)

在2023年这个AI爆发的元年，OpenAI作为这轮AI浪潮真正的奠基者，任何动作都一定是万众瞩目的。

11月7号凌晨2点，有史以来第一次的OpenAI开发者大会，更被戏称为AI春晚，在奥特曼预告了好几个月之后，终于正式开始了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7GhdrBCFtqg5pZLIdtDm8OyiaWMYeID1CVmRLSRWC49u4pmdOHCLibfrg/640?wx_fmt=png&from=appmsg)

干货和新消息非常多，核心是GPT4-Turbo模型和Agents，我分成了三趴：  

1.  新的GPT4-Turbo模型，功能更强大、更便宜、支持token更长。
    
2.  开放更多的API，包括视觉、图像创建（DALL·E 3） 和文本转语音（TTS），新出了Assistants API，可以帮助开发者构建在自己的应用程序中构建Agent。
    
3.  ChatGPT的更新，官宣AI Tools，发布用户可自定义的GPTs。
    

  

 **ChatGPT用户数** 

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7BHHHEvpytaxChj7OASledbPvbNrJyW7ribUmOVHC6r0z7vu73wAXrQQ/640?wx_fmt=png)

先恭喜OpenAI，目前有大概200万开发者，在500强中有92%用了GPT改善工作流，周活有将近1亿用户。

  

 **GPT-4 Turbo** 

1.GPT-4 Turbo 支持 128k 的上下文窗口，大概相当于300多页的文档。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7gYQfYcnCgrc3PaTSpnBPVaMYsOUTWvhg5icLlqXz6fX7aM6DxO7Cecw/640?wx_fmt=png)

2.函数调用更强了，可以一次性调用多个函数，准确性也更高。还有新的输出json模式，在这个模式下，新的API参数response\_format使模型能够约束模型输出，以生成语法正确的 JSON 对象。还有一个新的seed参数，能使模型在大多数时间返回一致的完成来实现可重现的输出。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7ibFEOKib3fcZbmCzLXuPDzN3tVOEfEYkZvIicf1UrAS9k9KLPQ8UDzXicg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7IsOI5XI0gdJ0aHtnwMwyMKaV0tCJxqxtfFUGjyABianPJ05rXwyEaIA/640?wx_fmt=png&from=appmsg)

3.知识库更新到了2023年4月。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic78FWgkA0KDDssB9CUibLPpTa9NH2uibdcPKpIAwYBXonX4v6NjoUHdFaQ/640?wx_fmt=png)

4.GPT4开放微调，并且OpenAI还开放了一个叫做Custom models(自定义模型）的功能，让选定的公司能跟 OpenAI 合作，针对他们的特定领域训练定制 GPT-4。支持修改模型训练过程的每个步骤，并且训练好后的模型是公司专属。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7K9lBPz95EE41grlbqqZlicXg6AOT16MOorrTq3GzLBhEfNxcjibGO4rg/640?wx_fmt=png)

5.GPT4的API价格更便宜了，GPT-4 Turbo 输入代币比 GPT-4 便宜 3 倍，为 0.01 美元，输出代币便宜 2 倍，为 0.03 美元。

顺带手把GPT-3.5 Turbo也给升级了，新版本GPT-3.5 Turbo默认支持16K了，版本的的价格也给砍了。

GPT-3.5 Turbo 4K 模型输入token减少 4 倍至 0.003 美元，输出token便宜 2.7 倍，至 0.006 美元。GPT-3.5 Turbo 16K版本输入便宜 3 倍，为 0.001 美元，输出便宜 2 倍，为 0.002 美元。  

并且OpenAI承诺不会拿API过来的数据进行训练，以保护开发者，避免版权纠纷。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7iaH3POxeSBE3XXKBZfzo8hiaSfD7XYgFgu8wGF4EbNtCHTBakKAVUMJw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7Lc9UfasITU0mhOJiaGkGBSeibRrxwrqD10lLkx2h4N1oqjeDA1UMHW1A/640?wx_fmt=png)

  

 **开放API** 

1.多模态、Dalle3、TTS都开放API，后面可以接入了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7zhAa2jMHwY4fHwqXpiaEeaeyib8tn1lkv70zrwQxpTLibAibjYrWjYToRQ/640?wx_fmt=png)

2.新的Assistants API，可以帮助开发者构建在自己的应用程序中构建Agent，Assistants API 包含Code Interpreter（代码解释器）、Retrieval（知识库）、Function calling（函数调用）。

具体的API文档可以看OpenAI的官方文档：

https://platform.openai.com/docs/assistants/overview

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7q8iaSJCu7cUQvU8jKhTNZQwNL3mu4FqS3J99ZgrY0hRlXj7zNmf8CEA/640?wx_fmt=png)

价格这块，Code interpreter 单次0.003美元，Retrieval 是0.20 美元/GB/助理/天，这些在11月17号前免费，17号后开始收费。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7NA1g8INeIsOGp9VQMAqemEEicCiczEsRYcbdLiazbJSddSMKHMamO17Dw/640?wx_fmt=png)

最后演示的时候挺搞笑的，他们现场做了一个，然后给在座的所有人都发了500美元的API额度。。。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7NianZJuUibYWRFgUNEoLicmV1vuia03uIfVrAw9fcxDmSHz56zyicF8rV9Q/640?wx_fmt=png)

3.开源了Whisper v3 和 Consistency Decoder。Whisper是大名鼎鼎的语音转文字的标杆，这次开源了V3版本，马上还要开放Whisper v3的API。Consistency Decoder是Stable Diffusion VAE的替代品，该解码器改进了与 Stable Diffusion 1.0+ VAE 兼容的所有图像，在文本、面部等方面有显着改进。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7ElKOU8icvVTOvqx7SzVLa4myu7I8LQ5osVNkyCDeSmHFTicF5t8IOZgQ/640?wx_fmt=png)

  

 **ChatGPT相关** 

1.正式发布AI Tools，GPT-4用户不用再点模型的各种下拉菜单了，以后只有一个窗口，模型可以自主调用代码解释器、联网工具、Dalle3等等，走上了通用AGI的第一步。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7EuNMcEXBHDhOUoD57NfoFPMHic8RJrDAPNmrXOQEcssiczIcmmxd8qGw/640?wx_fmt=png)

2.GPTs。ChatGPT 的自定义版本，用户为他的特定任务创建定制版本的 ChatGPT ，且无需编写任何代码行。也就是说，没有任何开发经验的用户，都可以在ChatGPT创作自己的Agents应用。

跟Assistants API不同的是，Assistants API是将GPT的Agent能力集成在他自己的应用程序上，而GPTs是活在ChatGPT上。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic78FxwUKTUgibC23ygkfRkR2XdDZNBBa6n40RR5mgyHibcTAljHC8wicHEw/640?wx_fmt=png)

而且用户做完的GPTs，还可以跟朋友分享，本月晚些时候，OpenAI将推出 GPT 商店，甚至还可以根据使用你创作的 GPT 的人数来赚钱。这个影响挺深远的，这就是AI时代的真正的GPTs store。生态会真正的起来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7Ecg0KibHAyibaFB7Z1miao847Xic0iavBJ03NagMT4f37w90qBLicVcfXn4Q/640?wx_fmt=png)

这个GPTs自定义性非常强，用户可以将GPT 连接到 API 以执行任务，例如管理数据库、电子邮件、发短信等等。

这里有一个演示视频可以看一下：

 **最后** 

这张图应该能说明很多东西了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooPm74zoFAGVQsRx4pOfic7eSicV2IPaAvgibTm7FSnrBBQCp7ecrblcGFkAHymUhw9Tf5OKzlLwn4Q/640?wx_fmt=png)

OpenAI在迈向通用AGI的路上，正式开始了第一步，推出了GPTs、推出了Assistants API，还发布新版本的GPT-4 Turbo，再把价格巨幅降低。  

我一边看到的是AI行业的狂欢，这是AI春晚也好不为过。  

而另一方面，看到的是无数中小AI创业公司的消亡。

AI实在是一个巨大的杠杆。  

今晚的OpenAI仿佛在重复着《三体》中的一句话：

**“我消灭你，与你无关”**

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言