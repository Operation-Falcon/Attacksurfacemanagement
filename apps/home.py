import streamlit as st


def app():
    st.title('Overview')

    col1, col2, col3=st.beta_columns(3)
    with col1:
        with st.form(key="web"):
            st.subheader("Web Assets")
            st.text("OPTIONS: ")
            st.text("subdomains")
            st.text("web services")
            st.text("internet archive")
            st.text("crawler")
            st.text("others")
            web_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if web_input=="subdomains":
            with st.beta_expander("overview"):
                st.text("it will give you subdomain from different \n"
                        "sources. it scrape, enumerate and brute  \n"
                        "forces to find subdomains")
        elif web_input=="web services":
            with st.beta_expander("overview"):
                st.text("web services will check for running http &\n"
                        "https service and put them in txt file \n"
                        "format")
        elif web_input=="internet archive":
            with st.beta_expander("overview"):
                st.text("it will collect urls and endpoints from\n"
                        "sources such as wayback machine and threat \n"
                        "exchange")
        elif web_input == "crawler":
            with st.beta_expander("overview"):
                st.text("it will crawl all urls, endpoints, js and \n"
                        "any other sources which are used in website \n"
                        "including third party support too.")
        elif web_input == "others":
            with st.beta_expander("overview"):
                st.text("others include information such as possible  \n"
                        "vulnerable endpoints which can be exploited  \n"
                        "to get the desirable results")
    with col2:
        with st.form(key="Network"):
            st.subheader("Network Assets")
            st.text("OPTIONS:")
            st.text("ipv4")
            st.text("ipv6")
            st.text("open ports")
            st.text("nmap results")
            st.text("brute force service")
            network_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if network_input=="ipv4":
            with st.beta_expander("overview"):
                st.text("it will give you ipv4 address by resolving \n"
                        "domain name to ip address and grepping them \n"
                        "using regular expression.")
        elif network_input=="ipv6":
            with st.beta_expander("overview"):
                st.text("it will give you ipv6 address by resolving \n"
                        "domain name to ip address and grepping them \n"
                        "using regular expression.")
        elif network_input=="open ports":
            with st.beta_expander("overview"):
                st.text("it will give you open ports running on those \n"
                        "ipv4 and ipv6 address  \n")
        elif network_input=="nmap results":
            with st.beta_expander("overview"):
                st.text("it will give you nmap results in a nice and \n"
                        "decent format for better effectiveness \n")
        elif network_input=="brute force service":
            with st.beta_expander("overview"):
                st.text("it will give you successful brute force results \n"
                        "on those running  servies \n")
    with col3:
        with st.form(key="Source code"):
            st.subheader("Source code")
            st.text("OPTIONS:")
            st.text("employee github account")
            st.text("contributors github account")
            st.text("users github account")
            st.text("sensitive secrets search")
            st.text("historical github search")
            source_code_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if source_code_input=="employee github account":
            with st.beta_expander("overview"):
                st.text("it will give list of users belonging to \n"
                        "particular organization which can be further\n"
                        "inspected for vulnerabilities")
        elif source_code_input=="contributors github account":
            with st.beta_expander("overview"):
                st.text("it will give list of contributors belonging to \n"
                        "particular organization which can be further\n"
                        "inspected for vulnerabilities")
        elif source_code_input=="users github account":
            with st.beta_expander("overview"):
                st.text("it will give list of users belonging to \n"
                        "particular organization which can be further\n"
                        "inspected for vulnerabilities")
        elif source_code_input=="sensitive secrets search":
            with st.beta_expander("overview"):
                st.text("Performing sensitive search on github account\n"
                        "belonging to the organization\n")
        elif source_code_input=="historical github search":
            with st.beta_expander("overview"):
                st.text("Performing historical search on github account\n"
                        "belonging to the organization\n")
    col4, col5, col6=st.beta_columns(3)
    with col4:
        with st.form(key="Email discovery"):
            st.subheader("Email discovery")
            st.text("OPTIONS :")
            st.text("email address based on domain name")
            st.text("online presence of email address")
            st.text("Verify email address ? real or fake")
            email_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if email_input=="email address based on domain name":
            with st.beta_expander("overview"):
                st.text("Find email address using domain name")
        elif email_input=="online presence of email address":
            with st.beta_expander("overview"):
                st.text("Finding Online presence of email address")
        elif email_input=="Verify email address ? real or fake":
            with st.beta_expander("overview"):
                st.text("verify the email address (FAKE, OR TRASH ONE )")
    with col5:
        with st.form(key="Infrastructure Discovery"):
            st.subheader("Infrastructure Discovery")
            st.text("OPTIONS :")
            st.text("mx records")
            st.text("details")
            st.text("exchange services")
            infrastructure_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if infrastructure_input=="mx records":
            with st.beta_expander("overview"):
                st.text("Find mail server responsible for communication")
        elif infrastructure_input=="details":
            with st.beta_expander("overview"):
                st.text("Details about particular dommain")
        elif infrastructure_input=="exchange services":
            with st.beta_expander("overview"):
                st.text("Details about office exchange services")

    with col6:
        with st.form(key="Data Leaks"):
            st.subheader("Data Leaks")
            st.text("OPTIONS :")
            st.text("leaked credentials")
            st.text("breached data")
            st.text("email address")
            data_leaks_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if data_leaks_input=="leaked credentials":
            with st.beta_expander("overview"):
                st.text("Hunting for leaked credentials")
        elif data_leaks_input=="breached data":
            with st.beta_expander("overview"):
                st.text("Hunting for breached data")
        elif data_leaks_input=="email address":
            with st.beta_expander("overview"):
                st.text("Hunting for email address in breached data")
    col7, col8, col9=st.beta_columns(3)
    with col7:
        with st.form(key="Social Media"):
            st.subheader("Socail Media")
            st.text("OPTIONS :")
            st.text("linkedin")
            st.text("glassdor")
            st.text("socialblade")
            st.text("social-searcher")
            st.text("checkuser")
            social_media_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if social_media_input=="linkedin":
            with st.beta_expander("overview"):
                st.text("enumerating employess found on linkedin")
        elif social_media_input=="glassdor":
            with st.beta_expander("overview"):
                st.text("enumerating employess found on glassdor")
        elif social_media_input=="socialblade":
            with st.beta_expander("overview"):
                st.text("hunting for targets on social platform")
        elif social_media_input=="social-searcher":
            with st.beta_expander("overview"):
                st.text("hunting for targets on social platform")
        elif social_media_input=="checkuser":
            with st.beta_expander("overview"):
                st.text("hunting for targets on communication platform")
    with col8:
        with st.form(key="Company Information"):
            st.subheader("Company Information")
            st.text("OPTIONS :")
            st.text("iexcloud")
            st.text("crunchbase")
            st.text("clearbit")
            st.text("maattermark")
            st.text("opencorporate")
            company_information_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if company_information_input=="iexcloud":
            with st.beta_expander("overview"):
                st.text("company information including third party association\n")
        elif company_information_input=="crunchbase":
            with st.beta_expander("overview"):
                st.text("company information including third party association\n")
        elif company_information_input=="clearbit":
            with st.beta_expander("overview"):
                st.text("company information including third party association\n")
        elif company_information_input=="maattermark":
            with st.beta_expander("overview"):
                st.text("company information including third party association\n")
        elif company_information_input=="opencorporate":
            with st.beta_expander("overview"):
                st.text("company information including third party association\n")

    with col9:
        with st.form(key="Internet Survey Data"):
            st.subheader("Internet Survey Data")
            st.text("OPTIONS :")
            st.text("shodan")
            st.text("binary edge")
            st.text("security trails")
            st.text("riskiq")
            st.text("censys")
            Internet_survey_input=st.text_input("Enter the assets")
            submit_button = st.form_submit_button(label='Submit')
        if Internet_survey_input=="shodan":
            with st.beta_expander("overview"):
                st.text("Shodan is a search engine that lets the user\n"
                        "find specific types of computers connected to\n "
                        "the internet using a variety of filters")
        elif Internet_survey_input=="binary edge":
            with st.beta_expander("overview"):
                st.text("It scan the internet and acquire data that\n"
                        "can be transformed into threat intelligence\n"
                        "feeds or security reports")
        elif Internet_survey_input=="security trails":
            with st.beta_expander("overview"):
                st.text("SecurityTrails enables you to explore\n"
                        "complete current and historical data\n"
                        "for any internet assets")
        elif Internet_survey_input=="riskiq":
            with st.beta_expander("overview"):
                st.text("It provides cloud-based software as a\n"
                        "service for organizations to detect\n"
                        "phishing, fraud, malware, and other\n"
                        "online security threats.")
        elif Internet_survey_input=="censys":
            with st.beta_expander("overview"):
                st.text("Censys provides a comprehensive inventorn\n"
                        "of your Internet assets drawn from our\n"
                        "Internet Discovery Algorithm and cloud\n"
                        "connectors")

    with st.form(key="Internet Scan Archived Information"):
        st.subheader("Internet Scan Archived Information")
        st.text("OPTIONS :")
        st.text("waybackmachine")
        st.text("shodan")
        st.text("censys")
        st.text("project sonar")
        Internet_scan_input = st.text_input("Enter the assets")
        submit_button = st.form_submit_button(label='Submit')
    if Internet_scan_input == "waybackmachine":
        with st.beta_expander("overview"):
            st.text("The Wayback Machine is a digital archive of the World Wide Web it allows the user to go back in time and see how websites looked in the past")
    elif Internet_scan_input == "shodan":
        with st.beta_expander("overview"):
            st.text("Shodan is a search engine that lets the user find specific types of computers connected to the internet using a variety of filters.\n"
                    "Some have also described it as a search engine of service banners, which are metadata that the server sends back to the client")
    elif Internet_scan_input == "censys":
        with st.beta_expander("overview"):
            st.text("Censys provides a comprehensive inventory of your Internet assets drawn from our Internet Discovery Algorithm and cloud connectors")
    elif Internet_scan_input == "project sonar":
        with st.beta_expander("overview"):
            st.text("Project Sonar started in September of 2013 with the goal of improving security through the active analysis of public networks.\n"
                    "While the first few months focused almost entirely on SSL, DNS, and HTTP enumeration, the discoveries and insights derived from these datasets,\n"
                    "especially around the identification of systems unknown to IT teams, led to the expansion of Project Sonar to include the scanning of UDP services")
