#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:04:51 2023

@author: orochi
"""
from abc import ABC, abstractmethod

class DataLoaderBase(ABC):
    @abstractmethod
    def load_single(self, filepath):
        '''
        Method to load data from a single episode into self.episode_data. 
        These should be broken up into different functions for different file types
        '''
        self.episode_data = []
    
    @abstractmethod
    def load_agregate(self, folderpath):
        '''
        Method to load data from a data folder into self.run_data
        Use of multiprocessing is advised for large numbers of episodes
        These should be broken up into different functions for different file types
        '''
        self.run_data = []
    
    @abstractmethod
    def load_config(self, config_folder):
        '''
        loads configuration information such as batch size, learning rate etc that may be used by some plotting functions
        '''
        self.config = []
    