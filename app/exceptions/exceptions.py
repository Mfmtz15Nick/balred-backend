class CustomError(Exception):
    status_code = 400

    def __init__(self, message=None):
        super().__init__(message)
        self.message = message
    
    def to_dict(self):
        return { 'message': self.message or 'An error ocurred' }