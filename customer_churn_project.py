
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

st.set_page_config(layout= 'wide', page_title='customer churn project')

html_title = """<h1 style="color:white;text-aligh:center;"> Customer Churn Project </h1>"""
st.markdown(html_title, unsafe_allow_html=True)

df = pd.read_csv('cleaned_df.csv',index_col=0)

x = st.sidebar.checkbox('Show Data',False,key=1)

if x:
    st.image('https://storage.googleapis.com/kaggle-datasets-images/9097496/14257610/627cb39fc8786af363d2f07abcf69112/dataset-cover.png?t=2025-12-22-14-34-11')
    st.header("DataSet")
    st.dataframe(df)

y = st.sidebar.checkbox('Churn Overview',False,key=2)

if y :
    churn_counts = df['churn'].value_counts()

    churn_overview,ax = plt.subplots(figsize=(6,6))
    ax.pie(churn_counts, labels=churn_counts.index,
        autopct='%1.1f%%', startangle=90)
    ax.set_title("Churn Rate")

    st.pyplot(churn_overview)
    st.markdown('Although the majority of customers are retained, the churn rate is relatively high,indicating a potential risk to revenue stability.')

section = st.sidebar.radio('Select Section',['Customer Behavior','Risk Factors','Service Impact'])

if section == 'Customer Behavior':
    option = st.sidebar.radio('Customer Behavior',
    ['Tenure vs Churn','Monthly Charge vs Churn','Total Charge vs Churn'])

    if option == 'Tenure vs Churn':
        st.title('Tenure vs Churn')
        fig,ax = plt.subplots(figsize=(8,5))
        sns.boxplot(x='churn', y='tenure', data=df,ax=ax)
        ax.set_title("Tenure vs Churn")
        st.pyplot(fig)
        st.markdown('Customers with shorter tenure are more likely to churn, especially in the early months.')

    elif option ==  'Monthly Charge vs Churn':
        st.title('Monthly Charge vs Churn')
        fig_1,ax = plt.subplots(figsize=(8,5))
        sns.boxplot(x='churn', y='monthly_charges', data=df,ax=ax)
        ax.set_title("Monthly Charges vs Churn")
        st.pyplot(fig_1)
        st.markdown('Churned customers tend to have higher monthly charges.')

    elif option == 'Total Charge vs Churn':
        st.title('Total Charge vs Churn')
        st.plotly_chart(px.box(data_frame=df,x='churn',y='total_charges'))
        st.markdown('Customers with higher total charges are more likely to churn, possibly due to dissatisfaction with pricing.')


elif section == 'Risk Factors':
    option = st.sidebar.radio('Risk Factors',[
    'Contract vs Churn','Payment Method vs Churn','High Support Calls','Churn by Contract and Internet Service(Heatmap)'])

    if option == 'Contract vs Churn':
        st.title('Contract vs Churn')
        fig_2,ax= plt.subplots(figsize=(8,5))
        sns.countplot(x='contract', hue='churn', data=df,ax=ax)
        ax.set_title("Contract vs Churn")
        st.pyplot(fig_2)
        ct = pd.crosstab(df['contract'], df['churn'], normalize='index')*100
        ct = ct.reset_index()
        fig_3=px.bar(ct,x='contract',y=['No','Yes'],title="Churn Percentage by Contract",labels={'value':'Percentage (%)', 'variable':'Churn'},barmode='stack')
        st.plotly_chart(fig_3, use_container_width=True)
        st.markdown('Customers with month-to-month contracts show significantly higher churn rates.')

    elif option == 'Payment Method vs Churn':
        st.title('Payment Method vs Churn')
        fig_4,ax= plt.subplots(figsize=(8,5))
        sns.countplot(x='payment_method', hue='churn', data=df,ax=ax)
        ax.set_title("Payment Method vs Churn")
        st.pyplot(fig_4)
        ct_1 = pd.crosstab(df['payment_method'], df['churn'], normalize='index')*100
        ct_1 = ct_1.reset_index()
        fig_5=px.bar(ct_1,x='payment_method',y=['No','Yes'],title="Churn Percentage by Payment Method",labels={'value':'Percentage (%)', 'variable':'Churn'},barmode='stack')
        st.plotly_chart(fig_5,use_container_width=True)
        st.markdown('Payment method does not appear to significantly influence customer churn behavior.')

    elif option == 'High Support Calls':
        st.title('High Support Calls')
        fig_6,ax= plt.subplots(figsize=(8,5))
        sns.countplot(x='support_calls', hue='churn', data=df,ax=ax)
        ax.set_title("Support Calls vs Churn")
        st.pyplot(fig_6)
        ct_2 = pd.crosstab(df['support_calls'], df['churn'], normalize='index')*100
        ct_2 = ct_2.reset_index()
        fig_7=px.bar(ct_2,x='support_calls',y=['No','Yes'],title="Churn Percentage by Support Calls",labels={'value':'Percentage (%)', 'variable':'Churn'},barmode='stack')
        st.plotly_chart(fig_7,use_container_width=True)
        st.markdown('The analysis shows a strong relationship between the number of support calls and customer churn.The more technical support calls a customer makes, the greater the likelihood of losing the customer.')

    elif option == 'Churn by Contract and Internet Service(Heatmap)':
        st.title('Churn by Contract and Internet Service(Heatmap)')
        ct = pd.crosstab([df['contract'], df['internet_service']], df['churn'])

        fig_7,ax= plt.subplots(figsize=(8,6))
        sns.heatmap(ct, annot=True, fmt='d', cmap='Blues',ax=ax)

        ax.set_title("Churn by Contract and Internet Service")
        ax.set_ylabel("Contract & Internet Service")
        ax.set_xlabel("Churn")

        st.pyplot(fig_7)
        st.markdown('Customers with month-to-month contracts and fiber internet service show higher churn rates compared to other groups.')

elif section == 'Service Impact':
    option = st.sidebar.radio('Service Impact',
    ['Tech Support vs Churn','Online Security vs Churn','Internet Service vs Churn'])

    if option == 'Tech Support vs Churn':
        st.title('Tech Support vs Churn')
        fig_8,ax = plt.subplots(figsize=(8,5))
        sns.countplot(x='tech_support', hue='churn', data=df,ax=ax)
        ax.set_title("Tech Support vs Churn")
        st.pyplot(fig_8)
        ct = pd.crosstab(df['tech_support'], df['churn'], normalize='index')*100
        ct = ct.reset_index()
        fig_9=px.bar(ct,x='tech_support',y=['No','Yes'],title="Churn Percentage by Tech Support",labels={'value':'Percentage (%)', 'variable':'Churn'},barmode='stack')
        st.plotly_chart(fig_9,use_container_width=True)
        st.markdown('Customers without technical support show significantly higher churn rates.')

    elif option == 'Online Security vs Churn':
        st.title('Online Security vs Churn')
        fig_11,ax= plt.subplots(figsize=(8,5))
        sns.countplot(x='online_security', hue='churn', data=df,ax=ax)
        ax.set_title("Online Security vs Churn")
        st.pyplot(fig_11)
        ct = pd.crosstab(df['online_security'], df['churn'], normalize='index')*100
        ct = ct.reset_index()
        fig_12=px.bar(ct,x='online_security',y=['No','Yes'],title="Churn Percentage by Online Security",labels={'value':'Percentage (%)', 'variable':'Churn'},barmode='stack')
        st.plotly_chart(fig_12,use_container_width=True)
        st.markdown('Churn rates are very similar for customers with and without online security.')

    elif option == 'Internet Service vs Churn':
        st.title('Internet Service vs Churn')
        fig_13,ax =plt.subplots(figsize=(8,5))
        sns.countplot(x='internet_service', hue='churn', data=df,ax=ax)
        ax.set_title("Internet Service vs Churn")
        st.pyplot(fig_13)
        ct = pd.crosstab(df['internet_service'], df['churn'], normalize='index')*100
        ct = ct.reset_index()
        fig_14=px.bar(ct,x='internet_service',y=['No','Yes'],title="Churn Percentage by Internet Service",labels={'value':'Percentage (%)', 'variable':'Churn'},barmode='stack')
        st.plotly_chart(fig_14,use_container_width=True)
        st.markdown('Churn rates are fairly consistent across internet service types.However, customers with unknown service information show slightly higher churn, which may indicate data quality issues or dissatisfaction.')


a = st.sidebar.checkbox('Key Insights',False,key=3)

if a :
    st.header('Key Insights (Answers to Research Questions)')
    st.markdown('1. The main factors influencing churn are: \n* Short customer tenure* Month-to-month contracts\n * High monthly and total charges\n * Lack of technical support\n * High number of support calls')
    st.markdown('2. Yes, customers with month-to-month contracts have significantly higher churn rates compared to long-term contracts.')
    st.markdown('3. There is a strong negative relationship between tenure and churn.Customers with shorter tenure are more likely to leave.')
    st.markdown('4. Customers with higher monthly charges tend to show higher churn rates,indicating possible dissatisfaction with pricing.')
    st.markdown('5. Customers who receive technical support show lower churn rates compared to those without support.')
    st.markdown('6. Customers with frequent support calls are more likely to churn, suggesting higher dissatisfaction levels.')
    st.markdown('7. The most at-risk customers are:\n * New customers (low tenure)\n * Month-to-month subscribers\n * High charge users\n * Customers without technical support\n * Customers with many support calls')

b = st.sidebar.checkbox('Business Recommendations',False,key=4)

if b :
    st.header('Business Recommendations')
    st.markdown('1. Encourage long-term contracts through discounts.\n 2. Improve customer support quality.\n 3. Monitor customers with frequent complaints.\n 4. Provide loyalty programs for long-term customers.\n 5. Offer personalized plans for high-risk segments.')

c = st.sidebar.checkbox('Conclusion',False,key=5)

if c :
    st.header('Conclusion')
    st.markdown('* This project analyzed customer churn data to identify the main drivers of customer attrition. \n * Contract type, tenure, pricing, and customer support were found to be key factors influencing churn. \n * The findings can help the company improve retention strategies and enhance customer satisfaction.')

