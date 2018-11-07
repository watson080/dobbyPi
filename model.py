import re

class Model(object):
    def __init__(self):
        self._wif_file_path = None
        self._current_row = 0
        self._wif_file_path = ""

    def set_wif_file_path(self, wif_file_path):
        self._wif_file_path = wif_file_path

    def convert_wif_lift_plan(self):
       with open(self._wif_file_path) as wif_file:
            for line in wif_file:
                line.split()
                lift_plan = [int(x) for x in re.split(r"[=,]", line[:-1])]
                if lift_plan[0] < self._current_row:
                    continue
                self._current_row = lift_plan[0]
                print(lift_plan[1:])
                
if __name__ == "__main__":
    model = Model()
    model.set_wif_file_path("./wif/20170924.wif")
    model.convert_wif_lift_plan()
