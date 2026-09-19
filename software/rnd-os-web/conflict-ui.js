export function describeConflict(conflict){
 return {
   title:"Sync conflict requires review",
   message:"The server changed this record after your local version. Choose the server version, keep the local version as a new revision, or create a manual merge.",
   conflict
 };
}
// Deliberately no automatic overwrite policy.