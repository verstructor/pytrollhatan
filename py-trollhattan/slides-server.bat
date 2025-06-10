@REM This batch file starts a simple HTTP server to serve files 
@REM from the "slides" directory on port 8000.

python -m http.server --directory slides 8000