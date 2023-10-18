from src.easy_logger import Logger

logger = Logger()


def foo_print(text: str):
    logger.add_log(text)


def foo_print_off(text: str):
    """ Do not show message in terminal but write in file"""
    logger.add_log(text, print_it=False)


def foo_event(text: str):
    logger.event(text)


def foo_exception(text: str):
    try:
        test_list = []

        test = test_list[1]

    except Exception as ex:
        logger.exception(f"{text}:{ex}")


if __name__ == "__main__":
    foo_print("test_1")
    foo_print_off("test_2")
    foo_event("test_3")
    foo_exception("test_exception")
