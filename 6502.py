from ByteInteger import ByteInteger
from ArithmeticLogic import add


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

    def __load(self, register, new_value):

        byte_int = ByteInteger(new_value)
        self.registers[register] = byte_int
        # TODO write abstract flag setting method.
        self.flags["negative"] = True if byte_int.signed else False
        self.flags["zero"] = True if byte_int.value == 0 else False

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
        self.flags["negative"] = True if self.registers[destination].signed else False
        self.flags["zero"] = True if self.registers[destination].value == 0 else False

    def transfer_a_to_x(self):
        self.__transfer("accumulator", "index_x")

    def transfer_x_to_a(self):
        self.__transfer("index_x", "accumulator")

    def transfer_a_to_y(self):
        self.__transfer("accumulator", "index_y")

    def transfer_y_to_a(self):
        self.__transfer("index_y", "accumulator")


proc = Sixty502()

a = ByteInteger(255)
b = ByteInteger(255)
c = ByteInteger(add(a, b))
print(c)
