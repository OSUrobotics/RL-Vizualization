from backend_base import PlotBackendBase
from data_loading_base import DataLoaderBase
from abc import ABC, abstractmethod

class GuiFrontend(ABC):
    def __init__(self):
        '''
        Method initializes a data loader and a plotter on the backend in addition to initializing the gui portion
        '''
        self.data_loader = DataLoaderBase()
        self.plotter = PlotBackendBase()
    
    @abstractmethod
    def run(self):
        '''
        Method to run the gui window. Should connect each button/slider defined in initialization to the desired functions in 
        either the plot backend or data loader
        '''
        pass

    @abstractmethod
    def save_figure(self,filename):
        '''
        Method to save the figure currently in the gui window to a desired filename/type
        '''
        pass
