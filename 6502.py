from ByteInteger import ByteInteger


class Sixty502:

    def __init__(self):

        self.registers = {
            "program_counter": 0,
            "stack_pointer": 0,
            "accumulator": 0,
            "index_x": 0,
            "index_y": 0
        }

        self.flags = {
            "carry": False,
            "zero": False,
            "interrupt_disable": False,
            "decimal": False,
            "break": False,
            "overflow": False,
            "negative": False
        }

        self.memory = [0] * 256

        self.stack = [0] * 256

    def __repr__(self):

        register_status = "\nregister status: \n"
        for key, value in self.registers.items():
            register_status += f"\t{key}: {value}\n"

        flag_status = "\nflag status: \n"
        for key, value in self.flags.items():
            flag_status += f"\t{key}: {value}\n"

        memory_status = "\nmemory status: \n"

        for address, value in enumerate(self.memory):
            if value != 0:
                memory_status += f"\t{address}: {value}\n"

        return register_status + flag_status + memory_status

    def __update_flag_value(self, new_flag_values):

        for key, value in new_flag_values.items():
            self.flags[key] = value

    def update_negative_flag(self, new_value):

        self.__update_flag_value({"negative": new_value})

    def update_zero_flag(self, new_value):

        if new_value == 0:
            self.__update_flag_value({"zero": True})
        else:
            self.__update_flag_value({"zero": False})

    def update_carry_flag(self, new_value):

        self.__update_flag_value({"carry": new_value})

    def update_interrupt_disable_flag(self, new_value):

        self.__update_flag_value({"interrupt_disable": new_value})

    def update_decimal_flag(self, new_value):

        self.__update_flag_value({"decimal": new_value})

    def update_break_flag(self, new_value):

        self.__update_flag_value({"break": new_value})

    def update_overflow_flat(self, new_value):

        self.__update_flag_value({"overflow": new_value})

    def __load(self, register, new_value):

        byte_int = ByteInteger(new_value)
        self.registers[register] = byte_int

        self.update_negative_flag(byte_int.signed)
        self.update_zero_flag(byte_int.dec_value)

    def load_accumulator(self, new_value):

        self.__load("accumulator", new_value)

    def load_index_x(self, new_value):

        self.__load("index_x", new_value)

    def load_index_y(self, new_value):

        self.__load("index_y", new_value)

    def __store(self, source, destination):

        try:
            self.memory[destination] = self.registers[source]
        except IndexError as index_error:
            print("Out of memory bound: memory location {}".format(destination))

    def store_accumulator(self, destination):

        self.__store("accumulator", destination)

    def store_index_x(self, destination):

        self.__store("index_x", destination)

    def store_index_y(self, destination):

        self.__store("index_y", destination)

    def __transfer(self, source, destination):
        self.registers[destination] = self.registers[source]

        self.update_negative_flag(self.registers[destination].signed)
        self.update_zero_flag(self.registers[destination].dec_value)

    def transfer_a_to_x(self):
        self.__transfer("accumulator", "index_x")

    def transfer_x_to_a(self):
        self.__transfer("index_x", "accumulator")

    def transfer_a_to_y(self):
        self.__transfer("accumulator", "index_y")

    def transfer_y_to_a(self):
        self.__transfer("index_y", "accumulator")


proc = Sixty502()

proc.load_accumulator(255)
print(proc)
