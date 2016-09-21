
class ParserError(Exception):
    """
    User defined exception for parsing a file.
    In addition to 'message', use *args to supply 'module name' and
    'line number' of where the parsing error occurred.
    """
    def __init__(self, *args):
        super(ParserError, self).__init__(args)
    
if __name__ == '__main__':
    try:
        raise ParserError()
    except ParserError as e:
        print e

    try:
        raise ParserError('Error parsing file...')
    except ParserError as e:
        print e

    try:
        raise ParserError('Error parsing file...', __name__)
    except ParserError as e:
        print e

    try:
        raise ParserError('Error parsing file...', __name__, 13)
    except ParserError as e:
        print e
