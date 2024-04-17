"""
Tests for the ExampleComponent class, essentially showcases how to implement basic tests on a Component.
"""

from psychopy_example_plugin.components.exampleComponent import ExampleComponent
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests

class TestExampleComponent(BaseComponentTests):
    """
    Creating a subclass of _TestBaseComponentsMixin means that your testing class will inherit all of its methods - and will therefore run its tests on your Component. Just make sure to specify the Component class in the class attributes.

    Attributes
    ----------`
    comp : type
        Component class to run tests on
    """
    comp = ExampleComponent

    # --- Tests ---

    def test_example(self):
        """
        You can add additional tests by adding methods to this class - remember that you can get the Component class via `self.comp`
        """
        pass
