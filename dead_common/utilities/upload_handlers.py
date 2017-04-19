from .basic import generate_key


def generic_upload(instance, filename, media_dirname="u"):
    name = filename.encode("utf-8").strip()
    name = name.lower()

    try:
        extension = name.split(".")[-1]
    except:
        extension = None

    name = generate_key()
    origname = name

    if extension is not None:
        name = name + "." + extension

    final = '/'.join([media_dirname, name])

    if len(final) > 200:
        final = '/'.join([media_dirname, origname])

    return final
