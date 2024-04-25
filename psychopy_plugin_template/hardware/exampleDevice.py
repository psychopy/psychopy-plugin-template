from psychopy.hardware.base import BaseDevice


class ExampleDevice(BaseDevice, aliases=["example"]):
    """
    Blank hardware object showcase how to make a new type of hardware object. If the hardware in question is a response device, such as a button box, you should check out the docs for [ExampleResponseDevice][psychopy_plugin_template.hardware.exampleResponseDevice.ExampleResponseDevice] instead.
    
    Should be deleted before publishing your plugin.
    """
