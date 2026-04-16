import cProfile

def my_function():
    print('good')
    # Your Python code here

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    my_function()
    profiler.disable()
    profiler.print_stats()
