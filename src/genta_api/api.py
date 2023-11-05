import requests

from typing import Optional, List, Dict, Union

class GentaAPI:
    """
    # GentaAPI

    GentaAPI is a Python wrapper for Genta API.

    Args:
        token (str): token from https://genta.tech/

    Examples:
        >>> from genta_api import GentaAPI
        >>> api = GentaAPI(token='your-token')
        >>> api.ChatCompletion(
        ...     chat_history=[
        ...         { "role": "user", "text": "Hello, how are you?" },
        ...         { "role": "assistant", "text": "I'm fine, thank you." },
        ...         { "role": "user", "text": "That's good to hear." },
        ...     ],
        ...     model_name='Starstreak',
        ...     best_of=1,
        ...     decoder_input_details=True,
        ...     details=True,
        ...     do_sample=True,
        ...     max_new_tokens=128,
        ...     repetition_penalty=1.03,
        ...     return_full_text=False,
        ...     seed=None,
        ...     stop=[],
        ...     temperature=0.7,
        ...     top_k=50,
        ...     top_n_tokens=None,
        ...     top_p=0.95,
        ...     truncate=None,
        ...     typical_p=0.95,
        ...     watermark=False,
        ... )
        ... (200, {
        ...     "generated_text": "Hello, how are you?",
        ... })
    """

    CHAT_URL = "https://api.genta.tech/chat/"
    TEXT_URL = "https://api.genta.tech/text/"

    def __init__(self, token: str):
        self.token = token

    def ChatCompletion(
        self,
        chat_history: List[Dict[str, str]],
        model_name: str = 'Starstreak',
        best_of: Optional[int] = 1,
        decoder_input_details: Optional[bool] = True,
        details: Optional[bool] = True,
        do_sample: Optional[bool] = True,
        max_new_tokens: Optional[int] = 128,
        repetition_penalty: Optional[float] = 1.03,
        return_full_text: Optional[bool] = False,
        seed: Optional[int] = None,
        stop: Optional[List[str]] = [],
        temperature: Optional[float] = 0.7,
        top_k: Optional[int] = 50,
        top_n_tokens: Optional[int] = None,
        top_p: Optional[float] = 0.95,
        truncate: Optional[int] = None,
        typical_p: Optional[float] = 0.95,
        watermark: Optional[str] = False,
    ) -> Union[Dict[str, str], int]:
        """
        ## ChatCompletion
        
        Create a chatbot response from chat history and parameters to the model name.

        Args:
            chat_history (List[Dict[str, str]]): chat history
            model_name (str, optional): model name. Defaults to 'Starstreak'.
            best_of (Optional[int], optional): number of samples to generate. Defaults to 1.
            decoder_input_details (Optional[bool], optional): include decoder input details. Defaults to True.
            details (Optional[bool], optional): include details. Defaults to True.
            do_sample (Optional[bool], optional): sample or greedy decoding. Defaults to True.
            max_new_tokens (Optional[int], optional): maximum number of tokens to generate. Defaults to 128.
            repetition_penalty (Optional[float], optional): repetition penalty. Defaults to 1.03.
            return_full_text (Optional[bool], optional): return full text. Defaults to False.
            seed (Optional[int], optional): random seed. Defaults to None.
            stop (Optional[List[str]], optional): stop token. Defaults to [].
            temperature (Optional[float], optional): temperature. Defaults to 0.7.
            top_k (Optional[int], optional): top k sampling. Defaults to 50.
            top_n_tokens (Optional[int], optional): top n tokens. Defaults to None.
            top_p (Optional[float], optional): top p sampling. Defaults to 0.95.
            truncate (Optional[int], optional): truncate. Defaults to None.
            typical_p (Optional[float], optional): typical p. Defaults to 0.95.
            watermark (Optional[str], optional): watermark. Defaults to False.

        Raises:
            ValueError: chat_history must be list of dict with role key: user, assistant, system

        Returns:
            Union[Dict[str, str], int]: response from API and status code
        """
        
        for i in chat_history:
            if chat_history['role'] not in ['user', 'assistant', 'system']:
                raise ValueError('chat_history must be list of dict with role key: user, assistant, system')
        
        data = {
            "token": self.token,
            "inputs": chat_history,
            "model_name": model_name,
            "parameters": {
                "best_of": best_of,
                "decoder_input_details": decoder_input_details,
                "details": details,
                "do_sample": do_sample,
                "max_new_tokens": max_new_tokens,
                "repetition_penalty": repetition_penalty,
                "return_full_text": return_full_text,
                "seed": seed,
                "stop": stop,
                "temperature": temperature,
                "top_k": top_k,
                "top_n_tokens": top_n_tokens,
                "top_p": top_p,
                "truncate": truncate,
                "typical_p": typical_p,
                "watermark": watermark,
            }
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(self.CHAT_URL, json=data, headers=headers)

        return response.json(), response.status_code

    def TextCompletion(
        self,
        text: str,
        model_name: str = 'Starstreak',
        best_of: Optional[int] = 1,
        decoder_input_details: Optional[bool] = True,
        details: Optional[bool] = True,
        do_sample: Optional[bool] = True,
        max_new_tokens: Optional[int] = 128,
        repetition_penalty: Optional[float] = 1.03,
        return_full_text: Optional[bool] = False,
        seed: Optional[int] = None,
        stop: Optional[List[str]] = [],
        temperature: Optional[float] = 0.7,
        top_k: Optional[int] = 50,
        top_n_tokens: Optional[int] = None,
        top_p: Optional[float] = 0.95,
        truncate: Optional[int] = None,
        typical_p: Optional[float] = 0.95,
        watermark: Optional[str] = False,
    ) -> Union[Dict[str, str], int]:
        """
        ## TextCompletion

        Create a text completion from text and parameters to the model name.

        Args:
            text (str): text
            model_name (str, optional): model name. Defaults to 'Starstreak'.
            best_of (Optional[int], optional): number of samples to generate. Defaults to 1.
            decoder_input_details (Optional[bool], optional): include decoder input details. Defaults to True.
            details (Optional[bool], optional): include details. Defaults to True.
            do_sample (Optional[bool], optional): sample or greedy decoding. Defaults to True.
            max_new_tokens (Optional[int], optional): maximum number of tokens to generate. Defaults to 128.
            repetition_penalty (Optional[float], optional): repetition penalty. Defaults to 1.03.
            return_full_text (Optional[bool], optional): return full text. Defaults to False.
            seed (Optional[int], optional): random seed. Defaults to None.
            stop (Optional[List[str]], optional): stop token. Defaults to [].
            temperature (Optional[float], optional): temperature. Defaults to 0.7.
            top_k (Optional[int], optional): top k sampling. Defaults to 50.
            top_n_tokens (Optional[int], optional): top n tokens. Defaults to None.
            top_p (Optional[float], optional): top p sampling. Defaults to 0.95.
            truncate (Optional[int], optional): truncate. Defaults to None.
            typical_p (Optional[float], optional): typical p. Defaults to 0.95.
            watermark (Optional[str], optional): watermark. Defaults to False.

        Returns:
            Union[Dict[str, str], int]: response from API and status code
        """

        data = {
            "token": self.token,
            "inputs": text,
            "model_name": model_name,
            "parameters": {
                "best_of": best_of,
                "decoder_input_details": decoder_input_details,
                "details": details,
                "do_sample": do_sample,
                "max_new_tokens": max_new_tokens,
                "repetition_penalty": repetition_penalty,
                "return_full_text": return_full_text,
                "seed": seed,
                "stop": stop,
                "temperature": temperature,
                "top_k": top_k,
                "top_n_tokens": top_n_tokens,
                "top_p": top_p,
                "truncate": truncate,
                "typical_p": typical_p,
                "watermark": watermark,
            }
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(self.TEXT_URL, json=data, headers=headers)

        return response.json(), response.status_code
