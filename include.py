# encoding=utf-8
INNODB_PAGE_SIZE = 16 * 1024 * 1024

# Start of the data on the page
FIL_PAGE_DATA = 38

FIL_PAGE_OFFSET = 4  # page offset inside space
FIL_PAGE_TYPE = 24  # File page type

# Types of an undo log segment */
TRX_UNDO_INSERT = 1
TRX_UNDO_UPDATE = 2

# On a page of any file segment, data may be put starting from this offset
FSEG_PAGE_DATA = FIL_PAGE_DATA

# The offset of the undo log page header on pages of the undo log
TRX_UNDO_PAGE_HDR = FSEG_PAGE_DATA

PAGE_LEVEL = 26  # level of the node in an index tree; the leaf level is the level 0 */

# innodb_page_type = {
#     '0000': u'Freshly Allocated Page',
#     '0002': u'Undo Log Page',
#     '0003': u'File Segment inode',
#     '0004': u'Insert Buffer Free List',
#     '0005': u'Insert Buffer Bitmap',
#     '0006': u'System Page',
#     '0007': u'Transaction system Page',
#     '0008': u'File Space Header',
#     '0009': u'extend description page',
#     '000a': u'Uncompressed BLOB Page',
#     '000b': u'1st compressed BLOB Page',
#     '000c': u'Subsequent compressed BLOB Page',
#     '45bf': u'B-tree Node',
#     '45bd': u'Tablespace SDI Index page'
# }

innodb_page_type = {
    '0000': 'Freshly allocated',
    '0002': 'Undo log', 
    '0003': 'File segment inode', 
    '0004': 'Insert buffer free list', 
    '0005': 'Insert buffer bitmap', 
    '0006': 'System internal', 
    '0007': 'Transaction system header', 
    '0008': 'File space header', 
    '0009': 'Extent descriptor', 
    '000a': 'Uncompressed BLOB', 
    '000b': 'First compressed BLOB', 
    '000c': 'Subsequent compressed BLOB', 
    '000d': 'Unknown', 
    '000e': 'Compressed', 
    '000f': 'Encrypted', 
    '0010': 'Compressed and Encrypted', 
    '0011': 'Encrypted R-tree', 
    '0012': 'Uncompressed SDI BLOB', 
    '0013': 'Compressed SDI BLOB', 
    '0014': 'Legacy doublewrite buffer', 
    '0015': 'Rollback Segment Array', 
    '0016': 'Index of uncompressed LOB', 
    '0017': 'Data of uncompressed LOB', 
    '0018': 'First page of an uncompressed LOB', 
    '0019': 'First page of a compressed LOB', 
    '001a': 'Data of compressed LOB', 
    '001b': 'Index of compressed LOB', 
    '001c': 'Fragment of compressed LOB', 
    '001d': 'Index of fragment for compressed LOB', 
    '45bd': 'Serialized Dictionary Information', 
    '45be': 'R-tree index', 
    '45bf': 'B+Tree index'}

innodb_page_direction = {
    '0000': 'Unknown(0x0000)',
    '0001': 'Page Left',
    '0002': 'Page Right',
    '0003': 'Page Same Rec',
    '0004': 'Page Same Page',
    '0005': 'Page No Direction',
    'ffff': 'Unkown2(0xffff)'
}

INNODB_PAGE_SIZE = 1024 * 16  # InnoDB Page 16K