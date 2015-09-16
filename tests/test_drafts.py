from unittest import TestCase
from rucola import Rucola
from rucola_drafts import Drafts


class Test(TestCase):

    def test(self):

        app = Rucola()
        yes = app.create('yes.md')
        no = app.create('no.md')
        app.create('missing.md')

        yes['draft'] = True
        no['draft'] = False

        app.use(Drafts())

        self.assertIsNone(app.get('yes.md'))
        self.assertIsNotNone(app.get('no.md'))
        self.assertIsNotNone(app.get('missing.md'))
