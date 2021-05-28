class MyMixin:
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    @staticmethod
    def get_upper(s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()
