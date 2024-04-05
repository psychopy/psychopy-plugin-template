from psychopy.experiment.components import BaseComponent

class ExampleComponent(BaseComponent):
    """
    Example Component to show you how to make and document one.
    """
    # mark it as coming from this plugin
    plugin = "psychopy-example-plugin"
    # specify what libraries it has code for - PsychoPy and/or PsychoJS
    targets = ["PsychoPy", "PsychoJS"]
