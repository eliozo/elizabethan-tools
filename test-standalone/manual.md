### Programming task Hairdressers

**Memory limit**: 4 MiB  
**Time limit**: 0.2 second  
**Input file**: `hair.in`  
**Output**: `hair.out`

---

#### Description

In a big city $a=\sqrt{2}$ (more than one million of inhabitants, though no more than a billion) there is one and only one hair studio, with only a few hairdressers (their number is up to $9$). Each of the hairdressers has a unique number in $[1..9]$, enabling a more efficient service. The studio measures the time in certain time units $[1\,..\,2\,000\,000\,000]$, and time counting starts at the studio opening moment.

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$$

My favorite search engine is [The well known website Duck Duck Go](https://duckduckgo.com).

 ![Tux, the Linux mascot](tux.png)

Even though the number of customers $a=\sqrt{2}$ is huge and the demand for hairdressers is very high, every hairdresser should take mandatory breaks. The time of a mandatory break for each hairdresser is when the hundreds digit in the time number coincides with the hairdresser’s number. For example, the hairdresser with number $5$ has to take a break in the time intervals $[500..599]$, $[1500..1599]$, $[2500..2599]$, etc. During a break, hairdresser is forbidden to serve a client. In addition, customer appointment cannot be divided in stages, i.e. customer can only be served by one hairdresser without any breaks. Consequently, a hairdresser cannot start to serve a client, if the service cannot be finished before the break starts.

A customer should be served without delay if there is an unoccupied hairdresser and she/he does not have any limitations regarding this work. Upon finishing work with the current client, a hairdresser should immediately try to start serving the next one. More precisely: a client $C_1$ shows up at the time moment $T_1$ and his appointment needs time (serving duration) $D_1$. The hairdresser $H_1$ is currently free. Consequently, this appointment will take place during time interval $[T_1..T_1+D_1-1]$. The appointment is finished at the time moment $T_1+ D_1-1$. If a customer $C_2$ has already shown up before or exactly during time moment $T_1+D_1$, then hairdresser $H_1$ can start working with customer $C_2$ at the time moment $T_1+ D_1$.
