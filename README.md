# Tiktok Follow (While You Sleep)
The purpose of this project is to automate the TikTok following such that one can click the follow button while actually the bot is cliking (not a human). This program acts as a bot.

## Description
The code uses the selinium driver for Firefox. The code uses logger to log for errors and information extracted out of the program.

## Getting Started
### Dependencies

* Selinium  <br /> 
* logging

## Installing
* Firefox<br /> 
* Python 3.x <br />
## Executing program
Change the Firefox Profile in the code FirefoxProfile in tiktok_follow_Firefox_foryou.py<br /> 
ffProfile = FirefoxProfile('/Users/YOUR-USER-NAME/Library/Application Support/Firefox/Profiles/XYZ.default-release') <br /> 

https://support.mozilla.org/en-US/kb/profile-manager-create-remove-switch-firefox-profiles

### How to run the program
* Run Firefox Browser <br /> 
* Signin to tiktok <br /> 
* Execute command "python3 tiktok_follow_Firefox_foryou.py" <br /> 

### Useful Tips
* "watch grep -c 'FollowButtonClicked' std.log" to find how many time Follow button is clicked
* "tail -f std.log" to view the latest logs 

### Authors
KazimR <br /> 
@kazimr

### Version History
* 0.1

### License
This project is licensed under the Open Source License - see the LICENSE.md file for details
