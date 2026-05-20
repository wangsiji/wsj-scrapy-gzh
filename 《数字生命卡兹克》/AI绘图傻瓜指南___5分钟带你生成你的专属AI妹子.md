     AI绘图傻瓜指南 - 5分钟带你生成你的专属AI妹子 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI绘图傻瓜指南 - 5分钟带你生成你的专属AI妹子
==========================

原创 卡兹克 数字生命卡兹克 2023-02-28 20:08 天津

> 原文地址: [https://mp.weixin.qq.com/s/GLJSeOJu\_pR5YjmqvMlFbA](https://mp.weixin.qq.com/s/GLJSeOJu_pR5YjmqvMlFbA)

AI绘图现在已经是非常成熟的方式了，很多大厂也引入了AI绘图的流程，也激发了很多人的创意（比如生成很多符合自己审美的妹子![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)）。  

想了解AI绘图的思考可以去看看我之前的文章：[关于ChatGPT的兄弟 - AI绘图的小思考](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647657627&idx=1&sn=e17677d7db3bf4c823aef0df3966dcfa&chksm=f007d0ccc77059da74ee75ce2cb63a954adc587a9922290eb74da170be7c6a82a0706ba62925&scene=21#wechat_redirect)

今天开始手把手教大家如何使用AI绘图生成自己的真人妹子，大概就是下图这样的（当然你可以随便自定义![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)）

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8poXYFPxFG7NCh5ibPpbopwuw0QEphia6PXBxTmQMxz8DDDPkfRhNwibwA/640?wx_fmt=png)

我们使用的东西叫做stable-diffusion，一个开源的很牛逼的AI绘图模型。现在市面上主流的有两种，stable-diffusion和Midjourney，stable-diffusion的优势是免费、开源、自定义强，但是需要设置一下；Midjourney的优势是简单快捷，生成效果棒，但是需要付费，同时又局限性。

废话不多说，直接开始。  

首先你一定要注意你是是**window电脑，显卡是NVIDIA的，并且显存6G以上。（此处不懂的去百度一下，不是重点）**

  

**一. 安装stable-diffusion**  

私信我，回复SD，拿到傻瓜式整合包。

（此处向整合包的原作者B站赛博菩萨@秋葉aaaki致以我最崇高的敬意）

下载好先把【SD-webui-aki-v3】这个压缩包解压到本地（文件包比较大，倒杯水![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_58@2x.png)抽根烟![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_96@2x.png)，咱别急）。解压完成以后，你就能在解压好的文件夹里看到这两个东西，A启动器和A用户协议。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk18uYOJ9zCzvgNjusPlsHABmOgWgSH76gfRZpMKQ3iaREbe1iamPtKiaibtQ/640?wx_fmt=png)

我们打开A用户协议，把【我已阅读并同意用户协议】复制到下面的位置

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk16YTm0Z52klFTLZRq6ootC5pHHyKg1z5n7cLXmfBBcCD8YvA4bE8Libw/640?wx_fmt=png)

复制过去以后，Ctrl+S保存，不放心可以多按几下，然后关闭记事本。打开A启动器。第一次启动得等一会。于是我们就看到了这个页面。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1DUJNs70ozFibdvPpQO35yh6O4QHhQkUok8mVx1YL294Rh6pezu9Gf7w/640?wx_fmt=png)

先升级一下，点击版本管理，一键升级，把咱们的stable-diffusion更新到最新版本。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1Z7uce7IZfUv66UQL2a9ketFNic61EngiaFyCF0icjAwQP8zlDZicLFuuFw/640?wx_fmt=png)

再点扩展管理，一键升级内置插件。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1iaFWHXZYWVLWvw7W77NReEic7D0zC5qGuYljOaZ976Ch9WFMZMAT4UZA/640?wx_fmt=png)

马上就好了，咱们再来安装两个模型，因为咱们需要生成特定的真人妹子嘛，所以咱们需要特殊的渲染模型才可以，如果用stable-diffusion原本自己的，那就完全出不来感觉了。点击模型管理，添加模型。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1eMlTs9BEFAGJQ7SKSUyicrywLhVvYA2n9yI1P4nuGOjwm73LgzEJNJA/640?wx_fmt=png)

还记得咱们还下了一个模型包文件不，再弹出的窗口中，找到下载的模型包，把里面的那两个文件点击打开添加进去，要一个一个添加，不支持批量。如果出现弹窗不用管内容，直接点击“是”

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1u0TAuCuib2icibAQmeiaSDndvlaHpO4Gj4EdEJUwfhKOibBwlyFXGa8eFpw/640?wx_fmt=png)

然后回到一键启动，点击右下角的一键启动，大功告成！你的本地化部署就完事了，是不是很简单！  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk12gJ98W59cGibtqhjDOS54Bg6hMM254SBZpib5UfFNIHP6IIz10LXKnUw/640?wx_fmt=png)

然后会出现一个代码窗口，不要慌不要怕，跑程序呢，等等，第一次运行时间也是有点长，需要个几分钟，去倒杯水抽根烟尿泡尿。直到过一会你的浏览器就会自动打开一个stable-diffusion的窗口，运行成功！

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1AwM4AZHypEPpXZwHQcAjcYDx9D2IIfxq6SGkSbfl7LlpXcDlicfjj4Q/640?wx_fmt=png)

  
**二****. 生成AI图**

stable-diffusion启动成功，接下来咱们愉快的开始生成你的专属AI妹子~

咱们先把左上角的模型选成ChilloutMix，这个就是专门生成真人照片用的模型。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1NGW9wzWNibCQENqiaV3RooDLq1Z7n1lnESL6Kibygyco8QuZvzVOicxatg/640?wx_fmt=png)

当然，stable-diffusion的世界里还有很多很多各种模型，比如能生成很多很多风格的Anythin4.5，比如能生成逼真3D幻想风格的DreamShaper，这个大家以后可以自己探索~这篇先教大家生成AI妹子。

然后我这里直接给大家一组关键词  

<lora:koreanDollLikeness\_v15:0.66>, best quality, ultra high res, (photorealistic:1.4), 1girl, beige sweater, smile, laughing, bare shoulders, solo focus, (full body), (platinum pink hair:1), ((puffy eyes)), looking at viewer, facing front, closeup  
Negative prompt: paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans  
Steps: 28, Sampler: DPM++ SDE Karras, CFG scale: 7, Seed: 1735215259, Size: 640x768, Model hash: fc2511737a, Model: chilloutmix\_NiPrunedFp32Fix, Denoising strength: 0.75, Clip skip: 2, Mask blur: 4

先不用管是什么意思，直接复制，然后粘贴到stable-diffusion的这个位置  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1WrgGWA0SqfEpu0eN5RPloLBXUH5HWndjFCC0xT7xqs0JKrKVFyh18g/640?wx_fmt=png)

然后点击这个小箭头

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk14cWxmF1VryAonbbmNXIloGyCicB2iczr3z9HHwttgxnNFiaqAZtfYYafw/640?wx_fmt=png)

就能看到字段变啦，大家先只要知道上面两个输入框是什么意思就行了

第一个框：提示词，Prompt，我们的图片会按照你的提示词来生成，每个提示词用逗号隔开，比如我们这次输入的提示词  

<lora:koreanDollLikeness\_v15:0.66>, best quality, ultra high res, (photorealistic:1.4), 1girl, beige sweater, smile, laughing, bare shoulders, solo focus, (full body), (platinum pink hair:1), ((puffy eyes)), looking at viewer, facing front, closeup

翻译过来就是

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1n2I1fq4Gcqdu4Qic0wOibOUsSCLmbjYvb2ibfibJib3ibFlhvKvVqcCucibiaQ/640?wx_fmt=png)

<lora:koreanDollLikeness\_v15:0.66>, best quality, ultra high res, (photorealistic:1.4), 这一部分大家可以不要动，无脑使用，而后面的提示词可以根据你的喜好随意更换。

第二个框：反向提示词，Negative prompt，意思就是你输入的词绝对不会出现，比如咱们这次输入的  

paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans

翻译过来就是

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1G98d06aiaWkHHHC4a8e9clxrybWotflaF8U50PHVA1kdIo4gg4RpPicQ/640?wx_fmt=png)

输完以后，咱们把种子这块的小骰子点一下，让左边的参数变成-1

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1ibvg8ljuOzEfXBPoya8NlrT6Yic8ia5XYoCvVas9ciafQ5AXqjpD1wWf8Q/640?wx_fmt=png)

全部完成以后，咱们愉快的点击右上角那个巨大的生成！

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1jicVHdRwm2vN4xRRLYW9H5sy7sQ7Dq2wDWvcgPojozOKdNGLLa2lNQg/640?wx_fmt=png)

嘟嘟嘟的跑起来后，你就可以看到自己生成的虚拟小姐姐啦。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrIcXBTiag1o1wbqvvIqWmk1aDiczloDR0df7Mntt3YVxgA99gCKRL30boUr0Zy823TMGz0qF0IsCxg/640?wx_fmt=png)

  

想生成不同风格图，直接换后面的提示词就可以，开心的玩起来吧~  

下一期，我再详细给教大家不同风格的模型用法、神器级别的可以控制动作插件controlnet。大家帮忙点个关注给个赞吧哈哈。  

写在最后。

AI无容置疑，已经到了一个危险和机遇共存的时间点。

**AI好玩，但是绝对不要用来做任何影响社会秩序、侵犯版权肖像权的事情，更不要用来违法犯罪！**  

以上，创作不易，有用的话请帮忙点个在看，感恩。

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言