# testing_rpy

Personal repository to test [my fork](https://github.com/DuncDennis/reservoirpy) of the 
[ReservoirPy package](https://github.com/reservoirpy/reservoirpy). 

If changes are made to my local clone of the fork, reinstall the package in the venv via 
```
pip install -e path/to/local/clone
```

**Note:** 
When using PyCharm, in order to have complete indexing for _reservoirpy_, the reservoirpy-directory
has to be added to the project sources 
(see [here](https://youtrack.jetbrains.com/issue/PY-976/Unresolved-references-to-editable-packages-pip-install-e-after-installing-before-restart-due-to-.egg-link-and-new-entries-in)).
This can be done via `File | Settings | Project: testing_rpy | Project Structure | + Add Content Root`. 
