     DeepSeek们越来越聪明，却也越来越不听话了。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

DeepSeek们越来越聪明，却也越来越不听话了。
=========================

原创 数字生命卡兹克 数字生命卡兹克 2025-05-20 09:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/BOvXyrHOuTHwzeE2xO0OKg](https://mp.weixin.qq.com/s/BOvXyrHOuTHwzeE2xO0OKg)

在今年，DeepSeek R1火了之后。

几乎快形成了一个共识，就是：

AI推理能力越强，执行任务时就应该越聪明。

从2022年Chain-of-Thought横空出世，到今天Gemini 2.5 Pro、OpenAI o3、DeepSeek-R1、Qwen3，这些旗舰模型的统治性表现，我们一直相信，让模型先想一想，是一个几乎不会出错的策略。

不过，这种聪明，也会带来一些副作用。

就是提示词遵循能力，变得越来越差。

换句话说，就是越来越不听你的话了。

我在过年期间写DeepSeek的攻略文：[DeepSeek的提示词技巧，就是没有技巧。](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647668247&idx=1&sn=c7898e4c2aa11703cd79011500f27f85&scene=21#wechat_redirect)的时候，也提到了这一点。

不过，这只是我自己使用中的感觉，它变的越来越聪明，但是感觉，却越来越不听话了，以至于我现在，最常用的模型，开始越来越变成了GPT4o，所有的推理模型，反而会用的越来越少了。

不过，确实没有经历过验证，所以也不是特别敢说。

直到昨晚回来，在扒拉论文的时候，看到一篇提到这个话题的论文，我读完以后，我觉得，终于可以来聊聊这个事了。

这篇论文叫，《When Thinking Fails: The Pitfalls of Reasoning for Instruction-Following in LLMs》

网址在此：https://arxiv.org/abs/2505.11423

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqePVR6J5mFSY4pPm7QUR1D84BgDu3pWwJSobfibnn63pDx3dictCw1Q9WokiaNKwqcqGBc7TgRYhdXQ/640?wx_fmt=png&from=appmsg)

它用用极其扎实的实验，验证了上述的论点。

当你让模型开始推理，它反而更容易违反你给出的指令。

是的，**当思考失败，这聪明的智商，反而就变成了负担。**

**我尽量用人话，来给大家简单的科普一下论文中的实验和内容，再说说我的理解。**

**先说论文本身。**

**论文的研究团队来自Harvard、Amazon和NYU，他们花了好几个月，干了一件特别简单却没人认真做过的事，就是把这个思考过程应用在一个最基础、最现实、最需要稳定性的场景上：**

**听懂人类指令，然后照做。**

**他们做了两组测试。**

第一组叫IFEval，一个标准的执行类任务测试集，每个任务都非常简单。

比如“写400字以上”“必须提到AI三次”“输出格式必须是JSON”“句末不能有标点”等等。

所有的任务都有明确的可验证标准，要么做对要么做错，没有模糊地带。

第二组叫ComplexBench，这就更有趣了，是那种“多约束、逻辑组合、顺序嵌套”的复杂指令，比如“先做A中的三选一，再加上B的格式要求，最后加上C的语言限制”。

听起来好像推理模型在这种任务上应该更有优势？毕竟这不是随便一两句话就能糊弄过去的内容。

然而，论文的结论惊人又统一：**绝大多数模型在使用CoT推理后，执行准确率反而下降了**。而且，下降得还不轻。

**他们一共测了15个模型，涵盖开源的（比如LLaMA、Mixtral、Qwen2.5、DeepSeek系列）和闭源的（GPT-4o-mini、Claude 3.5/3.7等等）。**

**在IFEval上，14个模型中有13个使用CoT时准确率变低；在ComplexBench上，**所有模型**都在使用CoT后，表现变差。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqePVR6J5mFSY4pPm7QUR1DgcDS2MWeTicPW2ttEyXU2Xn2j4hotgRZEAwjXnyyZKnahnJbQWgAic1A/640?wx_fmt=png&from=appmsg)

**甚至连像 LLaMA-3-70B-Instruct 这种参数量较大、训练完整的模型，在使用CoT时也会从85.6%的准确率掉到77.3%。**

**8个点的损失，在工业级任务里其实非常恐怖了。**

**还有推理模型模型开不开推理的对比，典型的就是DeeSeek V3和R1，还有Claude 3.7这种混合模型。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqePVR6J5mFSY4pPm7QUR1DguVmHyQ0oKQtZ84PPKJvSH7lSASaOsFPE9EiaJPPxKdbCGTibZ64h9HQ/640?wx_fmt=png&from=appmsg)

**会发现，几乎都有下降。**

**他们手工扒拉了1500多个样本，看了所有的思维链，总结出来了原因。**

他们发现，当模型用了思维链条之后，它确实变聪明了，比如能更好地遵守格式、注意字数、精确用词，像是“必须用15个大写字母”这种题，靠CoT反而更稳。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqePVR6J5mFSY4pPm7QUR1DaDvx64HIOwlMLz1eTKBNazRSg0ibVelWe0ibcyaJhazTHda8X3QIroaA/640?wx_fmt=png&from=appmsg)

但，它也变得神经质了。

它开始自作主张，觉得自己懂了任务的深层含义，于是它会擅自删掉、修改，甚至加上有帮助的解释。

论文里提到很多模型会在“只允许输出法语”的题目中，善意地补上一句“这是‘Bonjour’的英文翻译”，在“只能输出引号内容”的任务里，自动补充前情摘要。

它太想表现自己了，太想证明我真的理解你了，于是它忘了本该严格遵守的指令。这就是它学会推理之后的副作用。

**为了找出这个副作用的根源，他们引入了一个新概念：**

**约束注意力（Constraint Attention）。**

**他们发现，不管是GPT-4o-mini，还是Claude 3.7，几乎所有模型在用了CoT思维链后，它们的注意力，也就是在生成答案时，关注任务描述中“关键限制”的那部分注意力，明显下降。**

**你可以理解为，当你要求一个人边想边说，他反而忘了原本你只要他复述句子的简单目标。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqePVR6J5mFSY4pPm7QUR1D1HDX4iboNDciafcYibV08O9QzupiczicjiandDsxhkK5gBvXDcqfCq5C9d7A/640?wx_fmt=png&from=appmsg)

**更有趣的是，他们还测了一个我一直想知道的问题的答案：**

**就是CoT思考越长，准确率越高吗？**

**结果是，几乎没有显著相关性。**

**思考长度和是否做对，几乎没有直接联系。**

**也就是说，更努力≠更对。**

所以，其实结论很简单，就是在要求非常规范、精准的大模型输出任务上，完全不需要使用推理模型或者思维链，直接上非推理模型，效果会更好。

但是，如果，就是非要用，希望提升整体指令遵循效果呢？

**他们也基于自己的测试，给出了4种方案。**

第一种，是“Few-Shot少样本示例”。

给模型提前看几个做对的例子。

效果一般般，问题在于输入太长，而且示例选自已有模型，容易有偏。

第二种，是“Self-Reflection 自我反思”。

模型第一次输出之后，再自己复查一遍，“你刚才做对了吗？”然后再决定是否修改。

这招对大模型效果很好，因为它们确实能自省，但小模型效果惨不忍睹，因为它们智力不够，就像个不知错的小孩，越反思越错。

第三种，是“Self-Selective Reasoning”。让模型自己判断这个任务是否需要推理。

结果是：它召回率很高，基本上只要推理有用它都能猜出来，但精确度很低，**一言不合就开始推理**，哪怕你只是让它改个词。

第四种是最有效的，“Classifier-Selective Reasoning”。

直接训练一个小模型作为判断器，来帮主模型判断某个任务是否该启用CoT。

效果显著，在两个测试集上几乎都能恢复失去的准确率，甚至有些模型比原始还高。

缺点就是每个主模型都要单独训练一个判断器，成本太高。。。

这篇论文大概就是这样，对我自己非常有帮助，我看的论文不多，这篇是我自己看的，我认为对“CoT推理在执行任务中的潜在副作用”这个话题，比较完整的研究之一。

同时，我也想聊聊，这篇论文对我的启示。

我们总觉得，聪明，就意味着知道得多、分析得细、每个变量都不放过.

但事实上，真正强大的智能，从来都不是把所有细节一股脑地扫过一遍，而是，**知道在哪一秒钟，把注意力放在哪个点上**。

比如我们小时候考试，很多人因为太想得高分，最后反而在最简单的题上丢分。

成年人做选择，明明已经知道该怎么做了，却非得做个SWOT分析表、拉个10页PPT讨论，最后被复杂困死。

公司做决策，明明方向明确，却因为分析得太多、风险评估太细，最后团队谁也不敢拍板，错过风口。

AI其实跟人很像。

上面很多CoT的验证，还有Constraint Attention，其实也证明了，**大模型不是笨，而是思维资源错配了**。  

你让它完成任务，它却跑去想着“怎么把这段话说得更优雅”、“这句话需不需要加个逻辑转折”、“前后是不是够自然”。

你让它干活，它在脑子里脑补了几万种情节。

但是，真正牛逼的智能，其实应该是聚焦。

比如你叫一个人帮你看一下一份报告有没有错，一个低阶执行者可能就只会一句句校对标点。

而一个高阶智能，可能会反过来先问你，“你重点是要我看错字，还是看数据逻辑？”

你说清楚重点，他就能把80%的注意力锁死在正确位置。

而如果他啥都想看一点，最后很可能错得最离谱。

我们真正需要的，可能，是**对“该想什么”有判断能力的智能**。

就像我们人类那些最令人敬畏的时刻，不是我们知道多少，而是我们能瞬间把注意力聚焦在关键节点上。

危机时刻，考场钟响，夜深人静一个念头浮上心头的时候，你知道的，你不能全看，你只能看准。

**那个“看准”，在我看来，可能就是智能真正的体现。**

这一点，看似简单，却足够让AI从“聪明”，变成“智能”。

这就是我读完论文之后，真正想跟大家分享的东西。

我们不缺思考的能力，我们缺的，是思考的分寸感。

注意力，不是撒网。

而是出击。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言