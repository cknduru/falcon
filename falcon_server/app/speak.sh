#!/bin/bash
#echo "$1" | festival --tts
# gain is to prevent distortion
pico2wave -w voice_tmp.wav "$1" && play voice_tmp.wav speed 0.99 vol 6 gain -1 && rm voice_tmp.wav
