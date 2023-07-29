# [Welcome to PC HUB](http://pchub-ac046d943cba.herokuapp.com/)

![Alt text]()

## Introduction

Welcome to my very own [PC HUB](http://pchub-ac046d943cba.herokuapp.com/).
THIS WEBISTE IS FOR EDICUATIONAL PURPOSES ONLY.
I wanted to create an full-stack e-commerce web application selling gaming computers which I am very passionate about.

### Business Type
The approach I took to this topic is a B2C type of business which means its Business To Customer.

## AGILE Methodology

### User Stories

All User Stories were successfully performed.
Each respective User Story was seperated in a milestone making for a more organised project and helping keeping track of tasks and functions planned to be implemented. Each milestone has a collection of issues that I thought would be helful towards finishing the project and i seperated them in either Fton-Ebd or Back-end.
You can access them [here](https://github.com/andreasarreqi/PcHub/milestoness)

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have. They were assigned to piriority levels "Low Priority" "Medium Priority" "high Priority" . "Must have" stories were completed first, "should haves", "could haves" and finally "Wont have". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The User Stories board was created using github projects and can be viewed to see more information on the project cards. All stories except the documentation tasks have a set of acceptance criteria in order to define the functionality that marks that story as complete.

#### Epics

The project had 7 main Epics (milestones):

EPIC 1 - Site Functionality

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.



1. As a developer, I need to set up the general functionality of the website


<details>
            <summary> 1. Acceptance Criteria </summary

                Install Django/ 
                Create Pc Hub project/ 
                Modify gitignore file/ 
                Run initial migrations

</details>
<br>



2. As a developer, I want to create the base.html page and structure so the other pages can use the layout

    <details>
            <summary> 2. Acceptance Criteria </summary>

                 Install Bootstrap
                 Create base.html file
                 Create home app
                 Create home template
                 Add home content
                 Add base.css
                 Create home page sections
                 Style home page sections
    </details>
<br>




3. As a developer, I need to create a responsive functional navigation bar

    <details>
            <summary>3. Acceptance Criteria </summary>

                Create nav links structure
                Create main nav
    </details>
<br>




4. As a developer, I need to create a footer section on the main home page so the user can have a contact emain, Privacy Policy and social media links.

    <details>
            <summary>4. Acceptance Criteria </summary>

                Create footer
                Add contact link
                Add Privacy Policy link
                Add social media link
    </details
<br>

5. As a user , I want to be able to contact the website owners



<details>
            <summary> 5. Acceptance Criteria </summary>

                Create contacts model
                Create contacts.html
                Create PC technician model
                Create pc_technician.html

</details>
<br>


6. As a developer, I need to set up AWS to store static files of the project


<details>
            <summary> Acceptance Criteria </summary>

                Create AWS account
                Create s3 bucket
                Create bucket user
                Create bucket group
                Set up config variables on settings.py file
                Test AWS static files collection

</details>
<br>

6. As a developer, I need to create error pages for the website


<details>
            <summary> Acceptance Criteria </summary>

                Create 404.html
                Create 500.htm

</details>
<br>

7. As a developer, i need to setup the application for Search Engine Optimization


<details>
            <summary> Acceptance Criteria </summary>

                Add the proper Meta tags
                Create robots.txt
                Create sitemaps
                Email Marketing Newsletter

</details>
<br>

EPIC 2 - Admin 
The Admin epic is for all stories needed for the Admin  related soories.


1. As a developer, I need to create a super user to maintain and update the website.

<details>
            <summary> 1. Acceptance Criteria</summary>
                Create super user

</details>
<br>

2. As a developer, i need t o implement create/read/update/delete functionality.


<details>
            <summary> 2. Acceptance Criteria</summary>

                Allow admin to create/read/update/delete a product on the web page
</details>
<br



3. As a developer, I need to allow the admins to add a product from the front-end features

<details>
            <summary> 3. Acceptance Criteria </summary>

                Created The view
                Create the template
                Create the form code

</details>
<br>


3. As a developer, I need to allow the admins to delete a product from the front-end


<details>
            <summary> 3. Acceptance Criteria </summary>

                Created The view
                Create the template
                Create the form code
</details>
<br>


EPIC 3 - Account
The Account epic is for all stories related to account

ACCOUNT - USER STORIES

1. As a developer i need to install allauth so the users can register, login, logout.


<details>
            <summary> 1. Acceptance Criteria</summary>

                Install Allauth
                Create proper links for users to register/login
                Create my profile path so the user can view their purchases

</details>

<br>

2. As a user, I want to be able to have a profile section.


<details>
            <summary> 2. Acceptance Criteria</summary>

                Create Profiles app
                Create Profile models
                Create profile views
                Create profile templates
                Create profile templates

</details>
<br>

3. As a developer, I need to implement toasts so the user can get feedback based on their actions on the website

<details>
            <summary> 3. Acceptance Criteria</summary>

                Create Register toasts
                Create Login toasts
                Create Logout toasts
                Toasts display when product is added to bag
                Toasts display when product is deleted from bag
                Toasts when contact/pc technician forms are submitted

</details>
<br>


4. As a user, I want my personal details to be saved so i would not have to re-type everything everytime i want to buy a product

<details>
            <summary> 4. Acceptance Criteria</summary>

                Save user details on the web page

</details>
<br>



5. As a user, I want to be able to view products that will be arriving soon to the shop.


<details>
            <summary> 5. Acceptance Criteria</summary>

                Create arrivals app
                Create arrivals model
                Create arrivals view
                Create arrivals template
                Add arrival posts to the website

</details>
<br>



EPIC 4 - Products

This epic is for all stories related to products.


PRODUCTS - USER STORIES


1. As a developer , I need to create the products app so the user can navigate through the products


<details>
            <summary>1. Acceptance Criteria </summary>

                Create the products app
                Create super user
                Create the necessary database models

</details>
<br>

2. As a developer, I need to create the product models




<details>
            <summary>2. Acceptance Criteria </summary>

                Create Computers model
                Add computer products to database

</details>
<br>



3. As a developer, I need to create the products templates so the user can view the websites products




<details>
            <summary>3. Acceptance Criteria </summary>

                Create computers.html
                Create computer_detail.html
                Style computer_detail.html

</details>
<br>



4. As a user, i would like to see the add products to bag and view the bag contents




<details>
            <summary>4. Acceptance Criteria </summary>

                Create bag app
                Create bag templates
                Create bag views
                Create bag templatetags
                Add product to bag
                Update product from bag
                Delete product from bag
                Fix quantity input from decrementing below 0 value
</details>
<br>


EPIC 5 - Payments

This epic is for the payment related stories

PAYMENTS - USER STORIES

1. As a user, I would like to be able to checkout/purchase the products i chose



<details>
            <summary>1. Acceptance Criteria </summary>

                Create checkout app
                Create Checkout models
                Create signals.py
                Create forms.py
                Modify apps.py
                Create checkout views
                Create checkout templates
                Create css folder in the checkout app

</details>
<br>

2. As a developer, I need to set up a secure payment system with stripe.



<details>
            <summary>2. Acceptance Criteria </summary>

                Install Stripe
                Test payment
                Create Webhooks.py
                Create webhook_handler.py
                Add stripe keys to env
                Add stripe to settings.py

</details>
<br>



EPIC 6 - Deployment

This epic is for the deplyoment related stories

DEPLOYMENT - USER STORIES

1. As a user, I want to see a live website application.

<details>
<summary>1. Acceptance Criteria </summary>

- Deploy to Heroku

</details>
<br>




EPIC 7 - Documentation

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

DOCUMENTATION - USER STORIES

As a developer, I want to create a README file to document every step I took creating the project

<details>
<summary> Acceptance Criteria </summary>

- Anyone can see the procces of this page's development

</details>
<br>
### Features

<details>
<summary>Favicon</summary>

- The icon on the Browser tab next to the website name.
- There to help the user navigate easier through the browser tab.

![Alt text](static/media/favicon.ico)

</details>

<details>
<summary>Main Page</summary>

- Main page contains the nav bar
- Blog Posts
- Footer

![Alt text](static/images/front%20page.PNG)

</details>

<details>
<summary>Navigation Bar</summary

The nav bar (Home , Arrivals , Login , Register , Bag)

![Alt text](static/images/new%20nav.PNG)

</details>

<details>
<summary>Footer</summary>

- Footer contains the Social Media links that redirect to each respective link

![Alt text](static/images/footer.PNG)

</details>

<details>

<summary>Login Form</summary>

- Login form allows users to log into the website

![Alt text](static/images/login.PNG)

</details>

<details>
<summary>Logout Form</summary>

- Logout form allows user to log out of t he website

![Alt text](static/images/logout.PNG)

</details>

<details>
<summary>Register Form</summary>

- Register form allows user to create their own account

![Alt text](static/images/register.PNG)

</details>

<details>
<summary>Contact Us</summary>

- Contact form allows user to contatt the website's administrators.

![Alt text](static/images/contact%20form.PNG)

</details>

<summary>PC Technician form</summary>

- Contact form allows user to contatt the website's administrators.

![Alt text](static/images/contact%20form.PNG)

</details>

<details>
<summary>Add a post </summary>

- Allows the admin to add a post from the front end

![Alt text](static/images/add%20post.PNG)

</details>

<details>


<details>

<summary> Update/Delete Form</summary>

- Allows admin to update or delete the forms from front end

![Alt text](static/images/delete%20post.PNG)

![Alt text](static/images/update%20post.PNG)

</details>

<details>

<summary> Arrivals Page </summary>

- Allows users to Like or Comment a post

![Alt text](static/images/add%20comment.PNG)

![Alt text](static/images/likes.PNG)

</details>

<details>

<summary> Responsiveness</summary>

- Responsiveness was achieved using Bootstrap classes and CSS

![Alt text](static/images/responsive%20comment%20section%20%2B%20form.PNG)

![Alt text](static/images/responsive%20main%20page.PNG)

![Alt text](static/images/responsive%20post.PNG)

</details>

<details>

<summary> Error Pages </summary>
404.html error page

500.html error page

![Alt text](static/images/500%20error.PNG)

![Alt text](static/images/404%20error.PNG)

</details>

<summary> Computers page </summary>


![Alt text](static/images/500%20error.PNG)

![Alt text](static/images/404%20error.PNG)

</details>


<summary> Computer detail page </summary>


![Alt text](static/images/500%20error.PNG)

![Alt text](static/images/404%20error.PNG)

</details>


<summary> Bag </summary>


![Alt text](static/images/500%20error.PNG)

![Alt text](static/images/404%20error.PNG)

</details>

<summary> Toasts </summary>
404.html error page

500.html error page

![Alt text](static/images/500%20error.PNG)

![Alt text](static/images/404%20error.PNG)

</details>

<summary> Checkout </summary>
404.html error page

500.html error page

![Alt text](static/images/500%20error.PNG)

![Alt text](static/images/404%20error.PNG)

</details>




## Technologies used

- HTML (Templates)
- CSS (Style sheet)
- Python + Django (Programming language + Framework)
- Psycopg2 - ElephantSQL(Database)
- AWS (For storing images)
- Stripe (for payments)
- MailChimp(for emails)
- Git (Version Control)
- Github (Respository)
- GitPod(Cloud IDE)
- Heroku (Live Application Host)

## Packages Installed

Packages were installed using "pip3 install (repackage)

Packages were frozen using "pip3 freeze --local > requirements.txt" so heroku know which packages to install in the project.

                asgiref==3.7.2


                boto3==1.28.11


                botocore==1.31.11


                dj-database-url==2.0.0


                Django==3.2.20


                django-allauth==0.54.0


                django-countries==7.2.1


                django-crispy-forms==1.14.0


                django-storages==1.13.2


                gunicorn==21.2.0


                jmespath==1.0.1


                oauthlib==3.2.2


                Pillow==10.0.0


                psycopg2==2.9.6


                PyJWT==2.8.0


                python3-openid==3.2.0


                pytz==2023.3


                requests-oauthlib==1.3.1


                s3transfer==0.6.1


                sqlparse==0.4.4


                stripe==5.5.0


                urllib3==1.26.16


                backports.zoneinfo==0.2.1;python_version<"3.9"



### Future Features

- Allowing the user to customize the computers and giving them a chance to choose the components of the 
  computer.

- Reviews section so the users can leave a comment/review/feedback on a computer.


## Testing

<details>

<summary> PC HUB - Manual Testing </summary>

## Functionality

<table>
  <tr>
   <td>
<strong>Test Label</strong>
</li>
</ol>
   </td>
   <td><strong>Test Action</strong>
   </td>
   <td colspan="2" ><strong>Expected Outcome</strong>
   </td>
   <td><strong>Test Outcome </strong>
   </td>
  </tr>
  <tr>
   <td>Site loading
   </td>
   <td>Navigate the Home Page
   </td>
   <td colspan="2" >Nav bar with home/arrival/bag/login/register buttons and posts user can interact with
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Access Individual products
   </td>
   <td>User is met with the name of the product,  description, price, keep shopping/bag buttons.
   </td>
   <td colspan="2" >Buttons redirect to the designated location
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Login/Register buttons
   </td>
   <td>Clicking each button respectively and trying to interact with them.
   </td>
   <td colspan="2" > The user can register/login/logout of the web page
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Arrival
   </td>
   <td>Clicking the Arrival
   </td>
   <td colspan="2" >The user is met with the page of Arrivals consisting of new products that are soon to be sold on the web page
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Computer Detail
   </td>
   <td>Click the individual computer
   </td>
   <td colspan="2" > The user is redirected to the individual product where they can choose the quantity
   </td>
   <td>PASS
   </td>
  </tr>
  <tr>
   <td>Add to bag
   </td>
   <td>AClick add to bag button
   </td>
   <td colspan="2" > The user is notified via toasts that the product has been added to the bag along with the quantity, the price, and a checkout button
   </td>
   <td>PASS
   </td>
  </tr>
  <td>Contact Form
   </td>
   <td>Fill the form and click submit
   </td>
   <td colspan="2" > The form sends data to the admin panel
   </td>
   <td>PASS
   </td>
   <tr>
   <td>PC Technician Form
   </td>
   <td>Fill the form and click submit
   </td>
   <td colspan="2" > The form sends data to the admin panel
   </td>
   <td>PASS
   </td>
   </tr>
   <tr>
   <td>Bag input fields
   </td>
   <td>Choose the quantity of the product
   </td>
   <td colspan="2" > The input increments/decrements depending on the user input
   </td>
   <td>PASS
   </td>
   </tr>
   <tr>
   <td>Bag Update/Delete buttons 
   </td>
   <td>Click on update or delete button
   </td>
   <td colspan="2" > The buttons react accordingly to their purpose. Update notifies the user that the bag has been updated telling them that the quantity has changed(if it has changed). Delete notifies the user that they successfully deleted an item from the bag
   </td>
   <td>PASS
   </td>
   </tr>
   <td colspan="2" > The input increments/decrements depending on the user input
   </td>
   <td>PASS
   </td>
   </tr>
   <tr>
   <td>Checkout
   </td>
   <td>Fill the form and click secure checkout
   </td>
   <td colspan="2" > The order will be submited and the user is greeted with a thank you and their checkout details
   </td>
   <td>PASS
   </td>
   </tr>
   <tr>
   <td>Emails
   </td>
   <td>Regiest/subscribe
   </td>
   <td colspan="2" > An email is sent to the user automatically using MailChimp
   </td>
   <td>PASS
   </td>
   </tr>
  </tr>
</table>
<ol>

## Browser Compatibility

The website works on different browsers: <strong>Chrome, Firefox and Edge.</strong>

### Responsiveness

- Responsiveness was tested using: Chrome Dev Tools.

- Mobile Devices.

</details>

## Validator Testing

<details>
<summary>HTML</summary>
HTML validator.
All the pages that get displayed are validated.

![Alt text](static/images/add%20post%20html%20validator.PNG)

![Alt text](static/images/delete%20post%20html%20validator.PNG)

![Alt text](static/images/index%20html%20validator.PNG)

![Alt text](static/images/login%20form%20html%20validator.PNG)

![Alt text](static/images/register%20html%20validator.PNG)

![Alt text](static/images/shared%20posts%20html%20validator.PNG)

![Alt text](static/images/update%20post%20html%20validator%20testing.PNG)

![Alt text](static/images/contact%20form%20HTML%20validator.PNG)

![Alt text](static/images/500%20%20error%20HTML%20validator.PNG)

![Alt text](static/images/error%20HTML%20validator.PNG)

</details>

<details>
<summary>CSS</summary>
CSS validator.
All CSS code is validated.

![Alt text](static/images/css%20validator.PNG)

</details>

<details>
<summary>Python Validator</summary>
PEP8 validator.
All Python code is validated.

- Models

![Alt text](static/images/models%20pep8.PNG)

- Views

![Alt text](static/images/views%20pep8%20validator.PNG)

- Forms

![Alt Text](static/images/forms%20validator%20pep8.PNG)

- Contact

![Alt text](static/images/contact%20view%20PEP8.PNG)

![Alt text](static/images/contact%20PEP8%20validator.PNG)

![Alt text](static/images/contact%20admin%20PEP8.PNG)

![Alt text](static/images/contact%20form%20PEP8.PNG)

</details>
<details>
<summary>Lighthouse</summary>
Lighthouse.

![Alt text](static/images/lighthouse.PNG)

</details>

<details>
<summary>WAVE</summary>
WAVE validator.

![Alt text](static/images/wave%20validator.PNG)

</details>

### Unfixed Bugs / Other

- A few errors accur in the HTML validator but the web application works fine. The errors maybe appear due to use of Django elemetts in the HTML templates.
- Posts cannot have the same name. Only one post can have a specific name(title/artist name)

## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows:

  - In the Heroku profile, create a new project, name must be unique, location set to Europe
  - From the the project you have just created you can go to the setting page.
  - Once in the settings page, Add the right Configuration Variables to the project. SECRET_KEY DATABASE_URL and CLOUDINARY_URL.
  - Then from there you go to the Deploy page and link your GitHub repo to the project u intented to deploy.
  - Then you can scroll at the end of the page and click on the Deploy Branch
  - After Heroku starts compiling the files and creating your app , after 1 minute or so you'll have your delpyed app link.
  - The deployed app can be found [here](https://rapblog.herokuapp.com/)

## Credits

- [Code Institute](https://codeinstitute.net)
- For the great lessons (I think therefore blog)

- [Favicon](https://favicon.io)
- For the browser tab icon

- [StudyGyaan](https://studygyaan.com/django/how-to-create-a-unique-slug-in-django?utm_content=cmp-true)
- For the tutorial on Slugify

- [Font Awesome.](https://fontawesome.com/)
- For the Social MEdia icons , Like, Comment buttons

- [Bootstrap](https://bootstrap.com)
- Bootstrap was user to create a responsive desing on all platforms.

- [Pexels](https://pexels.com)
- Images were taken from Pexels.

- [<OrdinaryCoders>](https://ordinarycoders.com/blog/article/django-messages-framework)
- Django alert messages when post is added/edited/deleted and when contact form is submited

- [CoduBeta](https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to_)
- UserPassestestmixin was taken from here.

- [Biograpy](https://www.biography.com/musicians/tupac-shaku)
- Biography of the Artists taken from Biography.

## Acknowledgements

- I would like to thank my mentor Daisy for guiding me.