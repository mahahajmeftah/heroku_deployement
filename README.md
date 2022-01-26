# heroku_deployment (ML Model /Flask)
After creating your model , train it and setting up your web app .
It's time to deploy it to the cloud. in our case we use heroku using Github  and not the CLI :
to do so the first step is :
### Add a Procfile file 
go to your project and add a Procfile file.It should be without extension like "Procfile.txt" , just "Procfile" 
write inside the file the following code:
```python
web: gunicorn app:app
```
### Add a requirements.txt 

requirements.txt

### Comitting Code in a github repostitory:

create a github repository and upload the folder that contains your project 
![image](https://user-images.githubusercontent.com/77198470/151109991-95b866b0-096a-4e60-939c-0f0f93682b3c.png)

### Create and app on heroku 
* click on Create new app

![image](https://user-images.githubusercontent.com/77198470/151108696-1a446c7a-712c-4a16-a790-8e2aa855b984.png)
* Enter Your app name and Click Create 

![image](https://user-images.githubusercontent.com/77198470/151110081-27daacac-7175-4ebd-a1a5-9958940ab720.png)
* click on Connect to GitHub

![image](https://user-images.githubusercontent.com/77198470/151110396-96636e20-5b28-49c2-8c78-4086e2107e45.png)
* choose the repository where you had uploaded the project  code  in the search and Click connect 
![image](https://user-images.githubusercontent.com/77198470/151110537-bddcdd2a-85d9-4224-b80a-60d7bdf116b1.png)
* Click deploy Branch
 
 ![image](https://user-images.githubusercontent.com/77198470/151111375-d52774bf-71fb-4a88-8693-b3b479ad1f37.png)
 
* your app was successfully deployed

 ![image](https://user-images.githubusercontent.com/77198470/151111490-bcd7b0b6-74c1-41dc-b027-c8355987ee61.png)
  
 
* Testing your app 
click view app

The app is published at URL:https://heruko-deployment-app.herokuapp.com/









