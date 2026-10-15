#!/usr/bin/env python3
"""
Scientific Study: Polariton Information Overhead & Slow Light
Numerical Simulation Suite 6

Models:
1. Polariton Mixing & Quantum Entanglement: Photonic Fraction (cos^2 theta) vs Matter Memory Fraction (sin^2 theta)
2. Group Velocity Deceleration as an Information Overhead Factor: v_g / c_info = 1 / (1 + Memory_Ratio)
3. Cumulative Quantum Speed Limit (QSL) Dwell Time across distance in vacuum, water, glass, and ultracold BECs
4. Spatial Pulse Compression & Atomic Bit Storage Density

Author: Stefan Hertel (Independent Researcher)
Outputs:
- figures/fig21_polariton_information_overhead.svg
- data/sim_polariton_information.json
"""

import math
import os
import json
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
FIG_DIR = os.path.join(PROJECT_DIR, "figures")
DATA_DIR = os.path.join(PROJECT_DIR, "data")
os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)


def escape_xml(s):
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&apos;"))


class SVGPlotter:
    def __init__(self, width=900, height=680, title=""):
        self.width = width
        self.height = height
        self.title = title
        self.elements = []
        self.elements.append(
            f'<rect width="{width}" height="{height}" fill="#ffffff" stroke="none" />'
        )
        self.elements.append(
            f'<text x="{width/2}" y="36" font-family="system-ui, -apple-system, sans-serif" '
            f'font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">{escape_xml(title)}</text>'
        )

    def draw_panel(self, x, y, w, h, title, xlabel, ylabel, xlim, ylim, xscale="linear", yscale="linear"):
        self.elements.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="6" />'
        )
        self.elements.append(
            f'<text x="{x + w/2}" y="{y + 22}" font-family="system-ui, -apple-system, sans-serif" '
            f'font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">{escape_xml(title)}</text>'
        )
        self.elements.append(
            f'<text x="{x + w/2}" y="{y + h - 10}" font-family="system-ui, -apple-system, sans-serif" '
            f'font-size="11" font-weight="600" fill="#475569" text-anchor="middle">{escape_xml(xlabel)}</text>'
        )
        self.elements.append(
            f'<text x="{x + 16}" y="{y + h/2}" font-family="system-ui, -apple-system, sans-serif" '
            f'font-size="11" font-weight="600" fill="#475569" text-anchor="middle" '
            f'transform="rotate(-90, {x + 16}, {y + h/2})">{escape_xml(ylabel)}</text>'
        )
        return {
            "x": x + 55, "y": y + 35, "w": w - 75, "h": h - 65,
            "xlim": xlim, "ylim": ylim, "xscale": xscale, "yscale": yscale
        }

    def _to_pix(self, p, x_val, y_val):
        x0, y0, w, h = p["x"], p["y"], p["w"], p["h"]
        xmin, xmax = p["xlim"]
        ymin, ymax = p["ylim"]

        if p["xscale"] == "log":
            lx = math.log10(max(x_val, 1e-30))
            lxmin = math.log10(max(xmin, 1e-30))
            lxmax = math.log10(max(xmax, 1e-30))
            fx = (lx - lxmin) / (lxmax - lxmin) if lxmax != lxmin else 0.5
        else:
            fx = (x_val - xmin) / (xmax - xmin) if xmax != xmin else 0.5

        if p["yscale"] == "log":
            ly = math.log10(max(y_val, 1e-30))
            lymin = math.log10(max(ymin, 1e-30))
            lymax = math.log10(max(ymax, 1e-30))
            fy = (ly - lymin) / (lymax - lymin) if lymax != lymin else 0.5
        else:
            fy = (y_val - ymin) / (ymax - ymin) if ymax != ymin else 0.5

        fx = max(0.0, min(1.0, fx))
        fy = max(0.0, min(1.0, fy))

        px = x0 + fx * w
        py = y0 + (1.0 - fy) * h
        return px, py

    def draw_grid_and_ticks(self, p, xticks, yticks, xlabels=None, ylabels=None):
        x0, y0, w, h = p["x"], p["y"], p["w"], p["h"]
        for i, xt in enumerate(xticks):
            px, _ = self._to_pix(p, xt, p["ylim"][0])
            self.elements.append(
                f'<line x1="{px:.1f}" y1="{y0}" x2="{px:.1f}" y2="{y0+h}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="2,2" />'
            )
            lbl = xlabels[i] if xlabels and i < len(xlabels) else f"{xt:g}"
            self.elements.append(
                f'<text x="{px:.1f}" y="{y0+h+14}" font-family="system-ui, -apple-system, sans-serif" '
                f'font-size="9.5" fill="#64748b" text-anchor="middle">{escape_xml(lbl)}</text>'
            )

        for i, yt in enumerate(yticks):
            _, py = self._to_pix(p, p["xlim"][0], yt)
            self.elements.append(
                f'<line x1="{x0}" y1="{py:.1f}" x2="{x0+w}" y2="{py:.1f}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="2,2" />'
            )
            lbl = ylabels[i] if ylabels and i < len(ylabels) else f"{yt:g}"
            self.elements.append(
                f'<text x="{x0-6}" y="{py+3:.1f}" font-family="system-ui, -apple-system, sans-serif" '
                f'font-size="9.5" fill="#64748b" text-anchor="end">{escape_xml(lbl)}</text>'
            )

    def plot_line(self, p, xs, ys, stroke="#2563eb", stroke_width=2.5, stroke_dasharray=None):
        pts = []
        for x_val, y_val in zip(xs, ys):
            px, py = self._to_pix(p, x_val, y_val)
            pts.append(f"{px:.1f},{py:.1f}")
        dash = f' stroke-dasharray="{stroke_dasharray}"' if stroke_dasharray else ""
        self.elements.append(
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{stroke}" stroke-width="{stroke_width}"{dash} />'
        )

    def add_legend(self, x, y, items):
        # items: [(label, color, dasharray)]
        h_box = len(items) * 20 + 12
        self.elements.append(
            f'<rect x="{x}" y="{y}" width="210" height="{h_box}" fill="#ffffff" fill-opacity="0.92" '
            f'stroke="#cbd5e1" stroke-width="1" rx="4" />'
        )
        for i, (lbl, col, dash) in enumerate(items):
            iy = y + 15 + i * 20
            dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
            self.elements.append(
                f'<line x1="{x+10}" y1="{iy}" x2="{x+35}" y2="{iy}" stroke="{col}" stroke-width="2.5"{dash_attr} />'
            )
            self.elements.append(
                f'<text x="{x+42}" y="{iy+3.5}" font-family="system-ui, -apple-system, sans-serif" '
                f'font-size="10.5" fill="#1e293b" font-weight="600">{escape_xml(lbl)}</text>'
            )

    def save(self, filepath):
        svg_content = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="{self.width}" height="{self.height}">\n'
            + "\n".join(self.elements)
            + "\n</svg>"
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        # Validate XML
        ET.fromstring(svg_content)
        print(f"Validated and saved: {filepath}")


def run_simulation():
    c_info = 299792458.0  # m/s

    # --------------------------------------------------------------------------
    # Panel A: Polariton Mixing Angle theta & Information Partition
    # theta from 0 to pi/2 (0 = pure photon, pi/2 = pure atomic excitation)
    # --------------------------------------------------------------------------
    thetas_deg = [i * 0.9 for i in range(101)]  # 0 to 90 degrees
    thetas_rad = [math.radians(t) for t in thetas_deg]
    photonic_frac = [math.cos(t)**2 for t in thetas_rad]
    atomic_frac = [math.sin(t)**2 for t in thetas_rad]
    
    # Bipartite von Neumann entanglement entropy in bits: -p log2 p - (1-p) log2 (1-p)
    ent_entropy_bits = []
    for p in photonic_frac:
        if p <= 1e-9 or p >= 1.0 - 1e-9:
            ent_entropy_bits.append(0.0)
        else:
            q = 1.0 - p
            ent_entropy_bits.append(-(p * math.log2(p) + q * math.log2(q)))

    # --------------------------------------------------------------------------
    # Panel B: Group Velocity Deceleration (v_g / c_info) vs Memory Coupling Ratio
    # ratio = g^2 N / Omega_c^2 from 10^-2 (vacuum-like) to 10^8 (ultracold slow light)
    # --------------------------------------------------------------------------
    log_ratios = [-2.0 + i * 0.1 for i in range(101)]  # 10^-2 to 10^8
    ratios = [10.0**lr for lr in log_ratios]
    group_velocities = [1.0 / (1.0 + r) for r in ratios]  # v_g / c_info

    # Key material benchmarks:
    benchmarks = {
        "Vacuum": {"ratio": 0.0, "v_frac": 1.0, "v_phys": c_info},
        "Air": {"ratio": 0.0003, "v_frac": 1.0 / 1.0003, "v_phys": c_info / 1.0003},
        "Water": {"ratio": 0.33, "v_frac": 1.0 / 1.33, "v_phys": c_info / 1.33},
        "Dense Glass": {"ratio": 0.90, "v_frac": 1.0 / 1.90, "v_phys": c_info / 1.90},
        "BEC Slow Light (Hau 1999)": {"ratio": 1.76e7, "v_frac": 1.0 / 1.76e7, "v_phys": 17.0},
        "Stopped Light (EIT Memory)": {"ratio": 1e12, "v_frac": 1e-12, "v_phys": 0.0}
    }

    # --------------------------------------------------------------------------
    # Panel C: Cumulative Quantum Dwell Time Delta t_dwell vs Distance x (0 to 10 cm)
    # Delta t_dwell(x) = x * (n - 1) / c_info
    # --------------------------------------------------------------------------
    distances_cm = [i * 0.1 for i in range(101)]  # 0 to 10 cm
    distances_m = [d * 0.01 for d in distances_cm]

    dwell_vacuum_ns = [0.0 for _ in distances_m]
    dwell_water_ns = [(d * (1.33 - 1.0) / c_info) * 1e9 for d in distances_m]
    dwell_glass_ns = [(d * (1.90 - 1.0) / c_info) * 1e9 for d in distances_m]
    # For BEC slow light: n_g ~ 1.76e7, dwell time in milliseconds!
    dwell_bec_ms = [(d * (1.76e7 - 1.0) / c_info) * 1e3 for d in distances_m]

    # --------------------------------------------------------------------------
    # Panel D: Spatial Pulse Compression & Storage Density
    # Input 1 microsecond pulse: vacuum length = c_info * 1 us = 300 meters!
    # In glass: 158 meters. In Hau's BEC: 300 m compresses into 17 micrometers!
    # --------------------------------------------------------------------------
    pulse_dur_us = 1.0  # 1 microsecond pulse
    log_ngs = [0.0 + i * 0.075 for i in range(101)]  # n_g from 10^0 to 10^7.5
    ngs = [10.0**lng for lng in log_ngs]
    packet_lengths_m = [(c_info * 1e-6) / ng for ng in ngs]  # 300 m / n_g

    # --------------------------------------------------------------------------
    # Generate SVG Plot
    # --------------------------------------------------------------------------
    plotter = SVGPlotter(
        width=960, height=720,
        title="Figure 21: Polariton Information Overhead & The Quantum Mechanics of Slow Light"
    )

    # Panel 1: Mixing Angle & Entanglement Entropy
    p1 = plotter.draw_panel(
        x=45, y=55, w=420, h=300,
        title="A. Polariton State Partition & Entanglement Entropy",
        xlabel="Polariton Mixing Angle θ (degrees)",
        ylabel="State Fraction / Entropy (bits)",
        xlim=(0, 90), ylim=(0, 1.05)
    )
    plotter.draw_grid_and_ticks(
        p1, xticks=[0, 30, 45, 60, 90], yticks=[0.0, 0.25, 0.5, 0.75, 1.0]
    )
    plotter.plot_line(p1, thetas_deg, photonic_frac, stroke="#2563eb", stroke_width=2.5)
    plotter.plot_line(p1, thetas_deg, atomic_frac, stroke="#dc2626", stroke_width=2.5)
    plotter.plot_line(p1, thetas_deg, ent_entropy_bits, stroke="#7c3aed", stroke_width=2.5, stroke_dasharray="4,3")
    plotter.add_legend(
        x=235, y=140,
        items=[
            ("Photonic Fraction cos²θ", "#2563eb", None),
            ("Atomic Memory Fraction sin²θ", "#dc2626", None),
            ("Entanglement S_ent (bits)", "#7c3aed", "4,3")
        ]
    )

    # Panel 2: Group Velocity Deceleration vs Memory Coupling
    p2 = plotter.draw_panel(
        x=495, y=55, w=420, h=300,
        title="B. Velocity Deceleration vs Memory Coupling Ratio",
        xlabel="Matter Information Ratio (g²N / Ω_c²)",
        ylabel="Group Velocity v_g / c_info",
        xlim=(1e-2, 1e8), ylim=(1e-8, 1.5),
        xscale="log", yscale="log"
    )
    plotter.draw_grid_and_ticks(
        p2,
        xticks=[1e-2, 1e0, 1e2, 1e4, 1e6, 1e8],
        yticks=[1e-8, 1e-6, 1e-4, 1e-2, 1e0],
        xlabels=["10⁻²", "10⁰", "10²", "10⁴", "10⁶", "10⁸"],
        ylabels=["10⁻⁸", "10⁻⁶", "10⁻⁴", "10⁻²", "10⁰"]
    )
    plotter.plot_line(p2, ratios, group_velocities, stroke="#059669", stroke_width=3.0)

    # Annotate Hau 1999 BEC point on Panel 2
    px_hau, py_hau = plotter._to_pix(p2, 1.76e7, 1.0 / 1.76e7)
    plotter.elements.append(
        f'<circle cx="{px_hau:.1f}" cy="{py_hau:.1f}" r="5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5" />'
    )
    plotter.elements.append(
        f'<text x="{px_hau-10:.1f}" y="{py_hau-10:.1f}" font-family="system-ui, -apple-system, sans-serif" '
        f'font-size="10" font-weight="bold" fill="#dc2626" text-anchor="end">Hau BEC (17 m/s)</text>'
    )
    # Annotate Vacuum
    px_vac, py_vac = plotter._to_pix(p2, 1e-2, 1.0)
    plotter.elements.append(
        f'<circle cx="{px_vac:.1f}" cy="{py_vac:.1f}" r="5" fill="#2563eb" stroke="#ffffff" stroke-width="1.5" />'
    )
    plotter.elements.append(
        f'<text x="{px_vac+10:.1f}" y="{py_vac+15:.1f}" font-family="system-ui, -apple-system, sans-serif" '
        f'font-size="10" font-weight="bold" fill="#2563eb">Vacuum (v = c_info)</text>'
    )

    # Panel 3: Cumulative Quantum Dwell Time in Media
    p3 = plotter.draw_panel(
        x=45, y=385, w=420, h=300,
        title="C. Cumulative Quantum Memory Dwell Time (Δt_delay)",
        xlabel="Propagation Distance x (cm)",
        ylabel="Accumulated Memory Delay (ns)",
        xlim=(0, 10), ylim=(0, 0.35)
    )
    plotter.draw_grid_and_ticks(
        p3, xticks=[0, 2.5, 5.0, 7.5, 10.0], yticks=[0.0, 0.1, 0.2, 0.3]
    )
    plotter.plot_line(p3, distances_cm, dwell_vacuum_ns, stroke="#94a3b8", stroke_width=2.0, stroke_dasharray="3,3")
    plotter.plot_line(p3, distances_cm, dwell_water_ns, stroke="#0284c7", stroke_width=2.5)
    plotter.plot_line(p3, distances_cm, dwell_glass_ns, stroke="#d97706", stroke_width=2.5)
    plotter.add_legend(
        x=225, y=470,
        items=[
            ("Vacuum (0 ns delay)", "#94a3b8", "3,3"),
            ("Water n=1.33 (0.11 ns/10cm)", "#0284c7", None),
            ("Dense Glass n=1.90 (0.30 ns)", "#d97706", None)
        ]
    )

    # Panel 4: Spatial Pulse Compression & Spatial Bit Concentration
    p4 = plotter.draw_panel(
        x=495, y=385, w=420, h=300,
        title="D. Spatial Pulse Compression (1 μs pulse: 300 m in vacuum)",
        xlabel="Group Index n_g (Information Overhead)",
        ylabel="Physical Packet Length (meters)",
        xlim=(1e0, 1e7), ylim=(1e-5, 500.0),
        xscale="log", yscale="log"
    )
    plotter.draw_grid_and_ticks(
        p4,
        xticks=[1e0, 1e2, 1e4, 1e6],
        yticks=[1e-4, 1e-2, 1e0, 1e2],
        xlabels=["10⁰ (Vacuum)", "10²", "10⁴", "10⁶ (BEC)"],
        ylabels=["0.1 mm", "1 cm", "1 m", "100 m"]
    )
    plotter.plot_line(p4, ngs, packet_lengths_m, stroke="#b45309", stroke_width=3.0)

    # Annotate 300 m in vacuum vs 17 um in BEC
    px_lvac, py_lvac = plotter._to_pix(p4, 1.0, 300.0)
    plotter.elements.append(
        f'<circle cx="{px_lvac:.1f}" cy="{py_lvac:.1f}" r="5" fill="#2563eb" stroke="#ffffff" stroke-width="1.5" />'
    )
    plotter.elements.append(
        f'<text x="{px_lvac+10:.1f}" y="{py_lvac+4:.1f}" font-family="system-ui, -apple-system, sans-serif" '
        f'font-size="10" font-weight="bold" fill="#2563eb">Vacuum: 300 meters</text>'
    )
    px_lbec, py_lbec = plotter._to_pix(p4, 1.76e7, 300.0 / 1.76e7)
    plotter.elements.append(
        f'<circle cx="{px_lbec:.1f}" cy="{py_lbec:.1f}" r="5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5" />'
    )
    plotter.elements.append(
        f'<text x="{px_lbec-10:.1f}" y="{py_lbec-8:.1f}" font-family="system-ui, -apple-system, sans-serif" '
        f'font-size="10" font-weight="bold" fill="#dc2626" text-anchor="end">BEC: 17 micrometers!</text>'
    )

    fig_path = os.path.join(FIG_DIR, "fig21_polariton_information_overhead.svg")
    plotter.save(fig_path)

    # --------------------------------------------------------------------------
    # Save Structured Simulation Data
    # --------------------------------------------------------------------------
    data_output = {
        "simulation": "Polariton Information Overhead and Quantum Slow Light",
        "author": "Stefan Hertel",
        "affiliation": "Independent Researcher",
        "date": "2026-10-15",
        "physical_constants": {
            "c_info_m_s": c_info
        },
        "benchmarks": benchmarks,
        "sample_points": {
            "thetas_deg": thetas_deg[::10],
            "photonic_fractions": photonic_frac[::10],
            "atomic_fractions": atomic_frac[::10],
            "entanglement_entropy_bits": ent_entropy_bits[::10]
        },
        "summary_findings": [
            "Photons slow down in matter because they hybridize into polaritons with non-zero matter memory fraction sin^2(theta).",
            "The refractive index n_g = 1 + (g^2 N / Omega_c^2) measures the ratio of quantum information loaded into atomic spin memory vs bare field flux.",
            "Each atomic interaction imposes a finite quantum speed limit dwell time tau_dwell = pi hbar / (2 g).",
            "In Bose-Einstein condensates (Hau 1999), 99.99999% of the quantum state is stored in atomic spin coherence, compressing a 300-meter vacuum packet into 17 micrometers at 17 m/s.",
            "Causal velocity c_info remains strictly invariant throughout all dispersive and slow-light media."
        ]
    }

    data_path = os.path.join(DATA_DIR, "sim_polariton_information.json")
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data_output, f, indent=2)
    print(f"Saved dataset: {data_path}")


if __name__ == "__main__":
    run_simulation()
