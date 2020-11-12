# yhack2020

In the yhack zip file:
Should contain everything to launch a basic homepage, etc. Hopefully by looking at the structure of the index/question 1 functions in applications.py, it makes sense how the rest of the questions will work. 

To run the program, it should work by just typing "flask run" into the terminal (once you're in the yhack folder). 

Question1, question2, question3, etc. will be their own HTML files. each of those HTML files would have a corresponding function (as indicated), that is filled out. 

The "GET" and "POST" methods are basically to help distinguish between when we just need to show the user the html file (i.e. show the user the question), versus when we need to do something based on their response (indicate some information based on an answer). 

In the index function in application.py, you can see an if for request.method == "POST" and an else (which will correspond to "GET"). "GET" is when the user wants information from us, like the web page, and "POST" is when the user has submitted info to us (like clicked the submit button with an answer). Based on the "answers" (buttons pressed, etc) of a user, we can keep track of a point variable, move the user to the next question by saying something like "return render_template("question4.html")". For "GET", which we would assume is the "else" condition, we would just be saying "return render_template("question3.html")" if we are wanting the user to answer the third question/are on the 3rd question's function. 

Hopefully that makes sense!!

**To download yhack.zip**
1) Click on the top green button which says *Code*
2) Click on *download as zip*
3) Extract the folder, extract *yhack* within the folder

**If running it in anaconda prompt in Windows 10:**
1) run `pip install flask_session` (only the first time you run this program)
2) Navigate to yhack folder using `cd Desktop/FIGHTS/YHack/yhack2020-main/yhack` , this will vary for you depending on where the yhack folder is located.
3) run `set FLASK_APP=application.py`
4) run `flask run`

Terminal displays warning-

`WARNING: This is a development server. Do not use it in a production deployment.`
