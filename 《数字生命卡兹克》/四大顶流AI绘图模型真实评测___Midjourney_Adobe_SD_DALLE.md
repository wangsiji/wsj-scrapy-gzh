     四大顶流AI绘图模型真实评测 - Midjourney、Adobe、SD、DALLE \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

四大顶流AI绘图模型真实评测 - Midjourney、Adobe、SD、DALLE
==========================================

原创 数字生命卡兹克 数字生命卡兹克 2024-04-24 19:40 天津

> 原文地址: [https://mp.weixin.qq.com/s/kxaejpVZ86eUMXTVDvuwNw](https://mp.weixin.qq.com/s/kxaejpVZ86eUMXTVDvuwNw)

昨天，Adobe正式发布了他们新一代的AI绘图大模型：Adobe Firefly 3。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3R9nEQkZtL9C3xMsFKOYNDe9Kyr7YCs59E16DVndrRCpH32b4qY7McQ/640?wx_fmt=png&from=appmsg)

细节更强、语义理解更强、控制性更强等等。

还发了新一版本的PS AI。  

不过这些不是重点。

Adobe Firefly 3的发布，结合前段时间发布的SD3，让我有了再一次搞一个AI绘图大模型竞技场，评测一下的想法。

上一次做AI绘图的综合评测还在去年12月1号：

[四大巨头的AI绘图模型综合评测 - 写在Meta Imagine上线后](http://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&mid=2647660704&idx=1&sn=ab0b76c0986e30a3ac538fed0c701c75&chksm=f007c4f7c7704de12997ef48481b24e655b72894cf01db39f2332db3150d0c0c737215ab400a&scene=21#wechat_redirect)  

那时候Midjourney还没发V6，stability也没发SD3。

在现在这个节点，过了近半年的时候，来再看一下现在进化过的巨头们，已经达到了什么样的水平。

四家分别为：

Midjourney V6、Adobe Firefly 3、Stable Diffusion 3、Dalle 3。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3kOKVheGJ7dJnzFhbvicmibXFah3Uic87GVVeWEKPo3kEKhwpPeIA7XD8w/640?wx_fmt=jpeg&from=appmsg)

至于评测方式，我依然会从**细节质量、审美（构图色彩等）、语义理解**这三个维度来评测，剔除掉了风格多样化这个指标（没法测）。

细节质量、审美、语义理解每个类别14个case，总和42个Case（42这个数字的代表意义懂的都懂哈哈哈哈）

同时每个Prompt我会在AI绘图模型中roll3次出12张图，取效果最具有代表性的那个图，尽量减少偏见。同时为了保证公平，基本不会搞特别复杂的prompt。

同时，为了有最后整体可视化的评分让大家看着更直观，所以我会进行打分。在每个案例中，第一名为4分，第二为3分，第三为2分，最后一名为1分，最后计算平均分。

虽然每个case数量都不是很多，但是这也差不多了，而且是我个人的极限了。为了避免文章太长阅读体验极差，我就每个类别只放8个Case来做展示。  

OK，让我们开始吧。

  

 **一. 细节质量** 

主要测试AI绘图对于细节的表现能力，比如人物面部皮肤的质感、比如织物纹理的细节、场景细微元素的细节等等，这个是对模型精度和输出质量一个非常重要的考量。

1.Prompt：

Selfie of charming kpop girl, outdoors, evening time, brunette, casual giggle, 2 bun tied hairstyle

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc34cv3WRic0pzfhrsG4oicw8EnKnyhibaTBibJaMnJd6XmHPNibznAJmbOLVw/640?wx_fmt=jpeg)

Midjourney > SD3 > Adobe > Dalle

\-

2.Prompt： 

Portrait of a 2000s blonde woman posing on a sports car, white wired headphones, expressionless, 2000s hairstyle, 2000s fashion, sun rays, light teal and amber,Cinestill 50D

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3cBGoEAMCuvsCbuvNGuToy3GtF06ibicQTSoNm6DECTrtNTWatocNdiaeg/640?wx_fmt=jpeg&from=appmsg)

Midjourney > SD3 > Adobe > Dalle

\-

3.Prompt：

Photo of smiling Labrador wearing sunglasses and straw hat sitting on the beach bench with glass of cocktail, beach scene, realistic

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc37RDNf1ffiaicG7nj6cAz6ugOQqa0Ds1kpWhqntW0PibtJJrMX6A7eAeqw/640?wx_fmt=jpeg&from=appmsg)

Midjourney > SD3 > Adobe > Dalle

\-

4.Prompt：

a sports car drifting in a middle of partitions in a festival of vape and there is people around the car vaping, cinematic mood

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3ODO3JYPNibjkKjhfCPwT3wn23H8xKfANllzXC1ComDiaoL0HRvau1tpA/640?wx_fmt=jpeg&from=appmsg)

SD3 > Adobe > Midjourney > Dalle

\-

5.Prompt：

Realistic illustrations,The drumstick hits the frame and the drum bounces up water droplets

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3mfic71yEeWxiaydgYh4cFia7aFdN4qqW3n6T5RUMyx71rqCtstzL6Tp2w/640?wx_fmt=jpeg&from=appmsg)

Midjourney > Adobe > Dalle > SD3

\-  

6.Prompt：

a house design inside of the perfect beach house, rustic malibu in style, the beach and surf included in the photos, Photography

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3ibyQnlA45Aw3mXOblZic0iauLy0Oia83WuLHfx89TuJGEdJ2Teng1OicgJA/640?wx_fmt=jpeg&from=appmsg)

Midjourney > Adobe > SD3 > Dalle

\-  

7.Prompt：

beautiful blonde model made out of porcelain, long hair, wearing sci-fi light mecha armor, in the style of balanced symmetry, white and blue LED lights on armor

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3acmfyI2pqJDT4VNBMM06WqkNuYpd0lqpWjyefKHLHMm06icYMiafdVkQ/640?wx_fmt=jpeg&from=appmsg)

Midjourney > SD3 > Adobe > Dalle

\-

8.Prompt：

Delicious hamburger, floating in the air, food professional photography, studio lighting, studio background

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3HZNX2SxAOMiarc4yjfL2FOH6NPWg9gDeicFP7VFnBg1eMHMYIWpWo6TA/640?wx_fmt=jpeg&from=appmsg)

Midjourney > Adobe > SD3 > Dalle

\-  

剩下case略。

在细节质量部分，Midjourney基本以绝对的优势压倒性胜利。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3ic18rNoLJRynRuKBiaMfbyPNW6L3iaXLiaHLuemOzbQWhYjDn9247FqGvA/640?wx_fmt=png&from=appmsg)

  

 **二. 审美** 

主要测试AI绘图的审美能力，一张图好不好看，是美是丑，除了细节之外，更多的还需要看模型的审美能力，比如构图、色彩、光影等等，审美强，出的图才好看。

1.Prompt：

Creatures from the Book of Mountains and Seas of China, a golden alien tiger with a resting bird on its back, attack posture, with light and golden particles emitting in the air

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3nrNecV2FrqhSdjWPH3xcq7AVlTlNzsDEArX2iaqiaic5mTdeNgZgTuhBw/640?wx_fmt=jpeg&from=appmsg)

Midjourney > SD3 > Dalle \> Adobe

\-

2.Prompt：

A strong man riding a steel dragon flying in the sky, panorama, steel mecha, futuristic tech wind

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3yJSSx3DZ9qzMJWcxKoJxpIffQ4eXgGFEWJjSXOMBph2N5ibQaEWrs3w/640?wx_fmt=jpeg&from=appmsg)

Midjourney > Dalle > SD3 \> Adobe

\-

3.Prompt：

An abstract three-dimensional sculpture in the shape of an orchid, composed of gemstones and frosted viscous materials, in the style of tesseract, light-filled, sparkling water reflections, sunrays shine upon it

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3U363QPFSotKexxsibmNOQEwFjd65iba1B8IvTAwrjEH1woNJXchBg6vQ/640?wx_fmt=jpeg&from=appmsg)

Midjourney \> Adobe \> SD3 \> Dalle

\-

4.Prompt：

woman smiling and having a cup of 7-eleven coffee outside a 7-eleven convenience store in the morning in the style of 90's anime, 1990s anime texture and colors, thick line work

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3IppIVIRMnOrHFooZUsFcYt4MuibALic4EKOKrGPMIexIaLcduKGpnXhg/640?wx_fmt=jpeg&from=appmsg)

Midjourney > Dalle > SD3 \> Adobe

\-

5.Prompt：

fantasy greatsword made from crimson metal, oil painting

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc32m2DyLr6LGZicP2LDrVV5eVBwOx0EAfjqnkAq72ibgyIG0htxrUQZqzQ/640?wx_fmt=jpeg&from=appmsg)

Midjourney > SD3 > Dalle \> Adobe

\-

6.Prompt：

a dark ocean with great Sturm, Captive Souls Pirate's Redemption, ship emerging out of the fog, Giant octopus reaching out of the waters to pull down the ship

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3M56sPBdXoUe0494tTCK6ppZR7Vib61m3BkJ6WdbDibibNdwxJA2x9ziaaQ/640?wx_fmt=jpeg&from=appmsg)

Midjourney > Dalle > SD3 \> Adobe

\-

7.Prompt：

warhammer 40K, Islamic space marine, white armor, black and gold trim,  matte paintin

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3jM8Qc0JwnAlTGmD3sJ11dibzZOQ9ic7S8JElvsfiaJICygXicvHqlAgYFA/640?wx_fmt=jpeg&from=appmsg)

Midjourney > SD3 \> Adobe > Dalle

\-

8.Prompt：

oil painting of an angel with wings spread above the forest, light beam from its eyes illuminates path in bright green and blue colors

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3zJhnVsQAQnCrYCNwiaT6WzT4tlNdgUbj7CmgdmMILpq7znjqibdia0WqQ/640?wx_fmt=jpeg&from=appmsg)

Midjourney \> Adobe > SD3  > Dalle

\-

剩下case略。

在审美部分，Midjourney依然以绝对的优势压倒性胜利，而以设计起家的Adobe，反而拉了最大的跨。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3JAaPugUt35OWxOV2uNBTWpWwPGkWKeKNzvM7icib98uLyLmtvMknagUQ/640?wx_fmt=png&from=appmsg)

 **三. 语义理解** 

主要测试AI绘图对于复杂语义的理解能力，能否将文本内容都能清晰的表达出来并保证生成图片的质量。

1.Prompt：

Portrait photograph of an anthropomorphic tortoise seated on a New York City subway train

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3THx2ng6wFnWibj8MMYPBbDnQPcdBLhQEiaR7GhcJM1rWYoQxV9w5B3KA/640?wx_fmt=jpeg&from=appmsg)

Dalle > Midjourney > SD3 \> Adobe

\-

2.Prompt：

A businessman on a throne. The AI agents gathered behind him like royal guards. Photo Real

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3ukVABojADpp4AmicdTMoyXFNjwRpyRM6Ey5KUHricyB3tuM3h4SeiasOQ/640?wx_fmt=jpeg&from=appmsg)

Dalle > Midjourney > SD3 \> Adobe

\-

3.Prompt：

A cup of coffee sitting on a table in front of a window, outside the window is a futuristic city; a futuristic monorail can be seen close by, many lush plants around, shot from ground floor, clouds above

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3N0HxiaahKcWs2tp7Lapb8t9qE2uF5T0dDtKiaJDmL0IGtVH3KibS4wBLw/640?wx_fmt=jpeg&from=appmsg)

Dalle \> Adobe \> SD3 > Midjourney 

\-

4.Prompt：

A hyper-realistic image of an anthropomorphic corn cob working as a cashier at a convenience store, depicted with a cheerful expression while laughing. The corn cob, dressed in the store's uniform, features a friendly face with eyes and a mouth on the husk, showing a big, joyful smile. The scene captures the corn cob scanning items at the cash register, wearing a typical convenience store uniform that includes a neat polo shirt and a name tag

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3taGhjNU0Nulw0zxxCR4jicsUnglZTqwBFPvNKIVdGSznicoiapaGjCt1A/640?wx_fmt=jpeg&from=appmsg)

Dalle > Midjourney > SD3 \> Adobe

\-

5.Prompt：

Editorial photography of astronaut cooking Christmas colorful chocolate honey cookies on spaceship, Christmas honey cookies floating around astronaut, no gravity, in spaceship, levitated

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3mMWoj6kqvpR4ic6wcT3sVspHVSKbYS1jpTibdLeicNmAZvkx3X4GB8ia4Q/640?wx_fmt=jpeg&from=appmsg)

Dalle > Midjourney > SD3 \> Adobe

\-

6.Prompt：

a close up hyper realistic image of a medieval knight facing off against the grim reaper. Dramatic lighting

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc35960ovrd6qUz4ThayQ2uVh4H7KOFvib5rLgtiawKOicl3ITu3NBvOibWCg/640?wx_fmt=jpeg&from=appmsg)

Dalle = Midjourney > Adobe \> SD3

\-  

7.Prompt：

a very pretty young woman smilling flying over an aztec city with a dog, both the woman and the dog are flying, she is wearing an aztec outfit, the dog is wearing a colourful collar. they both seem to be having fun, ultra realistic

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3XvvB8BVNECZSlickfxSZ1MvbYukEKEJq8vUl5KiayvE5ue38AFPEic8ow/640?wx_fmt=jpeg&from=appmsg)

Dalle = Midjourney > Adobe \> SD3

\-

8.Prompt：

dungeons and dragons, high detailed, fantastic realism, female centaur with unicorn horn on head, hyper realistic

![](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3E2Ku2pYgj2GvkwXjPpbUQjMlb2OxX68SfcULOWwnPWT3ebObIghPaQ/640?wx_fmt=jpeg&from=appmsg)

Midjourney \> SD3 >  Dalle> Adobe

\-

剩下case略。

Dalle3和Midjourney基本上处于领先地位，Dalle还是领先一筹。Adobe继续垫底。  

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3vsE6dFC9NV1SiaRL2PT8QHjh8EebRSJdKw6bLDbS1GazjqnhF2621Pw/640?wx_fmt=png&from=appmsg)

  

 **最后总结** 

在四个大模型三个维度评完了以后，我相信大家应该能对这几个大模型有大概的了解了。

但是为了更直观一些，我再来做个雷达图吧。

![](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURo72ggc9dEIOGhrePbIoLc3Aocd7W2EmRt2bgos0tnInm4q1O02H5Rr3swO1LMetrFxaeQwcibSOeg/640?wx_fmt=png&from=appmsg)

细节质量方面，MJ V6 > SD3 > Adobe Fiefly 3 > Dalle 3。

审美方面，MJ V6 > SD3 >  Dalle 3 > Adobe Fiefly 3。

语义理解方面，Dalle 3 > MJ V6\> SD3 > Adobe Fiefly 3。

MJ依然稳坐头把交椅，很多人跟我说，啥XX大模型在什么什么参数评测中已经超越了MJ啥啥的，我每次都点点头：哦。

而Adobe Fiefly 3的全面拉胯以至于我几度怀疑自己是不是选错了模型，直到我再三确认我选的确实就是Fiefly  Image 3预览版。

就...拉胯的令人难以置信。

而SD3至少在我以API方式接入使用下，也没有很多自媒体或者其他人吹的那么神乎其神。

希望这个评测，能抛砖引玉吧，让大家对AI绘图综合有一些了解。

更建议的是，自己上手去试试。

又跑了十几个小时，虽然跟大家说的是只有42个Case，但是背后跑了不知道多少。希望能对大家有所帮助吧。  

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章。******

![](http://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURraibxGuHz6cfRAR74OFy6ib8iavRtmYufwwkQiczWlX1HRaicDTfBkQnZDdjM9PQibS2kh6gNt4gq20Vzw/0?wx_fmt=png) 数字生命卡兹克

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言