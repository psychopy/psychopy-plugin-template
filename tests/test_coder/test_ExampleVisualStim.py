"""
Tests for the ExampleVisualStim class, essentially showcases how to implement basic tests on a visual stim.
"""


from psychopy.tests.test_visual.test_basevisual import _TestColorMixin, _TestUnitsMixin
from psychopy import visual
from psychopy_example_plugin.visual.exampleVisualStim import ExampleVisualStim


class TestExampleVisualStim(_TestColorMixin, _TestUnitsMixin):
    def setup_class(self):
        """
        This method is run when the TestExampleVisualStim class is initialised, before any of the test methods.
        """
        # make a Window
        self.win = visual.Window(
            size=[128,128], pos=[50,50], 
            monitor="testMonitor", allowGUI=False,
            autoLog=False
        )
        
        # create an instance of the class to test
        self.obj = ExampleVisualStim(
            self.win, units="height", name="testExampleStim", autoLog=True
        )

        # as this stimulus doesn't actually draw, mark it as not using any of the standard color attributes
        self.borderUsed = self.fillUsed = self.foreUsed = False
        # if we were to test a color, we'd need to specify which pixel on the window (from top left) we expect to be that color
        self.borderPoint = (16, 16)
        self.fillPoint = (32, 32)
        self.forePoint = (64, 64)
    
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


