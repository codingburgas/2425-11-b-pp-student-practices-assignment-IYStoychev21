from tortoise import fields, models
from tortoise.fields.base import CASCADE

class HyperParams(models.Model):
    id = fields.IntField(pk=True)
    epochs = fields.IntField(default=0.0)
    learning_rate = fields.FloatField(default=0.001)

    class Meta:
        table = "hyper_params"


class TestTrainSplit(models.Model):
    id = fields.IntField(pk=True)
    testing = fields.FloatField(default=0.2)
    training = fields.FloatField(default=0.8)

    class Meta:
        table = "test_train_split"

class Params(models.Model):
    id = fields.IntField(pk=True)
    weights = fields.JSONField(default=list[list])
    bias = fields.FloatField(default=0.0)
    x_mean = fields.JSONField(default=list)
    x_std = fields.JSONField(default=list)

    class Meta:
        table = "params"

class ModelMetrics(models.Model):
    id = fields.IntField(pk=True)
    accuracy = fields.FloatField(default=0.0)
    precision = fields.FloatField(default=0.0)
    recall = fields.FloatField(default=0.0)
    f1_score = fields.FloatField(default=0.0)
    confusion_matrix = fields.JSONField(default=list[list])

    class Meta:
        table = "model_metrics"


class Models(models.Model):
    id = fields.IntField(pk=True)
    hyper_params = fields.ForeignKeyField(
            "models.HyperParams",
            related_name="models",
            on_delete=CASCADE,
        )
    test_train_split = fields.ForeignKeyField(
            "models.TestTrainSplit",
            related_name="models",
            on_delete=CASCADE,
        )
    params = fields.ForeignKeyField(
            "models.Params",
            related_name="models",
            on_delete=CASCADE,
        )
    model_metrics = fields.ForeignKeyField(
            "models.ModelMetrics",
            related_name="models",
            on_delete=CASCADE,
        )

    class Meta:
        table = "models"
