# Time Dilation as Conservation of Informational Bandwidth: Explaining Relativistic and Gravitational Clock Retardation via Finite Quantum Processing Capacity

**Author:** Stefan Hertel  
**Affiliation:** Independent Researcher  
**Date:** October 15, 2026  
**Document Type:** Theoretical Research Treatise & Foundational Mechanics Synthesis  
**Key Literature Analyzed:**
- Einstein, A. (1905). "Zur Elektrodynamik bewegter Körper." *Annalen der Physik*, 17(10), 891–921.
- Margolus, N., & Levitin, L. B. (1998). "The maximum speed of dynamical evolution." *Physica D: Nonlinear Phenomena*, 120(1-2), 188–195.
- Mandelstam, L., & Tamm, I. (1945). "The uncertainty relation between energy and time in non-relativistic quantum mechanics." *J. Phys. (USSR)*, 9, 249–254.
- Page, D. N., & Wootters, W. K. (1983). "Evolution without evolution: Dynamics described by stationary observables." *Physical Review D*, 27(12), 2885–2892.
- Rossi, B., & Hall, D. B. (1941). "Variation of the Rate of Decay of Mesotrons with Momentum." *Physical Review*, 59(3), 223–228.
- Hafele, J. C., & Keating, R. E. (1972). "Around-the-World Atomic Clocks: Predicted Relativistic Time Gains." *Science*, 177(4044), 166–168.

---

## 1. The Core Physical Problem & Intuition

For over a century since the publication of Special Relativity in 1905, time dilation has been presented as an axiomatic consequence of the Lorentz transformation:
$$\Delta t = \gamma \Delta \tau = \frac{\Delta \tau}{\sqrt{1 - \frac{v^2}{c^2}}}.$$

While mathematically watertight within the pseudo-Riemannian metric formulation, this standard textbook presentation leaves the underlying physical mechanism mysterious:
- **Why does physical motion through space retard internal temporal progression?**
- **Why do all physical clocks—from subatomic muons and cesium atomic fountains to biological human cells—slow down by the exact same Lorentz factor $\gamma$?**
- **What physical resource is being consumed when an object moves faster through space?**

Here, we formulate the exact answer within the **Speed of Information ($c_{\mathcal{I}}$)** paradigm proposed by Stefan Hertel:

$$\boxed{\begin{array}{l}
\textbf{Time dilation is the direct physical consequence of finite Informational Bandwidth.} \\
\textbf{Every physical entity moves through the 4D causal network at the single invariant speed } c_{\mathcal{I}}\textbf{.} \\
\textbf{Spatial motion diverts informational update bandwidth away from internal state transitions.} \\
\textbf{Clocks tick slower because less informational processing capacity remains for internal change.}
\end{array}}$$

---

## 2. Operational Clock Definition & The Quantum Speed Limit

In operational physics, time is not an invisible flowing river; time is **measured strictly by the state transitions of physical systems**.

### 2.1 The Operational Clock
Consider an arbitrary physical clock $\mathcal{C}$. To advance its dial by one unit (a "tick" $\Delta \tau$), the clock's quantum state $|\psi(0)\rangle$ must evolve into an orthogonal, distinguishable state $|\psi(\Delta \tau)\rangle$:
$$\langle \psi(0) | \psi(\Delta \tau) \rangle = 0.$$

By the fundamental **Mandelstam-Tamm (1945)** and **Margolus-Levitin (1998)** theorems of quantum information theory, the minimum time $\tau_{\text{QSL}}$ required for any quantum system with mean interaction energy $E_0$ and energy variance $\Delta E$ to transition between mutually orthogonal states is bounded by the **Quantum Speed Limit (QSL)**:
$$\tau_{\text{tick}} \ge \max\left( \frac{\pi \hbar}{2 \Delta E}, \frac{\pi \hbar}{4 E_0} \right) \equiv \frac{1}{\nu_0},$$
where $\nu_0$ is the maximal internal clock frequency in the system's rest frame.

Every physical clock—whether an oscillating cesium atom, a decaying radioactive nucleus, an electronic circuit, or a biological cell—is a quantum information engine whose operational tick rate is strictly bounded by the rate at which internal bits of quantum information can be processed.

---

## 3. The Law of Conservation of Informational Bandwidth

In the relational spacetime framework, spacetime metric geometry is an informational manifold. The 4-velocity of any physical system of rest mass $m > 0$ satisfies the universal timelike normalization condition:
$$u^\mu u_\mu = g_{\mu\nu} \frac{dx^\mu}{d\tau} \frac{dx^\nu}{d\tau} = -c_{\mathcal{I}}^2.$$

Expressed in coordinate time $t$ of an arbitrary inertial laboratory observer:
$$-c_{\mathcal{I}}^2 \left(\frac{d\tau}{dt}\right)^2 + \left(\frac{d\mathbf{x}}{dt}\right)^2 = -c_{\mathcal{I}}^2.$$

Dividing through by the invariant speed of information $c_{\mathcal{I}}^2$ yields the fundamental **Law of Informational Bandwidth Conservation**:

$$\boxed{\left(\frac{d\tau}{dt}\right)^2 + \frac{v^2}{c_{\mathcal{I}}^2} = 1},$$
where $v = \|d\mathbf{x}/dt\|$ is the physical velocity through space.

```
                      THE INFORMATIONAL BANDWIDTH QUARTER-CIRCLE
                      
        Internal Clock Rate (dτ/dt)
                     ▲
                1.00 ┼ (v = 0: 100% Internal Clock Bandwidth)
                     │ *
                     │   *
                     │     *
                0.866┼───────* (v = 0.500 c_I: 86.6% Clock Rate)
                     │        \
                     │         *
                0.500┼──────────* (v = 0.866 c_I, γ = 2.0: 50% Clock Rate)
                     │           \
                     │            *
                0.063┼─────────────* (v = 0.998 c_I, Cosmic Muon: 6.3% Clock Rate)
                     │              *
                0.00 ┼───────────────┴────► Spatial Velocity (v / c_I)
                    0.00            1.00 (v = c_I: 0% Internal Bandwidth, Time Stops)
```

### 3.1 Physical Interpretation of the Bandwidth Law
The equation $(d\tau/dt)^2 + (v/c_{\mathcal{I}})^2 = 1$ demonstrates that the total rate of information processing is an invariant circle of radius $1.0$:

1. **At Rest ($v = 0$):**  
   The entire informational bandwidth of the system ($100\%$) is available for internal state evolution:
   $$\frac{d\tau}{dt} = 1.0 \implies \nu(v) = \nu_0.$$
   The clock ticks at its full natural rest frequency.

2. **In Motion ($0 < v < c_{\mathcal{I}}$):**  
   The system must divert a fraction $(v/c_{\mathcal{I}})^2$ of its total informational capacity into updating its spatial coordinates relative to the surrounding causal diamond.  
   Consequently, the remaining bandwidth available for internal quantum state transitions is strictly reduced:
   $$\boxed{\frac{d\tau}{dt} = \sqrt{1 - \frac{v^2}{c_{\mathcal{I}}^2}} = \frac{1}{\gamma(v)}}.$$

3. **At the Luminal Limit ($v \to c_{\mathcal{I}}$):**  
   All available informational bandwidth is consumed by spatial translation ($v^2/c_{\mathcal{I}}^2 = 1.0$). Exactly **zero bandwidth remains for internal state changes**:
   $$\frac{d\tau}{dt} = 0 \implies \tau \equiv \text{constant}.$$
   All internal physical processes, oscillations, and decays are completely frozen.

4. **Massless Carriers ($\gamma \to \infty$, $v = c_{\mathcal{I}}$):**  
   Photons, gravitons, and other massless excitations carry zero rest frame clock capacity ($d\tau = 0$). From their own frame, emission and absorption are simultaneous; they are pure messengers dedicated $100\%$ to external spatial information transfer.

---

## 4. Microscopic Mechanism: Internal Causal Loops & Force Mediation Delay

Why do *all* composite physical systems—regardless of their chemical or nuclear composition—slow down by the exact same factor $\gamma$?

Every stable particle, atom, molecule, or living organism is a composite system bound together by internal gauge force carriers (virtual photons, gluons, W/Z bosons) that propagate at the invariant speed $c_{\mathcal{I}}$.

### 4.1 The Elementary Causal Loop
Consider an atomic system of characteristic internal diameter $L$. For the atom to maintain structural integrity and execute internal transitions, quantum state information must cycle between its components (e.g., between atomic nucleus and electron orbitals):

```
       REST FRAME (v = 0)                   LAB FRAME (v > 0)
       ──────────────────                   ─────────────────
          (E) Electron                         (E)                (E) Electron
           ▲                                  /                  /
           │                                 /                  /
       L   │ c_I                       c_I  /                  / c_I
           │                               /                  /
           ▼                              ▼                  /
          (N) Nucleus                    (N)───────────────(N) Nucleus
                                                v · Δt
          Round-trip path: 2L            Hypotenuse path: 2√(L² + (vΔt/2)²)
          Proper period: Δτ = 2L / c_I   Lab period: Δt = 2L / √(c_I² - v²) = γ · Δτ
```

1. **In the Rest Frame:**  
   The round-trip distance for internal state coordination is $s_0 = 2L$. The proper cycle period is:
   $$\Delta \tau = \frac{2L}{c_{\mathcal{I}}}.$$

2. **In the Moving Frame (Velocity $v$):**  
   While internal information is traveling between components, the system translates forward by distance $\Delta x = v \Delta t$.  
   The signal packet must therefore travel along the diagonal hypotenuse of a right triangle with base $v \Delta t / 2$ and height $L$:
   $$d_{\text{hypotenuse}} = \sqrt{L^2 + \left(\frac{v \Delta t}{2}\right)^2}.$$

3. **Invariant Speed along the Hypotenuse:**  
   Because information cannot travel faster than $c_{\mathcal{I}}$ along any path, the time required for the internal cycle in the laboratory frame satisfies:
   $$c_{\mathcal{I}} \left(\frac{\Delta t}{2}\right) = \sqrt{L^2 + \left(\frac{v \Delta t}{2}\right)^2}.$$

4. **Solving for $\Delta t$:**  
   $$c_{\mathcal{I}}^2 \left(\frac{\Delta t}{2}\right)^2 = L^2 + v^2 \left(\frac{\Delta t}{2}\right)^2 \implies \left(c_{\mathcal{I}}^2 - v^2\right) \left(\frac{\Delta t}{2}\right)^2 = L^2,$$
   $$\frac{\Delta t}{2} = \frac{L}{\sqrt{c_{\mathcal{I}}^2 - v^2}} = \frac{L}{c_{\mathcal{I}} \sqrt{1 - \frac{v^2}{c_{\mathcal{I}}^2}}},$$
   $$\boxed{\Delta t = \frac{2L / c_{\mathcal{I}}}{\sqrt{1 - \frac{v^2}{c_{\mathcal{I}}^2}}} = \gamma(v) \Delta \tau}.$$

Because **every internal force holding matter together is mediated at speed $c_{\mathcal{I}}$**, moving through space physically stretches the causal paths between interacting particles. Every atomic vibration, molecular reaction, and radioactive decay takes longer by the factor $\gamma$ because the internal exchange of coordinating information must traverse longer spatial paths.

---

## 5. Experimental Verification: Cosmic Muons and Atomic Clocks

This informational bandwidth trade-off is one of the most thoroughly confirmed facts in empirical physics:

### 5.1 Atmospheric Cosmic Ray Muons (Rossi & Hall 1941)
- **Rest Lifetime:** Muons at rest decay via the weak interaction with a mean lifetime $\tau_0 \approx 2.197\text{ }\mu\text{s}$.
- **Classical Vacuum Travel Distance:** Even traveling near $c_{\mathcal{I}}$, a muon without time dilation could travel at most:
  $$d_{\text{classical}} \approx c_{\mathcal{I}} \tau_0 = (3.0 \times 10^8\text{ m/s}) \times (2.2 \times 10^{-6}\text{ s}) \approx 660\text{ meters}.$$
- **Physical Reality:** Muons produced by cosmic rays in the upper atmosphere at altitudes of $h \approx 15\text{ km}$ easily reach surface detectors in vast numbers.
- **Informational Resolution:** At velocity $v = 0.998\,c_{\mathcal{I}}$, the muon diverts $99.6\%$ of its informational capacity into spatial translation. Only $6.3\%$ remains for internal decay channel evolution:
  $$\frac{d\tau}{dt} = \sqrt{1 - (0.998)^2} \approx 0.0632 \implies \gamma \approx 15.82.$$
  Its laboratory lifetime is dilated to:
  $$\Delta t_{\text{lab}} = \gamma \tau_0 \approx 15.82 \times 2.197\text{ }\mu\text{s} \approx 34.75\text{ }\mu\text{s}.$$
  The physical travel range becomes:
  $$d_{\text{dilated}} = v \Delta t_{\text{lab}} \approx (0.998 c_{\mathcal{I}}) \times (34.75\text{ }\mu\text{s}) \approx 10.4\text{ km},$$
  permitting the muons to survive the atmospheric descent and trigger detectors on Earth.

### 5.2 Global Positioning System (GPS) Kinematic Retardation
- GPS satellites orbit Earth at orbital speed $v_{\text{orbit}} \approx 3.874\text{ km/s} \approx 1.29 \times 10^{-5}\,c_{\mathcal{I}}$.
- The kinematic bandwidth diversion factor is:
  $$\frac{d\tau}{dt} \approx 1 - \frac{1}{2}\left(\frac{v}{c_{\mathcal{I}}}\right)^2 = 1 - 8.35 \times 10^{-11}.$$
- Over one day ($86,400\text{ s}$), moving atomic clocks lose:
  $$\Delta t_{\text{kinematic}} = -8.35 \times 10^{-11} \times 86,400\text{ s} \approx -7.21\text{ }\mu\text{s/day}.$$
  Without accounting for this informational bandwidth deficit, GPS navigation positions would drift by over $2.1\text{ km}$ per day.

---

## 6. Gravitational Time Dilation as Horizon Channel Capacity

The Speed of Information framework applies identically to General Relativity: **gravitational time dilation is the reduction in classical and quantum channel capacity caused by spacetime curvature.**

### 6.1 The Gravitational Metric as an Informational Redshift
In a static, spherically symmetric gravitational field of mass $M$ (Schwarzschild geometry), the invariant line element is:
$$ds^2 = -c_{\mathcal{I}}^2 d\tau^2 = -\left(1 - \frac{2GM}{r c_{\mathcal{I}}^2}\right) c_{\mathcal{I}}^2 dt^2 + \left(1 - \frac{2GM}{r c_{\mathcal{I}}^2}\right)^{-1} dr^2 + r^2 d\Omega^2.$$

For a clock stationed at constant radius $r$ ($dr = d\theta = d\phi = 0$):
$$\boxed{\frac{d\tau}{dt} = \sqrt{-g_{00}(r)} = \sqrt{1 - \frac{r_s}{r}}}, \quad r_s \equiv \frac{2GM}{c_{\mathcal{I}}^2}.$$

### 6.2 Channel Capacity to Infinity
To an observer at asymptotic infinity ($r \to \infty$), the rate at which bits of state information can be transmitted outward from radius $r$ is:
$$\mathcal{C}(r) = \mathcal{C}_\infty \sqrt{1 - \frac{r_s}{r}}.$$

- **Near Weak Fields (Earth's Surface):**  
  At $r \approx 6.371 \times 10^6\text{ m}$, the gravitational potential creates a slight blue-shift relative to orbit ($\Delta \tau / dt \approx 1 - GM / (rc_{\mathcal{I}}^2)$), adding $+45.8\text{ }\mu\text{s/day}$ to GPS clocks.
- **At the Schwarzschild Horizon ($r \to r_s$):**  
  $$\lim_{r \to r_s} \mathcal{C}(r) = 0, \quad \lim_{r \to r_s} \frac{d\tau}{dt} = 0.$$
  The event horizon is a **surface of strictly zero outgoing channel capacity**. An outside observer never sees an infalling clock tick past the horizon not because the clock breaks, but because zero bits of state transition can escape across the horizon barrier.

---

## 7. The Grand Duality: Slow Light vs. Time Dilation

Stefan Hertel's two insights reveal a breathtaking reciprocal duality at the heart of informational physics:

| Dimension | Slow Light in Matter *(Pillar 7)* | Time Dilation in Motion *(Pillar 8)* |
| :--- | :--- | :--- |
| **Physical Effect** | Light decelerates in space ($v < c_{\mathcal{I}}$). | Clocks decelerate in time ($d\tau/dt < 1$). |
| **Physical Cause** | Adding matter memory loading overhead. | Diverting bandwidth to spatial translation. |
| **Quasiparticle State** | Dark-State Polariton: $\hat{\Psi} = \cos\theta \hat{\mathcal{E}} - \sin\theta \sqrt{N}\hat{S}$. | Moving Bound State: $\mathbf{u} = \gamma(c_{\mathcal{I}}, \mathbf{v})$. |
| **Governing Equation** | $$v_g = \frac{c_{\mathcal{I}}}{1 + \frac{\mathcal{I}_{\text{matter}}}{\mathcal{I}_{\text{photon}}}} = \frac{c_{\mathcal{I}}}{n_g}$$ | $$\frac{d\tau}{dt} = \sqrt{1 - \frac{v^2}{c_{\mathcal{I}}^2}} = \frac{1}{\gamma}$$ |
| **Zero Limit** | $v_g = 0\text{ m/s}$ (Stopped Light in BEC). | $d\tau/dt = 0$ (Photons / Light Speed limit). |
| **Spacetime Invariance** | $c_{\mathcal{I}}$ is strictly constant (Sommerfeld front). | $c_{\mathcal{I}}$ is strictly constant (Hypotenuse speed). |

- **In Slow Light:** You load more information into matter registers $\implies$ **velocity through space drops**.
- **In Time Dilation:** You force higher velocity through space $\implies$ **internal informational processing rate drops**.

Both phenomena are two sides of the same immutable coin: **the invariant Speed of Information ($c_{\mathcal{I}}$) dictates the total bandwidth of physical reality.**

---

## 8. Summary & Repository Integration

This treatise formalizes:
1. The **Conservation of Informational Bandwidth Law**: $(d\tau/dt)^2 + (v/c_{\mathcal{I}})^2 = 1$.
2. The microscopic derivation of the Lorentz factor $\gamma$ via internal causal loops mediated at $c_{\mathcal{I}}$.
3. The quantum clock speed limit connection via the Margolus-Levitin theorem.
4. The gravitational time dilation formulation as horizon channel capacity.
5. The complete numerical simulation suite (`simulations/run_informational_time_dilation_simulation.py`), vector figure (`figures/fig22_time_dilation_information_bandwidth.svg`), and dataset (`data/sim_time_dilation_bandwidth.json`).
