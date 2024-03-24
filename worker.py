import asyncio
import y_py as Y
from websockets import connect
from ypy_websocket import WebsocketProvider
from llama_cpp import Llama

llm = Llama(
    model_path="./models/dolphin-2.2.1-mistral-7b.Q2_K.gguf",
    # n_gpu_layers=-1, # Uncomment to use GPU acceleration
    # seed=1337, # Uncomment to set a specific seed
    # n_ctx=2048, # Uncomment to increase the context window
)

async def client():
    ydoc = Y.YDoc()
    async with (
        connect("ws://localhost:1234/my-roomname") as websocket,
        WebsocketProvider(ydoc, websocket),
    ):

        def callback(event):
            print(yarray)
            output = llm(
                f"Q: {yarray[0]} A: ",  # Prompt
                # max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
                # Stop generating just before the model would generate a new question
                stop=["Q:", "\n"],
                echo=True  # Echo the prompt back in the output
            )  # Generate a completion, can also call create_completion
            print(output)

        yarray = ydoc.get_array("my-array")
        yarray.observe(callback)

        with ydoc.begin_transaction() as txn:
            yarray.append(txn, "hello de python")

        await asyncio.Future()  # run forever

asyncio.run(client())
