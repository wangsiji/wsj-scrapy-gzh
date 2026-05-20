     阿里深夜开源推理模型QwQ-32B，性能比肩R1满血版。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

阿里深夜开源推理模型QwQ-32B，性能比肩R1满血版。
============================

原创 数字生命卡兹克 数字生命卡兹克 2025-03-06 08:17 北京

> 原文地址: [https://mp.weixin.qq.com/s/zeBECoWJ4IqtiTTOevJIig](https://mp.weixin.qq.com/s/zeBECoWJ4IqtiTTOevJIig)

今夜，Manus发布之后，随之而来赶到战场的，是阿里。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2ppd6XonCMUIo2UEOLeJlQ3fKiaVDRERtotRciaibtLGSpWmdhMbC3GLSOg/640?wx_fmt=png&from=appmsg)

凌晨3点，阿里开源了他们全新的推理模型。

QwQ-32B。

本来还有点意识模糊，当看到他们发出来的性能比对图，我人傻了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2piaTL3Ou5689RWhCLjO3F7R4RfuiahqW7yHxU3QHQHbCO7v3Pib4PvTibIw/640?wx_fmt=png&from=appmsg)

不是，我没看懂，这特么是个什么怪物。

在几乎所有数据集里，QwQ-32B 都已经能跟满血版DeepSeek R1（671B）表现相当了。尤其是作为QwQ-32B 的主攻方向的数学和代码。

而且，QwQ-32B在基准测试上的性能跑分，几乎拉开o1-mini一个身位。

我人已傻。

今天这夜，对我的冲击有一点大。

GPT4.5刚刚证明传统的那套快撞墙了，转头阿里就来给你掏个大的，说，你看，强化学习还是能卷的，这条路，远远还没到头。

这么令人诧异的性能表现，其实也跟这两天在arxiv出来的一篇爆火论文互相印证了。

一堆斯坦福教授集中讨论，为什么Qwen-2.5-3B一开始就能自己检查自己的答案，Llama-3.2-3B却不行。

最后的原因还是落在了Qwen团队的强化学习上。因为，这能让模型自己学会一些关键的“思考习惯”。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2pa2HunzmwtQickY9T7eaicZqPnDHOktafT2icibxyLKO4fiar8xdI5nrC8QA/640?wx_fmt=png&from=appmsg)

没啥可说的，阿里NB。QwenNB。

QwQ-32B开源链接在此：

魔搭开源链接：https://modelscope.cn/models/Qwen/QwQ-32B

huggingface开源链接：https://huggingface.co/Qwen/QwQ-32B

当然如果想直接上手体验，官方也给出了在线体验的地址：

https://chat.qwen.ai/?models=Qwen2.5-Plus

左上角模型选择Qwen2.5-Plus，然后开启Thinking（QwQ），就能用QwQ-32B了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2pEJb2IicsyiaqpVjuuiaqYyFakiaag6A8iaicLbt4ffwEhafB5FNt03FjkBIw/640?wx_fmt=png&from=appmsg)

我这边也第一时间在AutoDL租了一台A800-80G的显卡，然后把模型下载了下来，并部署测试了一下这个怪物。综合体验下来，本地部署版和网页版其实是一样的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2pVYzbEnYmsicpDA3GwjtmS47ysxvBQI3wmrrtpEQdfHIqKrk7sapszFw/640?wx_fmt=png&from=appmsg)

性能曲线是这样的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2pkvl4Fv8zAxzCrxExyLjongoOzzG1j9gJWg0cw8eb3fia1VJEibA6FUAA/640?wx_fmt=png&from=appmsg)

我也做了一些测试。

首先就是，我觉得赛博半仙易主了。这回的QwQ-32B真的能当八字算命大师了。

懂得都懂，AI自媒体人的命也是命，它掐指一算，就知道我经常熬大夜，狂肝文章。下半年家里那些鸡毛蒜皮的事就别提了，为了搭我的摄影棚，把景深弄得更到位，我是真得搬家啊。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpPCVqw0sjLDbMHLoM6FNA3qC6HyNVVcibLZQndXGYRYGaibaf8AtUGKprfGA7WFwlQbDicwT9nOSZYw/640?wx_fmt=png&from=appmsg)

当然，AI算命只能算是个开胃菜，接下来还是得认真测下QwQ-32B的数学能力。

然后就是拿我的著名的国庆调休题来难为下这类推理模型了：

**这是中国2024年9月9日（星期一）开始到10月13日的放假调休安排:上6休3上3休2上5休1上2休7再上5休1。请你告诉我除了我本来该休的周末，我因为放假多休息了几天？**

比如Grok3这种，开了推理还是直接炸了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2pn2jpl6IhiaG1ia78ia9coBGddXtTC1034WQicibToK07WuicpjHMHLgxus2Q/640?wx_fmt=png&from=appmsg)

答案明明是4天，你咋独自加了3天。。。

而看看QwQ-32B，在一顿小推理之后。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2pra9s2mrd8fjEpgibfUYfBkGSspw1n7jjiaG9oMkOMO2OG1nkN1ibtutSw/640?wx_fmt=png&from=appmsg)

最后答案，完全正确。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2pjQphn9DfagJfkYXmCcliahPNAVsliaibALWS05ib6Vdw3Jp5UIiaGeqetAw/640?wx_fmt=png&from=appmsg)

要知道，这可只是一个32B的小模型啊。。

然后我还试了一下代码能力。我就直接去Leetcode找了一道困难级别的算法题，解数独。

可能有人不知道Leetcode是啥，LeetCode 是一个全球知名的在线编程练习平台，这个平台有大量不同难度的算法题库，从简单到困难的各种编程题都有。

我直接把解数独的题目还有代码模板丢给QwQ-32B，让它给出最优解的代码：

_编写一个程序，通过填充空格来解决数独问题。_

_数独的解法需遵循如下规则：_

_数字 1-9 在每一行只能出现一次。_

_数字 1-9 在每一列只能出现一次。_

_数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）_

_数独部分空格内已填入了数字，空白格用 '.' 表示。_

_然后给定你一个类，给我一个比较好的方案：_

_class Solution(object):_

_def solveSudoku(self, board):_

_"""_

_:type board: List\[List\[__str__\]\]_

_:rtype: None Do not return anything, modify board in-place instead._

_"""_

经过几分钟的思考，这道题的完整最优解代码也是被QwQ-32B成功给出。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2p4AUxPpicdWPOY8SsAH4iaWXDHDtDO89dCo6lDysUr0DsPowjeWYU28dA/640?wx_fmt=png&from=appmsg)

我把这段代码粘贴到了Leetcode平台上，直接提交，没想到这段代码竟然完美的通过了全部测试用例吗，而且执行用时才127ms，击败了93%的在这个算法题库做尝试的人。

说实话，这个结果让我挺惊讶的，毕竟127ms的用时，看平均的用时基本都在1691ms左右。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURooZRibaxzle1BGawXJgTO2p1ibtJbTOUYrDQnXQNI4neLlqqmgibHGE5iaG6SouXP593wlJ1C7QABcdQ/640?wx_fmt=png&from=appmsg)

很强，但是我觉得最强的，还是它未来的生态。

32B和671B，对于本地算力的要求，或者是云服务的成本来说，差别实在是太大太大了。

671B，在FP16精度下需要1400G的显存，这个门槛有多高大家懂得都懂。

而现在，32B的QwQ，4张4090就能跑，这是将近15倍的差距。

而且，智能水平差不多。

这也意味着很多普通企业还有普通开发者，可以直接拿到一个足以对标DeepSeek R1的逻辑推理、数学推理、代码思考能力的大模型，而且还开源，能在自家环境中任意调试、微调、二次开发。

更何况，阿里云上的资源、ModelScope、Hugging Face镜像都能对接，瞬间就把部署壁垒降到几乎为零。

对于那些创新型创业者、小型团队，或者想要做专业AI应用的公司而言，我说实话，这就是天降神兵。

对于大多数的企业垂直场景，一个优秀的32B的模型真的已经足以应付很很多，没必要非得上600多亿参数、又烧又贵的巨无霸。

这波QwQ-32B开源的意义，还是非常强的。

它用实力证明RLHF路线还能玩出花，打破了一些人对GPT4.5撞墙后的过度悲观。

用中等规模却拿到高级性能，给开源界注入了强大信心，你也不必搞那种天价设备和超大规模，也有机会跟国际巨头同场竞技。

真的，昨夜爆火的Manus，在技术架构上，也是Claude+很多微调的Qwen小模型。

那这次QwQ-32B，又是一次智能的提升。

每个大厂、每个团队都在全力冲刺，新的风暴还会一个接一个出现。

睡前一抬头，日历翻到新的数字。

又是个不眠之夜。

阿里NB，QwenNB。

我们中国的团队。

就是NB。

愿我们都能见证更多奇迹。

晚安，或者早安吧。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、芝兰山、wei

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言