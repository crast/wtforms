

class FormInput(object):
    """
    Basic input wrapper class.
    """
    def __init__(self, form_input, json_input, model, defaults):
        self.form_input = form_input
        self.json_input = json_input
        self.model = model
        self.defaults = defaults

    def get_input(self, field):
        """
        Get basic input, for most simple fields.

        This is an abstraction on
        """
        if self.form_input is not None:
            valuelist = self.form_input.getlist(field.name)
            if valuelist:
                return valuelist[0]
            else:
                return None
        if self.json_input is not None:
            return self.json_input[field.short_name]

    def get_model_data(self, field):
        return getattr(self.obj, field.short_name)

    def get_default(self, field):
        if field.short_name in self.defaults:
            return self.defaults[field.short_name]
        else:
            return field.default  # XXX TODO
