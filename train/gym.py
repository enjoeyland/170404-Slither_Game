import os
import platform
import random
import threading
import time
from itertools import count

# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
# from memory_profiler import profile

# sys.path.append(r"C:\joey\workplace\2017\Computer\pygame\Slither_Game")

import mainForTraining
from train.env import Environment


class Gym(object):
    _ids = count(0)

    def make(self, gameName = "slither_game_v0", *args, **kwargs):
        self._id = next(self._ids)
        server_address = ''
        if platform.system() == "Windows":
            server_address = ('localhost', random.randint(2000,4000))
        elif platform.system() == "Linux":
            server_address = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/socket_address/socket_%s'% random.randint(0,4000)))
        gameThread = threading.Thread(name = ("SlitherGame%s" % self._id), target = mainForTraining.main, args = (server_address, ))
        gameThread.daemon = True
        gameThread.start()
        time.sleep(0.1)
        return Environment(server_address)

if __name__ == "__main__":
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))

    gym = Gym()
    env_num = 2
    envs = [gym.make() for _ in range(env_num)]
    actions = [1] * env_num
    dones = [False] * env_num
    for i, env in enumerate(envs):
        env.reset()
    # from pympler.tracker import SummaryTracker
    # tracker = SummaryTracker()
    c = 0
    while c < 1000:
        # actions = [random.randint(0,envs[0].action_space.n) for _ in range(env_num)]
        actions  =[1] * env_num
        for i, env in enumerate(envs):
            if not dones[i]:
                ob, reward, done, info = env.step(actions[i])
            else:
                ob, reward, done, info = env.reset(), 0, False, None
            dones[i] = done
        c += 1
        # print(threading.enumerate())
    # tracker.print_diff()