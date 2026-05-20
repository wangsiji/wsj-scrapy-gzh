     花7000块实测Claude2.1 - 200K Token的超大杯效果究竟怎么样？ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

花7000块实测Claude2.1 - 200K Token的超大杯效果究竟怎么样？
==========================================

原创 数字生命卡兹克 数字生命卡兹克 2023-11-23 21:05 天津

> 原文地址: [https://mp.weixin.qq.com/s/RrvYPfchyemuD\_SDLiHEng](https://mp.weixin.qq.com/s/RrvYPfchyemuD_SDLiHEng)

昨天Claude2.1正式发布了，更新了一系列的新能力，不过只对API用户开放。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURricMgzcl9V8BnIROd3wBKrMQ4TGfkWQTpFzFrOTNaAbr24LosmyGJfwJOCcBY4vDaMFuShe9RPdJQ/640?wx_fmt=png&from=appmsg)

大概总结一下，200K Tokens的上下文窗口、模型幻觉率的显着降低、系统提示以及他们的新测试功能：工具使用。

其他的没啥可说的，**重点聊聊这个200K Tokens的上下文**。

记得几个月之前，Claude率先推出100K Token，引起了不小的风波，毕竟在那个上下文都还只有4K Tokens的年代，100K Token可是扎扎实实的降维打击。  

而这次，Claude2.1号称全球第一，扔出了2倍容量的200K Token。大家可能对Token没啥概念。我换种描述来说。

200K Token等于470页的PDF材料。  

按Claude自己的话说，你可以扔你整个代码库和技术文档、扔一整个财务报表，甚至把《奥德赛》或者《伊利亚特》扔进去。

这下是不是就大概有点数了？以前4K的小窗口，扔个几页PDF都费劲，现在，随便扔。

但是支持这么大的容量以后，使用起来到底怎么样？你不能光加容量，但是质量不加吧，就好比你喝瑞幸，以前是个普通中杯，给你放了半杯的冰，现在他说升级了，给你来了一口缸，但是缸里依然还特么的全是冰，咖啡就那么几口，那这升级有蛋用，对吧。  

Token也是一样的道理，你说是升级了200K，但你实际到50K就全都忘干净了，那你100K和200K有啥区别？  

所以X上一个大佬Greg Kamradt，为了弄明白Claude2.1的200K Token，究竟实测效果怎么样，就调用Claude 的API做了个压力测试。

**他做个压力测试，花了1016 美金。。。。**

你没看错，1016美金，折合人民币一共7255元。。。

只能说，太特么壕了，壕特么上天了。。。  

直接放他的测试结果图，为了大家阅读体验良好，我给做成中文版的了（图片可能在公众号上有压缩看不清，看完文章后可以对着我公众号私信"**测试图**"，我自动发你高清的原图）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURricMgzcl9V8BnIROd3wBKrMw22PIsxTF9oCg9dFT8YSHfHuct8oWMNKyNky4mNtwwibeayNibplMWOA/640?wx_fmt=jpeg&from=appmsg)

这个测试Greg Kamradt将其命名为"大海捞针"压力测试。

测试的目的是评估Claude从大量文本中检索信息的能力，特别是当信息被放置在文档的不同位置时的准确率。

横轴表示上下文长度（以Token表示），纵轴表示文档深度的百分比，这表示事实被放置在文档的位置。

横轴应该比较好理解，就是给的信息总量Tokens数，从1K到200K不等。  

纵轴我稍微解释一下，"文档深度百分比"实际上是表示要信息（事实）被放置在整个文档中的位置，就是你要从大海里捞的那根针所处的位置。

你可以想象一篇文章，它从头到尾都有文字。如果我们把这篇文章比作一堆纸叠在一起，那么“文档深度”的百分比就像是你从最顶部的纸张向下数，直到你找到那条信息所在的地方。

如果信息在文档的最开始部分，那么它的文档深度接近0%。

如果信息在文档的正中间，那么它的文档深度接近50%。

如果信息在文档的最末尾，那么它的文档深度接近100%。

如果一篇文章有100行，一个重要的事实被放在了第50行，我们可以说这个事实的文档深度是50%。如果这个事实在第25行，那么深度是25%；如果在第75行，深度就是75%。这个百分比告诉我们事实在文章中的位置，而不管文章有多长。

大概就是这个意思。

可以看到，**整个测试，Claude红了半边天，一半都检索失败，根本找不到。**

甚至可以看到文档到了200K的时候，除非你把那根"针"放在最顶部或者最底部，也就是文档深度0%的位置，才能成功。  

甚至你放在1%的文档深度的位置都能失败，简直就离谱。

**发现：**  

*   在20万个令牌（近470页）的文档深度下，Claude 2.1能够回忆起某些事实
    
*   位于文档最顶部和最底部的事实被几乎100%准确地回忆起来
    
*   位于文档顶部的事实的回忆表现不如底部（与GPT-4类似）
    
*   从大约90K个令牌开始，文档底部的回忆表现开始逐渐变差
    
*   在较低的上下文长度下，并不保证有良好的表现
    

**结论以及如何做：**

*   提示工程很重要。值得对您的提示进行调整，并进行A/B测试以测量检索的准确性
    
*   不能保证您的事实一定会被检索到。
    
*   更少的上下文 = 更高的准确性 - 这是众所周知的，但是如果可能的话，减少您发送给模型的上下文量可以增加它的回忆能力
    
*   位置很重要。但是放在文档最开始和文档深度50%到100%区间的事实似乎能被更好地回忆起来。
    
*   提示工程很重要 - 值得对您的提示进行调整，并进行A/B测试以测量检索的准确性
    

可以看到，Claude2.1的这个200K表现并不尽人意，更不能对它抱有过高的信任。总量达100K之后，检索成功率甚至只有50%不到。  

前几天GPT4也发布了128K的版本，虽然它比Claude2.1少了近一半，但依然是个容量极大的超大杯了。

我们再看看Greg Kamradt之前做的GPT4 128K的评测，来跟Claude2.1做一个横向的对比。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURricMgzcl9V8BnIROd3wBKrMs4CzBuj6n8nLyAPUNI6B73prUHLD1hjbu8g2RVMEs1II4ic9vlZ9adw/640?wx_fmt=jpeg&from=appmsg)

绿油油一片。  

**整个检索成功率几乎都保持着成功，只有到了73K以后，在7%~50%的文档深度之间，成功率才有所降低。**

可以从这个压力测试看出来，GPT4保持着遥遥领先的姿态，甩了Claude一大截。

Token这个东西，容量越大当然越好，但是相应的，质量你得跟上吧。

光大容量，结果掀开一看，全是冰块，那还玩个屁。  

OpenAI的一出闹剧，依然改变不了GPT4在AI行业的王者地位。  

希望后来者，能真正的给OpenAI一些压力。  

想要高清图的，可以对着我公众号私信"**测试图**"，就自动发你了。

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言