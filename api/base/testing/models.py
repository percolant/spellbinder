from django.db import models


class BaseModelTest:
    model: models.Model = None  # model class

    def test_issubclass_model(self):  # is it a subclass of model?
        assert issubclass(self.model, models.Model)
