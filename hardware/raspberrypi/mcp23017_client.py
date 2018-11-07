
import wiringpi2

class MCP_23017_Client(object):
    def __init__(self):
        self._num_of_healds = 32
        self._action_pattern = [0] * self._num_of_heald
        self._i2c_addr = [0x20, 0x21]
        self._solenoid_gpio_table = [88,87,86,85,84,83,82,81,89,90,91,92,93,94,95,96,72,71,70,69,68,67,66,65,73,74,75,76,77,78,79,80]

        self._pin_base_0 = 65
        self._pin_base_1 = 81

        wiringpi2.wiringpPiSetup()
        wiringpi2.mcp23017Setup(self._pin_base_0, self._i2c_addr[0])
        wiringpi2.mcp23017Setup(self._pin_base_1, self._i2c_addr[2])

        for pin in self._solenoid_gpio_table:
            wiringpi2.pinMode(pin, 1)
            wiringpi2.digitalWrite(pin, 0)

    @property
    def action_pattern(self):
        return self._action_pattern
    
    @action_pattern.setter
    def action_pattern(self, action_pattern_list):
        self._action_pattern = action_pattern_list
    
    def output_action_pattern_to_healds(self):
        for pin, state in enumerate(self._action_pattern):
            wiringpi2.digitalWrite(self._solenoid_gpio_table[pin], state)
            wiringpi2.delay(20)
        self._action_pattern = [0] * self._num_of_heald

    def reset_state_of_healds(self):
        for pin in self._solenoid_gpio_table:
            wiringpi2.digitalWrite(pin, 0)



    

