# Cloud-Titians - Voice-based Web browsing app for disabled people using Cloud APIs made by @[GeekyAmitesh](https://github.com/geekyamitesh)


## Deployment-website link - 'http://142.93.250.23/Incubate-Web-Assistant/speech-synthesis/browser-voices.html'


## Challenge given by Cloud Titans 

Basically you need to use a Text to speech API for a Web App that can be used in a browser like Chrome or Firefox.
In this Challenge, you need to make a Text to speech App as a prototype by your own set of names and data to convert it to speech [ should be working ].

## What I have made
1. I made this application for disbale people who can write,read and I have also included a prototype of voice controlled map.
2. I am begginer to do this work but Time to time I will make perfect web-assistant application that can be used by anyone free of cost.
3. I have added some feasible things in speech to text part(you can copy and mail)
4. This web assistant application has feasible for different different language
  
## Steps

Step 1 — Using the Web Speech API

The Web Speech API is broken into two major interfaces:
  
  1. SpeechSynthesis - For text-to-speech applications. This allows apps to read out their text content using the device’s speech synthesizer
   2. SpeechRecognition - For applications that require asynchronous voice recognition. This allows apps to recognize voice context from an audio input. 

Step 2 — Building the Text-to-Speech App

Step 3 — Building the Main Script

Step 4 — Building the website by use of bootsrap

Step 5 — I have also added some new feature such like speech to text other than text to speech

Step 6 — I deployed my website on Digitaloccean

step 7 — I added map api

### You can open project in local server by http://127.0.0.1:5503/speech-synthesis/browser-voices.html
### Show some :heart: and :star: the repo to support the project. 
For more, contact me @[facebook](https://www.facebook.com/amiteshmani.tiwari), @[Twitter](https://twitter.com/amitesh_mani) or @[Linkedin](https://www.linkedin.com/in/amitesh-mani-tiwari)



## Resources
 
How To Build a Text-to-Speech App with Web Speech API - Digital Ocean
>> https://www.digitalocean.com/community/tutorials/how-to-build-a-text-to-speech-app-with-web-speech-api

Samples & tutorials | Cloud Text-to-Speech Documentation - Sample GCP Projects for concept and reference.
>> https://cloud.google.com/text-to-speech/docs/samples

### Screenshots
   <img src="/screenshot/project1.PNG" height="200em"/>
   <img src="/screenshot/project2.PNG" height="200em" />
   <img src="/screenshot/project3.PNG" height="200em" />
 
### How can deploy on Digital-occean website
Step 1 — Go to @[Digital Ocean](https://www.digitalocean.com/) and sign up

Step 2 — Create a droplet(For deploying a static website, I think the cheapest plan would suffice.It is worth 5 dollars per month) 

Step 3  ***If you have not bought domain name or is not interested in setting one for your site just jump directly to setting up a web server part.***

Step 4 — Use this credentials, and do the following commands in terminal
             1. ssh root@IP_Address 
             2. type_your_password

Step 5 — For deploying  website We required server. I have used Nginx. ***Nginx is one of the most popular web servers in the world and is responsible for hosting some of the largest and highest-traffic sites on the internet***

Step 6 — Commands to install Nginx on Ubuntu
         1. Step One — Install Nginx
             a.sudo apt-get update
             b.sudo apt-get install nginx
             c.Check 'http://server_domain_name_or_IP'

         2. You can manage your web server by following commands
              a.To stop your web server
                 sudo service nginx stop
              b.start the web server
                 sudo service nginx start
              c. You want to reboot Server
                   sudo update-rc.d nginx defaults
              d. configure nginx to serve files from that directory
                 /etc/nginx/sites-available/default
              e. Restart nginx in order
                  sudo service nginx restart
              f. sudo chown -R user:user /srv/www
              ###I think this can solve your porblem.

## Facing Any Problem or need any Help:grey_question:
Write me in [issues]((https://github.com/geekyamitesh) section. I will try solve your issue within 10-12 hours.
</br>***Keep Developing and Destroying.*** :wink:

 

