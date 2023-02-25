def print_item(cstrt, prefix):
    for (name, classid) in cstrt._fields_:
        attr = getattr(cstrt, name)
        print(prefix + "{}, {},{}".format(name, classid, attr))
        if hasattr(attr, "_length_"):
            # member is Array of X
            if hasattr(attr[0], "_fields_"):
                # member is Array of Struct
                for atr in attr:
                    print_item(atr, prefix + "  ")
            elif hasattr(attr[0], "_length_"):
                # member is Array of Array
                print("no support for Array of Array")
            else:
                # member is Array of Scalar
                print(prefix + "  " + ', '.join(map(str, attr)))
        elif hasattr(attr, "_fields_"):
            # member is Struct
            print_item(attr, prefix + "  ")

def export_item(cstrt):
    ret = {}
    for (name, classid) in cstrt._fields_:
        attr = getattr(cstrt, name)
        if hasattr(attr, "_length_"):
            # member is Array of X
            ret[name] = []
            if hasattr(attr[0], "_fields_"):
                # member is Array of Structure
                for atr in attr:
                    ret[name].append(export_item(atr))
            elif hasattr(attr[0], "_length_"):
                # member is Array of Array
                print("no support for Array of Array")
            else:
                # member is Array of Scalar
                for atr in attr:
                    ret[name].append(int(atr))
        elif hasattr(attr, "_fields_"):
            # member is Structure
            ret[name] = export_item(attr)
        else:
            # member is Scalar
            ret[name] = int(attr)
    return ret

def import_item(cstrt, obj):
    for(name, classid) in cstrt._fields_:
        attr = getattr(cstrt, name)
        if hasattr(attr, "_length_"):
            # member is Array of X
            if hasattr(attr[0], "_fields_"):
                # member is Array of Structure
                for idx, atr in enumerate(attr):
                    import_item(atr, obj[name][idx])
            elif hasattr(attr[0], "_length_"):
                # member is Array of Array
                print("no support for Array of Array")
            else:
                # member is Array of Scalar
                for idx, atr in enumerate(attr):
                    getattr(cstrt, name)[idx] = obj[name][idx]
        elif hasattr(attr, "_fields_"):
            # member is Struct
            import_item(attr, obj[name])
        else:
            # member is Scalar
            setattr(cstrt, name, obj[name])
