class InvalidAmountError(Exception):
    """Raised when the amount is less than or equal to zero."""
    pass


class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    pass