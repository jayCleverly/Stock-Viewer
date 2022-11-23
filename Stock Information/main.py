import streamlit as st
import yfinance as yf

st.write("""
        # Stock Information
         """)

# gets data for ticker entered
ticker = st.text_input("Enter ticker").upper()
tickerData = yf.Ticker(ticker)

try:
    # gets the company name for ticker entered
    tickerName = tickerData.info['shortName']
    tickerDf = tickerData.history(start="2015-5-31")
    
    # outputs market close price graph
    st.write("""
            #### """ + tickerName + """ market close price
            """)
    st.line_chart(tickerDf.Close)
    
except:
    # company does not exist so ticker is invalid
    st.write("""
            #### Ticker does not exist 
             """)
    st.line_chart(None)
    