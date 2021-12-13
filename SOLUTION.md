Quick instructions:

pip install pipenv

pipenv install -r requirements.txt

pipenv shell

python manage.py runserver

For this test I created a front-end centric logistics application. To make it I used Django, Bootsrap 5 and a tiny bit of Javascript.

App description:

The home page(booking_mgmt.html) consists of two sections:

-The top section where the user can add bookings and see a list of them in order of departure date.

-A second section below, where the user can add vehicles, associate them with a booking, and see a list of vehicles grouped by booking.

Each item in both lists(Bookings and Vehicles) have two buttons, one to erase and another one to edit the item.

On the booking edition page(edit_booking.html), there is a preloaded form with all the booking information ready to edit. Underneath the form, there is a list of the vehicles assosiated to that booking.

On the vehicles edition page(edit_vehicle.html), there is a preloaded form with all the vehicle information ready to edit, the last field is a booking number dropdown that feeds its information from the existing bookings.

Considerations:

I decided to make this app front end centric as I assumed that the target market for this kind of application is not familiar with the use of api's. My focus was on ease to use and functionality.

Future improvements:

A rest-api could be implemented. Front end user and company login.

Include a SOLUTION.md file describing the app, decisions and technical considerations that you have taken as well as any type of improvements that could be applied.
