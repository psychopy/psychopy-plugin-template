"""
Tests for the ExampleVisualStim class, essentially showcases how to implement basic tests on a visual stim.
"""


from psychopy import visual
from psychopy_plugin_template.visual.exampleVisualStim import ExampleVisualStim


class TestExampleVisualStim:
    def setup_class(self):
        """
        This method is run when the TestExampleVisualStim class is initialised, before any of the test methods. Use it to setup things which you only want to happen once - like creating a window.
        """
        # make a Window
        self.win = visual.Window(
            size=[128,128], pos=[50,50], 
            monitor="testMonitor", allowGUI=False,
            autoLog=False
        )
    
    def teardown_class(self):
        """
        This method is run after all tests have completed.
        """
        # close the window
        self.win.close()
    
    def setup_method(self):
        """
        This method is run before each test starts. Use it to setup things which you want to be fresh at the start of each test, like creating the stimulus object.
        """
        # create an instance of the class to test
        self.obj = ExampleVisualStim(
            self.win, units="height", name="testExampleStim", autoLog=True
        )
    
    def teardown_method(self):
        """
        This method is run after each test finishes. Use it to clean up after each test, like deleting the stimulus object (ready to be recreated by setup_method)
        """
        # delete the instance of this class
        del self.obj
        self.obj = None
    
    # --- Tests ---
    
    def test_example(self):
        """
        Any method whose name begins with "test" will be run as a test - the test will fail if any error is raised, and will pass otherwise. Use `assert` if you want to check a specific value - which will raise an error if the value is False. For example:
        ```
        myVar = "red"
        assert myVar == "blue", f"myVar needs to be 'blue' to pass, but it was {myVar}"
        ```
        will raise:
        ```
        AssertionError: myVar needs to be 'blue' to pass, but it was red
        ```
        """
        return


