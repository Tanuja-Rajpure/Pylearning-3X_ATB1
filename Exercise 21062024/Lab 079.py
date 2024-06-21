import time


def note_time_taken(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time Taken is: " + str(end_time - start_time))

        return wrapper()


@note_time_taken
def logs_function():
    print("Print logs of time taken")


