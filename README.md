# INSTABOT_ALCAROHTAR ![Python_logo_mini](https://user-images.githubusercontent.com/89790994/132233323-31f21542-912d-4422-a8ae-3f0cd2d11c8a.jpg)

InstaBot is an instagram bot to add likes and comments automatically. It is also possible to follow or unfollow different users.
Users are saved in follower_InstaBot and follower_history_InstaBot files.
First file is blanked when unfollow command is sent.
Second file is never blanked since it is useful to check if user has ever been followed and never do it again.  


![Schermata_GUI](https://user-images.githubusercontent.com/89790994/132232211-147e7bc8-40d3-44e8-8603-870e5fda091c.jpg)
  
  
## What do you need?
- Firefox browser
- Download and modify the three text files: 
	1. tag_InstaBot (insert on each line a tag to search with also # symbol)
	2. user_InstaBot (insert user and password as in the example)
	3. comments_InstaBot (insert on each line a comment. The comment will be chosen randomly)
- Download InstaBot_Alcarohtar that is the executable file or InstaBot_Alcarohtar.py if you want to check the code or run the program by terminal
- Download geckodriver (you can find it on web for every OS) and copy it in one of the system path inside the $PATH variable. Usually /bin, /usr/local/bin and so on
- ***All files have to be in same directory***

## Options available
'1: Put a like'  
'2: Put a comment'  
'3: Like and comment on the photos'  
'4: Put a like and follow users'  
'5: Put a comment and follow users'  
'6: Unfollow users in follow_InstaBot file'  
  
## File Explanation
- InstaBot_Alcarohtar.py is the python source code. It could be useful if you need to check or modify the code. It could be run by terminal as **python3 InstaBot_Alcarohtar.py**
- InstaBot_Alcarohtar and InstaBot_Alcarohtar_MacOs are the two exe files for Linux or MacOs system. 
- comment_InstaBot is the file where to add the comments. They have to be added one for each line.
- tag_InstaBot is the file where to add the tag index, one for each line, with # at the beginning.
- follower_InstaBot has not to be modified. It records the user followed. It will be completely deleted when unfollowed option (6) is selected. 
- follower_history_InstaBot has never erased. It records the user followed history, so they will never follow again after unfollow.
- userpwd_InstaBot is useful to add user and password to login on Instagram. Not remove the "user:" and "password:".
  
***It has been tested on linux os and MacOs. New tests on windows will be done soon.***  
