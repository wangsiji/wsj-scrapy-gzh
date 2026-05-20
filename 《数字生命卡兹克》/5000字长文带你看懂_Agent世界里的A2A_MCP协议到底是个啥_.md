     5000字长文带你看懂，Agent世界里的A2A、MCP协议到底是个啥。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

5000字长文带你看懂，Agent世界里的A2A、MCP协议到底是个啥。
====================================

原创 数字生命卡兹克 数字生命卡兹克 2025-04-10 09:48 北京

> 原文地址: [https://mp.weixin.qq.com/s/WpRUWUpPy0j\_BOqAIyP55A](https://mp.weixin.qq.com/s/WpRUWUpPy0j_BOqAIyP55A)

昨天晚上，Google发了一个关于Agent的新开放协议。

叫Agent2Agent，简称A2A。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqz2yFdOUdVkXpiaxCuxbkw693sBdF0k2ZTpM7maabI6CTtBjnYmXwqm7ZVnGynhsGkSoVic0I6BMzg/640?wx_fmt=png&from=appmsg)

包括昨天阿里云百炼也官宣搞MCP了。

这些本来没打算写的，因为太技术了，也是感觉离普通人还是有很大距离。

但是有好几个朋友都在群里说。。。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqz2yFdOUdVkXpiaxCuxbkw6fTNETEWIHzfTTAw1ARHWHm6NdQ1su4ry4exL0jsutiaJbFzFUElAoTQ/640?wx_fmt=png&from=appmsg)

那还是来聊聊吧，正好也用我自己的理解，来做个小科普，让大家一片文章看懂，A2A、MCP，到底是个啥。

正好最近特朗普对等关税这事，非常火。

搞得全世界鸡犬不宁，每个国家之间的隔阂，好像又重新出现了。

我就用国与国之间的外交，来去解释这两个协议。不要以为八竿子打不着，其实真的非常的像。

我们现在，假设每个AI智能体（Agent）就是一个小国家，它们各自有自己的语言和规矩。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURprDdUC0CiaGRCb4eoKhiaSVTEvW3J2zicpBCAHbtBh4tfmuOUPh0JE2PXlxICAb6gwx43w9y8G2K4aw/640?wx_fmt=png&from=appmsg)

现在，这些国家的大使馆分布在同一栋大楼里，试图互相沟通、做生意、交换情报。

理想情况是，各国之间关系和睦，大家都有一套明晰的外交规则，只要大家坐在圆桌前，就能顺畅地交流、签署协议、并合作进行国际项目。

但现实却是，每个国家的大使馆互不统属，协议各异，有的只认英制度量衡，有的只收欧元货币，有的说谈判必须用法语，有的则坚持任何通信都要用自家加密算法……

结果，你想跟A国谈一个简单的贸易合作，得先备齐对方要求的一大堆条文、证明、翻译、特殊密钥。如果你还想同时跟B国、C国合作，那就得重复N遍相似的流程。

这种临时的、分散的、多头的各国各自为政，让所有人的沟通成本居高不下，每次对话都要额外缴一份信息关税。

过去，AI世界里的Agent想要合作，都面临一样的窘境。

举个例子，你可能有一个自动帮你帮你回邮件的Agent，还有一个内置在日历应用里的Agent，能帮你安排日程。

但这两个AI很难直接对话，必须得你充当翻译在中间手动复制粘贴信息，或者依赖开发者定制的接口。贼恶心。

  

结果就是，AI智能体各据山头，**互操作性**极差，这种碎片化现状让很多用户头疼，因为需要在多个AI应用间来回切换，也限制了AI的潜力发挥，很多本可以多Agent协同完成的复杂任务，被人为隔断在各自的小圈子里。

这种局面下，就有点像二战后世界的状态：每个AI智能体各自为政，缺乏统一规则，互通有壁垒。

当年二战后，也就是1940年代，美国寻求建立一套战后多边机构，其中之一将致力于重建世界贸易，搞了很多轮的谈判。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqz2yFdOUdVkXpiaxCuxbkw6o5FiajPBIQmLtLN2icGAbAaf0MWmBB81BrMM83sXiby4wSN5Pibkuv9lUA/640?wx_fmt=png&from=appmsg)

最后，历经50年，终于1995 年1月1日正式开始运作，依据 1994年马拉喀什协议 ，取代了1948 年建立的关税与贸易总协定。

我们有了人类历史上也是非常伟大的组织：

WTO，世界贸易组织。

而现在AI世界的生态，就有点像二战后的废墟，WTO成立的前夕，你调用我的功能要按我的接口来，我访问你的数据也得敲你定的门路。

没有标准，意味着每增加一种合作关系，都要付出额外“关税”（开发成本和沟通成本）。

AI生态因此变得割裂且低效。

人人设墙，自扫门前雪。

但是还好，在AI圈里也出现了想要**制定通用规则**的势力，就想大家在贸易混战中渴望一个WTO那样。****

****AI行业开始探讨能否有一套大家都认可的协议，让智能体之间、智能体与工具之间**互相对接更加顺畅。**

**这时候，Google和Anthropic分别站了出来，各自抛出了一个方案，也就是我们今天的主角：****A2A**协议和**MCP**协议。

  

一. A2A协议

先来看Google发布的 **A2A协议**。

A2A（Agent-to-Agent）协议，顾名思义，就是让AI代理彼此直接对话、协同工作的协议。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURprDdUC0CiaGRCb4eoKhiaSVTWQLQ2XqAhQxM8o3XAFu8OW7lk0nFlf4eoicOKBTVcmab3bLRqhdnjJg/640?wx_fmt=jpeg&from=appmsg)

这次Google得到了包括Salesforce、SAP、ServiceNow、MongoDB等在内的50多家科技公司的支持参与。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURprDdUC0CiaGRCb4eoKhiaSVTOjBI4rOCRhm6rfppg6icBju8MbR27hzzcQfGdVpibjnGhjoEXZxn8XQA/640?wx_fmt=png&from=appmsg)

A2A协议的设计初衷很简单：

让**不同来源、不同厂商**的Agent能够互相理解、协作。就像WTO旨在消减各国间的关税壁垒一样。

一旦采用A2A，不同供应商和框架的Agent就像一个个的小国家，加入了一个自由贸易区，能够用共同语言交流、无缝协作，联手完成单个Agent难以独立完成的复杂工作流程。

至于A2A是如何运作的，我尽量用现实类比来通俗易懂的解释下：

**1\. Agent = 国家外交官**

**每个Agent其实就像一个国家大使馆的外交官。他的名牌上写着自己能干啥、隶属于哪家企业，联络方式如何等。A2A要做的，就是制定一个****统一的外交礼仪和沟通流程**。

过去，A国外交官只会说法语，B国外交官只用西里尔字母写文件，C国外交官要求面谈时必须使用古老的云纹金箔信件。。。而A2A的出现，就是让大家在同一个会议室开会时，都能说一套约定好的通用语言，用相同格式提交文件，让商议好的结果可以被各方理解并执行。

2\. Agent Card（代理卡） = 外交国书 / 大使名片

在A2A规范中，每个Agent都要公开一份“Agent Card”，相当于其外交官的身份名片。

包含以下内容：Agent名称、版本、能力描述、支持什么“语言或格式”等等。

现实中，外交官的身份名片让对方知道他是谁，代表哪个国家，有哪些职权。同理，在A2A里，Agent Card列举了“我（这个Agent）能执行哪些技能”、“我的认证方式是什么”、“输入输出格式有哪些”等等。

这样，其他外交官想跟你合作就能很快找到你、理解你的能力，省去了大量沟通障碍。

**3\. Task（任务）= 双边或多边外交项目**

**A2A中最核心的概念之一是****Task。**  

当一个Agent想委托另一个Agent去完成什么事情，就像对外发布一份“合作项目意向书”。对方同意接单后，双方会记录一个Task ID，追踪项目进度、交换资料、直到该Task完成为止。

现实外交中，某国家就可能向某兔提议：“我们想合作修一条跨境高铁，麻烦你们派工程队来。” 

这就对应A2A的Task：由发起方提出需求（TaskSend），远程Agent表示接受（Task状态变更），然后双方在整个项目过程中随时更新任务进度

里面还有个Artifacts（成果物），就相当于这个项目最后落地的“合同文本、建设成果”。在AI里可能是生成的一份报告、一张图片或任意形式的输出。而在A2A语言里，用 Artifact 表示最终生成的成果。

Message（消息），则是项目前期或中期的各种来回沟通。它可能包含对任务细节的补充说明、要对方再确认某些条件等。这与现实外交中的电报、照会、使节往来是一模一样的。

**4\. Push Notifications（推送通知）= 外交使馆快报**

**在A2A里，如果一个Task是长期项目，远程Agent需要花很久时间才能完成，比如DeepResearch动辄十几分钟，某些复杂的Agent动辄一小时，它就可以通过****推送通知**机制向发起方更新进度。

就像在外交中，如果一个跨国基建项目周期很长，甲国会定期给乙国发通报：“进度到哪儿了？有什么问题需要协调？”

这样能大幅提升**异步协作**的能力。过去很多AI系统比较原始，只能用同步的“请求-响应”模式，就像放一个人在那24小时监控，一旦响应超时就中断。

A2A允许设置回调接口、服务器端事件（SSE）等方式，把漫长的任务分段汇报，让沟通保持流畅。

**5\. 身份认证与安全= 外交特权与协议**

**A2A采用企业级的认证策略，要求通信双方先验证对方的身份凭证。例如在现实外交中，不是谁都能随意闯进某国大使馆，必须持有相应的外交护照、获得许可。**

**这就是为了防范“冒名顶替”或“恶意窃听”。**

**在A2A里，“认证头信息”“token”“签名”等一系列安全手段，就相当于外交通行证或盖了公章的外事批准文书，确保你跟我谈判时是真的代表“你所在的国家”，而不是一个假冒的第三方。**

**这大概，就是A2A的机制，其实你看，跟国与国的外交，或者跟企业与企业之间的协同，没有任何本质的区别。**

  

二. MCP协议

再来看**MCP协议**，全称**Model Context Protocol**。

这就是Claude的母公司Anthropic在2024年11月推出并开源的一套标准。

A2A解决了AI外交官之间的交流流程问题，但是还有一个棘手的现实，再能言善辩的外交官或者企业商务，要是没有任何可靠的信息**来源**，对国际局势和资源配置就两眼一抹黑，根本就没法干活。

更何况，在现代社会，外交官往往需要调用种种外部工具，比如签证系统、国际结算系统、情报数据库等等，才能完成任务。

同理，一个Agent若想承担真正的复杂职责，也需要能连上各种数据库、文档系统、企业应用，甚至是硬件设备。

这就像给外交官建立完备的情报局，并授权他们使用某些工具处理事物。

过去，Agent要接入外部资源，常常得各自开发专用插件，与不同工具做深度整合，劳心劳力。

但是，我们现在有MCP了。

**MCP致力于标准化大型语言模型（LLM）与外部数据源、工具之间的交互方式**。Anthropic的官方比喻很形象：**MCP就像AI应用程序的USB-C端口**。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURprDdUC0CiaGRCb4eoKhiaSVTDkIduoEyEiciaOdFPykYry6B5cIZeqy7u3mpTAMPdGOgzXEOZZhelcKQ/640?wx_fmt=png&from=appmsg)

USB-C是如今设备通用的接口，不管充电、传数据都是一个口搞定。

MCP的野心也是这样的，**搞一个AI领域的万能接口**，让各种模型和外部系统接驳都用同一个协议，而不是每次另写一套集成方案。

**以后AI模型要连数据库、连搜索引擎、连第三方应用，不用每家各订各的协议，只要都支持MCP就能对上话。**

它大概是客户端-服务器架构的思路：

1\. MCP服务器= 整合的情报局

企业或个人可以把自己的数据库、文件系统、日历、甚至第三方服务封装成一个个“MCP Server”，这些Server符合MCP协议，向外暴露统一格式的访问端点，任何Agent只要符合MCP客户端标准，就能发送请求、检索信息或执行操作。

比如高德就把自己的一些API，封装成了MCP，只要你有高德的API Key，你就可以在Agent上调用高德。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURprDdUC0CiaGRCb4eoKhiaSVTExD5fMkDOLiaJ31SpSONx8LT7ZPbLqPeNEv4haujCh7DlzpbFO7kEbw/640?wx_fmt=png&from=appmsg)

2\. MCP客户端 = 外交官实际使用的终端设备

就像一个Agent外交官带着专用的终端设备，可以输入各种指令：“帮我查一下财务系统里库存数据”、“帮我向某个API提交请求”，“把某份PDF拿来我看看”。

过去，如果没有MCP，你得针对各种系统写不同的访问代码，整合起来极其麻烦；但是用了MCP后，只要客户端支持协议，就能轻松切换到不同的MCP服务器。

**调用不同的信息，随时获取情报、做业务流程。**

**这大概，就是MCP的机制。**

**三. A2A和MCP的不同**

**抽象讲了很多，可能很多人，还是有点云里雾里。**

**别急，我们通过一个**故事化的场景**来把A2A和MCP的区别与合作说明白。**

**比如我们现在，有一个世界版的**国际峰会。**  
**

**各国首脑其实是各家公司的Agent代表，比如谷歌代表是小G，Anthropic派出了小A，OpenAI来了个小O，国内的阿里派出小Q，腾讯派小T等等。大家齐聚一堂，要合作完成一项跨国任务，比如联合写一份全球经济分析报告。**

在没有通用协议之前，这会基本开不起来，因为每个代表讲自家语言，互相听不懂。

但现在好了，**有了A2A协议这套外交标准**，所有代表进入会场前都签了《A2A维也纳外交公约》：发言必须用统一格式，说话先报身份、标明意图，回应要引用之前的发言ID等等。

于是，小G可以正式地用A2A格式发消息给小O，小O收到后依样画葫芦地回复一个A2A消息。**这样，不同公司的AI首次实现了无障碍对话。**

**二对话进行中，各位AI代表难免需要查阅资料或使用工具帮助分析。**

**这时候Anthropic的小A说：“各位，如果需要外部数据或工具的支持，可以通过**MCP系统**获取。”**

**原来，会场边上还架设了一套“MCP同声传译室”。里面坐着各种专家（对应不同的MCP服务器）。**

**有谷歌Drive资料馆管理员、有Slack聊天记录管家、有GitHub代码管家，甚至还有Postgres数据库管理员…只要通过MCP提请求，他们就能用统一语言回应。**

**比如，小Q（阿里云代表）想调自家云端数据库算点东西，如果按老办法，他得派人打个飞的回国去拿。**

**现在他直接在会上发送一个MCP请求（这请求其实也是按MCP定义的JSON格式发给对应的MCP Server）：**

**“我要查询X数据库里的Y数据”。**

**MCP数据库管家翻译室收到请求，立刻查库拿到结果，用MCP语言回复给小Q。**

****整个过程对其他Agent来说是透明的**，他们也听懂了小Q引用的这份数据，因为MCP翻译过来的格式大家都认识。**

**继续写报告过程中，小G(谷歌)和小A(Anthropic)发现需要把各自部分内容对接起来分析。**

**小G擅长数值分析，小A擅长语言总结，那就**协作**：**

**小G通过A2A对小A说“我这边算完GDP增速了，数据如下”，小A收到后，在自己这边通过MCP又连了一下Excel表格插件，验证了数据趋势，然后再用A2A回复小G一个总结段落……**

**一来二去，**A2A让Agent彼此沟通任务，MCP让每个智能体方便地调用外部工具补充信息**，两套协议配合默契，报告很快完工。**

**这个故事中，大家可以清楚地看到：**

****A2A更像外交部专线**，解决的是Agent**直接对话**的问题。**

****MCP更像同声传译与资源共享系统**，解决的是**智能体对接外部信息**的问题。**

**两者配合起来，就是为AI版联合国量身打造的沟通协定。有了它们，AI Agents可以各展所长又紧密合作，真正形成一个**互联互通的AI生态体系**。**

**写在最后**

**当A2A和MCP这样的开放协议逐渐统一标准之后，我们有理由畅想一个全新的**AI Agent生态**。**

**无数AI Agent像网站一样部署在各处，它们通过A2A协议彼此发现、通信，通过MCP协议调动资源、分享知识。**

**我们作为用户，就像当年浏览网页一样，可以无感知地使用这些智能体的协同服务。比如，你的个人AI助理Agent接受了你的复杂委托：**

**“帮我计划一次欧洲旅行，顺便写一篇游记稿件。”** 

**它不会单打独斗，而是迅速通过A2A喊来各路好手：旅行规划Agent、航班预订Agent、翻译Agent、文案Agent……**

**大家分工合作，各显其能。**

正如我们希望国家间少打贸易战、多订规则，AI领域我们也乐见各家少搞闭关锁国，多推行兼容协议。

A2A和MCP的崛起，意味着AI产业已经在朝着**协作而非对抗**的方向进化。

现实世界，和AI世界，明明是一体，确实两种趋势。

真是讽刺。

最后，希望这篇文章，对你有一些帮助。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言