# 'spawn_model' Package
This repository is arrangement of objects on Gazebo.

*   Maintainer: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).
*   Author: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).

**Content:**

*   [Preparation](#preparation)
*   [Execution](#execution)
*   [Files](#files)
*   [References](#References)


## Preparation
You need to set parameter and filepath, etc in `__init__.py`.
The following are the items to set.

* Object file path
* Object file name
* Object list
* Target place name, position (you need to check the position which show placement of objects.)


## Execution
`roslaunch spawn_model spawn_model_default.launch`

"Please input word: spawn or delete" will appear on the terminal,  
so enter "spawn" to place it and "delete" to delete it.

## Files
 - `README.md`: Read me file (This file)

 - `spawn_model_default.launch`
 
 - `spawn_object_model.py`

 - `__init__.py`: Code for initial setting (PATH and parameters)
 

