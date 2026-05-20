     一文详解DeepSeek开源的FlashMLA，他们才是真正的“源神”。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

一文详解DeepSeek开源的FlashMLA，他们才是真正的“源神”。
====================================

原创 数字生命卡兹克 数字生命卡兹克 2025-02-24 11:12 北京

> 原文地址: [https://mp.weixin.qq.com/s/I3UMh19L8mQnAewBMa9YqQ](https://mp.weixin.qq.com/s/I3UMh19L8mQnAewBMa9YqQ)

刚刚，万众瞩目的DeepSeek，开源了他们第一天的项目。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo6vK0f00YTZPxCQiaUkIfCTEEuVYN8Jp4lnyV6EPfZmia1m8pz8ibqOpfMyfroHGwZKF9Libep6kTicew/640?wx_fmt=png&from=appmsg)

开源地址在此：  

https://github.com/deepseek-ai/FlashMLA

开源的是一个叫FlashMLA的东西。

不到半小时，Github已经已经300多Star了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo6vK0f00YTZPxCQiaUkIfCTFTticYiaGediaOzHIxBF40AyfGuIl774dD8UJd3k9fuRczzBQcR3OepAA/640?wx_fmt=png&from=appmsg)

几个参数：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo6vK0f00YTZPxCQiaUkIfCTgMpwRPA9oEsd0bJLgX6zbB3KKFjiaQP4bzcQvVZbgwNiaZdStlonZiccQ/640?wx_fmt=png&from=appmsg)

核心的一句话是：

**“FlashMLA is an efficient MLA decoding kernel for Hopper GPUs, optimized for variable-length sequences serving.”**  

**翻译过来就是：FlashMLA是一款面向Hopper GPU的高效MLA解码内核，并针对可变长度序列的服务场景进行了优化。**

因为确实比较硬核，我只能说用我仅有的知识，给大家简单科普一下这是个啥，可能会有错误，不保证对，如果出现错误欢迎大佬评论区拍砖。  

把这句话拆解一下。

**“MLA decoding kernel”。**

这里的“MLA”指的是Multi-head Latent Attention，多头潜在注意力，DeepSeek降低成本的王炸，反正它是个专门用来做解码阶段的注意力加速器。

大模型有两个主要阶段：训练（包括prefill）和推理解码（infer decoding）。在解码阶段，我们往往需要一次一次地拿KV缓存出来，反复计算，所以当序列变长之后，这部分开销会爆炸似的增长。如果能在解码阶段有更强的核去优化，意味着你的大模型可以更快地产出结果，特别对像这种长上下文对话就很关键。

**第二，“for Hopper GPUs”。**

英伟达的卡有几个架构，包括A架构和H架构。

A是Ampere架构（2020年发布），是NVIDIA的第七代GPU架构，主打通用计算和高性能AI训练/推理，典型代表型号为A100。

H代表Hopper架构（2022年发布），是NVIDIA的第九代架构（跳过第八代），目前最新的，专为超大规模AI和超算设计，显著优化了Transformer模型性能，典型的就是H100，不过因为国内问题，能用到的都是阉割版的H800。

所以，大家就可以明白，FlashMLA是DeepSeek专门针对NVIDIA H800这一代高端加速卡做的深度优化。

他们在release note里还说跑在H800上能达到“3000 GB/s memory-bound & 580 TFLOPS compute-bound”，这等于在“内存带宽”和“浮点算力”两方面都拉到极限了。基本已经是我见过的最逼近巅峰的了。

他们在致谢了写了灵感来自于FlashAttention。

我就去翻了下那个项目。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo6vK0f00YTZPxCQiaUkIfCTmISMibITSeQHVztZGrDBQOOJBVz0MLTt9lpUsbicWmecwSmlOHicYLNjA/640?wx_fmt=webp&from=appmsg)

相比FlashAttention-2，FlashMLA接近翻了2倍，甚至都能跟FlashAttention-3还差点，而别人是H100优化的，DeepSeek是针对H800优化的。

**第三，“optimized for variable-length sequences.” 。**

就是说它不仅仅适合固定batch，还对那种“每个人输入长度不一样，随时变更token长度”的场景特别好。

因为就大模型的实际应用而言，用户往往输入并不规则，随时来个长上下文对话或者给你干上去一个超长PDF，这就需要内核支持“动态序列”，同时还能保持高效，而这块，DeepSeek也做了大幅的优化。

目前整体上也可以开箱即用。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo6vK0f00YTZPxCQiaUkIfCTn8mNfJCdMAJlzg5HSM2qq5hsGG3TiaOQ7x1ApDWBa8zN8VIDjGs3D5g/640?wx_fmt=png&from=appmsg)

DeepSeek这是真的把自己最牛逼的东西开源出来了。

这尼玛，才是真正的OpenAI啊。

想起来了他们前几天发的论文《Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention》，整个目标也都是有异曲同工之妙。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo6vK0f00YTZPxCQiaUkIfCT7vyKbja1ccCUU2PSQbvuic9SAjLHfd3nZHDby4hqibVBLHmZ4j5EJfBA/640?wx_fmt=png&from=appmsg)

如果说FlashMLA是针对推理解码做的“终极性能爆破”，那么Native Sparse Attention就是对训练和推理做更全面的“稀疏化改革”。

两者结合到一起，意思就是DeepSeek在告诉你。

**“无论训练还是推理，我都要把硬件榨干，要做就做最猛的AI。”** 

对于整个AI生态来说，这是一件天大的好事。

特别是国内。

越多的开源优化，意味着以后大家都可以在高效注意力、稀疏推理、长上下文训练等方面取得突破，不用像过去那样闭源大厂独家享受。

如果你是小白或者纯产品经理，可以把这件事情当做：

**苹果又给iPhone做了一个专门的GPU调教，所以游戏跑得更爽了。**

只不过，这次是DeepSeek在给AI大模型做专门的GPU调教，把H800的极限性能都薅出来，换来更快的推理和训练速度。

这是妥妥的GPU性能红利。

所以我对DeepSeek挺佩服，敢搞硬件极限那一套，敢把论文跟开源项目一起放出来，而且频率这么高。

而且这还只是第一天。

后面还有四天，不敢想他们还会放出来多牛逼的东西出来。。

希望这篇小白友好版的文章能让你对FlashMLA有个更直观的理解。

**既然没卡，没有资源。**

**那我们自己，就特娘的打下那一片天。** 

**感谢DeepSeek。**

**你才是真正的源神。**

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言