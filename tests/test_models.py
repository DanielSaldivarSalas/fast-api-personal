
from models import ModelName


def test_correct_enum_values_for_ModelName():

    assert ModelName.alexnet == "alexnet"
    assert ModelName.resnet == "resnet"
    assert ModelName.lenet == "lenet"
