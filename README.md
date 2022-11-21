# rta-transient-receiver-comet

## Description
rta-transient-receiver-comet is a COMET plugin for handling VoEvents notices. The plugin writes the notices in a MySQL database and performs several processes for detecting a possible correlation among instruments. Then it sends an email alert to the team for further analysis.
This code just implements the class eventreciver and uses the code from https://github.com/ASTRO-EDU/rta-transient-receiver for the data manipulation. 

## Download
This repo contain a submodule so, clone the repo then download the submodules
```
git clone git@github.com:ASTRO-EDU/rta-transient-receiver-comet.git
cd rta-transient-receiver-comet/
git submodule update --init --recursive
```

## Installation

The dependencies are listed in the file requirement.txt. It is recommended to install them into a venv enviromnent.

For creating and install a new virtual enviroment: https://docs.python.org/3/library/venv.html

### Steps for installation:

First of all is important fill the config.json template with the required information. You can find this file in rta-transient-receiver/voeventhandler/config/config.json

Then create a new virtual enviroment in a folder named venv whith the following command:
```
python3 -m venv venv
```
Now activate the virtual enviroment whit the command:
```
source venv/bin/activate
```
Then install the dependency for the program and the submodule.
```
pip install -r rta-transient-receiver/requirements.txt 
pip install -r requirements.txt
```
And use the following commands for excecute the files setup.py to install the program 
```
pip install rta-transient-receiver/
pip install .
```

## Run transient-receiver

Comet commands can be found on the official documentation: https://comet.transientskp.org/en/stable/installation.html
For subscribing to a specific topic us needed specify the ip and receive-port

For example for reciving voevent from gcn the command is: 

```
twistd -n comet -r --local-ivo=ivo://hotwired.org --local-ivo=ivo://it.agile/mcal  --remote=45.58.43.186:8099 --receive-port=28098 --save-event --save-event-directory=/data01/homes/afiss/repos/voevents --receive-event
```

## Important email 
The code provides a special function for establish if a voevent is important and sholud be marked in a special way during the email notification. 
You can find this function in the path voeventhandler/emailnotifier.py and it's name is is_important(). 
From deafault configuration this class return False, but you can build yuor own rule creating conditional operations usign the field of the voeventdata object. For a fast look to what this field are look at the class voeventdata contained at path voeventhandler/utilis/voeventdata.py. The tag can be modified in the config file.
