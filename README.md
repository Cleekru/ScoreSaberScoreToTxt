# ScoreSaberScoreToTxt
A script that reads ScoreSaber profile statistics and writes it in a file in a human readable form.
Useful for displaying your rank in f.e. a livestream.

# Setup
* Open the "config.ini" file and put in the URL of your ScoreSaber profile and set your country.
* Run the "ScoreSaberScoreToTxt.py" script.
* This creates a "ranking.txt" file which is updated every 20 seconds while the script is running.

# Config
Other optional settings:
* refreshrate: the number of seconds between updates of the txt file (Deafult: 20)
* filename: the name of the file the script is writing in (Deafult: ranking.txt)
* country: set the description of your regional score (Deafult: Regional)
