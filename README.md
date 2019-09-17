# Posters

# Demo: 'https://posters-app.herokuapp.com/'

## The User's

When deciding upon the purpose of my App, I considered creating an app in which users will be able to buy and own there favourite superhero/ villian posters.
I idea is that users can create their own accounts with a personal user name and browse the site until they find the product they love.
The user will be able to add a particular quantity of product to the cart, Once in the cart the user can review what they are about to purchase and amend the quantity
by either adding or subtracting. 
Once ready the user can select the checkout and they will be prompted to enter their payment details including delivery address.
In order to go to checkout the user must first login.
The user will be able to easily tell if they are signed in or out. 

### Features
#### The Home Page:
The home page or index page will open where are the products are. from here users will be able to select a quantity and add to cart.
From here the user can select 'shopping cart' And then checkout, If they are not logged in, They will be redirected to the login screen.
From the Home screen nav-bar the user can select Register, Log in or Shopping Cart. 
Once Logged in the user can select Profile, Support Log out and Shopping Cart. 


#### The Support Page:
Here the user will see a form where they can provide a name, email and also what ever questions or issues they are having and this will be sent via email. 
From this screen the user will be able to access everything in the nav-bar. They will also be able to select the logo and be brought back to the Home page. 
 

#### The Profile Page:
This page will confirm to the user that they are Logged in successfully and what email they are signed in with. 
The user will also be able to search for whatever product they are looking using the search bar.
They can also access everything in the nav-bar just like above. 

#### The Login Page:
From here the user will be able to Log into their account that would have already Registered for.
They will have to enter a username or an email and a Password. If they have forgotten their Password they can click on the forgot Password
link and reset it.
If the user has come this far but does not already have an account, they can clcik on the Register button in the nav-bar and create an account.  


#### The Register Page:
From the Register Page the user can create an account. They will need to enter a username and follow the required steps.
They will also need an email address and they will have to create a Password and confirm it also.
Once they click create account and all the information is correct and the username or email doesn't already exist, their account
will be created and they can now log in using those details. 
If the user finds themselves here but they already have an account, they can click on the sign in link and sign into that account instead. 
The Passwords will have to match or an error will display.
Once Registered, The user will be signed in automatically. 

#### The Shopping Cart:
On this page the user will be able to see everything they have in their basket, An image of the products and also the total cost.
If they click the checkout button, they will be redirected to a payment method screen.

#### Log out:
When a user is signed in, they will see the option to Log out in the navigation bar.
Once they Log out successfully they will see a message on the screen saying so. 

#### The Payment Page:
Once the user is ready to place their order, they can click on Checkout and they will be redirected to the payment page.
Here the user will have to enter their details:  Name, address, phone number and card details.
I have set up the payment method via Stripe so once the user clicks on submit payment, Stripe will take care of the rest.  

## Testing.

##### Navigation Bar:
Click on the login and fill in the details in order to sign in.
Click on Register and do the same. 
Whatever screen you are on, click on the logo, 'Comic Wall' And it will bring you back to the Products page. 
Click on Shopping Cart and see what items are in the Cart. 
When signed in, click Support in the Navigation bar and fill out the details. 
Click on Profile and you can see what user is logged in. 
Click log out and it will render a message letting you know that the user is logged out. 
   
##### Social Links:
On each page there will be a like and a Share button, the user can Log into their Facebook Accounts and like the page
and Share the site. 

##### Support email form:
    - Go to Support page and fill out the form.
    - Type in your name. If nothing is entered an error will come after 
      you click the sign-up Button.
    - Type your email. Again an error will pop up if nothing is entered 
      or if the '@' Symbol isn't included.
    - I have tested the Emailjs with multiple email address on all screen sizes
      and received every email to my email address: Nathan.duggan0@gmail.com
##### The Login Page:
    - Here the user will have to enter their username and password that they would have already 
      created.
    - If the user enters wrong information then an error will appear telling the user that their 
      credentials are incorrect. 
    - If they have not yet registered, they can do so by clicking on the link 
      below the password box. 
##### Register Page:
    - Here the user will have to enter their name, create a username and create a password.
    - They will have to create a username that doesn't already exist, if it does, 
      they will see an error. 
    - Once they have successfully created an account, 
      they will be redirected to the Login screen page so that they can Login. 

## How it looks on different screen sizes and browsers:
   - Mobile: The pages fit in nicely, '375 X 667'. The Navigation bar is changed to a Hamburger drop down.
   - Tested ‘Support Form', Logging in and Registering across all screen sizes.
   - Tablet: Again, fits nicely '768 X 1024'. The Navigation stays the same as Desktop screen.
   - All photos and text fit in. Text is centred. 
   - I have tested all screens on multiple Browsers, including,
     Google Chrome, Safari, Firefox and Internet Explorer.
## Deployment: 
    - I have deployed this project on both Github and Heroku
    - I first ran a git init and started to track my files/images and committed them and then 
      pushed them up to Github, were they all open and load with no issues. 
    - I then logged into my github profile page and clicked on my project's name.
    - Clicked on settings, scrolled down to Github Pages,
    - Under source, Selected master branch. 
    - Deployment Github Link: https://github.com/Nathanduggan/posters
    Heroku:
    - Heroku Deployment: Python package runs the http server for the app, the
      Procfile gives Heroku the information to run the app and requirements.txt is a file that
      contains all the Python packages required to run the app.
    - Heroku Link: https://posters-app.herokuapp.com/
    - I deployed my project on Heroku. Link: https://posters-app.herokuapp.com/
    - I first ran a git init and started to track my files/images and committed them and then 
      pushed them up to Heroku, were they all open and load with no issues.
    - After setting up the Heroku account I simple connect Heroku with Github
      and pushed the code and deployed the Branch.

## Issues during deployment
    - I came across a number of issues while trying to deploy to Heroku.
    - I had multiple application errors or web pages not found errors.
    - I used all my resources to finally resolve the issues and learnt a lot in the process.
    - Some issues I came across: I decided to move from AWS Cloud9 To Visual Stduio Code 
      as I Thought AWS Was very restrictive.
    - While using VSC, I hadn't installed certain softwares correctly like psycopg2 Or whitenoise.
    - Thankfully after some troubeshooting I managed to get the project deployed on Heroku. 

## Contents:
   - The Images on each paged are from Google Images.
   - The Navigation bar is from Materialise,
   - The icons are from Google Icons
 

## Acknowledgment: 
     This will be my final project so I Would like to firstly thank my Mentor Guido,
     Who has helped me throughout the past Year, has always made time for me and
     worked tirelessly when I had complex issues.
     I would like to acknowledge my partner Natasha and my Dad who encouraged me to start 
     this course in the pursuit of bettering my career prospects. 
     Lastly I would like to thank everyone who works with the Code Institute tutoring support,
     They really helped me a lot during this Project, they were always friendly and made asking 
     for help easy. 
