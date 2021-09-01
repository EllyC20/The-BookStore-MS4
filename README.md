# The Book Store

![Am I Responsive Image]

## The Book Store is a fictional online book and supplies store. The stores purpose is to sell books, and other materials. These  materials could include arts and crafts supplies, notebooks, school supplies or home office products. The store will allow the owner to make more sales by moving to an online platform. 

#### The live website can be viewed [here](https://the-bookstore-ms4.herokuapp.com/)

<br>

## Table Of Contents 

- <a href="#ux">UX</a>
  - <a href="#user-stories">User Stories</a>
  - <a href="#strategy">Strategy</a>
  - <a href="#scope">Scope</a>
  - <a href="#structure">Structure</a>
- <a href="#database">Database</a>
- <a href="#wireframes">Wireframes</a>
- <a href="#surface">Surface</a>
- <a href="#crud">CRUD</a>
- <a href="#features">Features</a>
- <a href="#languages">Languages</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

<br>

<span id="ux"></span>

## UX 

<span id="user-stories"></span>

### User Stories 

**As a New User**

* I want to be able to use the site intuitively. 
* I want to be able to search for products.
* I want to be able to view the details of individual products.
* I want to be able to order products by category.
* I want to be able to order products by finer details such as A-Z, price low to high or vice versa. 
* I want to be able to add products to my basket and checkout, without an account.
* I want to be shown messages throughout my journey through the site.
* I want to be able to register an account.

**As a Site Owner/Super User**

* I want to have a payment system implemented.
* I want to be able to edit product details.
* I want to be able to add new products.
* I want to encourage returning users by having an easy to use site.
* I want to have a contact form where users can send any questions.

**As a Returning User/Signed In User**

* I want to be able to edit my delivery address and information.
* I want to have a personalised profile that shows any previous orders.
* I want to be able to log in to a previously registered profile. 
* I want to be able to leave reviews for products.


<span id="strategy"></span>

### 1.Strategy 

**Project Goals**

* To make a full-stack site based around business logic used to control a centrally-owned database.
* To make a full-stack site that uses HTML, CSS, JavaScript, Python + Django.
* Creating a website that uses a relational database.
* Creating a website that uses Stripe payments.

**Site Owner Goals(Business Goals)**

* Creating a secure, professional and profitable e-commerce website.
* Inspire users to read more or read new books.

<span id="scope"></span>

### 2.Scope

* Fits in with my current skill-set of HTML, CSS, JavaScript, Python and Django.

<span id="structure"></span>

### 3.Structure

**As A New User (Not Logged In)**

A new user can visit:
  * The home page
  * Can access the register and login pages 
  * The products page
  * Specific category pages
  * The basket
  * The checkout
  * Contact form


**As A Registered User (Logged In)** 
A returning user can visit:
  * The home page
  * Can access the log out functionality
  * Profile
  * The products page
  * Specific category pages
  * The basket
  * The checkout
  * Contact form

**As Superuser (Site Owner)**
A superuser can visit:
  * The home page
  * Can access the log out functionality
  * Profile
  * The products page
  * Specific category pages
  * The basket
  * The checkout
  * Contact form

<span id="database"></span>

### Database 

* During the development phase I used the sqlite3 database.
* For deployment, I used the PostgresSQL database which is provided by Heroku.

### Database Models

<br>

**Profile App**

**UserProfile model**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField |  User, on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Street address 1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Street address 2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
 Town/City | default_town_or_city | Charfield | max_length=40, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True

**Checkout App**

**Order model**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order number | order_number | CharField | max_length=32, null=False, editable=False
 User profile | user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full name | full_name | CharField | max_length=50, null=False, blank=False
 Email| email| EmailField | max_length=254, null=False, blank=False
 Phone number | phone_number | Charfield | max_length=20, null=False, blank=False
 Country| country | CountryField | blank_label='Country *', null=False, blank=False
 Postcode | postcode | CharField | max_length=20, null=True, blank=True
 Town/City | town_or_city | CharField | max_length=40, null=False, blank=False
 Street address 1 | street_address1 | CharField | max_length=80, null=False, blank=False
 Street address 2 | street_address2 | CharField | max_length=80, null=True, blank=True
 Date | date | DateTimeField | auto_now_add=True
 Delivery cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
 Order total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Grand total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Original bag | original_bag | TextField | null=False, blank=False, default=''
 Stipe pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

**OrderLineItem model**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order  | order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
 Product | product | ForeignKey | Product, null=False, blank=False, on_delete=models.CASCADE
 Quantity | quantity | IntegerField | null=False, blank=False, default=0
 Lineitem total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

**Products App**

**Category model**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 name | name | CharField | max_length=254
 Friendly name | friendly_name | CharField | max_length=254, null=True, blank=True

**Product model**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category| category| ForeignKey | Category, null=True, blank=True, on_delete=models.SET_NULL
 Image | image | ImageField | null=True, blank=True
 Name | name | CharField | max_length=300
 Author | author | CharField | max_length=300, blank=True
 Description | description | TextField | null=True, blank=True
 Image url | image_url | URLField | max_length=1024, null=True, blank=True
 Price | price | DecimalField | max_digits=6, decimal_places=2

**ProductReview model**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Product | product | ForeignKey | Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='reviews'
 User | user | ForeignKey | User, null=True, blank=True, on_delete=models.CASCADE
 Title | title | CharField | max_length=254
 Content | content | TextField | 
 Rating | rating | IntegerField | choices=rating_selection, default=3
 Date Added | date_added | DateTimeField | auto_now_add=True

**Home App**

**Subscribers model**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Email | email | EmailField | null=True
 Date | date | DateTimeField | auto_now_add=True

 **SubscriberEmail model**

 | **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Title | title | CharField | max_length=200, null=True
 Message | message | TextField | null=True

<span id="wireframes"></span>

### 4.Skeleton

**An inital layout of the file structure can be seen here.**

![ReadmeImage](readme_images/file_structure.jpeg)

 **Desktop wireframes can be viewed [here](https://github.com/EllyC20/The-BookStore-MS4/tree/master/readme_images/wireframes/lg-device)**

 **Mobile wireframes can be viewed [here](https://github.com/EllyC20/The-BookStore-MS4/tree/master/readme_images/wireframes/sm-device)** 

 **Tablet or medium device sizes can be viewed [here](https://github.com/EllyC20/The-BookStore-MS4/tree/master/readme_images/wireframes/md-device)**

 **When viewing the wireframes there are some changes that should be noted, they are detailed below.**

<span id="surface"></span>

### 5.Surface

**Colours**

* I kept the colours of the site, consistent and subtle. The colours flow together nicely and allow easy use of the site without overwhelming the user. The colours hold positive connotations - yellow and green are associated as positive / success colours.

![Colours](readme_images/ms4_colours.png)

**Font**

* I used Roboto Mono for the body text, and Bebas Neue for headings, brand name or text that required attention. The two fonts go well together and I used Google Fonts to choose this pairing. They feel modern together and are not difficult to read on any screen size. 

**Images**

* The home page has a carousel which showcases images related to the purpose of the site. These images show books, immediately informing the user of what the site does. They're comforting images for people who enjoy reading, showing a relaxing atmosphere such as a libary.

<br>

## Features 

<span id="crud"></span>

### CRUD 

**Create** 

* Create functionality is provided for the superuser via product management. A site owner (superuser) can add a new product using a front-end form that will add the product to the database and visually to the front end.
* Create functionality is provided for logged in / registered users as they can add reviews to products.

<br>

**Read** 

* All users can read the information within the site.

<br>

**Update**

* Update functionality is provided for the superuser via the product page, using the "edit" button. Here the site owner can edit the products information on the site and database. 

<br>

**Delete**

* Delete functionality is provided to the superuser via the product page, using the "delete" button. Here the site owner can delete a product from the site and database.

<br>

<span id="features"></span>

### Current Features 

* Home page with carousel image.
* Footer with social media links and 2 common e-commerce pages (FAQ's and Returns)
* Product page with pagination 
* Product page features a "filter by" option allowing users to choose how they see products.
* Categories dropdown from Navbar, allowing the user to access specific categories.
* Product detail page showing details.
* A contact page that provides feedback to the user after the form is submitted.
* A functional checkout process that requires a user to complete a valid form.
* Stripe payments, with and without card authentication. (Test card numbers can be used to prompt an authentication request.)
* Toast messages throughout user journey.
* Confirmation emails of orders.
* Contact emails are sent to a "business" email address.
* Option to add reviews to products as a logged in user.


### Feautures To Be Implemented

*

<br>

<span id="languages"></span>

## Languages Used 

* [HTML5](https://en.wikipedia.org/wiki/HTML5) 
  -  Used for basic content structure.
* [CSS3](https://en.wikipedia.org/wiki/CSS) 
  - Used for styling content.
* [Python](https://www.python.org/) 
  - Used to implement backend development. 
* [jQuery](https://jquery.com/)
  - Used to initialize interactive features.

## Frameworks, Libaries & Other Tools Used 

* [Gitpod](https://www.gitpod.io/)
  - For development of the project.
* [Django](https://docs.djangoproject.com/en/3.2/)
  - Framework for this project.
* [Github](https://github.com/)
  - Used to store the project.
* [Git](https://git-scm.com/)
  - Used for version control.
* [Google Fonts](https://fonts.google.com/)
  - To implement the fonts used.
* [TinyPng](https://tinypng.com/)
  - To compress image sizes.
* [Balsamiq](https://balsamiq.com/)
  - To design wireframes.
* [Heroku](https://id.heroku.com/)
  - Cloud platform to deploy the project.
* [Coolors](https://coolors.co/palettes/trending)
  - To visualise a colour scheme.
* [Font Awesome](https://fontawesome.com/)
  - For any icons within the site.
* [cdnjs](https://cdnjs.com/)
  - To get Font Awesome linked.
* [Lucidchart](https://www.lucidchart.com/pages/) 
  - For images used in "Structure" section of README.
* [Am I Responsive](http://ami.responsivedesign.is/) 
  - For the image showing the site at the top of this README.

<br>

<span id="testing"></span>

## Testing 

All testing detail can be found [here.](https://github.com/EllyC20/The-BookStore-MS4/blob/master/TESTING.md) 

<span id="deployment"></span>

## Deployment 

### To Clone 

* The project can be run locally by cloning or downloading.
* Open the repositorie and click "Code", then select either "clone" or "download". 
* If you choose to clone you will be provided with a URL. Copy the URL from the "Clone with HTTPS" section.
* In your IDE, open Git Bash.
* Type Git Clone and then paste the URL you copied.
* Press enter and this will create the clone.
* If you choose to download, you will be given a zip file which can be unzipped locally. 
* These files can then be uploaded to your IDE. 

### Heroku Deployment 

**Prior to running Heroku, set up your workspace.**

* To do this, create a **requirements.txt** file to store the project dependencies. In the CLI type <code>pip freeze --local > requirements.txt</code>

* Create a **Procfile**, this is so Heroku knows which file is the entry point. In the CLI type <code>python app.py > Procfile</code>

* Vist [Heroku](https://id.heroku.com/login) and create a free account.

* From the dashboard click the "new" button and create a new app. Name your app and select your region.

* For GitHub deployment, go to the "deploy" section within Heroku.
  - Search your repositorie name, when it is found click "connect".

* In the "settings", choose "config vars". Click on "Reveal config vars" then enter the variables contained in your **env.py** file.
  - These include "".

* In the "deploy" section, scroll down to "automatic deployments" choose "enable automatic deploys" and then click "deploy branch".

* Finally click "open app" and the app will be launched. 

<br>

<span id="credits"></span>

## Credits 

### Content

* The description of the books on the product details page are taken from [Book Depository](https://www.bookdepository.com/)
* Home page text, written by me.
* Footer / FAQ written by me. 
* Contact page, written by me. 

### Media 

* The stationary images (Office Supplies) are taken from [Pixabay](https://pixabay.com/)
* The book cover images are taken from a dataset on [Kaggle](https://www.kaggle.com/lukaanicin/book-covers-dataset)
* The home page carousel images are from [Pixabay](https://pixabay.com/)

### Acknowledgements

* To the Code Institute for the course content, and the last walk through project "Boutique Ado" which was used to implement some features.
* To Precious my mentor, for his time and guidance.
* To Tutor Support who have been extremeley helpful and willing with any questions.
* Slack community for providing help where possible.
* Stack Overflow for general queries.
