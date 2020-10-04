# QualityFeedbackIU
Quality Feedback project for FSE course in IU 2020.

## Installation

### Run postgresql

#### Linux/MacOS

Setup docker-compose, go to `./postgres` and run:

```sudo docker-compose up --build```

### Run the server

#### Linux/MacOS

Make sure that you have python3 and pip3 installed. After that install requirements:

```pip3 install -r requirements.txt```

To configure needed tables and start the server go to `./qualityfeedback/` and run:

```
python3 ./manage.py migrate
python3 ./manage.py runserver
```

#### Windows

##### cmd

Also, to run the server you should have python 3.X installed. Install requirements:

```python -m pip install -r requirements.txt```

Configure needed tables and start the server:

```
cd qualityfeedback
python ./manage.py migrate
python ./manage.py runserver
```

##### PyCharm

Open PyCharm and press `Get from Version Control`. Then enter the link to this repo and press `Clone`.

When the project will be opened, make sure that you have python 3.X interpreter in the bottom right of the IDE.

Open the `requirements.txt` file. IDE could suggest you to install requirements - in this case press install. If not - click the right mouse button, `Install All Packages`.

Note: go to the Windows cmd step to configure needed tables using `migrate`

Finally, to run the server, go to the subdirectory `./qualityfeedback` and open `manage.py`. Press `Alt+Shift+F10 -> Edit Configurations`. In the field `Parameters` type `runserver`, then `Apply -> close the window`. And now you can run it with `Shift+F10`
