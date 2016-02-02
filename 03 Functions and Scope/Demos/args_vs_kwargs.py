def format_with_indent(format_string, *args, indent: int=None, indent_with: str=" ", **kwargs):
    if indent is not None:
        indent_str = indent_with * indent  # will multiply the indent string
    else:
        indent_str = ""
    return indent_str + format_string.format(*args, **kwargs)

...

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer'))

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer', indent=4))

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer', indent=4, indent_with='-'))