import timeit
import pandas as pd
from functools import wraps


def time_decorator(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        stat_time = timeit.default_timer()
        value = func(*args, **kwargs)
        end_time = timeit.default_timer()
        run_time = end_time - stat_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


'''Calculate using vectorized operator which is faster the .apply() on the pd.Series object'''


@time_decorator
def cal_decade_using_vectorized_operators(dataset):
    year_ = dataset['Year'] // 10 * 10
    print(f"pd class name: {year_.__class__.__name__}")
    print(year_)


def decade(year):
    return year //10 *10

@time_decorator
def cal_decade_using_apply_function(dataset):
    apply = dataset['Year'].apply(decade)
    print(apply)


if __name__ == "__main__":
    csv = pd.read_csv('sources/babynames.csv')
    cal_decade_using_vectorized_operators(csv)
    cal_decade_using_apply_function(csv)
