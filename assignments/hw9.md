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
$$
E[S]=E[E[S|N]]=E[\sum_i^N X_i] =E[N \mu_x]=\mu_n \mu_x
$$
$$
Var[S]=E[S^2]-E[S]^2
$$
$$
E[S]^2=\mu_n^2\mu_x^2
$$
$$
E[S^2]=E[E[S^2|N]]=E[Var(S|N)+(E[S|N])^2]=\mu_n\sigma_x^2+\mu_n\mu_x
$$
$$
Var[S]=\mu_n\sigma_x^2+\mu_n\mu_x-\mu_n^2\mu_x^2
$$

4. 
$$
\begin{aligned}
\int_0^{\infty} \frac{\lambda^x}{x!}e^{-\lambda}\frac{\lambda_0^r}{\Gamma(r)}\lambda^{r-1}e^{-\lambda_0\lambda}d\lambda
&= \frac{\lambda_0^r \Gamma(r+x)}{x!\Gamma(r)(1+\lambda_0)^{x+r-1}} \\
&= {x+r-1 \choose x}(1-\lambda_0)^{x+r-1}\lambda_0^r
\end{aligned}
$$
Which is negative binomial distribution.

5. We know that $F_{Y_2}(y)=F(y)^n$ and $F_{Y_1}(y)=1-(1-F(y))^n$. Then $P(Y_1 \leq u, Y_2 \leq v)=F(v)^n - [F(v)-F(u)]^n$. So for $F(x;0, \theta)=\frac{x}{\theta}$, the join distribution is 
$$
(\frac{v}{\theta})^n-[\frac{v}{\theta}-\frac{u}{\theta}]^n
$$

6.
$$
P(X) = \int_0^{1} {n \choose x} \theta^X(1-\theta)^{n-x}\frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{B(\alpha, \beta)}d\theta = {n \choose x}\frac{B(\alpha+x,\beta+n-x)}{B(\alpha, \beta)}
$$
$$
\begin{aligned}
P(\theta|X) &= \frac{P(X|\theta)P(\theta)}{P(X)} \\
&= \frac{{n \choose x} \theta^x(1-\theta)^{n-x}\frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{B(\alpha, \beta)}}{{n \choose x}\frac{B(\alpha+x, \beta+n-x}{B(\alpha, \beta)}} \\
&= \frac{\theta^{x+\alpha-1}(1-\theta)^{\beta+n-x-1}}{B(\alpha+x,\beta+n-x)} \\
\implies P(\theta|X) &= \boxed{\text{Beta}(\alpha+x,\beta+n-x)}
\end{aligned}
$$

7. We have that $p(\mu) \propto \exp(-\frac{1}{2\sigma^2} (\mu^2-2\mu \mu_0))$. Then
$$
\begin{aligned}
p(\mu|x) &\propto p(x|\mu)p(\mu) \\
&\propto \exp(-\frac{1}{2\sigma^2}(\mu^2-2x\mu))\exp(-\frac{1}{2\sigma^2}(\mu^2-2\mu_0\mu)) \\
&= \exp(-\frac{1}{2\sigma^2}(\mu^2-2\mu(x+\mu_0))) \\
&\propto \text{N}(\mu, \sigma^2 | x+\mu_0)
\end{aligned}
$$
