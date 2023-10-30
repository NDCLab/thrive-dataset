#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on October 29, 2023, at 17:01
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'arrow-alert-v1-2'  # from the Builder filename that created this script
expInfo = {
    'id': '',
    'counterbalance': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'],
    'skipOther': '0',
    'session': '1',
    'run': '1',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/sub-%s_%s_psychopy_s%s_r%s_e1' % (expInfo['id'], expName, expInfo['session'], expInfo['run'], )

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\NDCLab\\Desktop\\Experiments\\THRIVE\\arrow-alert-v1-2\\arrow-alert_v1-2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='sys-1-asus', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "JS_code" ---

# --- Initialize components for Routine "setup" ---
# Run 'Begin Experiment' code from setup_code
import serial #used for sending eeg triggers
import time #indirerctly used for sending eeg triggers (how long to wait before clearing port)

win.mouseVisible = False #hide mouse cursor
port = serial.Serial('COM4') # Open specified serial port (COM4) for sending eeg triggers to   
PulseWidth = 0.002 #how long to wait before clearing port after sending trigger (2 ms is sufficient at 1000 hz sampling rate)
port.write([0x00]) #clear serial port
time.sleep(PulseWidth) #wait PulseWidth amount of time before doing anything else

# --- Initialize components for Routine "logo" ---
logo_image = visual.ImageStim(
    win=win,
    name='logo_image', 
    image='img/logo2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.2,.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
logo_resp = keyboard.Keyboard()

# --- Initialize components for Routine "welcome" ---
welcome_keyResp = keyboard.Keyboard()
welcome_keyResp2 = keyboard.Keyboard()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
welcome_text2 = visual.TextStim(win=win, name='welcome_text2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "instructRightSingle" ---
instructRightSingle_keyResp = keyboard.Keyboard()
instructRightSingle_keyResp_2 = keyboard.Keyboard()
instructRightSingle_keyResp_3 = keyboard.Keyboard()
instructRightSingle_keyResp_4 = keyboard.Keyboard()
instructRightSingle_keyResp_5 = keyboard.Keyboard()
instructRightSingle_text = visual.TextStim(win=win, name='instructRightSingle_text',
    text='This arrow is pointing to the RIGHT. \n\n\n\n\n\n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
instructRightSingle_text_2 = visual.TextStim(win=win, name='instructRightSingle_text_2',
    text='This arrow is pointing to the RIGHT. \n\nYou can tell this arrow is pointing to the RIGHT by looking at which side the point is on.\n\n\n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
instructRightSingle_text_3 = visual.TextStim(win=win, name='instructRightSingle_text_3',
    text='This arrow is pointing to the RIGHT. \n\nYou can tell this arrow is pointing to the RIGHT by looking at which side the point is on.\n\nThe point is on the RIGHT, so the arrow is pointing this way.\n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
instructRightSingle_text_4 = visual.TextStim(win=win, name='instructRightSingle_text_4',
    text='This arrow is pointing to the RIGHT. \n\nYou can tell this arrow is pointing to the RIGHT by looking at which side the point is on.\n\nThe point is on the RIGHT, so the arrow is pointing this way.\n\nYou would respond to this arrow by pressing the RIGHT button with your RIGHT hand.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instructRightSingle_text_5 = visual.TextStim(win=win, name='instructRightSingle_text_5',
    text='This arrow is pointing to the RIGHT. \n\nYou can tell this arrow is pointing to the RIGHT by looking at which side the point is on.\n\nThe point is on the RIGHT, so the arrow is pointing this way.\n\nYou would respond to this arrow by pressing the RIGHT button with your RIGHT hand.\n\nPress the RIGHT button to continue.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
instructRightSingle_rightArrow = visual.ImageStim(
    win=win,
    name='instructRightSingle_rightArrow', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.08, .08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-10.0)
instructRightSingle_rightArrowHighlight = visual.ImageStim(
    win=win,
    name='instructRightSingle_rightArrowHighlight', 
    image='img/rightArrowHighlight.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.08, .08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-11.0)
instructRightSingle_rightArrowSolid = visual.ImageStim(
    win=win,
    name='instructRightSingle_rightArrowSolid', 
    image='img/rightArrowSolid.png', mask=None, anchor='center',
    ori=0, pos=(0, -.4), size=(.08, .08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-12.0)

# --- Initialize components for Routine "instructLeftSingle" ---
instructLeftSingle_keyResp = keyboard.Keyboard()
instructLeftSingle_keyResp_2 = keyboard.Keyboard()
instructLeftSingle_keyResp_3 = keyboard.Keyboard()
instructLeftSingle_keyResp_4 = keyboard.Keyboard()
instructLeftSingle_keyResp_5 = keyboard.Keyboard()
instructLeftSingle_text = visual.TextStim(win=win, name='instructLeftSingle_text',
    text='This arrow is pointing to the LEFT. \n\n\n\n\n\n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
instructLeftSingle_text_2 = visual.TextStim(win=win, name='instructLeftSingle_text_2',
    text='This arrow is pointing to the LEFT. \n\nYou can tell this arrow is pointing to the LEFT by looking at which side the point is on.\n\n\n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
instructLeftSingle_text_3 = visual.TextStim(win=win, name='instructLeftSingle_text_3',
    text='This arrow is pointing to the LEFT. \n\nYou can tell this arrow is pointing to the LEFT by looking at which side the point is on.\n\nThe point is on the LEFT, so the arrow is pointing this way.\n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
instructLeftSingle_text_4 = visual.TextStim(win=win, name='instructLeftSingle_text_4',
    text='This arrow is pointing to the LEFT. \n\nYou can tell this arrow is pointing to the LEFT by looking at which side the point is on.\n\nThe point is on the LEFT, so the arrow is pointing this way.\n\nYou would respond to this arrow by pressing the LEFT button with your LEFT hand.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instructLeftSingle_text_5 = visual.TextStim(win=win, name='instructLeftSingle_text_5',
    text='This arrow is pointing to the LEFT. \n\nYou can tell this arrow is pointing to the LEFT by looking at which side the point is on.\n\nThe point is on the LEFT, so the arrow is pointing this way.\n\nYou would respond to this arrow by pressing the LEFT button with your LEFT hand.\n\nPress the LEFT button to continue.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
instructLeftSingle_leftArrow = visual.ImageStim(
    win=win,
    name='instructLeftSingle_leftArrow', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.08, .08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-10.0)
instructLeftSingle_leftArrowHighlight = visual.ImageStim(
    win=win,
    name='instructLeftSingle_leftArrowHighlight', 
    image='img/leftArrowHighlight.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.08, .08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-11.0)
instructLeftSingle_leftArrowSolid = visual.ImageStim(
    win=win,
    name='instructLeftSingle_leftArrowSolid', 
    image='img/leftArrowSolid.png', mask=None, anchor='center',
    ori=0, pos=(0, -.4), size=(.08, .08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-12.0)

# --- Initialize components for Routine "instructMiddle" ---
instructMiddle_keyResp = keyboard.Keyboard()
instructMiddle_keyResp2 = keyboard.Keyboard()
welcome_text_2 = visual.TextStim(win=win, name='welcome_text_2',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
welcome_text2_2 = visual.TextStim(win=win, name='welcome_text2_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "instructRight" ---
instructRight_text = visual.TextStim(win=win, name='instructRight_text',
    text='Below, the MIDDLE arrow is pointing to the right, so you would respond by pressing the right button with your right hand.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRight_centerImg = visual.ImageStim(
    win=win,
    name='instructRight_centerImg', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructRight_rightImg1 = visual.ImageStim(
    win=win,
    name='instructRight_rightImg1', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructRight_rightImg2 = visual.ImageStim(
    win=win,
    name='instructRight_rightImg2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructRight_leftImg1 = visual.ImageStim(
    win=win,
    name='instructRight_leftImg1', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
instructRight_leftImg2 = visual.ImageStim(
    win=win,
    name='instructRight_leftImg2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
insructRight_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "instructRight_2" ---
instructRight_text_2 = visual.TextStim(win=win, name='instructRight_text_2',
    text='Below, the MIDDLE arrow is pointing to the right, so you would respond by pressing the right button with your right hand.\n\nPress the right button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRight_centerImg_2 = visual.ImageStim(
    win=win,
    name='instructRight_centerImg_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructRight_rightImg1_2 = visual.ImageStim(
    win=win,
    name='instructRight_rightImg1_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructRight_rightImg2_2 = visual.ImageStim(
    win=win,
    name='instructRight_rightImg2_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructRight_leftImg1_2 = visual.ImageStim(
    win=win,
    name='instructRight_leftImg1_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
instructRight_leftImg2_2 = visual.ImageStim(
    win=win,
    name='instructRight_leftImg2_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
insructRight_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructLeft" ---
instructLeft_text = visual.TextStim(win=win, name='instructLeft_text',
    text='Below, the MIDDLE arrow is pointing to the left, so you would respond by pressing the left button with your left hand.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructLeft_centerImg = visual.ImageStim(
    win=win,
    name='instructLeft_centerImg', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructLeft_rightImg1 = visual.ImageStim(
    win=win,
    name='instructLeft_rightImg1', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructLeft_rightImg2 = visual.ImageStim(
    win=win,
    name='instructLeft_rightImg2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructLeft_leftImg1 = visual.ImageStim(
    win=win,
    name='instructLeft_leftImg1', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
instructLeft_leftImg2 = visual.ImageStim(
    win=win,
    name='instructLeft_leftImg2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
instructLeft_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "instructLeft_2" ---
instructLeft_text_2 = visual.TextStim(win=win, name='instructLeft_text_2',
    text='Below, the MIDDLE arrow is pointing to the left, so you would respond by pressing the left button with your left hand.\n\nPress the left button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructLeft_centerImg_2 = visual.ImageStim(
    win=win,
    name='instructLeft_centerImg_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructLeft_rightImg1_2 = visual.ImageStim(
    win=win,
    name='instructLeft_rightImg1_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructLeft_rightImg2_2 = visual.ImageStim(
    win=win,
    name='instructLeft_rightImg2_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructLeft_leftImg1_2 = visual.ImageStim(
    win=win,
    name='instructLeft_leftImg1_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
instructLeft_leftImg2_2 = visual.ImageStim(
    win=win,
    name='instructLeft_leftImg2_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
instructLeft_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructInconRight" ---
instructInconRight_text = visual.TextStim(win=win, name='instructInconRight_text',
    text='Sometimes the MIDDLE arrow will point in a different direction from the other arrows. However, your goal is to always respond to the MIDDLE arrow.\n\nBelow, the MIDDLE arrow is pointing to the right, so you would respond by pressing the right button with your right hand.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructIncon_centerImg = visual.ImageStim(
    win=win,
    name='instructIncon_centerImg', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructIncon_rightImg1 = visual.ImageStim(
    win=win,
    name='instructIncon_rightImg1', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructIncon_rightImg2 = visual.ImageStim(
    win=win,
    name='instructIncon_rightImg2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructIncon_leftImg1 = visual.ImageStim(
    win=win,
    name='instructIncon_leftImg1', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
instructInconRight_leftImg2 = visual.ImageStim(
    win=win,
    name='instructInconRight_leftImg2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
insructInconRight_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "instructInconRight_2" ---
instructInconRight_text_2 = visual.TextStim(win=win, name='instructInconRight_text_2',
    text='Sometimes the MIDDLE arrow will point in a different direction from the other arrows. However, your goal is to always respond to the MIDDLE arrow.\n\nBelow, the MIDDLE arrow is pointing to the right, so you would respond by pressing the right button with your right hand.\n\nPress the right button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructIncon_centerImg_2 = visual.ImageStim(
    win=win,
    name='instructIncon_centerImg_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructIncon_rightImg1_2 = visual.ImageStim(
    win=win,
    name='instructIncon_rightImg1_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructIncon_rightImg2_2 = visual.ImageStim(
    win=win,
    name='instructIncon_rightImg2_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructIncon_leftImg1_2 = visual.ImageStim(
    win=win,
    name='instructIncon_leftImg1_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
instructInconRight_leftImg2_2 = visual.ImageStim(
    win=win,
    name='instructInconRight_leftImg2_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
insructInconRight_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructInconLeft" ---
instructInconLeft_text = visual.TextStim(win=win, name='instructInconLeft_text',
    text='Below, the MIDDLE arrow is pointing to the left, so you would respond by pressing the left button with your left hand.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructInconLeft_centerImg = visual.ImageStim(
    win=win,
    name='instructInconLeft_centerImg', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructInconLeft_rightImg1 = visual.ImageStim(
    win=win,
    name='instructInconLeft_rightImg1', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructInconLeft_rightImg2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_rightImg2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructInconLeft_leftImg1 = visual.ImageStim(
    win=win,
    name='instructInconLeft_leftImg1', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
instructInconLeft_leftImg2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_leftImg2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
instructInconLeft_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "instructInconLeft_2" ---
instructInconLeft_text_2 = visual.TextStim(win=win, name='instructInconLeft_text_2',
    text='Below, the MIDDLE arrow is pointing to the left, so you would respond by pressing the left button with your left hand.\n\nPress the left button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructInconLeft_centerImg_2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_centerImg_2', 
    image='img/leftArrow.png', mask=None, anchor='center',
    ori=0, pos=(0, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instructInconLeft_rightImg1_2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_rightImg1_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
instructInconLeft_rightImg2_2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_rightImg2_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
instructInconLeft_leftImg1_2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_leftImg1_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.05, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
instructInconLeft_leftImg2_2 = visual.ImageStim(
    win=win,
    name='instructInconLeft_leftImg2_2', 
    image='img/rightArrow.png', mask=None, anchor='center',
    ori=0, pos=(-.1, -.3), size=(.04, .04),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
instructInconLeft_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "respond_onceInstruct" ---
respond_once_text = visual.TextStim(win=win, name='respond_once_text',
    text='Each time you see the arrows appear, respond as quickly as you can without making mistakes.\n\nHowever, only respond once each time you see the arrows appear. Even if you think you made the wrong response, do not respond again until you see the next set of arrows appear.\n\nExperimenter: demonstrate how to respond',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
respond_once_key_resp1 = keyboard.Keyboard()

# --- Initialize components for Routine "eeg_trigger_check" ---
# Run 'Begin Experiment' code from triggerCheck_code
#initialize usb connected variable
usbConnected = 1
triggerIssue_text = visual.TextStim(win=win, name='triggerIssue_text',
    text='EEG EQUIPMENT ISSUE: please ring bell for experimenter',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prac_blockReminders" ---
# Run 'Begin Experiment' code from prac_initAcc_code
#initialize the following variables at the start of experiment
trialNum = 0
accuracy = 0
numCorr = 0
blockAcc = 0
prac_blockText = visual.TextStim(win=win, name='prac_blockText',
    text='Practice',
    font='Arial',
    pos=(0, .3), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_reminder_text = visual.TextStim(win=win, name='prac_reminder_text',
    text='Remember to limit blinking to about once every ten seconds. Try to relax the muscles in your face, neck, and shoulders. \n\nRespond as quickly as you can without making mistakes. Only respond once each time you see the arrows appear.\n\nAlways respond to the direction of the MIDDLE arrow.\n\nTo get ready, rest your thumbs on the right and left buttons.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
prac_reminder_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_blockReminders_2" ---
prac_blockText_2 = visual.TextStim(win=win, name='prac_blockText_2',
    text='Practice',
    font='Arial',
    pos=(0, .3), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prac_reminder_text_2 = visual.TextStim(win=win, name='prac_reminder_text_2',
    text='Remember to limit blinking to about once every ten seconds. Try to relax the muscles in your face, neck, and shoulders. \n\nRespond as quickly as you can without making mistakes. Only respond once each time you see the arrows appear.\n\nAlways respond to the direction of the MIDDLE arrow.\n\nTo get ready, rest your thumbs on the right and left buttons.\n\nPress the right button to begin.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prac_reminder_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_initFixation" ---
initFixation_img_2 = visual.ImageStim(
    win=win,
    name='initFixation_img_2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, -.71), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# --- Initialize components for Routine "prac_stimRoutine" ---
# Run 'Begin Experiment' code from prac_isi_code
#initialize the thisISI variable
thisISI = 0
prac_centerImg = visual.ImageStim(
    win=win,
    name='prac_centerImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=[.6, .6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
prac_rightImg1 = visual.ImageStim(
    win=win,
    name='prac_rightImg1', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(.71, 0), size=[.6, .6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
prac_rightImg2 = visual.ImageStim(
    win=win,
    name='prac_rightImg2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(1.42, 0), size=[.6, .6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
prac_leftImg1 = visual.ImageStim(
    win=win,
    name='prac_leftImg1', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-.71, 0), size=[.6, .6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
prac_leftImg2 = visual.ImageStim(
    win=win,
    name='prac_leftImg2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-1.42, 0), size=(.6, .6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
prac_fixImg = visual.ImageStim(
    win=win,
    name='prac_fixImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, -.71), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
prac_stim_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_blockFeed" ---
prac_blockFeed_text = visual.TextStim(win=win, name='prac_blockFeed_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prac_pressContinue = visual.TextStim(win=win, name='prac_pressContinue',
    text='Experimenter: press key to continue',
    font='Arial',
    pos=(0, -.3), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_blockFeed_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "task_condition" ---
# Run 'Begin Experiment' code from condition_init_blockCounter
#initialize the following variables at the start of the condition
blockCounter = 0
endCondition = 0 
condition_whichCondition_text = visual.TextStim(win=win, name='condition_whichCondition_text',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.22, wrapWidth=1.8, ori=0.0, 
    color=[-0.3,-0.3,-0.3], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
condition_reminder_text = visual.TextStim(win=win, name='condition_reminder_text',
    text='Experimenter: provide instructions and then press key to continue',
    font='Arial',
    pos=(0, -.3), height=0.04, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
condition_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "eeg_trigger_check" ---
# Run 'Begin Experiment' code from triggerCheck_code
#initialize usb connected variable
usbConnected = 1
triggerIssue_text = visual.TextStim(win=win, name='triggerIssue_text',
    text='EEG EQUIPMENT ISSUE: please ring bell for experimenter',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "task_blockReminders" ---
task_blockText = visual.TextStim(win=win, name='task_blockText',
    text='',
    font='Arial',
    pos=(0, .14), height=0.12, wrapWidth=1.8, ori=0.0, 
    color=[-0.3,-0.3,-0.3], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
task_blockReminders_text = visual.TextStim(win=win, name='task_blockReminders_text',
    text='Remember to limit blinking to about once every ten seconds. Try to relax the muscles in your face, neck, and shoulders. \n\nRespond as quickly as you can without making mistakes. Only respond once each time you see the arrows appear.\n\nAlways respond to the direction of the MIDDLE arrow.\n\nTo get ready, rest your thumbs on the right and left buttons.\n\nPress the right button to begin.',
    font='Arial',
    pos=(0, -.19), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
task_blockReminders_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "task_initFixation" ---
initFixation_img = visual.ImageStim(
    win=win,
    name='initFixation_img', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, -.71), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "task_stimRoutine" ---
# Run 'Begin Experiment' code from task_isi_code
#no need to initialize thisISI, as already done in practice code snippit
task_centerImg = visual.ImageStim(
    win=win,
    name='task_centerImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(.6, .6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
task_rightImg1 = visual.ImageStim(
    win=win,
    name='task_rightImg1', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(.71, 0), size=(.6, .6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
task_rightImg2 = visual.ImageStim(
    win=win,
    name='task_rightImg2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(1.42, 0), size=(.6, .6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
task_leftImg1 = visual.ImageStim(
    win=win,
    name='task_leftImg1', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-.71, 0), size=(.6, .6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
task_leftImg2 = visual.ImageStim(
    win=win,
    name='task_leftImg2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-1.42, 0), size=(.6, .6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=True,
    texRes=512, interpolate=True, depth=-6.0)
task_fixImg = visual.ImageStim(
    win=win,
    name='task_fixImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, -.71), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
task_stim_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "task_blockFeed" ---
task_blockFeed_text = visual.TextStim(win=win, name='task_blockFeed_text',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.12, wrapWidth=1.8, ori=0, 
    color=[-0.3,-0.3,-0.3], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
task_blackFeed_text3 = visual.TextStim(win=win, name='task_blackFeed_text3',
    text='Please wait',
    font='Arial',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
task_blockFeed_text2 = visual.TextStim(win=win, name='task_blockFeed_text2',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
task_blockFeed_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "task_conditionComplete" ---
conditionComplete_text = visual.TextStim(win=win, name='conditionComplete_text',
    text='Please ring bell and wait for experimenter to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
conditionComplete_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "JS_code" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
JS_codeComponents = []
for thisComponent in JS_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "JS_code" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in JS_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "JS_code" ---
for thisComponent in JS_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "JS_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "setup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup" ---
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "logo" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
logo_resp.keys = []
logo_resp.rt = []
_logo_resp_allKeys = []
# keep track of which components have finished
logoComponents = [logo_image, logo_resp]
for thisComponent in logoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "logo" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *logo_image* updates
    if logo_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        logo_image.frameNStart = frameN  # exact frame index
        logo_image.tStart = t  # local t and not account for scr refresh
        logo_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(logo_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'logo_image.started')
        logo_image.setAutoDraw(True)
    
    # *logo_resp* updates
    waitOnFlip = False
    if logo_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        logo_resp.frameNStart = frameN  # exact frame index
        logo_resp.tStart = t  # local t and not account for scr refresh
        logo_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(logo_resp, 'tStartRefresh')  # time at next scr refresh
        logo_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(logo_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(logo_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if logo_resp.status == STARTED and not waitOnFlip:
        theseKeys = logo_resp.getKeys(keyList=['c'], waitRelease=False)
        _logo_resp_allKeys.extend(theseKeys)
        if len(_logo_resp_allKeys):
            logo_resp.keys = _logo_resp_allKeys[-1].name  # just the last key pressed
            logo_resp.rt = _logo_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in logoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "logo" ---
for thisComponent in logoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "logo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcome_keyResp.keys = []
welcome_keyResp.rt = []
_welcome_keyResp_allKeys = []
welcome_keyResp2.keys = []
welcome_keyResp2.rt = []
_welcome_keyResp2_allKeys = []
welcome_text.setText('Arrow Alert \n\nWelcome to the Arrow Alert game. In this game, arrows will be quickly flashed on the screen. Your goal is to respond to the direction of the arrows, and to respond as quickly as you can without making mistakes. \n\n\n')
welcome_text2.setText('Arrow Alert \n\nWelcome to the Arrow Alert game. In this game, arrows will be quickly flashed on the screen. Your goal is to respond to the direction of the arrows, and to respond as quickly as you can without making mistakes. \n\nPress the right button to continue\n')
# keep track of which components have finished
welcomeComponents = [welcome_keyResp, welcome_keyResp2, welcome_text, welcome_text2]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_keyResp* updates
    waitOnFlip = False
    if welcome_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_keyResp.frameNStart = frameN  # exact frame index
        welcome_keyResp.tStart = t  # local t and not account for scr refresh
        welcome_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_keyResp, 'tStartRefresh')  # time at next scr refresh
        welcome_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_keyResp.status == STARTED:
        if bool(welcome_keyResp.keys):
            # keep track of stop time/frame for later
            welcome_keyResp.tStop = t  # not accounting for scr refresh
            welcome_keyResp.frameNStop = frameN  # exact frame index
            welcome_keyResp.status = FINISHED
    if welcome_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_keyResp.getKeys(keyList=['c'], waitRelease=False)
        _welcome_keyResp_allKeys.extend(theseKeys)
        if len(_welcome_keyResp_allKeys):
            welcome_keyResp.keys = _welcome_keyResp_allKeys[-1].name  # just the last key pressed
            welcome_keyResp.rt = _welcome_keyResp_allKeys[-1].rt
    
    # *welcome_keyResp2* updates
    if welcome_keyResp2.status == NOT_STARTED and welcome_keyResp.keys:
        # keep track of start time/frame for later
        welcome_keyResp2.frameNStart = frameN  # exact frame index
        welcome_keyResp2.tStart = t  # local t and not account for scr refresh
        welcome_keyResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_keyResp2, 'tStartRefresh')  # time at next scr refresh
        welcome_keyResp2.status = STARTED
        # keyboard checking is just starting
        welcome_keyResp2.clock.reset()  # now t=0
        welcome_keyResp2.clearEvents(eventType='keyboard')
    if welcome_keyResp2.status == STARTED:
        theseKeys = welcome_keyResp2.getKeys(keyList=['8'], waitRelease=False)
        _welcome_keyResp2_allKeys.extend(theseKeys)
        if len(_welcome_keyResp2_allKeys):
            welcome_keyResp2.keys = _welcome_keyResp2_allKeys[-1].name  # just the last key pressed
            welcome_keyResp2.rt = _welcome_keyResp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_text2* updates
    if welcome_text2.status == NOT_STARTED and welcome_keyResp.keys:
        # keep track of start time/frame for later
        welcome_text2.frameNStart = frameN  # exact frame index
        welcome_text2.tStart = t  # local t and not account for scr refresh
        welcome_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_text2.started')
        welcome_text2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructRightSingle" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructRightSingle_keyResp.keys = []
instructRightSingle_keyResp.rt = []
_instructRightSingle_keyResp_allKeys = []
instructRightSingle_keyResp_2.keys = []
instructRightSingle_keyResp_2.rt = []
_instructRightSingle_keyResp_2_allKeys = []
instructRightSingle_keyResp_3.keys = []
instructRightSingle_keyResp_3.rt = []
_instructRightSingle_keyResp_3_allKeys = []
instructRightSingle_keyResp_4.keys = []
instructRightSingle_keyResp_4.rt = []
_instructRightSingle_keyResp_4_allKeys = []
instructRightSingle_keyResp_5.keys = []
instructRightSingle_keyResp_5.rt = []
_instructRightSingle_keyResp_5_allKeys = []
# keep track of which components have finished
instructRightSingleComponents = [instructRightSingle_keyResp, instructRightSingle_keyResp_2, instructRightSingle_keyResp_3, instructRightSingle_keyResp_4, instructRightSingle_keyResp_5, instructRightSingle_text, instructRightSingle_text_2, instructRightSingle_text_3, instructRightSingle_text_4, instructRightSingle_text_5, instructRightSingle_rightArrow, instructRightSingle_rightArrowHighlight, instructRightSingle_rightArrowSolid]
for thisComponent in instructRightSingleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructRightSingle" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructRightSingle_keyResp* updates
    waitOnFlip = False
    if instructRightSingle_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRightSingle_keyResp.frameNStart = frameN  # exact frame index
        instructRightSingle_keyResp.tStart = t  # local t and not account for scr refresh
        instructRightSingle_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_keyResp, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRightSingle_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRightSingle_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRightSingle_keyResp.status == STARTED:
        if bool(instructRightSingle_keyResp.keys):
            # keep track of stop time/frame for later
            instructRightSingle_keyResp.tStop = t  # not accounting for scr refresh
            instructRightSingle_keyResp.frameNStop = frameN  # exact frame index
            instructRightSingle_keyResp.status = FINISHED
    if instructRightSingle_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = instructRightSingle_keyResp.getKeys(keyList=['c'], waitRelease=False)
        _instructRightSingle_keyResp_allKeys.extend(theseKeys)
        if len(_instructRightSingle_keyResp_allKeys):
            instructRightSingle_keyResp.keys = _instructRightSingle_keyResp_allKeys[-1].name  # just the last key pressed
            instructRightSingle_keyResp.rt = _instructRightSingle_keyResp_allKeys[-1].rt
    
    # *instructRightSingle_keyResp_2* updates
    waitOnFlip = False
    if instructRightSingle_keyResp_2.status == NOT_STARTED and instructRightSingle_keyResp.keys:
        # keep track of start time/frame for later
        instructRightSingle_keyResp_2.frameNStart = frameN  # exact frame index
        instructRightSingle_keyResp_2.tStart = t  # local t and not account for scr refresh
        instructRightSingle_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRightSingle_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRightSingle_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRightSingle_keyResp_2.status == STARTED:
        if bool(instructRightSingle_keyResp_2.keys):
            # keep track of stop time/frame for later
            instructRightSingle_keyResp_2.tStop = t  # not accounting for scr refresh
            instructRightSingle_keyResp_2.frameNStop = frameN  # exact frame index
            instructRightSingle_keyResp_2.status = FINISHED
    if instructRightSingle_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = instructRightSingle_keyResp_2.getKeys(keyList=['c'], waitRelease=False)
        _instructRightSingle_keyResp_2_allKeys.extend(theseKeys)
        if len(_instructRightSingle_keyResp_2_allKeys):
            instructRightSingle_keyResp_2.keys = _instructRightSingle_keyResp_2_allKeys[-1].name  # just the last key pressed
            instructRightSingle_keyResp_2.rt = _instructRightSingle_keyResp_2_allKeys[-1].rt
    
    # *instructRightSingle_keyResp_3* updates
    waitOnFlip = False
    if instructRightSingle_keyResp_3.status == NOT_STARTED and instructRightSingle_keyResp_2.keys:
        # keep track of start time/frame for later
        instructRightSingle_keyResp_3.frameNStart = frameN  # exact frame index
        instructRightSingle_keyResp_3.tStart = t  # local t and not account for scr refresh
        instructRightSingle_keyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_keyResp_3, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_keyResp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRightSingle_keyResp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRightSingle_keyResp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRightSingle_keyResp_3.status == STARTED:
        if bool(instructRightSingle_keyResp_3.keys):
            # keep track of stop time/frame for later
            instructRightSingle_keyResp_3.tStop = t  # not accounting for scr refresh
            instructRightSingle_keyResp_3.frameNStop = frameN  # exact frame index
            instructRightSingle_keyResp_3.status = FINISHED
    if instructRightSingle_keyResp_3.status == STARTED and not waitOnFlip:
        theseKeys = instructRightSingle_keyResp_3.getKeys(keyList=['c'], waitRelease=False)
        _instructRightSingle_keyResp_3_allKeys.extend(theseKeys)
        if len(_instructRightSingle_keyResp_3_allKeys):
            instructRightSingle_keyResp_3.keys = _instructRightSingle_keyResp_3_allKeys[-1].name  # just the last key pressed
            instructRightSingle_keyResp_3.rt = _instructRightSingle_keyResp_3_allKeys[-1].rt
    
    # *instructRightSingle_keyResp_4* updates
    waitOnFlip = False
    if instructRightSingle_keyResp_4.status == NOT_STARTED and instructRightSingle_keyResp_3.keys:
        # keep track of start time/frame for later
        instructRightSingle_keyResp_4.frameNStart = frameN  # exact frame index
        instructRightSingle_keyResp_4.tStart = t  # local t and not account for scr refresh
        instructRightSingle_keyResp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_keyResp_4, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_keyResp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRightSingle_keyResp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRightSingle_keyResp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRightSingle_keyResp_4.status == STARTED:
        if bool(instructRightSingle_keyResp_4.keys):
            # keep track of stop time/frame for later
            instructRightSingle_keyResp_4.tStop = t  # not accounting for scr refresh
            instructRightSingle_keyResp_4.frameNStop = frameN  # exact frame index
            instructRightSingle_keyResp_4.status = FINISHED
    if instructRightSingle_keyResp_4.status == STARTED and not waitOnFlip:
        theseKeys = instructRightSingle_keyResp_4.getKeys(keyList=['c'], waitRelease=False)
        _instructRightSingle_keyResp_4_allKeys.extend(theseKeys)
        if len(_instructRightSingle_keyResp_4_allKeys):
            instructRightSingle_keyResp_4.keys = _instructRightSingle_keyResp_4_allKeys[-1].name  # just the last key pressed
            instructRightSingle_keyResp_4.rt = _instructRightSingle_keyResp_4_allKeys[-1].rt
    
    # *instructRightSingle_keyResp_5* updates
    waitOnFlip = False
    if instructRightSingle_keyResp_5.status == NOT_STARTED and instructRightSingle_keyResp_4.keys:
        # keep track of start time/frame for later
        instructRightSingle_keyResp_5.frameNStart = frameN  # exact frame index
        instructRightSingle_keyResp_5.tStart = t  # local t and not account for scr refresh
        instructRightSingle_keyResp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_keyResp_5, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_keyResp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRightSingle_keyResp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRightSingle_keyResp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRightSingle_keyResp_5.status == STARTED:
        if bool(instructRightSingle_keyResp_5.keys):
            # keep track of stop time/frame for later
            instructRightSingle_keyResp_5.tStop = t  # not accounting for scr refresh
            instructRightSingle_keyResp_5.frameNStop = frameN  # exact frame index
            instructRightSingle_keyResp_5.status = FINISHED
    if instructRightSingle_keyResp_5.status == STARTED and not waitOnFlip:
        theseKeys = instructRightSingle_keyResp_5.getKeys(keyList=['8'], waitRelease=False)
        _instructRightSingle_keyResp_5_allKeys.extend(theseKeys)
        if len(_instructRightSingle_keyResp_5_allKeys):
            instructRightSingle_keyResp_5.keys = _instructRightSingle_keyResp_5_allKeys[-1].name  # just the last key pressed
            instructRightSingle_keyResp_5.rt = _instructRightSingle_keyResp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructRightSingle_text* updates
    if instructRightSingle_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRightSingle_text.frameNStart = frameN  # exact frame index
        instructRightSingle_text.tStart = t  # local t and not account for scr refresh
        instructRightSingle_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_text, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_text.setAutoDraw(True)
    
    # *instructRightSingle_text_2* updates
    if instructRightSingle_text_2.status == NOT_STARTED and instructRightSingle_keyResp.keys:
        # keep track of start time/frame for later
        instructRightSingle_text_2.frameNStart = frameN  # exact frame index
        instructRightSingle_text_2.tStart = t  # local t and not account for scr refresh
        instructRightSingle_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_text_2, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_text_2.setAutoDraw(True)
    
    # *instructRightSingle_text_3* updates
    if instructRightSingle_text_3.status == NOT_STARTED and instructRightSingle_keyResp_2.keys:
        # keep track of start time/frame for later
        instructRightSingle_text_3.frameNStart = frameN  # exact frame index
        instructRightSingle_text_3.tStart = t  # local t and not account for scr refresh
        instructRightSingle_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_text_3, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_text_3.setAutoDraw(True)
    
    # *instructRightSingle_text_4* updates
    if instructRightSingle_text_4.status == NOT_STARTED and instructRightSingle_keyResp_3.keys:
        # keep track of start time/frame for later
        instructRightSingle_text_4.frameNStart = frameN  # exact frame index
        instructRightSingle_text_4.tStart = t  # local t and not account for scr refresh
        instructRightSingle_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_text_4, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_text_4.setAutoDraw(True)
    
    # *instructRightSingle_text_5* updates
    if instructRightSingle_text_5.status == NOT_STARTED and instructRightSingle_keyResp_4.keys:
        # keep track of start time/frame for later
        instructRightSingle_text_5.frameNStart = frameN  # exact frame index
        instructRightSingle_text_5.tStart = t  # local t and not account for scr refresh
        instructRightSingle_text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_text_5, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_text_5.setAutoDraw(True)
    
    # *instructRightSingle_rightArrow* updates
    if instructRightSingle_rightArrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRightSingle_rightArrow.frameNStart = frameN  # exact frame index
        instructRightSingle_rightArrow.tStart = t  # local t and not account for scr refresh
        instructRightSingle_rightArrow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_rightArrow, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_rightArrow.setAutoDraw(True)
    
    # *instructRightSingle_rightArrowHighlight* updates
    if instructRightSingle_rightArrowHighlight.status == NOT_STARTED and instructRightSingle_keyResp.keys:
        # keep track of start time/frame for later
        instructRightSingle_rightArrowHighlight.frameNStart = frameN  # exact frame index
        instructRightSingle_rightArrowHighlight.tStart = t  # local t and not account for scr refresh
        instructRightSingle_rightArrowHighlight.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_rightArrowHighlight, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_rightArrowHighlight.setAutoDraw(True)
    
    # *instructRightSingle_rightArrowSolid* updates
    if instructRightSingle_rightArrowSolid.status == NOT_STARTED and instructRightSingle_keyResp_2.keys:
        # keep track of start time/frame for later
        instructRightSingle_rightArrowSolid.frameNStart = frameN  # exact frame index
        instructRightSingle_rightArrowSolid.tStart = t  # local t and not account for scr refresh
        instructRightSingle_rightArrowSolid.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRightSingle_rightArrowSolid, 'tStartRefresh')  # time at next scr refresh
        instructRightSingle_rightArrowSolid.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructRightSingleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructRightSingle" ---
for thisComponent in instructRightSingleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructRightSingle" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructLeftSingle" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructLeftSingle_keyResp.keys = []
instructLeftSingle_keyResp.rt = []
_instructLeftSingle_keyResp_allKeys = []
instructLeftSingle_keyResp_2.keys = []
instructLeftSingle_keyResp_2.rt = []
_instructLeftSingle_keyResp_2_allKeys = []
instructLeftSingle_keyResp_3.keys = []
instructLeftSingle_keyResp_3.rt = []
_instructLeftSingle_keyResp_3_allKeys = []
instructLeftSingle_keyResp_4.keys = []
instructLeftSingle_keyResp_4.rt = []
_instructLeftSingle_keyResp_4_allKeys = []
instructLeftSingle_keyResp_5.keys = []
instructLeftSingle_keyResp_5.rt = []
_instructLeftSingle_keyResp_5_allKeys = []
# keep track of which components have finished
instructLeftSingleComponents = [instructLeftSingle_keyResp, instructLeftSingle_keyResp_2, instructLeftSingle_keyResp_3, instructLeftSingle_keyResp_4, instructLeftSingle_keyResp_5, instructLeftSingle_text, instructLeftSingle_text_2, instructLeftSingle_text_3, instructLeftSingle_text_4, instructLeftSingle_text_5, instructLeftSingle_leftArrow, instructLeftSingle_leftArrowHighlight, instructLeftSingle_leftArrowSolid]
for thisComponent in instructLeftSingleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructLeftSingle" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructLeftSingle_keyResp* updates
    waitOnFlip = False
    if instructLeftSingle_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeftSingle_keyResp.frameNStart = frameN  # exact frame index
        instructLeftSingle_keyResp.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_keyResp, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeftSingle_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeftSingle_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeftSingle_keyResp.status == STARTED:
        if bool(instructLeftSingle_keyResp.keys):
            # keep track of stop time/frame for later
            instructLeftSingle_keyResp.tStop = t  # not accounting for scr refresh
            instructLeftSingle_keyResp.frameNStop = frameN  # exact frame index
            instructLeftSingle_keyResp.status = FINISHED
    if instructLeftSingle_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = instructLeftSingle_keyResp.getKeys(keyList=['c'], waitRelease=False)
        _instructLeftSingle_keyResp_allKeys.extend(theseKeys)
        if len(_instructLeftSingle_keyResp_allKeys):
            instructLeftSingle_keyResp.keys = _instructLeftSingle_keyResp_allKeys[-1].name  # just the last key pressed
            instructLeftSingle_keyResp.rt = _instructLeftSingle_keyResp_allKeys[-1].rt
    
    # *instructLeftSingle_keyResp_2* updates
    waitOnFlip = False
    if instructLeftSingle_keyResp_2.status == NOT_STARTED and instructLeftSingle_keyResp.keys:
        # keep track of start time/frame for later
        instructLeftSingle_keyResp_2.frameNStart = frameN  # exact frame index
        instructLeftSingle_keyResp_2.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeftSingle_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeftSingle_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeftSingle_keyResp_2.status == STARTED:
        if bool(instructLeftSingle_keyResp_2.keys):
            # keep track of stop time/frame for later
            instructLeftSingle_keyResp_2.tStop = t  # not accounting for scr refresh
            instructLeftSingle_keyResp_2.frameNStop = frameN  # exact frame index
            instructLeftSingle_keyResp_2.status = FINISHED
    if instructLeftSingle_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = instructLeftSingle_keyResp_2.getKeys(keyList=['c'], waitRelease=False)
        _instructLeftSingle_keyResp_2_allKeys.extend(theseKeys)
        if len(_instructLeftSingle_keyResp_2_allKeys):
            instructLeftSingle_keyResp_2.keys = _instructLeftSingle_keyResp_2_allKeys[-1].name  # just the last key pressed
            instructLeftSingle_keyResp_2.rt = _instructLeftSingle_keyResp_2_allKeys[-1].rt
    
    # *instructLeftSingle_keyResp_3* updates
    waitOnFlip = False
    if instructLeftSingle_keyResp_3.status == NOT_STARTED and instructLeftSingle_keyResp_2.keys:
        # keep track of start time/frame for later
        instructLeftSingle_keyResp_3.frameNStart = frameN  # exact frame index
        instructLeftSingle_keyResp_3.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_keyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_keyResp_3, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_keyResp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeftSingle_keyResp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeftSingle_keyResp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeftSingle_keyResp_3.status == STARTED:
        if bool(instructLeftSingle_keyResp_3.keys):
            # keep track of stop time/frame for later
            instructLeftSingle_keyResp_3.tStop = t  # not accounting for scr refresh
            instructLeftSingle_keyResp_3.frameNStop = frameN  # exact frame index
            instructLeftSingle_keyResp_3.status = FINISHED
    if instructLeftSingle_keyResp_3.status == STARTED and not waitOnFlip:
        theseKeys = instructLeftSingle_keyResp_3.getKeys(keyList=['c'], waitRelease=False)
        _instructLeftSingle_keyResp_3_allKeys.extend(theseKeys)
        if len(_instructLeftSingle_keyResp_3_allKeys):
            instructLeftSingle_keyResp_3.keys = _instructLeftSingle_keyResp_3_allKeys[-1].name  # just the last key pressed
            instructLeftSingle_keyResp_3.rt = _instructLeftSingle_keyResp_3_allKeys[-1].rt
    
    # *instructLeftSingle_keyResp_4* updates
    waitOnFlip = False
    if instructLeftSingle_keyResp_4.status == NOT_STARTED and instructLeftSingle_keyResp_3.keys:
        # keep track of start time/frame for later
        instructLeftSingle_keyResp_4.frameNStart = frameN  # exact frame index
        instructLeftSingle_keyResp_4.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_keyResp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_keyResp_4, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_keyResp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeftSingle_keyResp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeftSingle_keyResp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeftSingle_keyResp_4.status == STARTED:
        if bool(instructLeftSingle_keyResp_4.keys):
            # keep track of stop time/frame for later
            instructLeftSingle_keyResp_4.tStop = t  # not accounting for scr refresh
            instructLeftSingle_keyResp_4.frameNStop = frameN  # exact frame index
            instructLeftSingle_keyResp_4.status = FINISHED
    if instructLeftSingle_keyResp_4.status == STARTED and not waitOnFlip:
        theseKeys = instructLeftSingle_keyResp_4.getKeys(keyList=['c'], waitRelease=False)
        _instructLeftSingle_keyResp_4_allKeys.extend(theseKeys)
        if len(_instructLeftSingle_keyResp_4_allKeys):
            instructLeftSingle_keyResp_4.keys = _instructLeftSingle_keyResp_4_allKeys[-1].name  # just the last key pressed
            instructLeftSingle_keyResp_4.rt = _instructLeftSingle_keyResp_4_allKeys[-1].rt
    
    # *instructLeftSingle_keyResp_5* updates
    waitOnFlip = False
    if instructLeftSingle_keyResp_5.status == NOT_STARTED and instructLeftSingle_keyResp_4.keys:
        # keep track of start time/frame for later
        instructLeftSingle_keyResp_5.frameNStart = frameN  # exact frame index
        instructLeftSingle_keyResp_5.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_keyResp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_keyResp_5, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_keyResp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeftSingle_keyResp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeftSingle_keyResp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeftSingle_keyResp_5.status == STARTED:
        if bool(instructLeftSingle_keyResp_5.keys):
            # keep track of stop time/frame for later
            instructLeftSingle_keyResp_5.tStop = t  # not accounting for scr refresh
            instructLeftSingle_keyResp_5.frameNStop = frameN  # exact frame index
            instructLeftSingle_keyResp_5.status = FINISHED
    if instructLeftSingle_keyResp_5.status == STARTED and not waitOnFlip:
        theseKeys = instructLeftSingle_keyResp_5.getKeys(keyList=['1'], waitRelease=False)
        _instructLeftSingle_keyResp_5_allKeys.extend(theseKeys)
        if len(_instructLeftSingle_keyResp_5_allKeys):
            instructLeftSingle_keyResp_5.keys = _instructLeftSingle_keyResp_5_allKeys[-1].name  # just the last key pressed
            instructLeftSingle_keyResp_5.rt = _instructLeftSingle_keyResp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructLeftSingle_text* updates
    if instructLeftSingle_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeftSingle_text.frameNStart = frameN  # exact frame index
        instructLeftSingle_text.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_text, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_text.setAutoDraw(True)
    
    # *instructLeftSingle_text_2* updates
    if instructLeftSingle_text_2.status == NOT_STARTED and instructLeftSingle_keyResp.keys:
        # keep track of start time/frame for later
        instructLeftSingle_text_2.frameNStart = frameN  # exact frame index
        instructLeftSingle_text_2.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_text_2, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_text_2.setAutoDraw(True)
    
    # *instructLeftSingle_text_3* updates
    if instructLeftSingle_text_3.status == NOT_STARTED and instructLeftSingle_keyResp_2.keys:
        # keep track of start time/frame for later
        instructLeftSingle_text_3.frameNStart = frameN  # exact frame index
        instructLeftSingle_text_3.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_text_3, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_text_3.setAutoDraw(True)
    
    # *instructLeftSingle_text_4* updates
    if instructLeftSingle_text_4.status == NOT_STARTED and instructLeftSingle_keyResp_3.keys:
        # keep track of start time/frame for later
        instructLeftSingle_text_4.frameNStart = frameN  # exact frame index
        instructLeftSingle_text_4.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_text_4, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_text_4.setAutoDraw(True)
    
    # *instructLeftSingle_text_5* updates
    if instructLeftSingle_text_5.status == NOT_STARTED and instructLeftSingle_keyResp_4.keys:
        # keep track of start time/frame for later
        instructLeftSingle_text_5.frameNStart = frameN  # exact frame index
        instructLeftSingle_text_5.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_text_5, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_text_5.setAutoDraw(True)
    
    # *instructLeftSingle_leftArrow* updates
    if instructLeftSingle_leftArrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeftSingle_leftArrow.frameNStart = frameN  # exact frame index
        instructLeftSingle_leftArrow.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_leftArrow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_leftArrow, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_leftArrow.setAutoDraw(True)
    
    # *instructLeftSingle_leftArrowHighlight* updates
    if instructLeftSingle_leftArrowHighlight.status == NOT_STARTED and instructLeftSingle_keyResp.keys:
        # keep track of start time/frame for later
        instructLeftSingle_leftArrowHighlight.frameNStart = frameN  # exact frame index
        instructLeftSingle_leftArrowHighlight.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_leftArrowHighlight.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_leftArrowHighlight, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_leftArrowHighlight.setAutoDraw(True)
    
    # *instructLeftSingle_leftArrowSolid* updates
    if instructLeftSingle_leftArrowSolid.status == NOT_STARTED and instructLeftSingle_keyResp_2.keys:
        # keep track of start time/frame for later
        instructLeftSingle_leftArrowSolid.frameNStart = frameN  # exact frame index
        instructLeftSingle_leftArrowSolid.tStart = t  # local t and not account for scr refresh
        instructLeftSingle_leftArrowSolid.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeftSingle_leftArrowSolid, 'tStartRefresh')  # time at next scr refresh
        instructLeftSingle_leftArrowSolid.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructLeftSingleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructLeftSingle" ---
for thisComponent in instructLeftSingleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructLeftSingle" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructMiddle" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructMiddle_keyResp.keys = []
instructMiddle_keyResp.rt = []
_instructMiddle_keyResp_allKeys = []
instructMiddle_keyResp2.keys = []
instructMiddle_keyResp2.rt = []
_instructMiddle_keyResp2_allKeys = []
welcome_text_2.setText('During the game, five arrows will appear at a time. They will be quickly flashed on the screen. Your goal is to respond to the MIDDLE arrow, and to respond as quickly as you can without making mistakes. \n\nIf the MIDDLE arrow is pointing to the right, use your right hand to press the right button. If the MIDDLE arrow is pointing to the left, use your left hand to press the left button. \n\n\n')
welcome_text2_2.setText('During the game, five arrows will appear at a time. They will be quickly flashed on the screen. Your goal is to respond to the MIDDLE arrow, and to respond as quickly as you can without making mistakes. \n\nIf the MIDDLE arrow is pointing to the right, use your right hand to press the right button. If the MIDDLE arrow is pointing to the left, use your left hand to press the left button. \n\nPress the right button to continue\n')
# keep track of which components have finished
instructMiddleComponents = [instructMiddle_keyResp, instructMiddle_keyResp2, welcome_text_2, welcome_text2_2]
for thisComponent in instructMiddleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructMiddle" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructMiddle_keyResp* updates
    waitOnFlip = False
    if instructMiddle_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructMiddle_keyResp.frameNStart = frameN  # exact frame index
        instructMiddle_keyResp.tStart = t  # local t and not account for scr refresh
        instructMiddle_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructMiddle_keyResp, 'tStartRefresh')  # time at next scr refresh
        instructMiddle_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructMiddle_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructMiddle_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructMiddle_keyResp.status == STARTED:
        if bool(instructMiddle_keyResp.keys):
            # keep track of stop time/frame for later
            instructMiddle_keyResp.tStop = t  # not accounting for scr refresh
            instructMiddle_keyResp.frameNStop = frameN  # exact frame index
            instructMiddle_keyResp.status = FINISHED
    if instructMiddle_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = instructMiddle_keyResp.getKeys(keyList=['c'], waitRelease=False)
        _instructMiddle_keyResp_allKeys.extend(theseKeys)
        if len(_instructMiddle_keyResp_allKeys):
            instructMiddle_keyResp.keys = _instructMiddle_keyResp_allKeys[-1].name  # just the last key pressed
            instructMiddle_keyResp.rt = _instructMiddle_keyResp_allKeys[-1].rt
    
    # *instructMiddle_keyResp2* updates
    if instructMiddle_keyResp2.status == NOT_STARTED and instructMiddle_keyResp.keys:
        # keep track of start time/frame for later
        instructMiddle_keyResp2.frameNStart = frameN  # exact frame index
        instructMiddle_keyResp2.tStart = t  # local t and not account for scr refresh
        instructMiddle_keyResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructMiddle_keyResp2, 'tStartRefresh')  # time at next scr refresh
        instructMiddle_keyResp2.status = STARTED
        # keyboard checking is just starting
        instructMiddle_keyResp2.clock.reset()  # now t=0
        instructMiddle_keyResp2.clearEvents(eventType='keyboard')
    if instructMiddle_keyResp2.status == STARTED:
        theseKeys = instructMiddle_keyResp2.getKeys(keyList=['8'], waitRelease=False)
        _instructMiddle_keyResp2_allKeys.extend(theseKeys)
        if len(_instructMiddle_keyResp2_allKeys):
            instructMiddle_keyResp2.keys = _instructMiddle_keyResp2_allKeys[-1].name  # just the last key pressed
            instructMiddle_keyResp2.rt = _instructMiddle_keyResp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *welcome_text_2* updates
    if welcome_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text_2.frameNStart = frameN  # exact frame index
        welcome_text_2.tStart = t  # local t and not account for scr refresh
        welcome_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text_2, 'tStartRefresh')  # time at next scr refresh
        welcome_text_2.setAutoDraw(True)
    
    # *welcome_text2_2* updates
    if welcome_text2_2.status == NOT_STARTED and instructMiddle_keyResp.keys:
        # keep track of start time/frame for later
        welcome_text2_2.frameNStart = frameN  # exact frame index
        welcome_text2_2.tStart = t  # local t and not account for scr refresh
        welcome_text2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_text2_2.started')
        welcome_text2_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructMiddleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructMiddle" ---
for thisComponent in instructMiddleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructMiddle" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructRight" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
insructRight_keyResp.keys = []
insructRight_keyResp.rt = []
_insructRight_keyResp_allKeys = []
# keep track of which components have finished
instructRightComponents = [instructRight_text, instructRight_centerImg, instructRight_rightImg1, instructRight_rightImg2, instructRight_leftImg1, instructRight_leftImg2, insructRight_keyResp]
for thisComponent in instructRightComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructRight" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructRight_text* updates
    if instructRight_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_text.frameNStart = frameN  # exact frame index
        instructRight_text.tStart = t  # local t and not account for scr refresh
        instructRight_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_text, 'tStartRefresh')  # time at next scr refresh
        instructRight_text.setAutoDraw(True)
    
    # *instructRight_centerImg* updates
    if instructRight_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_centerImg.frameNStart = frameN  # exact frame index
        instructRight_centerImg.tStart = t  # local t and not account for scr refresh
        instructRight_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_centerImg, 'tStartRefresh')  # time at next scr refresh
        instructRight_centerImg.setAutoDraw(True)
    
    # *instructRight_rightImg1* updates
    if instructRight_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_rightImg1.frameNStart = frameN  # exact frame index
        instructRight_rightImg1.tStart = t  # local t and not account for scr refresh
        instructRight_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_rightImg1, 'tStartRefresh')  # time at next scr refresh
        instructRight_rightImg1.setAutoDraw(True)
    
    # *instructRight_rightImg2* updates
    if instructRight_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_rightImg2.frameNStart = frameN  # exact frame index
        instructRight_rightImg2.tStart = t  # local t and not account for scr refresh
        instructRight_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_rightImg2, 'tStartRefresh')  # time at next scr refresh
        instructRight_rightImg2.setAutoDraw(True)
    
    # *instructRight_leftImg1* updates
    if instructRight_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_leftImg1.frameNStart = frameN  # exact frame index
        instructRight_leftImg1.tStart = t  # local t and not account for scr refresh
        instructRight_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_leftImg1, 'tStartRefresh')  # time at next scr refresh
        instructRight_leftImg1.setAutoDraw(True)
    
    # *instructRight_leftImg2* updates
    if instructRight_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_leftImg2.frameNStart = frameN  # exact frame index
        instructRight_leftImg2.tStart = t  # local t and not account for scr refresh
        instructRight_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_leftImg2, 'tStartRefresh')  # time at next scr refresh
        instructRight_leftImg2.setAutoDraw(True)
    
    # *insructRight_keyResp* updates
    waitOnFlip = False
    if insructRight_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insructRight_keyResp.frameNStart = frameN  # exact frame index
        insructRight_keyResp.tStart = t  # local t and not account for scr refresh
        insructRight_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructRight_keyResp, 'tStartRefresh')  # time at next scr refresh
        insructRight_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructRight_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructRight_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructRight_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = insructRight_keyResp.getKeys(keyList=['c'], waitRelease=False)
        _insructRight_keyResp_allKeys.extend(theseKeys)
        if len(_insructRight_keyResp_allKeys):
            insructRight_keyResp.keys = _insructRight_keyResp_allKeys[-1].name  # just the last key pressed
            insructRight_keyResp.rt = _insructRight_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructRight" ---
for thisComponent in instructRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructRight_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
insructRight_keyResp_2.keys = []
insructRight_keyResp_2.rt = []
_insructRight_keyResp_2_allKeys = []
# keep track of which components have finished
instructRight_2Components = [instructRight_text_2, instructRight_centerImg_2, instructRight_rightImg1_2, instructRight_rightImg2_2, instructRight_leftImg1_2, instructRight_leftImg2_2, insructRight_keyResp_2]
for thisComponent in instructRight_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructRight_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructRight_text_2* updates
    if instructRight_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_text_2.frameNStart = frameN  # exact frame index
        instructRight_text_2.tStart = t  # local t and not account for scr refresh
        instructRight_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_text_2, 'tStartRefresh')  # time at next scr refresh
        instructRight_text_2.setAutoDraw(True)
    
    # *instructRight_centerImg_2* updates
    if instructRight_centerImg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_centerImg_2.frameNStart = frameN  # exact frame index
        instructRight_centerImg_2.tStart = t  # local t and not account for scr refresh
        instructRight_centerImg_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_centerImg_2, 'tStartRefresh')  # time at next scr refresh
        instructRight_centerImg_2.setAutoDraw(True)
    
    # *instructRight_rightImg1_2* updates
    if instructRight_rightImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_rightImg1_2.frameNStart = frameN  # exact frame index
        instructRight_rightImg1_2.tStart = t  # local t and not account for scr refresh
        instructRight_rightImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_rightImg1_2, 'tStartRefresh')  # time at next scr refresh
        instructRight_rightImg1_2.setAutoDraw(True)
    
    # *instructRight_rightImg2_2* updates
    if instructRight_rightImg2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_rightImg2_2.frameNStart = frameN  # exact frame index
        instructRight_rightImg2_2.tStart = t  # local t and not account for scr refresh
        instructRight_rightImg2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_rightImg2_2, 'tStartRefresh')  # time at next scr refresh
        instructRight_rightImg2_2.setAutoDraw(True)
    
    # *instructRight_leftImg1_2* updates
    if instructRight_leftImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_leftImg1_2.frameNStart = frameN  # exact frame index
        instructRight_leftImg1_2.tStart = t  # local t and not account for scr refresh
        instructRight_leftImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_leftImg1_2, 'tStartRefresh')  # time at next scr refresh
        instructRight_leftImg1_2.setAutoDraw(True)
    
    # *instructRight_leftImg2_2* updates
    if instructRight_leftImg2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_leftImg2_2.frameNStart = frameN  # exact frame index
        instructRight_leftImg2_2.tStart = t  # local t and not account for scr refresh
        instructRight_leftImg2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_leftImg2_2, 'tStartRefresh')  # time at next scr refresh
        instructRight_leftImg2_2.setAutoDraw(True)
    
    # *insructRight_keyResp_2* updates
    waitOnFlip = False
    if insructRight_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insructRight_keyResp_2.frameNStart = frameN  # exact frame index
        insructRight_keyResp_2.tStart = t  # local t and not account for scr refresh
        insructRight_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructRight_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        insructRight_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructRight_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructRight_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructRight_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = insructRight_keyResp_2.getKeys(keyList=['8'], waitRelease=False)
        _insructRight_keyResp_2_allKeys.extend(theseKeys)
        if len(_insructRight_keyResp_2_allKeys):
            insructRight_keyResp_2.keys = _insructRight_keyResp_2_allKeys[-1].name  # just the last key pressed
            insructRight_keyResp_2.rt = _insructRight_keyResp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructRight_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructRight_2" ---
for thisComponent in instructRight_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructRight_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructLeft" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructLeft_keyResp.keys = []
instructLeft_keyResp.rt = []
_instructLeft_keyResp_allKeys = []
# keep track of which components have finished
instructLeftComponents = [instructLeft_text, instructLeft_centerImg, instructLeft_rightImg1, instructLeft_rightImg2, instructLeft_leftImg1, instructLeft_leftImg2, instructLeft_keyResp]
for thisComponent in instructLeftComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructLeft" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructLeft_text* updates
    if instructLeft_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_text.frameNStart = frameN  # exact frame index
        instructLeft_text.tStart = t  # local t and not account for scr refresh
        instructLeft_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_text, 'tStartRefresh')  # time at next scr refresh
        instructLeft_text.setAutoDraw(True)
    
    # *instructLeft_centerImg* updates
    if instructLeft_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_centerImg.frameNStart = frameN  # exact frame index
        instructLeft_centerImg.tStart = t  # local t and not account for scr refresh
        instructLeft_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_centerImg, 'tStartRefresh')  # time at next scr refresh
        instructLeft_centerImg.setAutoDraw(True)
    
    # *instructLeft_rightImg1* updates
    if instructLeft_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_rightImg1.frameNStart = frameN  # exact frame index
        instructLeft_rightImg1.tStart = t  # local t and not account for scr refresh
        instructLeft_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_rightImg1, 'tStartRefresh')  # time at next scr refresh
        instructLeft_rightImg1.setAutoDraw(True)
    
    # *instructLeft_rightImg2* updates
    if instructLeft_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_rightImg2.frameNStart = frameN  # exact frame index
        instructLeft_rightImg2.tStart = t  # local t and not account for scr refresh
        instructLeft_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_rightImg2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_rightImg2.setAutoDraw(True)
    
    # *instructLeft_leftImg1* updates
    if instructLeft_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_leftImg1.frameNStart = frameN  # exact frame index
        instructLeft_leftImg1.tStart = t  # local t and not account for scr refresh
        instructLeft_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_leftImg1, 'tStartRefresh')  # time at next scr refresh
        instructLeft_leftImg1.setAutoDraw(True)
    
    # *instructLeft_leftImg2* updates
    if instructLeft_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_leftImg2.frameNStart = frameN  # exact frame index
        instructLeft_leftImg2.tStart = t  # local t and not account for scr refresh
        instructLeft_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_leftImg2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_leftImg2.setAutoDraw(True)
    
    # *instructLeft_keyResp* updates
    waitOnFlip = False
    if instructLeft_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_keyResp.frameNStart = frameN  # exact frame index
        instructLeft_keyResp.tStart = t  # local t and not account for scr refresh
        instructLeft_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_keyResp, 'tStartRefresh')  # time at next scr refresh
        instructLeft_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeft_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeft_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeft_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = instructLeft_keyResp.getKeys(keyList=['c'], waitRelease=False)
        _instructLeft_keyResp_allKeys.extend(theseKeys)
        if len(_instructLeft_keyResp_allKeys):
            instructLeft_keyResp.keys = _instructLeft_keyResp_allKeys[-1].name  # just the last key pressed
            instructLeft_keyResp.rt = _instructLeft_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructLeft" ---
for thisComponent in instructLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructLeft_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructLeft_keyResp_2.keys = []
instructLeft_keyResp_2.rt = []
_instructLeft_keyResp_2_allKeys = []
# keep track of which components have finished
instructLeft_2Components = [instructLeft_text_2, instructLeft_centerImg_2, instructLeft_rightImg1_2, instructLeft_rightImg2_2, instructLeft_leftImg1_2, instructLeft_leftImg2_2, instructLeft_keyResp_2]
for thisComponent in instructLeft_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructLeft_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructLeft_text_2* updates
    if instructLeft_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_text_2.frameNStart = frameN  # exact frame index
        instructLeft_text_2.tStart = t  # local t and not account for scr refresh
        instructLeft_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_text_2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_text_2.setAutoDraw(True)
    
    # *instructLeft_centerImg_2* updates
    if instructLeft_centerImg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_centerImg_2.frameNStart = frameN  # exact frame index
        instructLeft_centerImg_2.tStart = t  # local t and not account for scr refresh
        instructLeft_centerImg_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_centerImg_2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_centerImg_2.setAutoDraw(True)
    
    # *instructLeft_rightImg1_2* updates
    if instructLeft_rightImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_rightImg1_2.frameNStart = frameN  # exact frame index
        instructLeft_rightImg1_2.tStart = t  # local t and not account for scr refresh
        instructLeft_rightImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_rightImg1_2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_rightImg1_2.setAutoDraw(True)
    
    # *instructLeft_rightImg2_2* updates
    if instructLeft_rightImg2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_rightImg2_2.frameNStart = frameN  # exact frame index
        instructLeft_rightImg2_2.tStart = t  # local t and not account for scr refresh
        instructLeft_rightImg2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_rightImg2_2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_rightImg2_2.setAutoDraw(True)
    
    # *instructLeft_leftImg1_2* updates
    if instructLeft_leftImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_leftImg1_2.frameNStart = frameN  # exact frame index
        instructLeft_leftImg1_2.tStart = t  # local t and not account for scr refresh
        instructLeft_leftImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_leftImg1_2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_leftImg1_2.setAutoDraw(True)
    
    # *instructLeft_leftImg2_2* updates
    if instructLeft_leftImg2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_leftImg2_2.frameNStart = frameN  # exact frame index
        instructLeft_leftImg2_2.tStart = t  # local t and not account for scr refresh
        instructLeft_leftImg2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_leftImg2_2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_leftImg2_2.setAutoDraw(True)
    
    # *instructLeft_keyResp_2* updates
    waitOnFlip = False
    if instructLeft_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_keyResp_2.frameNStart = frameN  # exact frame index
        instructLeft_keyResp_2.tStart = t  # local t and not account for scr refresh
        instructLeft_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeft_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeft_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeft_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = instructLeft_keyResp_2.getKeys(keyList=['1'], waitRelease=False)
        _instructLeft_keyResp_2_allKeys.extend(theseKeys)
        if len(_instructLeft_keyResp_2_allKeys):
            instructLeft_keyResp_2.keys = _instructLeft_keyResp_2_allKeys[-1].name  # just the last key pressed
            instructLeft_keyResp_2.rt = _instructLeft_keyResp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructLeft_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructLeft_2" ---
for thisComponent in instructLeft_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructLeft_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructInconRight" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
insructInconRight_keyResp.keys = []
insructInconRight_keyResp.rt = []
_insructInconRight_keyResp_allKeys = []
# keep track of which components have finished
instructInconRightComponents = [instructInconRight_text, instructIncon_centerImg, instructIncon_rightImg1, instructIncon_rightImg2, instructIncon_leftImg1, instructInconRight_leftImg2, insructInconRight_keyResp]
for thisComponent in instructInconRightComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructInconRight" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconRight_text* updates
    if instructInconRight_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconRight_text.frameNStart = frameN  # exact frame index
        instructInconRight_text.tStart = t  # local t and not account for scr refresh
        instructInconRight_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_text, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_text.setAutoDraw(True)
    
    # *instructIncon_centerImg* updates
    if instructIncon_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_centerImg.frameNStart = frameN  # exact frame index
        instructIncon_centerImg.tStart = t  # local t and not account for scr refresh
        instructIncon_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_centerImg, 'tStartRefresh')  # time at next scr refresh
        instructIncon_centerImg.setAutoDraw(True)
    
    # *instructIncon_rightImg1* updates
    if instructIncon_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_rightImg1.frameNStart = frameN  # exact frame index
        instructIncon_rightImg1.tStart = t  # local t and not account for scr refresh
        instructIncon_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_rightImg1, 'tStartRefresh')  # time at next scr refresh
        instructIncon_rightImg1.setAutoDraw(True)
    
    # *instructIncon_rightImg2* updates
    if instructIncon_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_rightImg2.frameNStart = frameN  # exact frame index
        instructIncon_rightImg2.tStart = t  # local t and not account for scr refresh
        instructIncon_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_rightImg2, 'tStartRefresh')  # time at next scr refresh
        instructIncon_rightImg2.setAutoDraw(True)
    
    # *instructIncon_leftImg1* updates
    if instructIncon_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_leftImg1.frameNStart = frameN  # exact frame index
        instructIncon_leftImg1.tStart = t  # local t and not account for scr refresh
        instructIncon_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_leftImg1, 'tStartRefresh')  # time at next scr refresh
        instructIncon_leftImg1.setAutoDraw(True)
    
    # *instructInconRight_leftImg2* updates
    if instructInconRight_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconRight_leftImg2.frameNStart = frameN  # exact frame index
        instructInconRight_leftImg2.tStart = t  # local t and not account for scr refresh
        instructInconRight_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_leftImg2, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_leftImg2.setAutoDraw(True)
    
    # *insructInconRight_keyResp* updates
    waitOnFlip = False
    if insructInconRight_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insructInconRight_keyResp.frameNStart = frameN  # exact frame index
        insructInconRight_keyResp.tStart = t  # local t and not account for scr refresh
        insructInconRight_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructInconRight_keyResp, 'tStartRefresh')  # time at next scr refresh
        insructInconRight_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructInconRight_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructInconRight_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructInconRight_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = insructInconRight_keyResp.getKeys(keyList=['c'], waitRelease=False)
        _insructInconRight_keyResp_allKeys.extend(theseKeys)
        if len(_insructInconRight_keyResp_allKeys):
            insructInconRight_keyResp.keys = _insructInconRight_keyResp_allKeys[-1].name  # just the last key pressed
            insructInconRight_keyResp.rt = _insructInconRight_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructInconRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructInconRight" ---
for thisComponent in instructInconRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructInconRight_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
insructInconRight_keyResp_2.keys = []
insructInconRight_keyResp_2.rt = []
_insructInconRight_keyResp_2_allKeys = []
# keep track of which components have finished
instructInconRight_2Components = [instructInconRight_text_2, instructIncon_centerImg_2, instructIncon_rightImg1_2, instructIncon_rightImg2_2, instructIncon_leftImg1_2, instructInconRight_leftImg2_2, insructInconRight_keyResp_2]
for thisComponent in instructInconRight_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructInconRight_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconRight_text_2* updates
    if instructInconRight_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconRight_text_2.frameNStart = frameN  # exact frame index
        instructInconRight_text_2.tStart = t  # local t and not account for scr refresh
        instructInconRight_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_text_2, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_text_2.setAutoDraw(True)
    
    # *instructIncon_centerImg_2* updates
    if instructIncon_centerImg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_centerImg_2.frameNStart = frameN  # exact frame index
        instructIncon_centerImg_2.tStart = t  # local t and not account for scr refresh
        instructIncon_centerImg_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_centerImg_2, 'tStartRefresh')  # time at next scr refresh
        instructIncon_centerImg_2.setAutoDraw(True)
    
    # *instructIncon_rightImg1_2* updates
    if instructIncon_rightImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_rightImg1_2.frameNStart = frameN  # exact frame index
        instructIncon_rightImg1_2.tStart = t  # local t and not account for scr refresh
        instructIncon_rightImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_rightImg1_2, 'tStartRefresh')  # time at next scr refresh
        instructIncon_rightImg1_2.setAutoDraw(True)
    
    # *instructIncon_rightImg2_2* updates
    if instructIncon_rightImg2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_rightImg2_2.frameNStart = frameN  # exact frame index
        instructIncon_rightImg2_2.tStart = t  # local t and not account for scr refresh
        instructIncon_rightImg2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_rightImg2_2, 'tStartRefresh')  # time at next scr refresh
        instructIncon_rightImg2_2.setAutoDraw(True)
    
    # *instructIncon_leftImg1_2* updates
    if instructIncon_leftImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructIncon_leftImg1_2.frameNStart = frameN  # exact frame index
        instructIncon_leftImg1_2.tStart = t  # local t and not account for scr refresh
        instructIncon_leftImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructIncon_leftImg1_2, 'tStartRefresh')  # time at next scr refresh
        instructIncon_leftImg1_2.setAutoDraw(True)
    
    # *instructInconRight_leftImg2_2* updates
    if instructInconRight_leftImg2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconRight_leftImg2_2.frameNStart = frameN  # exact frame index
        instructInconRight_leftImg2_2.tStart = t  # local t and not account for scr refresh
        instructInconRight_leftImg2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_leftImg2_2, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_leftImg2_2.setAutoDraw(True)
    
    # *insructInconRight_keyResp_2* updates
    waitOnFlip = False
    if insructInconRight_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insructInconRight_keyResp_2.frameNStart = frameN  # exact frame index
        insructInconRight_keyResp_2.tStart = t  # local t and not account for scr refresh
        insructInconRight_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructInconRight_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        insructInconRight_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructInconRight_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructInconRight_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructInconRight_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = insructInconRight_keyResp_2.getKeys(keyList=['8'], waitRelease=False)
        _insructInconRight_keyResp_2_allKeys.extend(theseKeys)
        if len(_insructInconRight_keyResp_2_allKeys):
            insructInconRight_keyResp_2.keys = _insructInconRight_keyResp_2_allKeys[-1].name  # just the last key pressed
            insructInconRight_keyResp_2.rt = _insructInconRight_keyResp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructInconRight_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructInconRight_2" ---
for thisComponent in instructInconRight_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconRight_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructInconLeft" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructInconLeft_keyResp.keys = []
instructInconLeft_keyResp.rt = []
_instructInconLeft_keyResp_allKeys = []
# keep track of which components have finished
instructInconLeftComponents = [instructInconLeft_text, instructInconLeft_centerImg, instructInconLeft_rightImg1, instructInconLeft_rightImg2, instructInconLeft_leftImg1, instructInconLeft_leftImg2, instructInconLeft_keyResp]
for thisComponent in instructInconLeftComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructInconLeft" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconLeft_text* updates
    if instructInconLeft_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_text.frameNStart = frameN  # exact frame index
        instructInconLeft_text.tStart = t  # local t and not account for scr refresh
        instructInconLeft_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_text, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_text.setAutoDraw(True)
    
    # *instructInconLeft_centerImg* updates
    if instructInconLeft_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_centerImg.frameNStart = frameN  # exact frame index
        instructInconLeft_centerImg.tStart = t  # local t and not account for scr refresh
        instructInconLeft_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_centerImg, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_centerImg.setAutoDraw(True)
    
    # *instructInconLeft_rightImg1* updates
    if instructInconLeft_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_rightImg1.frameNStart = frameN  # exact frame index
        instructInconLeft_rightImg1.tStart = t  # local t and not account for scr refresh
        instructInconLeft_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_rightImg1, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_rightImg1.setAutoDraw(True)
    
    # *instructInconLeft_rightImg2* updates
    if instructInconLeft_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_rightImg2.frameNStart = frameN  # exact frame index
        instructInconLeft_rightImg2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_rightImg2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_rightImg2.setAutoDraw(True)
    
    # *instructInconLeft_leftImg1* updates
    if instructInconLeft_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_leftImg1.frameNStart = frameN  # exact frame index
        instructInconLeft_leftImg1.tStart = t  # local t and not account for scr refresh
        instructInconLeft_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_leftImg1, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_leftImg1.setAutoDraw(True)
    
    # *instructInconLeft_leftImg2* updates
    if instructInconLeft_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_leftImg2.frameNStart = frameN  # exact frame index
        instructInconLeft_leftImg2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_leftImg2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_leftImg2.setAutoDraw(True)
    
    # *instructInconLeft_keyResp* updates
    waitOnFlip = False
    if instructInconLeft_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_keyResp.frameNStart = frameN  # exact frame index
        instructInconLeft_keyResp.tStart = t  # local t and not account for scr refresh
        instructInconLeft_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_keyResp, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructInconLeft_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructInconLeft_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructInconLeft_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = instructInconLeft_keyResp.getKeys(keyList=['c'], waitRelease=False)
        _instructInconLeft_keyResp_allKeys.extend(theseKeys)
        if len(_instructInconLeft_keyResp_allKeys):
            instructInconLeft_keyResp.keys = _instructInconLeft_keyResp_allKeys[-1].name  # just the last key pressed
            instructInconLeft_keyResp.rt = _instructInconLeft_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructInconLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructInconLeft" ---
for thisComponent in instructInconLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructInconLeft_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructInconLeft_keyResp_2.keys = []
instructInconLeft_keyResp_2.rt = []
_instructInconLeft_keyResp_2_allKeys = []
# keep track of which components have finished
instructInconLeft_2Components = [instructInconLeft_text_2, instructInconLeft_centerImg_2, instructInconLeft_rightImg1_2, instructInconLeft_rightImg2_2, instructInconLeft_leftImg1_2, instructInconLeft_leftImg2_2, instructInconLeft_keyResp_2]
for thisComponent in instructInconLeft_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructInconLeft_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconLeft_text_2* updates
    if instructInconLeft_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_text_2.frameNStart = frameN  # exact frame index
        instructInconLeft_text_2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_text_2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_text_2.setAutoDraw(True)
    
    # *instructInconLeft_centerImg_2* updates
    if instructInconLeft_centerImg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_centerImg_2.frameNStart = frameN  # exact frame index
        instructInconLeft_centerImg_2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_centerImg_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_centerImg_2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_centerImg_2.setAutoDraw(True)
    
    # *instructInconLeft_rightImg1_2* updates
    if instructInconLeft_rightImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_rightImg1_2.frameNStart = frameN  # exact frame index
        instructInconLeft_rightImg1_2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_rightImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_rightImg1_2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_rightImg1_2.setAutoDraw(True)
    
    # *instructInconLeft_rightImg2_2* updates
    if instructInconLeft_rightImg2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_rightImg2_2.frameNStart = frameN  # exact frame index
        instructInconLeft_rightImg2_2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_rightImg2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_rightImg2_2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_rightImg2_2.setAutoDraw(True)
    
    # *instructInconLeft_leftImg1_2* updates
    if instructInconLeft_leftImg1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_leftImg1_2.frameNStart = frameN  # exact frame index
        instructInconLeft_leftImg1_2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_leftImg1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_leftImg1_2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_leftImg1_2.setAutoDraw(True)
    
    # *instructInconLeft_leftImg2_2* updates
    if instructInconLeft_leftImg2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_leftImg2_2.frameNStart = frameN  # exact frame index
        instructInconLeft_leftImg2_2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_leftImg2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_leftImg2_2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_leftImg2_2.setAutoDraw(True)
    
    # *instructInconLeft_keyResp_2* updates
    waitOnFlip = False
    if instructInconLeft_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_keyResp_2.frameNStart = frameN  # exact frame index
        instructInconLeft_keyResp_2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructInconLeft_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructInconLeft_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructInconLeft_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = instructInconLeft_keyResp_2.getKeys(keyList=['1'], waitRelease=False)
        _instructInconLeft_keyResp_2_allKeys.extend(theseKeys)
        if len(_instructInconLeft_keyResp_2_allKeys):
            instructInconLeft_keyResp_2.keys = _instructInconLeft_keyResp_2_allKeys[-1].name  # just the last key pressed
            instructInconLeft_keyResp_2.rt = _instructInconLeft_keyResp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructInconLeft_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructInconLeft_2" ---
for thisComponent in instructInconLeft_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconLeft_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "respond_onceInstruct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
respond_once_key_resp1.keys = []
respond_once_key_resp1.rt = []
_respond_once_key_resp1_allKeys = []
# keep track of which components have finished
respond_onceInstructComponents = [respond_once_text, respond_once_key_resp1]
for thisComponent in respond_onceInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "respond_onceInstruct" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *respond_once_text* updates
    if respond_once_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respond_once_text.frameNStart = frameN  # exact frame index
        respond_once_text.tStart = t  # local t and not account for scr refresh
        respond_once_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respond_once_text, 'tStartRefresh')  # time at next scr refresh
        respond_once_text.setAutoDraw(True)
    
    # *respond_once_key_resp1* updates
    waitOnFlip = False
    if respond_once_key_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respond_once_key_resp1.frameNStart = frameN  # exact frame index
        respond_once_key_resp1.tStart = t  # local t and not account for scr refresh
        respond_once_key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respond_once_key_resp1, 'tStartRefresh')  # time at next scr refresh
        respond_once_key_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respond_once_key_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respond_once_key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respond_once_key_resp1.status == STARTED and not waitOnFlip:
        theseKeys = respond_once_key_resp1.getKeys(keyList=['c'], waitRelease=False)
        _respond_once_key_resp1_allKeys.extend(theseKeys)
        if len(_respond_once_key_resp1_allKeys):
            respond_once_key_resp1.keys = _respond_once_key_resp1_allKeys[-1].name  # just the last key pressed
            respond_once_key_resp1.rt = _respond_once_key_resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in respond_onceInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "respond_onceInstruct" ---
for thisComponent in respond_onceInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "respond_onceInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_block_loop = data.TrialHandler(nReps=99, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='prac_block_loop')
thisExp.addLoop(prac_block_loop)  # add the loop to the experiment
thisPrac_block_loop = prac_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_block_loop.rgb)
if thisPrac_block_loop != None:
    for paramName in thisPrac_block_loop:
        exec('{} = thisPrac_block_loop[paramName]'.format(paramName))

for thisPrac_block_loop in prac_block_loop:
    currentLoop = prac_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_block_loop.rgb)
    if thisPrac_block_loop != None:
        for paramName in thisPrac_block_loop:
            exec('{} = thisPrac_block_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "eeg_trigger_check" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from triggerCheck_code
    #(re)open trigger port. This is done in case the connection failed,
    #in which case triggers will no longer be sent until the port is reopened.
    
    #At start of routine, we try to close/open the port. This will usually be
    #succesful, causing us to end the routine altogether. However, it will fail if 
    #the usb is unplugged. In this latter case, the routine will then run code each
    #frame to constantly check for the usb being plugged back in, before continuing.
    
    try: 
    #if usb connected, port will close/open and routine will end
        port.close()
        port.open()
        usbConnected = 1 #if successful, set usbConnectd to 1
        continueRoutine = False #if successful, end the routine
    
    except: #if port close/open fails, then set usbConnected to 0. Routine will loop each frame until fixed.
        usbConnected = 0 #if failure, set usbConnected to 0
    # keep track of which components have finished
    eeg_trigger_checkComponents = [triggerIssue_text]
    for thisComponent in eeg_trigger_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eeg_trigger_check" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from triggerCheck_code
        #if the usb is not connected, then keep trying to open port to determine when it has been reconnected.
        if usbConnected == 0:
            
            try: 
                #if usb connected, port will close/open and routine will end
                port.close()
                port.open()
                usbConnected = 1 #if successful, set usbConnectd to 1
                #send trigger to indicate that there was a connection issue that is now resolved
                port.write([0x63]) #hexcode = 99; eeg trigger sent
                time.sleep(PulseWidth) #how long to wait before clearing trigger port
                port.write([0x00]) #clear trigger port by sending hexcode = 0
                #if successful, end the routine
                continueRoutine = False
            
            except: #if usb not connected, routine will continue (keep checking port and keep showing message)
                usbConnected = 0 #if failure, set usbConnectd to 0
                time.sleep(0.5) #wait .5 secs before checking again, to not overload the system
        
        # *triggerIssue_text* updates
        if triggerIssue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            triggerIssue_text.frameNStart = frameN  # exact frame index
            triggerIssue_text.tStart = t  # local t and not account for scr refresh
            triggerIssue_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triggerIssue_text, 'tStartRefresh')  # time at next scr refresh
            triggerIssue_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eeg_trigger_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eeg_trigger_check" ---
    for thisComponent in eeg_trigger_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "eeg_trigger_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prac_blockReminders" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_reminder_keyResp.keys = []
    prac_reminder_keyResp.rt = []
    _prac_reminder_keyResp_allKeys = []
    # keep track of which components have finished
    prac_blockRemindersComponents = [prac_blockText, prac_reminder_text, prac_reminder_keyResp]
    for thisComponent in prac_blockRemindersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_blockReminders" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockText* updates
        if prac_blockText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockText.frameNStart = frameN  # exact frame index
            prac_blockText.tStart = t  # local t and not account for scr refresh
            prac_blockText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockText, 'tStartRefresh')  # time at next scr refresh
            prac_blockText.setAutoDraw(True)
        
        # *prac_reminder_text* updates
        if prac_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_text.frameNStart = frameN  # exact frame index
            prac_reminder_text.tStart = t  # local t and not account for scr refresh
            prac_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_text, 'tStartRefresh')  # time at next scr refresh
            prac_reminder_text.setAutoDraw(True)
        
        # *prac_reminder_keyResp* updates
        waitOnFlip = False
        if prac_reminder_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_keyResp.frameNStart = frameN  # exact frame index
            prac_reminder_keyResp.tStart = t  # local t and not account for scr refresh
            prac_reminder_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_keyResp, 'tStartRefresh')  # time at next scr refresh
            prac_reminder_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_reminder_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_reminder_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_reminder_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = prac_reminder_keyResp.getKeys(keyList=['c'], waitRelease=False)
            _prac_reminder_keyResp_allKeys.extend(theseKeys)
            if len(_prac_reminder_keyResp_allKeys):
                prac_reminder_keyResp.keys = _prac_reminder_keyResp_allKeys[-1].name  # just the last key pressed
                prac_reminder_keyResp.rt = _prac_reminder_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockRemindersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_blockReminders" ---
    for thisComponent in prac_blockRemindersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_blockReminders" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prac_blockReminders_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_reminder_keyResp_2.keys = []
    prac_reminder_keyResp_2.rt = []
    _prac_reminder_keyResp_2_allKeys = []
    # keep track of which components have finished
    prac_blockReminders_2Components = [prac_blockText_2, prac_reminder_text_2, prac_reminder_keyResp_2]
    for thisComponent in prac_blockReminders_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_blockReminders_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockText_2* updates
        if prac_blockText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockText_2.frameNStart = frameN  # exact frame index
            prac_blockText_2.tStart = t  # local t and not account for scr refresh
            prac_blockText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockText_2.started')
            prac_blockText_2.setAutoDraw(True)
        
        # *prac_reminder_text_2* updates
        if prac_reminder_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_text_2.frameNStart = frameN  # exact frame index
            prac_reminder_text_2.tStart = t  # local t and not account for scr refresh
            prac_reminder_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_text_2, 'tStartRefresh')  # time at next scr refresh
            prac_reminder_text_2.setAutoDraw(True)
        
        # *prac_reminder_keyResp_2* updates
        waitOnFlip = False
        if prac_reminder_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_keyResp_2.frameNStart = frameN  # exact frame index
            prac_reminder_keyResp_2.tStart = t  # local t and not account for scr refresh
            prac_reminder_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_keyResp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_reminder_keyResp_2.started')
            prac_reminder_keyResp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_reminder_keyResp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_reminder_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_reminder_keyResp_2.status == STARTED and not waitOnFlip:
            theseKeys = prac_reminder_keyResp_2.getKeys(keyList=['8'], waitRelease=False)
            _prac_reminder_keyResp_2_allKeys.extend(theseKeys)
            if len(_prac_reminder_keyResp_2_allKeys):
                prac_reminder_keyResp_2.keys = _prac_reminder_keyResp_2_allKeys[-1].name  # just the last key pressed
                prac_reminder_keyResp_2.rt = _prac_reminder_keyResp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockReminders_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_blockReminders_2" ---
    for thisComponent in prac_blockReminders_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_blockReminders_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prac_initFixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    initFixation_img_2.setImage('img/fixationCross.png')
    # keep track of which components have finished
    prac_initFixationComponents = [initFixation_img_2]
    for thisComponent in prac_initFixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_initFixation" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *initFixation_img_2* updates
        if initFixation_img_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            initFixation_img_2.frameNStart = frameN  # exact frame index
            initFixation_img_2.tStart = t  # local t and not account for scr refresh
            initFixation_img_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(initFixation_img_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'initFixation_img_2.started')
            initFixation_img_2.setAutoDraw(True)
        if initFixation_img_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img_2.tStop = t  # not accounting for scr refresh
                initFixation_img_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img_2.stopped')
                initFixation_img_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_initFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_initFixation" ---
    for thisComponent in prac_initFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    prac_trial_loop = data.TrialHandler(nReps=10, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('prac_trials.xlsx'),
        seed=None, name='prac_trial_loop')
    thisExp.addLoop(prac_trial_loop)  # add the loop to the experiment
    thisPrac_trial_loop = prac_trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial_loop.rgb)
    if thisPrac_trial_loop != None:
        for paramName in thisPrac_trial_loop:
            exec('{} = thisPrac_trial_loop[paramName]'.format(paramName))
    
    for thisPrac_trial_loop in prac_trial_loop:
        currentLoop = prac_trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial_loop.rgb)
        if thisPrac_trial_loop != None:
            for paramName in thisPrac_trial_loop:
                exec('{} = thisPrac_trial_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_stimRoutine" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_isi_code
        # pick the ISI for the next routine
        # for the online version, this code component should be set to 'both' to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1500, 2000, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        prac_trial_loop.addData('ISI', thisISI)
        
        
        # show in console for debugging
        #print('thisISI: ', thisISI)
        prac_centerImg.setImage(middleStim)
        prac_rightImg1.setImage(rightStim1)
        prac_rightImg2.setImage(rightStim2)
        prac_leftImg1.setImage(leftStim1)
        prac_leftImg2.setImage(leftStim1)
        prac_fixImg.setImage('img/fixationCross.png')
        # Run 'Begin Routine' code from prac_stimTrigger_code
        #set stimTriggerSent to false at the start of the trial. this way
        #when the stimulus is shown, we can change it to True. This variable
        #is used to ensure we only throw the stimulus EEG trigger once.
        stimTriggerSent = False
        prac_stim_keyResp.keys = []
        prac_stim_keyResp.rt = []
        _prac_stim_keyResp_allKeys = []
        # Run 'Begin Routine' code from prac_respTrigger_code
        #clear out the keys_counbted variable at the start of the trial
        #this variable will hold the keys that have had eeg triggers thrown
        #already within a given trial.
        keys_counted = []
        # keep track of which components have finished
        prac_stimRoutineComponents = [prac_centerImg, prac_rightImg1, prac_rightImg2, prac_leftImg1, prac_leftImg2, prac_fixImg, prac_stim_keyResp]
        for thisComponent in prac_stimRoutineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_stimRoutine" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_centerImg* updates
            if prac_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_centerImg.frameNStart = frameN  # exact frame index
                prac_centerImg.tStart = t  # local t and not account for scr refresh
                prac_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_centerImg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_centerImg.started')
                prac_centerImg.setAutoDraw(True)
            if prac_centerImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_centerImg.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_centerImg.tStop = t  # not accounting for scr refresh
                    prac_centerImg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_centerImg.stopped')
                    prac_centerImg.setAutoDraw(False)
            
            # *prac_rightImg1* updates
            if prac_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_rightImg1.frameNStart = frameN  # exact frame index
                prac_rightImg1.tStart = t  # local t and not account for scr refresh
                prac_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_rightImg1, 'tStartRefresh')  # time at next scr refresh
                prac_rightImg1.setAutoDraw(True)
            if prac_rightImg1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_rightImg1.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_rightImg1.tStop = t  # not accounting for scr refresh
                    prac_rightImg1.frameNStop = frameN  # exact frame index
                    prac_rightImg1.setAutoDraw(False)
            
            # *prac_rightImg2* updates
            if prac_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_rightImg2.frameNStart = frameN  # exact frame index
                prac_rightImg2.tStart = t  # local t and not account for scr refresh
                prac_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_rightImg2, 'tStartRefresh')  # time at next scr refresh
                prac_rightImg2.setAutoDraw(True)
            if prac_rightImg2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_rightImg2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_rightImg2.tStop = t  # not accounting for scr refresh
                    prac_rightImg2.frameNStop = frameN  # exact frame index
                    prac_rightImg2.setAutoDraw(False)
            
            # *prac_leftImg1* updates
            if prac_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_leftImg1.frameNStart = frameN  # exact frame index
                prac_leftImg1.tStart = t  # local t and not account for scr refresh
                prac_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_leftImg1, 'tStartRefresh')  # time at next scr refresh
                prac_leftImg1.setAutoDraw(True)
            if prac_leftImg1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_leftImg1.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_leftImg1.tStop = t  # not accounting for scr refresh
                    prac_leftImg1.frameNStop = frameN  # exact frame index
                    prac_leftImg1.setAutoDraw(False)
            
            # *prac_leftImg2* updates
            if prac_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_leftImg2.frameNStart = frameN  # exact frame index
                prac_leftImg2.tStart = t  # local t and not account for scr refresh
                prac_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_leftImg2, 'tStartRefresh')  # time at next scr refresh
                prac_leftImg2.setAutoDraw(True)
            if prac_leftImg2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_leftImg2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_leftImg2.tStop = t  # not accounting for scr refresh
                    prac_leftImg2.frameNStop = frameN  # exact frame index
                    prac_leftImg2.setAutoDraw(False)
            
            # *prac_fixImg* updates
            if prac_fixImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_fixImg.frameNStart = frameN  # exact frame index
                prac_fixImg.tStart = t  # local t and not account for scr refresh
                prac_fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_fixImg, 'tStartRefresh')  # time at next scr refresh
                prac_fixImg.setAutoDraw(True)
            if prac_fixImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_fixImg.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_fixImg.tStop = t  # not accounting for scr refresh
                    prac_fixImg.frameNStop = frameN  # exact frame index
                    prac_fixImg.setAutoDraw(False)
            # Run 'Each Frame' code from prac_stimTrigger_code
            #the first if statement below ensures that the subsequent if statements (and throwing of triggers)
            #only occurs once per trial. That is, only when the stimulus is presented (.status = STARTED) and
            #stimTriggerSent is still False. Once a trigger is sent, we change stimTriggerSent to True so that 
            #the stimulus eeg trigger will not be sent again for this trial
            if prac_centerImg.status == STARTED and not stimTriggerSent:
                if stimNum == 1: #code denoting which stimulus array was sent (from excel file)
                    stimTriggerSent = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                    port.write([0x01]) #hexcode = 1; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
                elif stimNum == 2:
                    stimTriggerSent = True
                    port.write([0x02])
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 3:
                    stimTriggerSent = True
                    port.write([0x03])
                    time.sleep(PulseWidth)
                    port.write([0x00])
                elif stimNum == 4:
                    stimTriggerSent = True
                    port.write([0x04])
                    time.sleep(PulseWidth)
                    port.write([0x00])
            
            # *prac_stim_keyResp* updates
            waitOnFlip = False
            if prac_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_stim_keyResp.frameNStart = frameN  # exact frame index
                prac_stim_keyResp.tStart = t  # local t and not account for scr refresh
                prac_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_stim_keyResp.started')
                prac_stim_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_stim_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(prac_stim_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if prac_stim_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_stim_keyResp.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_stim_keyResp.tStop = t  # not accounting for scr refresh
                    prac_stim_keyResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_stim_keyResp.stopped')
                    prac_stim_keyResp.status = FINISHED
            if prac_stim_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = prac_stim_keyResp.getKeys(keyList=['1','8'], waitRelease=False)
                _prac_stim_keyResp_allKeys.extend(theseKeys)
                if len(_prac_stim_keyResp_allKeys):
                    prac_stim_keyResp.keys = [key.name for key in _prac_stim_keyResp_allKeys]  # storing all keys
                    prac_stim_keyResp.rt = [key.rt for key in _prac_stim_keyResp_allKeys]
            # Run 'Each Frame' code from prac_respTrigger_code
            if prac_stim_keyResp.keys and len(prac_stim_keyResp.keys) > len(keys_counted):# A key response has been made but we haven't yet "counted" it
                keys_counted.append(prac_stim_keyResp.keys[-1]) #add this response to list of keys pressed this trial (-1 is the last position)
                if len(prac_stim_keyResp.keys) < 2: #if this is  the first response
                    if prac_stim_keyResp.keys[-1] == '1':
                        if target == 'left': #correct response
                            port.write([0x0B]) # 11
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'right': #error response
                            port.write([0x0C])# 12
                            time.sleep(PulseWidth)
                            port.write([0x00])
                    elif prac_stim_keyResp.keys[-1] == '8':
                        if target == 'right': #correct response
                            port.write([0x0B]) # 11
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'left': #error response
                            port.write([0x0C])# 12
                            time.sleep(PulseWidth)
                            port.write([0x00])
                elif len(prac_stim_keyResp.keys) >= 2: #if this is NOT the first response
                    if prac_stim_keyResp.keys[-1] == '1':
                        if target == 'left': #technically correct response, but not the first response made
                            port.write([0x15]) # 21
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'right': #technically error response, but not the first response made
                            port.write([0x16])# 22
                            time.sleep(PulseWidth)
                            port.write([0x00])
                    elif prac_stim_keyResp.keys[-1] == '8':
                        if target == 'right': #technically correct response, but not the first response made
                            port.write([0x15]) # 21
                            time.sleep(PulseWidth)
                            port.write([0x00])
                        elif target == 'left': #technically error response, but not the first response made
                            port.write([0x16])# 22
                            time.sleep(PulseWidth)
                            port.write([0x00])
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_stimRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_stimRoutine" ---
        for thisComponent in prac_stimRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if prac_stim_keyResp.keys in ['', [], None]:  # No response was made
            prac_stim_keyResp.keys = None
        prac_trial_loop.addData('prac_stim_keyResp.keys',prac_stim_keyResp.keys)
        if prac_stim_keyResp.keys != None:  # we had a response
            prac_trial_loop.addData('prac_stim_keyResp.rt', prac_stim_keyResp.rt)
        # Run 'End Routine' code from prac_accuracy_code
        trialNum = trialNum + 1 #iterate trial number for this block
        
        if prac_stim_keyResp.keys: #if at least one response was made this trial
            if prac_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                if target == 'left': #if a left target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'right': #if a right target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
            elif prac_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                if target == 'right': #if a right target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this block
                elif target == 'left': #if a left target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
        
        elif not prac_stim_keyResp.keys: # if no response was made
            accuracy = 0
                    
        # save this trial's accuracy to our output file
        prac_trial_loop.addData('accuracy', accuracy)
        # the Routine "prac_stimRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 10 repeats of 'prac_trial_loop'
    
    
    # --- Prepare to start Routine "prac_blockFeed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_blockFeed_code
    blockAcc = numCorr / trialNum #compute accuracy for this block
    
    if blockAcc >= .75: #if accuracy >= 75% then say practice is complete and end practice loop to continue to main exp
        outPut = 'You will now play the real game' #feedback presented
        prac_block_loop.finished = True #end practice loop to continue to main exp
    elif blockAcc <= .75: #if accuracy < 75% then say that practice needs to be repeated and DO NOT end practice loop, instead, allow it to repeat
        outPut = 'Please try the practice again' #feedback presented
        prac_block_loop.finished = False #DO NOT end practice loop and allow to repeat
    
    #reset the following variables to zero before the next practice block starts
    trialNum = 0
    numCorr = 0
    prac_blockFeed_text.setText(outPut)
    prac_blockFeed_keyResp.keys = []
    prac_blockFeed_keyResp.rt = []
    _prac_blockFeed_keyResp_allKeys = []
    # keep track of which components have finished
    prac_blockFeedComponents = [prac_blockFeed_text, prac_pressContinue, prac_blockFeed_keyResp]
    for thisComponent in prac_blockFeedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_blockFeed" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockFeed_text* updates
        if prac_blockFeed_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_text.frameNStart = frameN  # exact frame index
            prac_blockFeed_text.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockFeed_text.started')
            prac_blockFeed_text.setAutoDraw(True)
        
        # *prac_pressContinue* updates
        if prac_pressContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_pressContinue.frameNStart = frameN  # exact frame index
            prac_pressContinue.tStart = t  # local t and not account for scr refresh
            prac_pressContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_pressContinue, 'tStartRefresh')  # time at next scr refresh
            prac_pressContinue.setAutoDraw(True)
        
        # *prac_blockFeed_keyResp* updates
        waitOnFlip = False
        if prac_blockFeed_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_keyResp.frameNStart = frameN  # exact frame index
            prac_blockFeed_keyResp.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_keyResp, 'tStartRefresh')  # time at next scr refresh
            prac_blockFeed_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_blockFeed_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_blockFeed_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_blockFeed_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = prac_blockFeed_keyResp.getKeys(keyList=['c','s'], waitRelease=False)
            _prac_blockFeed_keyResp_allKeys.extend(theseKeys)
            if len(_prac_blockFeed_keyResp_allKeys):
                prac_blockFeed_keyResp.keys = _prac_blockFeed_keyResp_allKeys[-1].name  # just the last key pressed
                prac_blockFeed_keyResp.rt = _prac_blockFeed_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockFeedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_blockFeed" ---
    for thisComponent in prac_blockFeedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from prac_blockFeed_code
    if prac_blockFeed_keyResp.keys[-1] == 's':
        prac_block_loop.finished = True #end practice loop to continue to main exp
    # the Routine "prac_blockFeed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 99 repeats of 'prac_block_loop'


# set up handler to look after randomisation of conditions etc
task_condition_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("condition_"+expInfo['counterbalance']+".xlsx"),
    seed=None, name='task_condition_loop')
thisExp.addLoop(task_condition_loop)  # add the loop to the experiment
thisTask_condition_loop = task_condition_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask_condition_loop.rgb)
if thisTask_condition_loop != None:
    for paramName in thisTask_condition_loop:
        exec('{} = thisTask_condition_loop[paramName]'.format(paramName))

for thisTask_condition_loop in task_condition_loop:
    currentLoop = task_condition_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTask_condition_loop.rgb)
    if thisTask_condition_loop != None:
        for paramName in thisTask_condition_loop:
            exec('{} = thisTask_condition_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "task_condition" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from condition_init_blockCounter
    #reset the following variables at the start of the experiment
    blockCounter = 0
    
    if conditionText == 'Observe other':
        endCondition = 1 # skip all trials for this condition; participant will not play game.
        if expInfo['skipOther'] == '1': #skip 'observe other' screen
            continueRoutine = False
    elif conditionText == 'Observed':
        endCondition = 0 # participant will play game.
    elif conditionText == 'Alone':
        endCondition = 0 # participant will play game.
    condition_whichCondition_text.setText(conditionText)
    condition_keyResp.keys = []
    condition_keyResp.rt = []
    _condition_keyResp_allKeys = []
    # keep track of which components have finished
    task_conditionComponents = [condition_whichCondition_text, condition_reminder_text, condition_keyResp]
    for thisComponent in task_conditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "task_condition" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *condition_whichCondition_text* updates
        if condition_whichCondition_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            condition_whichCondition_text.frameNStart = frameN  # exact frame index
            condition_whichCondition_text.tStart = t  # local t and not account for scr refresh
            condition_whichCondition_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condition_whichCondition_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'condition_whichCondition_text.started')
            condition_whichCondition_text.setAutoDraw(True)
        
        # *condition_reminder_text* updates
        if condition_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            condition_reminder_text.frameNStart = frameN  # exact frame index
            condition_reminder_text.tStart = t  # local t and not account for scr refresh
            condition_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condition_reminder_text, 'tStartRefresh')  # time at next scr refresh
            condition_reminder_text.setAutoDraw(True)
        
        # *condition_keyResp* updates
        waitOnFlip = False
        if condition_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            condition_keyResp.frameNStart = frameN  # exact frame index
            condition_keyResp.tStart = t  # local t and not account for scr refresh
            condition_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condition_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'condition_keyResp.started')
            condition_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(condition_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(condition_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if condition_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = condition_keyResp.getKeys(keyList=['c'], waitRelease=False)
            _condition_keyResp_allKeys.extend(theseKeys)
            if len(_condition_keyResp_allKeys):
                condition_keyResp.keys = _condition_keyResp_allKeys[-1].name  # just the last key pressed
                condition_keyResp.rt = _condition_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_conditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_condition" ---
    for thisComponent in task_conditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "task_condition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    task_block_loop = data.TrialHandler(nReps=10.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='task_block_loop')
    thisExp.addLoop(task_block_loop)  # add the loop to the experiment
    thisTask_block_loop = task_block_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask_block_loop.rgb)
    if thisTask_block_loop != None:
        for paramName in thisTask_block_loop:
            exec('{} = thisTask_block_loop[paramName]'.format(paramName))
    
    for thisTask_block_loop in task_block_loop:
        currentLoop = task_block_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTask_block_loop.rgb)
        if thisTask_block_loop != None:
            for paramName in thisTask_block_loop:
                exec('{} = thisTask_block_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "eeg_trigger_check" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from triggerCheck_code
        #(re)open trigger port. This is done in case the connection failed,
        #in which case triggers will no longer be sent until the port is reopened.
        
        #At start of routine, we try to close/open the port. This will usually be
        #succesful, causing us to end the routine altogether. However, it will fail if 
        #the usb is unplugged. In this latter case, the routine will then run code each
        #frame to constantly check for the usb being plugged back in, before continuing.
        
        try: 
        #if usb connected, port will close/open and routine will end
            port.close()
            port.open()
            usbConnected = 1 #if successful, set usbConnectd to 1
            continueRoutine = False #if successful, end the routine
        
        except: #if port close/open fails, then set usbConnected to 0. Routine will loop each frame until fixed.
            usbConnected = 0 #if failure, set usbConnected to 0
        # keep track of which components have finished
        eeg_trigger_checkComponents = [triggerIssue_text]
        for thisComponent in eeg_trigger_checkComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "eeg_trigger_check" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from triggerCheck_code
            #if the usb is not connected, then keep trying to open port to determine when it has been reconnected.
            if usbConnected == 0:
                
                try: 
                    #if usb connected, port will close/open and routine will end
                    port.close()
                    port.open()
                    usbConnected = 1 #if successful, set usbConnectd to 1
                    #send trigger to indicate that there was a connection issue that is now resolved
                    port.write([0x63]) #hexcode = 99; eeg trigger sent
                    time.sleep(PulseWidth) #how long to wait before clearing trigger port
                    port.write([0x00]) #clear trigger port by sending hexcode = 0
                    #if successful, end the routine
                    continueRoutine = False
                
                except: #if usb not connected, routine will continue (keep checking port and keep showing message)
                    usbConnected = 0 #if failure, set usbConnectd to 0
                    time.sleep(0.5) #wait .5 secs before checking again, to not overload the system
            
            # *triggerIssue_text* updates
            if triggerIssue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                triggerIssue_text.frameNStart = frameN  # exact frame index
                triggerIssue_text.tStart = t  # local t and not account for scr refresh
                triggerIssue_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(triggerIssue_text, 'tStartRefresh')  # time at next scr refresh
                triggerIssue_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in eeg_trigger_checkComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "eeg_trigger_check" ---
        for thisComponent in eeg_trigger_checkComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "eeg_trigger_check" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "task_blockReminders" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from task_blockReminder_code
        if endCondition: # skip all trials for this condition; participant will not play game.
            task_block_loop.finished = True
            continueRoutine = False
        
        blockCounter = blockCounter +1
        
        if blockCounter == 1:
            blockNumText = 'Block 1 of 10'
        elif blockCounter == 2:
            blockNumText = 'Block 2 of 10'
        elif blockCounter == 3:
            blockNumText = 'Block 3 of 10'
        elif blockCounter == 4:
            blockNumText = 'Block 4 of 10'
        elif blockCounter == 5:
            blockNumText = 'Block 5 of 10'
        elif blockCounter == 6:
            blockNumText = 'Block 6 of 10'
        elif blockCounter == 7:
            blockNumText = 'Block 7 of 10'
        elif blockCounter == 8:
            blockNumText = 'Block 8 of 10'
        elif blockCounter == 9:
            blockNumText = 'Block 9 of 10'
        elif blockCounter == 10:
            blockNumText = 'Block 10 of 10'
        task_blockText.setText(blockNumText)
        task_blockReminders_keyResp.keys = []
        task_blockReminders_keyResp.rt = []
        _task_blockReminders_keyResp_allKeys = []
        # keep track of which components have finished
        task_blockRemindersComponents = [task_blockText, task_blockReminders_text, task_blockReminders_keyResp]
        for thisComponent in task_blockRemindersComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task_blockReminders" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *task_blockText* updates
            if task_blockText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_blockText.frameNStart = frameN  # exact frame index
                task_blockText.tStart = t  # local t and not account for scr refresh
                task_blockText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_blockText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task_blockText.started')
                task_blockText.setAutoDraw(True)
            
            # *task_blockReminders_text* updates
            if task_blockReminders_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_blockReminders_text.frameNStart = frameN  # exact frame index
                task_blockReminders_text.tStart = t  # local t and not account for scr refresh
                task_blockReminders_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_blockReminders_text, 'tStartRefresh')  # time at next scr refresh
                task_blockReminders_text.setAutoDraw(True)
            
            # *task_blockReminders_keyResp* updates
            waitOnFlip = False
            if task_blockReminders_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_blockReminders_keyResp.frameNStart = frameN  # exact frame index
                task_blockReminders_keyResp.tStart = t  # local t and not account for scr refresh
                task_blockReminders_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_blockReminders_keyResp, 'tStartRefresh')  # time at next scr refresh
                task_blockReminders_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(task_blockReminders_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(task_blockReminders_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if task_blockReminders_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = task_blockReminders_keyResp.getKeys(keyList=['8'], waitRelease=False)
                _task_blockReminders_keyResp_allKeys.extend(theseKeys)
                if len(_task_blockReminders_keyResp_allKeys):
                    task_blockReminders_keyResp.keys = _task_blockReminders_keyResp_allKeys[-1].name  # just the last key pressed
                    task_blockReminders_keyResp.rt = _task_blockReminders_keyResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_blockRemindersComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task_blockReminders" ---
        for thisComponent in task_blockRemindersComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "task_blockReminders" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "task_initFixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from endTask_code
        if endCondition: # skip all trials for this condition; participant will not play game.
            task_block_loop.finished = True
            continueRoutine = False
        initFixation_img.setImage('img/fixationCross.png')
        # keep track of which components have finished
        task_initFixationComponents = [initFixation_img]
        for thisComponent in task_initFixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task_initFixation" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *initFixation_img* updates
            if initFixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                initFixation_img.frameNStart = frameN  # exact frame index
                initFixation_img.tStart = t  # local t and not account for scr refresh
                initFixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(initFixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img.started')
                initFixation_img.setAutoDraw(True)
            if initFixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > initFixation_img.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    initFixation_img.tStop = t  # not accounting for scr refresh
                    initFixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'initFixation_img.stopped')
                    initFixation_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_initFixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task_initFixation" ---
        for thisComponent in task_initFixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # set up handler to look after randomisation of conditions etc
        task_trial_loop = data.TrialHandler(nReps=10.0, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(whichCondition),
            seed=None, name='task_trial_loop')
        thisExp.addLoop(task_trial_loop)  # add the loop to the experiment
        thisTask_trial_loop = task_trial_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTask_trial_loop.rgb)
        if thisTask_trial_loop != None:
            for paramName in thisTask_trial_loop:
                exec('{} = thisTask_trial_loop[paramName]'.format(paramName))
        
        for thisTask_trial_loop in task_trial_loop:
            currentLoop = task_trial_loop
            # abbreviate parameter names if possible (e.g. rgb = thisTask_trial_loop.rgb)
            if thisTask_trial_loop != None:
                for paramName in thisTask_trial_loop:
                    exec('{} = thisTask_trial_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "task_stimRoutine" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from endTask_code_2
            if endCondition: # skip all trials for this condition; participant will not play game.
                task_trial_loop.finished = True
                task_block_loop.finished = True
                continueRoutine = False
            # Run 'Begin Routine' code from task_isi_code
            # pick the ISI for the next routine
            # for the online version, this code component should be set to 'both' to remove the 'np'
            # at the start of np.linspace (this is a python library JS won't know what to call. 
            
            # make range from a to b in n stepsizes
            ISIRange = np.linspace(1500, 2000, 500)
            
            # picking from a shuffled array is easier for random selection in JS
            shuffle(ISIRange)
            thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
            
            # save this ISI to our output file
            task_trial_loop.addData('ISI', thisISI)
            
            task_centerImg.setImage(middleStim)
            task_rightImg1.setImage(rightStim1)
            task_rightImg2.setImage(rightStim2)
            task_leftImg1.setImage(leftStim1)
            task_leftImg2.setImage(leftStim1)
            task_fixImg.setImage('img/fixationCross.png')
            # Run 'Begin Routine' code from task_stimTrigger_code
            #set stimTriggerSent to false at the start of the trial. this way
            #when the stimulus is shown, we can change it to True. This variable
            #is used to ensure we only throw the stimulus EEG trigger once.
            stimTriggerSent = False
            task_stim_keyResp.keys = []
            task_stim_keyResp.rt = []
            _task_stim_keyResp_allKeys = []
            # Run 'Begin Routine' code from task_respTrigger_code
            #clear out the keys_counbted variable at the start of the trial
            #this variable will hold the keys that have had eeg triggers thrown
            #already within a given trial.
            keys_counted = []
            # keep track of which components have finished
            task_stimRoutineComponents = [task_centerImg, task_rightImg1, task_rightImg2, task_leftImg1, task_leftImg2, task_fixImg, task_stim_keyResp]
            for thisComponent in task_stimRoutineComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "task_stimRoutine" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *task_centerImg* updates
                if task_centerImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_centerImg.frameNStart = frameN  # exact frame index
                    task_centerImg.tStart = t  # local t and not account for scr refresh
                    task_centerImg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_centerImg, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task_centerImg.started')
                    task_centerImg.setAutoDraw(True)
                if task_centerImg.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_centerImg.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        task_centerImg.tStop = t  # not accounting for scr refresh
                        task_centerImg.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'task_centerImg.stopped')
                        task_centerImg.setAutoDraw(False)
                
                # *task_rightImg1* updates
                if task_rightImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_rightImg1.frameNStart = frameN  # exact frame index
                    task_rightImg1.tStart = t  # local t and not account for scr refresh
                    task_rightImg1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_rightImg1, 'tStartRefresh')  # time at next scr refresh
                    task_rightImg1.setAutoDraw(True)
                if task_rightImg1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_rightImg1.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        task_rightImg1.tStop = t  # not accounting for scr refresh
                        task_rightImg1.frameNStop = frameN  # exact frame index
                        task_rightImg1.setAutoDraw(False)
                
                # *task_rightImg2* updates
                if task_rightImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_rightImg2.frameNStart = frameN  # exact frame index
                    task_rightImg2.tStart = t  # local t and not account for scr refresh
                    task_rightImg2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_rightImg2, 'tStartRefresh')  # time at next scr refresh
                    task_rightImg2.setAutoDraw(True)
                if task_rightImg2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_rightImg2.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        task_rightImg2.tStop = t  # not accounting for scr refresh
                        task_rightImg2.frameNStop = frameN  # exact frame index
                        task_rightImg2.setAutoDraw(False)
                
                # *task_leftImg1* updates
                if task_leftImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_leftImg1.frameNStart = frameN  # exact frame index
                    task_leftImg1.tStart = t  # local t and not account for scr refresh
                    task_leftImg1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_leftImg1, 'tStartRefresh')  # time at next scr refresh
                    task_leftImg1.setAutoDraw(True)
                if task_leftImg1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_leftImg1.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        task_leftImg1.tStop = t  # not accounting for scr refresh
                        task_leftImg1.frameNStop = frameN  # exact frame index
                        task_leftImg1.setAutoDraw(False)
                
                # *task_leftImg2* updates
                if task_leftImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_leftImg2.frameNStart = frameN  # exact frame index
                    task_leftImg2.tStart = t  # local t and not account for scr refresh
                    task_leftImg2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_leftImg2, 'tStartRefresh')  # time at next scr refresh
                    task_leftImg2.setAutoDraw(True)
                if task_leftImg2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_leftImg2.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        task_leftImg2.tStop = t  # not accounting for scr refresh
                        task_leftImg2.frameNStop = frameN  # exact frame index
                        task_leftImg2.setAutoDraw(False)
                
                # *task_fixImg* updates
                if task_fixImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_fixImg.frameNStart = frameN  # exact frame index
                    task_fixImg.tStart = t  # local t and not account for scr refresh
                    task_fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_fixImg, 'tStartRefresh')  # time at next scr refresh
                    task_fixImg.setAutoDraw(True)
                if task_fixImg.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_fixImg.tStartRefresh + thisISI-frameTolerance:
                        # keep track of stop time/frame for later
                        task_fixImg.tStop = t  # not accounting for scr refresh
                        task_fixImg.frameNStop = frameN  # exact frame index
                        task_fixImg.setAutoDraw(False)
                # Run 'Each Frame' code from task_stimTrigger_code
                #the first if statement below ensures that the subsequent if statements (and throwing of triggers)
                #only occurs once per trial. That is, only when the stimulus is presented (.status = STARTED) and
                #stimTriggerSent is still False. Once a trigger is sent, we change stimTriggerSent to True so that 
                #the stimulus eeg trigger will not be sent again for this trial
                if task_centerImg.status == STARTED and not stimTriggerSent:
                    if stimNum == 41: #code denoting which stimulus array was sent (from excel file)
                        stimTriggerSent = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                        port.write([0x29]) #hexcode = 41; eeg trigger sent
                        time.sleep(PulseWidth) #how long to wait before clearing trigger port
                        port.write([0x00]) #clear trigger port by sending hexcode = 0
                    elif stimNum == 42:
                        stimTriggerSent = True
                        port.write([0x2A])
                        time.sleep(PulseWidth)
                        port.write([0x00])
                    elif stimNum == 43:
                        stimTriggerSent = True
                        port.write([0x2B])
                        time.sleep(PulseWidth)
                        port.write([0x00])
                    elif stimNum == 44:
                        stimTriggerSent = True
                        port.write([0x2C])
                        time.sleep(PulseWidth)
                        port.write([0x00])
                    elif stimNum == 51: #code denoting which stimulus array was sent (from excel file)
                        stimTriggerSent = True #switch stimTriggerSent to True so that the stimulus eeg trigger will not be sent again this trial
                        port.write([0x33]) #hexcode = 51; eeg trigger sent
                        time.sleep(PulseWidth) #how long to wait before clearing trigger port
                        port.write([0x00]) #clear trigger port by sending hexcode = 0
                    elif stimNum == 52:
                        stimTriggerSent = True
                        port.write([0x34])
                        time.sleep(PulseWidth)
                        port.write([0x00])
                    elif stimNum == 53:
                        stimTriggerSent = True
                        port.write([0x35])
                        time.sleep(PulseWidth)
                        port.write([0x00])
                    elif stimNum == 54:
                        stimTriggerSent = True
                        port.write([0x36])
                        time.sleep(PulseWidth)
                        port.write([0x00])
                
                # *task_stim_keyResp* updates
                waitOnFlip = False
                if task_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_stim_keyResp.frameNStart = frameN  # exact frame index
                    task_stim_keyResp.tStart = t  # local t and not account for scr refresh
                    task_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task_stim_keyResp.started')
                    task_stim_keyResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(task_stim_keyResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(task_stim_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if task_stim_keyResp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_stim_keyResp.tStartRefresh + thisISI-frameTolerance:
                        # keep track of stop time/frame for later
                        task_stim_keyResp.tStop = t  # not accounting for scr refresh
                        task_stim_keyResp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'task_stim_keyResp.stopped')
                        task_stim_keyResp.status = FINISHED
                if task_stim_keyResp.status == STARTED and not waitOnFlip:
                    theseKeys = task_stim_keyResp.getKeys(keyList=['1','8'], waitRelease=False)
                    _task_stim_keyResp_allKeys.extend(theseKeys)
                    if len(_task_stim_keyResp_allKeys):
                        task_stim_keyResp.keys = [key.name for key in _task_stim_keyResp_allKeys]  # storing all keys
                        task_stim_keyResp.rt = [key.rt for key in _task_stim_keyResp_allKeys]
                # Run 'Each Frame' code from task_respTrigger_code
                if task_stim_keyResp.keys and len(task_stim_keyResp.keys) > len(keys_counted):# A key response has been made but we haven't yet "counted" it
                    keys_counted.append(task_stim_keyResp.keys[-1]) #add this response to list of keys pressed this trial
                    if len(task_stim_keyResp.keys) < 2: #if this is  the first response
                        if task_stim_keyResp.keys[-1] == '1':
                            if target == 'left': #correct response
                                port.write([0x0B]) # 11
                                time.sleep(PulseWidth)
                                port.write([0x00])
                            elif target == 'right': #error response
                                port.write([0x0C])# 12
                                time.sleep(PulseWidth)
                                port.write([0x00])
                        elif task_stim_keyResp.keys[-1] == '8':
                            if target == 'right': #correct response
                                port.write([0x0B]) # 11
                                time.sleep(PulseWidth)
                                port.write([0x00])
                            elif target == 'left': #error response
                                port.write([0x0C])# 12
                                time.sleep(PulseWidth)
                                port.write([0x00])
                    elif len(task_stim_keyResp.keys) >= 2: #if this is NOT the first response
                        if task_stim_keyResp.keys[-1] == '1':
                            if target == 'left': #technically correct response, but not the first response made
                                port.write([0x15]) # 21
                                time.sleep(PulseWidth)
                                port.write([0x00])
                            elif target == 'right': #technically error response, but not the first response made
                                port.write([0x16])# 22
                                time.sleep(PulseWidth)
                                port.write([0x00])
                        elif task_stim_keyResp.keys[-1] == '8':
                            if target == 'right': #technically correct response, but not the first response made
                                port.write([0x15]) # 21
                                time.sleep(PulseWidth)
                                port.write([0x00])
                            elif target == 'left': #technically error response, but not the first response made
                                port.write([0x16])# 22
                                time.sleep(PulseWidth)
                                port.write([0x00])
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in task_stimRoutineComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "task_stimRoutine" ---
            for thisComponent in task_stimRoutineComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if task_stim_keyResp.keys in ['', [], None]:  # No response was made
                task_stim_keyResp.keys = None
            task_trial_loop.addData('task_stim_keyResp.keys',task_stim_keyResp.keys)
            if task_stim_keyResp.keys != None:  # we had a response
                task_trial_loop.addData('task_stim_keyResp.rt', task_stim_keyResp.rt)
            # Run 'End Routine' code from task_accuracy_code
            trialNum = trialNum + 1 #iterate trial number for this block
            
            if task_stim_keyResp.keys: #if at least one response was made this trial
                if task_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                    if target == 'left': #if a left target stim was shown this trial
                        accuracy = 1 #mark this trial as correct
                        numCorr = numCorr +1 #iterate number of correct responses for this block
                    elif target == 'right': #if a right target stim was shown this trial
                        accuracy = 0 #mark this trial as an error
                elif task_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                    if target == 'right': #if a right target stim was shown this trial
                        accuracy = 1 #mark this trial as correct
                        numCorr = numCorr +1 #iterate number of correct responses for this block
                    elif target == 'left': #if a left target stim was shown this trial
                        accuracy = 0 #mark this trial as an error
            
            elif not task_stim_keyResp.keys: # if no response was made
                accuracy = 0
            
            # save this trial's accuracy to our output file
            task_trial_loop.addData('accuracy', accuracy)
            # the Routine "task_stimRoutine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 10.0 repeats of 'task_trial_loop'
        
        
        # --- Prepare to start Routine "task_blockFeed" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from endTask_code_3
        if endCondition: # skip all trials for this condition; participant will not play game.
            task_block_loop.finished = True
            continueRoutine = False
        # Run 'Begin Routine' code from task_blockFeed_code
        blockAcc = numCorr / trialNum #compute accuracy for this block
        
        if blockCounter < 10:
            if blockAcc >= .75:
                if blockAcc < .9:
                    blockFeed = 'Good job'
                    blockFeedCat = 1
                elif blockAcc >= .9:
                    blockFeed = 'Respond faster'
                    blockFeedCat = 2
            elif blockAcc < .75:
                blockFeed = 'Respond more accurately'
                blockFeedCat = 3
        elif blockCounter == 10:
            'You have completed all blocks'
        
        # save this block's feedback to our output file
        task_trial_loop.addData('blockFeedCat', blockFeedCat)
        
        #reset the following variables to zero before next block starts
        trialNum = 0
        numCorr = 0
        task_blockFeed_text.setText(blockFeed)
        task_blockFeed_text2.setText('Press the right button to continue')
        task_blockFeed_keyResp.keys = []
        task_blockFeed_keyResp.rt = []
        _task_blockFeed_keyResp_allKeys = []
        # keep track of which components have finished
        task_blockFeedComponents = [task_blockFeed_text, task_blackFeed_text3, task_blockFeed_text2, task_blockFeed_keyResp]
        for thisComponent in task_blockFeedComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task_blockFeed" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *task_blockFeed_text* updates
            if task_blockFeed_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_blockFeed_text.frameNStart = frameN  # exact frame index
                task_blockFeed_text.tStart = t  # local t and not account for scr refresh
                task_blockFeed_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_blockFeed_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task_blockFeed_text.started')
                task_blockFeed_text.setAutoDraw(True)
            
            # *task_blackFeed_text3* updates
            if task_blackFeed_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_blackFeed_text3.frameNStart = frameN  # exact frame index
                task_blackFeed_text3.tStart = t  # local t and not account for scr refresh
                task_blackFeed_text3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_blackFeed_text3, 'tStartRefresh')  # time at next scr refresh
                task_blackFeed_text3.setAutoDraw(True)
            if task_blackFeed_text3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_blackFeed_text3.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    task_blackFeed_text3.tStop = t  # not accounting for scr refresh
                    task_blackFeed_text3.frameNStop = frameN  # exact frame index
                    task_blackFeed_text3.setAutoDraw(False)
            
            # *task_blockFeed_text2* updates
            if task_blockFeed_text2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
                # keep track of start time/frame for later
                task_blockFeed_text2.frameNStart = frameN  # exact frame index
                task_blockFeed_text2.tStart = t  # local t and not account for scr refresh
                task_blockFeed_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_blockFeed_text2, 'tStartRefresh')  # time at next scr refresh
                task_blockFeed_text2.setAutoDraw(True)
            
            # *task_blockFeed_keyResp* updates
            waitOnFlip = False
            if task_blockFeed_keyResp.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
                # keep track of start time/frame for later
                task_blockFeed_keyResp.frameNStart = frameN  # exact frame index
                task_blockFeed_keyResp.tStart = t  # local t and not account for scr refresh
                task_blockFeed_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_blockFeed_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task_blockFeed_keyResp.started')
                task_blockFeed_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(task_blockFeed_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(task_blockFeed_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if task_blockFeed_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = task_blockFeed_keyResp.getKeys(keyList=['8'], waitRelease=False)
                _task_blockFeed_keyResp_allKeys.extend(theseKeys)
                if len(_task_blockFeed_keyResp_allKeys):
                    task_blockFeed_keyResp.keys = _task_blockFeed_keyResp_allKeys[-1].name  # just the last key pressed
                    task_blockFeed_keyResp.rt = _task_blockFeed_keyResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_blockFeedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task_blockFeed" ---
        for thisComponent in task_blockFeedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "task_blockFeed" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'task_block_loop'
    
    
    # --- Prepare to start Routine "task_conditionComplete" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from stimTask_code_4
    if endCondition: # skip all trials for this condition; participant will not play game.
        continueRoutine = False
    conditionComplete_key_resp.keys = []
    conditionComplete_key_resp.rt = []
    _conditionComplete_key_resp_allKeys = []
    # keep track of which components have finished
    task_conditionCompleteComponents = [conditionComplete_text, conditionComplete_key_resp]
    for thisComponent in task_conditionCompleteComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "task_conditionComplete" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *conditionComplete_text* updates
        if conditionComplete_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            conditionComplete_text.frameNStart = frameN  # exact frame index
            conditionComplete_text.tStart = t  # local t and not account for scr refresh
            conditionComplete_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(conditionComplete_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'conditionComplete_text.started')
            conditionComplete_text.setAutoDraw(True)
        
        # *conditionComplete_key_resp* updates
        waitOnFlip = False
        if conditionComplete_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            conditionComplete_key_resp.frameNStart = frameN  # exact frame index
            conditionComplete_key_resp.tStart = t  # local t and not account for scr refresh
            conditionComplete_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(conditionComplete_key_resp, 'tStartRefresh')  # time at next scr refresh
            conditionComplete_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(conditionComplete_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(conditionComplete_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if conditionComplete_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = conditionComplete_key_resp.getKeys(keyList=['c'], waitRelease=False)
            _conditionComplete_key_resp_allKeys.extend(theseKeys)
            if len(_conditionComplete_key_resp_allKeys):
                conditionComplete_key_resp.keys = _conditionComplete_key_resp_allKeys[-1].name  # just the last key pressed
                conditionComplete_key_resp.rt = _conditionComplete_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_conditionCompleteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_conditionComplete" ---
    for thisComponent in task_conditionCompleteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "task_conditionComplete" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'task_condition_loop'

# Run 'End Experiment' code from setup_code
win.mouseVisible = True #make the mouse cursor visable again
port.write([0xFF]) #set port values back to default state (FF)
time.sleep(PulseWidth) #wait PulseWidth amount of time before doing anything else
port.close() #close port opened at start of exp

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
