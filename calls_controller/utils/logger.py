import logging
from pathlib import Path

#TODO colocar em arquivo de configuracao
"""path_file = 'log'
Path(path_file).mkdir(exist_ok=True)
logging.basicConfig(filename=f'{path_file}/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
"""
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

