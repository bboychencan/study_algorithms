# ESAb ATAd
这道题看了答案后觉得其实没有那么难，我当时已经很接近正确答案了。
可能是对codejam的难度不是很了解，同时对这个interactival的题目很不顺手，所以失败了。

我当时想的时候思路基本是一样的，在每个quantatum变换后的10次query内，可以用3次query来确定这个变换的类型，然后用剩下的query去查询剩下的bits。
但是问题是，我始终找不到合适的3个bits，我希望能找到两个对称的相同的bits和两个对称的不同的bits，但是有一点我的思路始终认为这两组bits应该是
相邻的。结果就导致我一直想不出来，觉得万一找不到这样的组合怎么办。。。

看了答案后觉得很巧妙，而我也离答案只有一步之遥。
1. 查询对称的bits的思路是对的，因为牵扯到reverse，需要对称检查
2. 当对称的两个bit相同时，虽然无法断定是4中变化中的某一种，但是可以排除其中两种！这个信息其实已经够用了
3. 总结一下，这里不能指望一下子拿到所有的信息，其实有时候部分信息也是有价值的，尤其是再尝试其他几组，然后把不完整的信息拼接起来就可以！

