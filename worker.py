import asyncio
import y_py as Y
from websockets import connect
from ypy_websocket import WebsocketProvider
from llama_cpp import Llama
import uuid

ydoc = Y.YDoc()
my_id = uuid.uuid4().hex

todos = ydoc.get_map('todos')
doing = ydoc.get_map('doing')
done = ydoc.get_map('done')



    #ydoc = Y.YDoc()
    # x = ydoc.get_map("test")
    # nested = Y.YMap({"a": "A"})

    # ydoc.transact(lambda txn: x.set(txn, "key", nested))
    # ydoc.transact(lambda txn: nested.set(txn, "b", "B"))

    # assert type(x["key"]) == Y.YMap
    # assert {k : dict(v) for k, v in x.items()} == {"key": {"a": "A", "b": "B"}}

    # print(x["key"].get("b"))
    # ydoc.transact(lambda txn: nested.set(txn, "b", "UPDATED"))
    # res = x["key"].get("b")
    # print(res)

    # ydoc.transact(lambda txn: nested.pop(txn, "b"))
    # print(x["key"].get("b"))

ydoc.transact(lambda txn: doing.set(txn, "b", "B"))


def onTodosChange(e):

        print("-----------------------")
        # doing = ydoc.get_map('doing')
        # with ydoc.begin_transaction() as txn:
        #     todos.set(txn, "inner", "inner_map")

        print("\nTODOS:\n", todos, "\n")
        for id in todos.items():
            task = todos.get(id)
            print(id, "->", task)
            ydoc.transact(lambda txn: todos.pop(txn, id))
        print("\nTODOS:\n", todos, "\n")


        #id=randrange(10)  #uuid.uuid4().hex
        #ydoc.transact(lambda txn: doing.set(txn, "a", "B"))
        #print("\nDOING IN FIRST TODOS:\n", doing, "\n")
        # #loop over todos
        # for e in events:
        #     print("EVENT3", e)
            # print(id, "->", task, "->")
            # todos.pop(id)
            # task.set('asker', my_id)
            # if task.get('worker') is None:
            #     with ydoc.begin_transaction() as t:
            #         task.set('worker', my_id)
            #         doing.set(t, id, task)
            #         todos.pop(t,id)
            #     print (my_id, "is working on", task['text'], task)
            #     # with ydoc.begin_transaction() as t:
            #     #     doing.set(t, id, task)
            #     #     todos.pop(t,id)
            #     #     print("\nTODOS:\n", todos, "\n")
            #     #     print("\nDOING:\n", doing, "\n")
            #     output = llm(
            #         f"Q: {task['text']} A: ",  # Prompt
            #         # max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
            #         # Stop generating just before the model would generate a new question
            #         stop=["Q:", "\n"],
            #         echo=True  # Echo the prompt back in the output
            #     )  # Generate a completion, can also call create_completion

            #     print(output)
            #     output = output.replace("Q: ", "")
            #     task["output"] = output
            #     with ydoc.begin_transaction() as t1:
            #         done.set(t1, id, task)
            #     doing.pop(t1,id)

        # output = llm(
        #     f"Q: {todos[0]} A: ",  # Prompt
        #     # max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
        #     # Stop generating just before the model would generate a new question
        #     stop=["Q:", "\n"],
        #     echo=True  # Echo the prompt back in the output
        # )  # Generate a completion, can also call create_completion
        # print(output)

def onDoingChange(event):

        # doing = ydoc.get_map('doing')
        print("\nDOING:\n", doing, "\n")

def onDoneChange(event):
        print("\nDONE:\n", done, "\n")

todos.observe(onTodosChange)
doing.observe(onDoingChange)
done.observe(onDoneChange)



# llm = Llama(
#     model_path="./models/dolphin-2.2.1-mistral-7b.Q2_K.gguf",
#     # n_gpu_layers=-1, # Uncomment to use GPU acceleration
#     # seed=1337, # Uncomment to set a specific seed
#     # n_ctx=2048, # Uncomment to increase the context window
# )


async def client():





    async with (
        connect("ws://localhost:1234/my-roomname") as websocket,
        WebsocketProvider(ydoc, websocket),
    ):

 

        # with ydoc.begin_transaction() as txn:
        #     yarray.append(txn, "hello de python")

        await asyncio.Future()  # run forever

asyncio.run(client())
