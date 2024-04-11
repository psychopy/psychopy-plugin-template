-------------------------------
ExampleComponent
-------------------------------

Example Component to show you how to make and document one.


    **Categories:** Custom
    **Works in:** PsychoPy, PsychoJS

Parameters
-------------------------------

Basic
=================

Name
    Name of this component (alphanumeric or _, no spaces)

start type
    How do you want to define your start point?
    
    Options:
    - time (s)
    - frame N
    - condition

stop type
    How do you want to define your end point?

    Options:
    - duration (s)
    - duration (frames)
    - time (s)
    - frame N
    - condition

Start
    When does the component start?

Stop
    When does the component end? (blank is endless)

Expected start (s)
    (Optional) expected start (s), purely for representing in the timeline

Expected duration (s)
    (Optional) expected duration (s), purely for representing in the timeline

Data
=================

Save onset/offset times
    Store the onset/offset times in the data file (as well as in the log file).

Sync timing with screen refresh
    Synchronize times with screen refresh (good for visual stimuli and responses based on them)

Testing
=================

Disable component
    Disable this component

