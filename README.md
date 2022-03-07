# Project Title:
Bus Time Application

# Video Demo:
https://youtu.be/Kx2FuKz_uS0

# Description:
This project is created to allow users in Singapore to check their next bus timing. With the use of APIs from Singapore's very own Land Transport Authority, the application extract useful data from the API and display information on bus services, bus stop code and arrival timing of buses, allowing users to search for their next bus timing based on the bus service number or their desired bus stop code.

Users will have to give an input that could be either bus service number or bus stop code. The application will check for both and send the correct data to the user. If the user searched for a bus service number, the web-based application will show the arrival time of the bus service number at every single bus stop.

In the event the user search for a bus stop code, the application will show the bus arrival time of every bus found in the bus stop.

There is also an additional function where users can click on either the bus service number or bus stop code and it will automatically do a search on the button clicked.

Whenever a user gives an input, the program check whether it is a bus service number or a bus stop code based on the length of the input. Bus stop code usually comes in length of 5 and bus service number come with a range from 1 to 4. Should the length of the input be 5, the program checks for a valid bus stop code that matches the user input. If there is no such bus stop code, the program flashes "invalid bus stop code". Should the length of the input to be not equals to 5, the program checks for a bus service nubmer that matches the user input. Similarly, if there is no such service number, the program flashes "invalid bus service"

Under data_test folder, multiple python files were created to test and understand the datasets extracted from the respective APIs. This ensures that the data are usable, correct and suitable for the purpose of this application.

Static folder consist of the images used in the application itself and also the CSS file for styling of the webpage.

Templates folder consist of the different HTML templates. Layout.HTML is the reference HTML for every other HTML file.

"index.html" is the homepage of the application.

"busService.html" is rendered when users search for the bus service number. It shows the bus timing of a particular bus service. When users search for the bus service number, the input is obtained in flask and the information needed based on the user input is extracted from the JSON file.

"bustime.html" is rendered when users search for the bus stop code. It shows the bus timing of every bus in a bus stop code. When users search for a bus stop code, the bus services in is extracted using the bus stop code provided. The data is then sent back to the webpage and displayed.

"stops.html" is still an ongoing project that is planned for showing nearest bus stop closest to the user current location. The program will take in the latitude and longitude of the user current location using navigator.geolocation. With that data, the program will calculate the 5 nearest bus stops from the user location and display it on the webpage.

API_file.py is the python file used to extract the data in the APIs and write the data into a JSON file. It has to be run every few days to ensure that the data sent to the application is up to date.

app.py is the main python file that runs the application and logics.

routes.json, services.json and stops.json are the data extracted from the APIs.
