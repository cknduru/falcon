#!/bin/bash
#echo "$1" | festival --tts
 pico2wave -w voice_tmp.wav "$1" && play voice_tmp.wav speed 0.95 && rm voice_tmp.wav