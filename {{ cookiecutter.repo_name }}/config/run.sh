#!/bin/bash
mkdir -p /home/jovyan/opt/play/config/
mkdir -p /home/jovyan/.jupyter/lab/user-settings/\@jupyterlab/shortcuts-extension/
mkdir -p /home/jovyan/.jupyter/lab/user-settings/\@jupyterlab/codemirror-extension/
mkdir -p /home/jovyan/.ipython/profile_default/startup/

cp /opt/play/config/plugin.jupyterlab-settings ~/.jupyter/lab/user-settings/\@jupyterlab/shortcuts-extension/
cp /opt/play/config/commands.jupyterlab-settings ~/.jupyter/lab/user-settings/@jupyterlab/codemirror-extension/
echo "$(</opt/play/config/jupyter_notebook_config.py)" >> /home/jovyan/.jupyter/jupyter_notebook_config.py
echo "$(</opt/play/config/start.py)" >> /home/jovyan/.ipython/profile_default/startup/start.py
