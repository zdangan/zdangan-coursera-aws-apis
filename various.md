SSH key:

https://medium.com/sonabstudios/setting-up-github-on-aws-cloud9-with-ssh-2545c4f989ea

<p>GitHub on AWS Cloud9 with SSH
<ol>
<li>Generate RSA Key Pair:  $ ssh-keygen -t rsa (press enter when prompted for file name)</li>
<li>Copy Public Key: $ cd ~/.ssh & cat id_rsa.pub</li>
<li>In your Github profile go to Settings->SSH and GPG keys-> New SSH key, and paste the Public Key from the above step</li>
<li>Add SSH Key to the SSH Agent:
    <ul>
    <li>Start your ssh-agent in the background: $ eval $(ssh-agent -s)</li>
    <li>Add your ssh key: $ ssh-add id_rsa</li>
    </ul>
</li>
</ol>    
</p>
    
    
    
    
<p>
Virtual Environment:
<ol>
<li>python -m venv venv</li>
<li>source venv/bin/activate</li>
<li>deactivate</li>
</ol>    
</p>