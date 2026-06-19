# 两不动点距离比法：从定义到手动推导

这一页只讲一个原理：

$$
\frac{a_{n+1}-\alpha}{a_{n+1}-\beta}
=\lambda
\frac{a_n-\alpha}{a_n-\beta}.
$$

它不是一个需要背下来的公式，而是一次分式递推的结构事实。理解它以后，学生可以自己从头推出，不必依赖“老师说令这个”的记忆。

## 本页研究什么对象

我们研究的对象是由递推关系定义的数列：

$$
a_{n+1}=f(a_n),
$$

其中

$$
f(x)=\frac{px+A}{Bx+C}.
$$

这叫一次分式变换。它首先有定义条件：

$$
Bx+C\ne0.
$$

所以对数列来说，每一步都必须保证

$$
Ba_n+C\ne0.
$$

如果某一步分母为 0，原递推式本身就没有意义，后面的讨论不能继续。

## 定义：不动点

若数 $\alpha$ 满足

$$
f(\alpha)=\alpha,
$$

则称 $\alpha$ 是变换 $f$ 的不动点。

这句话的含义是：如果某一项刚好等于 $\alpha$，那么下一项仍然等于 $\alpha$：

$$
a_n=\alpha
\quad\Longrightarrow\quad
a_{n+1}=f(a_n)=f(\alpha)=\alpha.
$$

所以不动点是递推变换自己给出的稳定位置。它不是技巧的名字，而是这个变换的内在结构。

## 核心命题

设

$$
f(x)=\frac{px+A}{Bx+C}.
$$

若 $\alpha,\beta$ 是两个不同的不动点，即

$$
f(\alpha)=\alpha,\qquad f(\beta)=\beta,\qquad \alpha\ne\beta,
$$

并且相关分母都有意义，则存在常数 $\lambda$，使得

$$
\frac{f(x)-\alpha}{f(x)-\beta}
=\lambda
\frac{x-\alpha}{x-\beta}.
$$

把 $x$ 换成 $a_n$，就得到

$$
\frac{a_{n+1}-\alpha}{a_{n+1}-\beta}
=\lambda
\frac{a_n-\alpha}{a_n-\beta}.
$$

令

$$
b_n=\frac{a_n-\alpha}{a_n-\beta},
$$

则

$$
b_{n+1}=\lambda b_n.
$$

于是 $\{b_n\}$ 是等比数列。

## 为什么这个命题成立

下面完整推导，不跳步。

先从

$$
f(x)-\alpha
$$

开始。由 $f(x)=\frac{px+A}{Bx+C}$，

$$
f(x)-\alpha
=\frac{px+A}{Bx+C}-\alpha.
$$

通分：

$$
f(x)-\alpha
=\frac{px+A-\alpha(Bx+C)}{Bx+C}.
$$

展开分子：

$$
px+A-\alpha(Bx+C)
=(p-\alpha B)x+(A-\alpha C).
$$

现在要利用“不动点”这个条件。因为 $\alpha$ 是不动点，

$$
\alpha=\frac{p\alpha+A}{B\alpha+C}.
$$

在 $B\alpha+C\ne0$ 的条件下，两边同乘：

$$
\alpha(B\alpha+C)=p\alpha+A.
$$

展开：

$$
B\alpha^2+\alpha C=p\alpha+A.
$$

移项得到

$$
A-\alpha C=B\alpha^2-p\alpha.
$$

右边可以提取 $-\alpha$：

$$
B\alpha^2-p\alpha
=-\alpha(p-\alpha B).
$$

所以

$$
A-\alpha C=-\alpha(p-\alpha B).
$$

把它代回分子：

$$
(p-\alpha B)x+(A-\alpha C)
=(p-\alpha B)x-\alpha(p-\alpha B).
$$

提取公因式：

$$
(p-\alpha B)x-\alpha(p-\alpha B)
=(p-\alpha B)(x-\alpha).
$$

因此

$$
f(x)-\alpha
=\frac{(p-\alpha B)(x-\alpha)}{Bx+C}.
$$

同理，由 $\beta$ 是不动点可得

$$
f(x)-\beta
=\frac{(p-\beta B)(x-\beta)}{Bx+C}.
$$

两式相除：

$$
\frac{f(x)-\alpha}{f(x)-\beta}
=
\frac{\frac{(p-\alpha B)(x-\alpha)}{Bx+C}}
{\frac{(p-\beta B)(x-\beta)}{Bx+C}}.
$$

公共分母 $Bx+C$ 抵消：

$$
\frac{f(x)-\alpha}{f(x)-\beta}
=
\frac{p-\alpha B}{p-\beta B}
\cdot
\frac{x-\alpha}{x-\beta}.
$$

所以

$$
\lambda=\frac{p-\alpha B}{p-\beta B}.
$$

这就是两不动点距离比法的来源。

## 这个新变量到底在表示什么

新变量

$$
b_n=\frac{a_n-\alpha}{a_n-\beta}
$$

不是为了凑公式。它表示的是：$a_n$ 到两个不动点 $\alpha,\beta$ 的有向距离之比。

一次分式变换的特点是：它不会简单地把每个距离都变成常数倍，但它会把“到两个不动点的距离之比”变成常数倍。

这就是为什么单看 $a_n-\alpha$ 往往不够，而要看

$$
\frac{a_n-\alpha}{a_n-\beta}.
$$

## 手动推导流程

遇到

$$
a_{n+1}=\frac{pa_n+A}{Ba_n+C}
$$

时，按下面步骤手动推导。

### 第一步：写出变换和定义域

令

$$
f(x)=\frac{px+A}{Bx+C}.
$$

先记下

$$
Bx+C\ne0.
$$

对数列就是

$$
Ba_n+C\ne0.
$$

### 第二步：求不动点

解

$$
x=f(x).
$$

也就是

$$
x=\frac{px+A}{Bx+C}.
$$

在 $Bx+C\ne0$ 的条件下同乘：

$$
x(Bx+C)=px+A.
$$

整理成二次方程。若得到两个不同根 $\alpha,\beta$，就可以考虑距离比法。

### 第三步：先讨论特殊初值

如果

$$
a_1=\alpha,
$$

那么

$$
a_n=\alpha.
$$

如果

$$
a_1=\beta,
$$

那么

$$
a_n=\beta.
$$

这些常值情形要先处理，否则后面构造分式时可能出现分母为 0。

### 第四步：构造距离比

在 $a_n\ne\beta$ 的情形下，令

$$
b_n=\frac{a_n-\alpha}{a_n-\beta}.
$$

由核心命题可得

$$
b_{n+1}=\lambda b_n.
$$

因此

$$
b_n=b_1\lambda^{n-1}.
$$

### 第五步：把 $b_n$ 解回 $a_n$

设

$$
b_n=t_n.
$$

则

$$
\frac{a_n-\alpha}{a_n-\beta}=t_n.
$$

两边同乘：

$$
a_n-\alpha=t_n(a_n-\beta).
$$

展开：

$$
a_n-\alpha=t_na_n-t_n\beta.
$$

把含 $a_n$ 的项放在一边：

$$
a_n-t_na_n=\alpha-t_n\beta.
$$

提取 $a_n$：

$$
(1-t_n)a_n=\alpha-t_n\beta.
$$

所以

$$
a_n=\frac{\alpha-t_n\beta}{1-t_n}.
$$

最后检查初值和原递推分母。

## 完整例题

已知

$$
a_1=4,\qquad a_{n+1}=\frac{5a_n-4}{2a_n-1}.
$$

求 $a_n$。

### 1. 写出变换

$$
f(x)=\frac{5x-4}{2x-1}.
$$

定义条件是

$$
2x-1\ne0.
$$

### 2. 求不动点

解

$$
x=\frac{5x-4}{2x-1}.
$$

同乘：

$$
x(2x-1)=5x-4.
$$

展开：

$$
2x^2-x=5x-4.
$$

整理：

$$
2x^2-6x+4=0.
$$

两边除以 2：

$$
x^2-3x+2=0.
$$

因式分解：

$$
(x-1)(x-2)=0.
$$

所以两个不动点为

$$
1,\quad 2.
$$

这里 $a_1=4$，不是不动点，所以不是常值数列。

### 3. 构造距离比

取

$$
\alpha=2,\qquad \beta=1.
$$

令

$$
b_n=\frac{a_n-2}{a_n-1}.
$$

下面手动验证 $b_{n+1}$ 与 $b_n$ 的关系。

先算分子：

$$
a_{n+1}-2
=\frac{5a_n-4}{2a_n-1}-2.
$$

通分：

$$
a_{n+1}-2
=\frac{5a_n-4-2(2a_n-1)}{2a_n-1}.
$$

展开：

$$
a_{n+1}-2
=\frac{5a_n-4-4a_n+2}{2a_n-1}
=\frac{a_n-2}{2a_n-1}.
$$

再算分母：

$$
a_{n+1}-1
=\frac{5a_n-4}{2a_n-1}-1.
$$

通分：

$$
a_{n+1}-1
=\frac{5a_n-4-(2a_n-1)}{2a_n-1}.
$$

展开：

$$
a_{n+1}-1
=\frac{3a_n-3}{2a_n-1}
=\frac{3(a_n-1)}{2a_n-1}.
$$

所以

$$
b_{n+1}
=\frac{a_{n+1}-2}{a_{n+1}-1}
=
\frac{\frac{a_n-2}{2a_n-1}}
{\frac{3(a_n-1)}{2a_n-1}}.
$$

抵消公共分母：

$$
b_{n+1}
=\frac13\frac{a_n-2}{a_n-1}
=\frac13b_n.
$$

### 4. 求出 $b_n$

因为

$$
b_1=\frac{4-2}{4-1}=\frac23,
$$

所以

$$
b_n=\frac23\left(\frac13\right)^{n-1}
=\frac2{3^n}.
$$

### 5. 解回 $a_n$

由

$$
\frac{a_n-2}{a_n-1}=\frac2{3^n},
$$

两边同乘：

$$
3^n(a_n-2)=2(a_n-1).
$$

展开：

$$
3^na_n-2\cdot3^n=2a_n-2.
$$

移项：

$$
(3^n-2)a_n=2\cdot3^n-2.
$$

所以

$$
a_n=\frac{2\cdot3^n-2}{3^n-2}.
$$

### 6. 检查

当 $n=1$ 时，

$$
a_1=\frac{2\cdot3-2}{3-2}=4,
$$

符合初值。并且对这个结果，$2a_n-1$ 不为 0，原递推分母有意义。

## 和“平移后取倒数法”的关系

两不动点距离比法和平移后取倒数法不是两件互不相关的事。

设 $\alpha,\beta$ 是两个不动点。令

$$
B_n=a_n-\alpha.
$$

那么

$$
a_n-\beta=B_n+\alpha-\beta.
$$

距离比法写成

$$
\frac{B_{n+1}}{B_{n+1}+\alpha-\beta}
=\lambda
\frac{B_n}{B_n+\alpha-\beta}.
$$

设

$$
d=\alpha-\beta.
$$

则

$$
\frac{B_{n+1}}{B_{n+1}+d}
=\lambda
\frac{B_n}{B_n+d}.
$$

两边交叉相乘：

$$
B_{n+1}(B_n+d)=\lambda B_n(B_{n+1}+d).
$$

展开：

$$
B_nB_{n+1}+dB_{n+1}
=\lambda B_nB_{n+1}+\lambda dB_n.
$$

移项：

$$
(1-\lambda)B_nB_{n+1}+dB_{n+1}-\lambda dB_n=0.
$$

若 $B_nB_{n+1}\ne0$，两边除以 $B_nB_{n+1}$：

$$
(1-\lambda)+\frac d{B_n}-\frac{\lambda d}{B_{n+1}}=0.
$$

令

$$
C_n=\frac1{B_n},
$$

就得到

$$
C_{n+1}
=\frac1\lambda C_n+\frac{1-\lambda}{\lambda d}.
$$

这就是一次线性递推。也就是说，平移后取倒数法可以看成两不动点距离比法的另一种书写方式。

## 边界条件

使用本方法时必须检查：

1. 原递推分母是否可能为 0。
2. 求不动点时同乘的分母是否为 0。
3. 两个不动点是否真的不同。
4. 初值是否正好等于某个不动点。
5. 构造 $\frac{a_n-\alpha}{a_n-\beta}$ 时，是否出现 $a_n=\beta$。
6. 解回 $a_n$ 后，是否满足初值和原递推。

## 学生讲题问题

学生讲这一页时，不要求背公式，要求能回答：

1. 什么是不动点？
2. 为什么递推题里要找不动点？
3. 为什么看一个距离不够，而要看两个距离的比？
4. 核心等式
   $$
   f(x)-\alpha
   =\frac{(p-\alpha B)(x-\alpha)}{Bx+C}
   $$
   是怎么推出来的？
5. 为什么 $\{b_n\}$ 会成为等比数列？
6. 最后如何从 $b_n$ 解回 $a_n$？
7. 哪些分母不能为 0？

如果这些问题能讲清楚，才说明她不是在照搬，而是在理解这个方法。
