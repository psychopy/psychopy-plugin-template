from psychopy.hardware.base import BaseResponseDevice, BaseResponse


class ExampleResponse(BaseResponse):
    """ 
    Blank hardware response object to showcase how to make a new type of hardware response for a ResponseDevice.

    Parameters
    ----------
    t : float
        Time at which the response happened
    value
        Value received (e.g. the key on a keyboard)
    """

class ExampleResponseDevice(BaseResponseDevice):
    """
    Blank hardware object to showcase how to make a new type of hardware object for a response device.
    
    Should be deleted before publishing your plugin.

    Attributes
    ----------
    listeners : list[psychopy.hardware.listeners.BaseListener]
        List of listeners to send responses to
    responses : list[ExampleResponse]
        List of responses received by this device object
    muteOutsidePsychopy : bool
        If True, then mute any responses gathered when the PsychoPy window is not in focus
    """
    responseClass = ExampleResponse
