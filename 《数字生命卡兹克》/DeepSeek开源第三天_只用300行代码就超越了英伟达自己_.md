     DeepSeek开源第三天，只用300行代码就超越了英伟达自己。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

DeepSeek开源第三天，只用300行代码就超越了英伟达自己。
================================

原创 数字生命卡兹克 数字生命卡兹克 2025-02-26 10:49 北京

> 原文地址: [https://mp.weixin.qq.com/s/Y1VAY8eA4OSHHBALCjxY6w](https://mp.weixin.qq.com/s/Y1VAY8eA4OSHHBALCjxY6w)

不能再肝了，但我又觉得DeepSeek值得。。。

这两天，DeepSeek的高强度开源波，一山更比一山高。

先是给GPU安超频加速外挂的[FlashMLA](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647668908&idx=1&sn=403d802c370eaced19f43d6ace8e8557&scene=21#wechat_redirect)，又是叫英伟达知道“原来GPU没有商业护城河”的[DeepEP](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647668943&idx=1&sn=b3cebbb317239a34d8e5e5c2cd5c7c83&scene=21#wechat_redirect)。

我也都第一时间给大家带来了报道。

在追求效率、把硬件资源干下来的路上，DeepSeek快成AI性能效率上的Godfather了。。。

这回，他们开源的是一个叫做**DeepGEMM**的玩意儿，专门给当时爆cei全网的DeepSeek-V3做的。

Github星星没半小时，就几百个了。点的越多，意味着开源友友们越喜爱和越关注这个代码仓库，水分那是相当的少。一般几千的星星就已经算是爆款了，半小时就几百，这个含金量你懂的。

开源链接在此：https://github.com/deepseek-ai/DeepGEMM?tab=readme-ov-file

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURosfFrtiaMa0PJrpK5TTfg0edw0DricVUZUiaESPzYEXWf0cwic3xicvygoMsicNDoOX7iajibJerQWEHlKkg/640?wx_fmt=png&from=appmsg)

这东西，倒也没那么难懂。

举个例子，假如我结婚了。场面特别特别大，记得是假如。。。

几百万人组成的迎亲队伍、点鞭炮得点几亿种、接亲队伍也叫个几百万人来，甚至我再搞点大的出来，比如弄个几万盏灯光秀。

所有的一切的一切都需要计算好时间点，相互之间得互相搭配。而DeepGEMM这东西，能把以上所有东西塞进一个矩阵里。

所有迎亲队伍的实时行走轨迹、啥时候点鞭炮的精细时间规划、接亲队伍得到哪里等、等多久，几万盏灯光秀和几千万首音乐秀，几分几秒，该怎么配合，效果最好，等等。

全都能放进矩阵里计算，这都快成在天上俯瞰人间的God了。。。

用技术语言说，就是：

DeepGEMM 是一个为 DeepSeek-V3 专门设计的，用于 FP8 的，通用矩阵乘法（GEMM）库。还支持**普通的和专家混合（Mix-of-Experts，MoE）分组 GEMM**。

安装时，你都无需编译，只通过一个轻量级的即时编译（JIT）模块，在运行时就可以编译所有内核了。牛逼，一点多余东西都不舍得让你多干活。

**而且，只用了300行代码，实在是牛逼。。。**

目前，DeepGEMM跟前两天一样，还是只支持H卡。它为了让FP8这种速度快但精度偏低的计算方式变得更准确，利用了CUDA核心做了两次累加。

简单说就是先用FP8完成快速计算，然后再用CUDA核心对结果进行更精细的再加工，这样既能保持速度快，还能把精度提上去。

DeepGEMM也借鉴了英伟达CUTLASS和CuTe的一些概念。

CUTLASS 是基于英伟达明星当家CUDA架构。简单说，它是一个写给 NVIDIA显卡的工具包，专门用来加速“矩阵计算”的。

英伟达的CUTLASS实在是过于高效，以至于被用来构建内核时，几乎能帮显卡把矩阵计算的性能榨到极限，跑到显卡的理论峰值。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURosfFrtiaMa0PJrpK5TTfg0eDwNNS2IlefDWbBuOqfcnzRSgJLPlLIbRuDt9eq0JIkic8ytoLia8kp5Q/640?wx_fmt=png&from=appmsg)

但是如果你手里的硬件没那么强大，就像很多现在的AI公司们还停在上一代的卡上时，CUTLASS这种大而全的加速套件，就有点用不上了。

CUTLASS虽然时哥通用、功能强大的矩阵加速库，但是DeepGEMM这种激进的优化方式更专注、更轻量。

深刻的展现了DeepSeek那种“抠”到极致的理念。

把性能也抠到了极限。

性能只要卡的不死，DeepSeek就能拿效率调优这条至简大路冲出来，无形中连美国算力封锁都给捅破了。。。

它完全没有一点对英伟达项目的模版or代数的过分的依赖度，全凭自主。

而且不止是轻量化，性能也是直接起飞。

按他们的话说，

团队说，能够匹配甚至超越英伟达、ADM等等专家专门调优的库。。。

比英伟达自己的CUTLASS 3.6，速度还提升了2.7倍。

他们在H800上，测试了 DeepSeek-V3 和 R1 推理中可能用到的所有矩阵情况，性能水平，我都整理在这了。

先是密集模型档，估计老黄那个项目的人，也很难想明白，几百行代码怎么调优调成这样的。。。

之前不是都说，硬件是有护城河的嘛。。。现在看起来，DeepSeek比英伟达都懂GPU。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURosfFrtiaMa0PJrpK5TTfg0eD76BOPmUuYiakn9dFSibcBdLBQ92FjTiaLTlrqeosyXz39O5x03o4c2Tg/640?wx_fmt=png&from=appmsg)

然后就是现在被称为AI未来方向之一的专家混合模型MoE了。它在处理复杂任务上独树一帜。整体的性能，实在是太硬核了。数据如下：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURosfFrtiaMa0PJrpK5TTfg0eYsdlkoqjl4PxOhbibHYiaia0UHXR3ibbAEb4rGmKxxA4AenrR1XzPmNNQA/640?wx_fmt=png&from=appmsg)

但DeepSeek的人也确实说了。

DeepGEMM虽然非常牛逼，但是在某些情况上的表现确实不太好，欢迎所有人一起改进。

具体的部署上，依旧和之前每次DeepSeek开源时的动作一样，把饭喂到你嘴边，顺便走的时候，再给你擦擦嘴。

因为无需编译，部署速度会更快、更顺畅。这让我想起来了当年的贴吧大神们，只留下宝典教程里最核心的部分，挥挥衣袖，就跑了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURosfFrtiaMa0PJrpK5TTfg0eYkbcjFD8F5TRMZtKicNjNCHISt9DxsRUWj3sY8yGJN3LNOq8NcIIOhw/640?wx_fmt=png&from=appmsg)

随着下一代基座模型，比如DeepSeek V4、GPT-4.5等等的参数和复杂度继续增长时，深入到底层进行优化的DeepGEMM这种库，真的会越来越重要。  

AI圈子内曾经充斥着，闭源才是通向AGI的论调。

这平等地伤害了，每一个踏进AI大门的普通人们。

闭源的AI世界，就像是黑暗森林。

每个人都是拿着枪追着篝火的猎人。

但DeepSeek这一举。

让我突然想起来《教父》里那句名言。

永远不要动怒。

绝不要威胁。

要讲道理。

开源就是DeepSeek这群家伙们的道理。

共勉。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、芝兰山

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言