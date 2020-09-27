## SlideCast: Low Bandwith Presentation Recording Software

Slidecase is a low bandwith presentation software meant for delivery of online lectures done as an RnD under CSE Department IIT Bombay.


### Installation 

On Ubuntu, the software needs some packages to be installed for it to work. First clone the repository and install the following packages.

```
sudo apt-get install ffmpeg
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
```
These commands install the audio libraries needed for recording. Then install the python packages needed by typing the following command from the terminal:
```
pip install -r requirements.txt
```

This should install all the packages. Note that we need the script to be run as root since we are capturing the mouse and keyboard events in the recorder file.

To run the GUI run the following command from the terminal:
```
sudo python gui.py
```

Please note that only Python 3 is supported so ensure that the pip packages are installed in Python 3 and that Python 3 is called to run the program.