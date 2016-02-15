from wtforms.utils import unset_value


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
        json_input = self.get_json_input(field)
        if json_input is not unset_value:
            return json_input

        return unset_value

    def get_json_input(self, field):
        if self.json_input is not None and field.short_name in self.json_input:
            return self.json_input[field.short_name]
        return unset_value

    def get_model_input(self, field):
        if self.model is not None:
            return getattr(self.model, field.short_name, unset_value)

    def get_default(self, field):
        if field.short_name in self.defaults:
            return self.defaults[field.short_name]
        else:
            return unset_value

    # -- Legacy support functionality

    def __contains__(self, key):
        if self.form_input is None:
            return False
        return key in self.form_input

    def __iter__(self):
        if self.form_input is None:
            return iter(())
        return iter(self.form_input)

    def getlist(self, key):
        if self.form_input is None:
            return None
        return self.form_input.getlist(key)
