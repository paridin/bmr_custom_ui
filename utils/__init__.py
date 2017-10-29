import cx_Oracle
from sqlalchemy import create_engine

def get_engine(config):
    """Get an engine using a database configuration
    Parameters
    ----------
    config : dictionary
        It must contain the properties username, password, host, port and sid
        to connect with our database
    Usage
    -----
    >>> config = {
        'username': 'smith',
        'password': 'myPassword',
        'host': '10.225.153.156',
        'port': 1521,
        'sid': 'MYSID'
    }
    >>> engine = get_engine(config)
    """
    _ = config
    tns = cx_Oracle.makedsn(_['host'], _['port'], _['sid'])
    str_ctx = 'oracle+cx_oracle://{}:{}@{}'
    return create_engine(
        str_ctx.format(_['username'], _['password'], tns),
        arraysize=4000,
        echo=False)

def get_fields_type():
    field_types = {
        0: 'PIN_FLDT_UNUSED',
        1: 'PIN_FLDT_INT',
        2: 'PIN_FLDT_UINT',       # OBSOLETE
        3: 'PIN_FLDT_ENUM',
        4: 'PIN_FLDT_NUM',        # OBSOLETE
        5: 'PIN_FLDT_STR',
        6: 'PIN_FLDT_BUF',
        7: 'PIN_FLDT_POID',
        8: 'PIN_FLDT_TSTAMP',
        9: 'PIN_FLDT_ARRAY',     # array element
        10: 'PIN_FLDT_SUBSTRUCT', # sub-type substructure
        11: 'PIN_FLDT_OBJ',       # whole object
        12: 'PIN_FLDT_BINSTR',    # (short) binary string data
        13: 'PIN_FLDT_ERR',
        14: 'PIN_FLDT_DECIMAL',
        15: 'PIN_FLDT_TIME'
    }
    #define 16: PIN_FLDT_TEXTBUF    16
    #define PIN_FLDT_ERRBUF     PIN_FLDT_ERR
    #define PIN_FLDT_LAST       16
    return field_types

def get_field_type(_id):
    """
    This function receive an `id` and try to find it 
    inner the fields types structure.
    
    Returns the name of the field, if it found otherwise returns the `id`.
    >> get_field_type(14)
    'PIN_FLDT_DECIMAL'
    """
    fields_type = get_fields_type()
    if _id in fields_type:
        return fields_type[_id]
    return _id