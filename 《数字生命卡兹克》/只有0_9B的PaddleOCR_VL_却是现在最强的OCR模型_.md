     只有0.9B的PaddleOCR-VL，却是现在最强的OCR模型。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

只有0.9B的PaddleOCR-VL，却是现在最强的OCR模型。
=================================

原创 数字生命卡兹克 数字生命卡兹克 2025-10-23 09:30 广东

> 原文地址: [https://mp.weixin.qq.com/s/bUEDLhF6zoy9nOA3qvFqBg](https://mp.weixin.qq.com/s/bUEDLhF6zoy9nOA3qvFqBg)

这几天，OCR这个词，绝对是整个AI圈最火的词。

因为DeepSeek-OCR，甚至让OCR这个赛道文艺复兴，又给直接带火了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQose7LibibqmTODXSmGia1Z0z7r6kZOFqRljK4e4iaNAK9OmropZsPX2BAvFw/640?wx_fmt=png&from=appmsg)

整个Hugging Face的趋势版里，前4有3个OCR，甚至Qwen3-VL-8B也能干OCR的活，说一句全员OCR真的不过分。

然后在我上一篇讲DeepSeek-OCR文章的评论区里，有很多朋友都在把DeepSeek-OCR跟PaddleOCR-VL做对比，也有很多人都在问，能不能再解读一下百度那个OCR模型（也就是PaddleOCR-VL）。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosylGOcTyXUXyKVBWg0U1kxhqtFu6u0EeTQlQQsGcHYngUx796rv1j0w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQos9HuQyS1SbPHcA6iagUa4Hlu8tvzwBwUFQicmlpdBwWJJjtoZSUQ4IARQ/640?wx_fmt=png&from=appmsg)

所以我也觉得，不如就来写一篇关于PaddleOCR-VL的内容吧。

非常坦诚的讲，百度家的东西，我写的一直都会非常谨慎。

但是这个PaddleOCR-VL，是我真的觉得值得一写的。

因为，确实很牛逼。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosJ9gQL0lqQbWzsGj2XR4d80a8ibT0reqjiaQQlibtvkj6mbYricB7OO8cmw/640?wx_fmt=png&from=appmsg)

首先提一下，PaddleOCR这个项目本身，不是啥新东西，这是百度一直都在做的项目，很多年了，最早期甚至可以追溯到2020年，也是一直是开源的姿态。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosPERUE4H46icVnhQwOnaGKzDfRRN2YFicUSlhgV28evic7pfYmciaGhNenA/640?wx_fmt=png&from=appmsg)

后来他们就不断的迭代，整整5年时间，成了整个OCR领域最火的开源，现在也应该是现在Github上Star最高的OCR项目，有60K，基本属于断档领先。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosicP3ub0rSjGWPWud2k7bZQOtsVlfX3h5ia1YKqVRyemAhMy02NjyQjXg/640?wx_fmt=png&from=appmsg)

而PaddleOCR-VL模型，就是他们前几天开源了他们的PaddleOCR系列里最新的模型，这也是第一次，把大模型用在了整个OCR文档解析的最核心的位置。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosugVUxVQeUAGTm12z3D65FgnCWJAhdtLDJYUv4qWkK3C6hkFNnaacLw/640?wx_fmt=png&from=appmsg)

整个模型只有0.9B，但是几乎在OCR的评测集叫OmniDocBench v1.5的所有子项，都做到了SOTA。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosFFTlHuvRKAFkiagf8ADIsAABiaibWpTiaoNDl5mO0G2NPD4c6LUK5mWdkw/640?wx_fmt=png&from=appmsg)

左边有三个类型，分别是传统的多阶段流水线系统、通用多模态大模型、专门为文档解析训练的视觉语言模型。

PaddleOCR-VL参数最小，效果最好，然后因为发的刚好早了三四天，所以表里没有DeepSeek-OCR的跑分，但是OmniDocBench v1.5的最新跑分昨天也出炉了，DeepSeek-OCR综合跑分是86.46，比PaddleOCR-VL的92.56还是低了大概6分，不过也能理解。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQos2YFlteSB1RmdibeHn4T4iaS1vWR2qcrZLwJAiaic64E3mW7Q0ddgSkqECQ/640?wx_fmt=png&from=appmsg)

PaddleOCR-VL确实足够的猛，在垂直模型领域，把性价比做到了极致。

你可能会有一点点好奇，为啥一个0.9B的模型，能比其他的大模型都要强。

除了确实专精这个领域之外，还有个非常有趣的架构，是我觉得单独可以说一下的。

也是长上下文和避免幻觉的一种非常有趣的解法。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQoscKzYAZ0cgCUIT7GYBUITlG6h5Xkfr9CHyuz0Xue1qEfhNm7Hf3WmLA/640?wx_fmt=png&from=appmsg)

很多的多模态大模型，是端到端的，他们干OCR的方式其实是非常低效的。

就是你把一整张A4纸扔给它，它需要一口气把这张图上所有的文字、表格、公式、图片、排版等等全都看懂，然后再一口气生成一个完美的Markdown，这个难度，其实也挺地狱级的。

毕竟模型需要同时理解：“哦，这块是个表，它在页面的左上角，这个表有3行5列，哦表头是这个，哦内容是那个，它旁边的这段文字是在解释这个表……哦哎卧槽我第一个事是要干啥来着。。。” 

PaddleOCR-VL的做法就挺高效好玩的，它的架构，就两步：

**第一步，先让专干布局分析的传统视觉模型上。**这个玩意叫PP-DocLayoutV2，它干的活儿特纯粹，就是“框”。

它以极快的速度扫一眼整张图，然后把一些区域都框起来，然后告诉你：“报告老板，这里是标题，那里是正文，这块是个表，那块是公式。” 而且每个框的阅读顺序，也都是符合人类的阅读顺序的。

这个活儿，在CV领域已经很成熟了，根本不需要一个大模型来搞。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosbKEU48uXpKMzd939YsjSyu4L1ARBfr0DKEsotgFd1CSN3JtOpY5ZNg/640?wx_fmt=png&from=appmsg)

**第二步，就是主力登场。**这个主力，就是最核心的这个0.9B的PaddleOCR-VL模型。

它现在接到的任务，根本不是去看那张复杂的A4纸。它接到的是一堆被PP-DocLayoutV2裁好的小图片。

一个任务是：“这是一张200x500的小图，我（PP-DocLayoutV2）已经告诉你这是个表了，你（PaddleOCR-VL）给我把它转成Markdown。” 

下一个任务是：“这是一张50x50的小图，我知道这是个公式，你给我转成LaTeX。”

然后循环往复，最后，又准又快。

所以这种做法，根本不需要复杂的几百B的大模型，直接上0.9B的模型，却能达到最完美的效果。

我之所以把这个点单独拿出来说，也是想表达我的一个观点：

在普通用户眼里，其实很多时候技术根本没有优劣，能解决用户的问题，就是最牛逼的技术。黑猫白猫，能抓到耗子的，就是好猫。

至少我认为，PaddleOCR-VL的做法，就非常的巧劲。

我也专门找了几类特别有代表性，处理起来比较头疼的图片来给大家看一下实测的效果。

首先肯定是扫描PDF，这种应该是重中之重，比如下面这张非常糊的扫描件截图，肉眼看起来也会有点吃力。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosb7zk81yf6zv8sA3iaOPUfDKSW1rvwcoicsWUqxydAVFbsNs3XHjPKZzQ/640?wx_fmt=png&from=appmsg)

糊不拉几的，我眼睛看着都疼。

而把这个扔给PaddleOCR-VL，它处理起来很顺利，先是把需要识别的地方框了出来，并打上了阅读循序的序号。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosDp6GtjIVqabgF602icyJSr71NE03sicfz5iaf90QzFm9c4QZbict99N2Gw/640?wx_fmt=png&from=appmsg)

然后是第二步，分块识别出结果，效果很不错，公式也识别出来了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosNt3G25jJ2eV70tsic7lLibo4xgD2lgeN44LlvYEc9WXcwxN9qIHBRWOQ/640?wx_fmt=png&from=appmsg)

我详细核对了2、3遍，发现确实一个字都没错。

最后的那个+号后面之所以没东西了，是因为我截图的时候，不小心让搜狗输入法的图标给挡住了。。。

我又找了一些手写笔记的照片去试，这玩意绝对是OCR领域的硬骨头。

不管是中文还是英文，只要字迹别太潦草到像天书一样，PaddleOCR-VL给出的识别结果准确率都还挺在线的。

对比很多工具碰到手写基本就歇菜的情况，这个已经很能打了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosH1bJ9XEicT5iaN6DHps9kN1P5ekPvGn3sY84jkexeg8VtYKmNOqEycbQ/640?wx_fmt=png&from=appmsg)

当然，前提是你的手写字得大致能看懂，如果是医生的那种字，我觉得神仙来了都没用。。。

然后是论文这种排版密集的。报纸那小字、多分栏、紧凑的布局，对布局分析和识别都是不小的挑战。

实测下来，PaddleOCR-VL对多栏的处理还比较稳定，阅读顺序也能捋顺，文字识别本身也没啥毛病，基本全对，总体效果挺好。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosdscdalB1Sc0Wg5tiaZxOibfGWQib8o8tknGkFfuWW6pnmbDaWNzSQAT6Q/640?wx_fmt=png&from=appmsg)

因为支持端到端的解析，所以能给你把一些图表啥的都给你还原回来。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosNa6svibWY4OzOfZ0JIIfcMsbDL7Rv4abVAQAUv1kFnvb4PjibtKkLIUw/640?wx_fmt=png&from=appmsg)

这个点非常的牛逼。

还有就是票据，像发票收据这些。格式虽然相对固定，但里面混着机打字、数字、手写补充、甚至盖章，挺复杂的。

PaddleOCR-VL在处理这类半结构化文档、抓取关键信息时表现还行，我自己跑了很多次，不能说百分百没差错，但在同类模型里，已经算非常靠谱的了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosSibkicAxAXiaFKUZmbSYqIxrZWr9DEAjPxTTHQ00kAlDO23rhwLztgneg/640?wx_fmt=png&from=appmsg)

感觉这个已经完全可以替换我们现在多维表格上用的视觉大模型，接入到我们公司财务的多维表格系统里面了。。。

准确性强很多，真的能节省财务的不少时间。

还有那种大型表格，这就是重头戏了。

不管是论文里那种带合并单元格的复杂表，还是财报里密密麻麻的数字表，甚至是没啥框线的表，PaddleOCR-VL的表格结构识别能力是有一点让我惊讶的，不光能认出格子里面的字，还能把表格的行列关系比较好地还原出来，这对我们的一些自动化信息提取非常有帮助。

比如就是上文里面的那个跑分图。

识别提取出来之后，没有一丁点问题，这个是有点离谱的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosh8l4z2HPvicc4MuevkOicLaLdo2gpZJdjcicRAc0xUGE27TpRV7NQSkRg/640?wx_fmt=png&from=appmsg)

总的来说，这些实测跑下来，PaddleOCR-VL在处理这些复杂和刁钻的场景时，表现确实可圈可点。

而且实测确实会比DeepSeek-OCR准确更高，DeepSeek-OCR提取的时候总是会错一两个字，PaddleOCR-VL是一字不错，当然你不能把DeepSeek-OCR纯看成是一个纯OCR模型，毕竟意义还是不太一样。

我们自己其实有很多飞书多维表格的信息提取工作流，也已经在考虑换成PaddleOCR-VL了。

比如我们经常需要，批量上传一些各个平台的数据截图，然后提取里面的一些结构化信息。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdxhtuavLyHy79vcxhVQosLQFB3YlSccNlX77VqDc0vibKhWIVBHw7cj9rIaPmud3odqNfoPw9nQQ/640?wx_fmt=png&from=appmsg)

现在都是接了一些比较大的多模态大模型来做提取的，有一说一，从价格上来说，会比PaddleOCR-VL这种贵很多，而且有时候还会出错。

感觉把PaddleOCR-VL接进去，会是目前的最优解。

目前PaddleOCR-VL已经开源，网址在此：  

https://github.com/PaddlePaddle/PaddleOCR

我本来想跟DeepSeek-OCR一样，给大家手搓一个Windows的本地整合包，让大家能开箱即用，结果因为不同于一些常规的大模型，折腾了一夜，干到凌晨4点多，两眼发黑，还是没做出来，这个只能说对不起大家，还是有点太菜了= =

所以现阶段，大家如果有自己部署能力的，可以自己根据PaddleOCR Github上的部署教程来部署到本地。

只是想用一下的，不想折腾部署的，可以去各大demo平台上用官方自己部署的体验版本。

飞桨：https://aistudio.baidu.com/application/detail/98365

魔搭：https://www.modelscope.cn/studios/PaddlePaddle/PaddleOCR-VL\_Online\_Demo

Hugging Face：https://huggingface.co/spaces/PaddlePaddle/PaddleOCR-VL\_Online\_Demo

最后，还是想多说几句。

DeepSeek-OCR探索的上下文光学压缩确实非常新，也打开了大家对人类视觉感知的一些新的想象。

百度的PaddleOCR-VL，更是从实际出发，在一个细分领域达到了SOTA，成为了这个领域效果最好的模型。

高效、准确，也能实实在在地提升我们处理文档信息的效率。

两者都是非常优秀的工作，没有谁比谁强。

都是在自己领域。

最亮眼的仔。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言