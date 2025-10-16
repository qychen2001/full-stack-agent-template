# API Service

The API package exposes a FastAPI application and reads its
configuration from environment variables (optionally via a `.env`
file).

## Configuration

The following variables control the embedded Uvicorn server:

- `API_HOST`: Bind address for the HTTP server. Default `0.0.0.0`.
- `API_PORT`: Port number exposed by the server. Default `8000`.
- `API_RELOAD`: Enable auto-reload during development. Default `false`.
- `API_LOG_LEVEL`: Logging verbosity for Uvicorn. Default `info`.

Example `.env` configuration:

```
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true
API_LOG_LEVEL=debug
```
