"""
A Rucola plugin used to ignore draft pages.
"""


class Drafts:
    def __call__(self, app):

        for i in app.find('**/*'):
            if i.get('draft', False):
                app.files.remove(i)
