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


const yarray = doc.getArray('my-array')
yarray.observe(event => {
  console.log('yarray was modified')
})
// every time a local or remote client modifies yarray, the observer is called
yarray.insert(0, ['val']) // => "yarray was modified"