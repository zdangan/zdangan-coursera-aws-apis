SSH key:

https://medium.com/sonabstudios/setting-up-github-on-aws-cloud9-with-ssh-2545c4f989ea

GitHub on AWS Cloud9 with SSH
(1) Generate RSA Key Pair:  $ ssh-keygen -t rsa (press enter when prompted for file name)
(2) Copy Public Key: $ cd ~/.ssh & cat id_rsa.pub
(3) In your Github profile go to Settings->SSH and GPG keys-> New SSH key
(4) Add SSH Key to the SSH Agent:
    * Start your ssh-agent in the background: $ eval $(ssh-agent -s)
    * Add your ssh key: $ ssh-add id_rsa
    
    
    
    

Virtual Environment:
python -m venv venv
source venv/bin/activate
deactivate