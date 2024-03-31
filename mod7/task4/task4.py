from make_dict_config import dict_config
import logging
import logging.config

# Применение dict-конфигурации
logging.config.dictConfig(dict_config)
logger = logging.getLogger('app_logger')
# Пример использования
logger = logging.getLogger('my_module')
logger.debug('Debug сообщение')
logger.error('Error сообщение')


# Применение dict-конфигурации
logging.config.dictConfig(dict_config)
logger = logging.getLogger('utils_logger')
# Пример использования
logger = logging.getLogger('my_module')
logger.debug('Debug сообщение')
logger.error('Error сообщение')