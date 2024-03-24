import asyncio
import y_py as Y
from websockets import connect
from ypy_websocket import WebsocketProvider
from llama_cpp import Llama
import uuid

llm = Llama(
    model_path="./models/dolphin-2.2.1-mistral-7b.Q2_K.gguf",
    # n_gpu_layers=-1, # Uncomment to use GPU acceleration
    # seed=1337, # Uncomment to set a specific seed
    # n_ctx=2048, # Uncomment to increase the context window
)

async def client():
    ydoc = Y.YDoc()
    my_id = uuid.uuid4()
    async with (
        connect("ws://localhost:1234/my-roomname") as websocket,
        WebsocketProvider(ydoc, websocket),
    ):
        todos = ydoc.get_map('todos')
        doing = ydoc.get_map('doing')
        done = ydoc.get_map('done')

        def onTodosChange(event):
            #print(event)
            print("\nTODOS:\n", todos, "\n")
            #loop over todos
            for id, task in todos.items():
                print(id, "->", task, "->", task['worker'])
                if task['worker'] is None:
                    task['worker'] = my_id
                    doing.set(id, task)
                    todos.delete(id)
                    output = llm(
                        f"Q: {task['text']} A: ",  # Prompt
                        # max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
                        # Stop generating just before the model would generate a new question
                        stop=["Q:", "\n"],
                        echo=True  # Echo the prompt back in the output
                    )  # Generate a completion, can also call create_completion
                    
                    print(output)
                    output = output.replace("Q: ", "")
                    done.set(id, task)
                    doing.delete(id)

            # output = llm(
            #     f"Q: {todos[0]} A: ",  # Prompt
            #     # max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
            #     # Stop generating just before the model would generate a new question
            #     stop=["Q:", "\n"],
            #     echo=True  # Echo the prompt back in the output
            # )  # Generate a completion, can also call create_completion
            # print(output)
        def onDoingChange(event):
            print("\nDOING:\n", doing, "\n")
        def onDoneChange(event):
            print("\nDONE:\n", done, "\n")            
 
        todos.observe(onTodosChange)
        doing.observe(onDoingChange)
        done.observe(onDoneChange)

        # with ydoc.begin_transaction() as txn:
        #     yarray.append(txn, "hello de python")

        await asyncio.Future()  # run forever

asyncio.run(client())
