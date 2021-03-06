import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor


preprocessor = create_preprocessor('xception', target_size=(299, 299))

interpreter = tflite.Interpreter(model_path='clothing-model-v4.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
input_index = input_details[0]['index']
output_details = interpreter.get_output_details()
output_index = output_details[0]['index']


def predict(x):
    interpreter.set_tensor(input_index, x)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    return preds[0]


labels = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]


def decode_predictions(pred):
    result = {c: float(p) for c, p in zip(labels, pred)}
    return result

# this function is essential for the AWS Lambda (serverless service) to be able to execute the above code.
def lambda_handler(event, context):
    url = event['url']
    x = preprocessor.from_url(url)
    preds = predict(x)
    results_dict = decode_predictions(preds)
    final_result = max(results_dict.keys(),
                       key=(lambda key: results_dict[key]))
    return final_result
