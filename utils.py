import inspect
import time


def timing_log(func):
    def wrapped_func(*args, **kwargs):
        if inspect.iscoroutinefunction(func):
            # Handle async function
            async def async_wrapped_func(*args, **kwargs):
                start_time = time.perf_counter()
                result = await func(*args, **kwargs)
                end_time = time.perf_counter()
                print(f"time taken running async {func.__name__} took {end_time - start_time}")
                return result

            return async_wrapped_func(*args, **kwargs)


        start_time = time.perf_counter()

        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"time taken running {func.__name__} took {end_time-start_time} seconds")

    return wrapped_func