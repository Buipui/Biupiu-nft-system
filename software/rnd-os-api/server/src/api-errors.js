export const API_ERRORS=Object.freeze({
 AUTH_REQUIRED:{status:401,code:"AUTH_REQUIRED"},
 FORBIDDEN:{status:403,code:"FORBIDDEN"},
 NOT_FOUND:{status:404,code:"NOT_FOUND"},
 VERSION_CONFLICT:{status:409,code:"VERSION_CONFLICT"},
 VALIDATION:{status:422,code:"VALIDATION_ERROR"},
 INTERNAL:{status:500,code:"INTERNAL_ERROR"}
});
export function apiError(res,error,details={}){
 const e=API_ERRORS[error]||API_ERRORS.INTERNAL;
 return res.writeHead(e.status,{"content-type":"application/json"}),res.end(JSON.stringify({error:e.code,...details}));
}