from time import process_time, sleep

def timepassed(func):
    def nested():
        # start the timer
        # do func
        # end the timer
        # end minus start -> result
        # return result

        start = process_time()
        func()
        end = process_time()
        result = end - start
        print(result)
    return nested

@timepassed
def example_function():
    print('Start')
    sleep(50)
    print('Koniec')


@timepassed
def example_2():
    var = 4 + 5
    return var * 400



example_2()
