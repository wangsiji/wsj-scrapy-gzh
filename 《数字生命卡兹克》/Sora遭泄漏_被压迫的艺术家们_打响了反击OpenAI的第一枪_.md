     Sora遭泄漏，被压迫的艺术家们，打响了反击OpenAI的第一枪。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

Sora遭泄漏，被压迫的艺术家们，打响了反击OpenAI的第一枪。
=================================

原创 数字生命卡兹克 数字生命卡兹克 2024-11-27 09:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/q-3L9O7dxadr3xhsT9QpGw](https://mp.weixin.qq.com/s/q-3L9O7dxadr3xhsT9QpGw)

大半夜的，X上直接炸锅了。

Sora，这个牵动着无数人心弦的产品，被泄漏了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrEToO8z1BDxiad45JQ5ibmRKuBvkS0suXXKicY7863VjlK2rS5GeYcpia02NH466DOt3Rgd46osVbwgQ/640?wx_fmt=png&from=appmsg)

言简意赅的讲，就是有人把OpenAI给内测艺术家们的接口，直接打包到线上的huggingface上，给所有人用。  

网址在此（但是当我发出这篇文章的时候，已经不能用了）：  

https://huggingface.co/spaces/PR-Puppets/PR-Puppet-Sora

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrEToO8z1BDxiad45JQ5ibmRKKMLRlDWDLScs8fRdcqD0laVwGUFSYPpQW2MHsaK0vZ9R5ib2BiaiaKiapQ/640?wx_fmt=png&from=appmsg)

可以看到参数其实寥寥无几。

只有文生视频，尺寸不可选，默认16:9，分辨率有360P到1080P，时长是5～10s。

一些手快的人，也抢跑生存了一些样片。  

我给大家放一下。  

非常坦率的讲，跟2月16号给大家带来的震撼比，差太远了。  

我们已经不是2月没见过世面的小朋友们了，经受将近半年Runway、可灵、海螺、vidu、豆包、Pixverse、智谱的洗礼，我们已经长大了。

这个质量，挺好的，但是也就是挺好的了，调色很棒，很真实，动作幅度不错，稳定性不错，然后呢？  

没然后了。

X上也有大佬扒了代码，发现这个模型，应该是蒸馏过的Turbo模型。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrEToO8z1BDxiad45JQ5ibmRKIaYW1IiaUq3Ch0ic9XVebb25A7zxCXzhXJ1ltE5KwmCAIagm3ibxMiaPrQ/640?wx_fmt=png&from=appmsg)

真正的完全体模型，是什么样，不得而知。

大概在泄漏事件3小时后，OpenAI关闭了所有艺术家的API接口。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrEToO8z1BDxiad45JQ5ibmRKyiaJDCfTuV9TxG7ZsouYFDQeanpw9LqNqkIDic3UdxicLfaRlrFGb7ObQ/640?wx_fmt=png&from=appmsg)

直接一刀切，把所有人都关了。  

搞我是吧，都别用了。

Sora今年2月16号正式发布，距今已经整整9个月，可以测试上的人寥寥无几，仅限于做安全的红队和一些被邀请的艺术家们。

保密级别极高，放出来的能让大家看过的视频，肯定都是过过OpenAI的公关团队的，且放出来的艺术家创作的视频，也是通过OpenAI的官方渠道放出来。

这些艺术家们的数量，加起来，也不过300人，仅此而已。

而这次的泄漏事件，不是黑客、不是内部人员，正是这些艺术家们。  

他们在泄漏的页面上，讲了始末原委。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrEToO8z1BDxiad45JQ5ibmRK3xCLSk6quPvYqCPECAoybq0icKzvz0xzy0DHkSUaNfjYwPlh5RvUAhQ/640?wx_fmt=png&from=appmsg)

我用Claude翻译了一个中文版。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrEToO8z1BDxiad45JQ5ibmRKrqgv0hVpf8NpjD2Pr5Xgkmctw6gF4YnaK4vrUdc8LicjNN1ozjBfVCQ/640?wx_fmt=png&from=appmsg)

划重点：  

**“艺术家不是你们的免费研发人员，我们不是你们的：免费漏洞测试员、公关傀儡、训练数据、验证工具 ”  
**

**“每个作品在分享前都需要经过OpenAI团队的审批。这个早期访问计划似乎与其说是关于创意表达和评论，不如说是关于公关和广告。”  
**

**“我们向世界分享这一切，希望OpenAI能变得更加开放、更加友好对待艺术家，并超越公关噱头来真正支持艺术发展。”**  

这个过程，就是典型的偏见。

是某些科技巨头，对于艺术创作的偏见。

当我把Sora的权限开放给你，帮我测试、给我提修改意见、同时对外一切发声都要受我管控，未经许可不许对外发声，这其实是一种傲慢。  

他们实际在暗示一个点：  

**新产品新技术的访问权本身就具有足够的价值，足以抵消创作者付出的所有时间、精力和专业技能。**

也就是说，在他们的概念里，技术创新的价值凌驾于艺术创作的价值之上。

这就像是一个画笔制造商告诉达芬奇，"使用我们最新研发的画笔是一种荣幸，所以你帮我们测试产品、给建议，是应该的。"

当他们用"机会"来包装无偿劳动时，他们实际上是在否定这些专业投入的价值。

这种做法暴露了一个不平等的权力关系。

就是掌握技术的一方认为自己处于施予者的位置，而忽视了创作者同样带来的价值。

AI视频的创作和测试，说白了，是需要很多专业背景的，更别提Sora的那些艺术家，哪个不是声名赫赫有头有脸的人？

所以，他们在将近9个月以后，爆发了。  

不过他们很聪明，没有用传统的方式反抗，而是用这种开源的技术方式，去做一些无声的抗争。  

在19世纪工业革命时期，织工们曾经群起反抗自动织布机，那场著名的卢德运动中，工人们砸碎机器，不是因为害怕技术进步，而是在抗议工业化过程中对人的尊严的漠视。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURrEToO8z1BDxiad45JQ5ibmRK9SrDGr8m1xjia44VsP7LVOLd4H5DhQcAOoJ5YtxPhM5W1UkWxdw9k8w/640?wx_fmt=jpeg&from=appmsg)

这次的Sora泄漏事件，我觉得非常好的展示了，科技行业在处理创新与创作关系时的偏差。

国内其实也有过类似的事件，我就不说哪家公司了，当时在AI创作者圈中闹的沸沸扬扬。

大概就是这家公司有个新模型快要上线了，希望召集一波人来内测使用。而这个模型之前，其实已经跟国内很多的头部AI创作者有了链接，也合作过不少。  

正常来说，你模型要上线了，这些创作者们为爱发电，提前用上，做一做自己的作品，去公域上发发，再给你一些反馈和优化建议，这个模式至少在现在这种环境下，大家还是能接受的。  

但是那次变了。  

突然这个新模型的体验资格，变成了搞了一个比赛，这些老的合作的创作者们，想要获得这个新模型的体验资格，也要去参加那个比赛，用老模型来创作作品。只有在这个比赛中获胜的前几名，才能拿到这个体验资格。

最关键的是，**比赛比的不是质量，而是投稿数量。**  

这一下子就炸锅了。

我自认为在AI媒体和AI创作领域，都还算有一点小影响力的人，之前也合作过很久，在明确测试效果不好的话我会不写，也不会写写黑稿，稿子也必定会跟对方过PR的情况下，被告知，也必须要参加比赛，拿到名次才能有体验资格。

当时也是非常的恼火，然后很多朋友也都遇到了这样的答复，甚至有的没忍住，在朋友圈里疯狂开喷，死命的输出。  

当然，这家模型公司第二天，也算是反应过来了，把这事很好很快的解决了，最后的结果大家都比较满意，后续也能继续长久的合作。

但是同时，这也暴露的一个本质是跟OpenAI这波是一样的：

**“掌握技术的一方认为自己处于施予者的位置。”**

当然，这种现象，有很多的背景，我不想去聊那种东西，很多东西是悬而未决的。  

我只想说：  

1.  _艺术家，不仅是工具的使用者，更是创新过程中的重要贡献者。_
    
2.  _专业创作者的反馈和创作本身就具有重要的商业价值。_
    
3.  _创意劳动应该得到与其价值相匹配的实质性报酬。_
    
4.  _技术与艺术是相互促进的关系，而不是单向的恩赐。_
    

这可能，就是科技与人文的路口，另一种具像化的交叉吧。

我也挺想看到OpenAI，会如何处理这次事件。  

最后的最后，他们关于开源的呼吁，我觉得非常的棒，我自己也是双手双脚，支持一切开源，他们都是伟大的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrEToO8z1BDxiad45JQ5ibmRKD5bvz8dUZQbbm16HRQeOCpvSETdyNpWib5oHYEToDUmYlHaUiaOB80tQ/640?wx_fmt=png&from=appmsg)

而这个里面，出现了一个熟悉的面孔。

CogVideoX。  

有没有感觉，很熟悉？这就是智谱清影的基座模型。  

智谱这波，恐成最大赢家。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言