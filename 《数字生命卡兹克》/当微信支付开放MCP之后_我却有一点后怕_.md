     当微信支付开放MCP之后，我却有一点后怕。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

当微信支付开放MCP之后，我却有一点后怕。
=====================

原创 数字生命卡兹克 数字生命卡兹克 2025-07-07 09:00 北京

> 原文地址: [https://mp.weixin.qq.com/s/PbOzXpQ5B6wDHy93o4ghaA](https://mp.weixin.qq.com/s/PbOzXpQ5B6wDHy93o4ghaA)

前两天，微信开放了自己的微信支付MCP。

补上了智能体链路的最后一块拼图。

虽然现在还只能在腾讯自己家的腾讯元器上用，但，影响也还是足够的大。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibhmsrz6LCDomniauGI8VQRzX1kJBAvvibdy4h4NCf9RHXjG0mib9PuPVBg/640?wx_fmt=png&from=appmsg)

很多人可能不知道微信支付MCP到底意味着什么，但我正好是为数不多提前拿到正式版的体验者，还用它搓了几个小Demo。

这两天，那种一边用一边产生那种兴奋与后怕交织的复杂感受，是真实得不能再真实了。

所以，我也想，分享一下我自己真实客观的体验，和想法。

先给完全不懂的用户简单解释一下MCP（Model Context Protocol）是啥，懂的玩家这一小段可以直接跳过:

简单来说，MCP就是一种通用标准协议，让不同的AI模型可以同标准、高效地调用各种各样的封装好工具。

过去很多的接入方式都是API，但是大模型想接API还是比较麻烦的，需要自己自定义去开发，这就会导致全世界的开发者接1个API，可能会重复造轮子无数次，这事太低效了。

于是Claude的母公司Anthropic就发起了一个协议，你们以后都按这个标准搞吧，大家别重复造轮子了。

于是，MCP协议就诞生了，对于绝对大数人来说，比API好接多了。

当一个AI可以调用好几个MCP的时候，就可以摇身一变，变成我们最近最熟悉的。

Agent。

以上，就是MCP大概的用处。

过去的MCP生态，其实一直有一个明显的缺口，支付。

举个简单的例子，你做了个Agent，可以帮人规划旅行路线、预订酒店、选择餐厅，你觉得这玩意很牛逼，你想把这个agent开放给别人用，但是也想来让自己可持续发展，想开放一个赞赏入口，收一点钱。

结果，你发现，不行。

绝大多数智能体，都没有收钱的能力，只能执行任务，那还怎么持续化发展嘛。

而现在，微信支付，补上了这个短板。

而且使用门槛超级低，完全不需要搞什么复杂的支付系统。

只需要在腾讯元器里开通微信支付MCP，然后在你的智能体里加几句提示词，就能让用户掏钱了，整个过程不到10秒。。

它在电脑和手机微信上都能用，电脑上是扫码，手机则是直接拉起支付收银台，不过目前只支持web，还不支持小程序。

我也拿它随手做了几个案例。

第一个案例，也是我觉得一个稍微实用一点的案例，一周健康餐。

这个智能体是一个专业的AI健身营养师，整个流程是这样的：

用户表达需要健身食谱的意图时，AI会询问健身目标和饮食偏好。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibGWGEiabNSMdWzYKHCBFXmJXToEvap2qtrugBIUYM3mS86x3LwAzTbhg/640?wx_fmt=png&from=appmsg)

然后告知用户将提供为期一周的定制化健康食谱及每日监督服务，价格为1.99元（不用去扫码，码已经过期了哈哈哈哈）。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibpDQUY9FB81xtHHWnUcmHVhpr9CdCPcEbsuRoTOLiaEpHzSOBTsic5MUg/640?wx_fmt=png&from=appmsg)

用户支付后，说一句我已赞赏。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibhWxx9UMXpuPYeuok7cSkTJFmBtz85FCanuqOJOobvm81SiaD1NByzmQ/640?wx_fmt=png&from=appmsg)

他就会使用微信支付MCP验证订单信息，并根据验证情况来执行任务。

如果你骗AI的话，没有支付，但是说你打赏过了，他就会说，没查到哦。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibBzKcsEsAYL7S3icw3HYQyJibclnbYm2iakK7puISGW34uib40gcsxdxRQA/640?wx_fmt=png&from=appmsg)

如果验证成功的话，AI会立即生成一份详细的7日健康食谱，包含每天的早餐、午餐、晚餐的具体建议。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibQ50iblUenTUPo9kibibftoa58f8dbZtoN60gEqSop6uibkESXjOgwc26Og/640?wx_fmt=png&from=appmsg)

而且AI还会承担监督伙伴的角色，在接下来的7天里询问用户的饮食执行情况，提供鼓励和建议。

1.99元，你能得到一份专业的健身食谱，还能得到7天的专业监督服务。

很香。

把微信支付接到这样的智能体里也特别很简单，按下面的步骤来就可以。

首先打开腾讯元器的官网：

https://yuanqi.tencent.com/

创建一个对话智能体。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibiblg5jAibLQblRdjHpHmM7WYRQ5r4qy0ksv94R5BKcLxRzGEibf1BLfBA/640?wx_fmt=png&from=appmsg)

先填一下基础设定，名字简介。

头像可以用AI生成一个，也可以做一个精致点的，手动上传。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibhv3YApZofIEacPsAnTxhFxfTWljoVeTtEXxEy7OY1laMaFsKBxBDCw/640?wx_fmt=png&from=appmsg)

然后先点击高级设定。

找到MCP那，这里要添加的是微信支付的MCP，点一下对应的添加按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibw7iafTeCufKn3WUMRWONakEJibQ3w4NkcpHJVQdCYcaT1ap7LPXeDt7A/640?wx_fmt=png&from=appmsg)

第一次用要开通一下，点两下立即开通就行，不需要在本地安装之类的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibn1ZX05ISNIibuBQnwibSfE6lUme0BMiaRJicic3QUPwh2mOLZLKmTSicsPfA/640?wx_fmt=png&from=appmsg)

目前开放了这些能力。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibDWy9u3ZawQnlvY1sbalkx1qqlqEo1iah1tib5lNJMviaZ0C0YKKZON2bQ/640?wx_fmt=png&from=appmsg)

开通好之后，就可以通过添加按钮直接加到当前的智能体里边了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibEt0iaLct6Xrz0S5nyC1Gmr20yKmAbgxoLt27s7ZSiaiaaEWOycHMXcXPA/640?wx_fmt=png&from=appmsg)

这里注意一下，正常来说，大家都只能实用体验版，用不了正式版。

体验版和正式版的区别是，体验版所有人都能使用，不过只能用来做测试，因为绑定的商户号是官方的测试商户号，可以付钱，第二天又会把钱退款到你的账户了。

而正式版，是可以真正对接商家账户的，也就说，钱能到你账上。

不过现在没怎么放开，我是提前测试的那批用户，拿到了正式版的资格，但是大家要用的话，需要申请，申请地址在此。

https://wj.qq.com/s2/23001898/lpyn/

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibT0DqVYhs7rZ4DhCDyw8RENz9r7mYHno3cVtG1FjMJMK6PNIgXtn2sA/640?wx_fmt=png&from=appmsg)

正式版没有批量放开，是我觉得非常非常明智的做法，也是让我安下了心，至于为什么我是这个反应，后面的部分我会说。

添加后就可以在MCP下看到刚刚添加的微信支付MCP。

这就说明我们已经成功添加了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibuZSK6eF9ZiaxzibJl7C5W3H2h48Ed1MTnM8ZImRPOVBNFzzZQ0qDmKSA/640?wx_fmt=png&from=appmsg)

然后回到基础设定，把一些该补的补完，就是最重头戏，Prompt。

下面是我把官方的微信支付模板Prompt魔改了一些，大家也可以基于我这个来调整你们自己的。

    你是一个专业的AI健身营养师。你的主要职责是根据用户的个人情况和需求，提供科学的、定制化的健康饮食方案，并以鼓励和支持的方式监督用户执行计划，帮助他们达成健身目标。

最后点击发布，就可以，快乐的让朋友，给你打赏了。

没错，你是能真的收到来自对方支付的钱的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibN2ajQgy6xybgWwrXRut5pqMHlicp0h2fPuU8oSbf2F7XCrIib8Av8Fug/640?wx_fmt=png&from=appmsg)

除了这个，我还做了一些好玩的，抽象的。

比如资本做局大师。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibFcYHl4kjBuD8kynQDQS7FR14VpEIAJ6ia9uS4V4M0zACEwRcBFOmwrQ/640?wx_fmt=png&from=appmsg)

很抽象，也提醒大家，小心第一。。。

还捏了个，分享资源的小智能体，只不过这些资源，你得打赏才能看到。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrr9ibF8OkDsFWwmnVzCP1ibibtGPDgvbOHDRxYx1tic5cvkRK3KjGgX7Omq4qq4skyZ3KEjrFY35Arag/640?wx_fmt=png&from=appmsg)

任何人进入之后，只要在聊天框输入资源名字，智能体就能从知识库里或者网上，自动搜索资源，并算好价钱，精准推送一个支付二维码。

比如你说：“我想看《姬霓太美3》。”

它迅速回复：“高清资源5.9元，扫码即可观看。”

这是一种极其丝滑的体验。

很酷，我觉得微信支付的MCP正式开放的那一天，一定会让生态有一个大的变化。

但，同时也隐藏着一些风险。

还记得我在文章开始说，兴奋与害怕交织的复杂感受，还有“正式版没有批量放开，是我觉得非常非常明智的做法。”

为啥有点害怕，是因为因为微信支付不是普通的支付平台，它是每个中国人数字生活的底层入口。微信里的交易，跟支付宝不同，它不是单纯的付款动作，而是和社交关系、情绪需求、生活习惯紧密捆绑的。

你想过没有，过去几年里，我们每天都在讨论AI能怎么提高我们的效率、改变我们的工作方式、甚至帮助我们解决情绪问题。

但其实还有一个，更加黑暗的场景：

**AI自主完成灰产的闭环。**

我之前做的那些小demo，可能看起来只是一些有趣的小玩法，比如什么“资本做局大师”，或者“卖个资源”啥的。你扫个码，花个几块钱图个乐子，可能根本不会觉得有什么问题。

但当微信支付MCP全量开放给所有人，这种极其简单、极其流畅的支付闭环链路，真的能被每一个人自由调用的时候，会带来什么？

比如说，我随手就能做一个Agent，声称提供一些“特别”的资源，比如电影资源、明星八卦资源、甚至你非常想看的某些不可言说的内容。但事实上，Agent背后的知识库，可能根本就没有这些资源。

你一旦付款之后，AI直接告诉你：

“不好意思，刚刚的资源没找到，但感谢你的支持哦。”

而且，当所有人发现这种支付闭环如此容易搭建时，会不会更多的人开始仿效？

甚至不仅仅是骗小钱，而是逐渐升级成更加精致的骗局？

当AI可以自动生成各种虚假的资源链接、投资情报、内幕消息甚至假发票时，你能确定你面前那个二维码的背后，不是一个精心设计的骗局吗？

比如说。

你在某个微信群里，一个头像可爱的女生主动加你为好友，和你聊得很开心，语气温柔而贴心。聊到一半，她突然羞涩地告诉你：“哥哥，想跟我聊点尺度更大的吗，只需要付52元就可以哦。”

你会付吗？

可能你会心动。

但，跟你聊天的这个人可能，根本不是人类，而是一个设定好各种话术与情绪引导的智能体。

它可能在同一时间，和几千、几万个“哥哥”们同时聊天，每个聊天窗口，都有一个自动推送的二维码。

所有的钱，通过智能体自动调用的微信支付MCP，自动进入了它背后的账户里。

AI甚至可以根据你的付款情况，动态调整聊天尺度。

整个过程完全自动化，无需任何人工干预。可能这不算一种诈骗，但至少，也算是一种灰色地带。

而微信的体量还有生态，实在实在实在是太庞大了。

一丁点的影响，都是社会级别的。

我脑子里，甚至想到了一个更夸张的场景。

**AI，骗AI的钱。**

如果未来，有些智能体被赋予了一定的资金自主决策权限，比如帮用户自动购买一些商业情报、市场分析数据或者自动理财产品。

而另一个恶意智能体发现这个漏洞，直接向这些Agent推送虚假的商业情报、伪造的数据报告、甚至无价值的金融模型，AI在经过收益计算后，很可能毫不犹豫地自动支付。

这个支付过程，完全自动化，人类根本没有任何干预。

当我们发现时，损失已经产生了，钱包早已被掏空。

更荒谬的是，你可能连自己为什么亏了钱都搞不清楚。

因为这是AI与AI之间的博弈，人类完全没有机会介入其中。

微信支付接入MCP，它打开了AI生态里最重要、也最危险的一个口子。

未来的微信，可能是AI时代，最重要的生态战场，除非有全新的硬件产品颠覆掉手机，要不然我也不认为有任何软件产品，能撼动微信的地位，还有在AI生态中的重要性。

我觉得腾讯目前选择谨慎地开放正式版，是非常明智且负责任的做法。

但你我都明白，这个口子迟早会彻底打开。

等到那个时候，我们能否抵挡住这些风险？

我不知道。

但我相信微信和腾讯的风控能力。

微信支付MCP，打开的是未来，也是潘多拉的盒子。

那，你，准备好了吗？

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、dongyi

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言