from datetime import datetime
import os


def logger_with_path(path):

    def logger(foo):
        complete_path = os.path.join(path, '\log.txt')

        def new_foo(*args, **kwargs):
            log_before = f'Date and time: {datetime.now().strftime("%Y/%m/%d, %H:%M:%S")}\nName: {foo.__name__}\nArguments: {args} and {kwargs}'
            with open(complete_path, 'w') as f:
                f.write(log_before)
                result = foo(*args, **kwargs)
                result_test = f'\nResult of the function {foo.__name__}: {result}'
                f.write(result_test)
            return result

        return new_foo
    return logger