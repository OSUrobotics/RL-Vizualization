#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:04:51 2023

@author: orochi
"""
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class PlotBackendBase(ABC):
    
    @abstractmethod
    def __init__(self):
        '''
        Method initializes a figure and axes object that are used for subsequent plotting
        '''
        self.fig, self.ax = plt.subplots()

    @abstractmethod
    def reset(self):
        '''
        Method clears plots and resets saved information such as previous runs or configuration information
        '''
        pass
    
    @abstractmethod
    def draw_simple(self,dataframe):
        '''
        Method plots based on information from a single external dataframe. 
        '''
        pass
    
    @abstractmethod
    def draw_complex(self,dataframe,config):
        '''
        Method plots based on information from an external dataframe AND config specific information'''

    def get_figure(self):
        return self.fig, self.ax
    
