
The purpose of this repo is to give prospective plugin creators a starting point in the form of a minimal, working plugin to copy and edit rather than having to start from scratch.

## Setting up a dev environment


## Writing your plugin code
In general, how you write the Python code for your plugin is completely up to you! A plugin is ultimately just a normal Python package with some extra stuff (entry points) telling it how to interact with PsychoPy. The code in the folder [psychopy_plugin_template](psychopy_plugin_template/) (which you'll need to rename to the name you want your plugin to be imported as) gives an example structure and examples of a new Component, a new Standalone Routine and some new hardware and visual classes. Feel free however to start fully from scratch in whatever format you like!

## Setting up your pyproject.toml
The file [pyproject.toml](pyproject.toml) tells Python's packaging system what to do with your plugin - what to call it, what version it's on, who to list as author, what to put where in PsychoPy, etc.

The `pyproject.toml` for this repo is set up with details for the `psychopy-plugin-template` package, so you'll need to change the following values:
- **name**: Replace with the name you want your plugin to be installed by (should begin with `psychopy-` still)
- **version**: What version your plugin is on - if you're just starting it, this will be `0.0.0`. See [here](https://www.geeksforgeeks.org/introduction-semantic-versioning/) for more information about version number guidelines.
- **description**: Replace this with a description of your plugin telling users what it does.
- **authors**: Give yourself credit for your work! List your name and email here (you can remove OST Science Team)
- **dependencies**: If you need any Python packages which don't already come with PsychoPy, list them here and they'll be installed when users install your plugin
- **project.urls**: Once you've set up documentation (we'll get to that later), you'll need to replace the links here with links to your docs
- **project.entry-points."..."**: Entry points tell Python to pretend that parts of your plugin are in PsychoPy. We'll set these up later, but just be aware that all these values are going to change.

## Installing your plugin to test
Once you have some code you'd like to test out, and once your `pyproject.toml` is set up, you can do what's called an "editable install". Essentially, install your plugin from the folder it's in rather than from the usual installation process.

## Publishing your plugin to PyPi
Once you're happy that your plugin works, it's time to publish! As your project is already on GitHub, users could install it using `pip install git+https://github.com/<your username>/<plugin repo name>@<branch>`, but if you want it to appear in the packages search panel then it needs to be uploaded to PyPi - the go-to repository for Python packages. This repository is already set up with automatic publishing, so you just need to set up a few things to give permission.

### Create a `pypi` account
If you don't already have one, go to [PyPi.org](https://pypi.org) and create an account. They need to know who's publishing before letting you publish!

### Add a "trusted publisher" on PyPi
PyPi needs to know that your plugin repo is associated with your PyPi account, and the easiest way to do this is to add it as a "trusted publisher":
- Go to your account settings and select the "Publishing" tab
- Scroll down to the "Add a new pending publisher" and make sure the "GitHub" tab is selected
- Fill in the fields as instructed, the "Workflow name" needs to be `pypi.yaml` and the "Environment name" needs to be `pypi`
If you're setting up auto publishing for a project you've already created, you can find the same interface in the settings for that project rather than your user account and fill it out in the same way.

### Create an environment on GitHub
The "trusted publisher" form asked for the name of a GitHub environment, didn't it? Well, in order for it to work, there needs to be an environment by that name!
- Go to the settings for your plugin repo on GitHub
- Go to "Environments" from the tabs on the left side
- Click "New environment"
- Enter the name as `pypi`
- Click "Configure environment"
The default settings should do just fine, so you once you've created the environment there's no more you need to do (unless you want to of course)

### Create a "Release" on GitHub
Once you've done the previous steps, your repo is configured to automatically publish to PyPi whenever you make a new release on GitHub. So to publish, just go to "Releases" and click "New Release". Make sure you've updated the version number in your `pyproject.toml` file (as PyPi only lets you upload each numbered version once), and set the "tag" for this release to be that version number. Write some text to describe your plugin (see the releases of this repo for guidance) and then just click publish, the rest should work by magic!
