# K sorted list merge k 路归并

这个是一个非常经典且套路的问题，基本做法有若干种，如果熟悉了这些方法，在遇到类似的结构的时候就能够很快地有思路。

我在做*632. Smallest Range Covering Elements from K Lists* 的时候，我一个劲地想要用BIT和线段树往里套，可是百思不的其解，怎么也捋不出找出最有区间的方法，始终找不出一个结构来存储一个range，同时包含所有k个list的元素。
快要放弃的时候，我尝试先想出以每个元素为结尾的最小range的思路，从第一个元素开始，依次往后寻找到最近的一个满足包含所有k个list元素的range，然后用two pointer的思想，每次移动右边指针，同时check左边指针，移动到能满足条件的最小range，然后记录下最小range的值。

但是这种方法每次需要比较所有的k值，如果k值较大，那么复杂度较高。

看了讨论才发现，用heap的方法很巧妙，用k路归并的思想存储heap，heap可以记录当前遍历元素的最大值，同时每次弹出的元素即为当前最小值。 最最重要的一点，k路归并维护的heap可以保证每个list都至少有一个元素在heap里，这样就满足了题目的要求，即寻找最有range使得该range包含任意list至少一个元素。

所以总结一下，对k路归并不熟悉，导致遇到这个问题没能快速想到k路heap的这个结构。