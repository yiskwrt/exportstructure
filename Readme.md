# Export/Import Ctypes Structure to/from dictionary

## APIs

* print_items(ctypes.Structure instance, prefix)
  * debug print Structure members with indent
* dictionary = export_items(ctypes.Structure instance)
  * export Structure members to python dictionary
* import_items(ctypes.Structure instance, dictionary)
  * import dictionary items to Struct members

## examples

* Makefile
* examples/posix_mq/
  * YAML -> dictionary -> cstruct -> posix messagequeue -> cstruct -> dictionary -> debug print

## Limitations

* Array of Array is not supported.
* Scalar members are assumed to be integer. Currently, float is not supported.
