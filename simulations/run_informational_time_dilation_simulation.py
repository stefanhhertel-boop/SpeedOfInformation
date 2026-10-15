#!/usr/bin/env python3
"""
Scientific Study: Time Dilation as Conservation of Informational Bandwidth
Numerical Simulation Suite 7

Author: Stefan Hertel
Affiliation: Independent Researcher
Date: October 15, 2026

Models:
1. Informational Bandwidth Trade-Off: (d tau / dt)^2 + (v / c_I)^2 = 1
2. Elementary Causal Loop Geometry & Path Stretching: c_I^2 dt^2 = 4L^2 + v^2 dt^2
3. Quantum Margolus-Levitin Clock Rate vs Velocity & Atmospheric Muon Dilation
4. Gravitational Time Dilation as Horizon Channel Bandwidth: d tau / dt = sqrt(1 - r_s / r)

Outputs:
- figures/fig22_time_dilation_information_bandwidth.svg
- data/sim_time_dilation_bandwidth.json
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

C_INFO = 299792458.0  # m/s


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
    def __init__(self, width=980, height=740, title=""):
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
            "x": x + 60, "y": y + 35, "w": w - 85, "h": h - 65,
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

    def plot_filled_area(self, p, xs, ys, fill="#3b82f6", opacity=0.15):
        pts = []
        for x_val, y_val in zip(xs, ys):
            px, py = self._to_pix(p, x_val, y_val)
            pts.append(f"{px:.1f},{py:.1f}")
        # close to baseline
        px_end, py_base = self._to_pix(p, xs[-1], p["ylim"][0])
        px_start, _ = self._to_pix(p, xs[0], p["ylim"][0])
        pts.append(f"{px_end:.1f},{py_base:.1f}")
        pts.append(f"{px_start:.1f},{py_base:.1f}")
        self.elements.append(
            f'<polygon points="{" ".join(pts)}" fill="{fill}" fill-opacity="{opacity}" stroke="none" />'
        )

    def add_point(self, p, x_val, y_val, color="#dc2626", radius=4.5, label=None, label_pos="top"):
        px, py = self._to_pix(p, x_val, y_val)
        self.elements.append(
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{radius}" fill="{color}" stroke="#ffffff" stroke-width="1.5" />'
        )
        if label:
            dx = 0
            dy = -8 if label_pos == "top" else 15
            anchor = "middle"
            if label_pos == "right":
                dx = 8
                dy = 4
                anchor = "start"
            elif label_pos == "left":
                dx = -8
                dy = 4
                anchor = "end"
            self.elements.append(
                f'<text x="{px + dx:.1f}" y="{py + dy:.1f}" font-family="system-ui, -apple-system, sans-serif" '
                f'font-size="9.5" font-weight="bold" fill="{color}" text-anchor="{anchor}">{escape_xml(label)}</text>'
            )

    def add_legend(self, x, y, items):
        h_box = len(items) * 20 + 12
        self.elements.append(
            f'<rect x="{x}" y="{y}" width="220" height="{h_box}" fill="#ffffff" fill-opacity="0.92" '
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
        ET.fromstring(svg_content)
        print(f"Validated XML and successfully saved: {filepath}")


def run_simulation():
    plotter = SVGPlotter(
        width=980, height=740,
        title="Figure 22: Time Dilation as Conservation of Informational Bandwidth & Causal Loop Geometry"
    )

    # -------------------------------------------------------------
    # Panel A: Informational Bandwidth Conservation (Quarter-Circle)
    # -------------------------------------------------------------
    pA = plotter.draw_panel(
        x=25, y=55, w=450, h=315,
        title="Panel A: Informational Bandwidth Allocation: (dτ/dt)² + (v/c_I)² = 1",
        xlabel="Spatial Velocity v / c_I (Spatial Translation Bandwidth)",
        ylabel="Internal Clock Rate dτ/dt (Internal State Bandwidth)",
        xlim=[0.0, 1.0], ylim=[0.0, 1.05]
    )
    plotter.draw_grid_and_ticks(
        pA,
        xticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        yticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        xlabels=["0", "0.2 c_I", "0.4 c_I", "0.6 c_I", "0.8 c_I", "1.0 c_I"],
        ylabels=["0 (Frozen)", "0.20", "0.40", "0.60", "0.80", "1.00 (Rest)"]
    )

    # Generate quarter circle data
    v_vals = [i / 200.0 for i in range(201)]
    dtau_vals = [math.sqrt(max(0.0, 1.0 - v**2)) for v in v_vals]

    # Fill area under curve
    plotter.plot_filled_area(pA, v_vals, dtau_vals, fill="#3b82f6", opacity=0.18)
    plotter.plot_line(pA, v_vals, dtau_vals, stroke="#1d4ed8", stroke_width=3.0)

    # Diagonal partition reference (v = dtau)
    plotter.plot_line(pA, [0.0, 1.0], [1.0, 0.0], stroke="#94a3b8", stroke_width=1.5, stroke_dasharray="3,3")

    # Key points
    plotter.add_point(pA, 0.0, 1.0, color="#16a34a", radius=5.0, label="v=0: 100% Internal Time", label_pos="right")
    v_half = math.sqrt(0.75)  # 0.866
    plotter.add_point(pA, v_half, 0.5, color="#e11d48", radius=5.0, label="v=0.866 c_I (γ=2): 50% Time", label_pos="top")
    v_muon = 0.998
    dtau_muon = math.sqrt(1.0 - v_muon**2)  # ~0.063
    plotter.add_point(pA, v_muon, dtau_muon, color="#7c3aed", radius=5.0, label="Muon (γ=15.8): 6.3%", label_pos="left")
    plotter.add_point(pA, 1.0, 0.0, color="#dc2626", radius=5.0, label="v=c_I: Time Stops", label_pos="top")

    plotter.add_legend(
        pA["x"] + 15, pA["y"] + 175,
        [
            ("Internal Bandwidth: dτ/dt = √(1 - v²/c_I²)", "#1d4ed8", None),
            ("Spatial / Temporal Equipartition", "#94a3b8", "3,3")
        ]
    )

    # -------------------------------------------------------------
    # Panel B: Elementary Causal Loop & Hypotenuse Path Stretching
    # -------------------------------------------------------------
    pB = plotter.draw_panel(
        x=505, y=55, w=450, h=315,
        title="Panel B: Causal Loop Geometry: Signal Hypotenuse & Delay",
        xlabel="Spatial Coordinate Shift Δx = v · Δt (m)",
        ylabel="Transverse Separation L & Hypotenuse Path (m)",
        xlim=[-0.5, 3.5], ylim=[-0.2, 2.2]
    )

    # Draw schematic of the rest clock vs moving clock directly in SVG
    # Origin at (0,0), L = 1.0
    x0_pix, y0_pix = plotter._to_pix(pB, 0.0, 0.0)
    xL_pix, yL_pix = plotter._to_pix(pB, 0.0, 1.0)

    # Rest clock: vertical exchange
    plotter.elements.append(
        f'<line x1="{x0_pix:.1f}" y1="{y0_pix:.1f}" x2="{xL_pix:.1f}" y2="{yL_pix:.1f}" '
        f'stroke="#16a34a" stroke-width="3" />'
    )
    plotter.elements.append(
        f'<circle cx="{x0_pix:.1f}" cy="{y0_pix:.1f}" r="5" fill="#16a34a" />'
    )
    plotter.elements.append(
        f'<circle cx="{xL_pix:.1f}" cy="{yL_pix:.1f}" r="5" fill="#16a34a" />'
    )
    plotter.elements.append(
        f'<text x="{x0_pix-10:.1f}" y="{(y0_pix+yL_pix)/2:.1f}" font-family="system-ui" font-size="10" '
        f'fill="#16a34a" font-weight="bold" text-anchor="end">Rest: Path = 2L (Δτ = 2L/c_I)</text>'
    )

    # Moving clock: diagonal hypotenuse
    vx = 2.4
    x_mid, y_top = plotter._to_pix(pB, vx / 2.0, 1.0)
    x_end, y_bot = plotter._to_pix(pB, vx, 0.0)

    # Upward leg
    plotter.elements.append(
        f'<line x1="{x0_pix:.1f}" y1="{y0_pix:.1f}" x2="{x_mid:.1f}" y2="{y_top:.1f}" '
        f'stroke="#2563eb" stroke-width="3" />'
    )
    # Downward leg
    plotter.elements.append(
        f'<line x1="{x_mid:.1f}" y1="{y_top:.1f}" x2="{x_end:.1f}" y2="{y_bot:.1f}" '
        f'stroke="#2563eb" stroke-width="3" stroke-dasharray="4,3" />'
    )
    # Horizontal shift
    plotter.elements.append(
        f'<line x1="{x0_pix:.1f}" y1="{y0_pix:.1f}" x2="{x_end:.1f}" y2="{y_bot:.1f}" '
        f'stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2" />'
    )
    plotter.elements.append(
        f'<circle cx="{x_mid:.1f}" cy="{y_top:.1f}" r="5" fill="#2563eb" />'
    )
    plotter.elements.append(
        f'<circle cx="{x_end:.1f}" cy="{y_bot:.1f}" r="5" fill="#2563eb" />'
    )

    plotter.elements.append(
        f'<text x="{(x0_pix+x_mid)/2 - 5:.1f}" y="{(y0_pix+y_top)/2 - 8:.1f}" font-family="system-ui" '
        f'font-size="10.5" fill="#2563eb" font-weight="bold">c_I · (Δt/2) = √(L² + (vΔt/2)²)</text>'
    )
    plotter.elements.append(
        f'<text x="{(x0_pix+x_end)/2:.1f}" y="{y0_pix+18:.1f}" font-family="system-ui" '
        f'font-size="10" fill="#64748b" font-weight="600" text-anchor="middle">Spatial Shift: v · Δt</text>'
    )

    # Summary box in Panel B
    plotter.elements.append(
        f'<rect x="{pB["x"]+10}" y="{pB["y"]+160}" width="340" height="75" fill="#eff6ff" '
        f'stroke="#93c5fd" stroke-width="1" rx="5" />'
    )
    plotter.elements.append(
        f'<text x="{pB["x"]+20}" y="{pB["y"]+180}" font-family="system-ui" font-size="10.5" '
        f'font-weight="bold" fill="#1e3a8a">Pythagorean Informational Derivation:</text>'
    )
    plotter.elements.append(
        f'<text x="{pB["x"]+20}" y="{pB["y"]+198}" font-family="system-ui" font-size="9.5" '
        f'fill="#1e293b">• Invariant Causal Speed along Hypotenuse: c_I = constant</text>'
    )
    plotter.elements.append(
        f'<text x="{pB["x"]+20}" y="{pB["y"]+215}" font-family="system-ui" font-size="9.5" '
        f'fill="#1e293b">• Internal cycle time: Δt = 2L / √(c_I² - v²) = γ · Δτ</text>'
    )
    plotter.elements.append(
        f'<text x="{pB["x"]+20}" y="{pB["y"]+230}" font-family="system-ui" font-size="9.5" '
        f'font-weight="bold" fill="#2563eb">∴ All internal atomic forces take longer to coordinate!</text>'
    )

    # -------------------------------------------------------------
    # Panel C: Margolus-Levitin Quantum Clock Rate & Muon Dilation
    # -------------------------------------------------------------
    pC = plotter.draw_panel(
        x=25, y=395, w=450, h=315,
        title="Panel C: Margolus-Levitin Clock Rate & Atmospheric Muon Dilation",
        xlabel="Velocity v / c_I",
        ylabel="Quantum Clock Rate ν(v) / ν_0 & Lorentz Factor γ",
        xlim=[0.0, 1.0], ylim=[0.0, 18.0]
    )
    plotter.draw_grid_and_ticks(
        pC,
        xticks=[0.0, 0.2, 0.4, 0.6, 0.8, 0.998],
        yticks=[0.0, 2.0, 5.0, 10.0, 15.0, 18.0],
        xlabels=["0", "0.2 c_I", "0.4 c_I", "0.6 c_I", "0.8 c_I", "0.998 c_I"],
        ylabels=["0", "2", "5", "10", "15", "18"]
    )

    v_dense = [i / 500.0 for i in range(500)]
    gamma_curve = [1.0 / math.sqrt(max(0.001, 1.0 - v**2)) for v in v_dense if v < 0.9985]
    v_curve = v_dense[:len(gamma_curve)]
    nu_curve = [math.sqrt(max(0.0, 1.0 - v**2)) for v in v_curve]

    plotter.plot_line(pC, v_curve, gamma_curve, stroke="#dc2626", stroke_width=2.5)
    plotter.plot_line(pC, v_curve, nu_curve, stroke="#2563eb", stroke_width=2.5)

    # Real experimental points
    # Muon point
    gamma_muon = 1.0 / math.sqrt(1.0 - 0.998**2)  # 15.82
    plotter.add_point(pC, 0.998, gamma_muon, color="#7c3aed", radius=5.0, label="Cosmic Muon: γ=15.82", label_pos="left")
    # Rest point
    plotter.add_point(pC, 0.0, 1.0, color="#16a34a", radius=5.0, label="Rest: ν=ν_0, γ=1", label_pos="right")

    plotter.add_legend(
        pC["x"] + 15, pC["y"] + 20,
        [
            ("Lorentz Dilation Factor γ(v) = 1/√(1-v²/c_I²)", "#dc2626", None),
            ("Margolus-Levitin Clock Rate ν(v) / ν_0", "#2563eb", None),
        ]
    )

    # Muon experiment info box
    plotter.elements.append(
        f'<rect x="{pC["x"]+15}" y="{pC["y"]+135}" width="260" height="65" fill="#ffffff" '
        f'stroke="#cbd5e1" stroke-width="1" rx="4" />'
    )
    plotter.elements.append(
        f'<text x="{pC["x"]+25}" y="{pC["y"]+153}" font-family="system-ui" font-size="9.5" '
        f'font-weight="bold" fill="#0f172a">Experimental Verification: Cosmic Muons</text>'
    )
    plotter.elements.append(
        f'<text x="{pC["x"]+25}" y="{pC["y"]+169}" font-family="system-ui" font-size="9" '
        f'fill="#475569">Rest lifetime: τ_0 = 2.20 μs (Range: 660 m)</text>'
    )
    plotter.elements.append(
        f'<text x="{pC["x"]+25}" y="{pC["y"]+185}" font-family="system-ui" font-size="9" '
        f'font-weight="bold" fill="#7c3aed">Dilated lifetime: 34.8 μs (Range: 10.4 km → Reaches Earth!)</text>'
    )

    # -------------------------------------------------------------
    # Panel D: Gravitational Time Dilation as Horizon Channel Capacity
    # -------------------------------------------------------------
    pD = plotter.draw_panel(
        x=505, y=395, w=450, h=315,
        title="Panel D: Gravitational Time Dilation: Horizon Channel Capacity",
        xlabel="Radial Distance r / r_s (Schwarzschild Radii)",
        ylabel="Channel Capacity C(r) / C_∞ & Clock Rate dτ/dt",
        xlim=[1.0, 5.0], ylim=[0.0, 1.05]
    )
    plotter.draw_grid_and_ticks(
        pD,
        xticks=[1.0, 1.5, 2.0, 3.0, 4.0, 5.0],
        yticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        xlabels=["1.0 r_s", "1.5 r_s", "2.0 r_s", "3.0 r_s", "4.0 r_s", "5.0 r_s"],
        ylabels=["0 (Horizon)", "0.20", "0.40", "0.60", "0.80", "1.00 (Flat)"]
    )

    r_vals = [1.001 + (i / 100.0) * 4.0 for i in range(101)]
    dtau_grav = [math.sqrt(1.0 - 1.0 / r) for r in r_vals]

    plotter.plot_filled_area(pD, r_vals, dtau_grav, fill="#059669", opacity=0.15)
    plotter.plot_line(pD, r_vals, dtau_grav, stroke="#059669", stroke_width=3.0)

    # Event horizon asymptote line
    px_rs, _ = plotter._to_pix(pD, 1.0, 0.0)
    plotter.elements.append(
        f'<line x1="{px_rs:.1f}" y1="{pD["y"]}" x2="{px_rs:.1f}" y2="{pD["y"]+pD["h"]}" '
        f'stroke="#dc2626" stroke-width="2" stroke-dasharray="3,3" />'
    )
    plotter.add_point(pD, 1.0, 0.0, color="#dc2626", radius=5.0, label="r = r_s: Zero Channel Capacity", label_pos="right")
    plotter.add_point(pD, 2.0, math.sqrt(0.5), color="#0284c7", radius=5.0, label="r=2 r_s: 70.7% Clock Rate", label_pos="top")

    plotter.add_legend(
        pD["x"] + 80, pD["y"] + 155,
        [
            ("Channel Bandwidth: C(r) = C_∞ √(1 - r_s/r)", "#059669", None),
            ("Horizon Capacity Boundary: C = 0", "#dc2626", "3,3")
        ]
    )

    # Save SVG
    svg_path = os.path.join(FIG_DIR, "fig22_time_dilation_information_bandwidth.svg")
    plotter.save(svg_path)

    # -------------------------------------------------------------
    # Generate JSON Dataset
    # -------------------------------------------------------------
    dataset = {
        "title": "Time Dilation as Conservation of Informational Bandwidth Simulation Suite",
        "author": "Stefan Hertel",
        "affiliation": "Independent Researcher",
        "date": "2026-10-15",
        "parameters": {
            "c_info": C_INFO,
            "bandwidth_tradeoff_equation": "(dtau/dt)^2 + (v/c_I)^2 = 1",
            "margolus_levitin_bound": "nu_max = 2E / (pi * hbar)",
            "lorentz_factor_equation": "gamma = 1 / sqrt(1 - v^2/c_I^2)",
            "gravitational_dilation_equation": "dtau/dt = sqrt(1 - 2GM / (r * c_I^2))"
        },
        "operating_points": [
            {"label": "At Rest", "v_over_c": 0.0, "dtau_dt": 1.0, "gamma": 1.0, "internal_bandwidth_pct": 100.0},
            {"label": "GPS Satellite", "v_over_c": 1.3e-5, "dtau_dt": 0.999999999915, "gamma": 1.000000000085, "kinematic_dilation_us_day": -7.2},
            {"label": "50% Causal Speed", "v_over_c": 0.5, "dtau_dt": 0.866025, "gamma": 1.1547, "internal_bandwidth_pct": 75.0},
            {"label": "Half Clock Rate", "v_over_c": 0.866025, "dtau_dt": 0.500000, "gamma": 2.0000, "internal_bandwidth_pct": 25.0},
            {"label": "Cosmic Ray Muon", "v_over_c": 0.998, "dtau_dt": 0.063214, "gamma": 15.819, "rest_lifetime_us": 2.197, "dilated_lifetime_us": 34.75},
            {"label": "CERN LHC Proton", "v_over_c": 0.999999991, "dtau_dt": 0.000134, "gamma": 7450.0, "internal_bandwidth_pct": 1.8e-6},
            {"label": "Photon / Invariant Causal Limit", "v_over_c": 1.0, "dtau_dt": 0.0, "gamma": "infinity", "internal_bandwidth_pct": 0.0}
        ],
        "gravitational_channel_capacity": [
            {"r_over_rs": 1.0, "channel_capacity_ratio": 0.0, "clock_rate_ratio": 0.0},
            {"r_over_rs": 1.1, "channel_capacity_ratio": 0.3015, "clock_rate_ratio": 0.3015},
            {"r_over_rs": 1.5, "channel_capacity_ratio": 0.5774, "clock_rate_ratio": 0.5774},
            {"r_over_rs": 2.0, "channel_capacity_ratio": 0.7071, "clock_rate_ratio": 0.7071},
            {"r_over_rs": 3.0, "channel_capacity_ratio": 0.8165, "clock_rate_ratio": 0.8165},
            {"r_over_rs": 5.0, "channel_capacity_ratio": 0.8944, "clock_rate_ratio": 0.8944},
            {"r_over_rs": "infinity", "channel_capacity_ratio": 1.0, "clock_rate_ratio": 1.0}
        ]
    }

    json_path = os.path.join(DATA_DIR, "sim_time_dilation_bandwidth.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2)
    print(f"Saved dataset: {json_path}")


if __name__ == "__main__":
    run_simulation()
