import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import t

hide = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body {overflow: hidden;}
    div.block-container {padding-top:1rem;}
    div.block-container {padding-bottom:1rem;}
    </style>
    """

st.markdown(hide, unsafe_allow_html=True)

col1, col2 = st.columns([2,3])

with col1:
    st.write('t Distribution')
    df = st.number_input(
        "Degrees of freedom",
        min_value=0,
        step=1,
        value=10,
        key=11
    )

    calculate = st.selectbox(
        "Calculate",
        [
            "no calculation",
            "Probability given value",
            "Value given probability"
        ]
        )

    if calculate == "Probability given value":
        probability = st.selectbox(
            "Probability",
            [
                "P(X < value)",
                "P(X > value)",
                "P(value1 < X < value2)"
            ]
        )
        if probability == "P(value1 < X < value2)":
            value1 = st.number_input(
                "value1",
                value=0.000,
                step=0.001,
                key=21
            )
            value2 = st.number_input(
                "value2",
                value=0.000,
                step=0.001,
                key=22
            )
            
        else:
            value1 = st.number_input(
                "value",
                value=0.000,
                step=0.001,
                key=23
            )
   
    if calculate == "Value given probability":
        tail = st.selectbox(
            "Location",
            [
                "lower tail",
                "upper tail",
                "middle"
            ]
        )
        prob = st.number_input(
                "Desired probability",
                min_value=0.000,
                max_value=1.000,
                value=0.500,
                step=0.001,
                key = 3.1
        )

with col2:
    if calculate == "Probability given value":
        fig, ax = plt.subplots()
        x = np.linspace(t.ppf(0.0001, df=df), t.ppf(0.9999, df=df), 100)
        ax.plot(x, t.pdf(x=x, df=df), color='tab:blue')
        ax.set(xlabel='X', ylabel='Density')
        title1=('t(%02d)' %df)
        ax.title.set_text(title1)
        plt.ylim(bottom=0)  
        if probability == "P(X < value)":    
            x2 = np.linspace(t.ppf(0.0001, df=df), value1, 100)
            y2 = t.pdf(x=x2, df=df)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, t.pdf(value1, df=df)), scaley = False, color='tab:orange')
            probcalc = t.cdf(value1, df=df)
            text="P(X < %0.3f) = %0.3f" %(value1, probcalc) 
        elif probability == "P(X > value)":     
            x2 = np.linspace(value1, t.ppf(0.9999, df=df), 100)
            y2 = t.pdf(x=x2, df=df)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, t.pdf(value1, df=df)), scaley = False, color='tab:orange')
            probcalc = 1-t.cdf(value1,df=df)
            text="P(X > %0.3f) = %0.3f" %(value1, probcalc)
        else:     
            x2 = np.linspace(value1, value2, 100)
            y2 = t.pdf(x=x2, df=df)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, t.pdf(value1, df=df)), scaley = False, color='tab:orange')
            ax.plot((value2, value2), (-.02, t.pdf(value2, df=df)), scaley = False, color='tab:orange')
            probcalc = t.cdf(value2, df=df)-t.cdf(value1, df=df)
            text="P(%0.3f < X < %0.3f) = %0.3f" %(value1, value2, probcalc)
    elif calculate == "Value given probability":
        fig, ax = plt.subplots()
        x = np.linspace(t.ppf(0.0001, df=df), t.ppf(0.9999, df=df), 100)
        ax.plot(x, t.pdf(x=x, df=df), color='tab:blue')
        ax.set(xlabel='X', ylabel='Density')
        title1=('t(%02d)' %df)
        plt.ylim(bottom=0) 
        ax.title.set_text(title1)
        if tail == "lower tail":
            valresult=t.ppf(prob, df=df)
            x2 = np.linspace(t.ppf(0.0001, df=df), valresult, 100)
            y2 = t.pdf(x=x2, df=df)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((valresult, valresult), (-.02, t.pdf(valresult, df=df)), scaley = False, color='tab:orange')
            text="P(X < %0.3f) = %0.3f" %(valresult, prob)
        elif tail == "upper tail":
            valresult=t.ppf((1-prob), df=df)
            x2 = np.linspace(valresult, t.ppf(0.9999, df=df), 100)
            y2 = t.pdf(x=x2, df=df)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((valresult, valresult), (-.02, t.pdf(valresult, df=df)), scaley = False, color='tab:orange')
            text="P(X > %0.3f) = %0.3f" %(valresult, prob)
        else:
            valresult1=t.ppf((1-prob)/2, df=df)
            valresult2=t.ppf(1-(1-prob)/2, df=df)
            x2 = np.linspace(valresult1, valresult2, 100)
            y2 = t.pdf(x=x2, df=df)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((valresult1, valresult1), (-.02, t.pdf(valresult1, df=df)), scaley = False, color='tab:orange')
            ax.plot((valresult2, valresult2), (-.02, t.pdf(valresult2, df=df)), scaley = False, color='tab:orange')
            text="P(%0.3f < X < %0.3f) = %0.3f" %(valresult1, valresult2, prob)            
    else:
        fig, ax = plt.subplots()
        x = np.linspace(t.ppf(0.0001, df=df), t.ppf(0.9999, df=df), 100)
        ax.plot(x, t.pdf(x=x, df=df), color='tab:blue')
        ax.set(xlabel='X', ylabel='Density')
        title1=('t(%02d)' %df)
        ax.title.set_text(title1)
        plt.ylim(bottom=0) 
        text=""
    st.pyplot(fig)
    st.markdown(f"""<div style='text-align: center'>{text}</h1>""", unsafe_allow_html=True)

    check2 = st.checkbox("Show description")
    if check2:
        mean1=0
        stdev1=(df/(df-2))**0.5
        alttext1= "Probability distribution curve of a %s distribution. The distribution \
        is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
        of %0.2f." %(title1, mean1, stdev1)

        if calculate == "Probability given value":
            alttext2 = "The calculated probability is %s." %(text)
        elif calculate == "Value given probability":
            if tail == "lower tail":
                alttext2 = "The value such that P( X < value) = %0.3f is %0.3f, %s." %(prob, valresult, text)
            elif tail == "upper tail":
                alttext2 = "The value such that P( X > value) = %0.3f is %0.3f, %s." %(prob, valresult, text)
            else:
                alttext2 = "The middle %0.3f of the distribution lies between %0.3f and %0.3f, %s." %(prob, valresult1, valresult2, text)
        else:
            alttext2=""
        st.write(alttext1)
        st.write(alttext2)

