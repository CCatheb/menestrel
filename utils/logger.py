import logging


class LoggerFormatter(logging.Formatter):

    default_formatter = "%(asctime)s - [%(levelname)s] [%(name)s]: %(msg)s"

    FORMATS = {
        logging.DEBUG: "%(asctime)s - [%(levelname)s] [%(name)s] - [%(filename)s, %(lineno)s] - [%(threadName)s]: %(msg)s",
        logging.INFO: default_formatter,
        logging.ERROR: default_formatter,
        logging.WARNING: default_formatter,
        logging.CRITICAL: default_formatter,
    }

    def format(self, record: logging.LogRecord) -> logging.LogRecord:
        """Ovreload the format function from logging.Formatter class to add custom formats

        Args:
            record (logging.LogRecord): Log Record to formatP
        Returns:
            Formatted record
        """

        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


class CustomLogger():

    @staticmethod
    def get_logger(name: str, level=logging.DEBUG) -> logging.Logger:

        # Instantiate a logger
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Add a console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(LoggerFormatter())

        if len(logger.handlers) < 1:
            logger.addHandler(ch)

        return logger
