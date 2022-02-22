# MOOC Automated
一个串行播放慕课的脚本。它会自动逐个播放全部视频，文字和考试维持不动。

选择题答案被发送给了前端，可以用开发者工具查看。

**声明：这个脚本只是用来熟悉`selenium`的使用。其存在和公开并不代表我曾经跳过了、或者鼓励任何人跳过任何必要的教学环节。**

## 准备工作
1. 安装 geckodriver + Firefox （或者Chrome + 对应的应用，然后修改相应代码）
2. `pip install -r requirements.txt`

## 使用过程
1. 运行 `main.py`，它会自动启动浏览器。
2. 微信扫码登录，打开相应课程，找到待播放的视频。
3. 打开你想要播放的第一个**视频**。（注意是视频，而不是文字/考试）
4. 关闭所有其他页面。
5. 给脚本发送回车。
6. 等待脚本退出。

## 你可能想问
- 为什么看起来没有动静了？
    - 为了适应各种不良网络环境（比如xx假日酒店只有**1MB/s**、还不是很稳定阴间网络），我配置了几秒的`implicit wait`。

- 那为什么不用`expected_conditions/WebDriverWait` ?
    - 我太菜了，用它们写出来的不太鲁棒，干脆暴力等待，反正自动播放也不耗使用者的时间 \doge.
    
- 为什么不能自动完成文本内容？
    - 因为我没能成功在”下一单元”元素上触发`click`事件。如果用url直接进入页面，它总会留在上一个状态没法出来。

## 为什么不并行
有一种显然的办法可以几乎瞬间看完全部慕课：打开所有视频，等1h，关闭浏览器。如果网络、内存足够，你的慕课完成了。现有一些这样的脚本。

对于并行播放，也许`***`是一个令人担忧的问题。