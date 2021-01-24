# Capstone Proposal

1. What goal will your website be designed to achieve?

- This site will provide consolidation of many tools used during my day job (Implementation and training for car dealership software). It will also allow more efficient means to send follow up emails to clients, and keep track of task to be completed for clients.

2. What kind of users will visit your site? In other words, what is the demographic of your users?

- The demographic is people in the remote tech training field.

3. What data do you plan on using? You may have not picked your actual API yet, which is fine, just outline what kind of data you would like it to contain.

- I plan on using a small sample of generic contact information (from which I&#39;ll have emails) as well as a mock dealership and trainers.
- The API I plan on using for within-the-site mail delivery is MailGun.

4. In brief, outline your approach to creating your project (knowing that you may not know everything in advance and that these details might change later). Answer questions like the ones below, but feel free to add more information:

a. What does your database schema look like?

- My database schema is available in my models.py file [here](https://github.com/PaytonDev/Install_Hub).

b. What kinds of issues might you run into with your API?

- Issues with validating an email address or making sure that the user is aware when an email is not sent or is invalid.

c. Is there any sensitive information you need to secure?

- Yes, Users will have to be able to log in and with a username and password. I will also have split access among users depending on the job title.

d. What functionality will your app include?

- Creation of &quot;Projects&quot; which are assignments of dealership training to users.
- Also will have a 24hr timer on a covid check-in form.

e. What will the user flow look like?

1. The User will sign in with a company assigned username and chosen password. (user is already assumed to have this as my company utilizes single sign-on)
2. The user will be sent to their Install Detail Page. This page displays all needed information about the User&#39;s assigned dealership and the products the user will be training on. There is a side menu where the user can also navigate to the Interaction Log or the Task Checklist.

1. If the user&#39;s title is &quot;Implementation Manager&quot;, they will have the ability to navigate to the &quot;Create Install&quot; Page which will allow the user to create a project, assign a dealership, and assign the trainers to that dealership. This will be accessible from their side menu. They will also be able to remove or replace trainers.

f. What features make your site more than CRUD? Do you have any stretch goals?

- My major stretch goals are giving correct access to users, protecting their passwords with Bcrypt, and implementing the layout of data on the front end correctly since most of it will be dynamic.