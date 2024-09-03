# 8-14 Cars

def car_fax(manufacturer, model_name, **features):
    features['manufacturer'] = manufacturer
    features['model name'] = model_name
    return features

my_car = car_fax('kia', 'soul', engine='1.6L GDI Engine', drive_train='front-wheel drive', horsepower=130)

print(my_car)