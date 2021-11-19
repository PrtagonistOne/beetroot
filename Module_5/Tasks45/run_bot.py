from bot_app import run_bot
from config.init_logging import init_logging
from config.loggers import get_core_logger


def main():
    init_logging(
        # is_verbose=True,
    )

    get_core_logger().info('bot.start')

    run_bot()

    get_core_logger().info('bot.finish')


if __name__ == '__main__':
    main()