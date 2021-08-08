# Testing of The Book Store

## Testing Navigational Bar 

### Brand Name
* When I click the brand name "The Book Store" I expect to be taken to the home page. I tested this by using a laptop, Ipad and mobile device and physically clicking the brand name. By doing this I confirmed the expected results. 
### Navigational Links
* Within the navigational bar there are three main options, "All Products", "Categories" and "Contact". 
    * When clicking "All Products" I expect to be shown the products page which displays all products within the database. I tested this using a laptop, Ipad and mobile device and physically clicking the navigational link. I cross referenced the products with the database to confirm all were present. This confirmed all expected results.
    * When clicking "Categories" I expect to be shown a drop down menu featuring all of the categories listed within the database. I checked this by visiting the database and cross referencing the shown results. I tested this using a laptop, Ipad and mobile device and physically clicking the navigational link. This confirmed the expected results.
    * CONTACT FORM TO BE COMPLETED.
 ## User And Basket 
 
### Testing The Basket
* When a user first visits the site they should see the basket icon and as they haven't added any items to the basket yet, it should be empty and this should be represented by a value of 0.00. To test this I visited the site and visually inspected. This confirmed the expected results. 
    * At this point if a user clicks the basket icon, they should be taken to the bag page and shown a message that says the bag is empty. They should also be provided with a button to go shop all products. To test this I visited the site and visually inspected. This confirmed the expected results. 
* When a user adds something to the basket, the value of 0.00 should change to reflect the item price plus postage if applicable. To test this I added an item to the basket and observed the results. This confirmed the anticipated results. 
    * From here if the user clicks the basket icon, they should be taken to the bag page. Within the bag page the items added to the basket should be shown. This information should include a product image, product name, the quantity chosen and a price. To test this I added three items to the basket with varying quantities. I visually inspected the site and this confirmed the expected results.
* Within the bag page there should the option to edit the quantity or remove the item entirely. To test this I visited the bag and altered the quantity by choosing a different quantity to the one initially added. This confirmed the expected update to the quantity, subtotal and total price. 
* To test the remove function, I clicked the red remove button. This confirmed the expected result of the item being removed from the bag.

## Checkout 

* When a user has items in the basket, the checkout button should be available. Upon clicking this they should be taken to a checkout page displaying a form to be filled in by the user for delivery details. To check this I added an item to my basket and visited the basket page. From here I could see the checkout button, upon clicking this provided the expected results.

### Checkout Form 

TESTING TO BE COMPLETED. 

 ## Testing the "CTA" (call to action) button
 * On the homepage there is a button shown on the carousel. The button says "Shop Now" and when clicked should take the user to the "All Products" page. I tested this by using a laptop, Ipad and mobile device and physically clicking the button. By doing this I confirmed the expected results.

 ## Recently Added

 ## Footer 
 * Within the Footer, there are 2 navigational options for within the website and 2 social media icons. 

### Social Media Icons 
* The social media icons featured are Instagram and Facebook. When clicked they should take the user to the social media website in a new tab. I tested this by clicking the icons. Upon doing this I noted that I hadn't included links to the social media sites or the target "_blank" attribute. I fixed these errors and tried again. This confirmed the expected behaviour.

### Returns & FAQ Pages 
* Upon clicking the "Returns" link, users should be taken to the "Returns" page. I checked this by clicking the link, this confirmed the expected behaviours. 
* Upon clicking the "FAQ" link, users should be taken to the "FAQ" page. I checked this by clicking the link, this confirmed the expected behaviours. 

## Search Function 
* The expected behaviour of the search function is that, upon entering a valid input the site will be searched for a matching result. If there is no result the user should be informed of this. To test this I firstly entered the word "zoo" as I knew a book title matched this. The results confirmed the expected behaviour, I was shown one result named "Dear Zoo". The site url reflected the search, as it showed "?q=zoo" as anticiapted. 
* I then entered the word "grow" and this did not have any results. However this did not confirm the anticipated results as there was not an error message. ERROR MESSAGE FIX TO BE IMPLEMENTED.
* The search function should check the name of the book, the name of the author and also the description for the key word. 
    * I checked this was working by typing the name "Stephen" this gave two results of books both written by an author with the name Stephen. 
    * I then checked the description by using the word "learn", this gave one result and the word learn was within the description of this book.
