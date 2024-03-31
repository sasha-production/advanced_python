import logging_tree
from mod7.apps import logger
with open('logging_tree.txt', encoding='utf-8', mode='w') as file:
    file.write(logging_tree.format.build_description())