# genta-api
Genta Python API Package.

## Installation

This API wrapper can be installed by cloning the repository and running `pip install .` in the root directory. You can also use `pip install genta`

## Examples

You can use this module like so:

```python
from genta_api import GentaAPI
api = GentaAPI(token='your-token')
response, statusCode = api.ChatCompletion(
    chat_history=[
        { "role": "user", "text": "Hello, how are you?" },
        { "role": "assistant", "text": "I'm fine, thank you." },
        { "role": "user", "text": "That's good to hear." },
    ],
    model_name='Starstreak',
    best_of=1,
    decoder_input_details=True,
    details=True,
    do_sample=True,
    max_new_tokens=128,
    repetition_penalty=1.03,
    return_full_text=False,
    seed=None,
    stop=[],
    temperature=0.7,
    top_k=50,
    top_n_tokens=None,
    top_p=0.95,
    truncate=None,
    typical_p=0.95,
    watermark=False,
)
print(response, statusCode)
```

A variety of options can be configured when calling the `ChatCompletion` method:

- `chat_history`: a list of dictionaries, each containing a "role" (user, assistant, or system) and "text".
- `model_name`: the name of the machine learning model to use. By default, it uses 'Starstreak'.
- `best_of`: an integer specifying the number of responses the model should generate. The best one will be chosen. Default is 1.
- `decoder_input_details`, `details`, `do_sample`: boolean flags to control various model behaviors.
- `max_new_tokens`: the maximum output length that the model will produce.
- `repetition_penalty`: a penalty for repetitive output. Default is 1.03.
- `return_full_text`: whether the output includes original input text as well. Default is False.
- `seed`: an integer to seed random responses.
- `stop`: a list of stop tokens.
- `temperature`: a measure of randomness in the output.
- `top_k`, `top_n_tokens`, `top_p`, `truncate`, `typical_p`: control parameters for the output.
- `watermark`: whether to include a watermark in the output. Default is False.