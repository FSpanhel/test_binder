"""
Provides plotting functions.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot(x: pd.Series[float], y: pd.Series[float]) -> plt:
    """Plots x vs. y."""
    plt.figure()
    plt.plot(x, y, "bx")
    return plt


def plot_x_vs_yy(x: pd.Series[float], y1: pd.Series, y2: pd.Series[float]) -> plt:
    """Plots x vs. y1 and y2."""
    plt.figure()
    plt.plot(x, y1, "bx")
    plt.plot(x, y2, "r-")
    return plt
