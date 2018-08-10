class SignedIntegerBaseError(Exception):
    def __init__(self, extra_message, value, signed):

        if signed:
            int_sign_designation_str = "Signed integer"
        else:
            int_sign_designation_str = "Unsigned integer"

        self.message = f"{int_sign_designation_str} {value} out of bounds: {extra_message}"

        super().__init__(self.message)


class SignedIntegerTooSmallError(SignedIntegerBaseError):
    def __init__(self, value, signed):
        extra_message = "too small"
        super().__init__(extra_message, value, signed)


class SignedIntegerTooLargeError(SignedIntegerBaseError):
    def __init__(self, value, signed):
        extra_message = "too large"
        super().__init__(extra_message, value, signed)