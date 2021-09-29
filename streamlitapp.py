import pandas as pd 
import numpy as np 
#import matplotlib.pyplot as plt 

import streamlit as st 

st.title(' Historical Fundamental Screener')

st.write("This app can be used to filter and rank stocks based on financial ratios and test their 10 year performance")


import yfinance as yf 

#symbol = st.text_input("Enter Company Name:", 'RELIANCE')

#symbol='RELIANCE'
#yy=2011
#data=yf.download(tickers=[symbol+'.NS'],start=str(yy)+'-09-01',end=str(yy+10)+'-08-31')
#st.line_chart(data['Close'])

data=pd.read_csv('complete_backtester_refined.csv')
data['Change']=data['Close_Price']/data['Start_Price']
data.drop(columns=['ROCE_average'],inplace=True)
for i in data.columns:
  if i not in ['year','Company','Month']:
    if data[i].dtypes!='float64':
      data[i]=data[i].astype('str').str.replace(',','').str.replace('%','').astype('float')

data['Year']=data['Year'].astype('int')
#Now create some standard ratios and you are done!!. Also, make the results shown in the end of the app nice and easy to comprehend!
data['ROE']=data['Net Profit']/data['Share Capital']
data['PE']=data['Start_Price']/data['EPS in Rs']
data['DivYield']=data['Dividend Payout %']*data['EPS in Rs']/(100*data['Start_Price'])
data['Shares_Outstanding']=data['Net Profit']*10000000/data['EPS in Rs']
data['PricetoSales']=data['Start_Price']*data['Shares_Outstanding']/(data['Sales']*10000000)
st.write('Create Ratios')
val="data['Share Capital']"

agree = st.checkbox("I want to create a new ratio",key="1")
if agree==True:

	new_col_name=st.text_input("Enter Name for new Ratio",key="1")
	val="data['Share Capital']"

	val=st.text_input("Enter equation for new Ratio",key="1")
	





	if val:
		data[new_col_name]= eval(val)


agree2 = st.checkbox("I want to create a new ratio",key="2")
if agree2==True:

	new_col_name=st.text_input("Enter Name for new Ratio",key="2")
	val="data['Share Capital']"

	val=st.text_input("Enter equation for new Ratio",key="2")
	






	if val:
		data[new_col_name]= eval(val)


agree3 = st.checkbox("I want to create a new ratio",key="3")
if agree3==True:

	new_col_name=st.text_input("Enter Name for new Ratio",key="3")
	val="data['Share Capital']"

	val=st.text_input("Enter equation for new Ratio",key="3")
	






	if val:
		data[new_col_name]= eval(val)



agree4 = st.checkbox("I want to create a new ratio",key="4")
if agree4==True:

	new_col_name=st.text_input("Enter Name for new Ratio",key="4")
	val="data['Share Capital']"

	val=st.text_input("Enter equation for new Ratio",key="4")
	






	if val:
		data[new_col_name]= eval(val)



agree5 = st.checkbox("I want to create a new ratio",key="5")
if agree5==True:

	new_col_name=st.text_input("Enter Name for new Ratio",key="5")
	val="data['Share Capital']"

	val=st.text_input("Enter equation for new Ratio",key="5")
	






	if val:
		data[new_col_name]= eval(val)




	
colz=list(data.columns)
for i in ['year','Company','Month']:
	colz.remove(i)

st.write('SELECTION CRITERIA 1')


option1 = st.selectbox(
   'Ratio',
     colz)

option2=st.selectbox(
	'sign',('>=',">","<","<=")



	)
option3=st.number_input(
	'value')

if option2=='>=':
	sub=data[data[option1]>=option3]

elif option2=='>':
	sub=data[data[option1]>option3]

elif option2=='<=':
	sub=data[data[option1]<=option3]

elif option2=='<':
	sub=data[data[option1]<option3]


more_filts1=st.checkbox('More filters',key="1")
if more_filts1==True:
	st.write('SELECTION CRITERIA 2')


	option1 = st.selectbox(
	   'Ratio',
	     colz,key="2")

	option2=st.selectbox(
		'sign',('>=',">","<","<="),key="2"




		)
	option3=st.number_input(
		'value',key="2")

	if option2=='>=':
		sub=sub[sub[option1]>=option3]

	elif option2=='>':
		sub=sub[sub[option1]>option3]

	elif option2=='<=':
		sub=sub[sub[option1]<=option3]

	elif option2=='<':
		sub=sub[sub[option1]<option3]


more_filts2=st.checkbox('More filters',key="2")
if more_filts2==True:
	st.write('SELECTION CRITERIA 3')


	option1 = st.selectbox(
	   'Ratio',
	     colz,key="3")

	option2=st.selectbox(
		'sign',('>=',">","<","<="),key="3"




		)
	option3=st.number_input(
		'value',key="3")

	if option2=='>=':
		sub=sub[sub[option1]>=option3]

	elif option2=='>':
		sub=sub[sub[option1]>option3]

	elif option2=='<=':
		sub=sub[sub[option1]<=option3]

	elif option2=='<':
		sub=sub[sub[option1]<option3]

more_filts3=st.checkbox('More filters',key="3")
if more_filts3==True:
	st.write('SELECTION CRITERIA 4')


	option1 = st.selectbox(
	   'Ratio',
	     colz,key="4")

	option2=st.selectbox(
		'sign',('>=',">","<","<="),key="4"




		)
	option3=st.number_input(
		'value',key="4")

	if option2=='>=':
		sub=sub[sub[option1]>=option3]

	elif option2=='>':
		sub=sub[sub[option1]>option3]

	elif option2=='<=':
		sub=sub[sub[option1]<=option3]

	elif option2=='<':
		sub=sub[sub[option1]<option3]



more_filts4=st.checkbox('More filters',key="4")
if more_filts4==True:
	st.write('SELECTION CRITERIA 5')


	option1 = st.selectbox(
	   'Ratio',
	     colz,key="5")

	option2=st.selectbox(
		'sign',('>=',">","<","<="),key="5"




		)
	option3=st.number_input(
		'value',key="5")

	if option2=='>=':
		sub=sub[sub[option1]>=option3]

	elif option2=='>':
		sub=sub[sub[option1]>option3]

	elif option2=='<=':
		sub=sub[sub[option1]<=option3]

	elif option2=='<':
		sub=sub[sub[option1]<option3]



st.write('Rank By')
rankopt=st.selectbox('Ratio to rank stocks by',colz)
ascopt=st.selectbox('',options=('ascending','descending'))
heads=st.number_input('How many Companies ?',min_value=1, value=5, step=1)

if ascopt:
	if ascopt=='ascending':
		xx=True
	elif ascopt=='descending':
		xx=False

gains=[]
for year in [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]:
  subb=sub[sub['Year']==year]
  subb=subb.sort_values(rankopt,ascending=xx)
  subb=subb.head(heads).reset_index(drop=True)
  print(np.mean(subb['Change']))
  gains.append(np.mean(subb['Change']))
  st.write(subb[['Company','Year','Change']].head(heads))
  st.write('The return for the year '+str(year)+' is ' + str(int(100*(np.mean(subb['Change'])-1)))+' %')


gainz=np.prod(gains)**0.1
gainz-=1
gainz*=100
gainz=int(gainz)
st.write('10 Year Strategy CAGR : '+str(gainz)+' %')
st.line_chart(np.cumprod(gains))

st.write('Performance of Nifty')
symbol='^NSEI'
yy=2011
data=yf.download(tickers=[symbol],start=str(yy)+'-09-01',end=str(yy+10)+'-08-31')
st.line_chart(data['Close'])











