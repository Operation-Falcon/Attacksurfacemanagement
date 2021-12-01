from fastapi import FastAPI
import os

app=FastAPI()

################################# WEB ASSETS ##########################
@app.get("/web/subdomain")
def subdomain():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets", "Subdomain_results")
        with open(f"{path}/all_domains.txt", "r") as file:
            file=file.readlines()
            return {"subdomains": file}
    except Exception as e:
        print(e)

    
@app.get("/web/web-service")
def webservice():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets", "Web_service_results")
        with open(f"{path}/all_web_service.txt", "r") as file:
            file=file.readlines()
            return {"webservice": file}
    except Exception as e:
        print(e)

    
@app.get("/web/internet-archive")
def archive():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets", "Internet_archive")
        with open(f"{path}/waybackurls.txt", "r") as file:
            file=file.readlines()
            return {"archive": file}
    except Exception as e:
        print(e)



@app.get("/web/crawler")
def crawler():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets", "Crawler")
        with open(f"{path}/gospider.txt", "r") as file:
            file=file.readlines()
            return {"crawled": file}
    except Exception as e:
        print(e)

    
@app.get("/web/all-files")
def allfiles():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets")
        with open(f"{path}/all-files.txt", "r") as file:
            file=file.readlines()
            return {"all-files": file}
    except Exception as e:
        print(e)

@app.get("/web/cve-paths")
def cvepaths():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets")
        with open(f"{path}/cve-paths.txt", "r") as file:
            file=file.readlines()
            return {"cve-paths": file}
    except Exception as e:
        print(e)

@app.get("/web/juicy-paths")
def juicypaths():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets")
        with open(f"{path}/juicy-paths.txt", "r") as file:
            file=file.readlines()
            return {"juicy-paths": file}
    except Exception as e:
        print(e)

@app.get("/web/leaky-misconfigs")
def leakymisconfigs():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets")
        with open(f"{path}/leaky-misconfigs.txt", "r") as file:
            file=file.readlines()
            return {"leaky-misconfigs": file}
    except Exception as e:
        print(e)

@app.get("/web/juicy-paths")
def juicypaths():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "web_assets")
        with open(f"{path}/juicy-paths.txt", "r") as file:
            file=file.readlines()
            return {"juicy-paths": file}
    except Exception as e:
        print(e)
##############################   NETWORK ASSETS #############################

@app.get("/network/ipv4")
def ipv4():
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "network_assets")
        with open(f"{path}/all_ipv4.txt", "r") as file:
            file=file.readlines()
            return {"ipv4": file}
    except Exception as e:
        print(e)

#############################################################################
