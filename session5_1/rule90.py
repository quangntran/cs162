import numpy as np
from template import AbstractSimulation

class Rule90(AbstractSimulation):
    def __init__(self, number_steps, size=10):
        super().__init__(number_steps)
        self.size = size
        self.arr = np.random.randint(0,2, size=self.size) # randomly choose 0 and 1

    def run_one_step(self):
        roll_right = np.roll(self.arr, 1)
        roll_left = np.roll(self.arr, -1)
        # transition
        self.arr = np.bitwise_xor(roll_right, roll_left)

    def print_sim_state(self):
        out = ''
        for i in range(self.size):
            out += '.' if not self.arr[i] else '1'
        print(out )

def main():
    rule90 = Rule90(10, size=10)
    rule90.run()

if __name__ == '__main__':
    main()
