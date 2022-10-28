#!/usr/bin/env python

# https://fdm.dk/nyheder/bilist/2022-01-nu-bliver-det-dyrere-holde-bil-hvad-koster-din-bil-dig-2022

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def price_l(km_l):
    """Pricing in DKK"""
    _df = pd.DataFrame({"price/liter": np.arange(8, 20, 0.5)})
    _df["price/km"] = _df["price/liter"] / km_l
    return _df


def price_kwh(km_k):
    """Pricing in DKK"""
    _df = pd.DataFrame({"price/kwh": np.arange(0.05, 10, 0.01)})
    _df["price/km"] = _df["price/kwh"] / (km_k)
    return _df


def create_plot_1():
    fig = plt.figure()

    # Get data
    df_l = price_l(km_l)
    df_k = price_kwh(km_k)

    # km/l
    ax1 = fig.add_subplot(111)
    ax1.plot(df_l["price/km"], df_l["price/liter"], label="price/liter")
    ax1.set_ylabel("Price/liter")
    # ax1.set_ylim([0, None])

    # km/kwh
    ax2 = ax1.twinx()
    ax2.plot(df_k["price/km"], df_k["price/kwh"], "r", label="price/kwh")
    ax2.set_ylabel("Price/kWh")
    # ax2.set_ylim([0, None])

    # Shared settings
    ax1.set_title("Comparison of price/liter and price/kwh")
    ax1.set_xlabel("Price/km")
    ax2.set_xlim([0, 5.0])
    ax1.grid()
    ax1.legend()
    ax2.legend()

    # Create the plot
    st.pyplot(plt)


# Create the sliders
km_k = st.slider(label="km/kWh", value=3.5, min_value=1.0, max_value=15.0, step=0.5)
km_l = st.slider(label="km/liter", value=15.0, min_value=5.0, max_value=35.0, step=0.5)

# Start values
create_plot_1()
