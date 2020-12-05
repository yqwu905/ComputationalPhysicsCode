# Hartree–Fock method
## BO近似与IB方法
对于未经近似的分子/原子体系,其Halmiltonian为:  
$$H = K_e+K_n+E_{ee} + E_{ne} + E_{nn}$$
其中,$K_e,K_n$分别为电子和核子的动能,$E_{ee},E_{ne},E_{nn}$分别为电子之间,电子与核子之间和核子之间的库伦势.明显的,对于拥有$N_e$个电子和$N_n$个核子的体系,其自由度为:  
$$f = 3(N_e+N_n)$$
明显的,对于这样的体系,是很难求解的,我们想要简化这样的体系.  
首先引入波恩-奥本海默近似(Born-Oppenheimer approximation):
> 在固体中,原子核保持不动,仅电子可以自由移动  

这样的假设显然是合理的,因为对氢原子来说,其原子核也比电子重了1800多倍.  
引入BO近似后,体系的Halmiltonian为:  
$$H_{BO} = K_e+E_{ee} + E_{ne}$$
$K_n$项的消失是显然的,而$K_{nn}$项的消失是由于在BO近似下,其为一个常数,因此可以通过改变参考点来使其为0.  
但是,引入BO近似后,体系自由度仍有:  
$$f_{BO} = 3N_e$$
主要的复杂度来源于第二项,即$E_{ee}$,电子之间的库伦势.为了消除这一复杂度,我们引入单个粒子假设(Independent Particle),IP假设下,Hamiltonian具有如下形式:  
$$H_{IP} = \sum_{i=1}^{N}\left[\frac{p_i^2}{2m} + V(\vec{r_i})\right]$$
$V(\vec{r_i})$通常情况下,是一个相当复杂的势函数.

## Example:Helium
现在我们来考虑氦原子, 其具有两个电子, 和一个电荷数为2的原子核, 显然的,这两个电子在基态下应该具有相同的轨道及相反的自旋.   
波函数可以写成:
$$\Psi(\vec{r_1},s_1,\vec{r_2},s_2) = \phi(\vec{r_1})\phi(\vec{r_2})\frac{1}{\sqrt{2}}\left[\alpha(s_1)\beta(s_2) - \alpha(s_2)\beta(s_1)\right]$$
考虑BO近似, 则系统的Halmiltonian算符应具有如下形式:  
$$H_{BO} = \sum_{i=1}^2 \frac{m_e}{2}\nabla_i^2 + \frac{1}{4\pi\epsilon_0}\left(\frac{1}{\left|\vec{r_1}-\vec{r_2}\right|}-\frac{2}{r_1} - \frac{2}{r_2}\right)$$
可以通过选择合适的单位制,来对上式进行简化:
$$H_{BO} = -\frac{1}{2} \nabla_{1}^{2}-\frac{1}{2} \nabla_{2}^{2}+\frac{1}{\left|\vec{r_1}-\vec{r_2}\right|}-\frac{2}{r_{1}}-\frac{2}{r_{2}}$$
可以发现,此情况下Halmitonian是不显含自旋$s_1,s_2$的, 因此我们可以直接将$\Psi$的含自旋部分先略去.  
$$H_{BO}\Psi = H_{BO}(\phi(\vec{r_1})\phi(\vec{r_2}))\cdot f(s_1,s_2) = E\phi(\vec{r_1})\phi(\vec{r_2})\cdot f$$
考虑我们实际上难以分辨这两个电子(虽然他们自旋不同), 但直觉上,我们更期待一个仅含$\vec{r_1}$(或$\vec{r_2}$)的方程. 对上式, 左乘$\phi^*(\vec{r_2})$, 并对$\vec{r_2}$作积分. 我们依次讨论各项:  
对于第1项:  
$$-\frac{1}{2}\nabla_1^2\phi(\vec{r_1})\int_{\Omega} \phi^*(\vec{r_2})\phi(\vec{r_2}) = -\frac{1}{2}\nabla_1^2\phi(\vec{r_1})$$
第二项:  
$$-\frac{1}{2}\phi(\vec{r_1})\int_{\Omega} \phi^*(\vec{r_2})\nabla_2^2\phi(\vec{r_2}) = C_1\phi(\vec{r_1})$$
第三项:  
$$\phi(\vec{r_1})\int_{\Omega}\frac{1}{\left|\vec{r_1}-\vec{r_2}\right|}$$
