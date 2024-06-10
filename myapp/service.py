from modules.model_modules import get_model

model = get_model("") # init by dev

def s2t_sevice(file):
  # init model
  prediction = model.predict() #######
  return file