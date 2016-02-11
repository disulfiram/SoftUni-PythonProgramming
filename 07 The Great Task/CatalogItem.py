class CatalogItem:
    """def __init__(self, id, name, colors, group, sport, category, subcategory, sex):
        self.id = id
        self.name = name
        self.colors = colors.split(str="/")
        self.group = group
        self.sport = sport
        self.category = category
        self.subcategory = subcategory
        self.sex = sex"""

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.id = kwargs["id"]
            self.name = kwargs["name"]
            self.colors = kwargs["colors"].split(str="/")
            self.group = kwargs["group"]
            self.sport = kwargs["sport"]
            self.category = kwargs["category"]
            self.subcategory = kwargs["subcategory"]
            self.sex = kwargs["sex"]
        elif len(args) > 0:
            arguments = args[0]
            self.id = arguments[0]
            self.name = arguments[1]
            self.colors = arguments[2].split("/")
            self.group = arguments[3]
            self.sport = arguments[4]
            self.category = arguments[5]
            self.subcategory = arguments[6]
            self.sex = arguments[7]
