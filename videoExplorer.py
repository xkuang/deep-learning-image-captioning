from keras.models import Sequential,Model
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding,GRU,TimeDistributed,RepeatVector,Merge,BatchNormalization,Input
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Embedding,LSTM,GRU,TimeDistributed,RepeatVector,Merge,Input,merge,UpSampling2D
from keras.preprocessing import sequence
from keras import callbacks
from keras.optimizers import SGD, RMSprop, Adam

import numpy as np
from vgg16 import Vgg16
import matplotlib.pyplot as plt
import PIL.Image

from tqdm import tqdm

from utils import *

import cPickle as pickle
import string

import collections
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

import re
from numpy.random import random, permutation, randn, normal 

import os

import preprocessing as preproc

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from matplotlib import animation
from IPython.display import display, HTML

import pandas as pd
import imageio


def resize_video_frame(pic):
    return np.asarray(Image.fromarray(np.uint8(pic)).resize((224, 224), Image.NEAREST))

def read_video_frames(filename):
    vid = imageio.get_reader(filename,  'ffmpeg')
    
    frames = []
    
    for i, im in enumerate(vid):
        im = np.asarray(im)
        im = np.expand_dims(im,axis=0)
        frames.append(im)
    
    frames = np.vstack(frames)
    
    return [resize_video_frame(pic) for pic in frames]

def get_mp4_vid_frames(filename):
    
    frames = read_video_frames(filename)

    frames = np.transpose(np.asarray(frames),(0,3,1,2))
        
    return frames

def search_video_by(searched_word,images,predicted_captions):
    lmtzr = WordNetLemmatizer()
    lemm_word = lmtzr.lemmatize(searched_word)
    
    found_indexes = []
    for index,caption in enumerate(predicted_captions):
        lemm_caption_words = [lmtzr.lemmatize(word) for word in caption.split()]
        if lemm_word in lemm_caption_words:
            found_indexes.append(index)
   
    
    return ([images[i] for i in found_indexes],[predicted_captions[i] for i in found_indexes],found_indexes)
    

























