"""Shared figure style for the BSPC calibration-support manuscript (Figs 2-7).

Import this module first in every figure script so all figures share fonts,
colours, markers and the neutral sign shading.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

MM = 1 / 25.4  # inch per mm
FULL_W = 190 * MM  # double-column width
HALF_W = 90 * MM   # single-column width

mpl.rcParams.update({
    "font.family": "serif",
    "font.serif": ["STIXGeneral"],
    "mathtext.fontset": "stix",
    "font.size": 7.5,
    "axes.titlesize": 8,
    "axes.labelsize": 7.5,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7.5,
    "legend.fontsize": 7,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.major.size": 2.5,
    "ytick.major.size": 0,
    "xtick.direction": "out",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.dpi": 600,
})

# MR contrasts: Paul Tol "muted" subset, distinct from the C/F arm colours
# (blue #0072B2 / orange #E69F00) used in Fig. 1. Markers give a grayscale cue.
CONTRAST = {
    "FLAIR": dict(color="#332288", marker="o"),
    "T1": dict(color="#44AA99", marker="s"),
    "T2": dict(color="#CC6677", marker="^"),
}
CONTRASTS = ["FLAIR", "T1", "T2"]

# Ridge strength: open marker = 0.003, filled marker = 0.01 (all figures).
LAMBDA_FILL = {0.003: "open", 0.01: "filled"}

NEUTRAL = "#4D4D4D"
LIGHT = "#BDBDBD"
SHADE = "#F4F4F4"   # background for the positive (F higher error) side
ZERO = "#7F7F7F"


def sign_shading(ax, axis="x", label=True, lim=None):
    """Shade the positive side (F - C > 0, higher error with F) in light grey.

    Neutral wording only: the shading describes the sign, not quality.
    """
    if axis == "x":
        lo, hi = ax.get_xlim() if lim is None else lim
        ax.axvspan(0, max(hi, 0), color=SHADE, zorder=0, lw=0)
        ax.axvline(0, color=ZERO, lw=0.7, zorder=1)
        ax.set_xlim(lo, hi)
    else:
        lo, hi = ax.get_ylim() if lim is None else lim
        ax.axhspan(0, max(hi, 0), color=SHADE, zorder=0, lw=0)
        ax.axhline(0, color=ZERO, lw=0.7, zorder=1)
        ax.set_ylim(lo, hi)


def padded(lo, hi, frac=0.08, include_zero=True):
    if include_zero:
        lo, hi = min(lo, 0.0), max(hi, 0.0)
    span = hi - lo
    return lo - frac * span, hi + frac * span


def save(fig, stem):
    fig.savefig(f"{stem}.pdf", bbox_inches="tight", pad_inches=0.02)
    fig.savefig(f"{stem}.png", bbox_inches="tight", pad_inches=0.02)
