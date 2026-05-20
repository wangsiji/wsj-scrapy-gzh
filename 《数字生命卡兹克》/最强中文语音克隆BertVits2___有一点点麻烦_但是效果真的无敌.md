     最强中文语音克隆BertVits2 - 有一点点麻烦，但是效果真的无敌 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

最强中文语音克隆BertVits2 - 有一点点麻烦，但是效果真的无敌
===================================

原创 数字生命卡兹克 数字生命卡兹克 2024-01-15 18:04 天津

> 原文地址: [https://mp.weixin.qq.com/s/2P-aJ6zdNIaNrX0ET5QiaA](https://mp.weixin.qq.com/s/2P-aJ6zdNIaNrX0ET5QiaA)

曾经我写过一篇做语音克隆的AI音频工具：[11Labs](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647660086&idx=1&sn=daffe518acad39de416638660ade8c69&chksm=f007ca61c77043772991b50aae00ea6670649809d1233f5fe84a9a2754ac1d054fe71b4ce502&scene=21#wechat_redirect)

效果好是好，也非常傻瓜简单，但是很多朋友都跟我反馈说，11Labs中文效果不好。  

没办法，毕竟国外的产品，在世界的AI产品舞台上，中文从来不是主流语言。这也是一个非常让人伤心的话题，明明世界AI圈里，主流的从业人员都是华人，但是中文的数据集和效果...哎。  

而国内的AI音频产品，比如出门问问的魔音工坊，效果确实很好，而且他们也有做媲美11Labs语音克隆的实力，但是因为国内很多很多的原因，内部做出来了，有时候也不太对外放出来...具体的原因我就不细聊了，反正，懂得都懂。  

总之，还是得靠自己，所以去年我12月翻了很久的TTS项目之后，找到了这个：

**Bert-Vits-2**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtOFH9ufTCnCleK9MBsibIb8L31LnfpnDlAMuic8rTTBW2v6cKPEgBNtGw/640?wx_fmt=png&from=appmsg)

但是吧，这个效果虽好，但是没有好的特别影响代差的地步，直到上周有个大佬传了一个分支项目：  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdt62FDmiaZR7T2PiatQHXiapxlJdm1k1rrdyLWFOTzXWCkYlsibJPMTKbFgw/640?wx_fmt=png&from=appmsg)

我觉得，中文语音克隆TTS的最强项目，到来了。

可以听听看，我去网上扒了B站UP主“峰哥亡命天涯”的音频，训练成TTS模型之后，说话的效果：  

这可能是目前市面上，开源TTS这块，我能体验到的最好的中文音频克隆效果了。  

话不多说，开始教程，这次不是那么傻瓜，会有一点点麻烦，需要点好多下，但是毕竟各种乱七八糟的坑我都基本踩了个遍，所以我尽量写的清晰明白，让大家都能最方便快捷的训练自己的中文TTS。  

首先，第一步，肯定是上云，云会让大家成功率最高，少踩一些坑，也花不了几块钱；  

打开我们的国际标准炼丹平台AutoDL：https://www.autodl.com/

没注册的自己去链接注册去，我就不管了。

然后在西北A区租一台4090的机器。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtRiaicIPPbOrFibNbcE0jL3VT0R1puKAx72HpbygoTBpm280WZqbPhZWRw/640?wx_fmt=png&from=appmsg)

这里要注意一下，CPU型号别选AMD的，右边有一列叫“最高CUDA”，一定要大于11.8的，西北A区的一般都是12.0所以没啥问题，但是还是要留心一下，**CUDA版本小于11.8必报错。**  

然后在下方，选择社区镜像，就是别人已经做好的系统我们直接拿来用就行了。在输入框中输入Bert-Vits，就会自动联想出来一堆，**一定！一定！一定要选V11.1版本！！！要不然必报错！！！**  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtZCzSBAasicn43RNsVicHjw7ezFJxIZ810sSRRJW5wsYlOp6ytEiaicpNqw/640?wx_fmt=png&from=appmsg)

选完之后，我们就可以点击创建镜像。  

第一次创建镜像，可能会非常久，大概需要将近10分钟，不要急，耐心等等就好。

创建完成之后，点击JupyterLab进入系统。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtIRxwb4tSnk8PxcQcpjc2kyLCDDsLaSUF1ibic7rPlEnWGAnbHfOZlYibA/640?wx_fmt=png&from=appmsg)

进来后就会看到一大堆文字，不用管，直接往下滑，直到看到分割线页面，点击第一个代码块，然后点上方的三角按钮运行这个代码块。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdt0ktLrhq0iakiaLbbf98ux5tZSFExZia8ReibwZIjGhsH3nOicaicwjtM5wjA/640?wx_fmt=png&from=appmsg)

同时注意一下右上角这个圆圈的状态。  

实心圆则代表系统正在运行中，空心圆则代表上一步已经运行完成，目前系统空闲中。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtGmjKpDC8KwyKy2zqIFPgGwibsHEAVWVs2TlHl8yfMSwjqA0P0uFRJww/640?wx_fmt=png&from=appmsg)

所以只有当看到右上角圆圈是空心圆的时候，再去运行下面的代码块。  

第二个代码块比较重要，你可以先把这句话的speaker="Neuro" ，后面的这个Neuro改成你自己的名字，比如我就改成了speaker="Khazix"

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtx2CdkFmadfVq705rBGb6GG65Vg6Z9WK7VdcwuaIHxBWSCiaQ1EMuibhg/640?wx_fmt=png&from=appmsg)

改完以后，再点顶上的三角按钮运行。

后续的两个代码块，都不需要运行任何东西，跟着运行即可。但是记得右上角的圆圈状态一定要是空心圆再运行！  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtPAnQiaqp1hS43zBav7s0qBQjWLJQGEtdN48YBZOb9wqN64F6QYC2VeA/640?wx_fmt=png&from=appmsg)

这四步都运行完了之后，接下来就是数据集的上传与切割，我们大概需要半个小时到1个小时的纯人声说话的干声，一定要干声！尽量不要有任何杂音，这样效果才好。

同时注意你的口吻，最好是比较日常的、说话的，不要唱歌的、不要念课文的，要不然出来的效果也是稀奇古怪的朗读腔。

TTS大模型这种东西，90%的效果其实都跟原始数据集有密切的关系。  

数据集这块，我们一般都是需要处理成多段10~15秒的音频的，如果你没有切割过的话，你可以直接把你的文件传到autodl-tmp/workdir/audio-slicer/input这个文件夹里，然后自己直接在代码块点击后运行即可。

如果你是已经在本地用slicer-gui切过的同学，你就可以直接把数据集上传到autodl-tmp/workdir/auto-VITS-DataLabeling/raw\_audio这个路径下，直接拖进来就行。

就像这样，注意一下下面的蓝色的进度条就行，没传完别乱点。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtnqvaOekrqDPJBAnRGKwQF1Qrnen6Duq6diaU4b0tkINYJ5lyrAUibLbA/640?wx_fmt=png&from=appmsg)

传完以后，我们就要进行数据集的标注了。这两个代码块，连这运行就行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtRhjRzFQadVDdXGEaia8vDFCCdR0dGz8QiaWT8wibDQk537dURiadlQ3tag/640?wx_fmt=png&from=appmsg)

然后我们开始正儿八经的标注，继续运行代码块就行。数据集嘛，标注一下效果才好，你懂的。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtacqZvfeW7FJic7JsfKDUK05xibEQ1fQv5CokhCnMLZOrFiaoib4TIeJmHg/640?wx_fmt=png&from=appmsg)

这一步会有一点点久，毕竟得一条条语音识别出来。我1093条音频，大概花了9分钟，你们可以自己类推一下下~  

直到看到Done的提示，说明标注就完成啦。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoF2dkeQaDur4tmwzQyLdjVicw8UENiasDljqoDLs0jkk5WVQ5dU1RqKBhY9HNfViaJ0I0abRRD3ibib8w/640?wx_fmt=png&from=appmsg)

然后就是后面的5步，生成出各种东西，这5个代码块你也不需要改任何东西，看着右上角圆圈状态，无脑点击运行就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtmp9kiclWfx9PNr6YoV3ony29kGotoib5kxx3RToDm9UYTlFXjdAwsBTg/640?wx_fmt=png&from=appmsg)

每一步都运行完的提示大概长这样，你们可以对着验证一下：  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoF2dkeQaDur4tmwzQyLdjV6TG2yN3XnVetXf3sUILa6erula3V7scHAIeJOzI6aIuy26tqibNwZ8A/640?wx_fmt=png&from=appmsg)

最后，我们就要开始最后的一步！训练了！！！  

训练一共是3步，前两步还是跟之前一样，无脑点击就行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtWUAwJHcL4QXor6p1YI7aBFb4k7MBZ4MpwFWAnW4bLG5uZo8hOfVYjQ/640?wx_fmt=png&from=appmsg)

前两部运行完之后，等一等，停手！先别点第3步那个开始训练的代码块，而是返回顶部，找到我们最开始的speaker="Khazix"那个代码块，运行一下后，再回来开始训练！！！就是这个：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtIrYQSm1mbPBKtMibxOUp9mXtWGsTCDqGV4N2va6ZhpibUAlwu5mWybQA/640?wx_fmt=png&from=appmsg)

一定要，运行完以后，再回来开始训练！！要不然到时候报错了别来问我= =

OK，一切完毕，直接点击训练的那个代码块。如果你一切按我的来，从选机器开始，到最后的运行，基本是不会有BUG或者报错的，都能跑起来。你就能看到开始蠕动的进度条了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoF2dkeQaDur4tmwzQyLdjVibRXA3fn8bynpwriaANiaO9FJ1Y7Tt4BJCjicBSPsLuo5cFUZpoO6hTpFw/640?wx_fmt=png&from=appmsg)

等着就行，跟SVC类似，每1000步会在autodl-tmp/workdir/Bert-VITS2/Data这个文件夹里保存一个模型，我一般推荐4000步、5000步的模型可以听听效果了，没有大问题的话，就可以继续往后炼，10000步的模型差不多就可以用了，但是我还是推荐你10000步以后的每个保存下来的模型，都听一下，挑个最好的。

最后，模型差不多了，我们就要开始推理了~也就是真正的把文字转成语音了~推理我建议还是上云推理，本地推理要求最低也是8G显存，挺高的。。。像我这种垃圾3060想都不敢想。

推理第一步，先去改一下配置文件，因为这个项目比较新，所以用户体验不是特别好，大家忍耐一下，马上就完事了~  

我们在autodl-tmp/workdir/Bert-VITS2这个路径下，找到一个叫config.yml的文件。双击点开它。

找到105行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdt3paYTibqR7sUxjvrSqXfIzKicjRsMIChZvQibxxdyPVJPIkF67cd7Dqew/640?wx_fmt=png&from=appmsg)

把这行的路径model: "Data/maolei/models/G\_0.pth"，换成你自己的。

比如我的说话人最开始设的叫Khazix，现在我想用5000步的模型去做推理，那我就把这行改成：

model: "Data/**Khazix**/models/**G\_5000**.pth"

标红的这块就是需要你去修改的。改完以后，记得多按几下Ctrl+S保存。  

然后，保持在autodl-tmp/workdir/Bert-VITS2目录下，再点击右上角的+号，再点终端，进入命令行页面。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtx3ibQ810h8KenjQJMO7086z3JwUyiaVC3UgMaTNibf8v4uvYUmwJTDz8A/640?wx_fmt=png&from=appmsg)

输入代码：

    python webui.py

就会出来一串推理地址：  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtkb3QZZKdW5YED1u6vtg5OFEMKAaj9bGibTpfJdTOeW342iacG3sulN4g/640?wx_fmt=png&from=appmsg)

如果遇到报错，可以先把那边训练给停了，按顶上的方块停止按钮就行，下次再开是接着训练的，不影响。  

看到这个地址后，别直接点进去，会啥也看不到的，因为这是云机器的本地连接，所以我们要通过一些额外手段接进去。  

回到AutoDL的控制台首页，点击这个自定义服务，就可以进去了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtnp41UictVUftxwz1CUtRDicejAHtIfXufeaVz43w0W7MJxpGhOEajbMg/640?wx_fmt=png&from=appmsg)

然后，你就可以看到推理的WebUI了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtciaic92eFyq3uiaS3NLEVJhmFfUGHBySJ39s8eIKGJsBP6EqKx3QEibKicA/640?wx_fmt=png&from=appmsg)

在左上角正常输入你的文字内容就行。

有个有趣的东西是音频Prompt，你可以再传一段音频上去，把这段音频的风格作为Prompt，他就可以生成差不多效果的音频。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURrib21IzxJKwGomdO8ryxwdtv8JOWwUE6cCdXArGJsF4ibo6oVL3oibOeuvatnic8EqTymoXlRiblxF90w/640?wx_fmt=png&from=appmsg)

比如我传了一段峰哥8秒的说话切片作为参考，然后所有参数都不变，就生成了这么一段话。  

实在是太还原了，除了气口这个老大难问题，其他的都几乎一样，连峰哥语气词都还原出来了。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoF2dkeQaDur4tmwzQyLdjVibVV0ia0lQjkPNgKzmYWiaibjvTykOvG0yfo5gIjvCn93ENTqMsPjuicjkw/640?wx_fmt=png&from=appmsg)

下面的这些参数，其实只用看最后一个Length那个就行，那个是语速，有时候AI会贼快，所以可以适当的加大参数，参数越大越慢，另外三个最好别动，默认就行。

最后，你训练的模型如果要保存下来，记得去autodl-tmp/workdir/Bert-VITS2/Data/你的文件夹名字/models里，把三个模型下载下来，一定要保证后缀是一样的，下次直接传到同一个文件夹里，就可以继续推理了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURoF2dkeQaDur4tmwzQyLdjVt8X3zttYekHkpbyjTH7uEfIzNIYFQQteE7Ndv9I9vOQ15YUW8M2KnA/640?wx_fmt=png&from=appmsg)

以上，就是这一版Bert-Vits2中文特化版的全部用法。  

说实话，蹚坑挺累的，作为一个不懂技术的，我蹚坑真的蹚了好几个晚上，没有前路，只能自己把各种报错原因拿去跟GPT对话，然后研究怎么整。。。

但是好在，最后还是OK了。

希望，大家都能发挥出它的强大，用AI，真的去做一些有趣的事。

****以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。****

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言