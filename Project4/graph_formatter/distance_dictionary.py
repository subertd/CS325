class DistanceDictionary(dict):

    v = None

    def __init(self, v):
        dict.__init__(self)
        self.v = v

    def __getitem__(self, (a, b)):
        try:
            return dict.__getitem__(self, (a, b))
        except:
            return dict.__getitem__(self, (b, a))

    def __setitem__(self, (a, b), val):
        if dict.has_key(self, (b, a)):
            dict.__setitem__(self, (b, a), val)
        else:
            dict.__setitem__(self, (a, b), val)

    def start_caching(self):
        pass

    def clear_cache(self):
        pass
