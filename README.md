# Chung Tai Zen Center
## App for chung tai center.

### [Juliana Mei](http://www.julianamei.com)'s submission to [DigitalCrafts](http://www.DigitalCrafts.com)' individual project week.
------

### Summary
The Chung Tai Zen Center in Houston has been operating since 2008 from a foundation of dedicated volunteers and donations. They offer free meditation classes, ceremonies, and three meals a day open to the public. But the mundane work of maintaining records of students, volunteer sign up sheets, and donations are less than efficient. As of 11/28/2017, the current system is an excel sheet that feeds into Microsoft access to keep inventory of students.

And the [current website](http://www.cthouston.org/) is outdated and hard to navigate.

This project aims to provide a platform for Chung Tai Zen Center to capture student attendance with a public-facing website for a calendar for events and for users to sign up for classes, ceremonies, and volunteering.

-----

### MVP (Minimum Viable Product)

- [ ] User can login
- [ ] Users can see a calendar of events
- [ ] Users can sign up for classes, ceremonies, and volunteering

-----

### Stretch Goals
- [ ] Has ability for students to check-in via iPad at the front desk
- [ ] Admin can send mass email notifications
- [ ] Food page with Yelp API
- [ ] Draw Your Fortune page
- [ ] After ceremonies, members can upload photos
- [ ] User can see all library books
- [ ] Users can purchase memorial service and/or ashboxes
- [ ] Users can donate to Chungtai Zen Center
- [ ] Users can book appointments with Shifus
- [ ] Users can download sutras and chanting audio
- [ ] Meditation Simulator page with a timer functionality
- [ ] Meditation Simulator uses voice recognition: "Alexa, start meditation 30 minutes."

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
