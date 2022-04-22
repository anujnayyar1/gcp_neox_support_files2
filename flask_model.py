

from megatron.utils import print_rank_0, setup_for_inference_or_eval

from megatron.text_generation_utils import (
    generate_samples_input_from_file,
    generate_samples_from_prompt,
    generate_samples_unconditional,
    generate_samples_interactive,
    generate_samples_from_prompt_stream
)

# load model
model, neox_args = setup_for_inference_or_eval(use_cache=True)


"""
## example which should run in python
model_output = generate_samples_from_prompt_stream(
            neox_args=neox_args,
            model=model,
            text='Anuj was having a terrible Day',
            recompute=neox_args.recompute,
            temperature=neox_args.temperature,
            maximum_tokens=neox_args.maximum_tokens,
            top_k=neox_args.top_k,
            top_p=neox_args.top_p,
        )


"""






from flask import Flask, jsonify, request
from flask_sse import sse


app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')


@app.route('/')
def index():
	return jsonify({'we await': 'your json'})


@app.route('/hello')
def publish_hello():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"



# make text with a prompt
@app.route('/multi/<string:input_string>', methods=['GET'])
def call_model(input_string):

	print(f'input_string: {input_string}')
	input_string = input_string.replace('+', ' ')
	print(f'input_string: {input_string}')


    return app.response_class(
        generate_samples_from_prompt(
            neox_args=neox_args,
            model=model,
            text=input_string,  # Example: "Anuj was having a lovely Day"
            recompute=neox_args.recompute,
            temperature=neox_args.temperature,
            maximum_tokens=neox_args.maximum_tokens,
            top_k=neox_args.top_k,
            top_p=neox_args.top_p,
        ), 
        mimetype='text/event-stream')


    """
	model_output = generate_samples_from_prompt(
            neox_args=neox_args,
            model=model,
            text=input_string,  # Example: "Anuj was having a lovely Day"
            recompute=neox_args.recompute,
            temperature=neox_args.temperature,
            maximum_tokens=neox_args.maximum_tokens,
            top_k=neox_args.top_k,
            top_p=neox_args.top_p,
        )

	return jsonify({'result': model_output})
    """


if __name__ == '__main__':
	app.run()








