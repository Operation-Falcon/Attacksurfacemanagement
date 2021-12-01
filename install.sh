#!/bin/bash

#making the directory Tools

{

    mkdir -p /root/Tools

    #installing pip3
    echo installing pip3
    sudo apt-get install python3-pip

    #installing golang 
    echo installing golang
    sudo apt-get install golang-go -qq -y

    #installing jupyter notebook
    echo installing jupyter notebook
    sudo apt-get install jupyter-notebook
    
    #Downloading commonspeak wordlist
    wget https://raw.githubusercontent.com/assetnote/commonspeak2-wordlists/master/subdomains/subdomains.txt
    mv subdomains.txt /usr/share/amass/wordlists/subdomains.txt
    
    #Downloading goaltdns wordlist
    wget https://raw.githubusercontent.com/subfinder/goaltdns/master/words.txt
    mv words.txt /usr/share/amass/wordlists/words.txt

    #installing subfinder
    echo installing subfinder
    go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
    sudo mkdir -p /root/Tools/subfinder
    sudo cp /root/go/bin/subfinder /root/Tools/subfinder/
    sudo cp /root/go/bin/subfinder /usr/local/bin/subfinder

    #installing httpx
    echo installing httpx
    go get -v github.com/projectdiscovery/httpx/cmd/httpx
    sudo mkdir -p /root/Tools/httpx
    sudo cp /root/go/bin/httpx /root/Tools/httpx
    sudo cp /root/go/bin/httpx /usr/local/bin/httpx

    #installing waybackurls
    echo installing waybackurls
    go get github.com/tomnomnom/waybackurls
    sudo mkdir -p /root/Tools/waybackurls
    sudo cp /root/go/bin/waybackurls /root/Tools/waybackurls
    sudo cp /root/go/bin/waybackurls /usr/local/bin/waybackurls

    #installing gowitness
    echo installing gowitness
    go get -u github.com/sensepost/gowitness
    sudo mkdir -p /root/Tools/gowitness
    sudo cp /root/go/bin/gowitness /root/Tools/gowitness
    sudo cp /root/go/bin/gowitness /usr/local/bin/gowitness

    #installing hakrawler
    echo installing hakrawler
    go get github.com/hakluke/hakrawler
    sudo mkdir -p /root/Tools/hakrawler
    sudo cp /root/go/bin/hakrawler /root/Tools/hakrawler
    sudo cp /root/go/bin/hakrawler /usr/local/bin/hakrawler


    #installing shuffledns
    echo installing shuffledns
    go get -v github.com/projectdiscovery/shuffledns/cmd/shuffledns
    sudo mkdir -p /root/Tools/shuffledns
    sudo cp /root/go/bin/shuffledns /root/Tools/shuffledns
    sudo cp /root/go/bin/shuffledns /usr/local/bin/shuffledns

    #installing naabu 
    echo installing naabu
    go get -v github.com/projectdiscovery/naabu/v2/cmd/naabu
    sudo mkdir -p /root/Tools/naabu
    sudo cp /root/go/bin/naabu /root/Tools/naabu
    sudo cp /root/go/bin/naabu /usr/local/bin/naabu

    #installing dnsx
    echo installing dnsx
    go get -v github.com/projectdiscovery/dnsx/cmd/dnsx
    sudo mkdir -p /root/Tools/dnsx
    sudo cp /root/go/bin/dnsx /root/Tools/dnsx
    sudo cp /root/go/bin/dnsx /usr/local/bin/dnsx

    #installing gf 
    echo installing gf
    go get -u github.com/tomnomnom/gf
    echo 'source /root/go/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
    source ~/.bashrc
    cp -r /root/go/src/github.com/tomnomnom/gf/examples ~/.gf
    sudo mkdir -p /root/Tools/gf
    sudo cp /root/go/bin/gf /root/Tools/gf
    sudo cp /root/go/bin/gf /usr/local/bin/gf

    #installing nuclei
    echo installing nuclei 
    go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei
    sudo mkdir -p /root/Tools/nuclei
    sudo cp /root/go/bin/nuclei /root/Tools/nuclei
    sudo cp /root/go/bin/nuclei /usr/local/bin/nuclei

    #installing dalfox
    echo installing dalfox
    go get -v github.com/hahwul/dalfox/v2
    sudo mkdir -p /root/Tools/dalfox
    sudo cp /root/go/bin/dalfox /root/Tools/dalfox
    sudo cp /root/go/bin/dalfox /usr/local/bin/dalfox

    #installing ffuf
    echo installing ffuf
    go get -u github.com/ffuf/ffuf
    sudo mkdir -p /root/Tools/ffuf
    sudo cp /root/go/bin/ffuf /root/Tools/ffuf
    sudo cp /root/go/bin/ffuf /usr/local/bin/ffuf
 
    #installing massdns
    echo installing massdns
    cd /root/Tools
    git clone https://github.com/blechschmidt/massdns.git
    cd massdns
    make
    cd bin
    sudo mkdir -p /root/Tools/massdns
    sudo cp massdns /root/Tools/massdns
    sudo cp massdns /usr/local/bin/massdns

    #installing sectrails
    echo installing sectrails
    cd /root/Tools
    git clone https://github.com/Deepanjalkumar/sectrails.git
    cd sectrails
    pip3 install -r requirements.txt

    #installing hunter
    echo installing hunter
    cd /root/Tools
    git clone https://github.com/Deepanjalkumar/hunter.git
    cd hunter
    pip3 install -r requirements.txt

    
    #installing github search
    echo installing github search
    cd /root/Tools
    git clone https://github.com/gwen001/github-search.git
    cd github-search
    pip3 installing -r requirements3.txt

    #installing webdork
    echo installing webdork
    cd /root/Tools
    git clone https://github.com/Deepanjalkumar/webdork.git
    cd webdork
    pip3 installing -r requirements3.txt

    #installing cloud enum
    echo installing cloud enum
    cd /root/Tools
    git clone https://github.com/Deepanjalkumar/cloud_enum.git
    cd cloud_enum
    pip3 installing -r requirements3.txt

    #installing bypass firewall by dns history
    echo installing bypass firewall by dns history
    cd /root/Tools
    git clone https://github.com/Deepanjalkumar/bypass-firewalls-by-DNS-history.git
    cd bypass-firewalls-by-DNS-history
    

}
