# Chung Tai Zen Center
## App for chung tai center.

### [Juliana Mei](http://www.julianamei.com)'s submission to [DigitalCrafts](http://www.DigitalCrafts.com)' individual project week.
------

### Summary
The Chung Tai Zen Center in Houston has been operating since 2002 from a foundation of dedicated volunteers and donations. They offer free meditation classes, ceremonies, and three meals a day open to the public. But the mundane work of maintaining records of students, volunteer sign up sheets, and donations are less than efficient. As of 11/28/2017, the current system is an excel sheet that feeds into Microsoft access to keep inventory of students.

And the [current website](http://www.cthouston.org/) is outdated and hard to navigate.

This project aims to provide a platform for Chung Tai Zen Center to capture student attendance with a public-facing website for a calendar for events and for users to sign up for classes, ceremonies, and volunteering.

-----

### MVP (Minimum Viable Product)

- [x] User can login
- [x] Users can see a calendar of events
- [x] Users can sign up for classes and volunteering

-----

### Stretch Goals
- [ ] Has ability for students to check-in via iPad at the front desk
- [x] Admin can send mass email notifications
- [ ] Food page with Yelp API
- [x] Draw Your Fortune page
- [ ] After ceremonies, members can upload photos
- [ ] User can see all library books
- [x] Users can purchase memorial service and/or ashboxes
- [x] Users can donate to Chungtai Zen Center
- [ ] Users can book appointments with Shifus
- [ ] Users can download sutras and chanting audio
- [ ] Meditation Simulator page with a timer functionality
- [ ] Meditation Simulator uses voice recognition: "Alexa, start meditation 30 minutes."

------

### How to Run this App
 - Git clone the project repository
 - Create and start a virtual environment
 - Pip install requirements.txt with `pip install -r requirements.txt`
 - create a file named "secrets.sh"
 - touch secrets.sh (mac and linux)
 - obtain a secret from MiniWebTool key and add to secrets.sh
 - export SECRET_KEY='<secret_key>'
 - add secrets.sh to .gitignore file
 - Obtain access_token and secret_key and store in secrets.sh
 - Setup a Postgres DB, create user & database
 - Run `python manage.py migrate`
 - Create admin account with `python manage.py createsuperuser`
 - To start the server, run `python manage.py runserver`
 - Open localhost:8000 on your browser to view the app.
 - [Lost? More details here](https://stackoverflow.com/questions/37094032/how-to-run-cloned-django-project)

-----
## Developer's Journal
### Individual Project Week: December 6 - 12
#### December 6
Material kicked my butt! I destroyed everything I worked on today so now I have zero front end. But I guess that's okay because I met my MVP goal which was the ability to login. The backend works but none of the links are accessible. I guess I have to go back to good ol' bootstrap.
Things I worked on today:
- sign up for Mailgun: an email service for developers to allow for mass emailing
- typewriter effect on the front end
- troubleshoot a bug where Material JS file was overriding all clicking ability
- added django-material package
#### December 7
Today's original goal was to set up the ability to see a calendar of events. However, I spent most of today deal with yesterday's horror. After many hours, I have a decent front end. The best thing out of today is that the project now has the ability to send emails including: sign up email confirmation, reset-password emails, and mass emailing capability.
Things I worked on today:
- skeleton front-end
- hooking up email service and then integrating it into sign up workflow, password reset, and a contact form
#### December 8
Today I made a lot of progress on the front-end. Added a pop of color, little UI details that go a long way, very happy with how it's looking. Added a random quote generator. Created an little web image scraper to collect little-monk images =)
I closing today on a pause. I'm having trouble wrapping my head around how to organize the models. What is the best way to organize it so that it'll grow easily in the long run?
#### December 9
Yay! I figured out django's model and query language. Students can successfully sign up for a class =)
#### December 10
Lesson learned: multiple frameworks don't play nicely together. Something mysterious is overriding all of my JS code.
#### December 12
Putting on the final touches for the presentation by fleshing out the content with better front-end design. 
-----
