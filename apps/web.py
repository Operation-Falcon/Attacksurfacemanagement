import streamlit as st
import os

def app():
    with st.form(key="Web assets"):
        st.header("Web assets")
        search=st.text_input("Enter the domain name")
        st.header(" ")
        submit=st.form_submit_button()
    
    if submit:
        try:
            cwd=os.getcwd()
            path=os.path.join(cwd, "web_assets", "Subdomain_results")
            with open(f"{path}/all_domains.txt", "r") as file:
                file=file.readlines()
                with st.beta_expander("subdomains"):
                    st.write(file)

            
            cwd=os.getcwd()
            path=os.path.join(cwd, "web_assets", "Web_service_results")
            with open(f"{path}/all_web_service.txt", "r") as file:
                file=file.readlines()
                with st.beta_expander("web service"):
                    st.write(file)


            cwd=os.getcwd()
            path=os.path.join(cwd, "web_assets", "Crawler")
            with open(f"{path}/gospider.txt", "r") as file:
                file=file.readlines()
                with st.beta_expander("crawler"):
                    st.write(file)


            cwd=os.getcwd()
            path=os.path.join(cwd, "web_assets", "Internet_archive")
            with open(f"{path}/waybackurls.txt", "r") as file:
                file=file.readlines()
                with st.beta_expander("Wayback urls"):
                    st.write(file)
                            

        except Exception as e:
            print(e)