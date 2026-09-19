const KEY="biupiu-rnd-sync-queue-v1";
export function queueOperation(operation){
  const q=JSON.parse(localStorage.getItem(KEY)||"[]");
  q.push({...operation,queued_at:new Date().toISOString()});
  localStorage.setItem(KEY,JSON.stringify(q));
}
export function queuedOperations(){return JSON.parse(localStorage.getItem(KEY)||"[]")}
export function clearQueue(){localStorage.removeItem(KEY)}
// A future authenticated sync worker must submit operations to the API and
// resolve conflicts explicitly; it must never silently overwrite server data.