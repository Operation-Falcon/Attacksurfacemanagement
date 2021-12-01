import streamlit as st
from multiapp import MultiApp
from apps import home, web, network, sourcecode, bcid, cloud, cia, dataleaks, emaildiscovery, isai, isd, socialmedia # import your app modules here
st.set_page_config(layout="wide")
app = MultiApp()

st.markdown("""
# Attack Surface Management
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Web", web.app)
app.add_app("Network", network.app)
app.add_app("Source code", sourcecode.app)
app.add_app("Business communication and infrastructure discovery", bcid.app)
app.add_app("Cloud", cloud.app)
app.add_app("Company Information and Associations", cia.app)
app.add_app("Data Leaks", dataleaks.app)
app.add_app("Email discovery", emaildiscovery.app)
app.add_app("Internet scan and archived information", isai.app)
app.add_app("Internet survey data", isd.app)
app.add_app("Social Media", socialmedia.app)

# The main app
app.run()