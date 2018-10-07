sudo apt-get install portaudio19-dev
sudo apt-get install python3-pyaudio
pip3 install pyaudio
pip3 install SpeechRecognition
pip3 install gTTS
python3 -m pip install -U mypy

cd ZeroSeg/
sudo python3 setup.py install
sudo pip install spidev