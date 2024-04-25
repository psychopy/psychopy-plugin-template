"""
Tests for the ExampleComponent class, essentially showcases how to implement basic tests on a Component.
"""

from psychopy_plugin_template.components.exampleComponent import ExampleComponent
from psychopy_plugin_template.visual.exampleVisualStim import ExampleVisualStim
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestExampleComponent(BaseComponentTests, _TestLibraryClassMixin):
    """
    Creating a subclass of BaseComponentTests means that your testing class will inherit all of its methods - and will therefore run its tests on your Component. Just make sure to specify the Component class in the class attributes.

    The test_base_components module also includes some "Mixin" classes which add attributes and methods for further tests which may not be relevant to all Components. In this example I've included _TestLibraryClassMixin, which adds tests that the library class which the plugin writes code for (e.g. ImageStim for ImageComponent, TextStim for TextComponent, etc.) is setup correctly for use with a Component.

    Attributes
    ----------`
    comp : type
        Component class to run tests on
    libraryClass : type
        Class in the library which this Component writes code for
    """
    comp = ExampleComponent
    libraryClass = ExampleVisualStim

    # --- Tests ---

    def test_example(self):
        """
        You can add additional tests by adding methods to this class - remember that you can get the Component class via `self.comp`
        """
        pass
