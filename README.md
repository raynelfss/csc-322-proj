# CSC 32200: Project
This will be the github repo for our project.
## Team:
__1. Hussam Marzooq.__

__2. Raynel Sanchez.__

__3. Alan Tepoxtecatl.__

__4. Crystal Yang.__

# Electronic restaurant order and delivery system

To develop an on-line restaurant order and delivery system so that the restaurant can provide menus of food, customers browse and order the food from the menu, delivery people of the restaurant deliver the food.

In this system, there are three groups of users:

__1.	Employees:__ 

  1. at least two chefs who independently decide the menus and make the dish.

  1. at least two delivery people for food delivery.

  1. one manager who process customer registrations, handles customer compliments and complaints, hire/fire/raise/cut pay for chef(s) and delivery people.
  
__2.	Customers:__
  
  1.	Registered customers who can browse/search, order and vote (lowest 1 star to highest 5 stars) food delivered (on food and delivery quality/manners individually); can start/participate a discussion topic on chefs/dishes/delivery people.

  2.	Registered customers become a VIP after spending more than $100 or 5 orders as registered customers without outstanding complaints, they will receive 5%discount of their ordinary orders and 1 free delivery for every 3 orders, have access to specially developed dishes, and their complaints/compliments are counted twice as important as ordinary ones.
  
__3.	Visitors:__ who can browse the menus and ratings only, can apply to be the registered customers.
	
## System features:

  1.	Provide a GUI, not necessarily web-based, with pictures to show the descriptions of each dish and price; each registered customer/VIP has a password to login, when they log in, based on the history of their prior choices, different registered customer/VIP will have different top 3 listing dishes. For new customers or visitors, the top 3 most popular dishes and top 3 highest rated dishes are listed on the first page.

  2.	A customer can choose to 1) pick up the dishes in person, or 2) by restaurant delivery. For case 1)s/he can only complain/compliment the chef.

  3.	A customer can file complaints/compliments to chef of the food s/he purchased and delivery person who delivered the dish or other customers who didn’t behave in the discussion forums. Delivery person can complain/compliment customers s/he delivered dishes; all complaints/compliments are handled by the manager. The complained person has the right to dispute the complaint, the manager made the final call to dismiss the complaint or let the warning stay and inform the impacted parties. Customers/delivery people whose complaints are decided to be without merit by the manager will receive one additional warning.

  4.	Registered customers having 3 warnings are de-registered. VIPs having 2 warnings are put back to registered customers (with warnings cleared).The warnings should be displayed in the page when the customer logs in.

  5.	Every customer should deposit some money to the system. If the price of the order is more expensive than the deposited money in the account, the order is rejected, and the customer receives one warning automatically for being reckless.

  6.	Customers who are kicked out of the system or choose to quit the system will be handled by the manager: clear the deposit and close the account. And kicked-out customer is on the blacklist of the restaurant: cannot register anymore.

  7.	The chef whose dishes received consistently low ratings (<2) or 3 complaints, will be demoted (less salary), a chef demoted twice is fired. Conversely, a chef whose dishes receive high ratings (>4) or 3 compliments, will receive a bonus. One compliment can be used to cancel one complaint. The delivery people are handled the same way.

  8.	The delivery people will compete to deliver the order by bidding, the manager assigns the order from bidding results: the one with lowest delivery price is generally chosen; if the one with higher asking price is chosen, the manager should write a memo in the systems justifications. The delivery person who didn’t deliver any in the past 5 orders will automatically receive one warning.

  9.	Each team comes up with a creativity feature of the system to make it more exciting, e.g., smart-phone based system, voice-based features, or efficient route planning for delivery, which is worth 10% of overall score of the final project.
    
_Details that are not found in this requirement list are up to your team’s call: you fill in the details to your own liking._

