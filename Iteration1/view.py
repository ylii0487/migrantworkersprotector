# -----------------------------------------------------------------------------
# This class loads html files from the "template" directory and formats them using Python.
# -----------------------------------------------------------------------------
from flask import Flask, render_template_string
class View():

    def __init__(self,
                 template_path="templates/",  # Path to template files
                 template_extension=".html",  # Extension of templates, self can be overridden
                 **kwargs):  # Used to pass any global format arguments
        self.template_path = template_path
        self.template_extension = template_extension
        self.global_renders = kwargs

    def __call__(self, *args, **kwargs):
        return self.load_and_render(*args, **kwargs)

    def load_template(self, filename):
        path = self.template_path + filename + self.template_extension
        file = open(path, 'r')
        text = ""
        for line in file:
            text += line
        file.close()
        return text

    # Just calls the format method as appropriate
    def simple_render(self, template, **kwargs):
        template = render_template_string(template, **kwargs)
        return template

    def render(self, template, **kwargs):
        keys = self.global_renders.copy()
        keys.update(kwargs)
        template = self.simple_render(template, **keys)
        return template

    def load_and_render(self, filename, header="header", tailer="tailer", **kwargs):
        template = self.load_template(filename)
        rendered_template = self.render(template, **kwargs)
        rendered_template = self.load_template(header) + rendered_template
        rendered_template = rendered_template + self.load_template(tailer)
        return rendered_template
