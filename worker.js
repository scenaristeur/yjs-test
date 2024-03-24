import * as Y from "yjs";
import { WebsocketProvider } from "y-websocket";
import WebSocket from "ws";
const doc = new Y.Doc();

const wsProvider = new WebsocketProvider(
  "ws://localhost:1234",
  "my-roomname",
  doc,
  { WebSocketPolyfill: WebSocket }
);

wsProvider.on("status", (event) => {
  // logs "connected" or "disconnected"
  console.log(event.status);
});

const todos = doc.getMap('todos')
const doing = doc.getMap('doing')
const done = doc.getMap('done')

todos.observe((event) => {
   console.log("todos",todos.toJSON());
})

doing.observe((event) => {
   console.log("doing",doing.toJSON());
})

done.observe((event) => {
   console.log("done",done.toJSON());
})