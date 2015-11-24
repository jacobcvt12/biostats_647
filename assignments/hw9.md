---
title: "Homework 9"
author: "Jacob Carey"
date: \today
header-includes:
    - \usepackage{amsthm}
    - \usepackage{mathtools}
output: pdf_document
---

1. Let $X_n=o_p(1)$, $Y_n=O_p(\frac{1}{n})$ and $Z_n=X_n \times Y_n$. Then for all $\epsilon, \delta > 0$ there exist $N_1(\delta, \epsilon), N_2(\delta), K(\delta)$ such that $n > N_1(\delta, \epsilon) \implies P(|X_n| < \frac{\epsilon}{K(\delta)}) \geq 1-\delta$ and $n > N_2(\delta) \implies P(|Y_n| < \frac{K(\delta)}{n}) \geq 1-\delta$. Then set $N_3(\delta, \epsilon)=\max(N_1(\delta, \epsilon), N_2(\delta))$. We have that $|X_n||Y_n|=|X_nY_n| < \frac{\epsilon}{K(\delta)}\frac{K(\delta)}{n}$. Then for $n>N_3(\delta, \epsilon) \implies P(|X_nY_n| < \epsilon \frac{1}{n}) \geq 1-\delta$ and thus $o_p(1)O_p(1/n)=o_p(1/n)$.

2. Clearly, $\sqrt{n}(X_n-\mu) \xrightarrow{d} N(0, \sigma^2)$. For $g(x)=e^x$, it is differentiable everywhere. Then $\sqrt{n}(g(X_n)-g(\mu)) \xrightarrow{d} N(0, e^{2\mu} \sigma^2)$. Thus, $\sqrt{n}(g(X_n)) \xrightarrow{d} N(g(\mu) e^{2\mu} \sigma^2)$. Finally, $g(\bar{X}_n) \xrightarrow{d} N(g(\mu) \frac{e^{2\mu} \sigma^2}{n})$

3.

4. 
$$
\begin{aligned}
\int_0^{\infty} \frac{\lambda^x}{x!}e^{-\lambda}\frac{\lambda_0^r}{\Gamma(r)}\lambda^{r-1}e^{-\lambda_0\lambda}d\lambda
&= \frac{\lambda_0^r \Gamma(r+x)}{x!\Gamma(r)(1+\lambda_0)^{x+r-1}} \\
&= {x+r-1 \choose x}(1-\lambda_0)^{x+r-1}\lambda_0^r
\end{aligned}
$$
Which is negative binomial distribution.

5.

6.

7.