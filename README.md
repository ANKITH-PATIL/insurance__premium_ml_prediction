# insurance__premium_ml_prediction
This machine learning project predicts the premium of the insurance

```
CI-CD Pipleine:

CI: changing your code and sending the changes to the github 
CD: When the deployement criteria satisfies then the trigger is triggered 

```
how to clone from github repo
```
```
create a github repo
go on code and copy the https link of the repo
go to terminal of your system
git clone *paste the link* 
```
```
next steps : edit the repo using the VS code
```
```
type dir in command prompt
type cd *project name*
type code . *for opening the file in the vscode*
```

```
Advantages of maintaining the virtual environment for the project
```
```
its a lighter option than creating a new conda environment because as its stored in the same directory(folder).Thus, when u delete the project from your system the virtual environment also gets deleted
```

```
creating requirements.txt file
```
```
create a simple flask application
check its working for checking the reu=quirements.txt
```
```
to check the versions of the project which is created after every git commit
```
```
git log
```
```
how to deploy the model to heroku
```
```
To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = ankithpatilbusiness@gmail.com
2. HEROKU_API_KEY = 957321a3-aaea-4d90-a826-e9c5a897db68
3. HEROKU_APP_NAME = insurance-premiumapp


heroku api key you will get from the the account setting on the heroku website 
```
BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```

```
NEXT STEPS :
```
```
create a folder .github
and within that folder make another folder of workflows
and within that create main.yaml file 

then add readymade template to that file

then add the secrets to your github account(in settings>> secrets>> actions>> new repo secrets) to make sure that whatever secrets u have put in the main.yaml file for the deployemnet of the contd deployement of the(changes u have done to the code) contd integration. 
```
```


