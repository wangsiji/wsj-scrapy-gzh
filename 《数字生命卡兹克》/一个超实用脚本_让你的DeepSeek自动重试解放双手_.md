     一个超实用脚本，让你的DeepSeek自动重试解放双手。 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

一个超实用脚本，让你的DeepSeek自动重试解放双手。
============================

原创 数字生命卡兹克 数字生命卡兹克 2025-02-07 09:01 北京

> 原文地址: [https://mp.weixin.qq.com/s/t8lyNZ0sOkd0XsicYPF0-Q](https://mp.weixin.qq.com/s/t8lyNZ0sOkd0XsicYPF0-Q)

前两天我也连更两篇，写了怎么用硅基流动的API、秘塔联网搜索调用R1。

虽然这俩体验起来都很不错，可很多人还是觉得DeepSeek官方版的最好，就想用官方的，确实这也没毛病。

但是DeepSeek官方那边，这两天当然还是很卡。

不过可能是有其他平台分摊了一些火力，比起春节放假期间好了一点。之前50次都roll不出回答，现在大概roll十几次还是能被DeepSeek回应一下的。

有的时候我自己用，真的，点那个重试按钮，我都快把电脑鼠标和手机屏幕都戳烂了。

直到昨天中午他们在群里聊的时候，我突然看到群里群友的一句话：

“**搞个插件吗？遇到失败自己重试”**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHu3wr1dxvSLJJqOunsvMMZXqa7bHeF9dUJ1XJCZjlTBezC5OicMpcJicYA/640?wx_fmt=png&from=appmsg)

这一下子打开了我的新思路。。。

诶卧槽，不然我整个这个？

这不就是真实的用户需求嘛，随手又在其他几个群里问了一下，发现还有很多人真的想要一个。。。

那说干就干。

我直接原地打开我觉得最好用的编程AI，cursor。

当然思路其实都一样，你用啥都一样，Trea、windsurf啥的也行。

我其实也就花了不到十分钟，就用AI做了这么一个网页端的小脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHu1UefHjuibNt9s1ibG3qsOuweOdcSNQpY6LRuIgFqDiacnzxDXuFLtictKw/640?wx_fmt=png&from=appmsg)

这个小脚本我也放在了在公众号后台里，**直接后台私信我“ds”，系统就会自动发你脚本的文件了。**

说下怎么用。

这个脚本是在电脑浏览器里用的，脚本的使用也很简单。

下载+拖到Chrome浏览器的油猴插件里，完事。

这里说一下为啥要用脚本，而不是常见的那种Chrome插件。单纯的是更省心，一次安装后就不用管了，也不会占用你那宝贵的插件名额，会更不打扰你。

**第一步、安装油猴（Tampermonkey）插件。**

油猴插件的网站是这个：

https://www.tampermonkey.net/index.php?src=a&locale=zh\_CN

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuEb7Ba4MsRByLlKCkia4icuibxrbYZ19uiaYFXib2XR853NDSia4vnIWQibLZQ/640?wx_fmt=png&from=appmsg)

在这堆里面选择你用的浏览器就行。Chrome和Edge浏览器也可以从商店直接安装；Firefox可以从附加组件市场安装。

**第二步、把“自动重试”脚本安装到油猴插件里。**

安装完油猴插件以后，点击浏览器里油猴插件图标，就有俩眼睛的那个logo。然后选择选择“添加新脚本”。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuKia6JFNaC6lp3f74Zib7jUkelNhx5Wt4D32qPMrmemHzvZnctPV0MQng/640?wx_fmt=png&from=appmsg)

点开“添加新脚本”，进入<新建用户脚本>页面。

然后，把你下载的那个**auto\_retry.user.js**文件给拖过去。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuaoXrGe1HwRTSia4uw1asAydCficV3pBaJlHraTIVyqWrntlDEIo3pYBQ/640?wx_fmt=png&from=appmsg)

就会弹出这个安装界面。点击黄色边框的这个【安装】就可以了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuLoaqcoY22PEAV2w7ScEk609X1z4env2c87V43hmh9egzcNrOQ49ibIw/640?wx_fmt=png&from=appmsg)

**第三步、访问DeepSeek官网，启动脚本。**

DeepSeek官网应该没有人不知道了吧。不过还会再贴一下：

https://chat.deepseek.com/

在上一步安装成功后，可以再点油猴的logo种确认脚本已启用。然后访问DeepSeek的官网。像这样有“自动重试”且是开启状态就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHu07vN27RicNvQADTr6VWKicuichkJ6ZLuLC5EcajnMhfNeI3fzorXnMjPQ/640?wx_fmt=png&from=appmsg)

**第四步、自动运行。**

不用再进行任何脚本安装的操作，直接在对话框给DeepSeek发消息就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuFJtI4bPeJfSYF5jpUbwPwqCELIpOORMVibMYafRSZex4eIhCT6jClKA/640?wx_fmt=png&from=appmsg)

如果DeepSeek提示“服务器繁忙”，脚本会自动帮你点刷新按钮，直到roll出结果，或者脚本确认DS服务器算力不足。

运行起来大概就是这样的：

至此，大功告成。。。

这么一个小东西，还真的挺有用的。

当然，如果你想自己试着做一个，用cursor+一丢丢代码知识，你也能复刻一个。也简单。

这里我也说一下自己的心路历程和思路。

这个脚本的原理其实很简单：**检测到DeepSeek回复“服务器繁忙，请稍后重试”这句话，就让电脑模仿人点击【重新生成】按钮。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuktpJf8PTJlk4WFGia5jXUNPEXvxNrNkmXuwW6XusglzwFPHdtzNxrSA/640?wx_fmt=png&from=appmsg)

所以首先，需要找到出现加载bug时网页上能被检测的、正确的元素。

要做一个自动重试的插件，首先得让它能准确找到页面上真正的目标。

好比逛超市，我们需要知道要买的东西在哪个区域、哪个货架。网页也有它的货架和标注。每个按钮、文本框、图片等等等等都是一个特定的元素（elements），都有固定的位置和特征。

在DeepSeek这个场景下，我们主要需要找到两个关键元素：**显示“服务器繁忙”的AI回答区域，和重新生成的按钮。**

找这些元素很简单。在对应的位置右键点击，选择【检查】，就能看到这个元素的具体代码信息。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuxvgGiaaiafJUic3bMfSia4BBG1keOo9iaog0BwQlHlmiaaichdFe28iaZFQBmw/640?wx_fmt=png&from=appmsg)

点开检查后，网页右半边会出现一堆代码，那里就能查看页面内的所有元素了。

你还可以点击开发者工具栏上的【选择元素】按钮（就是那个虚线框带箭头的小icon），直接在页面上点击你想找的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuxgricKamMmw7lBAh0HWMfARER90wy6usQvmPI75hSZLFwOS6afeB9lw/640?wx_fmt=png&from=appmsg)

原理差不多就是这样，也不复杂。

找好需要的关键元素后，插件才知道该关注页面的哪些地方，该点击哪个按钮。

现在可以开始写自动重试的代码了。我自己其实经历了3个版本的迭代。

**1.0版本：**

1.0版本主要就实现了基础功能。我希望检测到页面出现服务器繁忙，就会显示3秒钟提示，然后随机延时1.5-3秒后自动点击重试。

需求清晰后，我把要求告诉给cursor。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuBywH6cmx52icwkbHf9JACpw1MBHIibIJZbeFAhfGYvrbc7cWDRFkCiaaA/640?wx_fmt=jpeg)

其实Prompt就一句话：**写一个油猴脚本，检测到服务器繁忙，请稍后再试。自动点重试**

    写一个油猴脚本，检测到服务器繁忙，请稍后再试。自动点重试

后面那一大串代码看着吓人，其实就是我从网页复制下来的整个对话区的elements。让Cursor知道前端UI啥样，知道脚本咋写。

很快Cursor就给我写了一个js脚本。这个脚本已经能模拟人发现服务器卡住，然后点击鼠标的行为了。

但我一开始没给脚本设置停顿，它直接刷新了20次，而且卡到飞起。吓得我以为是脚本被DS误判为DDOS攻击了。。。

后台一看，好消息：我没被检测为机器人。

坏消息：DS算力又崩了= =。

**2.0版本：**

但脚本但被误判为恶意行为的风险确实存在。服务器堵是一时的，被判定为恶意行为，DeepSeek可能会锁你一小时，不给你roll了。

所以我加了小判定：最多尝试重roll10次、加随机停顿时间等等。

    每次检测到繁忙时，要在右上角显示临时提示，持续3秒后自动消失。为了模拟真实用户行为，点击重试按钮前要随机延迟1.5-3秒。如果连续10次重试仍然失败，说明 DeepSeek 当前可能真的算力不足，此时显示持续提示"检测到多次失败，DeepSeek可能当前算力不足"，需要用户手动关闭。关闭提示后重置重试计数。

‍这样就可以最大化的进行风控，保证号的安全，也不会对DeepSeek那边有太大压力。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHubyEKX8oWnWQgsVu6C9IAsAyuiaZFzDsR76NwdWOFB0rIpV5s4ntw6Ig/640?wx_fmt=png&from=appmsg)

OK，这下应该是安全了。

我兴冲冲开始测试，结果又发现一个bug。

现在吧，这个插件有点敌我不分。

主要是昨天下午我看到了一个贼有意思的对话截图，用户和DS玩角色互换，就是让DS演用户我演AI。这倒反天罡的东西承包了我一天的笑点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuTtadLwDkxWCs1hoIfZLyVbKmS1Tx0BAVPqol0ibAE3jl0xW6GQ7PDMw/640?wx_fmt=jpeg&from=appmsg)

但，我在开脚本试图复刻的时候，翻车了。

我给ds发“服务器繁忙请稍后重试”的结果是，喜提一个deepseek无限流版。当时R1太太太卡了，我就先拿V3做个示范。

脚本把我的指令误判为报错，DS哪怕回答出内容了也会被强制重roll。

直接给我整不会了。

**3.0版本：**

排查了一下2.0这无限流bug的原因，是元素的识别出了点小错误。不过找到问题就好改，直接交给cursor。

    <div class="fa81"><div class="fbb737a4">服务器繁忙，请稍后再试<div class="ds-flex e0558cb1" style="position: absolute; right: calc(100% + 18px); top: 12px; gap: 12px;"><div class="ds-icon-button" tabindex="0" style="--ds-icon-button-text-color: #909090; --ds-icon-button-size: 20px;"><div class="ds-icon" style="font-size: 20px; width: 20px; height: 20px;"><svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><clipPath id="clip1248_20193"><rect id="鍥惧眰_1" width="17.052675" height="17.052441" transform="translate(1.000000 1.000000)" fill="white" fill-opacity="0"></rect></clipPath><clipPath id="clip1257_20794"><rect id="复制" width="20.000000" height="20.000000" fill="white" fill-opacity="0"></rect></clipPath></defs><g clip-path="url(#clip1257_20794)"><g clip-path="url(#clip1248_20193)"><path id="path" d="M5.03 14.64C4.77 14.64 4.5 14.62 4.24 14.56C3.98 14.51 3.73 14.43 3.49 14.33C3.24 14.23 3.01 14.1 2.79 13.96C2.57 13.81 2.37 13.64 2.18 13.45C1.99 13.26 1.82 13.05 1.68 12.83C1.53 12.61 1.4 12.37 1.3 12.13C1.2 11.88 1.13 11.63 1.07 11.36C1.02 11.1 1 10.84 1 10.57L1 5.07C1 4.8 1.02 4.54 1.07 4.27C1.13 4.01 1.2 3.76 1.3 3.51C1.4 3.26 1.53 3.03 1.68 2.81C1.82 2.58 1.99 2.38 2.18 2.19C2.37 2 2.57 1.83 2.79 1.68C3.01 1.53 3.24 1.41 3.49 1.31C3.73 1.2 3.98 1.13 4.24 1.07C4.5 1.02 4.77 1 5.03 1L10.49 1C10.75 1 11.01 1.02 11.27 1.07C11.53 1.13 11.78 1.2 12.03 1.31C12.27 1.41 12.51 1.53 12.73 1.68C12.95 1.83 13.15 2 13.34 2.19C13.53 2.38 13.69 2.58 13.84 2.81C13.99 3.03 14.11 3.26 14.21 3.51C14.31 3.76 14.39 4.01 14.44 4.27C14.5 4.54 14.52 4.8 14.52 5.07L12.94 5.07C12.94 4.91 12.92 4.75 12.89 4.58C12.86 4.43 12.81 4.27 12.75 4.12C12.69 3.97 12.61 3.83 12.52 3.69C12.43 3.56 12.33 3.43 12.22 3.32C12.1 3.2 11.98 3.1 11.85 3.01C11.71 2.92 11.57 2.84 11.42 2.78C11.27 2.72 11.12 2.67 10.96 2.64C10.81 2.61 10.65 2.59 10.49 2.59L5.03 2.59C4.87 2.59 4.71 2.61 4.55 2.64C4.4 2.67 4.24 2.72 4.09 2.78C3.95 2.84 3.8 2.92 3.67 3.01C3.54 3.1 3.41 3.2 3.3 3.32C3.18 3.43 3.08 3.56 2.99 3.69C2.9 3.83 2.83 3.97 2.77 4.12C2.71 4.27 2.66 4.43 2.63 4.58C2.6 4.75 2.58 4.91 2.58 5.07L2.58 10.57C2.58 10.73 2.6 10.89 2.63 11.05C2.66 11.21 2.71 11.37 2.77 11.52C2.83 11.67 2.9 11.81 2.99 11.94C3.08 12.08 3.18 12.2 3.3 12.32C3.41 12.43 3.54 12.54 3.67 12.63C3.8 12.72 3.95 12.79 4.09 12.86C4.24 12.92 4.4 12.96 4.55 13C4.71 13.03 4.87 13.04 5.03 13.04L5.03 14.64Z" fill="currentColor" fill-opacity="1.000000" fill-rule="evenodd"></path></g><path id="path" d="M14.75 18.91L9.3 18.91C9.03 18.91 8.77 18.88 8.51 18.83C8.25 18.78 8 18.7 7.75 18.6C7.51 18.49 7.27 18.37 7.05 18.22C6.83 18.07 6.63 17.9 6.44 17.71C6.25 17.52 6.09 17.32 5.94 17.1C5.79 16.87 5.67 16.64 5.57 16.39C5.47 16.14 5.39 15.89 5.34 15.63C5.28 15.37 5.26 15.1 5.26 14.83L5.26 9.33C5.26 9.06 5.28 8.8 5.34 8.54C5.39 8.28 5.47 8.02 5.57 7.77C5.67 7.53 5.79 7.29 5.94 7.07C6.09 6.85 6.25 6.64 6.44 6.45C6.63 6.26 6.83 6.09 7.05 5.95C7.27 5.8 7.51 5.67 7.75 5.57C8 5.47 8.25 5.39 8.51 5.34C8.77 5.29 9.03 5.26 9.3 5.26L14.75 5.26C15.01 5.26 15.28 5.29 15.54 5.34C15.8 5.39 16.05 5.47 16.29 5.57C16.54 5.67 16.77 5.8 16.99 5.95C17.21 6.09 17.41 6.26 17.6 6.45C17.79 6.64 17.96 6.85 18.1 7.07C18.25 7.29 18.37 7.53 18.48 7.77C18.58 8.02 18.65 8.28 18.71 8.54C18.76 8.8 18.78 9.06 18.78 9.33L18.78 14.83C18.78 15.1 18.76 15.37 18.71 15.63C18.65 15.89 18.58 16.14 18.48 16.39C18.37 16.64 18.25 16.87 18.1 17.1C17.96 17.32 17.79 17.52 17.6 17.71C17.41 17.9 17.21 18.07 16.99 18.22C16.77 18.37 16.54 18.49 16.29 18.6C16.05 18.7 15.8 18.78 15.54 18.83C15.28 18.88 15.01 18.91 14.75 18.91ZM9.3 6.86C9.13 6.86 8.97 6.87 8.82 6.91C8.66 6.94 8.51 6.98 8.36 7.05C8.21 7.11 8.07 7.18 7.93 7.28C7.8 7.37 7.68 7.47 7.56 7.58C7.45 7.7 7.35 7.82 7.26 7.96C7.17 8.09 7.09 8.24 7.03 8.38C6.97 8.54 6.92 8.69 6.89 8.85C6.86 9.01 6.84 9.17 6.84 9.33L6.84 14.83C6.84 15 6.86 15.16 6.89 15.32C6.92 15.48 6.97 15.63 7.03 15.78C7.09 15.93 7.17 16.07 7.26 16.21C7.35 16.34 7.45 16.47 7.56 16.58C7.68 16.7 7.8 16.8 7.93 16.89C8.07 16.98 8.21 17.06 8.36 17.12C8.51 17.18 8.66 17.23 8.82 17.26C8.97 17.29 9.13 17.31 9.3 17.31L14.75 17.31C14.91 17.31 15.07 17.29 15.23 17.26C15.38 17.23 15.54 17.18 15.69 17.12C15.83 17.06 15.98 16.98 16.11 16.89C16.24 16.8 16.37 16.7 16.48 16.58C16.59 16.47 16.7 16.34 16.79 16.21C16.87 16.07 16.95 15.93 17.01 15.78C17.07 15.63 17.12 15.48 17.15 15.32C17.18 15.16 17.2 15 17.2 14.83L17.2 9.33C17.2 9.17 17.18 9.01 17.15 8.85C17.12 8.69 17.07 8.54 17.01 8.38C16.95 8.24 16.87 8.09 16.79 7.96C16.7 7.82 16.59 7.7 16.48 7.58C16.37 7.47 16.24 7.37 16.11 7.28C15.98 7.19 15.83 7.11 15.69 7.05C15.54 6.98 15.38 6.94 15.23 6.91C15.07 6.87 14.91 6.86 14.75 6.86L9.3 6.86Z" fill="currentColor" fill-opacity="1.000000" fill-rule="nonzero"></path></g></svg></div></div><div class="ds-icon-button" tabindex="0" style="--ds-icon-button-text-color: #909090; --ds-icon-button-size: 20px;"><div class="ds-icon" style="font-size: 20px; width: 20px; height: 20px;"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M18.2286 17.3545H1.77142C1.34538 17.3545 1 17.6999 1 18.1259C1 18.552 1.34538 18.8973 1.77142 18.8973H18.2286C18.6546 18.8973 19 18.552 19 18.1259C19 17.6999 18.6546 17.3545 18.2286 17.3545Z" fill="currentColor"></path><mask id="mask0_400_418" maskUnits="userSpaceOnUse" x="1" y="1" width="15" height="15"><path d="M15.1429 1.10254H1V15.2454H15.1429V1.10254Z" fill="white"></path></mask><g mask="url(#mask0_400_418)"><path d="M2.48999 15.2425C2.36999 15.2425 2.26002 15.2225 2.15002 15.2025C2.04002 15.1725 1.94003 15.1325 1.84003 15.0825C1.73003 15.0325 1.63999 14.9825 1.54999 14.9025C1.45999 14.8325 1.39001 14.7525 1.32001 14.6625C1.25001 14.5825 1.19001 14.4825 1.14001 14.3825C1.09001 14.2825 1.05003 14.1725 1.03003 14.0625C1.01003 13.9525 1 13.8425 1 13.7225C1 13.6125 1.00998 13.5025 1.03998 13.3925L1.75 10.4325C1.9 9.81254 2.20001 9.28253 2.64001 8.83253L9.40002 2.08253C9.55002 1.92253 9.71997 1.78254 9.90997 1.66254C10.09 1.54254 10.28 1.44254 10.49 1.35254C10.69 1.27254 10.9 1.20254 11.12 1.16254C11.33 1.12254 11.55 1.10254 11.77 1.10254C12 1.10254 12.21 1.12254 12.43 1.16254C12.65 1.20254 12.86 1.27254 13.06 1.35254C13.27 1.44254 13.46 1.54254 13.64 1.66254C13.83 1.78254 14 1.92253 14.15 2.08253C14.31 2.24253 14.45 2.41254 14.57 2.59254C14.69 2.77254 14.79 2.97255 14.88 3.17255C14.96 3.37255 15.03 3.59254 15.07 3.80254C15.11 4.02254 15.13 4.24254 15.13 4.46254C15.13 4.68254 15.11 4.90253 15.07 5.11253C15.03 5.33253 14.96 5.54254 14.88 5.74254C14.79 5.95254 14.69 6.14254 14.57 6.32254C14.45 6.51254 14.31 6.68253 14.15 6.83253L7.40002 13.5925C6.95002 14.0425 6.42 14.3325 5.81 14.4825L2.84003 15.1925C2.73003 15.2225 2.60999 15.2425 2.48999 15.2425ZM11.67 2.73254C11.22 2.76254 10.84 2.94254 10.52 3.26254L3.78998 9.99254C3.55998 10.2225 3.41002 10.4925 3.33002 10.8125L2.66998 13.5625L5.42999 12.9025C5.73999 12.8225 6.02 12.6725 6.25 12.4425L13 5.68254C13.08 5.60254 13.15 5.52255 13.22 5.42255C13.28 5.33255 13.33 5.23254 13.38 5.12254C13.42 5.02254 13.45 4.91254 13.47 4.80254C13.5 4.68254 13.51 4.57254 13.51 4.46254C13.51 4.34254 13.5 4.23254 13.47 4.12254C13.45 4.01254 13.42 3.90254 13.38 3.79254C13.33 3.69254 13.28 3.59254 13.22 3.49254C13.15 3.40254 13.08 3.31254 13 3.23254C12.82 3.06254 12.62 2.92254 12.39 2.84254C12.16 2.75254 11.91 2.71254 11.67 2.73254Z" fill="currentColor"></path></g></svg></div></div></div></div></div>

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqtPibAS8ZrUpc0G5E3BadHuHt0o2rM7uX1ibpqy3JSWw1JppFFOhMSeWOkm2vtlYcjJ08hQDnGa2cA/640?wx_fmt=png&from=appmsg)

经历两次迭代，终于没啥明显的bug了。

最终测试！

无限流bug，修复成功。

以及多次重roll并计数。

很好，很稳，安心合眼ing。

从春节爆火到现在，都两周了。

DeepSeek的热度一点也没有下降。

我甚至感觉随着陆续开工，它还越来越卡了= =。。。

用户给服务器增压→倒逼官方扩容→吸引更多用户→再次增压…直接无限循环了。

虽然被“服务器繁忙”烦到火冒无数次，但看到越来越多人开始真正了解AI、用上AI。见证一个新时代的开始，还是觉得挺值得的。

作为一个AI殿堂门口的门童，看着越来越多人的进入这个殿堂，感受到它的魅力，真的也发自内心的开心。

以一灯传至诸灯，终至万灯皆明。

而我现在最大的愿望就一个：

DeepSeek你快点恢复吧，这个世界不能没有你。

我非常非常希望。

今天这个自动重试的插件，早日吃灰。

早日迎接DeepSeek的，满血回归。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克、dongyi、稳稳

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言