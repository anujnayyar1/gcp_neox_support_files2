

from megatron.utils import print_rank_0, setup_for_inference_or_eval

from megatron.text_generation_utils import (
    generate_samples_input_from_file,
    generate_samples_from_prompt,
    generate_samples_unconditional,
    generate_samples_interactive,
)

from flask import Flask, jsonify, request

app = Flask(__name__)


# load model
model, neox_args = setup_for_inference_or_eval(use_cache=True)



@app.route('/')
def index():
	return jsonify({'we await': 'your json'})



# make text with a prompt
@app.route('/multi/<string:input_string>', methods=['GET'])
def call_model(input_string):

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


if __name__ == '__main__':
	app.run()








