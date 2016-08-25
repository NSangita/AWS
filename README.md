# AWS
AWS 

This project discusses about how to use boto(Python library that provides you with an easy way to interact with and automate using various Amazon Web Services) to 
- create one user in AWS. 
- creating multiple users in AWS by reading a file which contains users in each line 

The steps I followed are:

1. Install pip 

  a) Download get-pip.py.
  b) Open a command prompt(run as administrator) in windows and navigate to the folder containing get-pip.py.
  c) Then run 
        python get-pip.py
  d) Check weather installed by typying pip in the command prompt
  
2. Install boto Library in Windows
  
  a) Downlload the boto package to your computer from say: http://boto.googlecode.com/files/boto-2.6.0.tar.gz
  b) Unzip it. Traverse to the unzipped folder using CMD prompt.
  c) run the following command in the command prompt
      setup.py install
  d) Verify the installation by trying to run import boto in python idle.
  e)If you have pip installed you can run.
      pip install -U boto
      
3. Sign in into the AWS Management Console 
  a) Create a AWS User (Save the Access Key Id and Secret Access Key) for the user.
  b  Save the credentails to your local disk.
  c) Create a group for the same user
  
  
4. Install the AWS CLI Using the MSI Installer (Windows) 
  a) Refer http://docs.aws.amazon.com/cli/latest/userguide/installing.html#choosing-an-installation-method
  b) Run the downloaded MSI installer.
  c) Follow the instructions that appear.
  
5. Configuring the AWS Command Line Interface
  a) Open a command prompt(run as an adminstrator) and run
      aws configure 
  b) It will prompt 
        AWS Access Key ID [None]: 
        AWS Secret Access Key [None]: 
        Default region name [None]: 
        Default output format [None]: 
    Enter the credentials here reffering the 3)b)
    
6. Run the createUser.py(in python idle) and it will create a single user in the AWS Console.

7. Run the readFileCreateUser.py(in python idle) and it will create multiple users reading the file(in this case createUser.txt)
   in the AWS Console.
        
  
      
