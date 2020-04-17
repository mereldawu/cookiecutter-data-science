#!/bin/bash
mkdir -p /home/jovyan/opt/app/config/
mkdir -p /home/jovyan/.jupyter/lab/user-settings/\@jupyterlab/shortcuts-extension/
mkdir -p /home/jovyan/.jupyter/lab/user-settings/\@jupyterlab/codemirror-extension/
mkdir -p /home/jovyan/.ipython/profile_default/startup/

cp /opt/app/config/plugin.jupyterlab-settings ~/.jupyter/lab/user-settings/\@jupyterlab/shortcuts-extension/
cp /opt/app/config/commands.jupyterlab-settings ~/.jupyter/lab/user-settings/@jupyterlab/codemirror-extension/
cp /opt/app/config/.pylintrc ~/opt/app/.pylintrc
echo "$(</opt/app/config/jupyter_notebook_config.py)" >> /home/jovyan/.jupyter/jupyter_notebook_config.py
