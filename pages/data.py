# aici vei prelua toate datele din interfata cu campuri de completat
# type here title you want
from  mysqlP import *

mycursor = connector()

titleCV = "CV"

# type here your name and surname
yourName = mycursor.execute("SELECT yourName FROM cv")

# type here current profession
yourProfession =  mycursor.execute("SELECT yourProfession FROM cv")

# type here your bio
yourBio = mycursor.execute("SELECT yourBio FROM cv")

# type here your current location
yourCountry = mycursor.execute("SELECT yourCountry FROM cv")

# if you want add another social media account, add here icon code of it
socialContact = mycursor.execute("SELECT socialContact FROM cv").split(",")

# type here some contact
yourContact = mycursor.execute("SELECT yourContact FROM cv").split(",")

# type here your birthday and (your age)
yourBirthday = mycursor.execute("SELECT yourBirthday FROM cv")

# type here your skills
yourSkills = mycursor.execute("SELECT yourSkills FROM cv").split(",")

# type here your hobbies
yourHobbies =mycursor.execute("SELECT yourHobbies FROM cv").split(",")

# type here your certificates
yourCerts =mycursor.execute("SELECT yourCerts FROM cv")

# type here your education info
yourEdu = mycursor.execute("SELECT yourEdu FROM cv")

# type here your education years (start-end)
eduYear = mycursor.execute("SELECT eduYear FROM cv")

# type here your work history
yourWork = mycursor.execute("SELECT yourWork FROM cv")

# type here your work years (start-end)
workYear = mycursor.execute("SELECT workYear FROM cv")

# type here your projects
yourProject = mycursor.execute("SELECT yourProject FROM cv")

# type here your projects link (if there is)
projectLink = mycursor.execute("SELECT projectLink FROM cv")

# type here your extras (driving license etc.)
yourExtras = [
    '-',
]

# footer text in here (please don't change)
footerText = "CV<a target='_blank' class='author' href='https://github.com/vmaria2002/proiect_IS'>cod</a>"

# thank you for use this template.