class Email:
    def __init__(self, value: str):
        if '@' not in value:
            raise ValueError('Invalid email')
        self.value = value
    def __str__(self):
        return self.value
