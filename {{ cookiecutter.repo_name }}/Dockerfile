FROM melioconsulting/jupyterlab-nlp:latest
LABEL maintainer='Merelda Wu'

USER root

# RUN apt-get update && apt-get install -y krb5-user=1.16-2ubuntu0.1
RUN pip install pympler joblib --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade

ARG HTTP_PROXY
ARG HTTPS_PROXY
RUN echo "HTTP_PROXY: $HTTP_PROXY"
RUN git config --global http.proxy ${HTTP_PROXY}
RUN git config --global https.proxy $HTTPS_PROXY

WORKDIR /app
RUN pip install git+https://github.com/melio-consulting/hana2py.git --upgrade

COPY config/run.sh /app/run.sh
COPY config/krb5.conf /etc/krb5.conf
COPY config/plugin.jupyterlab-settings  /opt/play/config/plugin.jupyterlab-settings
COPY config/commands.jupyterlab-settings /opt/play/config/commands.jupyterlab-settings
COPY config/jupyter_notebook_config.py /opt/play/config/jupyter_notebook_config.py 
COPY config/start.py /opt/play/config/start.py
RUN chmod +x /app/run.sh 
RUN /app/run.sh
