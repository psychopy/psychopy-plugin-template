from psychopy.visual.basevisual import BaseVisualStim
from psychopy.tools.attributetools import attributeSetter, setAttribute

class ExampleVisualStim(BaseVisualStim):
    """
    Blank visual stim to showcase how to make a new visual stim. Should be deleted before publishing your plugin.

    Parameters
    ----------
    win : psychopy.visual.Window
        Window to draw stimulus to
    units : str
        Spatial unit space in which to specify size, pos, etc. for stimulus.
    name : str
        Arbitrary name by which to refer to stimulus
    autoLog : bool
        Whether to automatically log any changes to stimulus' attributes
    """
    def draw(self):
        """
        Your stimulus class needs to define a `draw` function - otherwise you'll hit a NotImplementedError at the first win flip!
        """
        return
    
    @attributeSetter
    def exampleAttribute(self, value):
        """
        Example attribute to show how to use the attributeSetter decorator.

        Parameters
        ----------
        value : any
            Whatever value you want to set
        """
        # attributeSetter handles all of the necessary logging stuff - so all you need to do is set the base value in this object's __dict__
        self.__dict__['exampleAttribute'] = value
        # you may want setting this attribute to do something else - let's say changing color if given one of three color names
        if value in ("red", "green", "blue"):
            self.fillColor = value
    
    def setExampleAttribute(self, value, log=True):
        """
        If an attribute can be set each frame/repeat from Builder, there needs to be a function called set<attribute name in PascalCase> as this will be called from the generated code.

        Parameters
        ----------
        value : any
            Whatever value you want to set
        log : bool, optional
            Whether or not to log setting this attribute - will be True for set each repeat and False for set each frame
        """
        setAttribute(self, "exampleAttribute", value=value, log=log)

