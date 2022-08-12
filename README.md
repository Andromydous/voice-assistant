# voice-assistant
My own from scratch voice assistant. Tried to create it where "modules" could be added or removed.

command_list contains the dictionary of {"commands": related_function}

In order to get the current weather, you will have to sign up for openweathermap.org and get your
own api key. Then store your api key in a txt file in the same folder as the voice assitant files
are stored.

The way I have it setup is as follows: Functions that are called/tied to voice commands are in one file.
Functions that are not tied directly to voice commands, like get_weather(), are another file. To me, this
seemed the most readable way to do it.

If you're adding a "module", follow the above format and add {"command here": function here} to the command_list.
If you're removing a "module", just remove it from the command_modules.py and remove the dictionary entry from the
command_list.

IMPORTANT: If you're on Linux then you're stuck with either gTTS, which relies on Google Translate, or pyttsx3 sounding
like a robot. I will be working on a way to include both so that you can choose either or. Also, note that Google will only
allow a certain amount of translations per day. So reading from a pdf of any more than one page may come back as an error.
It's one of the key reasons that I'm considering adding in the pyttsx3 speech engine anyways.

First time use has a setup. Just follow the voice commands. You'll get to name your assistant and what name your voice assistant
calls you. Both your name and the voice assistants name are stored in their own separate txt file (1 for each).
