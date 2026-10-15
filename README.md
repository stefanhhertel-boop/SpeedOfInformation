# Scientific Study: Speed of Light vs. Speed of Information in Theoretical Physics

**Author:** Theoretical Physics AI Pair Researcher (acting as PhD Candidate in Theoretical Physics & Quantum Information)  
**Affiliation:** Center for Quantum Foundations, Relativity, and Emergent Spacetime  
**Date:** October 15, 2026

---

## Executive Summary & Research Question

> **Central Hypothesis:** Does replacing the concept of the "speed of light" ($c$) with the "speed of information" ($c_{\mathcal{I}}$) constitute a major step forward in theoretical physics? Furthermore, how does this new perspective combine Relativity with Quantum Probabilities?

This repository contains the complete scientific study, numerical simulations, formal academic paper, and advanced theoretical treatise addressing this question across:
1. **Axiomatic Spacetime Foundations:** Group-theoretic derivation of Lorentz transformations without electromagnetism (Ignatowsky-Lévy-Leblond formalism) and decoupling of metric invariants from photon mass (Proca electrodynamics).
2. **Optical Wave Dynamics & Dispersion:** Complex contour integration (Sommerfeld-Brillouin analysis and Kramers-Kronig relations) resolving apparent superluminal group velocities ($v_g > c$).
3. **Quantum Foundations & Microcausality:** Microcausality in QFT, the No-Signaling Theorem, and quantum teleportation information budgets.
4. **Unification of Relativity & Quantum Probabilities:**
   - **Information Causality:** Derivation of the Born rule ($L^2$ norm) and Tsirelson's bound ($S = 2\sqrt{2}$) from causal information capacity limits.
   - **Relational Causal Diamonds:** Resolving the "instantaneous collapse vs. relativity of simultaneity" paradox via Relational Quantum Mechanics (RQM) and Quantum Reference Frames (QRF).
   - **Quantum Fisher Information Metric:** Spacetime distance as quantum vacuum state distinguishability.
   - **The Black Hole Page Curve:** Synthesis of General Relativity horizon area ($A/4G$) and quantum von Neumann entropy via quantum extremal islands.

---

## Repository Structure

```
SpeedOfInformation/
├── README.md                                             # Project overview and summary
├── paper/
│   ├── Executive_Summary_Speed_of_Information.md         # High-level white paper & research synthesis
│   ├── Speed_of_Information_Paper.md                     # Full comprehensive scientific manuscript (Markdown)
│   ├── Speed_of_Information_Paper.tex                    # Publication-ready LaTeX manuscript
│   ├── Quantum_Probabilities_and_Relativity_Unification.md # Advanced treatise on Quantum-Relativity Unification
│   ├── Entanglement_Equilibrium_and_Einstein_Equations.md # Exact mathematical derivation of Einstein equations
│   ├── Entanglement_Derivation_Audit_and_Caveats.md      # Critical scientific audit & assumptions checklist
│   ├── Black_Hole_Information_Theory_and_Horizon_Dynamics.md # In-depth analysis of Black Holes, Scrambling, & Wormholes
│   ├── Cosmological_Horizons_and_Holographic_Complexity.md # Analysis of de Sitter Horizons, Dark Energy, & Complexity
│   └── paper_index.html                                  # Interactive HTML reader with MathJax and embedded SVGs
├── simulations/
│   ├── run_simulations.py                                # Suite 1: Optical, Proca, Lieb-Robinson, & MDR
│   ├── run_quantum_relativity_simulations.py             # Suite 2: Info Causality, Fisher Metric, RQM, Page Curve
│   ├── run_entanglement_einstein_derivation.py           # Suite 3: Causal Diamonds, Equilibrium Balance, Raychaudhuri
│   ├── run_black_hole_information_simulations.py         # Suite 4: Scrambling, Hayden-Preskill, Wormholes, Bekenstein
│   └── run_cosmology_and_complexity_simulations.py       # Suite 5: de Sitter Horizon, Dark Energy Lambda, Complexity = Action
├── figures/
│   ├── fig1_sommerfeld_brillouin_front.svg               # Front velocity vs superluminal peak in dispersive media
│   ├── fig2_proca_photon_velocity.svg                    # Massive photon velocity dispersion vs causal metric
│   ├── fig3_lieb_robinson_cone.svg                       # Quantum operator spreading & Lieb-Robinson commutator decay
│   ├── fig4_spacetime_causal_cone.svg                    # 2D Spacetime information light-cone emergence
│   ├── fig5_qg_mdr_delay.svg                             # Planck-scale Modified Dispersion Relations (MDR) delays
│   ├── fig6_information_causality_derivation.svg         # Derivation of Born Rule & Tsirelson Bound from Info Causality
│   ├── fig7_quantum_fisher_spacetime.svg                 # Spacetime metric from Quantum Fisher fidelity
│   ├── fig8_relational_causal_diamonds.svg               # Relational causal diamond updates vs collapse foliation
│   ├── fig9_black_hole_page_curve.svg                    # Unitary Page curve evolution via quantum extremal surfaces
│   ├── fig10_causal_diamond_modular_flow.svg             # Causal diamond & modular Hamiltonian flow lines
│   ├── fig11_entanglement_equilibrium_balance.svg        # Exact cancellation delta S_matter + delta S_area = 0
│   ├── fig12_raychaudhuri_area_deficit.svg               # Raychaudhuri null horizon focusing & area deficit
│   ├── fig13_black_hole_fast_scrambling.svg              # OTOC fast scrambling on the stretched horizon
│   ├── fig14_hayden_preskill_decoding.svg                # Hayden-Preskill protocol decoding fidelity jump
│   ├── fig15_traversable_wormhole_causality.svg          # ER=EPR traversable wormhole teleportation delay
│   ├── fig16_bekenstein_bound_saturation.svg             # Bekenstein holographic information packing saturation
│   ├── fig17_cosmological_event_horizon.svg              # Cosmological event horizon in de Sitter space
│   ├── fig18_dark_energy_information_scaling.svg         # Dark energy Lambda as inverse horizon entropy density
│   ├── fig19_holographic_complexity_growth.svg           # Complexity = Action linear growth at Lloyd's bound
│   └── fig20_complexity_four_epochs.svg                  # The Four Epochs of Quantum Complexity
└── data/
    ├── sim1_sommerfeld_brillouin.json                    # Numerical output from Simulation 1
    ├── sim2_proca_dispersion.json                        # Numerical output from Simulation 2
    ├── sim3_lieb_robinson.json                           # Numerical output from Simulation 3
    ├── sim4_quantum_gravity_mdr.json                     # Numerical output from Simulation 4
    ├── sim_info_causality.json                           # Numerical output from Info Causality Simulation
    ├── sim_quantum_fisher.json                           # Numerical output from Quantum Fisher Simulation
    ├── sim_page_curve.json                               # Numerical output from Page Curve Simulation
    ├── sim_entanglement_einstein.json                    # Numerical output from Entanglement Einstein Simulation
    ├── sim_raychaudhuri_focusing.json                    # Numerical output from Raychaudhuri Focusing Simulation
    ├── sim_fast_scrambling.json                          # Numerical output from Fast Scrambling Simulation
    ├── sim_hayden_preskill.json                          # Numerical output from Hayden-Preskill Simulation
    ├── sim_traversable_wormhole.json                     # Numerical output from Wormhole Simulation
    ├── sim_bekenstein_bound.json                         # Numerical output from Bekenstein Bound Simulation
    ├── sim_cosmological_horizon.json                     # Numerical output from Cosmological Horizon Simulation
    ├── sim_dark_energy_info.json                         # Numerical output from Dark Energy Scaling Simulation
    ├── sim_holographic_complexity.json                   # Numerical output from Complexity Growth Simulation
    └── sim_complexity_epochs.json                        # Numerical output from Complexity Epochs Simulation
```

---

## How to Run Simulations

All numerical simulation suites use standard library Python (zero external dependencies):

```bash
python3 simulations/run_simulations.py
python3 simulations/run_quantum_relativity_simulations.py
python3 simulations/run_entanglement_einstein_derivation.py
python3 simulations/run_black_hole_information_simulations.py
python3 simulations/run_cosmology_and_complexity_simulations.py
```

To view the interactive scientific paper with rendered formulas, interactive TOC, and all 20 vector figures:
- Open `paper/paper_index.html` in your web browser.
