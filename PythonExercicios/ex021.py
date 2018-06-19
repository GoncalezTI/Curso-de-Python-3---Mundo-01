'''021 - Faça um programa em Python que abra e reproduza um áudio
de um arquivo MP3.'''

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('ACDC - Back in Black')
