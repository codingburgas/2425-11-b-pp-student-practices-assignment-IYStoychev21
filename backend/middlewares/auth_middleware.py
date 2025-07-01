from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from fastapi import Request
from jose import JWTError
from core import security

EXCLUDE_PATHS = {"/api/auth/login", "/api/auth/register", "/docs", "/openapi.json"}

class AuthMiddleware(BaseHTTPMiddleware):
    """
    Authentication middleware for validating JWT tokens.
    
    This middleware intercepts all requests except those in EXCLUDE_PATHS,
    validates the JWT token in the Authorization header, and injects the
    user ID into the request state for use by protected endpoints.
    
    Attributes:
        EXCLUDE_PATHS: Set of paths that don't require authentication
    """
    
    async def dispatch(self, request: Request, call_next):
        """
        Process the request through authentication middleware.
        
        Args:
            request (Request): The incoming HTTP request
            call_next: The next middleware or endpoint to call
            
        Returns:
            Response: The response from the next handler or an error response
        """
        if request.url.path in EXCLUDE_PATHS:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

        token = auth_header.split(" ")[1]
        try:
            request.state.user_id = security.decode_access_token(token)
        except JWTError:
            return JSONResponse(status_code=401, content={"detail": "Invalid token"})

        return await call_next(request)
