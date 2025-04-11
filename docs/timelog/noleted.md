------------------------------------------------------------------------------------------------------------
Before Spring Break:
Before spring break, I spent approximately six hours researching the key risk factors of cardiovascular disease and searching for the ideal database for our project. 

Research Links:
https://link.springer.com/article/10.1007/s10916-016-0536-z
https://www.nature.com/articles/s41598-024-80919-9#Sec24

From these, I established an initial list of risk factors for CVD, HTN, and CAD:
--> CVD: Radiation exposure, age, ambient noise, irregular work hours, body weight and BMI, elevated triglyceride, history of HTN and CVD, elevated FBS levels, poor sitting posture, dust exposure, and smoking.
--> HTN: Continuous work shifts, BMI, body weight, family history of HTN, age, improper posture, elevated cholesterol levels, low HDL levels, gas exposure, prolonged sitting, smoking, dust exposure, and a history of HTN.
--> CAD: Smoking, Diabetes Mellitus, High Density Lipoprotein, Duke Treadmill Score, and Duration Recovery (from Duke Treadmill test)

Database Links:
https://www.kaggle.com/datasets/jocelyndumlao/cardiovascular-disease-dataset
https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators
https://www.kaggle.com/datasets/ankushpanday2/heart-attack-risk-and-prediction-dataset-in-india
https://www.kaggle.com/datasets/oktayrdeki/heart-disease
https://www.kaggle.com/datasets/thedevastator/exploring-risk-factors-for-cardiovascular-diseas/data

Final Database Link:
https://www.kaggle.com/datasets/ashishsahani/hospital-admissions-data/data
This database contains information collected from patients admitted to the Hero DMC Heart Institute, such as their age, sex, patient history, smoking status, alcohol use, hemoglobin, total lymphocyte count, platelets, glucose, urea, creatinine, brain natriuretic peptide, raised cardiac enzymes, and ejection fraction. 

This database was selected because it covers a wide array of risk factors and discusses multiple cardiovascular diseases. This makes it ideal for the Plan A+ version of our project, which can report the patient's risk for specific cardiovascular diseases.

Meetings:
I have met with Mariama to discuss the project every Tuesday and Saturday at 6:00PM to 6:30PM or 7:00PM. During these meetings, I presented my database research findings. In later meetings, Mariama has outlined the plan to analyze the data and has walked me through the code she has written in Jupyter. 

------------------------------------------------------------------------------------------------------------

Week of 3/24/25:
Monday: Spent 7 Hours (actually) watching Intro to HTML and Intro to CSS Tutorials and taking notes.
        Link: https://youtu.be/HGTJBPNC-Gw
              
Wednesday: Spent 6.5 Hours watching Intro to JavaScript and taking notes.
Thursday: Spent 3.5 Hours watching Intro to JavaScript and taking notes.
Friday: Spent 1.25 Hours watching Into to JavaScript and taking notes.
        Link: https://youtu.be/lfmg-EJ8gm4
        
Also on Friday: 0.5 Hours setting up Visual Studio Code and Linking Project Files
                1.5 Hours Intial GUI Coding
                
I now have a workspace in Visual Studio Code. I have installed the Live Server extension and can easily view the changes to my web GUI in real-time. I am following along with the web GUI outline provided in our design documents. Currently, I have created a home page containing a 'Login' button, which re-directs to a 'Login' page when clicked. This page has an in-progress form where the user can enter their username and password.
                
/* This week represented an above-average time-sink. I really wanted to learn JavaScript and
*  invested a LOT of time into it. All of the values above are genuinely accurate. I watched
*  a 1-hour HTML tutorial, a 4-hour CSS tutorial, and a 12-hour JavaScript tutorial in full.
*/

Saturday-Sunday: Spent 6.0 Hours constructing a draft of the MVP version of the graphical user interface. 

I now have a user interface which can validate user input into <input> and <select> elements. I have removed the possibility for the user to enter emojis or other unqiue characters that would be difficult to manage. I have created a system to ensure that the input in an <input> box is within a certain numerical range, which will be very helpful for validating our form before the user submits it.
------------------------------------------------------------------------------------------------------------

Week of 4/5/25:
Tuesday: Spent 1 Hour resarching how to submit HTML form data to MySQL using PHP. I eventually decided to abandon this approach in favor of using Flask. I then spent 2 Hours researching Flask, creating a Flask application, and integrating the existing user interface.
Later, I spent 1 Hour debugging to prevent the user from being able to access certain webpages without having first logged in. I spent another 1.5 Hours updating the user interface to more closely meet the requirements of the project. I reduced the JavaScript associated with each webpage and implemented error-checking in the Python back-end instead.

Wednesday: I spent 2 Hours researching how to use databases with Flask. I then spent 1 Hour coding what I had learned. The result was the creation of three databases, into which I could permanently place entries from the web application.

Thursday: I spent 2 Hours finalizing the databases, and then 0.75 Hours meeting with Mariama to discuss plans for RAPS, followed by 1.5 Hours of creating a presentation.
