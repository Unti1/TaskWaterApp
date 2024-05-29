from typing import Self, Optional, List, Dict

############################################
"""Прочие необходимые библиотеки"""
import shutil
import random
import traceback
import configparser
from threading import Thread
from ast import literal_eval
import platform
import csv
import sys
import time
import os
import re
import json

########################################### 
import datetime

'''
Bot development
'''
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router, types, F
from aiogram.types import Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.enums import ParseMode
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

##### FAST API
from fastapi import FastAPI, HTTPException
from fastapi import WebSocket, WebSocketDisconnect, APIRouter


##### Async needed
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio


USER_DATA_PATH = 'data/users.json'

config = configparser.ConfigParser()
config.read(r'settings/settings.ini')  # читаем конфиг

def config_update():
    with open(r'settings/settings.ini', 'w') as f:
        config.write(f)
    config.read(r'settings/settings.ini')

import logging
logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    format="%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    encoding="utf-8"
)
