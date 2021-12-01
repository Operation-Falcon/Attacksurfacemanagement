import streamlit as st
import os

def app():
    with st.form(key="Network assets"):
        st.header("Network assets")
        search=st.text_input("Enter the domain name")
        st.header(" ")
        submit=st.form_submit_button()
    
    if submit:
        try:
            cwd=os.getcwd()
            path=os.path.join(cwd, "network_assets")
            with open(f"{path}/all_ipv4.txt", "r") as file:
                file=file.readlines()
                with st.beta_expander("ip address"):
                    st.write(file)

            
                    

        except Exception as e:
            print(e)