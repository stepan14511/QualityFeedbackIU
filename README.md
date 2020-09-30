# QualityFeedbackIU
Quality Feedback project for FSE course in IU 2020.

## Installation

### Linux

Make sure that you have python3 and pip3 installed. After that install requirements:

```pip3 install -r requirements.txt```

To start the server go to `./qualityfeedback/` and run:

```python3 ./manage.py runserver```

### Windows

#### cmd

Also, to run the server you should have python 3.X installed. Install requirements:

```python -m pip install -r requirements.txt```

And start the server:

```
cd qualityfeedback
python ./manage.py runserver
```

#### PyCharm

Open PyCharm and press `Get from Version Control`. Then enter the link to this repo and press `Clone`.

When the project will be opened, make sure that you have python 3.X interpreter in the bottom right of the IDE.

Open the `requirements.txt` file. IDE could suggest you to install requirements - in this case press install. If not - click the right mouse button, `Install All Packages`.

Finally, to run the server, go to the subdirectory `./qualityfeedback` and open `manage.py`. Press `Alt+Shift+F10 -> Edit Configurations`. In the field `Parameters` type `runserver`, then `Apply -> close the window`. And now you can run it with `Shift+F10`
