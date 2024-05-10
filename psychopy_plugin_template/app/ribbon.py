import wx
from psychopy.app.ribbon import FrameRibbonPluginSection


class ExamplePluginRibbonSection(FrameRibbonPluginSection):
    def __init__(self, parent):
        # initialise the base class
        FrameRibbonPluginSection.__init__(
            self, parent, name="example", label="Example"
        )
        # add a button
        self.addButton(
            "exampleBtn", 
            label="Example button", 
            icon="example", 
            tooltip="Open the documentation for psychopy-plugin-template", 
            callback=self.openExamplePluginDocs, 
            style=wx.BU_NOTEXT
        )
    
    def openExamplePluginDocs(self, evt=None):
        """
        Button callback to open the docs for psychopy-plugin-template in the default web browser.

        Parameters
        ----------
        evt : wx.Event, optional
            The button press event triggering this callback, unused but needs to be accepted as wx will provide it.
        """
        import webbrowser
        webbrowser.open("https://psychopy.github.io/psychopy-plugin-template")

