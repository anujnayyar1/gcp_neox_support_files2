

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


# stream_tokens()  # makes an iterator producing text completions
# generate_samples_from_prompt() uses stream_tokens()
# format is 'for (inputs) in stream_tokens(inputs): do something'

# that 'do something' is this code in 'interactive' mode
if mpu.get_model_parallel_rank() == 0:
    generated_tokens = (
        batch_context_tokens[0]
        .cpu()
        .numpy()
        .tolist()[
            batch_token_generation_start_index[0]
            .item() : batch_token_generation_end_index[0]
            .item()
        ]
    )
    generated_text = neox_args.tokenizer.detokenize(generated_tokens)
    print_rank_0("Generated Text: " + generated_text)








from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/')
def index():
	return jsonify({'we await': 'your json'})



# make text with a prompt
@app.route('/multi/<string:input_string>', methods=['GET'])
def call_model(input_string):

	print(f'input_string: {input_string}')
	input_string = input_string.replace('+', ' ')
	print(f'input_string: {input_string}')

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








