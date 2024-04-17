from psychopy.visual.basevisual import BaseVisualStim


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
