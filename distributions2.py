import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import erlang
from scipy.stats import f
from scipy.stats import chi2

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
    distribution  =st.selectbox(
        "Distribution",
        [
            "chi-square",
            "F",
            "Erlang"
        ]
    )
    st.text("Enter value or use - and +")
    if distribution == "chi-square":
        df = st.number_input(
            "Degrees of freedom",
            min_value=1,
            step=1,
            value=1,
            key=11
        )
    elif distribution == "F":
        df1 = st.number_input(
            "Degrees of freedom 1",
            min_value=1,
            value=1,
            step=1,
            key=12
        )
        df2 = st.number_input(
            "Degrees of freedom 2",
            min_value=1,
            value=1,
            step=1,
            key=13
        )
    else:
        shape = st.number_input(
            "Shape",
            min_value=1,
            step=1,
            value=1,
            key=14
        )

    check = st.checkbox("Add second distribution")

    if check:
        if distribution == "chi-square":
            df2 = st.number_input(
                "Degrees of freedom",
                min_value=1,
                step=1,
                value=1,
                key=21
            )
        elif distribution2 == "F":
            df12 = st.number_input(
                "Degrees of freedom 1",
                min_value=1,
                value=1,
                step=1,
                key=22
            )
            df22 = st.number_input(
                "Degrees of freedom 2",
                min_value=1,
                value=1,
                step=1,
                key=23
            )
        else:
            shape2 = st.number_input(
                "Shape",
                min_value=0,
                step=1,
                value=1,
                key=24
            )

with col2:
    if check:
        fig, ax = plt.subplots()
        if distribution == "chi-square":
            x = np.linspace(chi2.ppf(0.0001, df), chi2.ppf(0.999, df))
            ax.plot(x, chi2.pdf(x=x, df=df), alpha=0.5)
            ax.set(xlabel='X', ylabel="Density")
            title1=("chi-square( %d )" %(df))
            x2 = np.linspace(chi2.ppf(0.0001, df2), chi2.ppf(0.999, df2))
            ax.plot(x2, chi2.pdf(x=x2, df=df2), color='darkorange', alpha=0.5)
            ax.set(xlabel='X', ylabel="Density")
            title2=("chi-square( %d )" %(df2))
            ax.legend([title1, title2])
        elif distribution == "F":
            x = np.linspace(f.ppf(0.0001, df1, df2), f.ppf(0.9999, df1, df2), 100)
            ax.plot(x, f.pdf(x=x, dfn=df1, dfd=df2), alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title1=('F(%d, %d)' %(df1, df2))
            x2 = np.linspace(f.ppf(0.0001, df12, df22), f.ppf(0.9999, df12, df22), 100)
            ax.plot(x2, f.pdf(x=x2, dfn=df12, dfd=df22), color='darkorange', alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title2=('F(%d, %d)' %(df12, df22))
            ax.legend([title1, title2])
        else:
            x = np.linspace(erlang.ppf(0.0001, scale=scale), erlang.ppf(0.9999, scale=scale), 100)
            ax.plot(x, erlang.pdf(x=x, scale=scale), alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title1=('Erlang(%d)' %scale)
            x2 = np.linspace(erlang.ppf(0.0001, scale=scale2), erlang.ppf(0.9999, scale=scale2), 100)
            ax.plot(x2, erlang.pdf(x=x2, scale=scale2), color='darkorange', alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title2=('Erlang(%d)' %scale2)
            ax.legend([title1,title2])
    else:
        fig, ax = plt.subplots()
        if distribution == "chi-square":
            x = np.linspace(chi2.ppf(0.0001, df), chi2.ppf(0.999, df))
            ax.plot(x, chi2.pdf(x=x, df=df), alpha=0.5)
            ax.set(xlabel='X', ylabel="Density")
            title1=("chi-square( %d )" %(df))
            ax.title.set_text(title1)
        elif distribution == "F":
            x = np.linspace(f.ppf(0.0001, df1, df2), f.ppf(0.9999, df1, df2), 100)
            ax.plot(x, f.pdf(x=x, dfn=df1, dfd=df2), alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title1=('F(%d, %d)' %(df1, df2))
            ax.title.set_text(title1)
        else:
            x = np.linspace(erlang.ppf(0.0001, scale=scale), erlang.ppf(0.9999, scale=scale), 100)
            ax.plot(x, erlang.pdf(x=x, scale=scale), alpha=0.5)
            ax.set(xlabel='X', ylabel='Density')
            title1=('Erlang(%d)' %scale)
            ax.title.set_text(title1)

    st.pyplot(fig)
   # check2 = st.checkbox("Show description")
   # if check2:
   #     if check:
   #         if distribution == "binomial":
   #             mean1=nobs*prob
   #             stdev1=(nobs*(prob)*(1-prob))**0.5
   #             lower1=int(binom.ppf(0.001, nobs, prob))
   #             upper1=int(binom.ppf(0.999, nobs, prob))
   #             alttext1= "Probability distribution graph of a %s distribution. The distribution \
   #             has a mean of %0.2f and a standard deviation of %0.2f. The 0.001 quantile is %02d \
   #             and the 0.999 quantile is %02d." %(title1, mean1, stdev1, lower1, upper1)
   #         elif distribution == "t":
   #             mean1=0
   #             stdev1=(df/(df-2))**0.5
   #             lower1=t.ppf(0.001, df)
   #             upper1=t.ppf(0.999, df)
   #             alttext1= "Probability distribution curve of a %s distribution. The distribution \
   #             is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
   #             of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
   #             %(title1, mean1, stdev1, lower1, upper1)
   #         else:
   #             mean1=meanmu
   #             stdev1=stsigma
   #             lower1=norm.ppf(0.001, meanmu, stsigma)
   #             upper1=norm.ppf(0.999, meanmu, stsigma)
   #             alttext1= "Probability distribution curve of a %s distribution. The distribution \
   #             is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
   #             of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
   #             %(title1, mean1, stdev1, lower1, upper1)

#            if distribution2 == "binomial":
#                mean2=nobs2*prob2
#                stdev2=(nobs2*(prob2)*(1-prob2))**0.5
#                lower2=int(binom.ppf(0.001, nobs2, prob2))
#                upper2=int(binom.ppf(0.999, nobs2, prob2))
#                alttext2= "A second distribution is also shown of the probability distribution graph \
#                of a %s distribution. The distribution has a mean of %0.2f and a standard deviation \
#                of %0.2f. The 0.001 quantile is %02d and the 0.999 quantile is %02d." \
#                %(title2, mean2, stdev2, lower2, upper2)
#            elif distribution2== "t":
#                mean2=0
#                stdev2=(df2/(df2-2))**0.5
#                lower2=t.ppf(0.001, df2)
#                upper2=t.ppf(0.999, df2)
#                alttext2= "A second distribution is also shown of the probability distribution curve \
#                of a %s distribution. The distribution is unomodal, symmetric, and bell-shaped with a \
#                mean of %0.2f and a standard deviation of %0.2f. The 0.001 quantile is %0.2f and the \
#                0.999 quantile is %0.2f." %(title2, mean2, stdev2, lower2, upper2)
#            else:
#                mean2=meanmu2
#                stdev2=stsigma2
#                lower2=norm.ppf(0.001, meanmu2, stsigma2)
#                upper2=norm.ppf(0.999, meanmu2, stsigma2)
#                alttext2= "A second distribution is also shown of the probability distribution curve \
#                of a %s distribution. The distribution is unomodal, symmetric, and bell-shaped with a \
#                mean of %0.2f and a standard deviation of %0.2f. The 0.001 quantile is %0.2f and the \
#                0.999 quantile is %0.2f." %(title2, mean2, stdev2, lower2, upper2)  
#            st.write(alttext1 + " " + alttext2)          
#        else:
#            if distribution == "binomial":
#                mean1=nobs*prob
#                stdev1=(nobs*(prob)*(1-prob))**0.5
#                lower1=int(binom.ppf(0.001, nobs, prob))
#                upper1=int(binom.ppf(0.999, nobs, prob))
#                alttext1= "Probability distribution graph of a %s distribution. The distribution \
#                has a mean of %0.2f and a standard deviation of %0.2f. The 0.001 quantile is %02d \
#                and the 0.999 quantile is %02d." %(title1, mean1, stdev1, lower1, upper1)
#            elif distribution == "t":
#                mean1=0
#                stdev1=(df/(df-2))**0.5
#                lower1=t.ppf(0.001, df)
#                upper1=t.ppf(0.999, df)
#                alttext1= "Probability distribution curve of a %s distribution. The distribution \
#                is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
#                of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
#                %(title1, mean1, stdev1, lower1, upper1)
#            else:
#                mean1=meanmu
#                stdev1=stsigma
#                lower1=norm.ppf(0.001, meanmu, stsigma)
#                upper1=norm.ppf(0.999, meanmu, stsigma)
#                alttext1= "Probability distribution curve of a %s distribution. The distribution \
#                is unomodal, symmetric, and bell-shaped with a mean of %0.2f and a standard deviation \
#                of %0.2f. The 0.001 quantile is %0.2f and the 0.999 quantile is %0.2f."\
#                %(title1, mean1, stdev1, lower1, upper1)
#            st.write(alttext1)
