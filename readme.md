# DataCloud Analytics: AaaS
### Pranshu Gupta & Akash Waghela

### Introduction
DataCloud Analytics will enable you to get insights from your consumer data in order to help you connect with the right customer, personalize every interaction and measure the effectiveness of each engagement.

### Data Analytics as a Service
Analytics as a Service (AaaS) refers to the provision of analytics software and operations through Web-delivered technologies. 

### Scope
The software will be a web service that will be used by businesses to visualize their consumer and product usage data to inform and measure their marketing. We will utilize the live product usage data to build insights and create dashboard for the business user. The dashboard will have rich data visualizations that will prove useful for building new marketing strategies. 

### System Interface
The web service system interface will consist of following components:
* Live Product Usage Data Listener
* Data Aggregator
* Insights Generator
* Data Visualizer 

These components will work together to provide the user with useful data visualizations on the dashboard.

### Implementation Details
We plan to use the following technologies and frameworks to build our software:
* Python/Django for Server side programming
* HTML5, CSS and JavaScript for front end UI
* D3.js for Data Visualization 

### Why Django?
We chose Django because of following points:
* Python is a really nice, elegant & powered language. There are guidelines how to write and format your code and there is, well most of   the time, a clean structure in your code, no matter what you do. Python follows the principle "code is much more read then written".
* The Django ORM is an incredibly powerful database tool. It handles creation of your database, as well as insert, update, delete queries and some quite advanced querying - although it's not perfect. It supports multiple databases - MySQL, PostgreSQL, Oracle & SQLite are all supported out-of-the-box assuming you have the relevant Python libraries installed. you write your database as Python class and query it using Python. You do not have to write one line SQL by yourself.
* Forms are not the most fun thing. While Django doesn't make them fun, it at least does a lot for you. You define some fields and how you want the basic validation to work, and Django creates the HTML adds the error messages and cleans the data so you don't get anything unexpected. The Django forms framework can even generate and update your database from a database model you create, make your job even easier.

### Why D3?
* Using D3.js we separate the data analysis and data visulaization componenets of our web service. Data Analysis is done on the server side with Python and the results are sent to the client side in JSON format which can be used by D3.js library to make visualization independently and without putting the load of graphics rendering on the server. 
* Infact Shiny itself is built upon D3.js and Google Charts. An D3.js literally has HUGE number of examples available on the web to get inspired from.
* We have also used Google Charts. We found that the code we have to write is less verbose as compared to D3 and in a few cases quality of charts rendered by Google Charts is superior to D3 (e.g. Geographical Charts). We might consider moving entirely to Google Charts.

