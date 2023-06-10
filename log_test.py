# -*- coding: utf-8 -*-
# Auther : jianlong
import logging
from ColorInfo import ColorLogger

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s [line:%(lineno)s] %(levelname)s %(message)s')
# logging.info('jianlong')

logger = ColorLogger(file='log.txt', txt=True, cover=True)
logger.info('name is {} {}'.format('Jianlong', '27'))
logger.warning('name is {} {}'.format('Jianlong', '27'))
logger.error('name is {} {}'.format('Jianlong', '27'))

