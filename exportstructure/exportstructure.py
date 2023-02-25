def print_item(cstrt, prefix):
    def print_ary(cary, prefix):
        # Array of X
        if hasattr(cary[0], "_fields_"):
            # Array of Struct
            for atr in cary:
                print_item(atr, prefix + "  ")
        elif hasattr(cary[0], "_length_"):
            # Array of Array
            for atr in cary:
                print_ary(atr, prefix + "  ")
        else:
            # member is Array of Scalar
            print(prefix + "  " + ', '.join(map(str, cary)))

    for (name, classid) in cstrt._fields_:
        attr = getattr(cstrt, name)
        print(prefix + "{}, {},{}".format(name, classid, attr))
        if hasattr(attr, "_length_"):
            # member is Array of X
            print_ary(attr, prefix + "  ")
        elif hasattr(attr, "_fields_"):
            # member is Struct
            print_item(attr, prefix + "  ")

def export_item(cstrt):
    def export_ary(cary):
        # Array of X
        ret = []
        if hasattr(cary[0], "_fields_"):
            for atr in cary:
                ret.append(export_item(atr))
        elif hasattr(cary[0], "_length_"):
            for atr in cary:
                ret.append(export_ary(atr))
        else:
            for atr in cary:
                ret.append(int(atr))
        return ret

    ret = {}
    for (name, classid) in cstrt._fields_:
        attr = getattr(cstrt, name)
        if hasattr(attr, "_length_"):
            # member is Array of X
            ret[name] = export_ary(attr)
        elif hasattr(attr, "_fields_"):
            # member is Structure
            ret[name] = export_item(attr)
        else:
            # member is Scalar
            ret[name] = int(attr)
    return ret

def import_item(cstrt, obj):
    def import_ary(cary, obj):
        # Array of X
        if hasattr(cary[0], "_fields_"):
            # Array of Structure
            for idx, atr in enumerate(cary):
                import_item(atr, obj[idx])
        elif hasattr(cary[0], "_length_"):
            # Array of Array
            for idx, atr in enumerate(cary):
                import_ary(atr, obj[idx])
        else:
            # Array of Scalar
            for idx, atr in enumerate(cary):
                cary[idx] = obj[idx]

    for(name, classid) in cstrt._fields_:
        attr = getattr(cstrt, name)
        if hasattr(attr, "_length_"):
            # member is Array of X
            import_ary(attr, obj[name])
        elif hasattr(attr, "_fields_"):
            # member is Struct
            import_item(attr, obj[name])
        else:
            # member is Scalar
            setattr(cstrt, name, obj[name])
