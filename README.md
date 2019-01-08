# MidiToArduinoSoftware
A software of which converts .mid files to arduino code which can be played through peizo buzzers.
Made for a science project.

# Building
## Requirements

If you haven't already, install any version of python 3.x

The only dependency you'll need is `python3-midi` found [here](https://github.com/louisabraham/python3-midi). Don't worry about installing manually though, just `cd` into the directory of this source and run `python3 -m pip install -r requirements.txt` and it should install everything. 
## Downloading
You can either use `git clone git@github.com:SenorEsqueleto/MidiToArduinoSoftware.git` or just press the "Clone or download" button on this website and press "Download ZIP". Extract/place the files somewhere and `cd` to it
## Running
Make sure you're using an enviroment where you can provide user input, and that you installed the libraries mentioned earlier. `cd` to the directory you placed your files and run `python3 main.py`. The program will ask you which .mid file to use and start the process
## Using
You can add .mid files to use by simply putting them in the same directory as the main.py. Once the process is finished, as long as you didn't get an error, the code will be written to `result.txt` in the same folder.

# TODO (In no particular order)
* Put `.mid`s in their own folder, along with the header/footer text.
* All notes supported
* Output a complete Arduino sketch instead of a .txt
* Fix tempo problems with ticks-per-beat making songs faster/slower
* User friendli-ness
* Remove `mido` dependency
* ???

# Authors
This converter was made by Elijah and Ethan (last names undisclosed)
For school, we were asked to create a science project that we could measure and make a graph out of. Well frankly we threw all of that out the window, and got permission from the teacher to do an activity project instead.

# Credit
Huge thanks to the creator of [vishnubob](https://github.com/vishnubob/python-midi) for the midi library we use, and [louisabraham](https://github.com/louisabraham/python3-midi) for his python3 port. 
