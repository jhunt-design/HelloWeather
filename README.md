# Hello, Weather!
### Video Demo:  <https://youtu.be/92gqmDrfeEw>
### Description:
Hello, Weather! is a web app that combines weather monitoring with an interactive weather character. When launching the app, the user can input their location (or any location), and upon submitting a form, the app will fetch the temperature from that location. Beyond displaying the temperature, the app uses the data to interactively control the state of the animated weather character, providing a dash of surprise and delight from our little hero, who displays a range of emotion and color influenced by the climate.

### Process:
How did I end up there? Well, I'm a motion designer by trade, and this project combines my love of design and animation with my newly obtained CS50 coding skills. My main goal in taking this course, after all, was to add basic coding knowledge to my toolbelt to assist me in writing expressions in After Effects, so it only made sense that my final project should combine coding with animation in some way.

After initial brainstorming, I thought about how I check the weather on my phone every morning, and although necessary, it's all a bit boring. I wanted to add a little surprise, delight, and excitement to checking the local temperature. The concept seemed simple enough to execute, allowing me to focus on the details without getting too overwhelmed by the scope. On the design and animation side, I've been intrigued by interactive animation for a while, originally with Unreal Engine. Lately, I've been hearing a lot about Rive, and how it's simple and intuitive interface is being used to create interactive animations on websites and apps. And apparently it would be quick to pick up since I'm already familiar with After Effects. At least that was the hope. I had been curious about it, and this was the perfect opportunity to experiment with it.

With those goals in mind, I set out to create a web app, likely using Python, HTML, CSS, and JS, that I would somehow integrate with an animated "weather face" created in Rive. The main flow would be: load the web app, allow the user to submit their location with a form, use an API to get the temperature from the location, and use that temperature to drive the character animation on the webpage.

#### >Coding
I started with the code, creating a flask server in Python, and a basic index HTML page that it would load. I knew one of my main coding hurdles would be getting and reading weather data. First I had to find a weather API that met some criteria: free, doesn't require a subscription or API key, lightweight, easy to understand. I ended up going with Open-Meteo, which checked all these boxes, and has very elegant documentation and presentation of how its API functions. I initially decided to write an API call in the Python server that was based on the one used in the Finance problem set. Before too long, I had a somewhat functional Python script that would make 2 API calls. One would send the input location (ZIP code or city) and request the latitude and longitude back. The next API call would send those geo coordinates and request the temperature back. I could then pass that temperature to my HTML template.

But I soon ran into some issues that didn't feel great. The user had to submit a form to the flask server, and once the python code was run, it would reload the webpage to refresh the HTML. It worked, but I was hoping for a more immediate update. Also, I was running into an issue where the first time I submitted the form and ran the API calls, everything was fine. But the second time the form was submitted, the API calls would hang without returning anything. I'm sure it was some coding error, but I was running into a wall trying to solve it.

I took a step back, and realized I was doing these API calls in the python server only because of my recent experience in using Python for the latest problem sets. I wondered if I could instead pull this off with JavaScript in order to get interactive updates without needing to reload the page. I had to dive in and start researching JS, but once I found out about the fetch() function, it all came together! I was able to properly string together API calls in the correct order, and get live updates to my web app!

#### >Rive Integration
The second half of the project would be learning the basics of Rive: both using the editor to create animations and a state machine, and then using the provided web runtime library to run and control the animations on my webpage. This took a lot of focused learning, and it certainly fired both sides of my brain as I ping-ponged between the design and animation, and the code implementation. To start, I created animations for 6 different character states. Default for when you first load the page, and then 5 weather states: Freezing, Cold, Mild, Hot, and Melting. I created a state machine that would transition to these states depending on a temperature input.

On the code side, the Rive runtime library for the web allows you to use Javascript to load the Rive state machine and the animations it controls, as well as request the inputs that are used to drive the state machine. The Rive player is loaded when the web page runs its Javascript, and once it is loaded, it listens for the  location "submit" button to be activated. When that happens, I make my API calls to update a temperature variable, which is what drives the state machine to activate different animations on the weather character.

At the end of the day, it's a fairly simple app, but it required me to learn a lot and combine skills in new ways. And I'm very happy I was able to solve the problems that were presented in order to create something that feels fun and responsive.

### Project Files:

#### >app.py
This is simply used to run the web server and serve my index.html page. It was originally where I was processing POST requests and making my API calls, but I ended up migrating that to Javascript.

#### >index.html
All the code for the content of my web app is here. I import Bootstrap for the main CSS styling and also use it for an Accordion element. I import a couple weights of a Google typeface that I use throughout the page. I also link to a custom, minimal CSS stylesheet.

For the body, I start with my heading text, and then implement a submission form where the user can type in a ZIP code or city location, and submit the information with a button. The submit button is tagged to return false so that it won't actually submit a form to a server, but rather just act as a trigger for JS.

Under that is a div called "feedback" that posts the requested location and temperature. Next is a canvas element that houses the Rive animation player, and finally a Bootstrap accordion element that contains a hidden input field where the user can enter in a temperature directly to play through the various character animation states.

The JS code comes next. First I set all my global variables, and then create a Rive object that contains the remainder of the code. The Rive object loads the Rive player in the canvas HTML element, then loads the weatherface.riv file I created, from which it pulls the state machine and sets it to autoplay the Default animation. Once the Rive player has finished loading it sends a callback that triggers the OnLoad function, within which contains the rest of the code. I get the inputs from the .riv file state machine (in this case there's only one, called "temp"), which lets me manipulate that variable within my JS code. I add an event listener to the input form's submit button. Once it's clicked, I reset some of my global variables, then I use the form data to prepare the geolocation URL that I will send to the weather API. I use the fetch method to pass the URL to an API that returns a response with the geolocation information. I parse the geolocation JSON to extract the latitude and longitude. I use the latitude and longitude to create a new URL that I pass to an API that returns a response with the weather forecast information. I parse the forecast JSON to extract the current temperature in Fahrenheit, setting the "temp" variable to that value.

I then call a riveCheck() function, passing in the temp value. This function sets the Rive state machine input to the new temperature value. Once this input variable is updated, it will trigger an animation based on a conditional check that is setup in the .riv file.

#### >weatherface.riv
This is the Rive runtime file that is exported from the Rive editor. It contains information about the vector graphics, state machines, animations, and inputs in your Rive file. This runtime file is loaded when the Rive object gets called in Javascript.

#### >styles.css
Basic CSS stylesheet I use to set font weight, colors, margins, etc.

