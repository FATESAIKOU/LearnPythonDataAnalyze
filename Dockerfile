# Python データ分析学習環境
# Jupyter Notebook + NumPy + Pandas + Matplotlib

FROM python:3.11-slim

# 作業ディレクトリの設定
WORKDIR /workspace

# 必要なシステムパッケージのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-noto-cjk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python パッケージのインストール
RUN pip install --no-cache-dir \
    jupyter \
    jupyterlab \
    numpy \
    pandas \
    matplotlib \
    openpyxl \
    japanize-matplotlib

# Jupyter の設定
RUN mkdir -p /root/.jupyter
RUN echo "c.NotebookApp.ip = '0.0.0.0'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.port = 8888" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py

# ポートの公開
EXPOSE 8888

# JupyterLab の起動
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
