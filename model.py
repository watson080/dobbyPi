import threading
import re

class Model(object):
    def __init__(self):
        self._current_row = 3000
        self._lines = []
    
    def read_all_lines_by_line(self, wif_file_path):
        with open(wif_file_path) as wif_file:
            self._lines = wif_file.readlines()

    def convert_wif_lift_plan(self):
        for line in self._lines:
            lift_plan = self.convert_healds_number_to_output_commnad(line)
            if lift_plan is not None:
                print(lift_plan[1:])
 
    def convert_healds_number_to_output_commnad(self, line):
        line.split()
        output_command = [int(x) for x in re.split(r"[=,]", line[:-1])]
        if output_command[0] < self._current_row:
            return None
        self._current_row = output_command[0]
        return output_command
        
if __name__ == "__main__":
    model = Model()
    model.read_all_lines_by_line("./wif/20170924.wif")
    model.convert_wif_lift_plan()
