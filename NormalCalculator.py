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
    st.write('Normal Distribution')
    meanmu = st.number_input(
        "Mean",
        value=0.00,
        step=0.01,
        key=11
    )
    stsigma = st.number_input(
        "Standard deviation",
        min_value=0.00,
        value=1.00,
        step=0.01,
        key=12    
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
        x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
        ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), color='tab:blue')
        ax.set(xlabel='X', ylabel='Density')
        title1=('normal(%0.3f, %0.3f)' %(meanmu, stsigma))
        ax.title.set_text(title1)
        plt.ylim(bottom=0)  
        if probability == "P(X < value)":    
            x2 = np.linspace(norm.ppf(0.0001, meanmu, stsigma), value1, 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, norm.pdf(value1, loc=meanmu, scale=stsigma)), scaley = False, color='tab:orange')
            probcalc = norm.cdf(value1,loc=meanmu, scale=stsigma)
            text="P(X < %0.3f) = %0.3f" %(value1, probcalc) 
        elif probability == "P(X > value)":     
            x2 = np.linspace(value1, norm.ppf(0.9999, meanmu, stsigma), 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, norm.pdf(value1, loc=meanmu, scale=stsigma)), scaley = False, color='tab:orange')
            probcalc = 1-norm.cdf(value1,loc=meanmu, scale=stsigma)
            text="P(X > %0.3f) = %0.3f" %(value1, probcalc)
        else:     
            x2 = np.linspace(value1, value2, 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((value1, value1), (-.02, norm.pdf(value1, loc=meanmu, scale=stsigma)), scaley = False, color='tab:orange')
            ax.plot((value2, value2), (-.02, norm.pdf(value2, loc=meanmu, scale=stsigma)), scaley = False, color='tab:orange')
            probcalc = norm.cdf(value2,loc=meanmu, scale=stsigma)-norm.cdf(value1,loc=meanmu, scale=stsigma)
            text="P(%0.3f < X < %0.3f) = %0.3f" %(value1, value2, probcalc)
    elif calculate == "Value given probability":
        fig, ax = plt.subplots()
        x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
        ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), color='tab:blue')
        ax.set(xlabel='X', ylabel='Density')
        title1=('normal(%0.3f, %0.3f)' %(meanmu, stsigma))
        plt.ylim(bottom=0) 
        ax.title.set_text(title1)
        if tail == "lower tail":
            valresult=norm.ppf(prob, meanmu, stsigma)
            x2 = np.linspace(norm.ppf(0.0001, meanmu, stsigma), valresult, 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((valresult, valresult), (-.02, norm.pdf(valresult, loc=meanmu, scale=stsigma)), scaley = False, color='tab:orange')
            text="P(X < %0.3f) = %0.3f" %(valresult, prob)
        elif tail == "upper tail":
            valresult=norm.ppf((1-prob), meanmu, stsigma)
            x2 = np.linspace(valresult, norm.ppf(0.9999, meanmu, stsigma), 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((valresult, valresult), (-.02, norm.pdf(valresult, loc=meanmu, scale=stsigma)), scaley = False, color='tab:orange')
            text="P(X > %0.3f) = %0.3f" %(valresult, prob)
        else:
            valresult1=norm.ppf((1-prob)/2, meanmu, stsigma)
            valresult2=norm.ppf(1-(1-prob)/2, meanmu, stsigma)
            x2 = np.linspace(valresult1, valresult2, 100)
            y2 = norm.pdf(x=x2, loc=meanmu, scale=stsigma)
            ax.plot(x2, y2, color='tab:blue')
            ax.fill_between(x2, 0, y2, color='tab:orange', alpha=0.6)
            ax.plot((valresult1, valresult1), (-.02, norm.pdf(valresult1, loc=meanmu, scale=stsigma)), scaley = False, color='tab:orange')
            ax.plot((valresult2, valresult2), (-.02, norm.pdf(valresult2, loc=meanmu, scale=stsigma)), scaley = False, color='tab:orange')
            text="P(%0.3f < X < %0.3f) = %0.3f" %(valresult1, valresult2, prob)            
    else:
        fig, ax = plt.subplots()
        x = np.linspace(norm.ppf(0.0001, meanmu, stsigma), norm.ppf(0.9999, meanmu, stsigma), 100)
        ax.plot(x, norm.pdf(x=x, loc=meanmu, scale=stsigma), color='tab:blue')
        ax.set(xlabel='X', ylabel='Density')
        title1=('normal(%0.3f, %0.3f)' %(meanmu, stsigma))
        ax.title.set_text(title1)
        plt.ylim(bottom=0) 
        text=""
    st.pyplot(fig)
    st.markdown(f"""<div style='text-align: center'>{text}</h1>""", unsafe_allow_html=True)

    check2 = st.checkbox("Show description")
    if check2:
        mean1=meanmu
        stdev1=stsigma
        lower1=norm.ppf(0.001, meanmu, stsigma)
        upper1=norm.ppf(0.999, meanmu, stsigma)
        alttext1= "Probability distribution curve of a %s distribution. The distribution \
        is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
        of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
        %(title1, mean1, stdev1, lower1, upper1)

        if calculate == "Probability given value":
            alttest2 = "The calculated probability, %s is %0.3f" %(probability, prob)
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


 

