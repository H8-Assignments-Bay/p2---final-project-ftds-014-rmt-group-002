import streamlit as st
import numpy as np
import pandas as pd
import requests

# =====================================

dict = {'2' : {'Segmentation_name' : 'Champions', 
                'Segmentation_desc' : 'Bought recently, buy often, & spend the most',
                'Strategy': 'Reward them, likely to be early adopters of a new product, they will promote your brand'},
        '5' : {'Segmentation_name' : 'Potential Loyalists', 
                'Segmentation_desc' : 'Recent customer but spending a good amount & have bought more than once',
                'Strategy': 'Offer membership or loyalty programs, recommend other products to them'},
        '0' : {'Segmentation_name' : 'About to Sleep', 
                'Segmentation_desc' : 'Below average recently, frequency & monetary values - will lose them of not reactivated',
                'Strategy': 'Share valuable resources, recommend a popular product at discount, and reconnect with them'},
        '4' : {'Segmentation_name' : 'At Risk', 
                'Segmentation_desc' : 'Spent big money and purchased often but havent purchased for a long time',
                'Strategy': 'Send personalized emails to reconnect, offer discounts, and provide a helpful resource'},
        '1' : {'Segmentation_name' : 'Hibernating', 
                'Segmentation_desc' : 'Last purchase was long back - these are low spenders who have placed few orders',
                'Strategy': 'Offer other relevant products and special discounts, recreate brand value'},
        '3' : {'Segmentation_name' : 'Lost Customer', 
                'Segmentation_desc' : 'Lowest recency, frequency, & monetary scores',
                'Strategy': 'Revive interest with reach out campaign, ignore them '}}

# =====================================

st.image('Image_Header.png')

st.markdown("<h1 style='text-align: center; color: Black;'>Customer Segmentation Apps</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: Black;'>Elevate Sales of Wholesales Merchandise in the UK with RFM</h5>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'></p>", unsafe_allow_html=True)

# st.title("Customer Segmentation Apps")
# st.write("Elevate Sales of Wholesales Merchandise in the UK with RFM")

st.image('Section.png')

st.subheader('Recency (in Day)')
st.info('The Lowest The Better - How recent was the customers last purchase? Customers who recently made a purchase will still have the product on their minds and are more likely to purchase our product again.')
Recency = st.slider("Recency", min_value=0, max_value=500, value=20, step=None)

st.subheader('Frequency (in transaction amount)')
st.info('The Highest The Better - How often did this customer make a purchase in a given period? Customers who purchased once are often more likely to purchase again.')
Frequency = st.slider("Frequency", min_value=1, max_value=500, value=80, step=None)

st.subheader('Monetary (in UK sterling)')
st.info('The Highest The Better - How much money did the customer spend in a given period? Customers who spend a lot of money are more likely to spend money in the future and have a high value to a business.')
Monetary = st.slider("Monetary", min_value=3, max_value=2000, value=1000, step=None)

st.image('Section.png')

st.title("Customer Segmentation Result")

# input user
new_data_raw = {'Recency': Recency,
            'Frequency': Frequency,
            'Monetary': Monetary}

# list_data = [Recency, Frequency, Monetary]

# ubah menjadi dataframe
new_data = pd.DataFrame([new_data_raw])
# transform log
new_data = np.log(new_data+1)

URL = "https://cust-seg-backend.herokuapp.com/predict"

r = requests.post(URL, json=new_data.to_dict('records')[0])
print(r.status_code)

# interpretasikan hasil probability
if r.status_code == 200:
    res = r.json()

    st.subheader('Result of Your Customer Segmentation')
    st.write(dict[res['result']]['Segmentation_name'])

    with st.expander("Learn more | Segmentation Detail & Strategy"):

        st.subheader('Customer Segmentation Description')
        st.success(dict[res['result']]['Segmentation_desc'])

        st.subheader('Strategy or Actionable Insight')
        st.warning(dict[res['result']]['Strategy'])

else:
  st.write('Error euy')

st.markdown("<p style='text-align: center; color: grey;'></p>", unsafe_allow_html=True)
st.caption('APP by Adnan Rio & Handoko Pramulyo | FTDS 14 Hactive8 2022')