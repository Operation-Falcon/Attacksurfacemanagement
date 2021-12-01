# Attacksurfacemanagement

# Note : You can run it in parallel to cover a vast majority of assets in less time. I suggest to give it a try

# Installation :

     git clone https://github.com/Deepanjalkumar/Attacksurfacemanagement.git
     
     cd Attacksurfacemanagement
     
     source notebook/bin/activate
     
     pip3 install -r requirements.txt
     
     ./install.sh
     
     Note : If you want to get a customize theme like me then use this :
     
                   pip install jupyterthemes
                   
                   jt -t monokai
                   
![shot1](https://user-images.githubusercontent.com/55708909/132466189-0a474476-ea62-4851-8826-e19c26f47b23.png)
     
# Usage/Examples :

     jupyter-notebook --allow-root
     
     select the directory offensive-notebook
     
     Inside it there all lots of engine which covers various aspect of hacking. Choose as per your requirement and start hacking.
     
     Now lets look at the other feature of it i.e sharing information on a real time . 
       
                    uvicorn api:app --reload ( Uvicorn running on http://127.0.0.1:8000 )
                    
                    /web/subdomain
                    
                    /web/web-service
                    
                    /web/internet-archive
                    
                    /web/crawler
                    
                    /web/all-files
                    
                    /web/cve-paths
                    
                    /web/juicy-paths
                    
                    /web/leaky-misconfigs
                    
                    /web/juicy-paths
                    
                    /network/ipv4
                    
                    It is flexible as you can create your own endpoints
                    
    For visual inspection and monitor mode i have used streamlit to have a visual analysis of whole AttackSurfaceManagement framework.
    
                    streamlit run dashboard.py
                    
                                    Local URL: http://localhost:8501
  
                                    Network URL: http://192.168.43.20:8501
                                    
                    Monitor the  AttackSurfaceManagement framework as per your needs.
                    
  ![rest](https://user-images.githubusercontent.com/55708909/132473053-247da829-5478-4c83-a614-b625a5459a1d.png)

  ![asm](https://user-images.githubusercontent.com/55708909/132473224-4e4e64b8-8f28-4e3d-a922-018d6430b2ff.png)
  
  ## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Feedback

If you have any feedback, please reach out to us at Linkedin Deepanjal kumar

  
## Tech Stack

**Programming Language:** PYTHON, HTML, CSS JS, GOLANG

**IDE:** VSCODE

**API:** Fastapi

**Dashboard:** Streamlit

**Notebook:** Jupyter

**Database:** SQLITE
  
## Support

For support, contact me over linkeding Deepanjal kumar

  
## API Reference


## Authors

- [@Deepanjalkumar](https://github.com/Deepanjalkumar)

  
## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
![](https://img.shields.io/badge/OS-Linux-informational?style=flat&logo=linux&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Shell-Bash-informational?style=flat&logo=gnu-bash&logoColor=white&color=2bbc8a)


  
## Contributing

Contributions are always welcome!

## Credits 

Credits goes to all the contributor whose tool has been integrated into attack surface management




