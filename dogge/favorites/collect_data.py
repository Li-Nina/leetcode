#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: 小马哥

import os
import logging
from logging.handlers import TimedRotatingFileHandler


class Logger(object):

    def __init__(self, name, logFilePath):
        name = name.replace('.log', '')
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        handler = TimedRotatingFileHandler(logFilePath,
                                      when='W0',
                                      backupCount=300)
        formatter = logging.Formatter('%(asctime)s _ %(name)s _ %(levelname)s _ %(message)s')
        handler.setFormatter(formatter)
        handler.suffix = "%Y-%m-%d-%H-%M-%S.log"
        logger.handlers=[]
        logger.addHandler(handler)
        self._logger = logger

    def get(self):
        return self._logger

