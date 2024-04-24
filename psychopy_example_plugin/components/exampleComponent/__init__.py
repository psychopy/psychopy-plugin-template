from psychopy.experiment.components import BaseComponent, Param, getInitVals
from pathlib import Path

class ExampleComponent(BaseComponent):
    """
    Example Component to show you how to make and document one.
    """
    # mark it as coming from this plugin
    plugin = "psychopy-example-plugin"
    # specify what libraries it has code for - PsychoPy and/or PsychoJS
    targets = ["PsychoPy"]
    # specify what category (or categories) to list this Component under in Builder
    categories = ['Custom']
    # path to this Component's icon file - ignoring the light/dark/classic folder and any @2x in the filename (PsychoPy will add these accordingly)
    iconFile = Path(__file__).parent / "example.png"
    # Text to display when this Component is hovered over
    tooltip = "Example Component to show you how to use PsychoPy"
    # what is the earliest version of PsychoPy this Component works with?
    version = "0.0.0"
    # is this Component still in beta?
    beta = True

    def __init__(
        self, exp, parentName, 
        # basic
        name="",
        # appearance
        exampleAttribute="red",
    ):
        # initialise the base component class
        BaseComponent.__init__(self, exp, parentName, name=name)
        # base params like start and stop time are already added by BaseComponent, so add any other params in here...

        # --- Params ---

        # appearance
        self.order += [
            "exampleAttribute"
        ]
        self.params['exampleAttribute'] = Param(
            exampleAttribute, valType="code", inputType="single", categ="Appearance",
            label="Example attribute", hint="An example attribute to show you how to add one"
        )
    
    def writeInitCode(self, buff):
        """
        Write the Python code which initialises the object for this Component.

        Parameters
        ----------
        buff : 
            String buffer to write to, i.e. the .py file
        """
        # any params using set each frame / repeat will need a safe value to start off with, this functon automatically substitutes those
        inits = getInitVals(self.params)
        # construct the actual code, using Python string formatting
        # remember that params with valType="str" will already have quotes so you don't need to add them
        code = (
            "%(name)s = visual.ExampleVisualStim(\n"
            "    win=win,\n"
            "    name='%(name)s',\n"
            ")\n"
            "%(name)s.setExampleAttribute(%(exampleAttribute)s, log=False)\n"
        )
        # write the code to the string buffer (with params inserted)
        buff.writeIndentedLines(code % inits)
    
    def writeInitCodeJS(self, buff):
        """
        This example only writes Python code, but if you want your Component to write JS you can use this function!

        Parameters
        ----------
        buff : 
            String buffer to write to, i.e. the .js file
        """
        pass

    def writeRoutineStartCode(self, buff):
        """
        Write the Python code which is called at the start of this Component's Routine

        Parameters
        ----------
        buff : 
            String buffer to write to, i.e. the .py file
        """
        # update any parameters which need updating
        self.writeParamUpdates(buff, updateType="set every repeat")
        # aaaaand that's all you need! unless you want anything else to happen here - it's essentially the equivalent of the Begin Routine tab in a Code Component
    
    def writeFrameCode(self, buff):
        """
        Write the Python code which is called each frame for this Component.

        Parameters
        ----------
        buff : 
            String buffer to write to, i.e. the .py file
        """
        # update any parameters which need updating
        self.writeParamUpdates(buff, updateType="set every frame")
        # some code we want to run just once on the first frame of the Component - so we'll use the writeStartTestCode function to open an if statement and then dedent after
        dedent = self.writeStartTestCode(buff)
        # we only want the following code written if an if loop actually was opened, not if the start time is None! so make sure to use dedent as a boolean to avoid writing broken code
        if dedent:
            # status setting is already written by writeStartTestCode, so here we can just worry about extra stuff
            code = (
                "%(name)s.autoDraw = True\n"
                "print('%(name)s has started! Yay!')\n"
            )
            buff.writeIndentedLines(code % self.params)
            # dedent after!
            buff.setIndentLevel(-dedent, relative=True)
        
        # use the same principle as we used for first-frame-of-Component code to add code which only runs while the Component is active
        dedent = self.writeActiveTestCode(buff)
        if dedent:
            # here we can just add anything we want to happen each frame - let's update some arbitrary variable for fun
            code = (
                "%(name)s.someAttribute = randchoice(['a', 'b', 'c']))\n"
            )
            buff.writeIndentedLines(code % self.params)
            # dedent after!
            buff.setIndentLevel(-dedent, relative=True)
        
        # use the same principles again for last-frame-of-Component code
        dedent = self.writeStopTestCode(buff)
        if dedent:
            # aaaaaaand some extra code for when the Component stops
            code = (
                "%(name)s.autoDraw = False\n"
                "print('%(name)s has finished! Yay!')\n"
            )
            buff.writeIndentedLines(code % self.params)
            # dedent after!
            buff.setIndentLevel(-dedent, relative=True)
    
    def writeRoutineEndCode(self, buff):
        """
        Write the Python code which is called at the end of this Component's Routine

        Parameters
        ----------
        buff : 
            String buffer to write to, i.e. the .py file
        """
        # create a copy of params so that we can safely edit stuff
        params = self.params.copy()
        # add reference to the current loop (handy for data writing)
        params['currentLoop'] = self.currentLoop
        # store any data we'd like to store (start/stop are already handled)
        code = (
            "%(currentLoop)s.addData('%(name)s.someAttribute', %(name)s.someAttribute)"
        )
        buff.writeIndentedLines(code % params)

        

