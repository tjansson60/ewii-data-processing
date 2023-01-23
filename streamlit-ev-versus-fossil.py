#!/usr/bin/env python

# https://fdm.dk/nyheder/bilist/2022-01-nu-bliver-det-dyrere-holde-bil-hvad-koster-din-bil-dig-2022

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


CURRENCY = "kr"


def price_l(km_l, price_per_unit):
    """Pricing in DKK"""
    _df = pd.DataFrame({"price/unit": price_per_unit})
    _df["price/km"] = _df["price/unit"] / km_l
    return _df


def price_kwh(kwh_100km, price_per_unit):
    """Pricing in DKK"""
    _df = pd.DataFrame({"price/unit": price_per_unit})
    _df["price/km"] = _df["price/unit"] / (100 / kwh_100km)
    return _df


def create_plot_1():
    fig = plt.figure(
        # figsize=(16, 9)
    )

    # Get data
    price_per_unit = np.arange(0, 18, 0.5)
    df_l = price_l(km_l, price_per_unit)
    df_k = price_kwh(kwh_100km, price_per_unit)

    # Plots
    ax1 = fig.add_subplot(111)
    ax1.plot(df_l["price/unit"], df_l["price/km"], label=f"Fossil [{CURRENCY}/l]")
    ax1.plot(df_k["price/unit"], df_k["price/km"], label=f"Electric [{CURRENCY}/kWh]")

    # Shared settings
    ax1.set_title(f"Fossil vs Electric cars by {CURRENCY}/km")

    ax1.set_ylabel(f"{CURRENCY}/km")
    ax1.set_xlabel(f"{CURRENCY}/kWh or {CURRENCY}/l")

    # ax1.set_ylim([0, None])
    ax1.legend()
    ax1.grid()

    # Create the plot
    st.pyplot(plt)


# Create the sliders
kwh_100km = st.slider(label="kWh/100km", value=20.0, min_value=10.0, max_value=40.0, step=1.0)
km_l = st.slider(label="km/liter", value=15.0, min_value=5.0, max_value=35.0, step=0.5)

# Start values
create_plot_1()
