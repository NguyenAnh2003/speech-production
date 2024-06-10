import torch


def _get_pretrained_model(model_name: str, use_nemo: bool):
    pass


def get_model(is_pretrained: bool):
	model = None
	if is_pretrained:
		model = _get_pretrained_model("", False)
	else:
		model = torch.load()
	return model