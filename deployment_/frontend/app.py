import streamlit as st
import numpy as np
import pandas as pd
import requests

# =====================================

dict = {'2' : {'Segmentation_name' : 'Champions', 
                'Segmentation_desc' : 'Bought recently, buy often, & spend the most',
                'Strategy': 'Reward them, Share periodic notes with champions that highlight exclusive or unique products, and increase their spending by emailing them offers on multi-product orders. THEY WILL PROMOTE YOUR BRAND!'},
        '5' : {'Segmentation_name' : 'Potential Loyalists', 
                'Segmentation_desc' : 'Recent customer but spending a good amount & have bought more than once',
                'Strategy': 'Offer membership or loyalty programs, recommend other products to them, send sneak-peak news about your product (stimulate a sense of urgency to buy a new product), and express exclusivity. Loyal customers are more likely to be active buyers when they feel special.'},
        '0' : {'Segmentation_name' : 'About to Sleep', 
                'Segmentation_desc' : 'Below average recently, frequency & monetary values - will lose them of not reactivated',
                'Strategy': 'Share valuable resources, recommend a popular product at a discount (small amount), and gradually reconnect with them with a gift after purchase.'},
        '4' : {'Segmentation_name' : 'At Risk', 
                'Segmentation_desc' : 'Spent big money and purchased often but havent purchased for a long time',
                'Strategy': 'Send personalized emails, start with a 10% discount, or free shipping, then, build up gradually to a two-for-one offer or a free gift with every purchase, & provide a helpful resource.'},
        '1' : {'Segmentation_name' : 'Hibernating', 
                'Segmentation_desc' : 'Last purchase was long back - these are low spenders who have placed few orders',
                'Strategy': 'Offer other relevant products and special discounts to recreate brand value, email blasts with stories about your team or product developments might delight them enough to revisit your site, and sprinkling a discount code or two into the mix certainly helps.'},
        '3' : {'Segmentation_name' : 'Lost Customer', 
                'Segmentation_desc' : 'Lowest recency, frequency, & monetary scores',
                'Strategy': 'Revive interest with the reach-out campaign, re-engage them with a discussion about your brand and also share your future mission, or ignore them (bringing a lost customer back is the biggest challenge your nurture campaigns can tackle).'}}

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