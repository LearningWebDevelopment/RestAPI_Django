# Learning Django Rest API
## Tech Stack used
- Vagrant
- VMBox
- ModHeader Chrome
- Python
- Django Web Framework
- Django REST API Framework

#### Cheat Sheets
1. [MarkDown Language](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Installing Vagrant on Ubuntu
`sudo apt update`
`sudo apt install virtualbox`

[Download Vagrant from Here](https://www.vagrantup.com/downloads "Vagrant Download Page")

`curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -`

`sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"`

`sudo apt-get update && sudo apt-get install vagrant`

[Download Vagrant Os Box from Here](https://app.vagrantup.com/ubuntu/boxes/focal64 "Vagrant Ubuntu Box Page")

In project folder - initialize vagrant in terminal  
`vagrant init ubuntu/focal64`  
configure vagrant file in the folder created by the above command  
`vagrant up`  

##### *NOTE - Please run in an external terminal not in VSCode terminal!!!*   

To connect to th VMBox  
`vagrant ssh`

To return to your machine  
`exit`  

There is folder the developer server created above that is synced with our folder   
To access it login to developer server and go to   
`cd /vagrant/`

check files using `ls`

### Create virtual environment in VMBox   
Create  
`python -m venv ~/env`  
Activate Virtual Env   
`source ~/env/bin/activate`
Deactivate Virtual Env   
`deactivate`   

### Python PIP
Here are some useful commands for working with the PIP Python Package Manager.   
Ensure you are connected to the Vagrant box and working on a Virtual Environment.    
   
**Installing Packages**   
`pip install <package-name>`   

**Saving Packages**   
`pip freeze > <destination/requirements.txt>`   

**Installing from Requirements File**   
`pip install -r <source/requirements.txt>`   

**Removing Packages**   
`pip uninstall <package-name>`   

**Updating Packages**   
`pip install --upgrade <package-name>`   

