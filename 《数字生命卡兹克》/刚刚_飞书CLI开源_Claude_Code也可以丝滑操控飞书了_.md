     刚刚，飞书CLI开源，Claude Code也可以丝滑操控飞书了。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

刚刚，飞书CLI开源，Claude Code也可以丝滑操控飞书了。
=================================

原创 数字生命卡兹克 数字生命卡兹克 2026-03-28 17:21 北京

> 原文地址: [https://mp.weixin.qq.com/s/fvjxT\_GgbEgxgsPCUlo-RQ](https://mp.weixin.qq.com/s/fvjxT_GgbEgxgsPCUlo-RQ)

大周末的，起床第一件事，就看到，飞书开源CLI了。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXJrRlmawyFrgC5iaWLxyEoPqrsyIaibn4uF8du9vFBwyVanxuT8B5jVYCjR2OoXJLFKiceaqQJqy4dwgk1X3yBs0zPm4NX1F16vw/640?wx_fmt=png&from=appmsg)

这个事情的意义之重大，我真的觉得，不亚于OpenClaw第一次可以接入飞书的那一天。

因为现在，飞书，这个我们公司天天在用的工具，我终于有一种全新的使用方式了。

我可以，直接在Claude Code里，通过一句话，随意的处理我飞书里面的所有信息和数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXyxgl4kBdVefsYibW57L1qdnF7ibVSK39xF4UDglNaxnv18ob4DxW2dBjEPFbibR0zLOcm7YG98skCItCbVQMGn7JJDl2d5Mwk3U/640?wx_fmt=png&from=appmsg)

我之前写过一篇文章，[AI，正在吞噬所有软件。](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647680642&idx=1&sn=5fa4079a7173030c78cf9a4b2a60f35f&scene=21#wechat_redirect)

那时候就说过，图形界面感觉正在被蚕食。

而现在，飞书这个可能是我日常使用时长仅次于微信、拥有我几乎全部工作数据的办公产品，用一种极度戏剧化的、将整个软件全部压缩降维成CLI化的方式，吹响了向Agent时代冲锋的号角。

未来，所有的产品，都将有两种形态。

GUI，面向普通用户。

CLI，面向开发者和AI。

很多朋友可能不是开发者，可能不知道CLI和GUI到底是个啥，所以，为了保证大多数人的阅读体验，我先做个小小的科普，如果已经非常了解的玩家，可以直接跳过这一趴。

GUI，Graphical User Interface，图形用户界面。

说人话就是，你现在看到的一切。

你手机上的微信界面，你电脑上的飞书窗口，你每天点来点去的那些按钮、菜单、对话框，全部都是GUI。

它的逻辑是，把所有功能变成你看得见摸得着的东西，你不需要记任何命令，看到按钮就点，看到输入框就填，简单直观，傻瓜式操作。

GUI是为人类设计的。

因为人类是视觉动物，我们需要看到东西才能理解东西。

而CLI，Command Line Interface，命令行界面。

就是那种，黑乎乎的屏幕，你敲一行字，电脑给你吐一行结果的东西，这个就是非常刻板印象的命令行。

![undefined](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqWaeVvYz2BYGiaIgq9E9Xrdca34ZEBHNGsic8EqFkO2r5KWux8Uu8feU3T5LRXEmw9dpuricqMtxkL4kiaxHKYgmGDC3fFUf0tm7XY/640?wx_fmt=jpeg)

很多人一看到这个界面就头大，觉得这玩意是程序员才用的。

以前确实是，但是现在，大人，时代变了。

现在很多Agent都是在CLI上跑效果最好，比如，大名鼎鼎的Claude Code。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXJr3w0WzXmjX2WS0ibibNppksd9xC7efevEb2JJVSmMpcmPdBVXBAw4yVdpuJsVbc5r8TIuLnIVur4cOmSiatV6phr7raQhloMSg/640?wx_fmt=png&from=appmsg)

因为CLI有一个GUI永远比不了的优势，就是，它天然适合被AI操控。

在这个年头，AI最核心的交互方式，依然是文字，是指令。

是一句一句的代码命令。

而CLI，恰好就是用命令来操作一切的。

所以你就能理解，为什么飞书要开源一个CLI了。

它不是给你用的。

嗯，也不完全是，你也可以用，但它最核心的用户，是AI。

是你的AI Agent。

是Claude Code，是Codex，是OpenCode，是OpenClaw，是那些未来所有那些帮你干活的AI助手。

所以我觉得，飞书这一步，迈的步子其实是有点狠的，因为很多传统的产品，都会看所谓的DAU，所谓的停留时长等等，这种口径，都要打开你的GUI产品才算。

但是当你把CLI开源出来之后，所有的Agent都可以通过命令行来直接调用你，那我其实，有些时候就不需要打开飞书了，那传统口径上的日活肯定会掉，但真正的对用户的价值，却反而上升了。

所以啊，飞书这一步，走的还是很漂亮，直接把整个产品压缩成了一套命令行工具，这也充分说明，自上到下，都想的非常清楚，一个效率工具，那就应该为了用户的效率去服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVv2lUWia9sT66mEic6R9TFN4lUA659BTmkqkItoF98OZiceNrKm37nvFhBpsqa8gMjl87GrDWgvFhE3ojpKrKxx3Tj7nPXBq9Y1Y/640?wx_fmt=png&from=appmsg)

从OpenClaw开始，飞书看来誓死要把Agent基建平台这个心智焊在脸上了。

飞书CLI开源地址：

https://github.com/larksuite/cli

安装和使用它也特别简单。

我用Claude Code举例子，Codex、OpenCode等等啥的都一样，你直接对着你的Agent说出一句话就行：

    帮我装一下所有的东西：https://github.com/larksuite/cli/blob/main/README.zh.md

直接复制我的这个Prompt就好了，你也完全不需要走什么申请审批，人人可用。

就是这块有个小细节注意一下，不要直接说装飞书CLI，这样有可能会不装Skills，所以用我的Prompt。

如果是之前装了飞书插件的OpenClaw用户，飞书会升级那个插件，就已经包含CLI了，不用把插件和CLI一起装。

发过去之后，Cluade Code就会直接把飞书CLI和19个Skills就给你装好了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUiaHjjlicDrkrJcBqjV41YFbP1GO7TS2lFRwKbBZVdeB1WIU99Iicb3BwjFfbhiaxXcsve7rIL4FVic5RTDZb2m6Nu8TbnM2snS9X4/640?wx_fmt=png&from=appmsg)

这个地方一定要确认下，Skills也都给你装上了，如果没有Skills，就把这个发给AI，再手动让AI安装一下：

    npx skills add larksuite/cli --all -y -g

但是因为只是装好了飞书CLI，还没有跟你自己的飞书账号关联上，所以还需要配置一下，你直接让他自己跑就行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWBAuqn8icI69cDNPnJONHsMboiaXwibVPEXicFaHWjYoUC2yAWLypaTF5rfCGiaIibnnU4SsZIIdZfRqicYGgdqXRDjJJE0cR2VccIgg/640?wx_fmt=png&from=appmsg)

然后就会给你一个二维码链接，复制到浏览器里面自己手动配置一下。

嗯，这个手动，其实就是让你选一下头像和名字，其他的都不用管。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVEVNKPutTLG50ia8ZFGibyA6IwroyBQ7DF058iaicLJDlmJCTCib2Ra3gEt8ibummm6ffPrMicHzMm2x420FUSK5SnzgppP4kvHICbKs/640?wx_fmt=png&from=appmsg)

点击创建，这个应用就创建完了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXYOkXeOKDYUwxQa3B3LKlWLNWVwTN4T6WrC5FRTMswoJPYjB7xhhqRIYVh5Z0zDSic6sjSrXVrvqOW0DVHWlibOC8icf8jO426pg/640?wx_fmt=png&from=appmsg)

然后Claude Code那边就会继续跑登录的授权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqW5y3WU4fIkia5NHiaicjZIZ7vXPoYpNAaCh2zsEhRb535Y8hibiaOOsEEia1vVTp89yAUaXpEicpu5U5YJUiass7ibPicwI6ZWNMnm8wl2Q/640?wx_fmt=png&from=appmsg)

会继续给你一个网址，手动粘贴授权就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXlBGsQ0IhVyt0mQeUbdX6kibogrnuVO38iatuzBKUZERkxsGKGNTjFMTicP6znoE14pVmTg4f2uy75wYMNtpjL9x4icoYobXib3I8U/640?wx_fmt=png&from=appmsg)

最后，安装步骤，一切大功告成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUuphRQnatQdomxDiaEbgfBBUKQlmySY0ECQhQIlyI9T3UfzKVFMGPWo3Cc5N7WtICpxheDyiafwjicw9k7uWcGROadnPibOyFa2ibQ/640?wx_fmt=png&from=appmsg)

靠，为什么抓到的又是我的真名。

至此，你就可以在Claude Code里，操控我的飞书了。

这时候，一定、一定、一定记得重启一下你的Claude Code、Codex、OpenCode等等Agent产品！

这不是装个Skill热重载就可以用了，记得重启。

目前，飞书CLI支持这些权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqURPJxMJrIficcDBIWCg2xUVurDPamj6JjxHibB7dJYFsJxrQ3njqBBUjKQxx3rGsa7VEbaJxJicspIvh5yibzqTk4X9Su3sj9Y3JA/640?wx_fmt=png&from=appmsg)

我说实话，他们这个开源的能力有点多，基本把核心功能全放出来了。。。

然后我装好飞书CLI后，干的第一件事。

是想把这个消息，用飞书私信的方式，通知一下我们公司的所有小伙伴。

我就写了一段话：

帮我给我的通讯录里的所有内部联系人，个性化的发一句话，大概意思就是：这是今天飞书CLI上线以后，我用Cluade Code操控飞书给大家发的第一条消息，以后飞书的使用方式就真的变了，感受一下Agent时代的魅力吧，周末愉快！然后附上飞书CLI的Github链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqUI4VYH5Ak9CSLb99Hicx9SHWEoeiaXqDOateMUgZnNvkqOulmJDhrpTO1j1a0hkPKyUYxELdeSK1hw6539amRZmQ6xjhQ3kAUQo/640?wx_fmt=jpeg)

我们公司现在25个人。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVws5L5mx5KIFYlQibET7mSAQqwlhbNrR4wNNuO7raoroHwnx8Z7swFullvz9AlYuBlgpkw3CJaIZJ1kbAoO4cPuxkYOibrJibSao/640?wx_fmt=png&from=appmsg)

然后，Agent也给我找到了25个联系人，把我自己排除掉，就是这24个。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVydHlejhwQ4bMc12uqFMfCbXE8sl7fCtKEZKGfW2HvUA5PFjvKUGpjuqLSTxKJdqMYhZXr02Cgoocp59siaclibSLiaxRnFH8Dro/640?wx_fmt=png&from=appmsg)

于是，Claude Code和飞书CLI开始发送信息，一共花了一分钟，消息就全部发出去了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVUqLhBl5fia0xnCZvia2yHZ77YOJoKImFZg4Bwj6D0DSB0jJl0OS2NyYJOf4Ttqkgx6HccgPib6Kaz2UONhqGicLJGic9TjHVBppzM/640?wx_fmt=png&from=appmsg)

10秒后，就有我们的同事，来给我反馈截图了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUXzYQZiaLQBlO1J8lRKwMWPKwibLTOuibQTEb6FweZh53iaDpLUHib0icI11I8UMgia3Kl19fyicLuHGqAcRdibMbkUoteXMnBnZlgD15I/640?wx_fmt=png&from=appmsg)

这就是Agent啊....爽爆了。

我还能直接，把我的公众号数据的那个多维表格，直接做成一个可视化网页。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUCY7Vl4iaBQmYXRMXpGcXahOlIhGxEbmJuN4hN7xtWnyT1WIZquzPlZUQFXHeP815EEZSyWcqfGwgl4NCgQJPNWic7hnDnMoZxA/640?wx_fmt=png&from=appmsg)

中间遇到需要授权的，你就直接给授权就行了。

然后，就非常丝滑的找到了我的那个多维表格。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVj66O8NhMictfRezTvUaSd8ia6jm8SMfjiaicENp7o9WSIe98iawCYbkqHcAiaKzzia1wxuKRoKa0ljjXpdN79bmG18dggcF581aDgGw/640?wx_fmt=png&from=appmsg)

然后，使用fontend design这个skill，给我设计了一个数据分析网页。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXicw18txDhNNgbSw9dXXADicTR1Y4VpMOlnibZZQPJNhJ7jochUNicrO3FJY6jwMQ7kiauxZLibeXmmQu7wHt29ymP6KuYfQEwfyPWk/640?wx_fmt=png&from=appmsg)

有些洞察还挺有意思，我是没想到，在我自己这里，越短的标题，数据量反而越好。

这甚至都比飞书的仪表盘好用了我说真的= =

然后我们自己整个MCN的项目管理，非常的庞杂，都放在了一张表里面，经纪人、商务、广告执行、财务基本都在一张表里面进行项目同步和协同。

那个表里面敏感信息太多了，我就不给大家贴了，我们有个痛点就是，那个表里数据量爆炸，而且虽然我们已经把绝大多数都做了自动化和公式，但很多依然都是人工手动填，没有办法自动化，所以偶尔就可能有个失误，导致数据出错，那现在，我就可以，直接把规则给AI，然后用Claude Code来检查了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUdicRibsAacZdolA5Itd6ssrfXYgRq90kasoYlYiccACLtNibv4MDZjsh6vEC8YHyoq25OkVMcwUOImLYtLNibasKCsppBHVHFynsk/640?wx_fmt=png&from=appmsg)

不扫不知道，一扫吓一跳。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVxa0dicIJoibvpt7ys68de0Ur5qLln75BPBDK3Sm1tf9vNeH7Gjiaj5zGiay7LyHxiaK4T9GB1F1bwUJc4rPBJRTPD4cAUIrvhWwwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqV9vHMlIrInTKlldiaJnknyedUClksCQblOXulOwd1nu3zk6lrVB2rXPhcmsk9Odp5lPRSicS6UbpfKRaSa6xgUUb2WX6AImpWgw/640?wx_fmt=png&from=appmsg)

。。。

一会我就设个自动化，Claude Code每周五扫一遍飞书多维表格，只要有空着的缺失字段，周五下午就给各个负责的同事直接自动发一下消息，让他们赶紧去填，别再漏字段了。

还有一个，我自己也是觉得蛮有用的，还免了我们的开发时间，就是把我自己做了一个给公司内部看的AIHOT热点监控网站。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWvia5jBcfkqic2QtGUBUjY8V6GcWKN8KC34DNdL4icprghelfmeZ2Cqczag4xYkicAiaqEcKfdqsciaOEBv2smpvAMx7gYMibGuZ34hs/640?wx_fmt=png&from=appmsg)

我一直还想做一个飞书日报，每天早上给我们发一份昨天监控的所有信息的汇总日报，之前没啥空开发，跟飞书协同也有点麻烦，现在，完全可以直接干了。

于是，我就直接拉了个群，把飞书CLI机器人也拉了进去。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUalRXk6PXeQmcsHZolo9mBnbIPwMMbTXYw6K89Dsr7JyzCJvJD0mrc8rNCxwh6BhTtgp2RoiasT4w6YEQQEIqLcnjibQdupNjw0/640?wx_fmt=png&from=appmsg)

然后打开Cluade Code，

直接说了我的需求。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVjeAmPahG66zNylkWWfps3WcInl0Z84cDgfGYibPmn5DQXykLQibelibRc4ereehhTg8EgrKfAnq7e6qQM4GBic5JXU4ibgFbzCwZ8/640?wx_fmt=png&from=appmsg)

他就开干了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUIT5tDicAG6sXM2uoVTpfM9nTa6RKGZjagIyFAPpoqd5xCNQdgUbicncx3pFbvpNTmNuQbUxLUVrergClSDicbxhETcvziboa5gYk/640?wx_fmt=png&from=appmsg)

几分钟后，开发完成，直接帮我部署上线到我的服务器上了。

10分钟不到，这个需求就做完了，爽飞了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXl6s63bBEG4UFCm4dTuZDkibAnuHR1NBhRuU4Wvib98M3kj7c0pDGcFo1j07CP2WXRobu86rZvsKcP2MMLyUibyAaRT6uk1939j0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWvBMm1aktWjTFvIHzvjKle2yNYjs2sL6MIx6RqKSbxjfeP5RgspdyDU1xuwgU8AxZoMBNkFV1wkmiazKgwHdqQfSNdficc5kPK4/640?wx_fmt=png&from=appmsg)

改都不用改，真的，夯爆了。

甚至，还能帮我汇总邮箱里收到的简历。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXptmuZQcJG6I9xMf7Nv6oyYb6f67nicrpfiaLOlBueAyXDD4oryOk8xMzYK9oKceoADbxC7GpCrUCXG3Ja6C3mchr0KoQicbeevk/640?wx_fmt=png&from=appmsg)

也是几分钟就能搞定，你完全可以自己沉淀成一个系统或者的评分Skill，以便后续进行复用。

Claude Code+飞书，真的爽爆了，我现在真的已经很少开一些软件了，Claude Code都快成了我的新操作系统了。

打开Claude Code，我感觉，我就拥有了全世界。

而且，这次飞书还有个小细节设计的非常好，截图不到了，我只能用嘴说一下了，是在过程中发现的。

就是一般我们会遇到一些API啥的报错信息，都是什么404、502啥的对吧。

但是飞书CLI会返回的是，哪个参数出了问题、具体错在哪里、下一步应该执行什么命令来修复，这个小细节我觉得真的很屌，AI拿到这些信息可以自主重试和修正，我觉得值得所有家学习。

讲真，作为一个曾经的UX设计师，我是真的觉得，曾经的那一套面向人类设计的UX理论，那座大厦的基石，都在坍塌。

Agent时代的软件，需要为AI操作设计。

AI不需要看到按钮。

AI不需要花里胡哨的动画。

AI需要的是，你给我一个接口，告诉我能做什么，我来调用。

一行命令，一个功能。

所以啊，以前，软件的演化路径是，CLI → GUI。

电脑最早就是命令行的，后来有了Windows、有了Mac的图形界面，普通人才开始用得上电脑。

而现在，路径反过来了，GUI → CLI。

不是因为我们要回到过去。

而是因为，那个新的用户来了。

这个新用户，叫Agent。

我突然想起之前看《西部世界》里面，有一句我至今还难忘的经典台词：

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUnRGKfiaHvwJ6kauj5sRkAWiaSBT4WiaHQucTgBXcZgHB0WibFGzrfXb23ibWLaic8uUX8okrUmQejXbzrxxka29j5RPaOAtSAt9txI/640?wx_fmt=png&from=appmsg)

如果这个世界，所有的软件都能跟飞书一样CLI化。

如果所有你日常使用的软件，都有一层CLI，都可以被AI直接调用。

那时候，我们心中所想的。

科幻世界里的那个超级AI助理。

就真的即将快被实现了。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言