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

2.

3.

4.

5.

6.

7.

8.
