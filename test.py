# InnoDB Page Type constants from include/fil0fil.h.
PAGE_TYPE = {
    "ALLOCATED": {
        "value": 0,
        "description": "Freshly allocated",
    },
    "UNDO_LOG": {
        "value": 2,
        "description": "Undo log",
    },
    "INODE": {
        "value": 3,
        "description": "File segment inode",
    },
    "IBUF_FREE_LIST": {
        "value": 4,
        "description": "Insert buffer free list",
    },
    "IBUF_BITMAP": {
        "value": 5,
        "description": "Insert buffer bitmap",
    },
    "SYS": {
        "value": 6,
        "description": "System internal",
    },
    "TRX_SYS": {
        "value": 7,
        "description": "Transaction system header",
    },
    "FSP_HDR": {
        "value": 8,
        "description": "File space header",
    },
    "XDES": {
        "value": 9,
        "description": "Extent descriptor",
    },
    "BLOB": {
        "value": 10,
        "description": "Uncompressed BLOB",
    },
    "ZBLOB": {
        "value": 11,
        "description": "First compressed BLOB",
    },
    "ZBLOB2": {
        "value": 12,
        "description": "Subsequent compressed BLOB",
    },
    "UNKNOWN": {
        "value": 13,
        "description": "Unknown",
    },
    "COMPRESSED": {
        "value": 14,
        "description": "Compressed",
    },
    "ENCRYPTED": {
        "value": 15,
        "description": "Encrypted",
    },
    "COMPRESSED_AND_ENCRYPTED": {
        "value": 16,
        "description": "Compressed and Encrypted",
    },
    "ENCRYPTED_RTREE": {
        "value": 17,
        "description": "Encrypted R-tree",
    },
    "SDI_BLOB": {
        "value": 18,
        "description": "Uncompressed SDI BLOB",
    },
    "SDI_ZBLOB": {
        "value": 19,
        "description": "Compressed SDI BLOB",
    },
    "LEGACY_DBLWR": {
        "value": 20,
        "description": "Legacy doublewrite buffer",
    },
    "RSEG_ARRAY": {
        "value": 21,
        "description": "Rollback Segment Array",
    },
    "LOB_INDEX": {
        "value": 22,
        "description": "Index of uncompressed LOB",
    },
    "LOB_DATA": {
        "value": 23,
        "description": "Data of uncompressed LOB",
    },
    "LOB_FIRST": {
        "value": 24,
        "description": "First page of an uncompressed LOB",
    },
    "ZLOB_FIRST": {
        "value": 25,
        "description": "First page of a compressed LOB",
    },
    "ZLOB_DATA": {
        "value": 26,
        "description": "Data of compressed LOB",
    },
    "ZLOB_INDEX": {
        "value": 27,
        "description": "Index of compressed LOB",
    },
    "ZLOB_FRAG": {
        "value": 28,
        "description": "Fragment of compressed LOB",
    },
    "ZLOB_FRAG_ENTRY": {
        "value": 29,
        "description": "Index of fragment for compressed LOB",
    },
    "SDI": {
        "value": 17853,
        "description": "Serialized Dictionary Information",
    },
    "RTREE": {
        "value": 17854,
        "description": "R-tree index",
    },
    "INDEX": {
        "value": 17855,
        "description": "B+Tree index",
    },
}

innodb_page_type = {}

for page_type in PAGE_TYPE:
    ret = PAGE_TYPE[page_type]
    value_hex = ret['value'].to_bytes(2,byteorder='big').hex()
    desp = ret['description']
    innodb_page_type[value_hex] = desp

print(innodb_page_type)