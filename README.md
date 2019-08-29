# Posters

# Demo: 'https://posters-app.herokuapp.com/'

## The User's

When deciding upon the purpose of my App, I considered creating an app in which users will be able to select a product, add it to a cart and enter payment details.
Users will also be able to register for an account and log in and log out as they please.
A username, email and strong passowrd will be required. 
/*------------------------------*/

### Features
#### The Home Page:
The home page or index page will open where are the products are. from here users will be able to select a quantity and add to cart.
From here the user select 'shopping cart' And then checkout, If they are not logged in, They will be redirected to the login screen.
From the Home screen nav-bar the user can select Register, Log in or Shopping Cart. Once Logged in
the user can select Profile, Support Log out and Shopping Cart. 


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
Once they click create account and all thge information is correct and the username of email doesn't already exist, their account
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
I have set up the payment method via Stripe so once the user click on submit payment, Stripe will take care of the rest.  

## Testing.

##### Navigation Bar:
Click on the login and file in the details in order to sign in.
Click on Register and do the same. 
Whatever screen you are on, click on the logo, 'Comic Wall' And it will bring you back to the Products page. 
Click on Shopping Cart and see what items are in the Cart. 
When signed in, click Support in the Navigation bar and fill out the details. 
Click on Profile and you can see what user is logged in. 
Click log out and it will render a message letting you know that the user is logged out. 
   
##### Social Links: /*-----------------*/
On each page there will be a like and a Share button, the user can Log into their Facebook Accounts and like the page
and Share the site. 

##### Support email form:
    - Go to Support page and will out the form.
    - Type in your name. If nothing is entered an error will come after you click the sign-up Button.
    - Type your email. Again an error will pop up if nothing is entered or if the '@' Symbol isn't
       included.
    - When the user clciks in the email, name or questions box, the background 
      will turn grey in color and once the
      user starts to type the text will be in white.
    - I have tested the Emailjs with multiple email address on all screen sizes
      and received every email to my email address: Nathan.duggan0@gmail.com
##### The Login Page:
    - Here the user will have to enter their username and password that they would have already 
      created.
    - If the user enters wrong information then an error will appear telling the user that their 
      credentials are incorrect. 
    - If they have not yet registered, they can do so by clicking on the link below the password box. 
##### Register Page:
    - Here the user will have to enter their name, create a username and create a password.
    - They will have to create a username that doesn't already exist or less they will get an error. 
    - Once they have successfully created an account, they will be redirected to the Login screen page 
      so that they can Login. 

## How it looks on different screen sizes and browsers:
   - Mobile: The pages fit in nicely, '375 X 667'. The Navigation bar is changed to a Hamburger drop down.
   - Everything else fits in a 'Col-xs-12' Grid including the Footer 
   - Tested ‘Sign up form’, Links in footer and ‘Read more’ button and all Works.
   - Tablet: Again, fits nicely '768 X 1024'. The Navigation stays the same as Desktop screen.
   - The Footer Links are indented inwards, and I have hidden some text on Mobile and Tablet Screens for display purposes.
   - All photos and text fit in. Text is centred. 
   - I have tested all screens on multiple Browsers, including,
     Google Chrome, Safari, Firefox and Internet Explorer.
## Deployment: 
    - I deployed my project on Heroku. Link: https://posters-app.herokuapp.com/
    - I first ran a git init and started to track my files/images and committed them and then 
      pushed them up to Heroku, were they all open and load with no issues. 
## Contents:
   - The Images on each paged are from Google Images.
   - The Navigation bar is from Materialise, Along with the drop down menu for the Notes.
   - The icons are from Google Icons
 

## Acknowledgment: 
     I received inspiration for this project from my partner Natasha Thompson (Tash). Tash is a  
     Teacher in Bray and was always complaining that the children are never organised with 
     Homework/Notes Etc
     I would also like to thank my mentor Guido . His support throughout has been
     of great assistance. 
     Lastly, I would like to acknowledge my dad who encouraged me to start this course in the 
     pursuit of bettering my career prospects. 
