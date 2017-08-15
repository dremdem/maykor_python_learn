import time

def count_down(seconds, step):
    """
    Countdown
    """
    for i in range(seconds, 1, -step):
        print('%s seconds to go...' % i)
        time.sleep(step)


count_down(20, 2)

print('KABOOM!!!')

# from time import time

# def sec():
#     count = 0
#     time_now = time()
#     while True:
#         a = time() - time_now
#         if not a % 1:
#             print(count)
#         print(a)
#         count += 1  


# sec()

