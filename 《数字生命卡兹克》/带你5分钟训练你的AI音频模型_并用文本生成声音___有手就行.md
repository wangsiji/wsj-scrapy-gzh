     带你5分钟训练你的AI音频模型，并用文本生成声音 - 有手就行 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

带你5分钟训练你的AI音频模型，并用文本生成声音 - 有手就行
===============================

原创 数字生命卡兹克 数字生命卡兹克 2023-05-10 22:46 天津

> 原文地址: [https://mp.weixin.qq.com/s/R2MzLphF-lPzHsdRlVj7Uw](https://mp.weixin.qq.com/s/R2MzLphF-lPzHsdRlVj7Uw)

在上一篇文章中，我推荐了一个SVC（Singing Voice Conversion）项目，歌声转换，也就是类似变声器的玩意，抽取一个人的声音作为训练数据，训练一个神经网络模型，学习他的声线；然后用模型在目标歌曲上做推理，即可实现用自己的声线唱目标歌曲：

[我把我的声音训练成了AI模型，并让它唱了一首歌...（附超全面教程，你奶奶看了都会用）](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647658355&idx=1&sn=0b1cec27677a8250585d43e0e69893a1&chksm=f007d324c7705a3296cf9bc19079e5f8378c0a183a5dc3c6e8db5228b839ca552459930efd39&scene=21#wechat_redirect)  

这个项目的质量确实极高，但是太硬核，太麻烦。  

**这篇文章，我想介绍一个有手就行的超级傻瓜的TTS（Text-to-Speech，文本生成音频）项目。**

微软、讯飞等等其实已经有非常成熟的TTS方案了，但是都是封装好的，没法去训练自己的声音（虽然他们有这个业务，但是普通人根本付不起那价格，就约等于没法训练）。

今天我们直接去训练自己的TTS，虽然效果略显粗糙，但是胜在有手就行，安心便捷。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhib7UDgx30iblIaAzzbNRHQOUVrkp4bPs3HGtpAcnmaYQsalYa7l5G4sw/640?wx_fmt=png)

百度飞浆平台上的PaddleSpeech项目，俗称有手就行。

步骤很简单：  

1.  准备数据集，十几段10秒以下的音频文件就可以。
    
2.  上飞浆平台租显卡，训练。
    
3.  TTS推理，完成。
    

**在开始玩之前，推荐大家去完成百度飞浆的新手任务，能白嫖100算力卡，等于100小时的V100 32G，25小时的A100 40G。属实是香的一笔。**

网址在此：https://aistudio.baidu.com/aistudio/newbie，也可以注册完在个人中心点左下角的新手礼包。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhWvJq7C9O7pzEH3mUEhXw7pJQxuZbJxwgSpf8pbCibP3MGYaOxVNVjaQ/640?wx_fmt=png)

极其简单的四步，几分钟就能搞定，约等于白给。  

拿到算力卡之后，我们进入飞浆的AI studio的项目大厅。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhel6XdUPktYqxVSTxlTo0iatMWiaJyviaEyf4qcVAtEwdXexcQgACf0X8A/640?wx_fmt=png)

**直接搜索四个字：语音合成。  
**

**第一个【有手就行】开头的那个就是。**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakh4rBicKGtRXRUeoKNHibSXUOS7990thEF2DmiaXiankeaghnEicrn6EsLiaAw/640?wx_fmt=png)

点进去，然后我们点击运行一下。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhdLYOz3wFRL0biccXHjuIMicicAibicTtSa66a2nAelKsdUBy59F4ColCic1Q/640?wx_fmt=png)

等个一小会，就完成了，弹出让我们选显卡的弹窗，**此处一定要注意，必须！必须选择V100 32G！！！必须！没有的话就刷新，直到刷到有为止！（不推荐A100是因为太贵了）**  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhrCElXfKRoeI3X7ReXm9qZnwbbpaIc5cmiauYDMTXoT3n3me34GCXkug/640?wx_fmt=png)

进入项目以后，我们就能看到这个项目详情，跟上一篇的SVC项目其实很类似，但是会大幅简化。我们啥也不用管，点顶部第二个小图标就行。全部运行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakh34x5nhHFV0orDbXKAaDDWe0Wfx0RTTZZZyb7RwPMQ9zxcn6DlYQSsQ/640?wx_fmt=png)

点完了以后，你就会发现自动滑到了安装环境的位置，它就突突突的自己开始装环境了，你就等着就行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakh7PBKMfUyCcDD3BHeavEAOoiaN7wI8dU49wJLavcXjx2W9aFK53DDyaA/640?wx_fmt=png)

当看到这句，运行时长和结束时间后，就说明环境装完了。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhibAhSeNuhDZGu5pe51qBDlmpleGiaTjvqehqDNRsZgbp50ac2NuiaQvww/640?wx_fmt=png)

我们继续下一步。在左侧找到文件 untitled.streamlit.py ，双击文件打开。然后找到红框位置图标，点击使用浏览器打开。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakh9RRUpKTrDA0EDdVLicjFdtOIDlpnAsARwR149iaChNQstIJKib6AP1IrQ/640?wx_fmt=png)

然后你就会在浏览器打开一个新的标签页，可能会白屏1分钟左右，别慌，等着就行。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhV77gn5BI2N3zkU1kz8mhycCcLmf3a9xq5yvEzeh6m7f0o6Wa1pZt8g/640?wx_fmt=png)

出现这个页面，就加载完成了，第一步当然是上传数据集啦，他们有几个要求，我给总结一下：  

1.  **优质干声，不要有杂音，一定不要有。  
    **
    
2.  **20段以上的2到9秒的wav格式音频。**
    
3.  **音频采样率必须在24000。**
    

要求其实不多，你完全可以用手机录一个3到5分钟的音频，然后转成24000采样率的wav格式，用上一篇的Audio Slicer（音频切分）去切出来。

这里转采样率和wav格式的我推荐一个在线免费网站：  

https://audio.online-convert.com/convert-to-wav

把音频传上去后，直接在这个位置改成24000采样率，然后start下载下来就行。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhgHF6RpLMS6AHnFqrA8lCQ5ZXJ32zkH2YQdfxEAxD1tFa9gvDy6AE9g/640?wx_fmt=png)

然后老规矩，跟上一篇一样，使用Audio Slicer（音频切分）去切音频，如果没有的话，关注我回复S，已经在整合包里了。

我们把Audio Slicer（音频切分）下载下来，解压后打开Slicer-gui。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpfC1RvIRlO2P2GllicqxRJCjRTqia1DFicLwJMMy3x3w38Xjn9RYNlibZjJYnPDicAgQjRwJoauBicib0yA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

然后把Minimun Length那一项改成8000，把我们需要处理的音频直接拖到左边窗口，在右下角选择输出路径。**同时此处注意，任何路径和文件命名，都一定不要带有中文和特殊的比如空格之类的字符！！！**

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpfC1RvIRlO2P2GllicqxRJCCiaCpTA8UzibU86v4ZoCQEvV8baZ7VeVibIoaN1bAAuIDYJqjCOqy27aA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

扔进去以后，我们直接点最右下角的Start。速度非常块，十几秒就切割完了。我们去我们选择的输出路径就能看到我们的文件。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpfC1RvIRlO2P2GllicqxRJCfhvxD5WLTbI4HLgrg3MEx7vyAfvZBF2rEAD2StVuxk2eGqrBuGRYTQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

然后我们选择时长排序，把低于2秒的，超过9秒的都给删了。数据集就算是处理完毕了~

回到我们的【有手就行】项目，我们把数据集上传上去。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhIXtOia2xSEO4EqHkuW6uN22fx28vdzlEdP4rMib61EmJEBic0KaUAkowQ/640?wx_fmt=png)

传完了后，我们校验一下数据集。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakh5OzrDF7X17m2pbmKOnxpW1v9ibWwWEIv9GhGxWoXb6h7fjhwnjiaI2Bg/640?wx_fmt=png)

校验完成以后，就会显示如下信息：

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhGksGQIVcsLWaEsvlmiaYdLbO16g8JuzNK9Hic1UUY661reGj5ibnGKUhg/640?wx_fmt=png)

我们就可以开始训练了，是不是比SVC简单太多了哈哈~  

这个训练只有1个参数，就是步数，100~20000的区间，基本可以理解为越高质量越好但是训练时间越长，他的速度非常快，**我的建议是先跑100步，看看模型有没有什么大问题，比如不是人声之类的，没大问题的话再上10000~20000步去跑。**

准备好了我们就直接微调训练，我这里先跑100步的。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakh6YloIGJKu5YfhsGibFKKz7SbRMg65VobOdjDftzpYWzC6dpdxGwDXAA/640?wx_fmt=png)

V100 32G跑起来很快，我30条数据集，100步基本2分钟就可以跑完~  

训练完成以后，直接点导出模型。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhSjeIYpU0np2icTbpjujDbq7Ficia2LqV8A7IOBGaicNsZs88yAxgfAI7RQ/640?wx_fmt=png)

导出完成以后，我们就可以在此处选择的自己的模型了~

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhdKJsJTeE1ltHp6cUJD7VyaiaiaZZBbrZoq86rv75ibtL1MibH42wkPiaW1w/640?wx_fmt=png)

选完了以后，就可以输入文本，然后点击合成，非常块，几秒钟就能合成完~

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURqdNgRxWc9AaF0EkeXxSiakhdY8n95EebFf3JUQf5UTqicRBZvaG34Owj7I7K2ged6ng37854iczVKYA/640?wx_fmt=png)

我们听听，效果没啥大问题的话，直接回去改步数，20000步走起~  

最后，不用项目的时候，别忘了停止哦~

  

**写在最后**

AI孙燕姿最近热火朝天，有越来越热的倾向。

也带着AI音频走向风口浪尖。

**AI虽好，但是绝对不要拿未经授权的声音去训练，绝对不要做涉及隐私走在灰色边缘的事情。**

以上，创作不易，有用的话请点个关注和在看，并给个星标，感恩。

  

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言