import logging

def get_logger(name: str) ->  logging.Logger:
    logger = logging.getLogger(name) # Установка нового логгера

    logger.setLevel(logging.DEBUG) # Установка уровня логирования

    handler = logging.StreamHandler() # Устанавливаем стримхендлер (будет писать в консоль)
    handler.setLevel(logging.DEBUG) # Уровень логирования стримхендлера

    formator = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    handler.setFormatter(formator) # Добавление форматера в хендлер
    logger.addHandler(handler) # Добавление хендлера в логгер

    return logger


