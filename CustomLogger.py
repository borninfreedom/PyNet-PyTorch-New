import logging
from logging.handlers import RotatingFileHandler


class CustomLogger:
    def __init__(self, log_file_path, log_level=logging.INFO):
        self.log_file_path = log_file_path
        self.log_level = log_level
        self.setup_logger()

    def setup_logger(self):
        # 定义日志格式，包括代码行信息
        log_format = '%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s'

        # 创建一个logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)

        # 创建一个handler，用于写入日志文件，使用RotatingFileHandler实现日志文件的自动轮转
        file_handler = RotatingFileHandler(self.log_file_path, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
        file_handler.setLevel(self.log_level)

        # 再创建一个handler，用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)

        # 定义handler的输出格式
        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

    # 使用示例


if __name__ == '__main__':
    log_file_path = 'my_log.log'
    log_level = logging.DEBUG  # 可以设置不同的日志级别，如 logging.INFO, logging.WARNING 等

    custom_logger = CustomLogger(log_file_path, log_level)
    logger = custom_logger.get_logger()

    # 现在可以使用logger来记录日志了
    logger.debug('This is a debug message.')
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')