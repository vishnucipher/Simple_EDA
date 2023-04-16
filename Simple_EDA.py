#Import Required modules
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport


#congfiguaration the webpage
st.set_page_config (page_title='Data Analysis📊',page_icon='chart.ico',layout="wide",initial_sidebar_state="expanded")

#Removing the streamlit Hamburger and Footer
st.markdown("""<style>
.css-164nlkn.egzxvld1
{
visibility:hidden;
}""",unsafe_allow_html=True)

st.image('eda.png',width=220)
#Giving titles and headers to the web app
st.markdown('''# Data Analysis 📈

- This is a simple Data Analysis web which made with `pandas`,`streamlit`,`matplotlib`and`seaborn` libraries

''')
'---'



#upload dataset
upload=st.file_uploader('**:green[Upload File(csv)]**',['csv'])

#reading  the uploaded data
if upload is not None:
    data=pd.read_csv(upload)

#using pandas profiling

if upload is not None:
    overview=ProfileReport(data)
    st.markdown('#### **:blue[📊To view the Data Analysis Overview  in One click]**')
    
    if st.button('**View Me!**'):
        st.balloons()
        st_profile_report(overview)
    
#get overal staistics
if upload is not None:
    st.write("👉 **:violet[Get overal statestics]**")
    df=data.describe()
    st.dataframe(df.style.set_properties(**{'background-color':'black','color':'green'}))

    

#showing the data
if upload is not None:
    st.markdown(" **:violet[To view the data]**")
    if st.checkbox('view data'):
        st.dataframe(data)
        
 #viewing the total data with graphs
    if upload is not None:
        st.markdown('''👉 **:violet[visualize the data into different graphs]**''')
#Lineplot
    if st.checkbox('Line'):
        columns=[]
        for i in data:
            columns.append(i)
        fig=pt.figure(figsize=(10,10),facecolor='#A0A0A0')
        ax=pt.gca()
        ax.set_facecolor('#001933')
        sns.lineplot(data)
        pt.grid(axis='both')
        pt.legend(labels=columns,facecolor='#E5FFCC')
        st.write(fig)
#histogram plot
if upload is not None:
    if st.checkbox('Histogram'):
        columns=[]
        for i in data:
            columns.append(i)
        fig=pt.figure(figsize=(10,10),facecolor='#A0A0A0')
        ax=pt.gca()
        ax.set_facecolor('#001933')
        sns.histplot(data)
        pt.grid(axis='both')
        pt.legend(labels=columns,facecolor='#E5FFCC')
        st.write(fig)
#count plot
if upload is not None:
    if st.checkbox('Count'):
        columns=[]
        for i in data:
            columns.append(i)
        fig=pt.figure(figsize=(10,10),facecolor='#A0A0A0')
        ax=pt.gca()
        ax.set_facecolor('#001933')
        sns.countplot(data)
        pt.grid(axis='both')
        pt.legend(labels=columns,facecolor='#E5FFCC')
        st.write(fig)

#show the haea and tail of the data
if upload is not None:
    st.write('👉 :violet[**Top 5 last 5 rows displayed**]')
    if st.checkbox('head'):
        df1=data.head()
        st.dataframe(df1.style.set_properties(**{'background-color':'black','color':'blue'}))
    if st.checkbox('tail'):
        df2=data.tail()
        st.dataframe(df2.style.set_properties(**{'background-color':'black','color':'blue'}))

#finding the no.of rows and columns
if upload is not None:
    st.write('👉 :violet[**The shape of data**]')
    if st.checkbox('Rows'):
        shape=data.shape
        st.write('The Number of Rows',shape[0])
        st.progress(shape[0])
    if st.checkbox('Columns'):
        shape=data.shape
        st.write('The Number of Columns',shape[1])
        st.progress(shape[1])

#checking the null values
if upload is not None:
    st.write('👉 :violet[Checking null values]')
    if st.checkbox('Null values'):
        null=data.isnull().values.any()
        if null==True:
            st.warning('Null values are present')
            st.write(":green[**Graph of Null values**]")
            fig=pt.figure(figsize=(10,10),facecolor='#A0A0A0')
            ax=pt.gca()
            ax.set_facecolor('#001933')
            sns.heatmap(data.isnull(),annot=True)
            pt.grid(axis='both')
            #pt.legend(labels=columns,facecolor='#E5FFCC')
            st.write(fig)
        else:
            st.success('NO Null values are present')

#checking the type of each column
if upload is not None:
    st.write('👉 **:violet[Datatypes of each column]**')
    st.write(data.dtypes)
    


#viewing the duplicates in dataset
if upload is not None:
    st.write("👉 **:violet[Find Dubplicates and Removing it]**")
    if st.checkbox('Duplicates'):
        
        dup=data.duplicated().any()
        st.write(dup)
        if dup:
            st.warning('This Data Set Contains Some Duplicate values')
            test=st.selectbox('Do you want to remove duplicate values',['Select One','Yes','No'])
            if test=='Yes':
                data.drop_duplicates(inplace=True)
                st.dataframe(data)
            if test=='No':
                st.text('Ok No Problem')

            


#About app

st.write('**About** **App**')
if st.button('About App'):
    
    st.text('Built With Streamlit❤️')
    st.text('Thanks To Streamlit')



